---
concept: Learning to Rank
tags: [ranking, ltr, deep-ranking, calibration, lambdamart]
sources:
  - kb/hard/raw/aman-ai/recommendation-systems-rankingscoring.md
  - kb/hard/raw/aman-ai/distilled-ad-click-prediction-recsys-design.md
  - kb/hard/raw/aman-ai/distilled-rental-search-ranking.md
  - kb/hard/raw/aman-ai/recommendation-systems-popular-architectures.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/recommendation-systems|Recommendation Systems]]"
  - "[[hard/wiki/two-tower-retrieval|Two-Tower Retrieval]]"
  - "[[hard/wiki/feature-engineering|Feature Engineering]]"
---

# Learning to Rank

Learning to rank (LTR) is the second major stage of a recommendation or search pipeline, operating on the hundreds of candidates produced by retrieval. Where retrieval optimizes for recall, ranking optimizes for precision — placing the most relevant items at the top of the list. The ranking stage justifies its additional compute cost by incorporating features that would have been prohibitively expensive to compute across the full catalog: cross features, dense user context, item embeddings, and session-level signals.

## Why a Separate Ranking Model?

Candidate generators (two-tower, matrix factorization) produce scores — why not use them to rank too? Three reasons:

1. **Incommensurable scores**: A system with multiple candidate generators (matrix factorization + social graph + trending items) produces scores on different scales that can't be compared.
2. **Limited feature expressiveness**: Retrieval models sacrifice feature richness for scalability. Ranking can use anything because it operates on ~100–1000 items, not millions.
3. **Different objectives**: Retrieval optimizes recall; ranking can directly optimize NDCG, CTR, or multi-objective business metrics.

## The Three LTR Paradigms

### Pointwise Methods

Score each item independently, treating ranking as a classification or regression problem.

**Logistic regression**: Binary classification (clicked vs. not clicked). Simple, fast, and interpretable. Coefficients directly indicate feature importance. The classic hard-to-beat baseline with good cross features. Limitation: linear decision boundary, no pairwise context.

**Gradient Boosted Decision Trees (GBDT)**: Ensemble method iteratively training decision trees on gradient residuals. Can optimize ranking metrics like NDCG. High predictive performance with complex feature interactions. Robustly handles missing values and mixed feature types. LinkedIn uses XGBoost for both retrieval (scoring top 1000) and as a feature generator for a downstream generalized linear model. Limitation: no pairwise context, computationally intensive for very large feature sets.

Pointwise methods are common in production because they're fast at inference (score each item independently, batch trivially) and easy to debug.

### Pairwise Methods

Learn to order pairs of items — "item A should rank above item B" — reducing ranking to binary classification over pairs.

**RankNet**: Neural network predicting pairwise preferences. Probabilistic cost function (logistic). End-to-end differentiable. Captures non-linear interactions. Limitation: quadratic number of pairs, slower convergence.

**LambdaRank**: Extends RankNet by computing gradients as if optimizing NDCG, without differentiating through the non-differentiable metric. "Lambda" encodes both pairwise preference and the NDCG gain from swapping a pair. Directly improves ranking quality. Standard in NDCG-focused pipelines.

Pairwise methods generally outperform pointwise on NDCG while remaining more computationally feasible than listwise approaches.

### Listwise Methods

Treat the entire ranked list as a single unit to optimize.

**ListNet**: Models permutation probability distribution via softmax. Directly optimizes NDCG. Computationally expensive.

**LambdaMART**: Combines LambdaRank with gradient boosted trees. The practical gold standard for LTR. Optimizes NDCG list-wise using GBDT, inheriting strong handling of complex feature interactions. Highly scalable, dominant in IR competitions (Yahoo! LTR challenge). Well-supported in XGBoost/LightGBM.

## Deep Ranking Architectures

When catalog scale and feature richness justify neural models, several architectures have become standard.

**Wide & Deep (Google, 2016)**: Combines a linear model (wide component) for memorization of specific feature interactions, with a DNN (deep component) for generalization. Wide component takes cross features — explicit second-order interactions like `AND(user_installed_app='netflix', impression_app='hulu')`. Deep component takes embeddings of categorical features. Joint training with shared loss. Introduced the critical insight that cross features are essential for production ranking quality.

**DeepFM (2017)**: Replaces the wide component's manual feature engineering with a Factorization Machine that automatically learns pairwise feature interactions. Shares embedding layers between FM and DNN components. Handles both low-order (FM) and high-order (DNN) interactions without feature engineering overhead.

**Deep & Cross Network (DCN, 2017)**: Introduces a "cross network" that applies explicit polynomial feature crossing at each layer: `x_{l+1} = x_0 * x_l^T * w_l + b_l + x_l`. Each cross layer increases the polynomial degree by 1. More parameter-efficient than manually engineering cross features. Parallel cross and deep components combined at output.

**DCN V2 (2020)**: Addresses DCN's scalability via low-rank approximations and mixture-of-experts in the cross network. DCN's cross network becomes expensive as embedding dimensions grow. DCN V2's MoE structure decomposes the weight matrix into smaller low-rank factors, reducing computation while maintaining expressiveness.

**DIN (Deep Interest Network)**: Applies attention over the user's historical interaction sequence to compute a context-aware user representation for each candidate item. Instead of pooling all history into a fixed vector, DIN weights historical items by their relevance to the current candidate. Captures the fact that different items activate different aspects of user preference.

**DHEN (2022)**: Deep Hierarchical Ensemble Network. Hierarchical interaction structure with multiple expert networks for feature interaction modeling.

## Position Bias and Debiasing

A fundamental problem in ranking training: items shown at higher positions receive more clicks simply due to position, not relevance. Training on this biased data creates a self-reinforcing feedback loop where position influences both what gets clicked and what the model learns, perpetuating suboptimal rankings.

**Naive debiasing**: Add position as a feature during training, set it to 1 for all items at serving time. This teaches the model the relationship between position and click probability, which it then removes at inference. Recommended in Google's Rules of Machine Learning.

**Propensity weighting**: Use the measured position bias (examination probability at each position) to inverse-propensity-weight the training loss. Items in lower positions get higher weight since they were less likely to be examined.

**Expectation maximization (EM)**: Model clicks as a product of examination (position-dependent) and relevance (item-dependent). Fit the EM model on logged data to separate the two effects. Google demonstrated this on email and file storage search logs.

See [[hard/wiki/counterfactual-evaluation|Counterfactual Evaluation]] for IPS-based debiasing at evaluation time.

## Multi-Objective Ranking

Production ranking models rarely optimize a single objective. A ranking model for YouTube needs to balance click probability, watch time, user satisfaction, and business goals (revenue, content diversity). Standard approaches:

**Multi-task learning**: Shared lower layers (embeddings, feature interactions) with separate output heads per objective. Each head predicts a different label (CTR, watch time, share probability). The final ranking score is a weighted combination of head outputs, with business-defined weights.

**Mixture of Experts (MMoE)**: Multiple expert networks, with gates that learn which experts to activate per task. Prevents task interference — negative transfer where optimizing one objective hurts another. TikTok and YouTube both use MMoE-based architectures.

**Constrained optimization**: Hard constraints on certain objectives (e.g., max diversity threshold, minimum coverage for new content) while optimizing a primary metric.

## Calibration and Production Patterns

**Calibration**: Ranking scores must reflect actual probabilities — miscalibrated outputs break ad auction pricing, blend weights, and multi-objective score combination. Downsampling negatives during training shifts the output distribution; correct post-training: `p_calibrated = p / (p + (1-p) / negative_sample_rate)`. For ad CTR prediction, Normalized Cross-Entropy (NCE) normalizes log-loss by background CTR, making it stable across different CTR baselines.

**Multi-stage ranking (Instagram Explore)**: Three passes with progressively more expensive models — distilled model (500 → 150 candidates), lightweight DNN with full dense features (150 → 50), full DNN with dense+sparse features (50 → 25). This cascading pattern trades precision for latency at each stage.

**Airbnb rental search**: Binary classification (booking vs. not-booking). Training split by time; validation on days immediately following the training cutoff. Cold-start for new listings addressed with content features. 50–100ms serving budget.

**Ad click prediction**: CTR ~1–2% requires heavy negative downsampling and frequent retraining (multiple times daily) to track distribution shift.

## Sources

- Aman.ai: [Recommendation Systems Ranking/Scoring](https://aman.ai/recsys/ranking/)
- Aman.ai: [Distilled — Ad Click Prediction](https://aman.ai/sysdes/adclickpred/)
- Aman.ai: [Distilled — Rental Search Ranking](https://aman.ai/sysdes/airbnb/)
- Aman.ai: [Popular Architectures](https://aman.ai/recsys/architectures/)
