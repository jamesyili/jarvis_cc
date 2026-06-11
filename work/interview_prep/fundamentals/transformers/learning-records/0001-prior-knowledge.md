# Prior knowledge: forward-pass architecture is solid; the gap is training

James arrives with strong, demonstrated understanding of the transformer **forward pass and its recsys applications** — established from `interview_prep/fundamentals/llm_fundamentals.md` (taught live, with his own clarifying Q-blocks) and `artifacts/transformers-for-recsys.html` (which he reviewed and extended). This sets the floor: lessons should **not** re-teach the forward architecture, and should start in the **training** direction.

**Known cold (skip re-teaching):**
- Self-attention `softmax(QKᵀ/√d_k)V`; why √d_k; Q/K/V as decoupled learned projections; causal masking.
- Multi-head attention; the transformer block (pre-norm: attention sublayer + FFN sublayer + residual + LayerNorm); matrix/shape form; the 4-step decode.
- Positional encoding concepts incl. sinusoidal + RoPE/ALiBi (exposed via the HTML; roadmap lists PE as the next *fundamentals* item — exposure, not yet demonstrated).
- Recsys mapping: item=token, history=sentence, next-item=next-token, catalog=vocabulary; cold-start/OOV via content embeddings; SASRec vs BERT4Rec.
- Pinterest-specific: TransAct v1/v2 (candidate early-fusion, NAL, 16k NN retrieval, serving), UPP FM/CFM/CLR (next-token-pretrained FM; CFM = FM + TransAct v2 + feature cross; two-tower CLR).

**Depth claimed/shown:** can explain mechanisms precisely and *draw connections* across them (architecture ↔ recsys ↔ internal systems). Strong conceptual, light on hands-on training mechanics.

**The genuine gap (where ZPD lives):**
- The **training loop** itself: loss → backward → optimizer step (the forward pass is known; what *changes the weights* is not yet hands-on).
- **Optimization** that converges (Adam, LR warmup/cosine, weight decay, grad clipping).
- **Debugging** training (loss sanity checks, overfit-one-batch, reading loss curves).
- **Recsys training specifics** as a *training* problem (sampled softmax, in-batch negatives, BCE + future-action loss, pretrain→finetune/LoRA) — he knows these as architecture facts, not as training mechanics.

## Implications
Start with **Lesson 01 = anatomy of one training step**. Sequence: training loop → optimization → debugging → recsys-training → pretrain/finetune. Gap-fill positional-encoding/KV-cache from his roadmap as short lessons when convenient. Tie every lesson back to a CFM/TransAct/CLR decision so it lands at Director altitude, not just interview altitude.
