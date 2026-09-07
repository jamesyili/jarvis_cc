---
concept: ML System Design Framework
tags: [system-design, interview, ml-pipeline, scoping, evaluation]
sources:
  - kb/hard/raw/eugene-yan/the-metagame-of-applying-machine-learning.md
  - kb/hard/raw/eugene-yan/how-to-write-design-docs-for-machine-learning-systems.md
  - kb/hard/raw/aman-ai/chapter-2-youtube-video-search.md
last_compiled: 2026-04-05
related: [recommendation-systems, feature-engineering, mlops-monitoring]
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# ML System Design Framework

The gap between knowing machine learning and applying it in industry is large — and mostly ignored in academic training. "Knowing ML" is the game; applying it at work is the metagame. This framework covers both: the structured approach to designing ML systems (for interviews and actual work) and the operational principles that separate ML practitioners who ship from those who don't.

## The Metagame: What Actually Determines Success

Before the framework: four overarching principles that apply to every ML system design problem.

### 1. Start From the Problem, Not the Tech

Never optimize for exciting technology over customer or business value. Dig past the surface request. Eugene Yan's logistics example: someone requested "boost FBL products in ranking." Ask why? "Faster delivery." Ask why? "Fewer complaints about late deliveries." The root problem was delivery forecasting, not ranking. Solving ranking would have been the wrong project.

How you _frame_ the problem is half the solution. Fraud detection can be unsupervised (isolation forests, graph clustering) or supervised (requires labeled data, human-in-loop). Each frame leads to a completely different system. Getting the frame right has outsized returns.

### 2. More System and Data Design, Less Model Design

Overall system design matters more than model architecture. Model performance depends more on the data you feed it than the architecture you choose. The famous "Hidden Technical Debt in Machine Learning Systems" paper makes this point visually.

**Negative examples of over-engineering**: Adding Kafka, Redis, and Lambda to a 3-person team's stack when Spark + Airflow was sufficient. Every extra component is an ops burden that compounds. Monzo's feature store was just a BigQuery → Cassandra periodic dump — no real-time processing. Simplest solution that solves the problem.

**Key data design decisions**:
- How to generate training labels (click data, purchase data, expert labels, crowdsourced)
- How to design negative samples — this is more art than science. Facebook: random negatives outperformed impressed-but-not-clicked for retrieval. Amazon: the opposite. JD: 50/50 mix worked best. No universal rule.
- Whether to use sequence-based or tabular representations (word2vec paradigm applied to user behavioral sequences has driven major industry gains)

### 3. Clarity About Objectives and Measurements

Don't confuse lower loss with better product. Offline metric improvement is not the same as A/B test improvement. The best proxy for production is a fast A/B testing pipeline, not a better offline metric.

Sean Taylor's rule: "If I had an hour to build a model, I'd spend 55 minutes building a fast and unambiguous evaluation procedure and 5 minutes trying out models."

Measurement period matters: short-term (session CTR) vs. long-term (customer lifetime value, retention). These can conflict — products that convert well in the short term may harm long-term engagement. Be explicit about which you're optimizing and why.

### 4. Modular > All-In-One

Multiple specialized models typically outperform one big model. Two-stage retrieval-then-ranking is industry standard for a reason: retrieval focuses on recall at scale, ranking focuses on precision over a small candidate set. Separate teams can iterate independently. Failures are isolated.

Exception: when you've exhausted the modular approach. Baidu combined retrieval+ranking into a single model when the modular version bottlenecked. TenCent moved to multi-task training for simultaneous click/watch/share optimization. These are sequels to a successful modular deployment, not the starting point.

---

## The Design Framework: Six Steps

### Step 1: Clarify Requirements and Scope

Before designing anything, nail down the problem boundaries through structured questions:

**Business/product questions**:
- What is the customer or business benefit?
- What are the success criteria? (Engagement, revenue, latency, cost reduction?)
- What's in scope vs. out of scope for this version?

**Scale questions**:
- How many items/users/documents? (Guides whether ANN is needed, whether batching is viable)
- Expected QPS? P99 latency budget?
- What data is available for training?

**Constraints**:
- Data privacy requirements (PII, GDPR)?
- Latency requirements? (Real-time vs. near-real-time vs. batch)
- Cost budget?

**YouTube video search example** (aman.ai):
- Input: text queries only (no multimodal input)
- Content: 1 billion videos
- Data: 10M labeled (video, query) pairs
- Personalization: not required
- Language: English only

These constraints directly determine the architecture. 1B videos → you need ANN indexing. No personalization → simpler ranking. Text-only queries → simpler query encoding.

### Step 2: Frame as an ML Task

Explicitly state the ML formulation:

- **Input/output**: What goes in, what comes out
- **ML category**: Ranking (pointwise/pairwise/listwise), classification, regression, generation, retrieval
- **Surrogate problem**: The label you can collect that proxies the real objective. Netflix: "predict ratings" was the stated objective, but "predict probability of watch" or "predict minutes watched" might be better surrogates. The surrogate choice has outsized impact on A/B test outcomes.
- **Objective function**: What loss you'll train on and why

Common framings:
- Recommendations: User-item score → ranking (two-stage: retrieval + ranking)
- Search: Query-document relevance → ranking
- Fraud detection: Transaction → binary classification (or unsupervised outlier detection)
- Content moderation: Text/image → multi-class classification

### Step 3: Data Strategy

**Training data**:
- Where does it come from? (User behavioral logs, expert labels, crowdsourcing, synthetic)
- What are the coverage gaps? (New items, new users, rare queries)
- How are labels defined? (Clicks, purchases, completions — be explicit about the signal quality)

**Negative samples**:
- For ranking/retrieval: how are negatives generated? Random, hard negatives, in-batch negatives, or impressed-but-not-clicked?
- The choice has a large impact on what the model learns (see Facebook vs. Amazon disagreement in [[hard/wiki/search-systems|Search Systems]])

**Feature engineering**:
- What user features? (Demographics, behavioral history, session context)
- What item features? (Metadata, content embeddings, statistical features)
- What interaction features? (Recency, frequency, diversity)

For unstructured data (text, images, video):
- Text → normalize → tokenize → token IDs (lookup table or hashing for OOV)
- Images → CNN embeddings or ViT
- Video → frame-level models (3D CNN, transformers) or video-level aggregation

### Step 4: Model Selection and Architecture

**Principles**:
- Start simple. A decision tree or logistic regression baseline is both a sanity check and sometimes the best model.
- More data usually beats better architecture. Spend effort on data quality before architecture search.
- If using deep learning for retrieval: two-tower (bi-encoder) is the standard for embedding-based retrieval. Cross-encoders are more accurate but too slow for first-stage retrieval.
- Model selection should follow from the problem framing. Don't pick BERT because it's exciting — pick it because the task benefits from contextual text understanding.

For the YouTube search case:
- Visual search: Two-tower (video encoder + text encoder), dot product similarity, ANN index over video embeddings
- Text search: Inverted index (Elasticsearch) over titles, descriptions, tags
- Fusion: Combine ranked lists from both paths

### Step 5: Evaluation Plan

**Offline evaluation**:
- Data split: For recsys and search, use **temporal split** (not random). Random splits allow future data to inform past predictions — this inflates offline metrics vs. production reality.
- For retrieval/search: Recall@k, Precision@k, MRR, NDCG
- For ranking: NDCG, AUC, calibration
- For generation: Task-specific metrics + LLM-as-judge

**Online A/B testing**:
- Define success metrics (primary) and guardrail metrics (floor constraints that cannot regress)
- Specify treatment/control split unit: user-level, session-level, or item-level
- Minimum detectable effect and required sample size
- Novelty effect monitoring: new features often show inflated positive effects in the first week; allow for settling period

**The offline-online gap is real**: don't kill a model just because offline metrics are neutral. Ship and measure.

### Step 6: Serving Architecture

Key components to specify:

**Data pipeline**: How raw data flows to features → training dataset → model training → model artifact

**Serving pipeline**:
- Pre-computation vs. real-time: Precompute item embeddings offline (batch). Compute user embeddings in real-time (or near-real-time from cached user features).
- Feature serving: Feature store for low-latency feature retrieval (Cassandra, Redis, DynamoDB)
- Model serving: API endpoint (SageMaker, Triton, vLLM for generative)
- ANN index: FAISS/Hnswlib/Pinecone for embedding retrieval

**Monitoring**:
- Model metrics: prediction drift, feature distribution shift, AUC degradation
- System metrics: latency (p50/p95/p99), error rate, throughput
- Business metrics: CTR, conversion, revenue per session
- Alarms and on-call procedures

**Scalability**:
- Horizontal vs. vertical scaling for each component
- Caching layers (semantic cache for LLM responses, feature cache, result cache)
- Latency budget decomposed by component

---

## Design Doc Structure

For real ML system design work (not interview), use the Why/What/How framework:

**Why**: Business case, customer benefit, motivation. Why now? Why not improve the existing system?

**What**:
- Success criteria (business goals, operational goals)
- Functional requirements (from customer perspective)
- Non-functional requirements (latency, throughput, security, cost)
- Scope: what's in/out

**How (Methodology)**:
- Problem statement and ML framing
- Data: sources, entities, features
- Techniques: baselines + proposed approaches
- Validation: offline metrics, experiment design, A/B test plan
- Human-in-the-loop: where manual override or review is needed

**How (Implementation)**:
- High-level architecture diagram (data flow diagram)
- Infrastructure choices (cloud/on-prem, training infra, serving infra)
- Performance targets (throughput, latency)
- Security and data privacy
- Monitoring and alarms
- Cost estimate

**Alternatives considered**: Document what was rejected and why. If assumptions change, this section guides revisiting.

---

## Interview Checklist

For ML system design interviews, use this progression:

1. **Clarify** (5 min): Ask scale, data, constraints, and personalization questions.
2. **Frame** (3 min): State ML task, input/output, surrogate problem explicitly.
3. **Data** (5 min): Training data sources, feature engineering, negative sampling strategy.
4. **Architecture** (10 min): Model selection with justification, two-tower for retrieval, ranking stage, serving pipeline.
5. **Evaluation** (5 min): Offline metrics (with split strategy), online A/B test design, guardrail metrics.
6. **Deep dive** (5-10 min): Latency optimization, cold start handling, scale challenges.

Signal to show throughout: you understand the business objective, not just the ML mechanics.

## Sources

- Eugene Yan: [The Metagame of Applying Machine Learning](https://eugeneyan.com/writing/machine-learning-metagame/)
- Eugene Yan: [How to Write Design Docs for Machine Learning Systems](https://eugeneyan.com/writing/ml-design-docs/)
- Aman.ai: [Chapter 2 — YouTube Video Search](https://aman.ai/h/des/youtube-video-search/)
