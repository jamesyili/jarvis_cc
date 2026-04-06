---
concept: Distributed Training & Memory Optimization
tags: [distributed-training, parallelism, deepspeed, gradient-checkpointing, mixed-precision]
sources:
  - kb/hard/raw/aman-ai/primers-distributed-training-parallelism.md
  - kb/hard/raw/aman-ai/primers-distributed-training.md
  - kb/hard/raw/aman-ai/gradient-accumulation-and-checkpointing.md
last_compiled: 2026-04-05
related: [large-language-models, neural-network-training]
---

# Distributed Training & Memory Optimization

Training large models requires distributing computation across multiple GPUs or machines. The challenge is not just throughput — it is also memory. A 70B-parameter model in FP32 requires ~280GB of VRAM just for weights, before accounting for gradients, optimizer states, and activations. Understanding the parallelism strategies and memory optimization techniques is essential for anyone training or fine-tuning large-scale models.

## The Memory Problem

A GPU running a training job must hold:
1. **Model weights:** Parameters themselves
2. **Gradients:** One gradient tensor per parameter
3. **Optimizer states:** Adam stores two additional tensors per parameter (first and second moments)
4. **Activations:** All intermediate outputs needed for the backward pass

For a model with N parameters in FP32:
- Weights: 4N bytes
- Gradients: 4N bytes
- Adam optimizer states: 8N bytes
- Total (excluding activations): ~16N bytes = ~16 GB per billion parameters

This is why even a 7B-parameter model requires ~112GB baseline — far beyond a single A100 (80GB).

## Parallelism Strategies

### Data Parallelism

**Concept:** Each GPU holds a complete copy of the model and processes a different mini-batch of data. After the backward pass, gradients are averaged across all GPUs before the optimizer step.

**DataParallel (DP) — single-machine legacy:**
- One process coordinates all GPUs on a single machine
- The primary GPU handles all gradient aggregation and optimization
- Bottleneck: primary GPU holds all memory and orchestrates communication
- Use only for single-machine setups; DDP is preferred in all modern contexts

**Distributed Data Parallel (DDP) — standard:**
- Each GPU runs in its own process with a complete model copy
- Gradients are synchronized via all-reduce (ring-based) after each backward pass
- All processes update their weights identically → models remain synchronized without a coordinator
- Scales efficiently to multi-node setups
- Limitation: the full model must fit on each individual GPU

### Model Parallelism

**Concept:** When a model is too large for a single GPU, split it across multiple GPUs. Different GPUs hold different parameters.

**Layer-wise (naive model parallelism):**
- Assign different layers to different GPUs
- Forward pass moves activations sequentially from GPU to GPU
- Problem: only one GPU is active at a time (pipeline bubble = high idle time)

**Tensor parallelism:**
- Split individual weight matrices across GPUs (e.g., split attention heads)
- All GPUs work simultaneously on different parts of the same layer
- Requires frequent inter-GPU communication within each layer
- Used by Megatron-LM for large-scale transformer training

**Pipeline parallelism:**
- Assign groups of consecutive layers to different GPUs
- Overlap computation with communication using microbatches
- Reduces idle time compared to naive layer-wise parallelism
- GPipe, PipeDream are standard implementations

### Hybrid / FSDP

**Fully Sharded Data Parallel (FSDP):**
- PyTorch's implementation of ZeRO-3 (see below)
- Shards model parameters, gradients, and optimizer states across all GPUs
- Parameters are gathered (via all-gather) before each layer's computation, then discarded
- Combines the throughput benefits of data parallelism with the memory efficiency of model parallelism
- Standard for fine-tuning large models in practice (70B+ on 8x80GB A100s)

**Choosing the right strategy:**

| Strategy | Model fits per GPU? | Scales to N GPUs? | Communication |
|---|---|---|---|
| DDP | Yes | Yes | Gradient sync (post-backward) |
| Model Parallelism | No | Yes (bounded) | Per-layer activation transfer |
| Pipeline Parallelism | No | Yes | Stage output transfer |
| Tensor Parallelism | No | Yes (bounded) | Per-operation |
| FSDP | No | Yes | Parameter gather + gradient scatter |

## ZeRO: Zero Redundancy Optimizer

DeepSpeed's ZeRO (Zero Redundancy Optimizer) eliminates memory redundancy across data-parallel workers by partitioning the memory footprint:

**ZeRO Stage 1:** Partition optimizer states only across GPUs. Each GPU holds 1/N of the optimizer states. Reduces optimizer memory by N×.

**ZeRO Stage 2:** Partition optimizer states + gradients. After each GPU computes its gradients, it retains only its assigned shard; others are discarded. Reduces gradient memory by N× on top of Stage 1.

**ZeRO Stage 3:** Partition optimizer states + gradients + model parameters. All parameters are sharded; each GPU holds 1/N of the model. This is equivalent to FSDP — full memory reduction but with more communication overhead. Enables training models with trillions of parameters.

**ZeRO-Infinity / ZeRO-Offload:** Extends ZeRO to offload optimizer states (and optionally parameters) to CPU RAM or NVMe SSD, enabling much larger models on GPU-constrained hardware at the cost of CPU↔GPU bandwidth.

**DeepSpeed** is the library implementing ZeRO alongside additional optimizations: mixed precision, gradient clipping, learning rate scheduling, and integration with model and pipeline parallelism. It wraps PyTorch and plugs into Hugging Face Trainer.

## Memory Optimization Techniques

### Gradient Accumulation

Gradient accumulation simulates a larger effective batch size when GPU memory cannot fit the desired batch. Instead of updating weights after each mini-batch, gradients are summed over `k` mini-batches before the optimizer step:

```python
for i in range(num_iterations):
    accumulated_grads = 0
    for j in range(accumulation_steps):
        batch = next(training_data)
        grads = compute_gradients(batch)
        accumulated_grads += grads
    update_weights(accumulated_grads)
```

**Effect:** Effective batch size = actual batch size × accumulation steps. Memory usage is determined by the actual batch size, not the effective one.

**Tradeoff:** Slower convergence per wall-clock time (more forward/backward passes per optimizer step). Particularly valuable for contrastive learning where large effective batch sizes improve representation quality.

**Practical numbers (Hugging Face benchmark):** Adding gradient accumulation (4 steps, batch size 1) reduces GPU memory from 14.9 GB to 8.7 GB, at the cost of ~15% slower throughput.

### Gradient Checkpointing

During standard backpropagation, all layer activations from the forward pass are stored (to use in gradient computation during the backward pass). For a 100-layer model, this is massive.

Gradient checkpointing stores only a subset of activations (the "checkpoints") and recomputes the rest on-demand during the backward pass.

**Tradeoff:** Reduces activation memory by approximately `O(√N)` for N layers, at the cost of ~20% increase in training time (one additional forward pass per checkpointed segment).

**When to use:** When you are memory-bound but not compute-bound. Almost always worth enabling for large models.

**Combined example:** Adding gradient checkpointing on top of gradient accumulation (from 8.7 GB) further reduces memory to 6.8 GB, but increases training time by ~20%.

### Mixed Precision Training

Stores weights and activations in FP16 (or BF16) but performs optimizer updates in FP32. FP16 reduces memory by 2× and often doubles throughput on modern GPUs (Tensor Cores are optimized for FP16/BF16).

**BF16 vs FP16:** BF16 has the same exponent range as FP32 (more numerically stable, less likely to overflow/underflow) but fewer mantissa bits (less precise). BF16 is preferred for LLM training on A100/H100 hardware.

### Quantization (4-bit / 8-bit)

QLoRA loads base model weights in 4-bit NF4 (Normal Float 4) quantization, reducing memory by ~4× versus FP16. Adapter weights (LoRA) are trained in BF16. Combined with FSDP, this enables training a 70B model on 2× consumer RTX 4090 GPUs (24GB each).

## Practical Guidance

**For fine-tuning a 7B model on a single 80GB A100:**
- Use DDP or FSDP (single GPU = no parallelism needed, but FSDP can still help via offloading)
- Enable gradient checkpointing
- Use BF16 mixed precision
- Use LoRA to reduce trainable parameters (see [[hard/wiki/transfer-learning|Transfer Learning & Fine-Tuning]])

**For training a 70B model on 8× A100 80GB:**
- Use FSDP (ZeRO-3) or DeepSpeed ZeRO-3
- BF16 mixed precision
- Gradient checkpointing
- Batch size 1 per GPU with gradient accumulation

**For training a 70B model on consumer hardware (2× RTX 4090):**
- FSDP + QLoRA (4-bit quantization)
- Gradient checkpointing + accumulation
- See Answer.AI's open-source FSDP+QLoRA system

## Sources

- Aman AI, "Primers: Distributed Training Parallelism" — `kb/hard/raw/aman-ai/primers-distributed-training-parallelism.md`
- Aman AI, "Primers: Distributed Training" — `kb/hard/raw/aman-ai/primers-distributed-training.md`
- Aman AI, "Gradient Accumulation and Checkpointing" — `kb/hard/raw/aman-ai/gradient-accumulation-and-checkpointing.md`
