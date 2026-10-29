# Awesome Forcing for Embodied AI

A **mechanism-first curated index** of Forcing methods in embodied AI, world/action models, robotics, and adjacent video generation.

> **v0.2 / work in progress.** The [machine-readable index](data/papers.csv) contains 33 entries: **25 reviewed against primary paper/project sources**, **2 pending initial-paper checks**, and **6 secondary-source-only entries**. Reviewed means bibliographic/method verification, not code execution. This is not a benchmark leaderboard.

## Why this list?

"Forcing" is not one unified algorithm. We classify **what is forced and where the intervention enters** rather than grouping papers merely by name.

## Mechanism taxonomy

| Family | Intervention | Example |
|---|---|---|
| Temporal / noise forcing | Per-position diffusion/noise schedules | Diffusion Forcing |
| Rollout / distribution forcing | Self-generated history and rollout alignment | Fréchet Forcing |
| Physical / structural supervision | Geometry, motion and consistency constraints | PhysisForcing |
| Action conditioning | Action adherence in predicted dynamics | WorldSync |
| Action representation | Discrete guidance for continuous control | Discrete Forcing |
| Semantic supervision | Language as training signal | Language-Forcing |
| Future prediction | Multi-horizon / multi-chunk objective | Next Forcing |

## Selected papers

| Paper | Primary source | Implementation | Verification |
|---|---|---|---|
| Diffusion Forcing (2024) | [arXiv](https://arxiv.org/abs/2407.01392) | [Project](https://boyuan.space/diffusion-forcing) | reviewed |
| PhysisForcing (2026) | [arXiv](https://arxiv.org/abs/2606.28128) | [GitHub](https://github.com/DAGroup-PKU/PhysisForcing) | reviewed |
| Fréchet Forcing (2026) | [arXiv](https://arxiv.org/abs/2610.25666) | [GitHub](https://github.com/Zhao-Yian/Frechet_Forcing) | reviewed |
| Relational Geometry Forcing (2026) | [arXiv](https://arxiv.org/abs/2610.29282) | not confirmed | pending |
| WorldSync / Action-Forcing (2026) | [arXiv](https://arxiv.org/abs/2608.24885) | not confirmed | pending |
| Discrete Forcing (2026) | [arXiv](https://arxiv.org/abs/2609.39526) | not confirmed | pending |
| Language-Forcing (2026) | [arXiv](https://arxiv.org/abs/2610.23894) | not confirmed | pending |
| Next Forcing (2026) | [arXiv](https://arxiv.org/abs/2606.11187) | not confirmed | pending |

## Automatic discovery

The [weekly GitHub Action](.github/workflows/discover.yml) queries arXiv and proposes changes to [unreviewed candidates](data/discovered-candidates.md) in a pull request. Human review is required before adding verified entries to the index.

## Release & reproducibility audit

- [Code/weights/evaluation availability inventory (33 entries)](data/release-audit.csv)
- [Official repository audit (2026-10-29)](docs/release-audit-2026-10-29.md)

## Reproducibility

The [preliminary audit](docs/audit.md) separates public source announcements from actual execution and independent replication. **No reported metric has yet been independently reproduced by this project.**

## Research questions

- Which forcing interventions address exposure bias, physical consistency, or control adherence?
- Which results are confounded by backbone, dataset, additional supervision or compute?
- Could closed-loop robot failure diagnoses drive adaptive selection of forcing mechanisms?

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the paper submission issue template. Missing URLs are intentionally left blank rather than guessed. See the [verification ledger](docs/verification-2026-10-29.md) for evidence levels and unresolved entries.

## Related resources

- [Awesome-Video-Forcing](https://github.com/Tammytcl/Awesome-Video-Forcing)
- [Awesome-World-Action-Models](https://github.com/RCL-Robotics/Awesome-World-Action-Models)
- [Awesome-Video-World-Models](https://github.com/hit-perfect/Awesome-Video-World-Models)

## License

[MIT License](LICENSE) for this repository's original material. Linked research and third-party code retain their own licenses.
