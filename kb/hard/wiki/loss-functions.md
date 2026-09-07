---
concept: Loss Functions
tags: [loss-functions, cross-entropy, contrastive-loss, ranking-loss]
sources:
  - kb/hard/raw/aman-ai/primers-loss-functions.md
  - kb/hard/raw/aman-ai/recommendation-systems-eval-metrics-and-loss.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/neural-network-training|Neural Network Training]]"
  - "[[hard/wiki/learning-to-rank|Learning to Rank]]"
  - "[[hard/wiki/embeddings-and-representation-learning|Embeddings & Representation Learning]]"
  - "[[hard/wiki/self-supervised-contrastive|Self-Supervised & Contrastive Learning]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Loss Functions

A loss function quantifies the discrepancy between model predictions and ground truth. It is the primary feedback signal for gradient-based optimization — the optimizer uses the loss gradient to update model parameters. No single loss is universally optimal; each encodes assumptions about the task structure, the output space, and the noise model.

Understanding which loss to use — and why — is a core modeling skill.

## Classification Losses

### Cross-Entropy Loss

**Cross-entropy** is the canonical loss for classification. It measures how surprised the model is by the true label:

Binary cross-entropy (two classes, sigmoid output):
`L = -(y·log(p̂) + (1-y)·log(1-p̂))`

Categorical cross-entropy (C classes, softmax output):
`L = -Σ_c y_c · log(p_c)`

Since labels are one-hot, this reduces to `L = -log(p_{true_class})` — the negative log probability assigned to the correct class. Minimizing cross-entropy forces the model to assign high probability to correct labels.

**Mathematical equivalence**: minimizing cross-entropy = minimizing KL divergence from the data distribution to the model distribution = maximum likelihood estimation under a categorical/Bernoulli distribution. These are the same objective with different interpretations.

**Why not MSE for classification?** MSE assumes Gaussian noise; classification outputs are categorical. When combined with sigmoid/softmax, MSE produces vanishing gradients near confidence extremes — correct but uncertain predictions receive large gradients, not informative ones. Cross-entropy's logarithmic penalty produces strong, calibrated gradient signals even for confident wrong predictions.

### Focal Loss

Focal loss (Lin et al. 2017, for dense object detection) addresses **class imbalance** by down-weighting easy examples:

`FL(p_t) = -(1 - p_t)^γ · log(p_t)`

When γ = 0, this is standard cross-entropy. As γ increases, the loss for well-classified examples (large p_t) is suppressed — training focuses on hard, misclassified examples. Combined with a class-weighting factor α, Focal Loss is the standard in imbalanced classification settings (object detection, medical imaging).

### Hinge Loss (SVM Loss)

Hinge loss enforces a margin between classes:

`L(y) = max(0, 1 - t·y)`

where t ∈ {-1, +1} is the label and y is the raw score. Zero loss only if the prediction is both correct and sufficiently confident (margin ≥ 1). Incorrect or close-to-boundary correct predictions incur a linear penalty.

Multi-class hinge (SVM loss) requires the correct class score to exceed all incorrect classes by a margin. While theoretically well-motivated for SVMs, hinge loss is less common in deep networks — it lacks probabilistic interpretation and is less convenient to optimize than cross-entropy.

### KL Divergence

KL divergence measures the difference between two probability distributions:

`D_KL(P||Q) = Σ_x P(x) log(P(x)/Q(x))`

Non-symmetric — `D_KL(P||Q) ≠ D_KL(Q||P)`. Decomposition: `H(P, Q) = D_KL(P||Q) + H(P)`, so minimizing cross-entropy is equivalent to minimizing KL divergence when P (the data distribution) is fixed.

KL divergence arises explicitly in:
- Variational autoencoders (regularizing the latent distribution toward a prior)
- RLHF (penalizing the policy for diverging from the reference model)
- Knowledge distillation (matching student to teacher distribution)

## Regression Losses

### Mean Squared Error (MSE / L2 Loss)

`MSE = (1/m) Σᵢ (yᵢ - ŷᵢ)²`

Corresponds to maximum likelihood under a Gaussian noise model. Smooth, differentiable everywhere, strong gradient signals. **Sensitive to outliers**: squares the error, so a single large residual can dominate the loss.

### Mean Absolute Error (MAE / L1 Loss)

`MAE = (1/m) Σᵢ |yᵢ - ŷᵢ|`

Corresponds to maximum likelihood under a Laplacian noise model. More **robust to outliers** — error grows linearly, not quadratically. Non-differentiable at zero (use subgradient). Constant gradient magnitude can slow convergence near the minimum.

### Huber Loss (Smooth L1)

The best of both: quadratic near zero, linear for large errors:

```
L_δ(a) = ½a²            if |a| ≤ δ
        δ(|a| - ½δ)     otherwise
```

Combines MSE's fast convergence for small errors with MAE's outlier robustness. Used as Smooth L1 in Fast R-CNN and PyTorch's `nn.SmoothL1Loss`. The threshold δ is a hyperparameter (commonly 1.0).

**Regression loss selection guide:**
- Gaussian noise, no outliers → MSE
- Heavy-tailed noise, outliers present → MAE or Huber
- Want differentiable everywhere with outlier resistance → Huber

## Ranking Losses

Ranking losses care about relative order, not absolute values. They appear in recommendation systems, information retrieval, and metric learning.

### Bayesian Personalized Ranking (BPR)

Designed for implicit feedback recommendation (clicks, views — no explicit ratings). Models relative preference: for user u, observed item i is preferred over unobserved item j.

`L_BPR = -Σ_{(u,i,j)} log σ(ŷ_ui - ŷ_uj) + λ||Θ||²`

The sigmoid encourages the model to score positive items higher than negative ones. Directly optimizes ranking quality (AUC-aligned) rather than pointwise prediction. Sensitive to the negative sampling strategy — hard negatives (plausible but wrong items) improve learning.

### Triplet Loss

Triplet loss (FaceNet, Schroff et al. 2015) operates on anchor-positive-negative triples:

`L = max(0, ||f(x) - f(x⁺)||² - ||f(x) - f(x⁻)||² + ε)`

Forces the anchor to be closer to the positive (same class) than the negative (different class) by margin ε. Key to learning discriminative embeddings for face recognition, person re-ID, image retrieval.

The choice of hard negatives (close but wrong) is critical — random negatives are often trivially easy and provide no learning signal. Hard negative mining (selecting the hardest negatives within a batch or across all examples) dramatically accelerates convergence.

### LambdaRank / LambdaLoss

LambdaRank addresses the non-differentiability of ranking metrics like NDCG. It defines pseudo-gradients (lambda weights) that weight each pairwise update by how much swapping two documents would change the target metric. This effectively optimizes NDCG/ERR end-to-end.

Used extensively in web search (Bing, Google) and ad ranking. LambdaMART (gradient boosted trees with LambdaRank gradients) is still competitive with deep learning approaches on many ranking benchmarks.

## Contrastive Losses

Contrastive losses operate on pairs or sets of examples, pushing similar items together and dissimilar items apart in embedding space.

### Contrastive Loss (Siamese Nets)

`L = 1{y=1} · ||f(x_i) - f(x_j)||² + 1{y=0} · max(0, ε - ||f(x_i) - f(x_j)||)²`

Similar pairs (y=1) are pulled together; dissimilar pairs are pushed apart to at least distance ε.

### InfoNCE Loss

InfoNCE (used in CPC, SimCLR, MoCo) treats the correct pair as the "positive class" in a classification problem over N samples:

`L_InfoNCE = -E[log(f(x, c) / Σ_{x'∈X} f(x', c))]`

This maximizes mutual information between input and context representations. Scales naturally with batch size — more negatives = better contrastive signal. The denominator is a sum over all in-batch samples.

### NT-Xent Loss (SimCLR)

SimCLR's normalized temperature-scaled cross-entropy:

`L(i,j) = -log[exp(sim(z_i, z_j)/τ) / Σ_{k≠i} exp(sim(z_i, z_k)/τ)]`

where sim(·,·) is cosine similarity and τ is a temperature hyperparameter. Within a batch of 2N augmented views (2 per image), each view's positive is its augmentation pair; the remaining 2N-2 are negatives. Requires large batch sizes for sufficient negatives.

## Task-Appropriate Selection

| Task | Recommended Loss |
|---|---|
| Binary classification | Binary cross-entropy |
| Multi-class classification | Categorical cross-entropy |
| Imbalanced classification | Focal loss |
| Regression (Gaussian noise) | MSE |
| Regression (outliers present) | Huber / MAE |
| Recommendation (implicit feedback) | BPR |
| Metric learning / face recognition | Triplet, ArcFace |
| Self-supervised representation learning | InfoNCE / NT-Xent |
| Learning-to-rank | LambdaRank / LambdaLoss |
| Distribution matching | KL divergence |
| Image segmentation (class imbalance) | Dice loss |

**Key principle**: the loss should match the statistical assumptions of the task. Use cross-entropy for probabilistic classification. Use MSE when assuming Gaussian residuals. Use ranking losses when only relative preferences matter. Mismatched losses produce poor gradient signals and hurt convergence.

---

## Sources

- Aman Chadha, "Primers: Loss Functions," aman.ai, 2026-04-05
- Aman Chadha, "Recommendation Systems: Eval, Metrics and Loss," aman.ai, 2026-04-05
