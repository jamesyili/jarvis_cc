# Mission: Transformers — from first principles to training & recsys

## Why
James drives Pinterest's recsys/personalization platform work (UPP — CFM/FM, TransAct, CLR) and is operating toward Director. He needs deep, first-principles fluency in how transformers are *trained* (not just how they run) to make and defend architecture/training calls, pressure-test proposals (CFM scaling, OneTrans, TransAct), coach ICs, and present at CEO/CTO altitude — while also converting ML/EM interviews (OpenAI, Sr EM system design).

## Success looks like
- Can train a small transformer from scratch end-to-end — data → training loop → a model that converges — and explain every line of the loop.
- Can diagnose a stalled, diverging, or overfitting training run from its loss curves + config (a repeatable debugging recipe).
- Can map every training concept to its recsys instantiation (next-item prediction, sampled softmax, in-batch negatives, BCE + future-action loss, pretrain→finetune, LoRA) and use that to pressure-test CFM / TransAct / CLR design choices.
- Can answer ML-system-design interview questions on transformer training & serving with confidence.

## Constraints
- **Rigorous, first-principles, no analogy-soup** (stated preference — see `feedback_learning_material_rigor`).
- Time-boxed: busy EM, frequent OOO/travel. Lessons must be quick wins, completable in one sitting.
- Build on existing artifacts — `self/interview_prep/fundamentals/llm_fundamentals.md` and `system/artifacts/transformers-for-recsys.html`. Do **not** re-teach the forward-pass architecture he already knows (see LR-0001).

## Out of scope (for now)
- Distributed-training infra internals (FSDP / Megatron / parallelism mechanics) — aware of, not building.
- Non-transformer architectures (diffusion, GNNs) except as contrast.
- Serving-kernel engineering beyond the conceptual level already covered in the TransAct notes.
