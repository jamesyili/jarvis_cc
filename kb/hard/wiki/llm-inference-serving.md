---
concept: LLM Inference & Serving
tags: [inference, kv-cache, speculative-decoding, quantization, serving]
sources:
  - kb/hard/raw/lilian-weng/large-transformer-model-inference-optimization.md
  - kb/hard/raw/sebastian-raschka/understanding-and-coding-the-kv-cache-in-llms-from-scratch.md
  - kb/hard/raw/aman-ai/primers-speculative-decoding.md
last_compiled: 2026-04-05
related: [distributed-training, model-compression, transformer-architecture]
---

# LLM Inference & Serving

LLM inference is fundamentally different from most ML serving tasks. Autoregressive generation is inherently sequential — each token depends on all previous tokens — which makes naive implementations memory-bandwidth-bound and compute-inefficient. The gap between theoretical GPU FLOPs and actual token generation throughput is often 10–100×. A suite of techniques — KV caching, speculative decoding, quantization, continuous batching, and FlashAttention — close this gap in production serving systems.

## Why Inference is Hard

Two core challenges (Pope et al. 2022):

1. **Memory-bandwidth bound, not compute-bound**: Generating one token requires loading the entire model from HBM to compute units. For a 70B model in FP16, that's 140GB of data movement *per token*. Modern A100s have ~2TB/s HBM bandwidth — meaning ~70ms of memory traffic per generation step before any actual computation. Compute utilization is typically only 5–20% for small-batch inference.

2. **Autoregressive bottleneck**: K tokens of output requires K sequential forward passes. Unlike prefill (processing the prompt), decode is strictly serial. You cannot parallelize across output tokens without fundamentally changing the algorithm.

## KV Cache

### The Problem

In transformer attention, each token attends to all previous tokens via key (K) and value (V) vectors. Without caching, generating token N requires recomputing K and V vectors for *all* N-1 previous tokens on every step. For a sequence of length 512 generating 200 tokens, that's ~200 × 512 = 102,400 redundant attention computations.

### The Solution

Cache the K and V tensors of all previously processed tokens. On each new step:
1. Compute K and V only for the *new* token.
2. Concatenate them to the cache.
3. Run attention using the full cached K/V (all past tokens) and the new query.

This reduces the decode computation per step from O(sequence_length) to O(1) (just the new token), at the cost of O(sequence_length × num_layers × hidden_dim) memory.

### Memory Cost

KV cache memory scales with:
- Batch size
- Sequence length (context window)
- Number of layers
- Model dimension

For a 70B model with 80 layers, 128 heads, and head dimension 128, the KV cache for a single sequence of 4096 tokens in FP16 is roughly:
```
2 (K+V) × 80 layers × 4096 tokens × 128 heads × 128 dim × 2 bytes ≈ 20GB
```

At batch size 16, this consumes 320GB — more than the model weights themselves. KV cache memory is a primary limiting factor on maximum batch size and context length in production.

### KV Cache Optimizations

**Multi-Query Attention (MQA)**: Share a single K and V head across all query heads. Reduces KV cache by `num_heads`×. Slight quality regression.

**Grouped-Query Attention (GQA)**: Share K and V within groups of query heads (intermediate between MHA and MQA). Mistral, Llama 2 70B+ use this. Reduces KV cache by `group_size`× with minimal quality loss.

**Multi-head Latent Attention (MLA)** (DeepSeek): Low-rank joint compression of K and V into a single latent vector. Dramatically reduces KV cache size (compression dimension 512 vs. full hidden dimension 7168 in DeepSeek-V3) while preserving expressive power.

**Paged KV Cache (vLLM)**: Manages KV cache memory in fixed-size "pages" rather than one contiguous allocation per sequence. Eliminates fragmentation, enables memory sharing across sequences with common prefixes, and supports much larger batch sizes.

## Speculative Decoding

Speculative decoding exploits the gap between the cost of *proposing* tokens (cheap) and *verifying* them (expensive) to generate multiple tokens per step without changing the output distribution.

### Draft-Model Approach (Leviathan et al. 2023)

1. A small, fast **draft model** autoregressively generates γ candidate tokens.
2. The large **target model** runs a single forward pass over the original context + γ draft tokens in parallel (one pass scores all γ+1 positions simultaneously due to attention masking).
3. Tokens are accepted greedily: if the target model agrees with the draft token, accept it. At the first mismatch, reject that token and sample the correction from the target model.
4. Repeat.

If acceptance rate is high (draft and target models are well-matched), 2–5 tokens are generated per forward pass of the target model rather than 1. Typical speedups: 2–3×. Crucially, the output distribution is **identical** to running the target model alone.

**Limitations**: Requires maintaining a separate draft model. Distribution mismatch between draft and target reduces acceptance rate. Both models must fit in memory simultaneously.

### Medusa (Cai et al. 2024)

Instead of a separate draft model, add multiple lightweight **speculative heads** to the main model — each predicts tokens 2, 3, 4, ... positions ahead from the current hidden state. A tree attention structure evaluates all candidate continuations in parallel. Acceptance schemes:
- **Rejection sampling**: preserves exact output distribution.
- **Typical acceptance**: heuristic, faster but slight distribution shift.

Speedup: 2.3–2.8× in practice. Single-model architecture simplifies deployment. Best for low-batch-size interactive settings.

### Multi-Token Prediction Heads (Gloeckle et al. 2024)

Train multiple output heads from scratch — each head predicts the token `i` positions ahead. The standard head predicts position 1; additional heads predict positions 2, 3, 4, etc. During inference, use all heads speculatively. No separate draft model needed. Speedup: 3× (4-token window) to 6× (8-token window). Requires modifying pretraining; quality benefits only materialize at 7B+ scale.

DeepSeek-V3 uses multi-token prediction (MTP with D=1) during training as a training signal and repurposes it for speculative decoding at inference, achieving 1.8× tokens-per-second improvement with 85–90% acceptance rate on the second predicted token.

## Quantization

Quantization reduces model weight (and sometimes activation) precision to use less memory and faster arithmetic:

| Precision | Memory (70B model) | Throughput | Quality |
|-----------|-------------------|------------|---------|
| FP32 | 280GB | Baseline | Full |
| BF16/FP16 | 140GB | ~2× | Minimal loss |
| INT8 | 70GB | ~2–4× | Small loss (<1%) |
| INT4 | 35GB | ~4–8× | Moderate loss (task-dependent) |
| FP8 | 70GB (like INT8) | ~2× | Very small loss |

**Post-training quantization (PTQ)**: quantize weights after training, no retraining. Simple to apply; some quality loss on INT4, acceptable on INT8 for most use cases.

**Quantization-aware training (QAT)**: simulate quantization noise during training or fine-tuning. Better quality at low precision but higher training cost.

**FP8 training and inference**: DeepSeek-V3 validated FP8 mixed-precision training at 671B scale, reducing memory usage and accelerating training while maintaining <0.25% relative loss error vs. BF16 baseline.

**Practical guidance**: 
- INT8 is nearly lossless for inference on most tasks.
- INT4 is acceptable for deployment where memory is the binding constraint; use GPTQ or AWQ for better INT4 quality.
- Use per-channel or per-group quantization (rather than per-tensor) to reduce outlier sensitivity.

## FlashAttention

Standard attention materializes the full N×N attention score matrix in HBM. For long sequences (N=8192+), this is both memory-intensive and slow. FlashAttention (Dao et al. 2022) reformulates attention computation to be *IO-aware*:

- Tiles the Q, K, V matrices into blocks that fit in fast SRAM (L2 cache).
- Computes attention in blocks, never materializing the full N×N matrix.
- Fuses all attention operations into a single kernel.

Result: attention memory scales O(N) instead of O(N²); attention computation is 2–4× faster on A100s. Now standard in virtually all production serving frameworks.

## Continuous Batching

Traditional batching processes all requests in a batch simultaneously, padding shorter requests to the longest. Continuous batching (vLLM, TGI) instead processes tokens from multiple requests in the same forward pass, with each request at a different generation position. New requests are inserted as running requests complete their generation. This dramatically improves GPU utilization (from ~20–40% to 70–90%) and reduces time-to-first-token for new requests.

## Model Parallelism for Serving

For models too large to fit on a single GPU:

**Tensor Parallelism (TP)**: split weight matrices across GPUs along one dimension. Each GPU computes a partial result, then an AllReduce synchronizes. Latency increases with GPU count due to AllReduce overhead but enables serving any model size.

**Pipeline Parallelism (PP)**: assign different layers to different GPUs. Reduces AllReduce overhead but introduces pipeline bubbles (idle time waiting for the previous stage).

**Expert Parallelism (EP)**: for MoE models, distribute different experts across GPUs. Tokens are routed to the appropriate device via all-to-all communication. Scales naturally with number of experts.

In practice, serving systems combine these strategies. DeepSeek-V3 uses 16-way PP + 64-way EP for training; serving configurations vary by hardware.

## Throughput vs. Latency Trade-off

The fundamental serving trade-off:
- **Higher batch size** → higher throughput (tokens/second/GPU), but higher latency per request.
- **Lower batch size** → lower latency (time-to-last-token), but lower GPU utilization.

For interactive applications (chatbots, copilots): optimize for latency, use small batches.
For batch workloads (offline document processing): optimize for throughput, use large batches.

Speculative decoding reduces latency for single requests. Continuous batching improves throughput in multi-tenant serving. These techniques are complementary.

## Sources

- Lilian Weng, "Large Transformer Model Inference Optimization" — `kb/hard/raw/lilian-weng/large-transformer-model-inference-optimization.md`
- Sebastian Raschka, "Understanding and Coding the KV Cache in LLMs from Scratch" — `kb/hard/raw/sebastian-raschka/understanding-and-coding-the-kv-cache-in-llms-from-scratch.md`
- Aman.ai, "Primers: Speculative Decoding" — `kb/hard/raw/aman-ai/primers-speculative-decoding.md`
