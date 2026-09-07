---
concept: Personalization Patterns
tags: [personalization, context-aware, user-signals, push-notifications]
sources:
  - kb/hard/raw/eugene-yan/patterns-for-personalization-in-recommendations-and-search.md
  - kb/hard/raw/eugene-yan/push-notifications-what-to-push-what-not-to-push-and-how-often.md
last_compiled: 2026-04-05
related: [recommendation-systems, feature-engineering, bandits-exploration-exploitation]
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Personalization Patterns

Personalization is the process of customizing each individual's experience. The same search query "Apple" should return different results for a software engineer and a chef. An electronics geek and a cooking hobbyist should see different homepage recommendations. This article catalogs the recurring patterns for achieving that, from continuous bandit exploration to graph-based user modeling, and extends the discussion to push notifications — a form of recommendation with distinctive constraints.

## Pattern 1: Bandits — Continuous Learning via Exploration

Multi-armed bandits balance exploration (trying new actions to learn their rewards) and exploitation (taking the action with the currently highest expected reward). They minimize cumulative regret: the gap between total reward obtained and what would have been obtained with perfect knowledge.

**Contextual bandits** extend this by observing context (user demographics, device, time of day, behavioral history) before selecting an action. They learn how context and actions jointly affect reward.

**Advantages over batch ML:**

- No waiting for data collection, model training, and A/B test conclusion. Bandits update continuously.
- Better for long-tail and cold-start scenarios where batch models fall back to popular items. Bandits continue to explore uncertain items.
- Lower regret — users benefit from better recommendations earlier.

**Netflix's contextual bandit for artwork personalization**: the bandit selects a show thumbnail from a set of candidates (action) and observes minutes played after the impression (reward). Context includes user's watch history, genre preferences, country, language, day of week, time of day. Offline evaluation uses *replay*: match the bandit's predicted image with randomly-served images from exploration, evaluate on matched pairs. The unbiased metric is quality plays / impressions.

**DoorDash's multi-level cuisine bandit**: explores cuisine types to learn user preferences, exploits to recommend favorites. Critically, uses **geolocation priors** at multiple levels (district, submarket, market, region). Cold-start users inherit the local prior until sufficient personal data accumulates. This balances individual preference with locally popular options.

**Spotify's contextual bandit for "recsplanations"**: jointly personalizes both the recommendation and the explanation for it. A factorization machine with 2nd-order interactions (embeddings + inner products) between recommendation, explanation, and user context outperformed plain logistic regression, which had no context-conditional behavior. Sample reweighting corrects for non-uniform recommendation probabilities in production.

**When to use bandits**: want to continuously explore while minimizing regret; long-tail or cold-start scenarios; personalizing non-content elements (thumbnails, notification copy, explanation text).

## Pattern 2: Embedding + MLP — Learning Embeddings, Pooling Them

Sparse input features (user IDs, item IDs, context) are mapped to dense embedding vectors. Variable-length behavioral sequences (watch history, purchase history) are compressed into fixed-length vectors via pooling. Everything is concatenated and fed through fully connected layers. The recommendation task is framed as classification — predict engagement probability via sigmoid, or item probability via softmax.

**TripAdvisor's experience recommender**: trains general-purpose 100-dim item embeddings with StarSpace (word2vec-style), fine-tunes for the experience recommendation task. Variable-length browsing histories are compressed via exponential recency-weighted average (most recent interactions weighted more heavily). Two ReLU layers (2048-dim, 512-dim) followed by softmax over 64,000 experiences.

**YouTube's two-stage system** (canonical reference):

*Candidate generation*: user interest represented by mean-pooled watch + search embeddings. Other features concatenated (geography, demographics, video age for freshness). Several ReLU layers → softmax over millions of videos. Negative sampling (several thousand negatives) for efficient training — 100x+ speedup over dense softmax. ANN search at serving time.

*Ranking*: video candidate from retrieval is concatenated with all other features. ReLU layers → sigmoid weighted by observed watch time (clickbait mitigation — short watches are down-weighted). Output is predicted watch time per video, used for ranking.

**Alibaba's Deep Interest Network (DIN)**: the key insight is that mean-pooling collapses diverse user interests into a single vector, obscuring which past behaviors are relevant for a given candidate ad. DIN inserts an attention layer between embedding and pooling, learning item-specific user representations. The attention layer weighs historical behaviors based on similarity to the candidate ad. Result: 2% offline AUC improvement, 10% online CTR improvement, 3.8% RPM improvement.

**When to use embedding+MLP**: starting with neural recommendation; good default. Upgrade to attention pooling (DIN-style) when users have diverse interests and item-specific user representations matter.

## Pattern 3: Sequential — Learning from Item Order

When the ordering of interactions matters — not just which items a user has engaged with, but the sequence and recency — sequential models capture that temporal structure.

**GRU-based session recommendation** (Telefonica): single GRU layer processes the current session item by item. The hidden state represents "what the user has been doing so far in this session." Works well for short session-level data without long historical context. Outperforms item-KNN on co-occurrence.

**Behavioral Sequence Transformer (BST)** (Alibaba): applies a Transformer encoder block to the user's full interaction history in the ranking stage. Position is encoded as the time difference between each interaction and the recommendation time — better than standard sinusoidal encodings for capturing recency. Single Transformer block (deeper led to overfitting). Output concatenated with other features before sigmoid. Achieved 4.5% CTR improvement over mean pooling.

**Spotify's session-level user embeddings**: learns embeddings per session (mean of track embeddings, with separate embeddings for played vs. skipped tracks). An LSTM learns across sessions, predicting the next session's embedding. The final user representation blends predicted session embedding with long-term embedding via learned attention weights.

**When to use sequential models**: have long-term user histories where sequence and recency matter; temporal patterns in user behavior (e.g., browsing history leading up to a purchase).

## Pattern 4: Graph — Learning from User/Item Neighborhoods

Graph-based approaches model the user-item interaction network directly. A user's embedding is enriched by their interaction history, the items they've interacted with, and the other users who interacted with the same items.

**Uber Eats' graph recommendation**: builds two bipartite graphs — user-dish (weighted by order count + rating) and user-restaurant. Applies GraphSAGE with mean/max pooling aggregation and sampling to limit computation. Weighted edges require a two-part hinge loss: strong edges (multiple orders) > weak edges (few orders) > non-edges, each by a margin. Dishes embedded via description + image features; restaurants via menu/cuisine features; a projection layer normalizes all node types to the same dimension.

**Alibaba's Graph Intention Network**: builds the user-item graph from session-level co-clicks. Applies diffusion (retrieve neighbors) and aggregation (attention over neighbors) to learn user intention. Reveals two relationship types: homogeneous groups (enrich user interests with sparse data) and complementary pairs (introduce serendipity).

**PinSage** (Pinterest): GraphSAGE variant for web-scale item embeddings. Aggregates from pin neighborhoods via random walks; scalable to billions of nodes and edges.

**When to use graphs**: sparse behavior data but rich relationships (social networks, item co-purchase graphs); want to leverage structural signals like mutual connections or item neighborhoods.

## Pattern 5: User Embeddings — Learning a Model of the User

Rather than representing users as a sequence or graph, learn a direct embedding for each user that encodes their overall preferences.

**Airbnb's user-type embeddings**: data sparsity problem — travel users book once or twice a year, not enough for user-level embeddings. Solution: learn user-type embeddings (based on location, device, language, past booking behavior) by interleaving them with listing sessions in a skip-gram model. User-type embeddings live in the same vector space as listing embeddings. Feature importance analysis showed user-type embeddings (86% coverage) far outperformed short-term user history features (8% coverage) for search ranking.

**Tencent's user lookalike model** for long-tail content: train user embeddings via click prediction on interaction history. Then learn a two-tower lookalike model: target user embedding vs. lookalike centroids (K-means with K=20). Global attention weighs lookalikes by overall quality; local attention weighs by similarity to target user's interests. The resulting lookalike recommendations surface long-tail content that would otherwise be buried by popularity bias.

**When to use user embeddings**: want generic embeddings reusable across multiple recommendation problems; personalizing long-tail content to users with sparse interaction data; when user-level model has sufficient coverage.

## Practical Selection Guide

Eugene Yan's heuristic for choosing which pattern to use:

| Goal | Pattern |
|------|---------|
| Continuously explore, minimize regret | Bandits |
| Simple neural recsys starting point | Embedding + MLP |
| Long-term user histories, temporal patterns matter | Sequential |
| Sparse behavior but rich relationships/metadata | Graphs |
| Generic embeddings across multiple problems | User embeddings |

**Starting baseline**: logistic regression with crossed features. Surprisingly strong and hard to beat. If building a real-time recommender (generates on request), word2vec-style item embeddings + ANN is lean and captures most of the value from session-level behavioral data.

## Push Notifications as Recommendation

Push notifications are a form of recommendation with four critical differences:

1. **Unknown intent**: unlike search (explicit query) or on-page recommendations (browsable context), push has no observable intent signal. The system guesses what the user might want from prior behavioral patterns.
2. **Form matters more than content**: Alibaba found that pushes explaining *why* an item is relevant (e.g., tying it to a recent purchase) outperform generic personalized recommendations by 44% in open rate. DPG Media found that transparency ("we're sending this because you subscribed to this topic") increased forgiveness when relevance missed.
3. **Disengagement is permanent**: an irrelevant push risks notification disable, app uninstall, or habitual ignoring. This is a one-way door.
4. **Tight constraints**: single-item slots, message caps (daily/weekly limits), timeliness requirements (breaking news decays fast), timeliness of the recommendation lifecycle.

**What to push — being helpful:**

*Complementary products* (Alibaba): recommend products that complete a past purchase rather than substitutes. Substitute recommendations annoy users (they already own the alternative). Complementary recommendations feel additive. A complement score minus substitute score identifies strongly complementary pairs.

*Power users vs. regular users* (JOOL Health): highly active users preferred personalized insights ("your willpower outlook is high tomorrow"). New/regular users preferred generic suggestions. Personalized insights require historical depth — they don't work for new users because there isn't enough data to make them meaningful.

*Recovering/sleeping bandits* (Duolingo): template arms decay in expected reward the more recently they were shown to a user (recovering bandit). Some templates are ineligible if a user isn't on a streak or hasn't indicated a relevant preference (sleeping bandit). This approach increased DAU by 0.5% and new user retention by 2%.

**What not to push — being harmless:**

*LinkedIn's filter-eligible notifications*: events in the user's network (shares, mentions, connections in the news) are filter-eligible — high volume, lower signal. A response prediction model trained on historical push engagement filters notifications likely to be ignored. Retrieval step first selects candidate recipients via edge affinity and connection strength; ranking step then filters on predicted engagement.

*Pinterest's unsubscribe prediction*: rather than predicting engagement, Pinterest predicts whether a push will cause the user to unsubscribe. Training data labels are collected with a 4-week delay (enough for user activity to stabilize). The key insight: train on the *assigned* notification volume, not the *actual* volume sent (avoids survivorship bias — users who unsubscribed received fewer notifications, not because they wanted fewer, but because they stopped receiving them).

**Volume control — how many to push:**

*Pinterest*: for each user, compute the optimal budget where incremental value from additional notifications is maximized. Models three components: probability of unsubscribing, long-term activity of unsubscribed users, predicted activity of subscribed users. Result: 6-24% reduction in notification volume, 11-31% increase in CTR, 1-3% increase in site engagement. Shifted volume from core users (fewer) to marginal users (more), improving retention of at-risk users.

*Twitter*: HMM with six states segments users by notification engagement behavior. Grid search over A/B tests finds optimal push cap per state. Augmented by a neural network predicting long-term utility with a two-month delay for labels. Reward function: `U(c) = Σ(logins|x,c) + α·p(reachability|x,c)`. Increased DAU by 0.62% on iOS.

## Sources

- Eugene Yan — [Patterns for Personalization in Recommendations and Search](https://eugeneyan.com/writing/patterns-for-personalization/)
- Eugene Yan — [Push Notifications: What to Push, What Not to Push, and How Often](https://eugeneyan.com/writing/push/)
