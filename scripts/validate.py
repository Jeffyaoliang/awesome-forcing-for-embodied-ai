#!/usr/bin/env python3
"""Local, offline checks for the curated Forcing paper index."""
import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
paper_path = root / "data" / "papers.csv"
release_path = root / "data" / "release-audit.csv"
required = {"title", "year", "paper_url", "code_url", "mechanism_family", "verification"}
errors = []
with paper_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fields = set(reader.fieldnames or [])
    if missing := required - fields:
        errors.append(f"Missing paper columns: {sorted(missing)}")
    papers = list(reader)
seen_titles = {}
seen_papers = {}
def check_url(label, value):
    if value and (urlparse(value).scheme not in {"https", "http"} or not urlparse(value).netloc):
        errors.append(f"Invalid URL for {label}: {value}")
for idx, p in enumerate(papers, start=2):
    name = p.get("title", "").strip()
    if not name:
        errors.append(f"Row {idx}: missing title")
        continue
    key = name.casefold()
    if key in seen_titles:
        errors.append(f"Duplicate title rows {seen_titles[key]} and {idx}: {name}")
    seen_titles[key] = idx
    for col in ("paper_url", "code_url"):
        check_url(f"{name}.{col}", p.get(col, ""))
    url = p.get("paper_url", "")
    m = re.search(r"arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})", url)
    if m:
        identifier = m.group(1)
        if identifier in seen_papers:
            errors.append(f"Duplicate arXiv ID: {identifier}")
        seen_papers[identifier] = idx
    if not p.get("verification"):
        errors.append(f"Row {idx}: missing verification")
with release_path.open(encoding="utf-8", newline="") as f:
    releases = list(csv.DictReader(f))
release_names = [p.get("title", "") for p in releases]
for name in seen_titles:
    if not any(n.casefold() == name for n in release_names):
        errors.append(f"Missing audit row: {name}")
if len(release_names) != len(set(x.casefold() for x in release_names)):
    errors.append("Duplicate titles in release-audit.csv")
for p in releases:
    check_url(f"{p.get('title')}.source_url", p.get("source_url", ""))
print(f"Checked {len(papers)} papers, {len(releases)} release-audit records")
if errors:
    print("\n".join("ERROR: " + x for x in errors), file=sys.stderr)
    sys.exit(1)
print("PASS: CSV structure, unique titles/arXiv IDs, URL format, release-audit coverage")
