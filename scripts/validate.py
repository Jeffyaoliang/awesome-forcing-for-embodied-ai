#!/usr/bin/env python3
"""Offline consistency checks; no network dependency."""
import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
def read_csv(path):
    with (ROOT / path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)
fields, papers = read_csv("data/papers.csv")
release_fields, releases = read_csv("data/release-audit.csv")
errors = []
required = {"title", "year", "paper_url", "code_url", "mechanism_family", "verification", "embodied_relevance"}
errors.extend("Missing column: " + c for c in required - set(fields))
release_index = {r.get("title", "").casefold(): r for r in releases}
seen_titles, seen_ids = set(), set()
for n, row in enumerate(papers, 2):
    title = row.get("title", "").strip()
    name = title.casefold()
    if not title or name in seen_titles:
        errors.append(f"Line {n}: missing or duplicate title {title!r}")
    seen_titles.add(name)
    if not re.fullmatch(r"20[0-9]{2}", row.get("year", "")):
        errors.append(f"{title}: invalid year")
    if row.get("embodied_relevance") not in {"core", "transferable", "adjacent"}:
        errors.append(f"{title}: invalid embodied_relevance")
    if not row.get("mechanism_family") or not row.get("verification"):
        errors.append(f"{title}: missing classification/verification")
    if not row.get("paper_url"):
        errors.append(f"{title}: missing primary-paper URL")
    for key in ("paper_url", "code_url"):
        value = row.get(key, "")
        if value:
            parsed = urlparse(value)
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{title}: invalid {key} URL")
    match = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", row.get("paper_url", ""))
    if match:
        identifier = match.group(1)
        if identifier in seen_ids:
            errors.append(f"{title}: duplicate arXiv ID {identifier}")
        seen_ids.add(identifier)
    if name not in release_index:
        errors.append(f"{title}: missing release-audit record")
for row in releases:
    if row.get("title", "").casefold() not in seen_titles:
        errors.append(f"Orphan release audit: {row.get('title')}")
if len(releases) != len(release_index):
    errors.append("Duplicate release-audit title")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
table_titles = []
for line in readme.splitlines():
    m = re.match(r"^\|\s*20\d{2}\s*\|\s*([^|]+)\s*\|", line)
    if m:
        table_titles.append(m.group(1).strip())
if len(table_titles) != len(papers) or set(table_titles) != {p["title"] for p in papers}:
    errors.append(f"README table differs from CSV: {len(table_titles)} listed / {len(papers)} indexed")
print(f"Validated {len(papers)} paper rows, {len(releases)} release rows, {len(table_titles)} README entries")
if errors:
    for e in errors:
        print("ERROR:", e, file=sys.stderr)
    sys.exit(1)
print("PASS")
