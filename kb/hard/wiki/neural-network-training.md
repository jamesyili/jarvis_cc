---
concept: Neural Network Training & Optimization
tags: [training, optimization, sgd, adam, learning-rate, debugging]
sources:
  - kb/hard/raw/karpathy/a-recipe-for-training-neural-networks.md
  - kb/hard/raw/aman-ai/coursera-dl-improving-deep-neural-networks-hyperparameter-tuning-regularization.md
  - kb/hard/raw/aman-ai/primers-gradient-descent-and-backprop.md
last_compiled: 2026-04-05
related: [neural-network-fundamentals, distributed-training, regularization]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Neural Network Training & Optimization

Training a neural network is not like using a standard software library. The abstraction leaks — backprop and SGD do not magically produce results, and failures are silent. A model that silently trains to mediocre performance because of a misconfiguration looks identical on the surface to one that is working correctly. The discipline of training is therefore as much about building trust in your setup as it is about tuning hyperparameters.

## The Training Recipe (Karpathy's Process)

The most robust approach to training a new model is to build complexity incrementally, never introducing multiple unknowns at once.

**1. Become one with the data.** Before writing model code, spend hours scanning thousands of examples. Look for duplicates, corrupted labels, class imbalances, and systematic biases. Understanding your data's distribution directly informs architecture choices and is the only reliable way to catch bugs introduced through preprocessing.

**2. Build a minimal skeleton first.** Start with the simplest possible model — a linear classifier, a tiny ConvNet. Verify the end-to-end pipeline:
- Fix a random seed for reproducibility.
- Verify loss at initialization. For a classifier with N classes, the initial softmax loss should be approximately `-log(1/N)`.
- Overfit a single batch of 2–5 examples to zero loss. If you cannot do this, there is a bug.
- Train an input-independent baseline (zero all inputs) — it should perform worse than the real model.
- Visualize data immediately before the forward pass (`y_hat = model(x)`) to confirm preprocessing is correct.

**3. Overfit, then regularize.** First get a model large enough to overfit the training set. Focus only on training loss. Once you have confirmed the model has sufficient capacity, layer in regularization (see [[hard/wiki/regularization|Regularization & Overfitting]]) to close the gap between training and validation loss.

**4. Tune, then squeeze.** Hyperparameter search comes after the regularization strategy is established. Model ensembles, longer training runs, and architecture refinements are last-mile optimizations.

## Gradient Descent and Backpropagation

All optimization in neural networks flows from one idea: the gradient of the loss with respect to each parameter tells you which direction to move to reduce loss.

**Forward pass:** Compute the predicted output and the scalar loss value. Each layer stores intermediate activations needed for the backward pass.

**Backward pass (backpropagation):** Apply the chain rule recursively from the loss back to the input. For a nonlinear two-layer network with sigmoid activation:

```
∂L/∂W1 = ((w2ᵀ · ∂L/∂ŷ) ⊙ A ⊙ (1 - A)) · Xᵀ
```

The key insight is that stored forward-pass activations are reused in the backward pass — this is why gradient checkpointing (trading compute for memory) works by recomputing them on demand during the backward pass.

**Gradient descent variants:**
- **Batch GD:** uses the full dataset per update. Exact gradients, computationally expensive.
- **SGD:** uses one sample. Noisy but fast; noise can help escape local minima.
- **Mini-batch SGD:** the standard. Balance between noise and computational efficiency.

## Optimizers: SGD to Adam to AdamW

**Vanilla SGD:** `θ ← θ − α∇L(θ)`. Simple and well-understood, but sensitive to learning rate. For ConvNets, well-tuned SGD slightly outperforms Adam — but the optimal LR is narrow.

**SGD with Momentum:** Accumulates a velocity vector in the direction of persistent gradients, dampening oscillations and accelerating convergence in low-curvature directions.

**Adam:** Adapts per-parameter learning rates using first-moment (mean gradient) and second-moment (uncentered variance) estimates. Much more forgiving of hyperparameter choices. **Karpathy's rule of thumb:** `lr = 3e-4` with Adam as the safe default for baselines. For RNNs and transformers, Adam is the standard.

**AdamW:** Decouples weight decay from the gradient update, which fixes a subtle bug in Adam's regularization. In Adam, L2 regularization is absorbed into the adaptive learning rate, reducing its effect on large-gradient parameters. AdamW applies weight decay directly to the weights: `θ ← θ − α · (m̂/√v̂ + ε) − λθ`. This is the standard optimizer for modern LLM training.

## Learning Rate Schedules

The learning rate is the most impactful hyperparameter. Common schedules:

- **Constant:** Simplest. Karpathy recommends disabling decay entirely during initial experimentation and tuning it last.
- **Step decay:** Reduce by a factor (e.g., 10x) at fixed epochs. The epoch milestones are dataset-specific — do not copy ImageNet defaults.
- **Cosine annealing:** Smoothly decays from max to near-zero LR over training. Standard for most modern training runs.
- **Warmup:** Linearly ramp up LR from near-zero for the first N steps, then decay. Critical for training transformers from scratch; prevents gradient instability at initialization.
- **Cyclical LR / 1-cycle:** Alternates between low and high learning rates. Can accelerate convergence.

## Hyperparameter Search

**Random search beats grid search** for neural networks. Because sensitivity varies dramatically across hyperparameters (LR may matter 10x more than dropout rate), grid search wastes budget exploring the insensitive dimensions. Random search samples each dimension more densely.

Priority order for tuning: learning rate → batch size → weight decay → architecture size → dropout → LR schedule shape.

## Debugging Neural Networks

Debugging a neural network requires deliberate verification at each stage — silent failures are the norm.

**Key diagnostics:**
- **Gradient flow check:** Zero out all inputs except example i and confirm the loss gradient is non-zero only at position i. This catches bugs where batch dimension is incorrectly mixed (e.g., `view` vs. `transpose`).
- **Prediction dynamics:** Track model predictions on a fixed held-out batch throughout training. Visualizing the dynamics reveals instabilities — excessive jitter indicates high LR; flat dynamics indicate too-low LR or vanishing gradients.
- **First-layer weights:** For image models, visualize first-layer filters. Edge detectors should be visible; noise suggests something is wrong with data preprocessing or the training objective.
- **Loss at init:** Mismatched initialization causes "hockey stick" loss curves where the network spends early iterations simply learning to predict the mean.

**Common silent bugs:**
- Off-by-one bug causing autoregressive model to see its own target
- Gradients clipped on loss (not gradient norm), silently discarding outlier examples
- LR schedule tied to epoch count when training set size changed
- Not using original preprocessing mean/std from a pretrained checkpoint

## The Overfitting Paradox

The counterintuitive result: **try a larger model, then early-stop**. Larger models overfit harder, but their "early stopped" validation performance often exceeds that of smaller models that were fully trained. The reason is that larger models have more capacity to find good solutions before overfitting kicks in. Overfitting-prevention via capacity reduction is typically less effective than overfitting-prevention via regularization applied to a large model.

## Sources

- Karpathy, "A Recipe for Training Neural Networks" — `kb/hard/raw/karpathy/a-recipe-for-training-neural-networks.md`
- Aman AI, "Primers: Gradient Descent and Backprop" — `kb/hard/raw/aman-ai/primers-gradient-descent-and-backprop.md`
- Aman AI, "Coursera DL: Improving Deep Neural Networks" — `kb/hard/raw/aman-ai/coursera-dl-improving-deep-neural-networks-hyperparameter-tuning-regularization.md`
