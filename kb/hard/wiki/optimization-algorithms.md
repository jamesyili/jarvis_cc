---
concept: Optimization Algorithms
tags: [optimization, sgd, adam, momentum, convergence]
sources:
  - kb/hard/raw/aman-ai/primers-gradient-descent-and-backprop.md
  - kb/hard/raw/aman-ai/cs229-linear-regression-and-gradient-descent.md
  - kb/hard/raw/aman-ai/coursera-dl-improving-deep-neural-networks-hyperparameter-tuning-regularization.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/neural-network-training|Neural Network Training]]"
  - "[[hard/wiki/neural-network-fundamentals|Neural Network Fundamentals]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Optimization Algorithms

Training a neural network is an optimization problem: find the parameters θ that minimize a loss function L(θ) over the training data. Gradient-based optimization is the universal approach — use the gradient ∇L(θ) to guide parameter updates. The challenge is doing this efficiently and stably across non-convex loss landscapes at scale.

## Gradient Descent

The foundational idea: move parameters in the direction of steepest descent.

`θ ← θ - α · ∇_θ L(θ)`

where α is the learning rate. For a loss surface visualized as a bowl, gradient descent follows the slope downhill toward the minimum.

**Batch Gradient Descent** computes the gradient over the entire training set before each update. Stable and consistent steps toward the minimum, but prohibitively expensive for large datasets — one gradient requires a full pass over the data.

**Stochastic Gradient Descent (SGD)** uses a single randomly sampled example per update. Computationally cheap (one update per example), but the gradient estimate is extremely noisy. The updates oscillate around the minimum rather than converging cleanly.

**Mini-batch Gradient Descent** is the practical compromise: compute the gradient on a mini-batch of 32–512 examples. This:
- Is computationally efficient (vectorized operations on GPU)
- Provides a lower-variance gradient estimate than single-sample SGD
- Introduces enough noise to escape sharp local minima (a form of implicit regularization)
- Enables progress without processing the full training set

In practice, "SGD" almost always means mini-batch SGD. Batch sizes are typically powers of 2 (64, 128, 256) for memory alignment efficiency.

### Convergence Behavior

- Batch GD: smooth, consistent progress
- SGD: noisy, oscillates, may never fully converge
- Mini-batch GD: noisy but trends downward; the cost function oscillates due to varying mini-batch difficulty

The learning rate α is the most critical hyperparameter:
- Too large: overshoots minima, diverges
- Too small: painfully slow convergence
- Just right: fast, stable convergence

## Momentum

Standard SGD wastes energy oscillating across "valleys" in the loss landscape — large updates in directions of high curvature, slow progress in directions of low curvature.

**Momentum** maintains a velocity vector `v` that accumulates gradient history. Each update adds a fraction of the previous velocity:

```
v_t = β · v_{t-1} + (1-β) · ∇L(θ)
θ ← θ - α · v_t
```

The momentum term β (typically 0.9) gives the update "inertia" — it dampens oscillations in high-curvature directions while accelerating progress in consistent directions. Analogy: a ball rolling down a hill gains speed on shallow slopes and doesn't bounce around narrow valleys.

With β = 0.9, the update effectively averages gradients over the last ~10 iterations, smoothing out noise.

## RMSprop

Momentum addresses oscillations but doesn't adapt the learning rate per-parameter. **RMSprop** divides each parameter update by the root mean square of its recent gradients:

```
S_{dW} = β · S_{dW} + (1-β) · dW²   (element-wise)
W ← W - α · dW / (√S_{dW} + ε)
```

**Intuition:** If a parameter has consistently large gradients (oscillates a lot), S_{dW} is large, and the effective learning rate for that parameter shrinks. If gradients are small and consistent, the learning rate stays high. This adapts the step size per dimension, enabling faster learning in flat directions and dampening oscillations in steep ones.

ε (typically 1e-8) prevents division by zero.

RMSprop was introduced not in a paper but in Geoffrey Hinton's Coursera course.

## Adam (Adaptive Moment Estimation)

**Adam** combines momentum (first moment) and RMSprop (second moment) — the most widely used optimizer in modern deep learning.

First moment (momentum):
`V_{dW} = β₁ · V_{dW} + (1-β₁) · dW`

Second moment (RMSprop):
`S_{dW} = β₂ · S_{dW} + (1-β₂) · dW²`

**Bias correction** compensates for initialization at zero (both V and S start at 0, biasing early estimates toward zero):
```
V̂_{dW} = V_{dW} / (1 - β₁^t)
Ŝ_{dW} = S_{dW} / (1 - β₂^t)
```

Parameter update:
`W ← W - α · V̂_{dW} / (√Ŝ_{dW} + ε)`

**Default hyperparameters:**
- β₁ = 0.9 (momentum decay)
- β₂ = 0.999 (RMSprop decay)
- ε = 1e-8
- α: task-specific, typically 3e-4 for transformers

Adam is robust across architectures and rarely needs hyperparameter tuning beyond learning rate. It adapts the effective learning rate per parameter, converges quickly on sparse gradients, and handles non-stationary objectives well.

## AdaGrad

**AdaGrad** accumulates all squared gradients from the beginning of training and divides updates by their square root:

`G_{dW} += dW²`
`W ← W - α · dW / (√G_{dW} + ε)`

**Strength**: excellent for sparse features — parameters that receive rare but large gradients get larger updates. Common in NLP applications with bag-of-words features.

**Weakness**: the accumulated sum grows monotonically, so the effective learning rate shrinks continuously and eventually becomes near zero. Training stalls for long training runs. RMSprop fixes this by using an exponentially decaying average instead of a cumulative sum.

## AdamW

**AdamW** decouples weight decay from the gradient update. In vanilla Adam, L2 regularization is applied by adding λW to the gradient before the update — but this means the regularization is scaled by the adaptive learning rate, which varies per parameter and over time. AdamW instead applies weight decay directly to the weights:

```
W ← W - α · [V̂_{dW} / (√Ŝ_{dW} + ε) + λ · W]
```

This is the correct way to apply weight decay with adaptive optimizers. AdamW is now the standard for training transformers (BERT, GPT, LLaMA all use it).

## Learning Rate Scheduling

The learning rate is rarely held constant throughout training. Common schedules:

**Step decay**: reduce α by a fixed factor every N epochs.

**Exponential decay**: `α = α₀ · 0.95^epoch`

**Cosine annealing**: smoothly decays α following a cosine curve from α_max to α_min over a training cycle. Can be combined with warm restarts (SGDR) to periodically reset α.

**Linear warmup + decay**: start with small α, linearly increase to α_max over the first few thousand steps, then decay. Standard for training large language models — warmup prevents early instability when model weights are random.

**Cyclic learning rates**: oscillate α between a min and max range, allowing the optimizer to escape sharp minima.

**The core intuition for scheduling**: large learning rates early in training enable fast exploration of the loss landscape; smaller rates near convergence enable fine-grained updates into the minimum.

## Convergence and Loss Landscapes

Neural network loss functions are **non-convex** — they have many local minima, saddle points, and flat regions. The intuition from older convex optimization doesn't fully apply:

- Most "bad" local minima are actually saddle points, not truly stuck
- Large neural networks tend to have many roughly equivalent quality minima
- Sharp minima generalize worse than flat minima — a flat basin means the model is less sensitive to small parameter perturbations

**Second-order methods** (Newton's method, L-BFGS) use the Hessian matrix to take curvature-aware steps. They converge faster in theory but are prohibitively expensive at scale — the Hessian of a 100M parameter model has 10^16 entries. In practice, first-order methods (Adam, SGD+momentum) dominate deep learning.

## Practical Optimizer Selection

| Scenario | Recommended |
|---|---|
| General deep learning | Adam or AdamW |
| Training transformers | AdamW with warmup + cosine decay |
| Fine-tuning LLMs | AdamW with small α |
| Computer vision (ResNets) | SGD + momentum (often edges out Adam) |
| Sparse NLP features | AdaGrad |
| Large batch training | LARS or LAMB (scale-aware variants) |

**Key insight**: SGD + momentum can outperform Adam on image classification tasks because Adam's adaptive learning rates can hurt generalization on well-conditioned problems. Adam tends to converge to sharper minima. For transformers with variable-scale gradients, Adam's adaptivity is essential.

---

## Sources

- Aman Chadha, "Primers: Gradient Descent and Backprop," aman.ai, 2026-04-05
- Aman Chadha, "CS229: Linear Regression and Gradient Descent," aman.ai, 2026-04-05
- Aman Chadha, "Coursera-DL: Improving Deep Neural Networks," aman.ai, 2026-04-05
