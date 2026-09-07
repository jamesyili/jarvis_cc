---
concept: Decision Trees & Ensemble Methods
tags: [decision-trees, random-forest, gradient-boosting, xgboost, ensemble]
sources:
  - kb/hard/raw/aman-ai/cs229-decision-trees.md
  - kb/hard/raw/aman-ai/cs229-ensemble-methods.md
  - kb/hard/raw/aman-ai/primers-decision-trees-and-ensemble-methods.md
last_compiled: 2026-04-05
related: [learning-to-rank, feature-engineering, supervised-learning]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 0  # not obviously relevant
knowledge_updated: 2026-09-07
---

# Decision Trees & Ensemble Methods

Decision trees are the foundational building block for some of the most practically useful ML algorithms in production systems. Their inherent non-linearity, interpretability, ability to handle mixed feature types without preprocessing, and suitability for ensembling make them central to recommendation and ranking pipelines.

## Decision Trees

A decision tree partitions the input space into disjoint rectangular regions, assigning a prediction to each region. Unlike linear models, which produce hypothesis functions of the form `h(x) = θᵀx`, decision trees produce non-linear boundaries without requiring a hand-crafted feature mapping.

### Tree Construction: Greedy Top-Down Splitting

Building an optimal decision tree is NP-hard. In practice, trees are grown greedily: at each step, choose the leaf node, feature, and threshold that maximally reduces the loss:

```
Decrease in loss = L(R_parent) - [|R1|·L(R1) + |R2|·L(R2)] / (|R1| + |R2|)
```

**For classification:** Use cross-entropy loss (or Gini impurity), not misclassification rate. Misclassification rate is not strictly concave, so it can fail to distinguish between useful and useless splits. Cross-entropy is strictly concave, guaranteeing that any non-trivial split reduces loss.

```
L_cross(R) = -Σ_c p̂_c · log₂(p̂_c)
```

**For regression:** Use squared loss. The prediction for a region is the mean of all training targets in that region.

### Split Criteria at a Glance

| Criterion | Task | Why Use It |
|---|---|---|
| Cross-entropy / Information Gain | Classification | Strictly concave; sensitive to probability shifts |
| Gini impurity | Classification | Computationally cheaper approximation to cross-entropy |
| Variance reduction (MSE) | Regression | Direct optimization of squared error |

### Regularization for Trees

A fully grown tree (one sample per leaf) has zero training error but extreme variance. Regularization heuristics:
- **Minimum leaf size:** Do not split a region if its cardinality falls below a threshold.
- **Maximum depth:** Limit the number of recursive splits.
- **Maximum number of nodes:** Stop when the total leaf count exceeds a threshold.
- **Post-pruning:** Grow the tree fully, then prune branches that provide minimal reduction in validation error. Preferable to early stopping heuristics because greedy single-feature splits can miss higher-order interactions.

### Properties and Limitations

**Advantages:** Non-linear, naturally handle categorical variables (subset membership queries), highly interpretable (trace any prediction to a sequence of if-then rules), fast at inference time (`O(depth)`), handle missing features gracefully.

**Key limitation — no additive structure:** A boundary like `x1 + x2 > k` requires many axis-aligned splits to approximate, since each split can only threshold one feature at a time. Linear models capture this directly. This is why ensembles of trees (especially boosted trees) dramatically outperform single trees on real data.

**Runtime:** Training is `O(n·f·d)` where n = samples, f = features, d = depth. Inference is `O(d)`.

## Bagging and Random Forests

### The Variance Reduction Principle

If n correlated models each have error variance σ² and pairwise correlation ρ, the variance of the averaged ensemble is:

```
Var(mean) = ρ·σ² + (1-ρ)/n · σ²
```

Averaging reduces the second term (the independent-error component) by n. Decreasing correlation ρ reduces the first term. Both matter. Bagging targets the second term; random forests target both.

### Bagging (Bootstrap Aggregation)

Bagging generates M bootstrap samples (each sampled with replacement from the training set, approximately 63% unique examples) and trains one model on each. The final prediction is the average (regression) or majority vote (classification).

**Out-of-bag (OOB) estimation:** Each bootstrap sample omits ~37% of training examples. These can serve as a free validation set. In the limit, OOB error approximates leave-one-out cross-validation.

**Effect on bias-variance:** Bagging primarily reduces variance. Bias slightly increases (each model trains on a noisier subset). In practice, the variance reduction dominates. Adding more models M never increases overfitting — variance can only decrease.

**Variable importance:** For each feature, average the loss reduction across all splits using that feature, across all trees in the ensemble. Note this is not the same as the effect of removing the feature, because correlated features can substitute for each other.

### Random Forests

Random forests extend bagging by restricting each split to a random subset of features (typically `√f` for classification, `f/3` for regression). This directly reduces the inter-tree correlation ρ, even when a dominant predictor exists. The result: lower variance, graceful handling of missing features (trees that used the missing feature can simply be excluded).

Tradeoffs vs. bagged trees: lower variance, slightly higher bias, and harder to interpret (variable importance metrics become the main interpretability tool).

## Boosting

### The Bias Reduction Principle

Bagging reduces variance; boosting reduces bias. Boosting trains a sequence of weak learners (typically decision stumps — depth-1 trees), with each learner focusing on the mistakes of the prior ensemble.

### AdaBoost

At each round m:
1. Train a weak classifier `G_m` on the training data weighted by `w_i`
2. Compute weighted error: `err_m = Σ w_i · 1[y_i ≠ G_m(x_i)] / Σ w_i`
3. Compute this learner's weight: `α_m = log((1 - err_m) / err_m)`
4. Up-weight misclassified examples: `w_i ← w_i · exp(α_m · 1[y_i ≠ G_m(x_i)])`
5. Final classifier: `f(x) = sign(Σ_m α_m · G_m(x))`

AdaBoost is a special case of Forward Stagewise Additive Modeling with exponential loss. Unlike bagging, each new learner is dependent on the previous ones — increasing M does risk overfitting.

### Gradient Boosting

Gradient boosting generalizes boosting to arbitrary differentiable loss functions. Instead of re-weighting examples, each new weak learner fits the negative gradient of the current ensemble's loss:

```
g_i = ∂L(y_i, f(x_i)) / ∂f(x_i)
```

Train a regression tree to match `g_i`, then add it (scaled by a learning rate) to the ensemble. For squared loss, `g_i = y_i - f(x_i)` (the residual) — so gradient boosting reduces to fitting residuals sequentially.

**XGBoost** and **LightGBM** are production-grade gradient boosting implementations with:
- Second-order (Newton) optimization for more accurate step direction
- Regularization terms on leaf weights and tree complexity
- Histogram-based approximate splitting (LightGBM: much faster on large datasets)
- Sparse-aware computation for one-hot and missing features

### Boosting vs. Bagging

| Property | Bagging / Random Forest | Gradient Boosting |
|---|---|---|
| Primary effect | Variance reduction | Bias reduction |
| Training | Parallel | Sequential |
| Overfitting risk | Low (more trees = safer) | Increases with rounds |
| Sensitivity to noise | Low | Higher |
| Typical use in ranking | Feature engineering, baselines | Main ranker (XGBoost, LightGBM) |

## Role in Ranking Pipelines

In recommender and ranking systems (see [[hard/wiki/learning-to-rank|Learning to Rank]]):

- Gradient boosted trees (GBDT) are the dominant algorithm for the scoring stage in many production rankers due to their ability to capture feature interactions, handle heterogeneous feature types, and produce calibrated scores.
- Random forests and bagged trees are useful for feature importance analysis and for ensemble diversity.
- Feature interactions discovered by trees (leaf node indices) are commonly used as features in downstream linear or neural ranking models (GBDT-LR stacking).

## Sources

- Aman AI, "CS229: Decision Trees" — `kb/hard/raw/aman-ai/cs229-decision-trees.md`
- Aman AI, "CS229: Ensemble Methods" — `kb/hard/raw/aman-ai/cs229-ensemble-methods.md`
- Aman AI, "Primers: Decision Trees and Ensemble Methods" — `kb/hard/raw/aman-ai/primers-decision-trees-and-ensemble-methods.md`
