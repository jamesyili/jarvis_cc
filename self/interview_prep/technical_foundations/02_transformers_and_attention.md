# 02 — Transformers & Attention

> **Bridge:** This is the vocabulary floor — the one place a generic answer caps you. But you have a real anchor: the UPP Foundation Model is a **decoder-only transformer over user-action sequences** (user-level next-token prediction), and OneTrans/CLR are transformer-tokenized retrieval. And the deep idea — **attention is retrieval** — turns your two-tower background into transformer fluency.
> **Book:** Ch 3 (architecture essentials), Ch 15–16 (inference/KV cache). Your study plan: *skim for vocabulary, don't derive flash attention.* That's right — know the shapes, not the kernels.

---

## 1. The core idea

A transformer is a stack of layers that repeatedly does two things to a sequence of vectors: **(a) mix information across positions (attention)**, then **(b) transform each position independently (a feed-forward network)**. Residual connections + normalization keep it trainable at depth. That's it. Everything else is detail.

The one sentence that makes you sound like you *get* it rather than memorized it:

> **Attention is differentiable retrieval.** Each position emits a *query*; it scores that query against every position's *key* (a similarity / soft nearest-neighbor search); it then reads out a weighted blend of every position's *value*. A transformer layer is "every token retrieves from every other token, then updates itself." Stack that, and you get a model that builds richer and richer contextual representations.

You have been building the non-differentiable, billion-item version of this exact operation (two-tower retrieval → ANN) for years. Say so.

---

## 2. The mechanics (know the shapes, not the kernels)

### Scaled dot-product attention
For an input sequence $X \in \mathbb{R}^{n\times d}$, learn three projections to get queries, keys, values:
$$Q = XW_Q,\quad K = XW_K,\quad V = XW_V$$
$$\text{Attention}(Q,K,V) = \underbrace{\text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)}_{\text{attention weights }n\times n} V$$

- $QK^\top$ = all-pairs similarity (the "retrieval scores"). $\sqrt{d_k}$ stops the dot products from saturating the softmax.
- Softmax over the row = "how much should this position read from each other position."
- Multiply by $V$ = the weighted read-out.

### The pieces around it
- **Multi-head:** run $h$ attentions in parallel on slices of the dimension, concatenate. Different heads learn different relations (syntax, coreference, position). More heads = more *kinds* of retrieval per layer.
- **Causal mask (decoder-only):** zero out attention to future positions so position $t$ only sees $\le t$. This is what makes **next-token prediction** well-posed — and it's the UPP FM setup (predict the next user action from past actions).
- **Position encodings:** attention is permutation-invariant, so you must inject order. Modern default is **RoPE** (rotary) — rotates Q/K by position so relative distance is encoded in the dot product; generalizes to longer contexts better than learned absolute embeddings. (One-liner depth is enough.)
- **FFN / MLP:** per-position $\text{up} \to \text{nonlinearity (SwiGLU)} \to \text{down}$. This is where most parameters and most "stored knowledge" live. (MoE replaces this with sparse experts — guide 07.)
- **Residual + pre-norm:** $x \leftarrow x + \text{sublayer}(\text{norm}(x))$. **RMSNorm**, **pre-norm** (norm before the sublayer) is the modern stable choice.

### Two numbers you must be able to recite
- **Compute / memory of attention is $O(n^2 d)$** in sequence length $n$ — quadratic. This is *the* reason long context is hard and why the variant zoo below exists.
- **Decoder-only** is the dominant LLM architecture (GPT/Claude/Llama). Encoder-decoder (T5) and encoder-only (BERT) exist; know they exist and when (BERT = embeddings/classification, decoder-only = generation).

### But "attention is quadratic" is the 2017 picture (say this — it's the currency check)
Frontier models attack the cost from two sides, and naming this progression is a strong senior signal:
- **KV-cache compression — the progression `MHA → MQA → GQA → MLA`.** MHA caches one K/V per head (expensive); **MQA** shares *one* K/V set across all heads (cheap, slight quality hit); **GQA** shares K/V within $G$ groups — the expressiveness/efficiency sweet spot and the **Llama-2/3, Mistral, Gemma default**; **MLA** (DeepSeek) low-rank-compresses the KV into a small latent vector. Each step shrinks the KV cache (guide 07's binding constraint) for cheaper long-context decode.
- **Sub-quadratic attention itself** — sliding-window / local (Mistral, $O(n\cdot W)$, global reach recovered by stacking layers), linear attention (Linformer). Separately, **FlashAttention** does *not* lower the $O(n^2)$ complexity — it makes it **IO-efficient on-GPU** (fewer HBM read/writes). Keep that distinction straight; people conflate them.
- *EM altitude: name the progression and which models use what; don't derive the kernels (your study plan's Tier-3 line).*

---

## 3. Your anchor: the UPP FM, OneTrans, and sequence modeling

- **UPP Foundation Model = decoder-only transformer over user actions.** "User-level next-token prediction" maps word-for-word: the *sequence* is the user's action history (your **L500** = last 500 actions), the *tokens* are actions/items, the *objective* is causal next-action prediction. The learned per-position representation **is** the user state that base retrieval/ranking consume. You are running the LLM recipe on behavioral sequences.
- **OneTrans** (the P2P unified-transformer tokenization that surprised UPP) and **CLR** are transformer-based retrieval — tokenizing heterogeneous features into a sequence and attending over them, instead of hand-engineered feature crosses. The industry trend you lived through — *feature-cross layers → transformer tokenization* — is the same trend as *hand-engineered NLP features → attention*.
- **Sequence modeling is your native turf.** Recsys has been doing sequential user modeling (GRU4Rec → SASRec/BERT4Rec → transformer rankers) in parallel with NLP. When an interviewer asks "how would you model a user's history," you don't reach for a toy — you have L500 + a pretrained user transformer in production.

---

## 4. The frontier-lab connection

- This *is* the LLM. Decoder-only transformer + next-token pretraining (guide 03) + RLHF (guide 05) = a modern chat model. You now hold all three.
- **What an EM must know:** the QKV intuition, multi-head, causal masking, why position encodings exist, the $O(n^2)$ cost and what it implies, decoder-only vs encoder-only. **What an EM does *not* need:** to derive FlashAttention, hand-write the backward pass, or recite head-dim hyperparameters. Your study plan flags this correctly — depth here is a trap for an EM loop.
- **The KV cache** (why generation is memory-bound, not compute-bound) is the one inference detail worth a sentence — full treatment in guide 07.

---

## 5. Interview-portable (90 seconds)

> *"A transformer is alternating layers of attention — which mixes information across positions — and a per-position MLP, wrapped in residual connections. The thing I'd emphasize is that attention is just differentiable retrieval: every token emits a query, scores it against every other token's key, and reads out a weighted blend of values — a soft nearest-neighbor search over the sequence. I find that framing natural because I've spent years building the hard-retrieval version of it: two-tower models doing approximate nearest-neighbor over billions of items. On the modeling side, the foundation model my org pretrains is a decoder-only transformer over user-action sequences — user-level next-token prediction over the last 500 actions — so the same causal-masking, next-token recipe that trains a language model trains our user representation. The cost story is that attention is quadratic in sequence length, which is what drives the whole long-context and KV-cache toolbox."*

**Likely probes:**
- "Why $\sqrt{d_k}$?" → keeps dot products from saturating softmax into one-hot, preserving gradients.
- "Why multi-head?" → parallel subspaces learn different relations; one head can only express one weighting.
- "Encoder vs decoder-only?" → encoder = bidirectional, embeddings/classification (BERT); decoder-only = causal, generation (GPT/Claude). Most LLMs are decoder-only.
- "Why is generation slow?" → quadratic attention + memory-bound autoregressive decoding; KV cache amortizes recompute (guide 07).
- "How would you handle a 100k-token / 10k-action context?" → the $O(n^2)$ problem → KV-cache compression (GQA → MLA), sliding-window/local attention, or chunking/retrieval; name the trade-off, don't derive.
- "What attention do modern LLMs actually use?" → not vanilla MHA — GQA is the open-weights default (Llama/Mistral/Gemma), MLA is DeepSeek's KV-compression variant; FlashAttention for IO-efficiency on top.

---

## 6. Self-test (out loud, from memory)

1. Write scaled dot-product attention. What is each of Q, K, V, and what does the softmax-over-keys mean?
2. Explain "attention is retrieval" in one breath. What's the analogue of the ANN index in a transformer?
3. What does the causal mask do, and why is it required for next-token prediction? Tie it to the UPP FM.
4. Why do transformers need position encodings at all? What does RoPE buy over learned absolute?
5. State the compute complexity of attention in sequence length and name two consequences.
6. Walk the `MHA → MQA → GQA → MLA` progression — what does each step buy, and which models use GQA vs MLA? Why is FlashAttention *not* in that list?
7. Map "user-level next-token prediction over L500" onto the GPT training setup, term by term.

*Shaky on 1, 4, 5? Hoang Ch 3, skim only. 3 and 6 you already own — they're your FM.*
