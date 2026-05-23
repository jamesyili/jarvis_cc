# [Design] Video / Newsfeed Recommendation

*Source: `interview_prep/system_design_prep.pdf`, pages 71–75. James's prep notebook — extracted text, lightly cleaned.*

---

● Interaction-based Training: Transition from annotated dataset to continuous training using real-time user interactions (clicks, watch time, shares) for labels. Strategic: Aligns with Pinterest's Homefeed approach and your expertise.

 ● Query Understanding: Spelling correction, query category identification, entity recognition components.

 ● Multi-Modal System: Incorporate speech and audio content of videos for better relevance.

 ● Internationalization: Support for other languages. ● Near-Duplicate Detection: Remove highly similar videos from results. ● Query Taxonomy: Tailoring search approaches for head, torso, and tail queries. ● Real-world System Complexity: Acknowledge the simplified nature and mention areas of added complexity in production systems (e.g., personalization, complex re-ranking).

[Design] Video / Newsfeed Recommendation
Alright, James, let's break down this Video Recommendation System design, specifically a homepage system similar to YouTube's. This aligns very well with your current role at Pinterest in Homefeed recommendations and your ambition to be a Director of Engineering, as it touches on personalization, scale, and complex ML pipelines.

 1. Clarify Requirements: ● Primary Goal: Increase user engagement by recommending personalized videos on the user's homepage.

● Input/Output: User profile/context → Ranked list of engaging videos. ● Media Type: Only videos. ● Relevance: Maximize the number of relevant videos (ML Objective choice). Relevance defined by implicit/explicit user reactions (e.g., explicit like, watch ≥ 50% of video).

 ● Training Data: Construct dataset based on user interactions with video content. ● Language: Users and videos worldwide, multi-language support assumed. ● Scale: ≈ 10 billion videos on the platform. ● Latency: Recommendations ≤ 200 milliseconds. ● Simplifications: No playlists feature.

2. Frame as ML Task: ● Business Objective: Increase user engagement. ● ML Objective (Chosen): Maximize the number of relevant videos . ○ Rationale: Provides explicit control over signals, avoids "clickbait" issues (max clicks) and "short video bias" (max completed videos).

 ● System Input: User ID and contextual information. ● System Output: Ranked list of videos. ● ML Category: Personalized Recommendation System , specifically Hybrid Filtering (combining Collaborative Filtering and Content-Based Filtering).

 ○ Rationale: Hybrid approach leverages strengths of both: CF for discovering new interests and general trends (no domain knowledge needed), Content-based for new videos (cold-start) and capturing unique niche interests (requires video features/domain). They are complementary.

 ○ Implementation Strategy: Sequential Hybrid Filtering (e.g., CF-based for Candidate Generation , Content-based for Scoring/Ranking ).

3. Data Preparation: ● Data Choice: ○ Videos: Raw video files, Video ID, Duration, Language, Titles, Tags (manual/auto-generated).

 ○ Users: User ID, Demographics (Age, Gender, City, Country, Language, Time zone).

 ○ User-Video Interactions: Likes, Clicks, Impressions, Watch Time, Past Searches, Comments. Includes contextual info (Location, Timestamp).

 ● Feature Engineering: ○ Video Features: ■ Video ID: Embedding layer (learned during training). ■ Duration: Numerical feature (users prefer certain lengths). ■ Language: Embedding layer (categorical). ■ Titles & Tags: Map into feature vectors. ■ Tags: Lightweight pre-trained model (e.g., CBOW) for feature vectors.

 ■ Titles: Context-aware word embedding model (e.g., pre-trained BERT) for feature vectors.

 ○ User Features:

■ User Demographics: Age, Gender (embeddings if categorical), City, Country, Language, Time Zone.

 ■ Contextual Information: ■ Time of Day: User preference variation. ■ Device: e.g., shorter videos on mobile. ■ Day of Week: Behavioral shifts. ■ User Historical Interactions: (Key for personalization!) ■ Search History: Pre-trained BERT for query embeddings, then average embeddings for fixed-size vector.

 ■ Liked Videos: Video IDs → embedding layer, then average embeddings.

 ■ Watched Videos / Impressions: Similar to liked videos. ○ Constructing Dataset for Training: ■ Data Point: Features from a ⟨ user, video ⟩ pair. ■ Labeling: "Positive" if user explicitly liked or watched ≥ 50% (combines explicit/implicit feedback for relevance). "Negative" from random videos not interacted with, or explicitly disliked.

 ■ Imbalanced Data: Acknowledge this issue (many more negatives than positives) and note the need for techniques to address it (e.g., negative sampling, re-weighting, data augmentation for positives).

4. Modeling: ● Embedding-Based Models: Goal is to learn user and video embeddings such that their distance (e.g., dot product) represents relevance.

 ○ A. Matrix Factorization (MF): (Typically for Candidate Generation / CF-based) ■ Concept: Decomposes a sparse user-video feedback matrix into lower-dimensional user and video embedding matrices.

 ■ Feedback Matrix Construction: Combination of explicit and implicit feedback for relevance (e.g., like=1, watch 50%+=1, no interaction=0, dislike=0).

 ■ Loss Function: Weighted combination of squared distance over observed and unobserved ⟨ user, video ⟩ pairs.

 ■ Purpose: Addresses MF's weakness of not penalizing unobserved pairs (leading to all-ones embeddings) and avoiding unobserved pairs dominating observed ones (leading to all-zeros predictions).

 ■ Formula: First summation for observed, second for unobserved, with a weight W for balance.

 ■ Optimization: Weighted Alternating Least Squares (WALS) preferred for faster convergence and parallelizability over SGD.

 ■ Pros: Efficient training and serving (embeddings are static after learning). ■ Cons: Relies only on user-video interactions (no other features like age, language), struggles with new users (cold-start) as no interactions mean no meaningful embedding.

 ○ B. Two-Tower Neural Network: (Preferred for Ranking/Scoring / Hybrid)

■ Architecture: Two encoder towers: User Tower (User features → User Embedding) and Video Tower (Video features → Video Embedding). Shared embedding space.

 ■ Loss Function: Cross-Entropy (for binary classification of user-video relevance). (See formula in prior responses).

 ■ Pros: ■ Utilizes Rich Features: Can incorporate all user features (demographics, context, history) and video features (duration, title, tags). This enhances predictive capability and personalization.

 ■ Handles New Users (Cold Start): Can make recommendations based on demographic/contextual features even without interaction history.

 ■ Cons: ■ Slower Serving: User embedding must be computed at query time. If using video features in video tower, video embeddings also need re-computation if not pre-indexed.

 ■ More Expensive Training: More parameters than MF.

5. Evaluation: ● Offline Metrics: ○ Precision@k: Proportion of relevant videos in top k. (Use multiple k values). ○ mAP (Mean Average Precision): Measures ranking quality for binary relevance. ○ Diversity: Calculate average pairwise similarity (e.g., cosine similarity) of videos in the recommended list. Lower score = higher diversity.

 ■ Note: Use in conjunction with relevance metrics; diverse but irrelevant is bad.

 ● Online Metrics: (Focus on increasing user engagement - the business objective) ○ Click-Through Rate (CTR): Clicks / Impressions. Good for initial engagement, but can be susceptible to clickbait.

 ○ Number of Completed Videos: How many recommended videos users watch to the end.

 ○ Total Watch Time: Total time users spend watching recommended videos. Strong indicator of relevance and engagement. (Crucial for YouTube-like systems).

 ○ Explicit User Feedback: Likes/Dislikes. Most accurate reflection of user opinion.

6. Deployment & Serving (Multi-Stage Design): ● Prediction Pipeline: ○ Goal: Efficiently narrow down billions to thousands (Candidate Gen), then accurately rank thousands (Scoring). Maximize efficiency in stage 1, accuracy in stage 2.

 ○ Components: ■ Candidate Generation (Stage 1): ■ Goal: Narrow 10B videos → thousands. Prioritize efficiency over accuracy.

■ Model: Two-Tower Neural Network (CF-style: user features → user embedding; video ID → video embedding). Choose this as it handles new users and is relatively lightweight for this stage.

 ■ Process: User ID → User Encoder → User Embedding. User Embedding → ANN Nearest Neighbor Service (against billions of pre-computed video embeddings) → Top-K candidate videos.

 ■ Diversification: Can use multiple candidate generators (e.g., based on popularity, trending, user's location) to ensure diversity of recommendations.

 ■ Scoring (Ranking) (Stage 2): ■ Goal: Rank the thousands of candidates accurately. Prioritize accuracy over efficiency.

 ■ Model: Two-Tower Neural Network (Content-based style: uses all available rich user and video features to compute relevance scores). Can be heavier model due to smaller candidate set.

 ■ Process: Takes user and candidate video features, computes fine-grained relevance scores for each candidate video.

 ■ Re-ranking: ■ Applies business rules/constraints: region restrictions, freshness boosts, misinformation filtering, duplicate removal, fairness/bias adjustments, explicit clickbait filtering models.

 ● Indexing Pipelines: ○ Video Indexing Pipeline: ■ Raw Video → Video Encoder (from the two-tower model) → Video Embedding.

 ■ Video Embedding → Indexing Service (stores embedding, uses vector quantization for memory efficiency for NN search) → ANN Nearest Neighbor Service.

 ○ User Indexing Pipeline: ■ User Features → User Encoder (from the two-tower model) → User Embedding.

 ■ User Embedding → Indexing Service (for quick retrieval during Candidate Generation).

7. Monitoring: ● System Health: Latency (critical for <200ms), throughput, error rates for all services. ● Model Performance (Offline): Continuous monitoring of Precision@k, mAP, Diversity on validation sets.

 ● Online Performance: Real-time tracking of CTR, Video Completion Rate, Total Watch Time, Explicit Feedback. Set up alerts for unexpected drops or changes.

 ● Data Quality: Monitor incoming user interaction data (clicks, likes, watch time) for integrity and distribution shifts.

 ● Cold Start Handling: Monitor engagement metrics for new users/videos to validate cold-start strategies.

 ● Bias Monitoring: Track metrics across different user demographics or content types to ensure fairness.
