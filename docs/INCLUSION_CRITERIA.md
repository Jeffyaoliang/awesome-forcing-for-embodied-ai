# Inclusion and editorial policy

This is a **curated** research list, not a comprehensive keyword dump.

## Required for inclusion

1. A real, independently identifiable research paper with a primary DOI/arXiv/publisher URL.
2. A precise technical intervention and a concrete answer to **"what is forced?"**
3. Relevant evaluation or a reasoned transfer connection to robot learning, action-conditioned world models, or long-horizon video.
4. Author/date metadata consistent with the source; prefer first public appearance for the year.
5. Explicitly distinguish an author repository, project page, third-party adaptation and an unverified link.

## Scope tiers

- **core**: robot policy, manipulation/navigation, action-controllable robotic world model, or robot-specific evaluation.
- **transferable**: world/video methods with a documented, plausible transfer mechanism, even if no robot success metric.
- **adjacent**: systems, video throughput, memory/cache methods; keep them visible but below the core list.

Classification is an editorial judgment and can change when new experiments appear.

## Exclude or postpone

- Title-only "Forcing" matches without a concrete mechanism.
- Duplicate papers, renamings, benchmark-only marketing, unrelated physical forcing terminology.
- Entries supported solely by a company/blog post without a traceable research paper.
- Unverified new discoveries: put these in `data/discovered-candidates.md` until reviewed.

## Source/release evidence

- `reviewed` means primary-paper identity and mechanism were checked, **not** that claims were reproduced.
- A paper's promise to release code is not code availability.
- A third-party adaptation cannot be presented as the official author's implementation.
- Checkpoints, train scripts, infer scripts, evaluation code and executable reproduction are independent attributes.
- Keep uncertain states and dated evidence rather than assigning a false yes/no.

## Quality bar for PRs

Provide the primary citation, one-sentence contribution, mechanism category and tier justification. When changing code-release status, supply an author-affiliated repository or project evidence. Keep README, `data/papers.csv` and `data/release-audit.csv` aligned and pass `python scripts/validate.py`.

Editorial disagreements are welcome when accompanied by primary-source evidence.
