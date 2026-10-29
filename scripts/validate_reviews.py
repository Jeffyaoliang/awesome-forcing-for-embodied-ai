#!/usr/bin/env python3
"""Validate review pilot manifests and JSON reviews. Never runs models."""
import csv
import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parents[1]
errors = []
with (root / "data/reviewer-pilot.csv").open(newline="",encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
if len(rows)!=8 or len({r["paper_id"] for r in rows})!=8:
    errors.append("Pilot manifest must contain 8 unique papers")
ids={r["paper_id"] for r in rows}
for r in rows:
    if r["status"] not in {"not_started","draft_generated","human_reviewed"}:
        errors.append("Invalid pilot status")
    if r["status"]=="not_started" and (r["review_path"] or r["human_verified"]!="no"):
        errors.append("Do not assign a review or human verification before reviewing")
for path in (root/"reviews").glob("*.json"):
    if path.name=="schema.json":continue
    try:
        obj=json.loads(path.read_text(encoding="utf-8"))
        for key in ("paper_id","model_id","paper_sha256","research_quality","curation_value","claims","recommendation","human_verified"):
            if key not in obj:errors.append(f"{path}: missing {key}")
        if obj.get("paper_id") not in ids:errors.append(f"{path}: unknown paper")
        if not re.fullmatch(r"[a-fA-F0-9]{64}",obj.get("paper_sha256","")):errors.append(f"{path}: invalid PDF hash")
        if obj.get("recommendation") not in {"include","include_with_caveats","defer","exclude","abstain"}:errors.append(f"{path}: invalid recommendation")
        if obj.get("human_verified") is not False:errors.append(f"{path}: must be independently human verified")
        for claim in obj.get("claims",[]):
            if not claim.get("source_location"):errors.append(f"{path}: citation location missing")
    except (ValueError,TypeError) as e: errors.append(f"{path}: invalid JSON {e}")
print(f"Pilot: {len(rows)} papers; reviewed JSON files: {len([p for p in (root/'reviews').glob('*.json') if p.name!='schema.json'])}")
for e in errors:print("ERROR:",e,file=sys.stderr)
if errors:sys.exit(1)
print("PASS: no fabricated review results")
