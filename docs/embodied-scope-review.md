# Scope review: what belongs in an Embodied Forcing list?

A **curation judgment**, not a new claim about experimental results. Reviewed against indexed papers' stated target tasks and intervention mechanisms (2026-10-29).

## Core embodied / robotic work (9)

These papers explicitly target robotic policies, robotic world/action models, robot manipulation/navigation, or action-control learning.

- PhysisForcing
- Relational Geometry Forcing
- WorldSync (Action-Forcing)
- Discrete Forcing
- Language-Forcing
- Next Forcing
- AR Forcing
- Step Forcing (RoboWorld)
- Action Forcing

## Transferable world/video modeling (14)

These may be relevant to embodied research through long-horizon prediction, physical structure, controllability or self-rollouts, but they **do not automatically demonstrate a robot closed-loop gain**.

- Diffusion Forcing
- Fréchet Forcing
- Self Forcing
- Self-Forcing++
- Rolling Forcing
- Geometry Forcing
- Memory Forcing
- Pack and Force Your Memory
- Reward Forcing
- Causal Forcing
- Causal Forcing++
- Delta Forcing
- Self-Aligned Forcing
- Steady-Forcing

## Adjacent video generation and systems (10)

These primarily concern inference throughput, KV/memory budgeting or streaming video systems. Keep them for context and possible transfer, **not** as evidence of robotics performance.

- Deep Forcing
- Head Forcing
- Forcing-KV
- Future Forcing
- Focused Forcing
- Pyramid Forcing
- Recency Forcing
- RECAP-Forcing
- Neighbor Forcing (SoulX-LiveAct)
- Speculative Forcing

## Important borderline calls

- **Diffusion Forcing** is placed in transferable because it is a general sequence method with decision/planning applications; the robotics relevance is real but the scope is broader.
- **Fréchet Forcing** uses robot video (DROID), but its primary training outcome is long-horizon world/video rollouts, so robot data alone does not make it a core robot-policy study.
- **Geometry Forcing** gives geometry-supervised video generation, versus **Relational Geometry Forcing**, focused on embodied action representation.
- **Delta Forcing** targets interactive action-conditioned video: actionable world modeling, but not necessarily a robot policy evaluation.
- **Neighbor Forcing** is a streaming animation module, not a robot-neighbor-control algorithm.
- **Pyramid, Deep, Forcing-KV** are system-level improvements and should not be mixed into manipulation-success leaderboards.

## Inclusion policy

Core = explicitly robotic control/robot evaluation or WAM. Transferable = world/video mechanism with plausible robotics use. Adjacent = useful supporting infrastructure, not an embodied method.

These labels can be revised when a primary paper demonstrates new robotics evaluation evidence. Do not infer embodied relevance solely from using DROID or mentioning physical plausibility.
