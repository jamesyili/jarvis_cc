# LLM Fundamentals — first principles

**Style:** rigorous and direct. Define the object, show the mechanism and the math, explain *why* each piece exists, name the failure modes. No analogies unless a specific point needs one.

**How this doc is built:** taught live with James, written down as we go. James's clarifying questions are captured inline as **Q (James)** blocks so the reasoning behind each refinement is preserved.

## Roadmap

1. Tokenization — text → integer IDs (BPE) — *todo*
2. Embeddings — IDs → vectors — *assumed known (recsys); revisit on request*
3. Self-attention — the core operation — **done**
4. Multi-head attention — **done**
5. The transformer block — attention + FFN + residual/norm — **done**
6. Positional encoding — how order is injected — *next*
7. Training objective — next-token prediction, what pretraining optimizes — *todo*
8. Decoding / inference — generation, KV cache — *todo*

---

## 3. Self-attention

**Setup.** Input is a sequence of `n` tokens, each already an embedding vector of dimension `d`. Stack them into a matrix `X` of shape `(n, d)` — one row per token.

**Three projections.** Learn three weight matrices and project `X` three times:

```
Q = X·W_Q      (queries)
K = X·W_K      (keys)
V = X·W_V      (values)
```

`W_Q, W_K` have shape `(d, d_k)`; `W_V` has shape `(d, d_v)`. Every token now has a query, a key, and a value vector — three different learned linear views of the same token.

**The operation.**

```
Attention(Q,K,V) = softmax( Q·Kᵀ / √d_k )·V
```

Piece by piece, each with its reason:

- **`Q·Kᵀ`** → shape `(n, n)`. Entry `(i, j)` = dot product of token `i`'s query with token `j`'s key. A raw score: how much should token `i` pull information from token `j`? High dot product = relevant to each other in this learned space.
- **`/ √d_k`** → scaling. Dot products of `d_k`-dim vectors grow in magnitude like `√d_k`. Unscaled, the softmax inputs get large, softmax saturates (one weight ≈ 1, rest ≈ 0), and the gradient there ≈ 0 → training stalls. Dividing by `√d_k` holds variance ~1 so gradients stay healthy. That is the only reason this term exists.
- **`softmax(...)`** → per row. Turns each token's `n` raw scores into positive weights summing to 1. Row `i` is a distribution over "where token `i` looks."
- **`·V`** → weighted average of all tokens' value vectors, weighted by attention. Output row `i` has shape `(n, d_v)`.

**Result.** A new representation of each token that has mixed in information from the tokens it found relevant. The weights are computed fresh from the actual token content every forward pass — not fixed.

**Causal masking (critical for LLMs).** A language model predicts the next token, so token `i` must not see tokens after it. Before softmax, set every score `(i, j)` with `j > i` to `−∞`; after softmax those are 0 weight. Each token attends only to itself and earlier tokens. This is what makes left-to-right next-token training well-posed.

### Worked example — dynamic (attention) vs fixed (pooling) aggregation

Toy 3-D item embeddings, dims hand-labeled `[camping, cooking, fashion]` for visibility (real embeddings aren't interpretable). User's history:

| Item | `[camping, cooking, fashion]` |
|---|---|
| Hiking boots | `[0.9, 0.1, 0.3]` |
| Dress | `[0.0, 0.0, 1.0]` |
| Cookware set | `[0.1, 0.9, 0.0]` |
| Sleeping bag | `[0.95, 0.0, 0.1]` |
| Sneakers | `[0.2, 0.0, 0.7]` |

**Pooling (fixed):** average, uniform `1/5` weights → `user = [0.43, 0.20, 0.42]`. One blurry vector, used to score *everything*. Weights don't depend on what's being predicted.

**Attention (dynamic):** weight each past item by `softmax(Q·K)`, query = current context.

- *Scoring a TENT*, query `[1.0, 0.1, 0.0]`: raw `Q·K` = boots 0.91, dress 0.0, cookware 0.19, sleeping bag 0.95, sneakers 0.20 → softmax weights `{boots .29, dress .12, cookware .14, bag .30, sneakers .14}` → camping items carry ~0.60 → `user = [0.59, 0.16, 0.34]`.
- *Scoring a HANDBAG*, query `[0.0, 0.0, 1.0]`: weights `{boots .17, dress .33, cookware .12, bag .14, sneakers .25}` → fashion items dominate → `user = [0.34, 0.13, 0.57]`.

```
Pooling (either):   [0.43, 0.20, 0.42]   ← identical, can't adapt
Attention, tent:    [0.59, 0.16, 0.34]   ← camping-forward
Attention, handbag: [0.34, 0.13, 0.57]   ← fashion-forward
```

**Same history → different representation per context.** That is content-dependent weighting: weights are a function of the query, recomputed every forward pass. Caveats: (1) real `Q/K` are *learned* projections, so "relevance" can be cleverer than similarity (e.g. complementary not just similar items); (2) `/√d_k` scaling omitted here for clarity.

### Jay Alammar's per-token diagram — computing z1 for "Thinking"

The scalar, token-by-token unrolling of `softmax(Q·Kᵀ/√d_k)·V`. Here `d_k = 64`, so `√d_k = 8`.

```
                        "Thinking" (tok 1)        "Machines" (tok 2)
  Input                 Thinking                  Machines
  Embedding             x1                        x2
  Queries               q1                        q2
  Keys                  k1                        k2
  Values                v1                        v2
  ───────── computing z1: use q1, score it against every key ─────────
  Score  (q1·k_j)       q1·k1 = 112               q1·k2 = 96
  Divide by 8 (√d_k)    14                        12
  Softmax               0.88                      0.12
  Softmax × Value       0.88·v1   (full)          0.12·v2   (faded)
  Sum                   z1 = 0.88·v1 + 0.12·v2  ◄─ output for "Thinking"
```

**Interpretation of the last three rows:**

1. **Softmax → 0.88 / 0.12 = attention weights.** The mixing proportions: build Thinking's new representation from 88% its own content + 12% Machines'. Normalized to sum to 1; here it attends mostly to itself (common).
2. **Softmax × Value → scaled contributions.** Each token's *value* (content payload) is scaled by its weight. `v1` stays nearly intact (full); `v2` washes out (faded) — Machines is in the mix, quietly. The **value** is scaled, not the key — the key already did its job (setting the weight).
3. **Sum → z1 = the self-attention output for this token.** Collapses the row into one vector: Thinking *as it sits in this sentence* (was `x1` in isolation). Flows up into the FFN sublayer.

One motion: **weights (how much) → weighted values (scaled content) → sum (one blended output).** The diagram is per-token scalars; the matrix form does all tokens at once. The `0.88/0.12` weights are specific to `q1`; `z2` is computed the same way with `q2`'s own scores.

---

## 4. Multi-head attention

**The problem with one head.** A single attention computes *one* distribution per token and *one* weighted average. But a token usually needs to attend to different things for different reasons at once — subject–verb agreement, a pronoun's antecedent, local adjacency. One head collapses all of that into a single averaged mixture; distinct patterns interfere.

**Mechanism.** Split into `h` heads. Each head `i` has its own smaller projections to dimension `d_k = d/h`:

```
head_i = Attention(X·W_Q^i, X·W_K^i, X·W_V^i)        # each output (n, d/h)
MultiHead(X) = Concat(head_1, …, head_h)·W_O          # back to (n, d)
```

Run scaled dot-product attention independently in each head, concatenate the `h` outputs along the feature dimension (recovering width `d`), then apply an output projection `W_O` of shape `(d, d)` to mix across heads.

**Why it's nearly free.** `h` heads of width `d/h` cost ≈ the same total compute as one head of width `d`, but give `h` independent attention patterns in `h` different subspaces. Strictly more expressive at ~equal cost. Heads empirically specialize (one tracks adjacency, another coreference, etc.) — observed, not enforced.

---

## 5. The transformer block (decoder-only)

A block composes multi-head self-attention with a position-wise feed-forward network, wrapped in residual connections and layer norm. Modern pre-norm form:

```
z = x + MultiHeadSelfAttention(LayerNorm(x))
y = z + FFN(LayerNorm(z))
```

**Two sublayers, clean division of labor:**
1. **Attention sublayer** — the *only* place tokens exchange information across positions.
2. **FFN sublayer** — processes each token independently; no cross-token mixing.

**FFN.** `FFN(u) = W_2·φ(W_1·u + b_1) + b_2`. `W_1` expands `d` → hidden (classically `4d`); `φ` is a nonlinearity (GELU; SwiGLU in modern LLMs); `W_2` projects back to `d`. Most parameters and much of the stored "knowledge" live here. Applied identically and separately to every position.

**Residual connections** (`x + …`). Let each block learn a *delta* to the representation instead of rebuilding it, and let gradients flow through deep stacks. Essential for training depth (dozens to 100+ layers).

**LayerNorm.** Normalizes each token vector (mean 0, variance 1 across its `d` features, then learned scale/shift) to keep activations well-conditioned. Pre-norm (normalize inside the residual branch, before each sublayer) is the modern default — it makes very deep stacks stable to train.

**Stacking.** An LLM is `L` of these blocks in sequence; each block's output is the next block's input. Lower layers tend toward local/syntactic structure, higher layers toward abstract/semantic — emergent, not designed.

---

## Tangents & questions

### Q (James): Why do transformers work for recsys too — is it the sequential part? And why are transformers tied to "scaling"? (intuition)

**Recsys.** Sequential recommendation does map to next-token prediction (history = sequence of item embeddings; predict next item — SASRec/BERT4Rec). But the reason transformers beat RNNs/pooling is three mechanisms:
1. **Direct long-range access** — RNNs crush history into one fixed hidden state (decays over steps); attention reads any past interaction directly, path length 1, learned weight.
2. **Content-dependent dynamic weighting** — relevance of each past item is computed from content (`Q·K`), so the model focuses selectively (camping history up-weighted before a tent purchase) vs. uniform pooling.
3. **Parallelism** — RNNs are sequential (`t` needs `t−1`); transformers compute all positions at once → feasible to train on huge interaction logs.

Deepest framing: attention is **learned, content-dependent aggregation over a set with explicit pairwise interactions**. Sequences are the common case; it also helps for feature-interaction and candidate-set modeling.

**Scaling.** The referent is **scaling laws**: transformer test loss falls as a clean power law in params/data/compute over many orders of magnitude (Kaplan 2020, Chinchilla 2022) — *predictably*, so you can forecast a bigger model's quality before training it. Why transformers scale:
1. **No saturating bottleneck** — unlike RNN fixed state / CNN fixed receptive field, all-to-all attention lets added width/depth/heads always be used; no dead capacity.
2. **Parallelism delivers the scale** — turns more compute into more throughput; RNNs can't.
3. **Self-supervision removes the data ceiling** — next-token needs no labels, so the data axis is ~unlimited.

**Shared fact:** the same property — **all-to-all attention + parallel computation** — powers both. All-to-all access gives long-range recsys modeling *and* bottleneck-free scaling; parallelism makes both large recsys logs and large pretraining feasible. One architectural property, two payoffs.

### Q (James): What do Q/K/V and the W matrices represent in recsys? Does every item have an ID embedding, and what about cold-start (OOV/OOC)?

**Q/K/V (roles):** Query = "what am I looking for" (the prediction context — most recent item / candidate being scored). Key = "what do I match against" (each past item's advertised index; controls *whether* it's attended to). Value = "what I contribute" (the content that flows once attended; controls *what* flows). Crux: **key and value are different learned projections of the same item** — matching geometry decoupled from content geometry. Continuity with two-tower: same dot-product relevance, applied within the history and recomputed per context.

**W_Q/W_K/W_V (matrices):** the learned projections that *define* query/key/value. Shared across all positions (one `W_Q` for every item → sequence length adds no params). `W_K/W_Q` carve the matching subspace, `W_V` the content subspace. The 64-vs-512 in Jay's post = multi-head split: `d_k = d_model/h = 512/8 = 64`; 8 heads × 64 ≈ one 512-wide head's cost.

**ID embeddings + cold-start:** Vanilla SASRec/BERT4Rec keep a per-item-ID embedding *lookup table* (= token table; vocab = catalog). Gives the OOV problem in two forms: (1) cold-start — unseen items have no trained row; (2) long-tail starvation — rare IDs barely trained, table huge. Fixes, usually combined:
- **Content/feature embeddings** (image/text/category → encoder): new items have content even with zero interactions → generalize to unseen (why OmniSage-style content embeddings exist). *Main fix.*
- **Hashing trick:** hash any ID into fixed buckets → unseen IDs still map somewhere (lossy via collisions).
- **Hybrid (industry default):** ID embedding (sharp CF/memorization for the head) ⊕ content embedding (generalization for tail + cold); warm up the ID online once interactions accrue.

**Precise NLP parallel:** NLP killed OOV via **subword/BPE** — unseen words decompose into known sub-units. Recsys can't (an item doesn't decompose into "sub-items"), so it escapes via **content features** instead. Same problem, different hatch, because of what an "item" is vs. a "word."
