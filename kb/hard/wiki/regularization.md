---
concept: Regularization & Overfitting
tags: [regularization, dropout, batch-norm, overfitting, bias-variance]
sources:
  - kb/hard/raw/aman-ai/primers-dropout.md
  - kb/hard/raw/aman-ai/primers-batchnorm.md
  - kb/hard/raw/aman-ai/primers-regularization.md
last_compiled: 2026-04-05
related: [neural-network-fundamentals, neural-network-training]
---

# Regularization & Overfitting

Regularization is a collection of techniques that reduce the gap between training and validation performance — the signature of overfitting. Overfitting occurs when a model learns the statistical noise in the training set rather than the underlying pattern. A model with insufficient capacity underfits (high bias); a model with excess capacity that is not constrained overfits (high variance). The goal of regularization is to navigate this bias-variance tradeoff to achieve good generalization.

## The Bias-Variance Tradeoff

**Bias:** Error from underfitting — the model is too simple to capture the true function. High bias manifests as high training error.

**Variance:** Error from overfitting — the model is too sensitive to noise in the specific training set. High variance manifests as a large gap between training and validation error.

Regularization techniques generally reduce variance at the cost of a small increase in bias. The overall generalization error can be decomposed as:

`Error = Bias² + Variance + Irreducible Noise`

Practical implication: adding more data reduces variance without increasing bias, making it the most reliable regularization method. When data collection is not feasible, the techniques below provide the next best options.

## L1 and L2 Regularization (Weight Penalties)

Both techniques modify the loss function by adding a penalty on weight magnitude:

```
J_regularized = J_cross_entropy + λ · J_penalty
```

**L2 regularization (weight decay):**
- Penalty: `λ · Σ ||w||²`
- Update rule: `w ← w − 2αλw − α · ∂J/∂w`
- Effect: Penalizes weight proportionally to its magnitude. Large weights shrink faster. Weights approach but never exactly reach zero.
- Result: Distributes weight magnitude uniformly across the weight matrix. Reduces sensitivity to individual features.
- Use case: General-purpose. Standard for deep networks. AdamW implements this as decoupled weight decay.

**L1 regularization:**
- Penalty: `λ · Σ |w|`
- Update rule: `w ← w − αλ · sign(w) − α · ∂J/∂w`
- Effect: Subtracts a constant regardless of weight magnitude. Weights that would cross zero are set exactly to zero.
- Result: Produces sparse weight vectors — many weights are exactly zero. This is "feature selection."
- Use case: Wide models, high-cardinality categorical features, situations where feature selection is desired.

**Key difference:** L2's penalty is proportional to weight size (smaller weights → smaller penalty), so it approaches but never reaches zero. L1's penalty is constant regardless of size, so weights can hit exactly zero. Geometrically, the L1 constraint set is a diamond (corners touch axes), pushing solutions toward axes; the L2 constraint is a sphere (no corners), producing uniform shrinkage.

## Dropout

Dropout (Srivastava et al., 2014) addresses overfitting by randomly deactivating a fraction of neurons during each training update. This simulates training an exponential number of different network architectures and averaging their predictions.

**Mechanism:**
- During training: each neuron is retained with probability `p` (dropped with probability `1-p`). The effective network architecture changes every batch.
- During inference: all neurons are active, but weights are scaled by `p` to maintain expected activation magnitude.

**Inverted dropout** (standard in PyTorch/Keras): Scale activations by `1/(1-p)` during training instead. This avoids any modification at inference time — the trained model can be used directly.

**Interpretation:** Dropout breaks co-adaptation between neurons — units can no longer rely on specific other units being present, so they are forced to learn redundant, independent features. This improves robustness.

**Practical guidelines:**
- Hidden layers: keep probability `p` = 0.5–0.8
- Input layer: keep probability close to 1.0 (0.8–1.0)
- Use spatial dropout (dropout2d) for convolutional layers
- Size the network appropriately: if dropout rate is 0.5, use approximately `n/0.5 = 2n` units to maintain effective capacity
- Do not combine naively with batch normalization (their interactions are problematic — BN statistics become noisy when dropout randomly removes units)

**When to use:** Most effective on small-to-medium datasets where overfitting is the primary concern. For very large datasets, the computational cost may outweigh the benefit.

## Batch Normalization

Batch normalization (Ioffe & Szegedy, 2015) normalizes the inputs to each layer within a mini-batch. The original motivation was reducing "internal covariate shift" — the change in layer input distributions as upstream weights update. More recently, evidence suggests its primary effect is smoothing the loss landscape, enabling larger learning rates and faster convergence.

**Training-time computation (per feature):**
1. Compute batch mean `μ` and variance `σ²`
2. Normalize: `x̂ = (x - μ) / √(σ² + ε)`
3. Scale and shift: `y = γx̂ + β` where `γ` and `β` are learned parameters

**Inference-time:** Uses running mean and variance computed via exponential moving average during training. This is why you must call `model.eval()` (PyTorch) or equivalent before inference — otherwise the model uses noisy batch statistics.

**Benefits:**
- Dramatically reduces training epochs needed for convergence
- Allows higher learning rates
- Reduces sensitivity to weight initialization
- Provides mild regularization (the noise from batch statistics acts as a regularizer)

**Placement:** The original paper recommends placing BN before the activation function. For ReLU networks, this is standard. For sigmoid/tanh, placing it after activation may be better — test both.

**Do not combine with dropout:** BN's statistics become unreliable when dropout randomly removes units. Choose one or the other.

### Layer Normalization and RMSNorm

For transformers and RNNs, **Layer Normalization** normalizes across the feature dimension for each sample independently (rather than across the batch). This eliminates the batch-size dependency, making it suitable for single-sample inference and variable-length sequences — which is why all modern LLMs use LayerNorm rather than BatchNorm.

**RMSNorm** is a simplified variant that normalizes by the root-mean-square of activations, omitting the mean subtraction step. It reduces computational cost and is used in LLaMA and other modern architectures.

## Data Augmentation

Data augmentation generates additional training examples by applying transformations to existing data. It is one of the most effective regularization techniques because it directly addresses the root cause: insufficient data diversity.

- **Images:** flips, rotations, crops, color jitter, mixup, cutout
- **Text:** back-translation, synonym replacement, paraphrase
- **Audio:** time-stretch, pitch shift, noise injection

Key caution: if augmentation changes the label semantics (e.g., flipping a "left turn" traffic sign), ensure labels are also updated.

## Early Stopping

Stop training when validation loss stops improving. This is a form of implicit regularization — training is halted before the model has had time to overfit. Track the validation loss at regular checkpoints and restore the best checkpoint at the end.

Counterintuitive finding (see [[hard/wiki/neural-network-training|Neural Network Training]]): larger models with early stopping often outperform smaller models trained to convergence. The larger model has more capacity to find a good solution before overfitting begins.

## Other Techniques

**Weight constraint (max-norm):** Cap the L2 norm of incoming weight vectors per neuron to a maximum value (typically 3–4). Recommended alongside dropout to prevent weight explosion in response to dropped units.

**Label smoothing:** Replace hard one-hot targets with soft targets: `y_smooth = (1 - ε) · y_hard + ε / K`, where K is the number of classes and ε is typically 0.1. Prevents the model from becoming overconfident, improving calibration and generalization. Standard in vision and NLP training.

**Smaller batch size:** Smaller mini-batches introduce more noise in batch norm statistics, providing additional regularization. This is the mechanism behind the observation that larger batch sizes sometimes generalize worse.

## Sources

- Aman AI, "Primers: Regularization" — `kb/hard/raw/aman-ai/primers-regularization.md`
- Aman AI, "Primers: Dropout" — `kb/hard/raw/aman-ai/primers-dropout.md`
- Aman AI, "Primers: Batchnorm" — `kb/hard/raw/aman-ai/primers-batchnorm.md`
