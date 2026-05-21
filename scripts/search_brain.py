#!/usr/bin/env python3
"""Small lexical search helper for the second-brain vault.

Usage:
  python3 scripts/search_brain.py "axianews scoring"

Returns compact ranked snippets from wiki/, docs/, and raw/.
"""
from __future__ import annotations
import re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SEARCH_DIRS=[ROOT/'wiki', ROOT/'docs', ROOT/'raw']
MAX_RESULTS=20

def terms(q:str):
    return [t.lower() for t in re.findall(r"[\wÀ-ÿ.-]+", q) if len(t)>1]

def score(text:str, ts:list[str]):
    low=text.lower()
    return sum(low.count(t) for t in ts)

def snippets(text:str, ts:list[str], n=2):
    lines=text.splitlines()
    out=[]
    for i,line in enumerate(lines,1):
        low=line.lower()
        if any(t in low for t in ts):
            out.append(f"L{i}: {line.strip()[:240]}")
            if len(out)>=n: break
    return out

def title(text:str, path:Path):
    m=re.search(r"^title:\s*(.+)$", text, re.M)
    if m: return m.group(1).strip()
    m=re.search(r"^#\s+(.+)$", text, re.M)
    if m: return m.group(1).strip()
    return path.stem

def main():
    q=' '.join(sys.argv[1:]).strip()
    if not q:
        print('Usage: search_brain.py "query"', file=sys.stderr); return 2
    ts=terms(q)
    results=[]
    for d in SEARCH_DIRS:
        if not d.exists(): continue
        for p in d.rglob('*.md'):
            try: text=p.read_text(encoding='utf-8', errors='replace')
            except Exception: continue
            s=score(text, ts)
            if s>0:
                results.append((s,p,text))
    results.sort(key=lambda x:(-x[0], str(x[1])))
    print(f"Query: {q}")
    print(f"Results: {len(results)} total, showing {min(MAX_RESULTS,len(results))}\n")
    for s,p,text in results[:MAX_RESULTS]:
        rel=p.relative_to(ROOT)
        print(f"## {rel}  score={s}")
        print(f"Title: {title(text,p)}")
        for sn in snippets(text, ts): print(sn)
        print()
    return 0
if __name__=='__main__': raise SystemExit(main())
