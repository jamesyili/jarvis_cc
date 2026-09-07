---
concept: Transfer Learning & Fine-Tuning
tags: [transfer-learning, fine-tuning, lora, peft, domain-adaptation]
sources:
  - kb/hard/raw/aman-ai/primers-fine-tuning-models.md
  - kb/hard/raw/aman-ai/primers-parameter-efficient-fine-tuning.md
  - kb/hard/raw/aman-ai/primers-transferability-estimation.md
last_compiled: 2026-04-05
related: [large-language-models, rl-for-llms]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Transfer Learning & Fine-Tuning

Transfer learning is the practice of leveraging knowledge acquired during training on a large source task to improve performance on a smaller target task. It is the dominant paradigm in modern deep learning: the marginal cost of a new capability is not training from scratch, but adapting an already-capable model. Fine-tuning is the mechanism by which this adaptation happens; parameter-efficient fine-tuning (PEFT) is the set of techniques that makes it tractable.

## The Pretraining / Fine-Tuning Paradigm

**Why transfer?** Training a deep network from scratch on a small dataset leads to overfitting — the model has millions of parameters but only thousands of labeled examples. A network pretrained on a large, diverse dataset (ImageNet for vision; a web-scale text corpus for language) has already learned general-purpose representations: edges and textures in early vision layers, syntactic and semantic structure in early transformer layers. Fine-tuning reuses these representations rather than re-learning them.

**When to fine-tune vs. train from scratch:**
- Fine-tune if your target domain is not radically different from the pretraining domain (e.g., medical images using ImageNet features; domain-specific NLP on a general LLM)
- Train from scratch if your domain is highly specialized and no relevant pretrained model exists
- Use feature extraction (no fine-tuning at all) if your labeled dataset is very small and the target domain closely matches the source domain

**Layer freezing heuristic:** Early layers learn universal features (edges, basic syntax); later layers learn task-specific features. When fine-tuning:
- Freeze early layers (preserve universal features)
- Fine-tune later layers (adapt task-specific representations)
- Always replace the final classification head with one sized for the target task

**Learning rate:** Use a learning rate 10× smaller than the scratch training rate. Large learning rates destroy the pretrained weights before the model has adapted.

## Transferability Estimation

When multiple pretrained models are available and retraining all of them is expensive, transferability estimation helps select the best source model without fine-tuning.

**LEEP (Log Expected Empirical Prediction):** Run the source model on target data to get predicted label distributions, then measure how well these distributions predict target labels via log-likelihood. Correlation with final fine-tuned accuracy is typically >0.94. Fast: requires only one inference pass.

**OTDD (Optimal Transport Dataset Distance):** Computes the Wasserstein distance between source and target datasets based on feature-label pair distributions. Does not require training a model. Drawback: computationally expensive due to Wasserstein distance approximation; correlation with transfer performance is more variable (~0.85).

**Practical takeaway:** LEEP is the better default for selecting among pretrained checkpoints. OTDD is useful when you want a model-free distance measure between datasets.

## Full Fine-Tuning vs. PEFT

Full fine-tuning updates every parameter in the model. For a 7B-parameter LLM, this means storing and updating 7B weights + 7B gradients + 14B Adam optimizer states ≈ 112 GB in FP32. This is infeasible on consumer hardware and slow even on data center hardware.

**PEFT (Parameter-Efficient Fine-Tuning)** freezes most of the pretrained model and trains only a small number of additional parameters. Key benefits:
- Dramatically lower memory footprint (only small adapter parameters need gradients and optimizer states)
- Faster training
- Reduced overfitting (fewer free parameters)
- Avoids **catastrophic forgetting** — because the original weights are frozen, the model retains its general capabilities while adapting to the new task
- Multi-task deployment: one frozen base model, multiple small task-specific adapters

## PEFT Methods

### Adapter Modules

Adapters insert small bottleneck modules between existing transformer layers. Each adapter module:
1. Projects from dimension d to bottleneck dimension m (`d×m` parameters)
2. Applies a non-linearity
3. Projects back from m to d (`m×d` parameters)
4. Adds a residual connection

Total parameters per adapter: `2dm`. With `d=1024` and `m=24`, this is 49,152 parameters vs. 1,048,576 for a full `d×d` layer — a 21× reduction. The skip connection with near-zero initialization ensures stable fine-tuning (the adapter starts as a near-identity function and diverges gradually).

Only adapter parameters are updated during training; the original model remains frozen.

### Prompt Tuning and Prefix Tuning

**Soft prompt tuning:** Prepend a small set of trainable "soft prompt" tokens to the input embeddings. The model's weights are frozen; only these embedding vectors are learned. Enables a single frozen model to serve multiple tasks (different soft prompts per task). Scales well: at T5-XXL scale, a soft prompt of 5 tokens needs 20,480 parameters vs. 11 billion for a full model copy.

**Prefix tuning:** Extends soft prompt tuning to all transformer layers. Instead of prepending trainable tokens only to the input, prepend trainable prefix vectors to the key and value matrices in every attention layer. Subsequent tokens attend to the prefix as if it were part of the context. By learning 0.1% of parameters, prefix tuning matches full fine-tuning in the full-data regime and outperforms it in low-data settings.

**Hard prompt tuning:** Manual modification of the input text string. No gradient-based optimization. Useful for zero-shot and few-shot in-context learning but cannot match fine-tuned performance for specialized tasks.

### LoRA (Low-Rank Adaptation)

LoRA is the dominant PEFT technique for LLM fine-tuning. The key insight: pretrained weight updates during fine-tuning tend to have low intrinsic rank — the useful signal lives in a low-dimensional subspace of the full weight space.

**Mechanism:** For a weight matrix `W ∈ R^(d×k)`, instead of updating W directly, parameterize the update as a product of two low-rank matrices:

```
W' = W + ΔW = W + B·A
```

where `A ∈ R^(r×k)` and `B ∈ R^(d×r)` with rank `r ≪ min(d, k)`. Only A and B are trained; W is frozen.

**Initialization:** A is initialized with a Gaussian; B is initialized to zero. This ensures `ΔW = B·A = 0` at initialization, preserving the original model's behavior at the start of training.

**Scaling:** The update is scaled by `α/r` where α is a hyperparameter. Setting `α = r` is a common default that gives the effective learning rate a stable interpretation across rank values.

**No inference latency:** After training, the LoRA update can be merged: `W' = W + B·A`. The merged model is identical in architecture to the original and runs at full speed. During serving, adapters can also remain unmerged to enable hot-swapping between tasks.

**Parameter count:** For a `d×k` attention weight matrix with rank `r`, LoRA introduces `r(d+k)` parameters vs. `dk` for full fine-tuning. With `r=8` and typical transformer dimensions, LoRA trains ~0.1–1% of total parameters.

**Hyperparameters:**
| Hyperparameter | Typical Range | Notes |
|---|---|---|
| Rank `r` | 4–64 | Higher = more capacity but more overfitting risk |
| Alpha `α` | Equal to r or 2r | Controls effective learning rate |
| Dropout `p` | 0.05–0.1 | Applied to LoRA inputs |
| Learning rate | 1e-4 to 3e-4 | Higher than full fine-tuning |
| Which matrices | Query, Value | Key and FFN sometimes included |

**Regularization effect:** The low-rank constraint limits the effective complexity of the weight update. Lower layers, which are more general, are affected less than higher layers, which are more task-specific — LoRA naturally concentrates adaptation in task-relevant dimensions.

**Catastrophic forgetting:** LoRA largely avoids it because W is frozen. The original capabilities are preserved; only the additive adapter ΔW changes.

### QLoRA

QLoRA combines 4-bit quantization of the base model with LoRA adapters trained in BF16. The base model is loaded in 4-bit NF4 (Normal Float 4) quantization — a data type optimized for normally-distributed weight values. LoRA adapters are stored and computed in BF16.

**Memory impact:** A 65B model in FP16 requires ~130GB. With QLoRA, it fits on ~48GB — enabling fine-tuning on 2–4 consumer GPUs.

**Key components:**
- NF4 quantization (information-theoretically optimal for normal distributions)
- Double quantization (quantize the quantization constants themselves)
- Paged optimizer states (spill to CPU RAM when GPU memory is under pressure)

**Practical note:** QLoRA performance is typically 1–2% below full-precision LoRA. The gap narrows with more fine-tuning data. For most practical tasks, QLoRA achieves comparable results to full fine-tuning of smaller models.

## Choosing a PEFT Method

| Method | Memory | Performance | Inference Cost | Best For |
|---|---|---|---|---|
| Full fine-tuning | Very high | Highest | Same | Large data, ample compute |
| Adapter | Low | Near-full FT | Slight overhead | Multi-task serving |
| Soft Prompt | Very low | Good at scale | None | Multi-task, frozen model |
| Prefix Tuning | Low | Near-full FT | None | Generation tasks |
| LoRA | Low | Near-full FT | None (mergeable) | Standard LLM fine-tuning |
| QLoRA | Very low | Near-LoRA | None (mergeable) | Consumer GPU fine-tuning |

**Default recommendation:** LoRA for any LLM fine-tuning task where you have access to a 16-bit GPU. QLoRA when GPU memory is severely constrained. Full fine-tuning only when you have the infrastructure and the task demands it (e.g., RLHF reward model training).

## Sources

- Aman AI, "Primers: Fine-tuning Models" — `kb/hard/raw/aman-ai/primers-fine-tuning-models.md`
- Aman AI, "Primers: Parameter Efficient Fine-Tuning" — `kb/hard/raw/aman-ai/primers-parameter-efficient-fine-tuning.md`
- Aman AI, "Primers: Transferability Estimation" — `kb/hard/raw/aman-ai/primers-transferability-estimation.md`
