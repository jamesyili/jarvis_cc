---
concept: Supervised Learning Algorithms
tags: [linear-regression, logistic-regression, svm, naive-bayes, classification]
sources:
  - kb/hard/raw/aman-ai/cs229-logistic-regression.md
  - kb/hard/raw/aman-ai/cs229-support-vector-machines.md
  - kb/hard/raw/aman-ai/primers-naive-bayes.md
last_compiled: 2026-04-05
related: [neural-network-fundamentals, decision-trees-ensembles, feature-engineering]
---

# Supervised Learning Algorithms

Supervised learning algorithms learn a mapping from inputs to outputs using labeled training examples. This article covers the classical algorithms — logistic regression, SVMs, and Naive Bayes — that remain relevant both as production components and as conceptual foundations for understanding more complex models.

## Logistic Regression

### Why Not Linear Regression for Classification?

Linear regression applied to binary classification produces outputs outside `[0, 1]` and is sensitive to outliers: a single extreme example can dramatically shift the decision boundary. These problems are solved by logistic regression.

### The Logistic Model

Logistic regression squashes the linear combination of features through the sigmoid function:

```
h_θ(x) = g(θᵀx) = 1 / (1 + e^(-θᵀx))
```

The sigmoid `g(z)` maps any real input to `(0, 1)`, giving an output interpretable as the probability that `y = 1`. Decision boundary: predict `y = 1` when `h_θ(x) ≥ 0.5`, i.e., when `θᵀx ≥ 0`.

**Useful derivative:** `g'(z) = g(z)(1 - g(z))`. This clean form propagates through the update rule derivation.

### Training: Maximum Likelihood Estimation

Assuming independent examples, the log-likelihood under a Bernoulli model is:

```
ℓ(θ) = Σ_i [y^(i) log h(x^(i)) + (1 - y^(i)) log(1 - h(x^(i)))]
```

Maximize this via gradient ascent. The resulting update rule is:

```
θ_j := θ_j + α · Σ_i (y^(i) - h_θ(x^(i))) · x_j^(i)
```

Despite looking identical to the LMS (least-mean-squares) update for linear regression, this is a different algorithm — `h_θ(x)` is now nonlinear. This is not a coincidence: logistic regression is a generalized linear model (GLM), and this update form is universal across the GLM family.

### Properties

- Outputs calibrated probabilities
- Fast to train; scales well to large datasets
- Interpretable: coefficient for feature j is the log-odds change per unit increase in j
- Linear decision boundary — cannot model non-linear separations without feature engineering
- Foundation of the recall layer in many recommendation systems (fast, calibrated, parallelizable)

## Support Vector Machines

### Margin Intuition

SVMs extend the idea of a linear decision boundary by maximizing the margin — the perpendicular distance between the decision boundary and the nearest training examples (the support vectors). A larger margin means more confident predictions and better generalization.

### Geometric Margin

For classifier `h(x) = g(wᵀx + b)`, the geometric margin of training example `(x^(i), y^(i))` is:

```
γ^(i) = y^(i) · (w/‖w‖)ᵀ x^(i) + b/‖w‖)
```

Unlike the functional margin `ŷ = y(wᵀx + b)`, the geometric margin is invariant to rescaling of `(w, b)`. The SVM maximizes the minimum geometric margin over all training examples.

### The Optimization Problem

Setting the functional margin of the training set to 1 (a normalization constraint), the primal SVM optimization is:

```
min_{w,b}  (1/2)‖w‖²
s.t.       y^(i)(wᵀx^(i) + b) ≥ 1,  ∀i
```

This is a convex quadratic program (QP) — solvable with standard QP solvers. The solution is the maximum-margin separating hyperplane.

### The Kernel Trick

The dual form of the SVM optimization depends on training data only through inner products `⟨x^(i), x^(j)⟩`. This allows replacing the inner product with a **kernel function** `K(x, z) = φ(x)ᵀφ(z)` — computing the inner product in a high-dimensional (or infinite-dimensional) feature space φ(x) without explicitly constructing that space.

Common kernels:
- **Linear:** `K(x, z) = xᵀz` (standard SVM)
- **Polynomial:** `K(x, z) = (xᵀz + c)^d`
- **RBF / Gaussian:** `K(x, z) = exp(-‖x - z‖² / 2σ²)` — infinite-dimensional feature space, most commonly used

**Mercer's theorem:** A function K is a valid kernel if and only if it is symmetric positive semidefinite. The RBF kernel satisfies this and can represent any continuous function in its RKHS.

### Soft-Margin SVM

Real data is rarely linearly separable. The soft-margin SVM introduces slack variables `ξ^(i) ≥ 0` allowing some examples to violate the margin constraint:

```
min_{w,b,ξ}  (1/2)‖w‖² + C · Σ_i ξ^(i)
s.t.         y^(i)(wᵀx^(i) + b) ≥ 1 - ξ^(i)
             ξ^(i) ≥ 0
```

`C` is a regularization parameter trading off margin maximization against training error tolerance. Large `C` = small tolerance for misclassification = risk of overfitting.

### Properties and Use Cases

- Effective in high-dimensional spaces (text, genomics)
- Works well with few training examples relative to feature count
- The kernel trick enables non-linear classification without explicit feature mapping
- Prediction time is `O(n_sv · d)` where `n_sv` is the number of support vectors
- Not inherently probabilistic; calibration requires Platt scaling
- Limited to binary classification natively; multi-class requires one-vs-one or one-vs-rest

## Naive Bayes

### The Generative Approach

Where logistic regression and SVMs directly model `P(y|x)` (discriminative models), Naive Bayes models the joint distribution `P(x, y)` and applies Bayes' theorem to classify:

```
P(C|X) = P(X|C) · P(C) / P(X)
```

Predict the class with the highest posterior `P(C|X)`.

### The Naive Independence Assumption

The "naive" assumption is that features are conditionally independent given the class:

```
P(X|C) = P(x1, x2, ..., xn|C) = Π_i P(x_i|C)
```

This allows decomposing the likelihood into a product of per-feature terms, making parameter estimation tractable even with many features. Despite the assumption almost never holding in practice, Naive Bayes produces competitive results in many domains.

### Variants

| Variant | Data Type | Distribution Assumption |
|---|---|---|
| Gaussian NB | Continuous | Normal per class |
| Multinomial NB | Count data (word frequencies) | Multinomial |
| Bernoulli NB | Binary features | Bernoulli |

### Spam Detection Example

Given `P(Spam) = 0.2`, `P(word="offer"|Spam) = 0.9`, `P(word="offer"|Not Spam) = 0.1`:

```
P(Spam|"offer") = P("offer"|Spam) · P(Spam) / P("offer")
                = 0.9 × 0.2 / 0.26 ≈ 0.69
```

The email is classified as spam.

### Properties and Use Cases

**Strengths:**
- Extremely fast to train and predict — no iterative optimization
- Works well with high-dimensional data (text, genomics)
- Requires very little data to estimate parameters
- Handles multi-class naturally

**Weaknesses:**
- Conditional independence assumption often violated
- Probability estimates are poorly calibrated
- Cannot model feature interactions

**Typical use cases:** Spam filtering (historical baseline), text classification, medical diagnosis baseline, recommendation feature for domain classification.

## Comparing the Algorithms

| Algorithm | Decision Boundary | Probabilistic Output | Key Strength |
|---|---|---|---|
| Logistic Regression | Linear | Yes (calibrated) | Speed, interpretability, calibration |
| SVM (linear) | Linear | No (needs calibration) | Max-margin, high-dim robustness |
| SVM (kernel) | Non-linear | No | Complex boundaries without features |
| Naive Bayes | Linear (features independent) | Yes (uncalibrated) | Speed, very few examples |

In practice, for tabular data with engineered features, gradient boosted trees (see [[hard/wiki/decision-trees-ensembles|Decision Trees & Ensembles]]) will typically outperform all of these. These algorithms remain relevant as fast baselines, interpretable models, and as components within larger pipelines (e.g., logistic regression on top of GBDT features).

## Sources

- Aman AI, "CS229: Logistic Regression" — `kb/hard/raw/aman-ai/cs229-logistic-regression.md`
- Aman AI, "CS229: Support Vector Machines" — `kb/hard/raw/aman-ai/cs229-support-vector-machines.md`
- Aman AI, "Primers: Naive Bayes" — `kb/hard/raw/aman-ai/primers-naive-bayes.md`
