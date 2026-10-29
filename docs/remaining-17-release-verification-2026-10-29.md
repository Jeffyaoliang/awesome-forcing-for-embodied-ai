# Follow-up primary-source release verification — 2026-10-29

Scope: the 17 entries that were still ambiguous after the earlier inventory audit. Every entry received a source/evidence classification in [release-audit.csv](../data/release-audit.csv). **Some remain unconfirmed**. This is not runtime verification.

## Confirmed public implementations, or partial implementation

| Work | Evidence | Important limitation |
|---|---|---|
| Diffusion Forcing | [Official repo](https://github.com/buoyancy99/diffusion-forcing): v1.5 implementation, original paper branch | No independent run |
| Next Forcing | [Official repo](https://github.com/robbyant-research/next-forcing): training, zero-overhead inference, two model checkpoints and RoboTwin evaluation | **2× MCP-accelerated inference mode is expressly not in the released code** |
| Discrete Forcing | [XPolicyLab adapter](https://github.com/XPolicyLab/XPolicyLab/blob/main/policy/Discrete_Forcing/README.md) offers training/evaluation adapters | Integration is not proof of upstream release; original source not independently checked |

## Official project page/repository, but code not confirmed or explicitly forthcoming

| Work | Best evidence | Reading |
|---|---|---|
| Self-Forcing++ | [Author repo](https://github.com/justincui03/Self-Forcing-Plus-Plus) | README + assets; explicitly promises future code |
| Memory Forcing (Minecraft) | [Author page](https://junchao-cs.github.io/MemoryForcing-demo/) and [author profile](https://junchao-cs.github.io/) | Author profile says code coming soon; repository name alone is not release proof |
| Pack and Force Your Memory | [Author project](https://wuxiaofei01.github.io/PFVG/) | Project includes a code link; target implementation not audited |
| Head Forcing | [Project link from paper](https://jiahaotian-sjtu.github.io/headforcing.github.io/) | Code state not verified |
| Self-Aligned Forcing | [Paper-linked anonymous page](https://anonymous.4open.science/w/self-aligned-forcing/) | Runtime implementation not verified |
| Step Forcing / RoboWorld | [Author project](https://byeongguks.github.io/RoboWorld/) | Demo and paper; release not confirmed |

## No trustworthy official code release established in this pass

Relational Geometry Forcing; WorldSync / Action-Forcing Expert; Language-Forcing; Future Forcing; Recency Forcing; Action Forcing. **Not established is not the same as definitively closed source.**

## Paper explicitly promises release

- [AR Forcing](https://arxiv.org/abs/2605.31314) — abstract says code will be released soon.
- [Focused Forcing](https://arxiv.org/abs/2605.18346) — abstract says code will be released on GitHub.

## Consistency corrections

1. A project's methods paper, the author's demo page, a downstream adapter, and an executable upstream source release are separate evidence levels.
2. Next Forcing's RoboTwin checkpoint + baseline inference and evaluation code are public, but its advertised accelerated inference variant is not.
3. Memory Forcing's code status should not be inferred solely from an empty or placeholder repository.
4. All 33 entries remain `execution_checked=no`: no downloads, package installation, GPU execution, or independent metric reproduction happened.

**Next validation:** do git tree-level inspection, check checkpoint revision/size/license, run import tests, then reproduce one short evaluation under the published protocol.
