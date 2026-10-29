# Six unresolved Forcing methods: official code-release check (2026-10-29)

**Scope:** original paper identities, official software, downloadable model weights, and evaluation code. **Finding:** no author-attributable official implementation or checkpoint was established for any of the six below from targeted public searches on the audit date. This does **not** prove the code is private, and does not preclude newer or unindexed releases.

| Method | Primary paper | What could be verified | Official implementation | Checkpoints | Evaluation code |
|---|---|---|---|---|---|
| Relational Geometry Forcing | [2610.29282](https://arxiv.org/abs/2610.29282) | WAM training-only relational geometry supervision | Not located | Not located | Not located |
| WorldSync / Action-Forcing Expert | [2608.24885](https://arxiv.org/abs/2608.24885) | WorldEcho evaluation and WorldSync action-following approach, revised Oct 23 | Not located | Not located | Not located |
| Language-Forcing | [2610.23894](https://arxiv.org/abs/2610.23894) | Whole-body WAM semantic supervision and HumanoidArena evaluations | Not located | Not located | Not located |
| Future Forcing | [2605.30083](https://arxiv.org/abs/2605.30083) | Training-free future-aware KV policy | Not located | Not needed for training-free algorithm | Not located |
| Recency Forcing | [2609.19729](https://arxiv.org/abs/2609.19729) | Training-free and training-based temporal-response bias variants | Not located | No method-specific checkpoint confirmed | Not located |
| Action Forcing | [2609.30595](https://arxiv.org/abs/2609.30595) | Video-based unsupervised egomotion bases | Not located | Not located | Not located |

## Audit standard

- **Not located** means targeted primary-paper and public source/code searches did not confirm an author-attributable release as of the audit date.
- Third-party reimplementations and similarly named unrelated repositories do not count as official code.
- For training-free methods, no new model checkpoint may be necessary; record base-model dependencies separately.
- All records still have `execution_checked=no`; no GPU execution, download authentication, or performance replication was conducted.
