#!/usr/bin/env python3
"""Discover arXiv candidate papers. Does not auto-validate entries."""
import csv
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path(__file__).resolve().parents[1]
query = 'ti:"Forcing" AND (all:"video" OR all:"robot" OR all:"world model" OR all:"diffusion")'
params = urllib.parse.urlencode({"search_query": query, "start": 0, "max_results": 100,
                                 "sortBy": "submittedDate", "sortOrder": "descending"})
request = urllib.request.Request("https://export.arxiv.org/api/query?" + params,
                                 headers={"User-Agent": "AwesomeForcingEmbodiedAI/0.2"})
with urllib.request.urlopen(request, timeout=35) as response:
    atom = ET.fromstring(response.read())
ns = {"a": "http://www.w3.org/2005/Atom"}
with (root / "data" / "papers.csv").open(encoding="utf-8") as f:
    papers = list(csv.DictReader(f))
seen_ids = {p["paper_url"].split("/")[-1] for p in papers if p["paper_url"]}
seen_titles = {p["title"].lower().strip() for p in papers}
items = []
for entry in atom.findall("a:entry", ns):
    title = " ".join(entry.findtext("a:title", "", ns).split())
    url = entry.findtext("a:id", "", ns)
    arxiv_id = re.sub(r"v[0-9]+$", "", url.split("/")[-1])
    if arxiv_id in seen_ids or title.lower() in seen_titles:
        continue
    date = entry.findtext("a:published", "", ns)[:10]
    items.append(f"- {date} · [{title}](https://arxiv.org/abs/{arxiv_id})")
header = ["# Unreviewed Forcing paper candidates", "",
          "Automatically discovered, **not verified or endorsed**.", "", f"Query: `{query}`", ""]
(root / "data" / "discovered-candidates.md").write_text(
    "\n".join(header + (items or ["No new results in the latest 100 hits."])) + "\n",
    encoding="utf-8")
print(f"{len(items)} candidates")
