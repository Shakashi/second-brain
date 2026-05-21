#!/usr/bin/env python3
"""Fast sanity lint for the second-brain vault."""
from __future__ import annotations
import re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WIKI=ROOT/'wiki'
INDEX=WIKI/'index.md'
SCHEMA=WIKI/'SCHEMA.md'
errors=[]
warnings=[]
mds=[p for p in WIKI.rglob('*.md') if p.name not in {'index.md','log.md','SCHEMA.md'}]
idx=INDEX.read_text(errors='replace') if INDEX.exists() else ''
slugs={p.stem for p in mds}
# Extract taxonomy tags
schema=SCHEMA.read_text(errors='replace') if SCHEMA.exists() else ''
tax=set()
for line in schema.splitlines():
    m=re.match(r"-\s+([a-z0-9-]+)\s*$", line.strip())
    if m: tax.add(m.group(1))
for p in mds:
    txt=p.read_text(errors='replace')
    if not txt.startswith('---\n'):
        errors.append(f'missing frontmatter: {p.relative_to(ROOT)}'); continue
    parts=txt.split('---',2)
    if len(parts)<3:
        errors.append(f'bad frontmatter: {p.relative_to(ROOT)}'); continue
    fm=parts[1]
    for field in ['title:','created:','updated:','type:','tags:','sources:','confidence:','contested:']:
        if field not in fm: errors.append(f'missing {field} {p.relative_to(ROOT)}')
    if p.stem not in idx: warnings.append(f'not in index: {p.relative_to(ROOT)}')
    mt=re.search(r'tags:\s*\[([^\]]*)\]', fm)
    if mt and tax:
        tags=[t.strip().strip('"\'') for t in mt.group(1).split(',') if t.strip()]
        for t in tags:
            if t not in tax: warnings.append(f'tag not in taxonomy: {t} in {p.relative_to(ROOT)}')
    for target in re.findall(r'\[\[([^\]|#]+)', txt):
        slug=re.sub(r'[^a-z0-9]+','-',target.lower()).strip('-')
        if slug not in slugs and target not in slugs:
            warnings.append(f'possible broken link [[{target}]] in {p.relative_to(ROOT)}')
print(f'Pages checked: {len(mds)}')
if errors:
    print('\nERRORS:'); [print('-',e) for e in errors]
if warnings:
    print('\nWARNINGS:'); [print('-',w) for w in warnings[:100]]
if not errors and not warnings: print('OK')
returncode=1 if errors else 0
raise SystemExit(returncode)
