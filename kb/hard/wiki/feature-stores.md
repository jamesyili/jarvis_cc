---
concept: Feature Stores
tags: [feature-store, real-time-features, train-serve-consistency, feast]
sources:
  - kb/hard/raw/eugene-yan/feature-stores-a-hierarchy-of-needs.md
  - kb/hard/raw/eugene-yan/a-practical-guide-to-maintaining-machine-learning-in-production.md
last_compiled: 2026-04-05
related: [feature-engineering, ml-production-maintenance, mlops-monitoring]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Feature Stores

A feature store is a centralized system for creating, storing, sharing, and serving ML features. The concept exists because features are the most labor-intensive part of ML: at Airbnb, ML practitioners spent ~60% of their time on data collection and transformation. At GoJek, features representing the same business concept were being redeveloped by different teams — sometimes with 10 different versions of the same feature.

What a feature store actually *is* depends entirely on what a team needs. Eugene Yan's **hierarchy of needs** framework organizes feature store requirements from foundational to advanced, borrowing from Maslow's pyramid: lower levels must be satisfied before higher ones become relevant.

## The Hierarchy of Needs

### Level 1: Access

The most basic need: making features discoverable and reusable.

Without access, teams build the same features in parallel, creating duplicate pipelines and inconsistent model inputs. GoJek built Feast (Feature Store) as the interface between data engineers and ML practitioners — data engineers contribute features; ML teams consume them.

Uber's Palette feature store achieved similar goals: a shared repository where any team could contribute or consume features, minimizing duplication and accelerating the ML process.

At this level, a feature store behaves mostly like a well-organized data warehouse. What distinguishes a feature store from a data warehouse is the next level: serving.

### Level 2: Serving

Features must be available in production at low latency and high throughput — not via SQL queries.

A common failure mode: features exist in an analytics stack (BigQuery, Hive) but aren't available in the production stack when the model runs inference. Monzo Bank solved this with a lean approach: a cron job syncs feature tables from BigQuery to Cassandra. Tags on SQL queries flag which tables need to be available in production.

**Dual-store architecture** is the standard pattern:
- **Offline store** (Hive, BigQuery, Parquet/S3): Updated in batches, used for training
- **Online store** (Cassandra, Redis, DynamoDB): Updated continuously, serves real-time inference

Uber's Palette syncs both directions: new features in Hive are automatically copied to Cassandra; real-time features added to Cassandra are ETL-ed back to Hive.

DoorDash's **Gigascale feature store** is the extreme version of serving requirements:
- Billions of feature-value pairs (millions of users, merchants, food items)
- 10+ million QPS across all use cases
- Daily batch writes plus real-time updates for moving-average features

After benchmarking Redis, Cassandra, CockroachDB, ScyllaDB, and YugabyteDB, DoorDash chose Redis for its latency profile at this scale.

### Level 3: Integrity

Integrity addresses two pain points: train-serve skew and point-in-time correctness.

**Train-serve skew** occurs when features computed at training time differ from features computed at serving time — different code paths, different imputation logic, different encoders. The consequences are silent and insidious: the model performs well offline and degrades unexpectedly online.

GoJek addressed this with Apache Beam as a unified data processing layer: the same pipeline (ingesting from BigQuery and Kafka) writes to both offline BigQuery and online Redis. Identical feature transformations in both environments.

Netflix uses **shared feature encoders**: offline Spark pipelines and online serving pipelines use the same classes, libraries, and data formats for feature generation. Different infrastructure, identical semantics.

**Point-in-time correctness** (aka time travel) prevents data leakage in training. When constructing training examples, historical features must reflect what was actually known at the label timestamp — not future information that leaked backward. Netflix built distributed time-travel for this: snapshots of offline data and online microservice state, sampled across contexts (device type, viewing patterns, region) via Spark, stored as Parquet in S3. Queried via simple API:

```scala
val snapshot = new SnapshotDataManager(sqlContext)
  .withTimestamp(1445470140000L)
  .withContextID(OUTATIME)
  .getViewingHistory
```

**Feature monitoring**: Uber's Data Quality Monitor builds multi-dimensional time series on feature metrics (mean, median, null counts, cardinality), applies PCA to the top components, then uses one-step-ahead forecasting to detect anomalies. Airbnb's Zipline shows feature distribution visualizations, feature-label correlations, and clustering analysis directly in the UI.

### Level 4: Convenience

Convenience means the API is fast enough to use that practitioners actually adopt it, rather than building workarounds.

GoJek provides unified Python/Java/Go SDKs where `get_historical_features()` and `get_online_features()` share nearly identical syntax — the same call pattern for training and serving. This removes friction when switching from offline experimentation to production deployment.

Uber's Palette DSL (domain-specific language) extends Spark Transformer abstractions to provide a declarative syntax for feature retrieval and composition — e.g., retrieving batch features, real-time features, and derived features from a restaurant entity, then combining them.

### Level 5: Autopilot

The highest level: automation of tedious maintenance work.

Airbnb Zipline's backfill UI lets data scientists specify a new feature, date range, and parallelism — Airflow handles the rest. Previously, backfilling was the primary bottleneck when iterating on training sets.

Other autopilot capabilities:
- Netflix Metacat: cost/storage analysis for identifying unused feature tables
- Uber Data Quality Monitor: automatic anomaly detection and daily quality scores
- Uber feature discovery: users provide labels; Palette suggests correlated features

Most organizations only need Levels 1–3, plus part of Level 4 to be unblocked. Levels 4–5 become relevant at scale or when iteration speed is a strategic priority.

## Practical Starting Point

**Feast** (open source, GoJek/Google origin) covers access and serving, with a consistent API for training and online inference. It's the recommended starting point for teams building their first feature store.

For most teams, the minimum viable feature store is:
1. A registry of feature definitions with lineage
2. An offline store for training data retrieval
3. An online store synced from the offline store
4. Consistent transformation logic between both

The key failure to avoid is building offline infrastructure without planning for online serving — it creates a cliff edge when the model ships to production.

## Train-Serve Skew Prevention Tactics

Beyond feature stores, two practices from production ML maintenance directly prevent skew:

1. **Train on served features**: Log the processed features at serving time and use those logged features as training data. The model then learns on the exact data distribution it will encounter in inference. Bonus: the training pipeline simplifies because upstream ETL for feature construction is no longer needed.

2. **Positional feature trick**: In ranking/recommendation, include position as a feature during training (the model learns its high correlation with CTR). At serving time, drop positional features or set them to a constant. This isolates organic relevance from position bias in the training signal.

## Sources

- Eugene Yan, [Feature Stores: A Hierarchy of Needs](https://eugeneyan.com/writing/feature-stores/)
- Eugene Yan, [A Practical Guide to Maintaining Machine Learning in Production](https://eugeneyan.com/writing/practical-guide-to-maintaining-machine-learning/)
