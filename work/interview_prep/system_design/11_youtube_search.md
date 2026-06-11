# [Design] YouTube Search (Text → Video)

*Source: `interview_prep/system_design_prep.pdf`, pages 66–70. James's prep notebook — extracted text, lightly cleaned.*

---

[Design] Youtube Search (Text → Video)
 1. Clarify Requirements: ● Primary Goal: Given a text query, retrieve a ranked list of relevant videos. ● Input/Output: Text query → Ranked list of relevant videos. ● Media Type: Platform serves only videos. ● Relevance: Determined by video's visual content and associated textual data (title, description). No other metadata for simplicity.

 ● Training Data: 10 million pairs of ⟨ video, text query ⟩ available. ● Language: English only (for simplicity). ● Scale: 1 billion videos on the platform. ● Personalization: None required (opposed to recommendation systems).

2. Frame as ML Task: ● ML Objective: Rank videos based on their relevance to the text query.

● System Input: Text query. ● System Output: Ranked list of videos. ● ML Category: Ranking Problem solved via Representation Learning (for visual search) and Inverted Index (for text search).

 ○ Representation Learning (Visual Search Component): ■ Train a Text Encoder (Text query → Text Embedding) and a Video Encoder (Video → Video Embedding).

 ■ Goal: Learn embeddings such that the dot product (similarity score) between a text embedding and a video embedding reflects their relevance.

 ■ Rank videos by similarity scores to the text query embedding. ○ Inverted Index (Text Search Component): ■ Non-ML approach (no training cost). ■ Uses an inverted index (e.g., Elasticsearch) to perform efficient full-text search on video titles, descriptions, and tags.

 ■ Finds videos with keyword overlap with the text query.

 3. Data Preparation: ● Data Choice: Annotated dataset of 10M ⟨ video, text query ⟩ pairs. ○ Example: Video Name, Query, Split Type (Train/Val/Test). ● Feature Engineering (Preparing Text Data): ○ Text Normalization (Cleanup): ■ Lowercasing. ■ Punctuation removal. ■ Whitespace trimming. ■ Normalization Form KD (NFKD) / Strip accents. ■ Lemmatization/Stemming (e.g., "walking" → "walk"). ○ Tokenization: Convert text into tokens. ■ Subword Tokenization (e.g., BPE, SentencePiece): Preferred. ■ Pros: Handles OOV (out-of-vocabulary) words by decomposing them into seen subwords; smaller vocabulary size than word-level; balances expressiveness with manageable vocabulary.

 ■ Cons: More complex to implement than word/char level. ■ (Avoid Character-level: too granular; Word-level: too large vocab, frequent OOV).

○ Tokens to IDs: Convert tokens to numerical IDs. ■ Lookup Table: Map each unique token to an ID (1:1 mapping). ■ Pros: Quick conversion, easy ID to token lookup. ■ Cons: Memory-intensive for large vocab, cannot handle unseen tokens, no collisions.

 ■ Hashing (Feature Hashing): Use a hash function to get IDs, no lookup table needed.

 ■ Pros: Memory efficient, handles unseen tokens. ■ Cons: Slower conversion (hash computation), no ID to token lookup, potential for collisions.

 ■ Chosen Approach: Lookup table is standard for Transformer-based models; hashing is for very large vocabularies or memory constraints. For 10M pairs, lookup table is fine.

 ● Feature Engineering (Preparing Video Data): ○ Workflow: Raw Video → Sample Frames → Image Preprocessing (Resizing, Scaling, Normalization) → Frame Embeddings.

4. Modeling: ● Text Encoder Model: ○ Purpose: Convert text query into a meaningful embedding vector. ○ Choice: Transformer-based models (e.g., BERT) . ■ Why: Captures semantic and contextual meaning (word order, different embeddings for same word in different contexts). Powerful for NLP tasks.

 ○ Avoid: Statistical methods (BoW, TF-IDF) due to limitations in capturing word order/semantic meaning, and sparse representations. Word2vec/Embedding layers (simple, but less contextual than Transformers).

 ○ Key Components (Deep dive if asked): ■ Token Embedding: Converts token IDs to dense vectors. ■ Position Embedding: Adds positional information (fixed or learned) to token embeddings for sequence order.

 ■ Multi-Head Attention/Self-Attention: Allows tokens to weigh importance of other tokens in the sequence. Output of multiple heads are concatenated and linearly transformed.

 ■ Prediction Head: (Not relevant for encoder's primary output, but generally part of pretext task training).

 ● Video Encoder Model: ○ Purpose: Convert video into a meaningful embedding vector. ○ Architectural Options: ■ Video-level Models: Process whole video (e.g., 3D CNNs, Video Transformers).

 ■ Pros: Captures full temporal context (actions, motions). ■ Cons: Computationally expensive, slower. ■ Frame-level Models: (Chosen Approach) ■ Process: Sample frames from video → run image model on frames → aggregate frame embeddings (e.g., average) into video embedding.

 ■ Model: ViT (Vision Transformer) or ResNet applied per frame.

■ Pros: Faster training/serving speed, computationally less expensive.

 ■ Cons: May not fully understand temporal aspects (actions/motions).

 ○ Chosen Approach: Frame-level model (e.g., ViT) due to speed and computational efficiency, as temporal understanding is not crucial for basic video search here.

 ● Model Training (Contrastive Learning): ○ Objective: Optimize parameters of both Text and Video Encoders simultaneously.

 ○ Goal: Ensure relevant video-text pairs have high similarity (dot product) in the embedding space, and irrelevant pairs have low similarity.

 ○ Loss Function: Similar to the Visual Search system: Contrastive Loss. ■ Compute dot product similarity between text embedding (ET ) and each video embedding
(EV ).

 ■ Apply Softmax over these similarities to get probabilities. ■ Compute Cross-Entropy Loss against the ground truth (the one relevant video among the candidates).

 ■ Formula: $L = - \log(P_{\text{relevant_video}})$ (where $P_{\text{relevant_video}}$ is the softmax probability assigned to the true relevant video).

5. Evaluation: ● Offline Metrics: ○ Evaluation Dataset: Given ⟨ text query, associated relevant video ⟩ pairs. ○ Choice: Mean Reciprocal Rank (MRR) . ■ Why: Addresses shortcomings of Precision@k and Recall@k for this specific dataset setup (where only one relevant video per query is given). MRR measures how high the first relevant item is ranked.

 ■ Formula: MRR=m1 ∑i=1m ranki 1 (where m is total queries, ranki is rank of first relevant item for query i).

 ■ (Avoid Precision@k/mAP: Numerator is max 1, leads to low values. Avoid Recall@k: Always 0 or 1, doesn't distinguish between rank 15 vs 50).

 ● Online Metrics: ○ Click-Through Rate (CTR): CTR=Total number of suggested videosNumber of clicked
videos . Good general engagement metric.

 ○ Video Completion Rate: Percentage of videos watched till the end from search results.

 ○ Total Watch Time of Search Results: Sum of time users spend watching videos retrieved from search. Strong indicator of relevance/engagement.

6. Deployment & Serving: ● Prediction Pipeline: 1. Text Query Input: User enters query. 2. Visual Search Component:

■ Text Query → Text Encoder → Text Embedding. ■ Text Embedding → ANN Nearest Neighbor Service → Top-K Video Embeddings.

 ■ (Leverage) ANN algorithms (e.g., Faiss, ScaNN) for billions of videos, as in Visual Search System.

 3. Text Search Component: ■ Text Query → Elasticsearch (using Inverted Index) → Top-K Videos based on title/tag overlap.

 4. Fusing Layer: ■ Combines ranked lists from Visual Search and Text Search. ■ Implementation: Weighted sum of predicted relevance scores (simpler, faster at serving than training a new model).

 5. Re-ranking Service: ■ Applies business logic: filters inappropriate content, removes duplicates, enforces policies.

 ● Indexing Pipelines: (Two parallel pipelines) 1. Video Indexing Pipeline: ■ Raw Video → Video Encoder → Video Embedding. ■ Video Embedding → Indexing Service (stores embedding, uses vector quantization for memory efficiency) → Nearest Neighbor Service.

 2. Text Indexing Pipeline: ■ Video Titles, Manual Tags, Auto-Generated Tags → Text Preprocessing (normalization, tokenization, IDs) → Elasticsearch (Inverted Index).

 ■ Auto-Tagger Component: Standalone ML model (e.g., a text classifier or generative model) to generate tags for videos without manual tags. Valuable for discoverability, even if noisier.

7. Monitoring: ● System Health: Latency, throughput, error rates for all services (encoders, NN, Elasticsearch, fusing, re-ranking).

 ● Model Performance (Offline): Continuous MRR monitoring on evaluation datasets to track embedding quality and retrieval accuracy.

 ● Online Performance: Monitor CTR, Video Completion Rate, and Total Watch Time of search results. Alert on significant deviations.

 ● Data Quality: Monitor text query distribution, video ingestion rates, and tag quality (manual vs. auto-generated).

 ● ANN Accuracy: Periodically evaluate ANN recall/precision against exact NN on a small sample to ensure search quality is maintained.

Other Potential Discussion Points (for senior roles): ● Multi-Stage Design: Candidate Generation (faster, broad retrieval) + Re-ranking (slower, more complex ranking logic).

 ● Additional Video Features: Incorporate video length, popularity, freshness, creator reputation, etc., into the ranking.
