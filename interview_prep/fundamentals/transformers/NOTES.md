# NOTES — working notes & preferences

## Teaching preferences (from James)
- **Rigor over analogy.** First-principles, real math, name the failure modes. (`feedback_learning_material_rigor`)
- **Draw connections** back to his real world (CFM/TransAct/CLR/Reflex) and across to known fundamentals.
- **Flag uncertainty.** Mark inferred/contested; don't present as settled.
- **Quick wins**, one tight thing per lesson. Time-boxed.
- Lessons phone-readable MD in Phase 1 (no JS/interactivity — email strips it). Rich HTML + code = Phase 2.

## Curriculum
**`PLAN.md` is authoritative.** Three streams, **sequential**: Stream 1 (training theory) → Stream 2 (recsys) → Stream 3 (post-training/RLHF). Phase 2 = hands-on at computer (~June 23+).

## Raschka book → Phase-2 map (the train-from-scratch code spine)
- Ch2 (text data) → P2 data work · **Ch5 (pretraining loop)** → P2-1..3 ground truth · App.D (warmup/cosine/clip) → maps to Stream-1 1.3 · Ch6 (classification finetune) + Ch7 (instruction) + **App.E (LoRA)** → P2-6 + Stream-2 2.4/2.5 bridge. Skip/skim Ch3–4 (forward arch, known). **Phase 2 only** — don't require for Phase 1.

## Sequence tracker (Phase 1, on-demand)
Order: **1.1 · 1.2 · 1.3 · 1.4 · 1.5 · 2.1 · 2.2 · 2.3 · 2.4 · 2.5 · 3.1 · 3.2 · 3.3 · 3.4**
**Delivered:** 2.1 (`lessons/0002`, out of order — do when we reach Stream 2); **1.1 (`lessons/0003`) = current start.**
**Next on "next":** 1.2 (training objective).
**Pending from James:** answers to 1.1 ★ questions → log learning-record → 1.2.

## Lesson file index (creation order ≠ stream order)
- `0001` (html) — Anatomy of one training step (foundational; pre-stream)
- `0002` (md) — Stream 2 · Module 2.1 — next-token → next-item
- `0003` (md) — Stream 1 · Module 1.1 — positional encoding / RoPE

## Session log
- 2026-06-08 — Workspace + L01 (html). OOO two-phase plan built. Streams renamed 1/2/3 and switched to **sequential** (1→2→3) per James. RLHF book confirmed = Lambert. Delivered 2.1 (`0002`) then re-sequenced; delivered **1.1 (`0003`)** as the real start. Emailed updated plan + 1.1 + backup bundle.
