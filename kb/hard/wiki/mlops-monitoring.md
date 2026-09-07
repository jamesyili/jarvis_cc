---
concept: MLOps & Model Monitoring
tags: [mlops, monitoring, drift, model-versioning, cd4ml]
sources:
  - kb/hard/raw/aman-ai/primers-mlops-tooling.md
  - kb/hard/raw/aman-ai/primers-mlops-testing.md
  - kb/hard/raw/aman-ai/primers-data-drift.md
  - kb/hard/raw/eugene-yan/a-practical-guide-to-maintaining-machine-learning-in-production.md
last_compiled: 2026-04-05
related: [model-deployment, a-b-testing, feature-stores]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# MLOps & Model Monitoring

MLOps — machine learning operations — is the discipline of reliably deploying, monitoring, and maintaining ML models in production. It adapts software engineering's DevOps practices (CI/CD, automated testing, observability) to the unique challenges of ML: non-deterministic outputs, training-serving skew, and performance decay caused by shifting data distributions.

## The CD4ML Production Lifecycle

Continuous Delivery for Machine Learning (CD4ML) treats model releases like software releases. The lifecycle has three phases:

**Develop** — Feature engineering, training, offline evaluation. Experiments are tracked (MLflow, Weights & Biases, Neptune) with full parameter and metric logging, including the git commit hash.

**Deploy** — Model validation before promotion, containerized serving (Docker/KFServing/BentoML), shadow deployment, rollback capability. The gold standard is to validate the candidate model on a held-out recent window before releasing it. If it fails validation, the pipeline breaks and the stale model stays live — a stale model beats a broken one.

**Monitor** — Continuous observation of data quality, model behavior, and business metrics once live. This is where most teams under-invest.

## Data & Concept Drift

Model performance degrades when the world changes. There are four distinct drift types:

| Type | What changes | Detection signal |
|------|-------------|-----------------|
| Covariate drift | Distribution of input features P(X) | K-S test, Jensen-Shannon divergence on feature histograms |
| Concept drift | Relationship P(Y\|X) | Accuracy/loss degradation over time |
| Label drift | Distribution of targets P(Y) | Chi-squared test on label proportions |
| Feature interaction drift | Correlations between features | Pairwise mutual information shifts |

**Covariate drift** is the most common. A model trained on desktop traffic starts receiving mobile traffic — screen size and click-rate features shift. Detection: compare CDFs between training data and live data using the Kolmogorov-Smirnov statistic `D = sup_x |F1(x) - F2(x)|`. Netflix uses K-S monitoring at the Spark + AI Summit level.

**Concept drift** is the most insidious. A spam filter becomes ineffective as spammers evolve their tactics. The relationship between features and labels changes even if the raw inputs look identical. This manifests as accuracy drops, not distribution shifts.

Concept drift can be sudden (new competitor launches, a meme goes viral), gradual (social norms shift), or cyclic (weekday vs. weekend ride-share patterns).

**Not all drift requires retraining**, but all requires monitoring. Some features are more drift-prone than others — an app store ranking changes fast while demographic features are stable. In production, a less accurate but more stable feature can sometimes be preferable.

## Statistical Tests for Drift Detection

- **K-S test**: Non-parametric, compares continuous distributions. Good for covariate drift.
- **Chi-squared test**: For categorical features and label drift.
- **Jensen-Shannon Divergence (JSD)**: Symmetric version of KL-divergence, range [0,1]. Values above ~0.1 warrant investigation.
- **Wasserstein/Earth Mover's Distance**: Measures the "cost" to transport one distribution into another; intuitive for continuous variables.
- **ML-based drift detector**: Label training data as class 1, production data as class 0, fit a classifier. High AUC = significant drift. Matthews Correlation Coefficient (MCC) is a reliable metric here.

**Key libraries**: Evidently AI (tabular drift dashboards), Alibi-Detect (tabular + image + text, supports MMD and C2ST), Scikit-Multiflow (streaming, ADWIN algorithm), Deepchecks (end-to-end validation suites).

## Testing ML Systems

Testing ML systems requires a two-tier workflow:

**PR gate (fast, <20–30 min)**
- Data validation tests: schema checks, row counts, null proportion checks, column range checks
- Unit tests: individual utilities run correctly; use synthetic data
- Smoke tests: fast version of expensive tests (subset of data, 1 epoch) to catch obvious failures

**Nightly builds (slow, hours)**
- Functional tests: correct outputs on real data (e.g., RMSE is positive and bounded)
- Integration tests: data ingestion pipelines interact correctly with compute
- Performance tests: latency and memory footprint stay within bounds
- Responsible AI tests: fairness, explainability, privacy checks
- Regression tests: parity between old and new code versions

With nightly builds, use a **two-level branching strategy**: pull requests merge into a staging branch; the main branch is only updated after nightly builds pass. This keeps main always deployable.

## Production Observability

**What to monitor**:

1. **Input data quality**: Schema correctness, null proportions, value ranges, distribution stability (daily aggregates). Basic checks — row counts, duplicate primary keys, unexpected categories — catch the majority of upstream pipeline failures.

2. **Training-serving skew**: Features at serving time should match features at training time. Log both the raw inputs and the processed features during serving. The simplest fix: train on served features (historical processed features, not raw upstream data).

3. **Model health**: Staleness (when was it last retrained?), feature importance stability (sudden importance spikes suggest data leaks), SHAP/LIME explainability for operational staff.

4. **Offline-online metric correlation**: Does an AUC improvement offline actually translate to CTR improvement online? Invest in finding dependable offline proxies — this pays continuous dividends. Focus online metrics on direct impacts (clicks, purchases) before indirect or lagging metrics.

5. **Prediction drift**: Compare rank distributions of consecutive model versions. A product jumping from rank 10,000 to rank 1 warrants investigation.

## MLOps Tooling Landscape

| Category | Key tools |
|----------|----------|
| Experiment tracking | MLflow, Weights & Biases, Neptune AI |
| Data versioning | DVC, Git LFS |
| Pipeline orchestration | Airflow, Kubeflow |
| Data validation | Great Expectations, Deepchecks, Cleanlab |
| Drift detection | Evidently AI, Alibi-Detect, TorchDrift |
| Model serving | BentoML, KFServing, Cortex |
| Feature store | Feast |
| Vector DBs | Milvus, Pinecone, Qdrant |
| CI/CD | GitHub Actions, ClearML |

**AWS native stack**: SageMaker Model Monitor → CloudWatch → EventBridge → SNS → Lambda for automated drift detection, alerting, and retraining workflows. Kinesis handles real-time streaming into Model Monitor.

## Must-Have vs. Good-to-Have

**Must-haves** (highest ROI per Eugene Yan):
1. Model validation before deployment — single check eliminates most misbehavior
2. Input data validation — basic distribution and schema checks
3. Rollback capability — lets teams iterate fast without production fear

**Good-to-haves**:
- End-to-end data scientists (reduces coordination overhead, increases ownership)
- Centralized MLflow server + Docker containers for reproducibility
- Customer service tooling for blacklisting, boosting, and explaining outputs

## Sources

- Aman Chadha, [MLOps Tooling](https://aman.ai/primers/ai/mlops-tooling/)
- Aman Chadha, [MLOps Testing](https://aman.ai/primers/ai/mlops-testing/)
- Aman Chadha, [Data Drift](https://aman.ai/primers/ai/drift/)
- Eugene Yan, [A Practical Guide to Maintaining Machine Learning in Production](https://eugeneyan.com/writing/practical-guide-to-maintaining-machine-learning/)
