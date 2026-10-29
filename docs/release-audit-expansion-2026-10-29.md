# Release audit expansion — 2026-10-29

All **28 formerly unexamined entries** in [release-audit.csv](../data/release-audit.csv) now have individual review outcomes. This closes the *inventory pass*, **not** an execution/reproduction audit. The full table includes the five already audited entries, giving 33 rows.

## High-confidence official release evidence

| Method | Training | Inference | Weights / evaluation | Official source |
|---|---|---|---|---|
| Geometry Forcing | repository code | repository code | checkpoint 2025-09-24; eval code 2025-10-08 | [repo](https://github.com/CIntellifusion/GeometryForcing) |
| Reward Forcing | released | released | 1.3B advertised; 14B in progress | [repo](https://github.com/JaydenLyh/Reward-Forcing) |
| Deep Forcing | not required | released | depends on base model | [repo](https://github.com/cvlab-kaist/DeepForcing) |
| Causal Forcing / ++ | released | released | multiple Hugging Face checkpoints announced | [repo](https://github.com/thu-ml/Causal-Forcing) |
| Delta Forcing | released | released | checkpoint and detailed evaluation/ablation protocol announced | [repo](https://github.com/wyhallenwu/DeltaForcing) |
| Forcing-KV | not required | released | VBench/Helios evaluation; external backbones | [repo](https://github.com/zju-jiyicheng/Forcing-KV) |
| RECAP-Forcing | not required | released | external Self-Forcing backbone; benchmark result descriptions | [repo](https://github.com/xXuHaiyang/RECAP-Forcing) |
| Neighbor Forcing | **not yet released** | released | model weights released; demo | [repo](https://github.com/Soul-AILab/SoulX-LiveAct) |
| Steady-Forcing | train.sh and recipe | repository implementation | model weights and eval scripts not separately verified | [repo](https://github.com/minar09/steady-forcing) |
| Self Forcing | repository available | repository available | checkpoint specifics not separately audited | [repo](https://github.com/guandeh17/Self-Forcing) |

## Items for which release is NOT CONFIRMED

Diffusion Forcing; Relational Geometry Forcing; WorldSync; Discrete Forcing; Language-Forcing; Next Forcing; Self-Forcing++; Memory Forcing; Pack and Force Your Memory; Head Forcing; Future Forcing; Focused Forcing; Recency Forcing; Self-Aligned Forcing; AR Forcing; Step Forcing; Action Forcing.

**“Not confirmed” does not mean no code exists**. It means this pass did not find sufficient primary-source evidence to label a release as available. These are a queue for later deeper code-path inspection. AR Forcing's abstract says code is forthcoming.

## Previously audited five

PhysisForcing, Fréchet Forcing, Rolling Forcing, Pyramid Forcing, and Speculative Forcing retain their earlier availability assessments; see [original release audit](release-audit-2026-10-29.md).

## Known metadata issues

- Geometry Forcing was previously a secondary-only candidate; official repository confirms code, checkpoint and evaluation release.
- Causal Forcing++ is a distinct paper but shares an implementation repository with Causal Forcing.
- Neighbor Forcing is the technique in SoulX-LiveAct, not an independently named repository; training release remains unchecked on the official release plan.
- Memory Forcing is an ambiguous title across different projects.
- Speculative Forcing's public repository does not imply its source code is public.

## Audit limits

No network checkpoint download, no `pip install`, no CUDA execution, no test suite execution, and no independent metric replication were performed. `release-audit.csv` intentionally preserves unknown evidence rather than manufacturing completeness.
