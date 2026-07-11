# Stream 1 · Module 1.1 — Positional encoding: sinusoidal → RoPE

*Transformers › Stream 1 (training theory) › ~45–60 min › read on phone, work in Notes + chat*

> **Mission tie-in.** This is the literal next item on your `llm_fundamentals` roadmap, and it has a sharp recsys payoff: in a user-sequence model, *position is time*, and how you encode time is a real design lever (TransAct v1 vs v2 actually disagree on it). Get this and you can reason about temporal modeling in CFM/TransAct, not just recite it.

---

## The one idea

Self-attention is **order-blind**. You have to *inject* position. The field moved from **adding** an absolute position vector (sinusoidal) to **rotating** the query/key vectors so the attention score depends only on **relative** distance (RoPE). RoPE is the modern default — understand *why* and you understand the whole arc.

---

## Why position must be injected at all

Self-attention is **permutation-equivariant**: permute the input tokens and the outputs permute identically. Formally, if `P` is a permutation, `Attention(PX) = P·Attention(X)`. Attention is a weighted average over a *set* — it has no built-in notion of "token 3 comes before token 7."

So "the cat sat" and "sat the cat" would produce the same representations (just reordered) without position information. Position has to be added explicitly. (Vaswani et al. 2017.)

---

## Approach 1 — Absolute sinusoidal (the original)

Add a fixed vector to each token's embedding, where each dimension is a sinusoid of a different wavelength:

`PE(pos, 2i)   = sin( pos / 10000^(2i/d) )`
`PE(pos, 2i+1) = cos( pos / 10000^(2i/d) )`

Low dimensions oscillate fast, high dimensions slowly — a continuous "binary clock." Two nice properties:
- **Extrapolates** past training length (it's a function, not a table).
- **Relative offsets are expressible**: because of the `sin/cos` angle-addition identities, `PE(pos+k)` is a *linear function* of `PE(pos)`. So the model *can* learn to attend "k positions back."

## Approach 2 — Learned absolute (GPT-2, BERT)

Just a learned embedding per position index, added to the token embedding. Simple and works — but it's a fixed table, so it **does not extrapolate** beyond the maximum length seen in training, and it bakes in *absolute* index rather than relative distance.

---

## The shift to RELATIVE position

Insight: for most sequence tasks what matters is **how far apart** two tokens are, not their absolute indices. "The adjective modifies the noun two words later" is a *relative* fact. So the modern designs encode relative distance directly.

## Approach 3 — RoPE (Rotary Position Embedding) — the modern default

Instead of *adding* a position vector, **rotate** each query and key vector by an angle proportional to its position. Take the vector in consecutive 2-D pairs; for a pair `(x1, x2)` at position `m`, rotate by `m·θ`:

`x1' = x1·cos(mθ) − x2·sin(mθ)`
`x2' = x1·sin(mθ) + x2·cos(mθ)`

Each pair `i` uses its own frequency `θ_i = 10000^(−2i/d)` (same frequency schedule idea as sinusoidal). Apply this rotation to `q` (at its position `m`) and to `k` (at its position `n`) *before* the dot product.

**The magic:** a dot product of two rotated vectors depends only on the **difference of their rotation angles**. Rotating `q` by `mθ` and `k` by `nθ`, the score `q_m · k_n` comes out as a function of `(m − n)` — the **relative** offset — and the absolute positions cancel. So RoPE gives you relative position *for free, inside the attention dot product*, at every layer.

Why RoPE won (LLaMA, most current LLMs use it):
- **Relative position falls out naturally** of the score — no extra terms.
- **Applied at every layer**, inside attention (not just added once at the input).
- **Norm-preserving** — it's a rotation, so it doesn't rescale the vectors.
- **Better long-context extrapolation** than learned-absolute (and tunable via the base frequency).

## Honorable mention — ALiBi

Even simpler: add a **distance-proportional penalty** straight to the attention scores (`score − slope·|m−n|`), no position embeddings at all. Strong length extrapolation; common in some models. Good to know it exists as the "just bias the scores" option.

---

## The recsys payoff: position is TIME

This is where it gets directly useful to you.

- In a user-sequence transformer, the sequence index is a proxy for **time** — and in recsys **time is a genuine feature**, not just ordinal order. A purchase **1 hour ago** ≠ **1 year ago**, even if both are "the previous item." Recency and absolute time-gaps carry signal.
- So recsys models often inject **timestamps / time-gap embeddings**, not just ordinal position. RoPE-style relative schemes map naturally onto **"how long ago"** rather than "which index."
- **The TransAct tension (reason about this):** TransAct **v1** found positional encoding *didn't help* at sequence length ~100 — action-type features + the recency structure already carried enough. But TransAct **v2** models **lifelong (≈2-year, 16k-action)** sequences. Across two years, *when* something happened is hugely informative, so temporal encoding matters far more at lifelong scale than at length-100. Same architecture family, opposite conclusion about position — because the time-span changed.

**Design/interview frame:** "How do you encode position/time in a user-sequence model?" → ordinal vs **timestamp** vs **time-gap** embeddings; prefer **relative** ("how long ago") for recency; note that the value of temporal encoding *scales with the sequence's time-span* — marginal at short real-time windows, essential at lifelong scale.

---

## Your work (the 45–60 min) — answer in Notes, paste the starred ones to me

1. State precisely **why self-attention is order-blind.** (Use the word "permutation.")
2. **★** RoPE rotates `q` and `k` by an angle proportional to position. **Walk through why the resulting attention score depends only on the relative offset `(m − n)`** and not the absolute positions. (You don't need the algebra — reason it from "dot product of two rotated vectors.")
3. **★** TransAct v1 found positional encoding *didn't help* at length 100; v2 models lifelong 16k sequences. **Argue why temporal encoding should matter more at lifelong scale.** What changed?
4. One sentence: the difference between **absolute** and **relative** position encoding.

**Reflection (write in Notes):** In 3 sentences, "why RoPE beat absolute sinusoidal/learned encodings." Force the words *relative*, *every layer*, *extrapolation*.

**Reply to me with #2 and #3.** I'll push on your reasoning, then log a learning-record and advance to **1.2 — the training objective (cross-entropy, perplexity, teacher forcing)**.

---

*Sources: Vaswani et al. 2017 "Attention Is All You Need" (sinusoidal); Su et al. 2021 "RoFormer" (RoPE); Press et al. 2021 "ALiBi"; your `artifacts/transformers-for-recsys.html` Part 2 (Q-A) and the TransAct v1/v2 sections (Part 5).*
