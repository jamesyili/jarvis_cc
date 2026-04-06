---
concept: Model Compression & Quantization
tags: [quantization, pruning, distillation, model-compression, on-device]
sources:
  - kb/hard/raw/aman-ai/primers-quantization.md
  - kb/hard/raw/aman-ai/primers-model-compression-for-on-device-ai.md
  - kb/hard/raw/aman-ai/primers-model-acceleration.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/llm-inference-serving|LLM Inference & Serving]]"
  - "[[hard/wiki/large-language-models|Large Language Models]]"
---

# Model Compression & Quantization

A 70B-parameter model in float32 requires ~280 GB of memory — well beyond any single consumer GPU. Model compression converts large trained models into smaller, faster variants that can run in constrained environments: edge devices, mobile phones, single GPUs, or latency-critical inference servers. The four core techniques are quantization, pruning, knowledge distillation, and low-rank decomposition. In production, these are typically combined.

## Why Compression Is Necessary

Modern frontier models contain 100B to 1T parameters. At 4 bytes per float32 parameter, the memory footprint ranges from 400 GB to over 4 TB. Even at float16 (2 bytes), a 70B model requires 140 GB. Consumer GPUs top out at 24–80 GB. On-device deployment on mobile chips is orders of magnitude more constrained.

Compression enables: on-device inference (privacy, latency, no network dependency), lower serving cost (more requests per GPU-hour), and accessible fine-tuning (QLoRA lets you fine-tune a 65B model on a 48 GB GPU). The trade-off space is always accuracy vs. size vs. inference speed.

## Quantization

Quantization reduces the numerical precision of weights and/or activations. The standard flow: train in float32, then reduce to float16, int8, or int4 for deployment.

### Floating-Point Formats

Understanding the precision hierarchy is prerequisite to understanding quantization:

- **float32** (32 bits): 1 sign, 8 exponent, 23 mantissa. Default training format. Supports range ~10⁻⁴⁵ to 10³⁸.
- **bfloat16** (16 bits): 1 sign, 8 exponent, 7 mantissa. Same dynamic range as float32, but lower precision. Preferred for training — avoids overflow. Native on TPUs, A100/H100.
- **float16** (16 bits): 1 sign, 5 exponent, 10 mantissa. Narrower range (~10⁻⁵ to 10⁴). Risk of overflow in training; fine for inference.
- **int8** (8 bits): Integer representation. Requires scale + zero-point to map floats to integers. Supported by Tensor Cores on Turing+ GPUs with high throughput.
- **int4/int3** (4–3 bits): Extreme compression; quality degrades fast without calibration.

### Integer Quantization Mechanics

Integer quantization maps float values to integers using two parameters:

```
# Quantize float → int
q = round(x / scale) + zero_point

# Dequantize int → float
x = scale * (q - zero_point)
```

**AbsMax (symmetric)**: scale = max(|x|) / 127. Zero-point is always 0. Simple; works when distributions are symmetric around zero.

**ZeroPoint (asymmetric)**: scale = (max - min) / 255; zero-point shifts the range. More accurate for asymmetric distributions like post-ReLU activations.

### Post-Training Quantization (PTQ) vs. QAT

**PTQ** applies quantization after training with no weight updates. Fast to apply; quality depends on calibration. Works well at int8 for most models. At int4, naive PTQ causes significant accuracy loss.

**QAT (Quantization-Aware Training)** simulates quantization noise during training using fake quantize operations — weights appear to be quantized in the forward pass but float gradients flow in the backward pass. The model learns to be robust to quantization error. Best accuracy at int4 or lower, but requires a full training run.

**Dynamic quantization** quantizes weights statically but activations at runtime based on their observed range. No calibration dataset needed; lower overhead.

### Modern PTQ Techniques for LLMs

Standard PTQ at int4 degrades LLM quality substantially. Several techniques improve on it:

**GPTQ**: Uses second-order Hessian information to compensate for quantization error, layer by layer. Enables 4-bit quantization of 70B+ models with <1% perplexity degradation. Widely used for offline weight-only quantization.

**AWQ (Activation-Aware Weight Quantization)**: Observes that only ~1% of weights are "salient" — they correspond to activation channels with large magnitudes. AWQ protects these salient weights by scaling them up before quantization (and scaling down corresponding activations), so precision is preserved where it matters most. Result: better quality than GPTQ at equivalent bit-width, without needing to update weights.

**SmoothQuant**: Quantizing activations (not just weights) is harder because activation outliers are extreme and shift per-input. SmoothQuant migrates quantization difficulty from activations to weights by multiplying a per-channel smoothing factor s into the weights and dividing it out of the activations before quantization. Enables W8A8 (8-bit weights + 8-bit activations) quantization with near-lossless quality — important for throughput since int8 activations unlock faster matrix multiplications.

**GGUF**: File format for quantized models running on CPU/GPU via llama.cpp. Supports a spectrum from Q2_K (extreme compression, rough quality) through Q4_K_M and Q5_K_M (practical balance) to Q8_0 (near-lossless). K-quants use mixed precision — more sensitive layers get higher bit-width. Imatrix (importance matrix) calibrates which weights most affect model behavior. The practical format for local model deployment.

### Quantization Decision Guide

| Scenario | Recommended |
|----------|-------------|
| Production server, quality-critical | float16 or int8 with SmoothQuant |
| Local GPU inference, 7B–70B | GGUF Q4_K_M or AWQ 4-bit |
| On-device mobile | int4 or int3 with QAT |
| Fine-tuning large model on single GPU | QLoRA (4-bit base + float16 adapters) |
| Exact throughput maximization | W8A8 with SmoothQuant + TensorRT |

## Pruning

Pruning removes weights from a trained network. The hypothesis: neural networks are overparameterized; many weights contribute negligibly to the output and can be zeroed or deleted.

**Unstructured pruning** removes individual weights with smallest magnitude (L1/L2 norm) or smallest impact on loss (gradient-based saliency). Achieves high sparsity ratios (50–90%) but produces irregular sparse tensors that are difficult to accelerate — standard GPU hardware doesn't exploit unstructured sparsity well without specialized sparse kernels (NVIDIA 2:4 structured sparsity is an exception).

**Structured pruning** removes entire neurons, attention heads, or layers. The resulting model is dense and directly runs faster on standard hardware without special kernels. Examples: pruning low-magnitude attention heads (some models have redundant heads that can be removed with <1% quality loss); pruning transformer layers in models that have more depth than needed for a specific task.

**Iterative pruning + fine-tuning** is the standard workflow: (1) train full model, (2) identify and remove the bottom-p% of weights by a criterion, (3) fine-tune the pruned model to recover performance, (4) repeat. Single-shot aggressive pruning degrades quality far more than gradual iterative pruning.

Practical ceiling: unstructured pruning can reach 80%+ sparsity on medium-sized models with minimal accuracy loss. Structured pruning is more limited — removing 20–30% of heads or layers typically requires careful selection and fine-tuning to stay within 1–2% accuracy degradation.

## Knowledge Distillation

Knowledge distillation trains a small **student model** to mimic a large **teacher model**, transferring knowledge without transferring parameters. The student learns to match the teacher's output distribution — not just the hard labels — which provides a richer training signal.

**Response-based distillation**: Match the teacher's output logits (soft probabilities over all classes/tokens). The temperature parameter T scales the softmax: high T creates a softer distribution that reveals the teacher's relative confidences across classes. This soft target carries more information than the one-hot hard label (e.g., the model is 60% confident in "cat" and 30% confident in "tiger" — that "near-miss" signal trains the student on similarity structure).

```
loss = α * CE(student_logits, hard_labels) + (1-α) * KL(softmax(student/T) || softmax(teacher/T)) * T²
```

**Feature-based distillation**: Align intermediate layer representations between teacher and student, not just the final output. Forces the student to develop similar internal representations. Common in DistilBERT, TinyBERT.

**Relation-based distillation**: Preserve relationships between examples (e.g., attention maps, pairwise distances in embedding space), not just per-example outputs.

**Distillation modes**:
- *Offline*: Teacher is frozen and pre-generates predictions; student trains against these. Simple and cheap.
- *Online*: Teacher and student train simultaneously; more complex but can improve student quality.
- *Self-distillation*: A model distills into itself across epochs or uses its own earlier checkpoint as teacher.

**Why distillation works better than training the student from scratch**: The teacher's soft outputs contain information about the data manifold that hard labels discard. The class probability distribution encodes which mistakes are reasonable vs. egregious — a kind of dark knowledge about the structure of the problem. Students trained via distillation converge faster and generalize better with the same data and architecture budget.

Production examples: DistilBERT (40% smaller than BERT-base, 60% faster, 97% of BERT's NLU performance); GPT-3's soft outputs used to train smaller open models; Claude's RLHF training involves distillation-like components where the policy learns from larger reference signals.

## Low-Rank Decomposition

Large weight matrices can often be approximated by the product of two smaller matrices:

```
W (N×N) ≈ U (N×k) @ V (k×N),  where k << N
```

This reduces storage from O(N²) to O(N·k) and reduces matrix multiply FLOPs proportionally. SVD (singular value decomposition) gives the optimal rank-k approximation by keeping the top-k singular values; CP decomposition is used for tensors.

In practice, fine-tuning after decomposition is essential — the approximation introduces error that can be partially recovered. Low-rank decomposition is less commonly used standalone for LLMs (quantization and distillation tend to be more practical), but it's the theoretical basis for LoRA and QLoRA fine-tuning, where the adaptation is parameterized as low-rank updates rather than full-rank weight changes.

**QLoRA** (Dettmers et al. 2023): Combines 4-bit quantization of the base model with float16 low-rank adapters. The base model weights are frozen in 4-bit (using NF4, a float-like 4-bit format optimized for normally distributed weights). Only the small LoRA adapter matrices (~0.1% of parameters) are trained in float16. Result: fine-tune a 65B model on a single 48 GB A100 with <1% quality loss versus full float16 fine-tuning.

## Combining Techniques

Production compression pipelines typically layer multiple techniques:

- **Distillation + quantization**: Distill a large model to a medium model, then quantize the medium model. Distillation enables a smaller architecture; quantization reduces the bit-width of what remains.
- **Pruning + quantization**: Prune redundant structures (attention heads, layers), then quantize remaining weights. Common in edge deployment pipelines.
- **QLoRA for fine-tuning, GGUF/AWQ for serving**: Fine-tune with QLoRA to produce float16 adapters, merge adapters, then quantize the merged model to GGUF or AWQ for deployment.

## Practical Trade-offs

| Technique | Size reduction | Speed gain | Quality risk | Best use case |
|-----------|---------------|------------|--------------|---------------|
| float16 | 2× | 1.5–2× | Negligible | Default inference |
| int8 (SmoothQuant) | 4× | 2–3× | <1% | Production servers |
| int4 (AWQ/GPTQ) | 8× | 3–4× | 1–3% | Local/edge, constrained GPU |
| Pruning 50% | 1.5–2× | Variable | 1–5% | Structured heads/layers |
| Distillation | 3–10× | 3–10× | 3–10% | When smaller architecture is acceptable |
| QLoRA | 8× (base) | Inference not improved | <1% | Fine-tuning, not deployment |

The general principle: quantization is the first tool to reach for (high compression, low quality cost, minimal effort). Distillation is highest leverage when you can afford to train from scratch. Pruning fills the gap when you need a dense model that is architecturally smaller.

## Sources

- Aman.ai: Primers — Quantization — AbsMax/ZeroPoint formulas, GPTQ, AWQ, SmoothQuant, GGUF, QAT vs PTQ, float/int format comparison
- Aman.ai: Primers — Model Compression for On-Device AI — quantization, knowledge distillation, pruning, low-rank decomposition, lightweight model design, QLoRA
- Aman.ai: Primers — Model Acceleration — FlashAttention, KV cache mechanics, speculative decoding, throughput vs latency trade-offs
