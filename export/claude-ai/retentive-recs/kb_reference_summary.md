# Knowledge Base Reference Summary

Condensed summaries of KB articles directly relevant to the Retentive Recommendations blog post and KDD paper. Use these for grounding claims, citing prior work, and framing technical context. Full articles live in `kb/` in the Leo repo.

---

## 1. RecSys Beyond Accuracy (Serendipity, Diversity, Novelty)

**Sources:** Eugene Yan — "Serendipity: Accuracy's Unpopular Best Friend," "RL for Recs and Search," "RecSys 2022 Keynote"

Accuracy alone (NDCG, AUC, recall@k) is insufficient. Systems that only optimize short-term click relevance produce boring recommendations, concentrate attention on popular items, and cause long-term churn. Four beyond-accuracy metrics matter:

- **Diversity:** How different are recommended items from each other? Measured by average pairwise embedding distance or category coverage.
- **Novelty:** How rare/unusual are the recommendations? `Novelty(i) = -log2(P(recommended i))`.
- **Unexpectedness:** How different from what the user usually sees? Cosine distance between recommended and historical items.
- **Serendipity:** Unexpectedness × Relevance. An unexpected item the user *engages with*. `Serendipity = (1/|U|) Σ Unexpectedness(i) × Relevance(i)`.

**Key insight for Retentive Recs:** The offline-online gap is especially wide for serendipity. Systems that look worse offline on relevance but better online on engagement/return rate should win. A/B testing is the only trustworthy signal. This validates the program's approach of optimizing for retention (WAU) rather than point-wise accuracy.

**Business case:** In e-commerce, poor diversity creates power-law concentration (5% of products drive 95% of revenue). In content, it starves the creator ecosystem. Deliberately surfacing long-tail items via exploration collects training signal that accuracy-only systems never generate — a cold-start virtuous cycle.

---

## 2. Bandits & Exploration-Exploitation

**Sources:** Lilian Weng — "The Multi-Armed Bandit Problem," Eugene Yan — "Bandits for Recommender Systems," Aman.ai — "Multi-Armed Bandits"

Bandits model uncertainty explicitly and explore items with low confidence, learning faster than pure exploitation while minimizing regret (the opportunity cost of suboptimal actions).

**Core algorithms:**
- **Epsilon-greedy:** Random exploration with probability epsilon. Simple but unguided — wastes exploration budget on clearly bad arms.
- **UCB (Upper Confidence Bound):** "Optimism in the face of uncertainty." Select arm with highest estimated value + confidence interval. Degrades with delayed feedback (herding problem).
- **Thompson Sampling:** Sample from each arm's posterior distribution (Beta for binary rewards), pick highest sample. Robust to delayed feedback. Preferred in production.

**Thompson Sampling details (directly relevant to Geometric Bandit):**
- Binary rewards: `Beta(alpha, beta)` where alpha = successes, beta = failures. Mean = alpha/(alpha+beta).
- As data accumulates, distribution narrows — exploration naturally decreases.
- DoorDash warm-starts from regional priors (hierarchical: regional -> subregional -> user).
- Deezer found pessimistic initialization `Beta(1, 99)` outperformed naive `Beta(1, 1)`.

**Contextual bandits:** Condition on user/context features. LinUCB uses ridge regression per arm. Yahoo reduced 1,200 user features to 5 via PCA. Deezer found user clustering (100 k-means groups) outperformed per-user bandits — semi-personalization beats full personalization in low-data regimes.

**Off-policy evaluation:** The replay method (Li et al., 2011) — requires logged data from near-uniform policy. Twitter found PR-AUC and CTR diverge: greedy policies score high on PR-AUC but low on actual CTR. Conventional supervised evaluation on biased logged data doesn't predict real-world policy value.

---

## 3. Recommendation Systems (Funnel Architecture)

**Sources:** Aman.ai — Intro, System Design, Popular Architectures; Eugene Yan — System Design for Discovery, Real-time ML

All production recsys share a funnel: retrieval (millions -> hundreds) -> ranking (hundreds -> tens) -> reranking/ordering. You can't run your best model against the full catalog.

**4-stage model:** Retrieval -> Filtering (business rules) -> Scoring (deep model) -> Ordering (diversity, novelty, business objectives).

**Offline vs. online split:** Same feature store for training and serving prevents train-serve skew. ANN lookup targets single-digit ms. Full ranking pipeline: 50-200ms.

**Multi-objective ranking:** YouTube moved from maximizing clicks (clickbait) to watch time, then balanced multi-objective. Multi-task learning with shared lower layers and separate heads per objective. The ordering step blends these.

**Real-time vs. batch:** Most use cases don't need real-time. Real-time matters for: shifting session intent, contextual consumption (YouTube variety), cold-start, fast-expiring content. Retentive Recs' UIC-based approach is batch-computed (GSS Feature Store) with session-level signal incorporated.

---

## 4. RecSys Embeddings & Collaborative Filtering

**Sources:** Aman.ai — Candidate Generation, Cold Start, GNNs

**Matrix Factorization:** Decomposes user-item interaction matrix R into U * V^T. User and item embeddings; dot product predicts engagement. WALS parallelizes efficiently for distributed compute.

**Neural CF (NCF):** Replaces dot product with MLP. Embedding + MLP is ubiquitous in industry. Key: attention-weighted pooling (DIN) learns item-specific user representations — 10% CTR gain over mean pooling.

**Sequential models:** GRU for session-level; BST (Behavioral Sequence Transformer) for full history with time-difference positional encoding. SASRec (GPT-style autoregressive) is the standard strong baseline.

**GNNs:** PinSage (Pinterest) — GraphSAGE variant, web-scale item embeddings via random walks. Billions of nodes. LightGCN removes transformation layers, keeps only aggregation — simpler is better for CF.

**Cold start:** Content-based features for new items, demographic clustering for new users, bandits for controlled exploration, feature hashing for new vocabulary. GraphSAGE is inductive — generates embeddings for unseen nodes.

---

## 5. Two-Tower Retrieval

**Sources:** Aman.ai — Video Rec System Design, YouTube Search, Embeddings, Airbnb Listings

Two-tower (dual encoder): separate query and item towers, dot product similarity, ANN serving. Towers cannot interact at inference — enables pre-computation across billion-scale catalogs.

**Training:** Contrastive loss (InfoNCE). Hard negatives critical — Airbnb added same-region negatives because random negatives were too easy. Global context as training signal: Airbnb adds "eventually booked listing" as persistent positive.

**ANN serving:** FAISS (batch), ScaNN (single-query), HNSW (graph-based). Typical: recall@100 > 0.95 with <10ms latency. Product quantization reduces memory.

**Cross-tower limitation:** Can't model fine-grained query-item interactions. This is why two-tower is retrieval (recall) not ranking (precision). Deep interaction models (Wide & Deep, DCN, DIN) handle ranking on the small candidate set.

**Pinterest context:** CLR and UPP are architecturally two-tower. Key complexity: real-time user representation updates for session-level intent shifts.

---

## 6. RecSys Evaluation & Bias

**Sources:** Aman.ai — Eval Metrics, Calibration; Eugene Yan — Position Bias

**Offline metrics:** Recall@K (retrieval ceiling), Precision@K, NDCG (rank-weighted relevance), MRR (first relevant item), MAP@N.

**Online metrics:** CTR (gameable), CVR, dwell time/session length, DAU/WAU/MAU (slow to move, noisy).

**Position bias:** Self-reinforcing — top items get more clicks, look more relevant, stay on top. Mitigations: inverse position weighting (IPW), positional features at training time set to neutral at inference (Google Rule 36), propensity scoring.

**Popularity bias:** Logit adjustment — subtract log(P(item)) from raw logit.

**Duration bias:** Quantile-based watch-time prediction removes confound between content quality and video length.

**Calibration:** Platt scaling (sigmoid fit), isotonic regression (non-parametric), Bayesian (BBQ). Critical when blending scores from multiple models — miscalibrated scores break blending weights.

**Offline-online gap:** The most dangerous situation is offline improvement without online improvement. Causes: temporal leakage, covariate shift, metrics that don't capture what users care about, position bias exploitation.

---

## 7. Personalization Patterns

**Sources:** Eugene Yan — "Patterns for Personalization," "Push Notifications"

Five patterns for personalizing recommendations:

1. **Bandits** — continuous learning, minimize regret, best for fast-changing catalogs and long-tail.
2. **Embedding + MLP** — the default starting point. Upgrade to DIN-style attention when interests are diverse.
3. **Sequential** — when order and recency matter. BST for long histories; GRU for sessions.
4. **Graph** — when behavior is sparse but relationships are rich. PinSage for web-scale.
5. **User embeddings** — reusable across problems. Airbnb user-type embeddings (86% coverage) outperformed short-term history (8%).

**Starting baseline:** Logistic regression with crossed features. "Surprisingly strong and hard to beat."

**Push notifications as recommendation:** Unknown intent, form matters more than content (Alibaba: relevance explanations +44% open rate), disengagement is permanent (one-way door). Pinterest predicts unsubscribe rather than engagement — trains on assigned volume to avoid survivorship bias.

---

## 8. Reinforcement Learning (Foundations)

**Sources:** Lilian Weng — "A Long Peek into RL," "Policy Gradient Algorithms"; Karpathy — "Deep RL: Pong from Pixels"; Aman.ai — CS229 RL

**MDP formulation:** States, actions, transition probabilities, rewards, discount factor. Policy pi(a|s) maximizes expected discounted return.

**Value-based (Q-learning / DQN):** Learn Q(s,a) and act greedily. DQN: neural Q-function, experience replay, frozen target network. Off-policy — learns from stored transitions.

**Policy gradient (REINFORCE / PPO):** Directly optimize the policy. REINFORCE: increase probability of actions proportional to their advantage. High variance — baseline (V(s)) reduces it. PPO: clips importance sampling ratio to prevent catastrophic updates. Dominant practical algorithm. Used in RLHF.

**Actor-critic (A2C):** Actor (policy) + critic (value function). Critic provides low-variance advantage estimates. Multiple parallel workers improve sample diversity.

**Explore vs. exploit:** Epsilon-greedy, entropy bonus, UCB. The fundamental tension: exploit known good actions vs. explore uncertain ones.

**Credit assignment:** Which earlier action caused a delayed reward? Discounted returns + return normalization address this.

**Connection to Retentive Recs:** The Geometric Bandit (Section 6 of retentive_recs.md) operates in the contextual bandit regime — stateless, no delayed credit assignment, updates from single interactions. This is deliberately simpler than full RL, sidestepping the compounding challenges of high-dimensional action spaces, non-stationarity, and off-policy training that make full RL deployment in recsys rare.

---

## Source Index

### Wiki articles (compiled concept syntheses)
| Article | Path in Leo repo |
|---------|-----------------|
| RecSys Beyond Accuracy | `kb/hard/wiki/recsys-beyond-accuracy.md` |
| Bandits & Exploration-Exploitation | `kb/hard/wiki/bandits-exploration-exploitation.md` |
| Recommendation Systems | `kb/hard/wiki/recommendation-systems.md` |
| RecSys Embeddings & CF | `kb/hard/wiki/recsys-embeddings.md` |
| Two-Tower Retrieval | `kb/hard/wiki/two-tower-retrieval.md` |
| RecSys Evaluation & Bias | `kb/hard/wiki/recsys-evaluation.md` |
| Personalization Patterns | `kb/hard/wiki/personalization-patterns.md` |
| Reinforcement Learning | `kb/hard/wiki/reinforcement-learning.md` |

### Raw source articles (deep dives)
| Article | Author | Path in Leo repo |
|---------|--------|-----------------|
| Serendipity: Accuracy's Unpopular Best Friend | Eugene Yan | `kb/hard/raw/eugene-yan/serendipity-accuracys-unpopular-best-friend-in-recommenders.md` |
| Bandits for Recommender Systems | Eugene Yan | `kb/hard/raw/eugene-yan/bandits-for-recommender-systems.md` |
| RL for Recommendations and Search | Eugene Yan | `kb/hard/raw/eugene-yan/reinforcement-learning-for-recommendations-and-search.md` |
| Counterfactual Evaluation for Rec Systems | Eugene Yan | `kb/hard/raw/eugene-yan/counterfactual-evaluation-for-recommendation-systems.md` |
| The Multi-Armed Bandit Problem | Lilian Weng | `kb/hard/raw/lilian-weng/the-multi-armed-bandit-problem-and-its-solutions.md` |
| Recommendation Systems: Multi-Armed Bandits | Aman.ai | `kb/hard/raw/aman-ai/recommendation-systems-multi-armed-bandits.md` |
| Recommendation Systems: Candidate Generation | Aman.ai | `kb/hard/raw/aman-ai/recommendation-systems-candidate-generation.md` |
| Recommendation Systems: Eval Metrics and Loss | Aman.ai | `kb/hard/raw/aman-ai/recommendation-systems-eval-metrics-and-loss.md` |
| Patterns for Personalization | Eugene Yan | `kb/hard/raw/eugene-yan/patterns-for-personalization-in-recommendations-and-search.md` |
