---
concept: Transformer Architecture
tags: [transformer, attention, self-attention, positional-encoding, mha, gqa, mla, flashattention]
sources:
  - kb/hard/raw/aman-ai/primers-transformers.md
  - kb/hard/raw/jay-alammar/how-gpt3-works-visualizations-and-animations.md
  - kb/hard/raw/sebastian-raschka/a-visual-guide-to-attention-variants-in-modern-llms.md
  - kb/hard/raw/lilian-weng/the-transformer-family-version-20.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/large-language-models|Large Language Models]]"
  - "[[hard/wiki/llm-inference-serving|LLM Inference & Serving]]"
  - "[[hard/wiki/embeddings-and-representation-learning|Embeddings & Representation Learning]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Transformer Architecture

The transformer, introduced by Vaswani et al. in "Attention Is All You Need" (2017), replaced sequential RNN-based processing with a fully parallel attention mechanism. It became the backbone of every major language model and most state-of-the-art vision systems. Understanding its internals — from scaled dot-product attention through positional encoding to the modern GQA/MLA attention variants — is essential for any serious ML practitioner.

## Why Transformers Replaced RNNs

RNNs process tokens sequentially, passing a hidden state left to right. That design created two fundamental problems: long-range dependencies degraded because gradients vanished over many timesteps, and sequential computation blocked parallelism, making training slow. Transformers eliminate both problems. Every token attends to every other token in a single operation, and the full sequence can be processed in parallel on GPUs. The trade-off is quadratic memory in sequence length — a limitation that has driven decades of subsequent research.

The representational insight is that attention computes *contextual* embeddings. The word "bank" in "river bank" and "bank account" gets different vector representations after attention because its neighbors differ. Static word2vec embeddings cannot do this.

## Self-Attention: The Core Operation

Given an input sequence of length L with embedding dimension d, self-attention projects each token into three vectors: query (Q), key (K), and value (V) using learned weight matrices W_q, W_k, W_v ∈ R^{d × d_k}.

Scaled dot-product attention:

```
A = softmax(QK^T / sqrt(d_k)) * V
```

The scaling by sqrt(d_k) prevents the dot products from growing so large that softmax saturates into near-zero gradients. The attention matrix A ∈ R^{L×L} captures every pairwise token relationship. Each row answers: "when updating this token, how much should each other token contribute?"

In **decoder-only** (GPT-style) models, a causal mask zeros out the upper-right triangle of A — each position can only attend to past tokens. This is enforced during both training and inference. In **encoder-only** (BERT-style) models, there is no mask and every position can attend to the full sequence bidirectionally.

## Multi-Head Attention (MHA)

Single-head attention captures one type of relationship. Multi-head attention (MHA) runs h parallel attention heads, each with its own learned projections, then concatenates and projects the outputs:

```
MultiHead(Q,K,V) = Concat(head_1,...,head_h) W^o
where head_i = Attention(Q W_i^q, K W_i^k, V W_i^v)
```

Different heads specialize: one may capture syntactic dependencies, another semantic similarity, another positional proximity. GPT-2 used MHA with h=16 heads; modern LLMs have 32–128 heads. MHA is the baseline all other attention variants are measured against.

## Multi-Query Attention (MQA) and Grouped-Query Attention (GQA)

The KV cache is a major bottleneck at inference time. For a sequence of length L with h heads and dimension d_v, caching the K and V matrices costs O(L × h × d_v) memory per layer. For long contexts and large models, this becomes the binding constraint.

**MQA** (Shazeer 2019) collapses all heads to share a single K and V projection. This reduces KV cache by a factor of h but can hurt model quality noticeably.

**GQA** (Ainslie et al. 2023) is the practical compromise: group the h query heads into g groups, with each group sharing one K and V projection. If g = 1, GQA degrades to MQA; if g = h, it recovers MHA. Most modern models (Llama 3, Qwen3, Gemma 3) use GQA with g typically between 4 and 8. At long contexts, the KV cache savings become pronounced — the cache shrinks by h/g relative to MHA.

The rule of thumb: GQA is simpler to implement than MLA, robust across model sizes, and the default choice for most labs building models under ~100B parameters.

## Multi-Head Latent Attention (MLA)

MLA, introduced in DeepSeek-V2 (2024) and central to DeepSeek-V3/R1, takes a different approach to KV cache compression. Rather than sharing heads (GQA), MLA compresses the K and V tensors into a low-dimensional latent representation before caching. At inference time, the latent is projected back to full resolution.

The key advantage: ablation studies in the DeepSeek-V2 paper showed MLA maintained or exceeded MHA modeling performance at the same memory budget, while GQA degraded below MHA. This makes MLA compelling for very large models (100B+) where cache traffic dominates. The cost is implementation complexity — MLA is harder to build and serve than GQA.

Current landscape (2025): GQA dominates dense models under ~100B (Llama 4 Maverick, Qwen3, Gemma 3). MLA is used in DeepSeek-V3, Kimi K2, Mistral Large 3, and increasingly in the 100B+ tier.

## Positional Encoding

Attention has no inherent notion of token order — it treats the input as a set. Positional encoding injects position information.

**Sinusoidal (absolute) PE**: The original transformer added fixed sinusoidal functions at different frequencies directly to token embeddings. Simple and parameter-free, but tokens at each position always get the same encoding regardless of neighbors. Struggles to generalize to sequence lengths longer than those seen during training.

**Rotary Position Embeddings (RoPE)**: Introduced in 2021, RoPE encodes position by rotating query and key vectors in a way that depends only on the *relative distance* between positions. The dot product QK^T then naturally encodes relative position. Crucially, RoPE enables context length extension: by adjusting the rotation frequencies (via positional interpolation or YaRN), models can be extended from 4K to 128K tokens with modest fine-tuning. Llama made RoPE the de-facto standard; virtually all modern LLMs use it.

**ALiBi (Attention with Linear Biases)**: Instead of encoding position in the embeddings, ALiBi adds a linear bias to attention scores — positions further apart get a larger negative bias. This makes attention naturally favor nearby tokens. ALiBi extrapolates well to longer sequences with no modification, making it attractive for long-context models, though it is less common than RoPE in recent frontier models.

## The Transformer Block

Each transformer layer stacks two sub-modules with residual connections and normalization:

1. **Multi-head attention** (causal or bidirectional depending on architecture)
2. **Feed-forward network (FFN)**: two (or three, in SwiGLU) linear layers with a nonlinearity

Modern LLMs replace LayerNorm with **RMSNorm** (simpler, slightly faster — no mean centering) and move normalization *before* each sub-module (Pre-Norm), which stabilizes training gradients compared to Post-Norm. Some models (OLMo 2, Gemma 3) experiment with both pre- and post-norm simultaneously.

The FFN is usually expanded 4x the model dimension. The SwiGLU variant uses three matrices and a gating mechanism that provides multiplicative interaction — this improves expressivity with similar parameter counts and is now standard (Llama, Qwen, gpt-oss).

Stacking N such blocks, GPT-3 has 96 layers; LLaMA 3 8B has 32; DeepSeek-V3 has 61 (with MoE substituting the FFN in most).

## Encoder vs. Decoder Architectures

**Encoder-only** (BERT-style): All tokens attend to all others. Trained with masked language modeling (MLM) — predict randomly masked tokens. Best for classification, NLI, embedding tasks where understanding context from both directions matters. Not used for generation.

**Decoder-only** (GPT-style): Causal mask enforces left-to-right attention. Trained with next-token prediction (NTP). The dominant architecture for LLMs since GPT-2 showed it scales extremely well. At inference, tokens are generated autoregressively one at a time.

**Encoder-decoder** (T5, BART-style): Encoder processes the full input with bidirectional attention; decoder generates output with causal attention plus cross-attention over encoder states. Good for translation and summarization where the input and output are distinct sequences.

## FlashAttention

Standard self-attention materializes the full L×L attention matrix in GPU HBM (high-bandwidth memory), requiring O(L²) memory and substantial memory bandwidth. For long contexts, this is both slow and memory-intensive.

FlashAttention (Dao et al. 2022; v2 2023) reorders attention computation to stay in GPU SRAM — faster by 2–4x and sublinear in memory with respect to sequence length. It uses tiling to compute attention in blocks without ever writing the full matrix to HBM. FlashAttention-2 is now standard in virtually all production LLM implementations. It makes 128K+ context windows practical.

## KV Cache

At inference, the transformer reprocesses all previous tokens at every generation step — a costly O(L²) operation. The KV cache stores the K and V projections for all previously seen tokens, reducing each new step to O(L) attention over the cached state. This is the core mechanism enabling fast autoregressive generation, but cache memory grows linearly with sequence length, which motivates GQA, MLA, and sliding window attention as compression strategies.

## Sources

- Aman.ai Primers: Transformers — detailed walkthrough of every component with code
- Jay Alammar: How GPT-3 Works — visual intuition for the forward pass and scale
- Sebastian Raschka: A Visual Guide to Attention Variants in Modern LLMs — MHA, GQA, MLA, SWA comparison
- Lilian Weng: The Transformer Family v2.0 — comprehensive survey of architecture variants
