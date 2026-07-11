# [Design] Similar Content / Visual Search

*Source: `interview_prep/system_design_prep.pdf`, pages 76–79. James's prep notebook — extracted text, lightly cleaned.*

---

Other Potential Discussion Points (for senior roles / if time permits): ● Exploration-Exploitation Trade-off: How to balance recommending known relevant videos (exploitation) with recommending novel or new videos to discover new interests (exploration).

 ● Bias Mitigation: Detailed strategies for addressing popularity bias, positional bias, feedback loop biases.

 ● Multi-Objective Optimization: Optimizing for watch time, diversity, freshness, and relevance simultaneously.

 ● Negative Feedback: Explicitly using dislikes or skips to refine recommendations. ● Sequence Modeling: Incorporating the sequence of watched/searched videos using RNNs or Transformers in user embeddings for richer context. Strategic: Aligns with your AI/ML interests.

 ● Seasonality: Adapting recommendations to changes in user behavior over seasons/holidays.

[Design] Similar Content / Visual Search Recommendation
 1. Clarify Requirements: ● Primary Goal: Retrieve images visually similar to a user-provided query image, ranked by similarity.

 ● Input/Output: Query image (can be a crop) → Ranked list of visually similar images. ● Media Type: Only images. No video, no text queries (for simplicity). ● Personalization: None. Same query image yields same results for all users.

● Metadata Usage: No reliance on image metadata (tags, etc.), only image pixels (for simplicity, but note this is a simplification from real-world).

 ● User Actions: Only image clicks (as proxy for similarity). No save/share/like (for simplicity).

 ● Content Moderation: Out of scope for this design, but acknowledged as critical for a safe platform.

 ● Training Data: Online construction using user interactions (clicks as proxy) is the expected approach.

 ● Scale: 100-200 billion images on the platform. Search must be fast .

2. Frame as ML Task: ● ML Objective: Accurately retrieve images visually similar to the query image. ● System Input: Query image (pixels). ● System Output: Ranked list of similar images. ● ML Category: Ranking Problem solved via Representation Learning . ○ Representation Learning: Train a model to transform input images into N-dimensional embedding vectors (points in an embedding space). The goal is for similar images to have embeddings in close proximity .

 ○ Ranking Process: 1. Compute query image embedding. 2. Calculate similarity scores (distances) between query embedding and all other image embeddings in the platform.

 3. Rank images by these similarity scores (most similar first).

3. Data Preparation: ● Data Choice: ○ Images: Raw image pixel data (including cropped query images). ○ User-Image Interactions: Impressions and Clicks (User ID, Query Image ID, Displayed Image ID, Position, Interaction type, Timestamp). Clicks are key for positive signal.

 ● Feature Engineering (Image Preprocessing): ○ Resizing: Standardize to fixed dimensions (e.g., 224x224 pixels) for model input. ○ Scaling: Normalize pixel values (e.g., 0-1 range). ○ Z-score Normalization: Mean 0, Variance 1 for better model convergence. ○ Consistent Color Mode: Ensure uniform color representation (e.g., RGB). ● Constructing Dataset for Contrastive Training: ○ Data Point: (Query Image, Positive Image, N-1 Negative Images). Ground truth is the index of the positive image among the N candidates.

 ○ Positive Image Selection Options (and Trade-offs): 1. Human Judgments: High accuracy, but very expensive, time-consuming, not scalable for 100-200B images.

 2. User Clicks (Proxy): Automatic, no manual work. Pros: Real-world implicit feedback. Cons: Noisy (users click for many reasons), sparse (most images lack clicks), leads to poor performance if used naively.

3. Self-Supervision (Data Augmentation): Artificially create similar images by augmenting the query image (e.g., rotation, cropping, color jitter). Frameworks like SimCLR/MoCo use this.

 ■ Pros: No manual work, fully automated, less noisy (augmented image is always similar), scalable to huge datasets.

 ■ Cons: Artificial similarity may not perfectly reflect real-world visual/semantic similarity.

 ○ Chosen Approach: Start with Self-Supervision (Data Augmentation) due to automation, no upfront cost, and scalability with billions of images (as shown by SimCLR results). Acknowledge that we can iterate and incorporate noisy click data later or use human labeling for refinement if initial results are unsatisfactory. Strategic point: This demonstrates adaptability and an iterative approach.

4. Modeling: ● Model Selection: ○ Neural Networks (NNs): Ideal for unstructured data like images and capable of producing learned embeddings for representation learning.

 ○ Architectures: CNN-based (e.g., ResNet) or Transformer-based (e.g., ViT) are strong candidates for image processing.

 ○ Simplified Model Architecture: (Figure 2.5) Input Image → (Convolutional Layers → Fully Connected Layers) → Embedding Vector. Hyperparameters (layers, neurons, embedding size) are tuned experimentally.

 ● Model Training (Contrastive Training): ○ Goal: Optimize model parameters so that similar images have embeddings close to each other, and dissimilar images are far apart.

 ○ Process: Provide (Query Image, Positive Image, N-1 Negative Images). Model learns to make positive closer to query than negatives.

 ○ Loss Function (Simplified Contrastive Loss): 1. Compute Similarities: Measure similarity between query embedding
(Eq ) and candidate embeddings
(Ex ) using:

 ■ Dot Product: Eq ⋅ Ex ■ Cosine Similarity: ∣∣ Eq ∣∣⋅∣∣ Ex ∣∣ Eq ⋅ Ex (often preferred as it's scale-invariant for embedding vectors)
 ■ (Note: Euclidean distance generally performs poorly in high dimensions due to curse of dimensionality).

 2. Softmax: Apply softmax over the computed similarities to convert them into probabilities:

Pi =∑j=1N exp(similarity(Eq ,Ej ))exp(similarity(Eq ,Ei ))
 3. Cross-Entropy: Compute Cross-Entropy loss between these predicted probabilities and the one-hot ground truth label (index of the positive image).

LContrastive =−∑i=1N yi log(Pi ) (where
yi =1 for positive image, 0 for negatives).

 ■ Purpose: Minimizing this loss ensures the model assigns high probability to the positive image and low probabilities to negative images, indicating good separation in embedding space.

 ● Pre-training / Fine-tuning: Leverage pre-trained contrastive models (e.g., from ImageNet or large web datasets) and then fine-tune on Pinterest's specific interaction

data. This significantly reduces training time and leverages learned general representations. Strategic point: This aligns with operational excellence and efficient resource utilization.

5. Evaluation: ● Offline Metrics: ○ Evaluation Dataset: Query image, candidate images, and continuous ground truth similarity scores (0-5).

 ○ Choice: nDCG (Normalized Discounted Cumulative Gain) . ■ Why: Unlike MRR, Recall@k, or Precision@k, nDCG explicitly accounts for the graded relevance (0-5 scores) and the position of relevant items in the ranked list, giving higher scores to highly relevant items placed at the top. This perfectly aligns with the requirement to rank "most similar to least similar."
 ■ Formulas: ■ DCGp =∑i=1p log2 (i+1)reli ■ nDCGp =IDCGp DCGp (where IDCG is DCG of ideal ranking) ○ (Avoid MRR, Recall@k, Precision@k shortcomings as discussed in context). ● Online Metrics: ○ Click-Through Rate (CTR): CTR=Total number of suggested imagesNumber of clicked
images . A high CTR indicates users find suggestions relevant and click frequently.

 ○ Average Daily/Weekly/Monthly Time Spent on Suggested Images: Measures user engagement with search results. Expected to increase with system accuracy.

 ○ (Self-reflection: For Pinterest, this aligns with key metrics for user engagement and growth).

6. Deployment & Serving: ● Prediction Pipeline: (Figure 2.19 - right side) 1. Embedding Generation Service: ■ Preprocesses query image (resizing, scaling, normalization, color mode). ■ Passes preprocessed image through the trained embedding model. ■ Outputs the query image embedding. 2. Nearest Neighbor Service: ■ Takes the query embedding. ■ Performs a Nearest Neighbor (NN) search against the indexed embeddings of all images on the platform.

 ■ Choice: Approximate Nearest Neighbor (ANN) algorithms (e.g., from Faiss, ScaNN) are mandatory due to 100-200 billion images (Exact NN / Linear Search is O(N×D) and too slow).

 ■ ANN Categories (High-level understanding): Tree-based (Kd-trees, Annoy), Locality-Sensitive Hashing (LSH), Clustering-based. These reduce search complexity to sub-linear (e.g., O(DlogN)).

 3. Re-ranking Service: ■ Applies business logic and policies: filters inappropriate results, removes private/duplicate images, applies other product rules.
