# Forcing bibliography verification — 2026-10-29

**Scope:** 33 rows in `data/papers.csv`. Verification refers to checking research identity and core mechanism, **not** reproducing code.

## Evidence summary

- **25 primary-reviewed**: 19 of 25 added candidate entries plus 6 of the original 8.
- **6 secondary-listed**: a curated community index mentions them, but the present pass did not independently confirm exact primary URLs and paper-level mechanism.
- **2 pending**: Discrete Forcing; Language-Forcing. Their original arXiv links are retained pending a complete primary-page check.

## Newly primary-reviewed (19)

Self Forcing; Self-Forcing++; Rolling Forcing; Reward Forcing; Memory Forcing (2025 Minecraft); Deep Forcing (ICML 2026); Causal Forcing; Head Forcing; Forcing-KV; Future Forcing; Focused Forcing; Pyramid Forcing; Recency Forcing; Self-Aligned Forcing; AR Forcing; Step Forcing (RoboWorld); Action Forcing; RECAP-Forcing; Speculative Forcing.

Primary URLs are stored in `data/papers.csv`.

## Remaining secondary-only (6)

- Geometry Forcing
- Pack and Force Your Memory
- Causal Forcing++
- Delta Forcing
- Neighbor Forcing (SoulX-LiveAct)
- Steady-Forcing

These titles were encountered in community research indexes, but have not yet passed the direct-paper verification standard in this repository. **Do not cite these as primary-verified.**

## Corrections

1. **Deep Forcing** was previously entered as 2025; the confirmed ICML proceedings publication is **2026**.
2. **Memory Forcing** is ambiguous: the curated 2025 Minecraft paper (arXiv:2510.03198) differs from a 2026 streaming video paper with the same leading title (arXiv:2610.11756). They should become separate entries if both are included.
3. **Speculative Forcing** has an official repository README, but that README says code is **under internal review**; a code-repository URL must not be equated with a released implementation.
4. **WorldSync** is the method name within the paper *Do Robotic World Models Really Follow Actions?*, not the paper title itself.

## Interpretation limits

- Code links may lead to documentation-only repositories or partial releases.
- Numerical gains in abstracts are **author reported**.
- No independent execution, checkpoint loading or standardized benchmark reproduction was carried out during this bibliography pass.
