---
concept: Recommendation Systems
tags: [recsys, ml-system-design, retrieval, ranking, personalization]
sources:
  - kb/hard/raw/aman-ai/recommendation-systems-introduction.md
  - kb/hard/raw/aman-ai/recommendation-systems-system-design.md
  - kb/hard/raw/aman-ai/recommendation-systems-popular-architectures.md
  - kb/hard/raw/eugene-yan/system-design-for-recommendations-and-search.md
  - kb/hard/raw/eugene-yan/real-time-machine-learning-for-recommendations.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/two-tower-retrieval|Two-Tower Retrieval]]"
  - "[[hard/wiki/learning-to-rank|Learning to Rank]]"
  - "[[hard/wiki/recsys-embeddings|RecSys Embeddings]]"
  - "[[hard/wiki/reranking|Reranking]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Recommendation Systems

Recommendation systems are the backbone of product discovery at every major consumer platform — Netflix, YouTube, Spotify, Amazon, Pinterest. They match users to items across catalogs that range from thousands to billions, under strict latency budgets, using a multi-stage funnel that progressively narrows and refines candidates. Understanding this funnel end-to-end, including the offline/online split, is the core mental model for recsys system design.

## The Funnel Architecture

All production recommendation systems share the same structural insight: you cannot run your most accurate model against your entire catalog, so you filter progressively. Eugene Yan's canonical 2×2 framing captures this cleanly — two environments (offline vs. online) crossed with two processes (candidate retrieval vs. ranking).

**2-Stage (2×2) Model** — The simplest form:
1. **Retrieval**: Quickly narrows millions of items to hundreds of candidates, trading precision for speed. Typical methods include matrix factorization, two-tower neural networks, and approximate nearest neighbor (ANN) search.
2. **Ranking**: Applies a more expensive model to the smaller candidate set, incorporating richer features — user context, item metadata, cross features — to score and order candidates with higher precision.

**4-Stage (2×4) Model** (NVIDIA's extension) — Adds two intermediate steps for greater operational control:
1. **Retrieval** — broad, fast candidate generation
2. **Filtering** — business logic layer (remove out-of-stock items, enforce regional restrictions, user blocklists)
3. **Scoring** — deep model with full feature set, predicts interaction probability
4. **Ordering** — finalizes the list, balancing relevance with diversity, novelty, and business objectives (e.g., avoid filter bubbles, boost sponsored content within guardrails)

The filtering stage deserves explicit attention: business rules that belong there should not be baked into scoring models, which creates fragility and interpretability problems.

## Offline vs. Online Environments

**Offline environment** handles batch work: model training, building item embeddings, constructing ANN indices, and loading feature stores. These artifacts flow upward into the online environment. A critical discipline here is using the same feature store for offline training and online serving — this minimizes train-serve skew, including preventing data leakage from future features ("time travel").

**Online environment** serves real-time requests. A typical request flows left-to-right: input query/user is embedded → retrieval via ANN lookup → feature augmentation from the feature store → ranking model → optional reranking and post-processing.

The offline/online split determines where your latency budget sits. ANN lookup typically targets single-digit milliseconds. Full ranking pipelines are usually 50–200ms end-to-end. Instagram's three-pass ranking (distilled model → lightweight DNN → full DNN) is a canonical example of cascading model complexity within a tight budget.

## Architectural Patterns in Production

**Alibaba (Taobao)**: Session-based interactions mined to build a weighted item graph, random walk sequences, word2vec embeddings stored in a key-value i2i similarity map. Online: fetch recent user interactions → retrieve from similarity map → deep ranking (Wide & Deep, Behavioral Sequence Transformer).

**Facebook Search**: Two-tower model producing query and document embeddings offline. Documents quantized into FAISS ANN index. Online: query embedded → ANN retrieval with boolean filtering → ranked with full embeddings from a forward index.

**JD (e-commerce)**: Two-tower query-item model. Practical optimization: unified query embedding + ANN lookup in a single service instance to eliminate a network hop, reducing latency by half. Training data compression reduced storage 90% by loading user/item dictionaries into memory as lookup tables.

**LinkedIn Talent Search**: XGBoost as both a retrieval ranker (top 1000 candidates) and a feature generator for a downstream GLMix generalized linear model. Demonstrates that well-tuned gradient boosting remains competitive with neural approaches in lower-data regimes.

**DoorDash**: Knowledge graph (Neo4J) for query expansion — a query for "KFC" returns tags like "fried chicken" and "wings," enabling retrieval of similar restaurants like Popeyes. Shows that graph-based retrieval is a valid alternative to embedding+ANN.

## Production Considerations

**Latency**: ANN libraries (FAISS, ScaNN, hnswlib) trade recall for speed. At 1000 QPS, 30 m5.xlarge SageMaker instances with ScaNN can achieve p50=25ms, p99=65ms — real-time recsys is accessible without specialized infra. FAISS is optimized for batch queries; ScaNN outperforms for single-query serving.

**Real-time vs. batch**: Most use cases don't need real-time recommendations — batch is cheaper, operationally simpler (pre-computed into KV store), and more resilient (serving from cache even if compute fails). Real-time makes sense for mission-centric sessions (shopping with shifting intent), highly contextual consumption (YouTube within-day variety), cold-start scenarios, and fast-expiring content (news, ads).

**Cold start**: New users or items have no interaction history. Mitigations include demographic-based clustering for users, content-based features for new items, and deliberate exploration via [[hard/wiki/bandits-exploration-exploitation|Bandits]].

**Real-time feature updates**: Systems like Alibaba 1688 use streaming engines to update user preference weights (Swing i2i, category affinity) with each interaction. This enables recommendations to respond to in-session behavior without full model retraining. The tradeoff is significant operational complexity.

## Offline and Online Evaluation

**Offline metrics**: NDCG, Recall@k, Precision@k, AUC, MRR. These evaluate recommendations against historical interaction data.

**The observational/interventional gap**: The fundamental problem of recsys evaluation. Training on logged data learns `P(view3=iphone | view1=pixel, view2=galaxy)` but what we want is `P(click=True | recommend=iphone, view1=pixel)` — the interventional question. This is why offline metrics and online A/B tests frequently diverge. Counterfactual evaluation via IPS/SNIPS attempts to bridge this gap — see [[hard/wiki/counterfactual-evaluation|Counterfactual Evaluation]].

**Online metrics**: CTR, conversion rate, watch time, session length, revenue lift. A/B testing is the gold standard but has cycle time and deployment risk. The key discipline is always to define online success metrics — business outcomes, not just ML metrics — before shipping.

**Multi-objective ranking**: Production systems rarely optimize a single metric. YouTube moved from maximizing clicks (clickbait problem) to maximizing watch time, then to a balanced multi-objective approach. Multi-task learning with shared lower layers and separate output heads per objective allows simultaneous optimization of engagement, satisfaction, revenue, and diversity. The 4-stage ordering step is where these objectives are blended.

## Sources

- Aman.ai: [Recommendation Systems Introduction](https://aman.ai/recsys/intro/)
- Aman.ai: [System Design Cheatsheet](https://aman.ai/primers/ai/sys-design/)
- Aman.ai: [Popular Architectures](https://aman.ai/recsys/architectures/)
- Eugene Yan: [System Design for Recommendations and Search](https://eugeneyan.com/writing/system-design-for-discovery/)
- Eugene Yan: [Real-time Machine Learning for Recommendations](https://eugeneyan.com/writing/real-time-recommendations/)
