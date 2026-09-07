---
concept: ML Production Maintenance
tags: [ml-production, monitoring, drift, retraining, operational]
sources:
  - kb/hard/raw/eugene-yan/a-practical-guide-to-maintaining-machine-learning-in-production.md
  - kb/hard/raw/eugene-yan/6-little-known-challenges-after-deploying-machine-learning.md
  - kb/hard/raw/eugene-yan/mechanisms-for-effective-machine-learning-projects.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/mlops-monitoring|MLOps Monitoring]]"
  - "[[hard/wiki/feature-stores|Feature Stores]]"
  - "[[hard/wiki/ml-testing|ML Testing]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# ML Production Maintenance

Deploying a model is the starting line, not the finish. The hard work comes after: keeping the system honest, catching silent failures, managing the operational burden, and iterating without breaking things. This is substantially harder than deployment itself.

## Why Production is Harder Than You Think

The root problem is that ML models are static but the world is dynamic. A model trained on last year's data embeds assumptions about the world that may no longer hold. Meanwhile, the system you built is now a live organism entangled with upstream data pipelines, downstream consumers, other models, and real users with real edge cases.

Six categories of post-deployment challenges consistently appear in practice:

**Schema drift:** Upstream data changes without notice. A `gender` field that had values `male`/`female` gets updated to include `Male`, `Female`, `Transgender`, and `Prefer not to say`. Feature encoders silently nullify the new values. The model keeps running, appears healthy, and gradually degrades in performance — especially in segments where that feature matters. Structural drift changes the schema; semantic drift changes the meaning of a field without changing its name (e.g., `hospitalization_days` being silently updated from estimated to actual values).

**Feedback loops:** Production models affect the world, which affects the data the model trains on, which affects the model. A ranking system that promotes high-engagement items today will generate training data showing those items have high engagement, reinforcing their ranking tomorrow. New items can never surface because they have no engagement history. An inventory forecasting model penalized for overstock consistently underestimates demand; stores sell out, and the model learns from the artificially capped sales data. Both are forms of self-fulfilling prophecy that are difficult to detect because offline metrics look fine.

**Entangled codebases:** ML systems attract glue code — one-off scripts to move data from S3 to a database, multiple languages (Python for modeling, Scala for Spark, SQL scattered everywhere), magic numbers embedded in production code. Over time this becomes expensive to maintain and impossible to onboard new engineers onto.

**Model interactions:** Your recommender doesn't live in isolation. A widget ranker allocates screen real estate across multiple models. If your model's online metrics worsen, it may be because a competing widget improved, not because your model degraded. Diagnosing causality in multi-model systems is genuinely hard.

**Org friction:** As systems mature, they attract stakeholders. Adding a feature now requires a data engineer, a data scientist, an engineer to productionize, and a QA pass. Division of labor creates coordination costs that make iteration velocity collapse.

**Operational requests:** Users will discover flaws at scale. Fixing them becomes recurring work that competes with development. Without tooling that empowers customer service agents to self-serve (blacklisting product IDs, flagging bad predictions), this load lands directly on the ML team.

## Monitoring What Matters

**Input data validation** is the first line of defense. Check files before processing: is the schema correct, is the format parseable, is the volume reasonable? Check distributions: are nulls within expected ranges, do categorical columns have unexpected new values, are numeric columns within sane bounds? For continuous features, monitor aggregates (median, IQR) day-over-day. For timestamps, verify format and reasonableness. Statistical tests (chi-squared for categoricals, homogeneity tests for distributions) can formalize these checks at scale.

**Training-serving skew** is a more subtle failure. It occurs when the features computed during training differ from the features served at inference — different code paths, different preprocessing, enriched training data that's unavailable in real-time. The mitigation: log serving features and train on them directly. This eliminates the gap by construction and simplifies the training pipeline.

**Model staleness** compounds over time. Check when the production model was last refreshed. More deeply, use interpretability tools (SHAP, LIME) to monitor feature importance drift. If a feature suddenly jumps in importance, it may indicate a data leak. If a feature that should be important stops contributing, something upstream has changed.

**Offline-online metric correlation** is worth investing in. Many decisions (model selection, deployment gating) are made using offline metrics. If AUC doesn't correlate with CTR in your domain, AUC is not a useful gate. Running controlled experiments to calibrate which offline metrics predict online improvements pays dividends across every future decision.

## Retraining and Deployment

**Validate before promoting.** Before deploying a retrained model, hold out the most recent days of data as a validation set and retrain on the rest. Assert that the new model outperforms a naive baseline (e.g., sort by yesterday's sales) and does not regress on key metrics relative to the current production model. If validation fails, block the deploy — a stale model is better than a misbehaving new one.

**Compare prediction distributions.** Beyond aggregate metrics, compare individual predictions between the old and new model. A product ranked 10,000th by the old model and 1st by the new model is worth investigating before shipping. Large rank inversions on stable items are a signal of something unexpected.

**Shadow release.** Run the new model in production on live traffic, logging its predictions without serving them. Measure latency, error rates, and prediction distributions against the current model. Only promote after confirming production-readiness. Shadow release is especially important for large architectural changes (e.g., decision trees → neural networks) where the surface area of potential failures is large.

**Build rollback capability.** Deploy via containers (Docker). Keep previous working images. When something misbehaves post-deploy, rollback should take minutes, not hours. This is the operational safety net that allows teams to iterate and deploy fast.

## Reducing Operational Burden

**Log configurations, not just metrics.** Model hyperparameters, training data date ranges, thresholds, and commit hashes should be logged to an experiment tracker (MLflow, W&B) for every run. This makes debugging production regressions tractable — you can diff what changed.

**Prune redundant features periodically.** After each round of feature additions, use permutation importance or drop-column importance to identify which features are no longer contributing. Removing them reduces pipeline complexity and compute cost with minimal accuracy impact.

**Learn thresholds from data.** Fixed classification thresholds are fragile under data drift. Instead, evaluate a range of thresholds (e.g., every 1% from 1–99) against your production requirements (target precision, recall, or F1) and update the threshold with each model refresh.

**Audit samples regularly.** Take 1–5% of production predictions and have humans review them. This catches error patterns (systematic misclassifications, new types of adversarial behavior) before they compound. When error patterns are identified, use active learning to relabel similar cases.

**Favor end-to-end ownership.** Data scientists who own the full cycle — problem framing, data, training, deployment, monitoring — iterate faster, learn faster, and develop accountability that division-of-labor structures dilute. Where specialization is necessary, define clear interfaces between roles and build tools that minimize coordination overhead.

## Project-Level Mechanisms

Beyond production monitoring, effective ML projects share structural patterns that reduce failure risk:

A **pilot and copilot** structure assigns one person as the main project owner (pilot) and one as a reviewer (copilot) who checks in periodically, reviews design docs and prototypes, and has veto power over critical methodological decisions. The copilot catches errors (invalid train-validation splits, data leaks, wrong problem framing) early when they're cheap to fix. A rough ratio: for every 10 hours the pilot spends, the copilot spends 1.

**Methodology reviews** — similar to code reviews but for ML experiments — surface these errors systematically: is future data leaking into training? Is the train-validation split by time (required for temporal problems) or randomly? What's the theoretical performance ceiling if the model is allowed to overfit?

**Timeboxing** forces prioritization. Most ML work is research-flavored with many dead ends; without explicit time constraints, it's easy to spend months on a path that leads nowhere. Setting deliberate timeboxes (a week for literature review, 4–8 weeks for a prototype) and treating them as stretch goals builds discipline without eliminating flexibility.

## Sources

- Yan, Eugene. "A Practical Guide to Maintaining Machine Learning in Production." eugeneyan.com, May 2020. https://eugeneyan.com/writing/practical-guide-to-maintaining-machine-learning/
- Yan, Eugene. "6 Little-Known Challenges After Deploying Machine Learning." eugeneyan.com, May 2020. https://eugeneyan.com/writing/challenges-after-deploying-machine-learning/
- Yan, Eugene. "Mechanisms for Effective Machine Learning Projects." eugeneyan.com, Jan 2023. https://eugeneyan.com/writing/mechanisms-for-projects/
