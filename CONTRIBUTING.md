# Contributing to Awesome Forcing for Embodied AI

We welcome paper suggestions, metadata corrections and independently reproducible experiments.

## Inclusion standards

1. Identify a **specific technical intervention** (training conditions, history distributions, geometry/action/language supervision, memory, sampling or cache control). A paper's title alone is not enough.
2. Supply a **primary paper URL** (arXiv / DOI / publisher), the year of first public appearance and a concise explanation of what is forced.
3. Separate **official author code**, **third-party implementations**, **project pages** and **unreleased announcements**. A GitHub README containing only a code-release promise is *not* a release.
4. Distinguish released **training scripts**, **inference scripts**, **checkpoints** and **evaluation scripts** in [release-audit.csv](data/release-audit.csv). Leave unknown evidence unknown.
5. For adaptations and forks, link the original paper and identify the downstream implementation clearly.
6. Do not claim successful reproduction without execution logs, environment configuration and a benchmark protocol.

## Verification labels

- `candidate`: surfaced in discovery, paper identity not independently checked.
- `reviewed`: primary paper and mechanism identity checked. This does **not** certify public code, weights or execution.
- `executed`: contributors ran the cited implementation with reproducible setup.
- `reproduced`: cited metric recreated with protocol, environment and repeatability evidence.

Release states are independently maintained in [release-audit.csv](data/release-audit.csv) and should not be inferred from `verification=reviewed`.

## Submission procedure

Open a paper suggestion issue or pull request. Update `data/papers.csv`, `data/release-audit.csv` and the matching README row. If classification is debatable, explain your primary intervention choice.

Run `python scripts/validate.py` before submitting. The check is **offline**: it verifies structure, duplicate IDs and README coverage but cannot certify external URL reachability or the claims in papers.

## Maintenance principles

- Prefer a useful, readable Awesome List over long audit narratives in the README.
- Preserve uncertainty and date sources where release availability may change.
- Avoid duplicate entries for renamings or incremental versions; separate true method-level contributions.
- Do not merge unreviewed entries automatically from arXiv discovery.
