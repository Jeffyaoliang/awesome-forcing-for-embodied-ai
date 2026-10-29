# AI-assisted paper curation: 8-paper pilot

**Status:** pipeline scaffold, not completed model reviews. No AI judgments have been generated or validated. Do not treat reviewer output as peer review or automatic acceptance.

## Goal

Compare a specialized open reviewer (e.g. OpenReviewer 8B), an evidence-oriented agent reviewer, and a human-verified reference set for the eight Starter Kit papers.

## Workflow

1. Download full paper text legally from authors/arXiv using a reproducible extraction process; record PDF revision and SHA-256, plus exact page/section.
2. Generate a draft review with structured, source-linked claims. Require citations to the actual paper. Classify each claim as supported, contradicted or unverified based on human checks.
3. Separately label **research quality** (soundness, novelty context, experimental validity, reproducibility) and **curation fit** (forcing mechanism, robot relevance, representative value).
4. Human reviewer checks at least three substantive critique claims per paper, including potential false positives.
5. Compute precision of substantiated criticisms, evidence traceability, human agreement, runtime/cost, and abstention. Never rank papers by a single aggregate score.

## Security and reproducibility

Do not execute code, shell commands or instructions copied from papers. Treat text downloaded from the internet as untrusted. Use a fixed prompt, pinned model version, temperature, paper hashes and an explicit output schema. Never commit API keys or copyrighted full-text PDFs to the repository.

## Baselines and licenses

- [OpenReviewer](https://github.com/maxidl/openreviewer)
- [CMU Paper Reviewer](https://github.com/prometheus-eval/cmu-paper-reviewer)
- [ReviewEval](https://github.com/madhavkrishangarg/ReviewEval)

These links are research references, **not** proof of installability or license compatibility. Verify weights, code release and licenses before adopting a particular model.

## Outcomes

- `data/reviewer-pilot.csv`: 8 paper records, deliberately unreviewed.
- `reviews/schema.json`: validated output structure.
- `scripts/validate_reviews.py`: offline guardrails, not LLM inference.
- Generated reviews should be proposed in a PR for human approval; no automatic rejection, admission or merge.
