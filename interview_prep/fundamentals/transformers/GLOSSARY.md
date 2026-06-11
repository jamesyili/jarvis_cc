# Transformers Glossary

Canonical language for this workspace. Terms are added only once James demonstrably understands them. Seeded with the forward-pass terms already known cold (LR-0001); training terms get added as lessons establish them.

## Architecture (known)

**Self-attention**:
The operation `softmax(QKᵀ/√d_k)·V` — a data-dependent weighted average where each position pulls information from others by content similarity.
_Avoid_: "the attention thing", soft lookup

**Q / K / V**:
Three separate learned linear projections of the same input — query ("what I'm looking for"), key ("what I match on"), value ("what I contribute"). K and V are deliberately decoupled.

**Multi-head attention**:
`h` independent attention operations of width `d/h` run in parallel, concatenated and projected — several relationship types at ≈ the cost of one wide head.

**Transformer block**:
One pre-norm unit: `z = x + Attn(LN(x))`, `y = z + FFN(LN(z))`. Attention = the only cross-position mixing; FFN = per-token compute (most params).

**Causal mask**:
Setting attention scores for future positions to −∞ before softmax, so position `t` sees only `≤ t`. Makes left-to-right next-token training well-posed.

**Logits**:
The pre-softmax scores over the vocabulary produced by the final linear ("unembedding") layer.

## Recsys (known)

**Next-item prediction**:
The recsys instance of next-token prediction — given a user's interaction history, predict the next engaged item. Training objective behind SASRec and the FM.

**Candidate early-fusion**:
Concatenating the candidate item onto every history token before self-attention, making the encoder candidate-aware (TransAct v1). The realized form of DIN-style target attention.

<!-- Training terms (cross-entropy, backprop, Adam, learning rate schedule, gradient clipping, teacher forcing, etc.) will be added here as lessons establish demonstrated understanding. -->
