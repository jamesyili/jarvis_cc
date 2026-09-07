---
concept: Ad Systems Design
tags: [ad-systems, ctr-prediction, auction, ad-serving, budget-pacing]
sources:
  - kb/hard/raw/aman-ai/ad-end-to-end.md
  - kb/hard/raw/aman-ai/ad-click-aggregator.md
  - kb/hard/raw/aman-ai/ad-online-auction.md
last_compiled: 2026-04-05
related: [recommendation-systems, learning-to-rank, distributed-systems]
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Ad Systems Design

Ad systems are one of the most complex distributed systems in production. They must deliver highly personalized, auction-determined content to hundreds of millions of users at sub-100ms latency, while simultaneously handling budget pacing, fraud detection, inventory forecasting, and real-time performance analytics. This article covers the full stack: from ad ingestion and indexing through auction mechanics and click aggregation.

## Scale Constraints

A typical large-scale ad platform operates at:
- 200M daily active users, ~300K ad requests per second at peak
- Ad retrieval latency under 100ms
- 99.99% uptime
- Ad corpus: ~10TB; user behavior data: ~50TB/month
- Write throughput: ~10K writes/second; read throughput: ~50K reads/second

Ad click aggregation at scale (1B clicks/day, 2M ads) requires separate consideration — covered in the Click Aggregation section below.

## Full Ad Serving Stack

### Advertiser-Side: Campaign Management

The ad data model has four layers:
1. **Campaign**: Top-level marketing initiative with budget and objectives
2. **Ad Set / Line Item**: Groups ads with shared targeting and delivery settings
3. **Ad**: Individual creative unit (text, image, video)
4. **Creative / Media**: The actual content, decoupled from the ad structure

Advertisers interact via a web UI (single-page JS app) or REST API. The API layer is essential for agencies managing campaigns programmatically. A **creation flow wizard**, **stats and reporting dashboard**, **asset library**, **audience manager**, and **billing integration** (Braintree) round out the advertiser surface area.

### Ads Database → Indexing Pipeline

When advertisers create or modify campaigns, those changes flow through an indexing pipeline before they can be served:

1. **Gateway**: Lightweight stream processor (Kafka Streams, Flink) converts heterogeneous update events into a normalized format. At-least-once delivery.

2. **Updater**: Tails Kafka topics, extracts structured data, writes to Storage Repo with transaction protection.

3. **Storage Repo**: Durable store with cross-row transactions and column-level change notification. PostgreSQL or TiDB for RDBMS semantics; Debezium for change data capture.

4. **Argus**: Notification-triggered worker. On schema change, reads dependent data, performs heavy computation (Spark), generates final servable documents, and publishes to the serving layer.

### Index Publisher

Directly querying the ads DB at serving time is too slow — active ad status requires joining Campaign, Ad Set, Ad, and Creative tables with complex status filters. The **Index Publisher** pre-computes three indices:

- **Live Index**: All currently active ads with metadata needed to form an ad response. Includes secondary indices for targeting rule matching.
- **Pacing Index**: Pacing status and multipliers. Kept separate for resilience — live ads continue to serve even if the pacing system has issues.
- **Feature Index**: Precomputed ad features for the ML ranker. Alternatively backed by low-latency Cassandra or in-memory Redis.

Batch computation (Hadoop/Spark/Dataflow) runs on an hourly schedule for the live index. Kafka handles real-time streaming updates for time-sensitive changes.

### Ads Mixer (Ad Server)

The Ads Mixer is a stateless microservice that orchestrates the per-request serving path:

1. **Request Anatomy**:
   - Client notifies server of active user; user profile loads into memory DB
   - Client sends ad request with context (device, placement, user ID)
   - Live index + targeting rules filter ineligible ads
   - Frequency caps, budget caps applied
   - Remaining candidates go to auction

2. **Candidate Retrieval**: 
   - HNSW (Hierarchical Navigable Small World) approximate nearest neighbor search for embedding-based retrieval
   - Manas (Pinterest's system) maintains both an inverted index (for candidate generation + lightweight scoring) and a forward index (for full scoring)
   - Hybrid search: ANN + structured filters ("shoes < $100, 4 stars+, ships to UK")

3. **Distributed KV Store**: Ad details (content, metadata, targeting, bidding) stored in DynamoDB, Cassandra, or Bigtable keyed by ad ID. The mixer fetches full ad details from this store after retrieving candidate IDs from HNSW.

4. **Parallelization + Caching**: Local caching of the KV store reduces lookup latency and infrastructure cost. Parallel execution of index fetch and ranking.

### Auction Mechanics

Auction is the core of the ad engine:

**Second-Price Auction**: The winning bidder pays the second-highest bid plus a small increment. Encourages truthful bidding.

**Total Bid Formula**:
```
Total Bid = k * EAV + EOV
```
- `k`: Pacing factor (higher urgency → higher k → more likely to win)
- `EAV`: Estimated Advertiser Value — depends on advertising goal. For CPC (cost-per-click): `EAV = bid_price * pCTR`
- `EOV`: Estimated Organic Value — platform benefit, including negative weights for ad fatigue signals

**Generalized Second Price (GSP)**: For auctioning multiple slots simultaneously (e.g., a feed with 3 ad positions). Each winning bidder pays the price bid by the next highest bidder. Non-truthful but widely used.

**Waterfall system**: Candidates grouped into priority tiers. Higher-priority tiers are evaluated first; only if no winner emerges does the system cascade to lower tiers. A minimum bid floor accounts for delivery infrastructure cost.

### Budget Pacing

Pacing ensures ad budgets are spent evenly across a campaign's lifetime, avoiding front-loading (exhausting spend in the first hour) or ad fatigue (the same user seeing the same ad repeatedly).

**Simple approach**: Split budget into hourly chunks; filter out ads that have exhausted their hourly allocation. Simple but inflexible.

**PID Controller approach**:
- Continuously measures the gap between **desired state** (linear projection from 0 to total impressions over campaign lifetime) and **current state** (actual impressions delivered)
- Proportional-Integral-Derivative terms adjust the **pacing factor** k in the bid formula
- Lagging pacing → higher k → higher bids → more wins
- Distributed systems challenge: coordinating pacing factors across many ad server machines

### ML Ranking Pipeline

Beyond hardcoded auction scores, modern ad systems extend into a full ML pipeline:

1. **Feature Engineering**: Context (device, time, placement), demographics, engagement history, ad specifics, fatigue factors, content features
2. **Batch Transformation**: Dataflow or Spark writes features to a feature store (see [[hard/wiki/feature-stores|Feature Stores]])
3. **Model Training**: Sparse Logistic Regression or Gradient Boosting (XGBoost, LightGBM) for CTR/CVR prediction; TensorFlow for deep architectures
4. **Validation + Deployment**: Validated model published to model registry; canary deployment on subset of traffic before full rollout
5. **Real-time Features**: Feature index from live data (ad stats, user engagement) consulted at runtime

### CTR Calibration (pCTR)

Raw CTR predictions from models are often uncalibrated — they predict relative ordering well but absolute probabilities poorly. **Platt scaling** (logistic regression over model output) or **isotonic regression** corrects for this. Calibrated pCTR is essential for auction math: if EAV = `bid * pCTR`, a biased pCTR distorts the entire auction.

## Ad Click Aggregation at Scale

At 1B clicks/day (~10K TPS average, 50K TPS peak), the click pipeline has distinct requirements from ad serving.

**Architecture**:

1. **CDN**: Serves the ad HTML/CSS/JS from edge nodes closest to users
2. **Click Capture Service**: JavaScript beacon fires on click, sends JSON `{ad_id, user_id, timestamp, metadata}` to capture endpoint
3. **Kafka**: Durable message queue decouples capture from processing. 10K-50K TPS well within Kafka's envelope. Retains data for reprocessing.
4. **Dual processing path**:
   - **Flink** (real-time stream processing): Continuous aggregation — CTR per ad, impressions per campaign, live dashboards. Low latency.
   - **Lambda / Task Runners** (event-driven): Custom aggregation queries, data enrichment, downstream integrations
5. **Reconciliation**: MapReduce on raw click data for deduplication and exact counts. Clicks can be captured multiple times (at-least-once); reconciliation corrects double-counting — critical because clicks directly affect advertiser billing.
6. **Dual storage**:
   - **Time Series DB** (InfluxDB, OpenTSDB): Real-time advertiser dashboards, low granularity
   - **OLAP DB** (BigQuery, Redshift): Historical analysis, invoice generation, campaign reports

**Deduplication**: View counts cannot be double-counted as they impact billing. Reconciliation via MapReduce on `(user_id, ad_id, time_window)` keys is the standard approach.

**Storage sizing**: 0.1KB/click × 1B clicks/day × 365 days ≈ 36.5TB/year for raw data; aggregated data is significantly smaller.

## Inventory Forecasting

Forecasting answers: "If I create this new campaign with these targeting parameters, how many impressions will it receive?"

**Naive approach**: Bucket historical traffic by targeting attributes, count. Unscalable — must be maintained separately from production logic.

**Simulation approach**: Replay historical impressions through the actual serving path with the new campaign "live." More accurate; reflects production behavior.

Optimization tricks for simulation performance:
- Downsample historical requests
- Disable non-essential server modules
- Parallelize across machines (each machine handles one new ad independently)
- Reuse recent forecasting data for existing ads, only simulate the new ad

Forecasting enables reach-and-frequency booking (guaranteeing N impressions to M unique users) and helps validate pacing systems.

## Reliability & Observability

- **Fallback**: If the ranking system fails, a default model (e.g., recency-sorted) must be in place
- **Canary deployment**: Route small traffic slice to new model before full rollout
- **Warm backup servers**: Pre-loaded with last known good index for instant failover
- **Metrics service**: Generic collectors → Kafka → Spark → dual routing to TSDB (real-time) and OLAP (historical). One pipeline, two destinations.

## Sources

- Aman Chadha, [Ad End to End](https://aman.ai/sysdes/adsEndToEnd/)
- Aman Chadha, [Ad Click Aggregator](https://aman.ai/sysdes/adclickeng/)
- Aman Chadha, [Ad Online Auction](https://aman.ai/sysdes/adonlineauction/)
