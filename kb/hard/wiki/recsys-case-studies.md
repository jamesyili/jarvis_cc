---
concept: Applied RecSys Case Studies
tags: [case-studies, youtube, airbnb, linkedin, pinterest, system-design]
sources:
  - kb/hard/raw/aman-ai/chapter-6-video-recommendation-system.md
  - kb/hard/raw/aman-ai/chapter-10-personalized-news-feed.md
  - kb/hard/raw/aman-ai/chapter-11-people-you-may-know.md
  - kb/hard/raw/aman-ai/chapter-9-similar-listings-on-vacation-rental-platforms.md
  - kb/hard/raw/aman-ai/chapter-7-event-recommendation-system.md
last_compiled: 2026-04-05
related: [recommendation-systems, two-tower-retrieval, feature-engineering]
---

# Applied RecSys Case Studies

Five end-to-end system designs drawn from interview preparation material, modeled after real-world systems at YouTube, Facebook, LinkedIn, Airbnb, and Eventbrite. Each case study follows the ML system design loop: clarify requirements → frame the ML problem → data and feature engineering → model development → evaluation → serving.

## Case Study 1: Video Recommendation System (YouTube-style)

**Business objective**: maximize user engagement on the homepage. Translating business objective to ML objective: maximize the number of relevant videos (user watches ≥50% or explicitly likes), not just clicks (clickbait risk) or completion (biases toward short videos) or watch time (biases toward long videos).

**Scale**: 10 billion videos, global users, <200ms latency.

**Architecture choice**: hybrid filtering. CF-based model for candidate generation (no domain knowledge needed, discovers cross-interest), content-based model for ranking (handles cold-start new videos, captures specific user interests).

**Feature pipeline:**

- *Video features*: ID, length, manual tags, title (BERT/CLIP embedding), views, likes, language
- *User features*: demographics, location, timezone, historical watch/search sequences (mean-pooled into fixed-length vectors)
- *Contextual features*: age of video (freshness), time of request

**Model development (two stages):**

1. **Candidate generation** — matrix factorization or two-tower neural network. For two-tower: user tower (embed user history, demographics, context), item tower (embed video features). Train with in-batch negative sampling. At serving: compute user embedding, ANN search against pre-computed item embeddings.
2. **Ranking** — deeper model with full feature set. Weighted logistic regression (watch time as weight) to avoid clickbait. Or DNN with sigmoid predicting engagement probability weighted by observed watch time.

**Key trade-offs: MF vs two-tower neural network:**

| Dimension | Matrix Factorization | Two-Tower NN |
|-----------|---------------------|--------------|
| Can use item features | No | Yes |
| Cold start | Poor | Better |
| Scalability | Good | Good |
| Expressiveness | Limited (linear) | Higher (nonlinear) |

**Serving pipeline:**
1. Candidate generation service (retrieve ~500-1000 candidates via ANN)
2. Scoring service (rank with deep model)
3. Reranking service (apply diversity, freshness, fairness constraints)

**Cold start handling**: fall back to content-based filtering for new videos. Use demographics and popular items for new users.

**Challenges**: serving speed (ANN index updates), diversity (greedy embedding similarity produces homogeneous slates), training scalability (billion-scale interaction logs).

---

## Case Study 2: Personalized News Feed (Facebook-style)

**Business objective**: maximize user engagement; increase platform revenue via ad exposure. Feed shows unseen posts and posts with unseen comments, personalized by engagement score.

**ML objective**: maximize a weighted score across multiple reaction types — not single-signal (click-only leads to clickbait; like-only has too little data):

| Reaction | Example weight | Notes |
|----------|---------------|-------|
| Click | 1 | Implicit, abundant |
| Like | 5 | Explicit positive signal |
| Comment | 10 | Strong engagement |
| Share | 20 | Viral signal |
| Hide | -20 | Negative; reduces score |
| Block | -50 | Strong negative |

Engagement score = Σ(predicted probability × reaction weight). Multiple binary classifiers predict each reaction probability independently; scores are summed with weights.

**Feature pipeline:**

- *Post features*: textual content (BERT embedding), images/videos (ResNet/CLIP embedding), reaction counts, hashtags (feature-hashed + TF-IDF), post age (bucketized)
- *User features*: demographics, timezone, number of connections, account age
- *User-author affinity*: profile views between users, mutual connections, frequency of past interactions with this author, close friend / family member flags
- *Friendship table*: explicit relationship strength features

**Model**: pointwise Learning to Rank (LTR). DNN with concatenated feature embeddings; multiple heads for passive users (fewer interaction signals). Cross-entropy loss for each reaction classifier.

**Serving**: prediction pipeline must run in <200ms for 2B DAU checking feed twice daily. Pre-computation of post scores at ingestion time, with online re-scoring at request time using freshness/context features.

**Offline metrics**: NDCG across all posts in test set, F1 per reaction classifier. **Online metrics**: CTR, likes per session, session length, DAU.

---

## Case Study 3: People You May Know (LinkedIn-style)

**Business objective**: maximize formed connections to grow user networks.

**Scale**: 1B total users, 300M DAU, 1000 connections per user average.

**Problem framing**: edge prediction on the social graph — predict whether an edge (connection) will form between two nodes (users). Two approaches:

1. **Pointwise LTR**: binary classifier taking two user profiles as input, predicts connection probability. Simple but ignores social graph structure.
2. **Edge prediction with GNNs**: incorporates k-hop neighborhoods. If user A and user B have 4 mutual connections who are also interconnected, they're far more likely to connect than if they share 0 mutual connections. GNNs propagate this structural signal into node embeddings.

**Features:**

- *User features*: demographics, schools attended (standardized), companies, industry, number of connections/followers, account age
- *User-user affinity*:
  - **Mutual connections** — strongest single predictor
  - **Time-discounted mutual connections** — mutual connections formed long ago decay; recent connections indicate active, growing overlapping networks
  - **Education/work affinity**: same school, overlapping years, same major, companies in common, same industry
  - **Social affinity**: profile views (target user viewed candidate's profile), interaction frequency

**Model**: GNN (GraphSAGE-style) for edge prediction. Takes social graph + node features as input. Predicts connection probability for (user A, user B) pairs.

**Serving challenges:**
- 1B users makes exhaustive scoring infeasible
- **Friend-of-Friend (FoF) filtering**: only score pairs sharing mutual connections (dramatically reduces candidate space — most likely connections are FoFs)
- **Pre-computation**: since the social graph changes slowly, PYMK scores can be pre-computed offline and cached. Update on trigger events (new connection formed, profile update)

**PYMK generation pipeline**: offline batch job generates candidate PYMK lists per user → online prediction pipeline scores and ranks on request → cached results served with TTL.

**Offline metrics**: precision@K, recall@K for connection formation. **Online metrics**: connection acceptance rate, number of connections formed.

---

## Case Study 4: Similar Listings on Vacation Rental Platforms (Airbnb-style)

**Business objective**: increase bookings by helping users discover similar relevant listings.

**Key insight**: this is a **session-based recommendation** problem, not a traditional long-term preference problem. Users browsing listings in a session have short-term, context-dependent interests — price range, neighborhood, number of guests. Long-term user models are less relevant than the current browsing session.

**ML objective**: predict which listing the user will click next, given the listing currently viewed.

**Approach**: learn listing embeddings via co-occurrence in browsing sessions (word2vec-style skip-gram). Two listings that frequently appear in the same user session get similar embedding vectors.

**Training data**: extract search sessions — sequences of clicked listing IDs ending in a booked listing. Each session forms a window of (context listing, positive listing) pairs. Train a shallow neural network to predict co-occurring listings given a context listing.

**Loss function improvements:**
- **Booked listing as global context**: the eventually-booked listing is included as a global positive signal in every training window within the session. This biases embeddings toward bookable properties.
- **Hard negatives from same region**: random negatives are easy (listings in different cities). Add negatives from the same city/neighborhood to force finer-grained discrimination.

**Serving pipeline:**
1. *Training pipeline*: batch retraining on new session data (daily/weekly)
2. *Indexing pipeline*: compute embeddings for all listings → store in ANN index
3. *Prediction pipeline*:
   - **Embedding fetcher service**: fetch embedding for the currently viewed listing
   - **Nearest neighbor service**: ANN search against the index
   - **Re-ranking service**: apply business rules (block duplicate hosts, enforce regional diversity)

**Offline metrics**: MRR, recall@K for predicting the eventual booking from the session. **Online metrics**: click-through rate on similar listings widget, bookings attributed to the widget.

---

## Case Study 5: Event Recommendation System (Eventbrite-style)

**Business objective**: maximize ticket sales. ML objective: maximize event registrations.

**Key domain characteristics**: events are **ephemeral** (one-time occurrences that expire), **location-dependent** (nearby events are strongly preferred), and **social** (friend attendance drives registration). These characteristics demand specialized features.

**Feature categories:**

*Location features*:
- Distance and travel time from user's location to event (via Google Maps API)
- Whether event is in user's home city vs. travel destination
- Historical location preference (regions user frequently visits)

*Time features*:
- Time until event
- Day of week, time of day the event starts (weeknight concert vs. weekend daytime)
- Overlap with user's schedule (if calendar integration available)

*Social features*:
- How many friends are attending? (strong signal)
- Is the user explicitly invited by others?
- Is the event host a friend?
- How often has user attended past events by this host?

*Event features*:
- Price (free vs. paid, price range)
- Embedding of event description (similarity to events user registered for previously)
- Category/tags

*User features*:
- Age, gender, city
- Past registration history (embedding of events attended)

**ML approach**: pointwise LTR reformulated as binary classification. For each (user, event) pair, predict P(registration). Rank events by predicted probability.

**Model comparison:**

| Model | Notes |
|-------|-------|
| Logistic Regression | Strong baseline; interpretable |
| Decision Tree | Non-linear; overfits easily |
| Bagging (Random Forest) | Reduces variance; good default |
| GBDT | Best offline accuracy for tabular features |
| Neural Network | Best if embeddings are key; requires more data |

**Chosen model**: GBDT or NN depending on data volume. Social features (friend attendance) are the highest-signal features for this domain.

**Serving**: online learning pipeline — new events are added continuously, user-event interaction data streams in, model is updated frequently. Prediction pipeline generates ranked lists at request time using cached event embeddings and real-time social feature lookups.

**Offline metrics**: AUC, precision@K. **Online metrics**: registration rate, ticket sales per session.

---

## Interview Pattern Summary

Across all five case studies, the same design loop applies:

1. **Clarify requirements** before touching ML: scale, latency, business objective, available data
2. **Translate business objective to ML objective**: clicks vs. engagement score vs. relevant items — the objective choice has major downstream consequences
3. **Feature engineering reflects the domain**: social graphs for PYMK, location/time for events, session sequences for similar listings
4. **Two-stage serving is standard**: candidate generation (fast, high recall) → ranking (slow, high precision) → optional reranking (diversity, fairness)
5. **Cold start is always a concern**: identify which cold start problem you have (item? user? both?) and state your mitigation explicitly

## Sources

- Aman.ai — [Chapter 6: Video Recommendation System](https://aman.ai/h/des/video-recommendation/)
- Aman.ai — [Chapter 10: Personalized News Feed](https://aman.ai/h/des/personalized-news-feed/)
- Aman.ai — [Chapter 11: People You May Know](https://aman.ai/h/des/people-you-may-know/)
- Aman.ai — [Chapter 9: Similar Listings on Vacation Rental Platforms](https://aman.ai/h/des/similar-listings/)
- Aman.ai — [Chapter 7: Event Recommendation System](https://aman.ai/h/des/event-recommendation/)
