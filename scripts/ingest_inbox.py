#!/usr/bin/env python3
"""Prepare files dropped in inbox/ for LLM Wiki ingestion.

This script does technical ingestion only:
- PDF -> markdown text using pdftotext
- TXT/MD -> normalized markdown copy
- add raw frontmatter with sha256
- move originals to inbox/processed/

It does NOT perform LLM synthesis. After running it, an agent must read the raw
files and update wiki/ pages, index.md, and log.md.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "inbox"
PROCESSED = INBOX / "processed"
RAW_PAPERS = ROOT / "raw" / "papers"
RAW_TEXTS = ROOT / "raw" / "texts"

SUPPORTED = {".pdf", ".txt", ".md", ".markdown"}


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "source"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suffix = path.stem, path.suffix
    i = 2
    while True:
        candidate = path.with_name(f"{stem}-{i}{suffix}")
        if not candidate.exists():
            return candidate
        i += 1


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def pdf_to_text(path: Path) -> str:
    if not shutil.which("pdftotext"):
        raise RuntimeError("pdftotext is required for PDF ingestion. Install poppler-utils.")
    proc = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return proc.stdout.strip()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").strip()


def frontmatter(title: str, source_type: str, source_file: str, body: str) -> str:
    return (
        "---\n"
        f"title: {title}\n"
        f"source_type: {source_type}\n"
        f"source_file: {source_file}\n"
        "source_url: \n"
        f"ingested: {date.today().isoformat()}\n"
        f"sha256: {sha256_text(body)}\n"
        "status: raw\n"
        "---\n\n"
    )


def process_file(path: Path) -> Path | None:
    ext = path.suffix.lower()
    if ext not in SUPPORTED:
        return None
    if path.is_dir():
        return None

    title = path.stem.replace("-", " ").replace("_", " ").strip().title()
    slug = slugify(path.stem)

    if ext == ".pdf":
        body = pdf_to_text(path)
        source_type = "pdf"
        out_dir = RAW_PAPERS
    elif ext in {".md", ".markdown"}:
        body = read_text(path)
        source_type = "markdown"
        out_dir = RAW_TEXTS
    else:
        body = read_text(path)
        source_type = "text"
        out_dir = RAW_TEXTS

    if not body:
        raise RuntimeError(f"No text extracted from {path}")

    out_dir.mkdir(parents=True, exist_ok=True)
    out = unique_path(out_dir / f"{slug}.md")
    out.write_text(frontmatter(title, source_type, path.name, body) + f"# {title}\n\n" + body + "\n", encoding="utf-8")

    PROCESSED.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(unique_path(PROCESSED / path.name)))
    return out


def main() -> int:
    INBOX.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    errors: list[str] = []

    for path in sorted(INBOX.iterdir()):
        if path.name.startswith(".") or path.name == "processed":
            continue
        try:
            out = process_file(path)
            if out:
                created.append(out)
        except Exception as e:
            errors.append(f"{path}: {e}")

    if created:
        print("Created raw sources:")
        for p in created:
            print(f"- {p.relative_to(ROOT)}")
    else:
        print("No supported files found in inbox/.")

    if errors:
        print("\nErrors:", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
