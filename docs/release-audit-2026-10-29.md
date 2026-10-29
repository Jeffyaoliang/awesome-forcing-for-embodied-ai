# Forcing release and reproducibility audit — 2026-10-29

This is an **availability audit**, not a successful reproduction. Public README/entrypoint evidence only; no weight download, dependency installation, GPU run, or numerical replication was performed.

## Audited projects

| Project | Training | Inference | Weights | Evaluation | Source |
|---|---|---|---|---|---|
| PhysisForcing | Released (Wan/Cosmos) | Released | Author-announced | Paper benchmark results; full reproducibility TBD | [Official](https://github.com/DAGroup-PKU/PhysisForcing) |
| Fréchet Forcing | Released | Released | DROID checkpoint advertised; Sekai coming soon | Long-horizon evaluation scripts available | [Official](https://github.com/Zhao-Yian/Frechet_Forcing) |
| Rolling Forcing | Released (8-GPU recipe) | Released | External ODE/teacher/base weights described | Not fully checked | [Official](https://github.com/TencentARC/RollingForcing) |
| Pyramid Forcing | Training-free method | Released | Requires external Self-Forcing checkpoint | Self-Forcing baseline config and tests | [Official](https://github.com/IF-LAB-PKU/Pyramid-Forcing) |
| Speculative Forcing | Not released | Not released | Unconfirmed | Not released | [Official](https://github.com/naver-ai/speculative-forcing) |

## Important caveats

- Fréchet Forcing offers a DROID Hugging Face checkpoint download command. Sekai model checkpoint is explicitly marked `Coming soon`. Base checkpoints and data may be additional dependencies.
- PhysisForcing claims it released both training/inference bundles on 2026-09-07 and 2026-07-08, respectively. The release is supported by a maintainer response on issue #8, but auxiliary teacher checkpoints and setup should be audited separately.
- Rolling Forcing reports a single-node eight-GPU training recipe and downloads from Self-Forcing/Wan dependencies.
- Pyramid Forcing is a **training-free** cache mechanism: treating it as missing training code is wrong. It supplies `inference.py`, `configs/self-forcing.yaml`, and head-aware config. Officially tested on H200 with >=48 GB memory.
- Speculative Forcing's GitHub repository currently hosts README only; code marked *under internal review*.
- An accessible repository is not proof that released checkpoint links resolve or that output matches paper metrics.

## Follow-up checks

1. Verify exact GitHub paths and downloadable checkpoint metadata for other papers.
2. Run dependency/container smoke tests on a suitable GPU.
3. Preserve model/backbone/data/compute differences before comparing outcomes.
4. Record dataset access conditions, evaluation scripts, and seed variance.

Full inventory: [data/release-audit.csv](../data/release-audit.csv).
