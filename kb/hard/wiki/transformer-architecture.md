---
concept: Transformer Architecture
tags: [transformer, attention, self-attention, positional-encoding, llm-foundations, kv-cache, flashattention]
sources:
  - kb/hard/raw/aman-ai/primers-transformers.md
  - kb/hard/raw/aman-ai/recommendation-systems-transformers.md
  - kb/hard/raw/lilian-weng/the-transformer-family-version-20.md
  - kb/hard/raw/lilian-weng/the-transformer-family.md
  - kb/hard/raw/sebastian-raschka/a-visual-guide-to-attention-variants-in-modern-llms.md
  - kb/hard/raw/sebastian-raschka/understanding-and-coding-the-kv-cache-in-llms-from-scratch.md
  - kb/hard/raw/aman-ai/natural-language-processing-transformers.md
  - kb/hard/raw/aman-ai/natural-language-processing-attention.md
  - kb/hard/raw/aman-ai/primers-flashattention.md
  - kb/hard/raw/louis-wang/the-attention-bottleneck-how-modern-llms-solved-a-problem-that-nearly-broke-the.md
  - kb/hard/raw/cameron-wolfe/gpt-oss-from-the-ground-up.md
last_compiled: 2026-04-05
related: [embeddings-and-representation-learning, large-language-models, recommendation-systems]
---

# Transformer Architecture

## The Core Idea

The Transformer (Vaswani et al., 2017 — "Attention Is All You Need") replaced RNN-based encoder-decoders by making attention the primary sequence-processing mechanism. The key insight: instead of compressing a sequence into a fixed-length context vector (the RNN bottleneck), every token can directly attend to every other token.

**Scaled dot-product attention** is the fundamental operation:

```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) · V
```

Q (queries), K (keys), and V (values) are linear projections of the input embeddings. The scaling by `sqrt(d_k)` prevents dot products from becoming large enough to push softmax into near-zero gradient regions. The result is a T×T attention matrix where each row encodes how much each token attends to every other token. In decoder-only models, the upper-right triangle is masked to enforce causality.

**Multi-head attention (MHA)** runs H independent attention heads in parallel with different learned projections, then concatenates and projects the outputs. Different heads specialize — one might focus on local dependencies, another on long-range semantic relationships. Each head operates at dimension `d/H`, keeping total compute roughly constant.

**The full transformer block** wraps attention with:
1. Residual connection + layer norm (pre-norm is now standard)
2. Position-wise feed-forward network (two linear layers with a nonlinearity, typically ~4× hidden dim)
3. Another residual + layer norm

Multiple stacked blocks progressively build richer representations — the first layer attends to word-pair relationships; deeper layers attend to pairs-of-pairs, extending effective receptive field. [Aman AI: NLP Attention]

## Positional Encoding

Transformers have no built-in notion of order, so position must be injected explicitly.

**Sinusoidal (original):** Fixed sin/cos functions of position and frequency. Generalizes to unseen lengths but encodes absolute position.

**Learned embeddings:** Each position gets a trainable vector. Simple, effective within training range, but doesn't extrapolate.

**RoPE (Rotary Position Embedding):** Applied to Q and K before the dot product by rotating vectors in 2D subspaces by an angle proportional to position. The key property: when Q and K are multiplied, the rotation matrices cancel to `R(θ, n-m)` — only the *relative* distance between tokens is encoded, not absolute position. This is why RoPE extrapolates better to longer contexts. Original base frequency is 10K; Llama 3 uses 500K, Gemma 3 uses 1M, enabling longer context windows. Extensions like NTK-aware interpolation and YaRN modify the base frequency or apply temperature scaling to the softmax for further context extension. [Cameron Wolfe: GPT-oss]

**ALiBi (Attention with Linear Biases):** Adds a learned linear bias to attention scores based on token distance. Doesn't modify embeddings; designed for length extrapolation without fine-tuning.

## Architecture Variants

Three canonical forms emerged from the original encoder-decoder design:

| Variant | Examples | Use case |
|---------|----------|----------|
| **Encoder-only** | BERT, RoBERTa | Classification, NLU, embeddings. Bidirectional — every token sees all others. Pre-trained with masked language modeling (MLM) and next-sentence prediction. |
| **Decoder-only** | GPT family, Llama, Mistral | Autoregressive generation. Causal mask enforces left-to-right attention. |
| **Encoder-decoder** | T5, BART | Seq2seq tasks: translation, summarization. Encoder has bidirectional attention; decoder uses cross-attention over encoder outputs. |

BERT uses 12–24 transformer blocks, 768–1024 hidden dims, 12–16 attention heads, and pre-training on masked tokens lets the model condition on both left and right context. GPT-style models use the same decoder architecture but generate autoregressively. T5 frames all NLP tasks as text-to-text and pre-trains with a denoising objective. [Aman AI: NLP Transformers]

## Attention Variants: The KV Head Reduction Spectrum

Standard MHA is memory-intensive at inference: every head caches its own K and V tensors, growing linearly with sequence length per head. This became the primary inference bottleneck at scale.

**Multi-Query Attention (MQA)** (Shazeer, 2019): Keeps H query heads but collapses K/V to a single shared head. Cache shrinks by H×. Can cause quality degradation and training instability at scale. Used in PaLM.

**Grouped-Query Attention (GQA)** (Ainslie et al., 2023): G groups of query heads share K/V, where `1 < G < H`. MHA is GQA with G=H; MQA is GQA with G=1. At G=8 (Llama 3 configuration), cache is 8× smaller than MHA with near-identical quality. To convert an MHA checkpoint to GQA, mean-pool the H/G K/V projections within each group and continue training briefly. GQA is now the default in most production LLMs: Llama 2 70B, Llama 3, Mistral 7B, Gemma. [Louis Wang: Attention Bottleneck; Sebastian Raschka: Visual Guide]

**Multi-head Latent Attention (MLA)** (DeepSeek-V2, 2024): Instead of reducing the number of K/V heads, MLA compresses K and V into a low-dimensional latent vector `c_KV` and caches only that. Keys and values are reconstructed at attention time via up-projection. Only `c_KV` is stored, reducing the KV cache by 93.3% versus MHA — versus roughly 8× for GQA with G=8. Ablation studies show MLA maintains or slightly exceeds MHA quality while GQA can degrade below MHA at large scale. Trade-off: more implementation complexity. MLA is used in DeepSeek V2/V3/R1, Kimi K2, and Mistral Large 3. Practical observation: MLA seems to work better at 100B+ scale; GQA remains the easier choice for smaller models. [Sebastian Raschka: Visual Guide; Louis Wang: Attention Bottleneck]

| Variant | K/V heads | Cache vs. MHA | Quality vs. MHA |
|---------|-----------|---------------|-----------------|
| MHA | H | 1× (baseline) | Baseline |
| GQA (G groups) | G | H/G× smaller | Near-identical |
| MQA | 1 | H× smaller | Small degradation |
| MLA | Compressed latent | ~57–93× smaller | Comparable or better |

**Sliding Window Attention (SWA):** Each token attends only to a fixed local window of W recent tokens rather than the full prefix. This reduces the attention matrix from O(n²) to O(n·W). Information still propagates globally because stacked layers chain local windows — with L layers and window W, information travels up to L×W tokens. Gemma 3 uses a 5:1 local-to-global layer ratio with W=1024, showing modest perplexity impact. SWA and GQA are often combined since they address different bottlenecks (attention pattern vs. cache size). [Sebastian Raschka: Visual Guide]

## KV Cache: Why It Matters for Inference

During autoregressive decoding, generating each new token requires attending over all previous tokens. Without caching, this means recomputing K and V for every prior token at every step — O(n²) total work. The KV cache stores computed K and V tensors for previously seen tokens. On each new step, only the new token's K/V are computed; prior values are retrieved from cache.

The catch: cache size grows as `O(n · d · num_kv_heads · num_layers)` per sequence. At long contexts (100K+ tokens) with large models, this can exceed available GPU memory. GQA, MQA, and MLA all exist primarily to shrink this footprint. [Sebastian Raschka: KV Cache]

## FlashAttention: Memory-Efficient Training

Standard attention materializes the full N×N attention matrix in HBM (GPU high-bandwidth memory) — O(n²·d) reads/writes. FlashAttention (Dao et al., 2022) reframes this as an IO problem: the bottleneck is data movement between HBM and on-chip SRAM, not FLOPs.

**Core technique:** Tile Q, K, V into blocks that fit in SRAM. Process tiles sequentially, accumulating partial results and recomputing per-block softmax normalization on the fly (online softmax with streaming max/sum updates). Never materialize the full N×N matrix. IO complexity drops from O(n²) to O(n·d) — provably optimal for typical SRAM sizes.

**FlashAttention versions:**
- **v1:** Fused CUDA kernel combining QK^T, masking, softmax, dropout, and output multiply. 3× speedup over PyTorch on GPT-2 (seq=1K); enables contexts up to 64K.
- **v2:** Added parallelism over sequence length (not just batch/heads), reduced non-matmul FLOPs by delaying softmax scaling. 2× speedup over v1; 225 TFLOPs/s at 72% utilization on A100.
- **v3:** Targets Hopper (H100) GPUs. Uses warp specialization + ping-pong scheduling to overlap GEMM and softmax. Adds FP8 block quantization with incoherent processing (2.6× lower RMSE than baseline FP8). 1.5–2× over v2; ~740 TFLOPs/s in FP16, ~1.2 PFLOPs/s in FP8.

All versions compute exact attention (no approximation). FlashAttention 2 is the stable default for Ampere GPUs; v3 for H100s with FP8. [Aman AI: FlashAttention]

## Transformers in Recommendation Systems

The self-attention mechanism's ability to capture long-range dependencies in sequences maps naturally onto user behavior modeling.

**Sequential recommendation:** User action histories are treated as sequences. The transformer attends over the full action history to build a context-aware user representation, unlike fixed-length pooling approaches.

**SASRec / BST:** SASRec (Self-Attentive Sequential Recommendation) applies a causally-masked transformer decoder to item sequences, predicting the next interaction. BST (Behavior Sequence Transformer, Alibaba) applies transformer encoding over user behavior sequences for CTR prediction.

**Pinterest examples:**
- **PinnerFormer:** A transformer over user action sequences (pin saves, clicks, etc.), each action encoded with PinSage embedding + metadata (action type, surface, timestamp as sin/cos features). Uses a dense all-action loss — predicts engagement over a 14-day window rather than just the next action, bridging batch and real-time inference. Significantly improved homefeed engagement and DAU/WAU. [Aman AI: Recsys Transformers]
- **ItemSage:** Transformer encoder that aggregates text and image features for product embeddings. A 1-layer transformer block over 32 feature embeddings via a [CLS] token, producing 256-dim embeddings compatible with PinSage and SearchSage for ANN retrieval. Multi-task training across purchases, add-to-cart, saves, and clicks.

The cross-domain pattern: transformers in recsys are typically used for user representation (encoding action sequences) or item representation (encoding multimodal features), then plugged into standard candidate generation or ranking pipelines. See [[hard/wiki/recommendation-systems|Recommendation Systems]] for the broader retrieval and ranking context.

## Scaling Laws and Emergent Capabilities

Transformer performance on language modeling follows predictable power laws in compute, data, and parameter count (Chinchilla scaling laws). Key finding: for a fixed compute budget, optimal training balances model size and data volume roughly equally. Emergent capabilities — behaviors that appear abruptly at scale thresholds — include multi-step reasoning, few-shot learning, and instruction following. These are not explicitly trained; they arise from scale. The mechanisms are not fully understood but are empirically robust across architectures.

## Quick-Reference: Architecture Choices in Modern LLMs

| Model | Attention | Positional Encoding | Flash Attn |
|-------|-----------|---------------------|------------|
| GPT-2 | MHA | Learned | No |
| PaLM (2022) | MQA | RoPE | Standard |
| Llama 2 70B | GQA | RoPE | v2 |
| Mistral 7B | GQA + SWA | RoPE | v2 |
| Llama 3 | GQA | RoPE (base 500K) | v2 |
| DeepSeek V2/V3 | MLA | RoPE | v2 |
| Gemma 3 | GQA + SWA | RoPE (base 1M) | v2 |

## Sources

- Vaswani et al. (2017) — "Attention Is All You Need"
- Ainslie et al. (2023) — "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
- DeepSeek-V2 paper (2024) — MLA introduction and ablations
- Dao et al. (2022, 2023, 2024) — FlashAttention v1/v2/v3
- Su et al. (2024) — "RoFormer: Enhanced Transformer with Rotary Position Embedding"
- [Lilian Weng: The Transformer Family v2.0](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/)
- [Sebastian Raschka: A Visual Guide to Attention Variants in Modern LLMs](https://magazine.sebastianraschka.com/p/visual-attention-variants)
- [Sebastian Raschka: Understanding and Coding the KV Cache in LLMs from Scratch](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)
- [Louis Wang: The Attention Bottleneck](kb/hard/raw/louis-wang/the-attention-bottleneck-how-modern-llms-solved-a-problem-that-nearly-broke-the.md)
- [Cameron Wolfe: GPT-oss From the Ground Up](kb/hard/raw/cameron-wolfe/gpt-oss-from-the-ground-up.md)
- [Aman AI: FlashAttention Primer](https://aman.ai/primers/ai/flashattention/)
- [Aman AI: NLP Attention](https://aman.ai/primers/ai/attention/)
- [Aman AI: Recsys Transformers](https://aman.ai/recsys/transformer/)
