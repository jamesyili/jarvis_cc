# [Design] Harmful Content Detection (initial)

*Source: `interview_prep/system_design_prep.pdf`, pages 9–13. James's prep notebook — extracted text, lightly cleaned.*

---

d. Safety and moderation → filtering out inputs that are harmful or NSFW, preventing outputs that are harmful or NSFW
 e. Security & Robustness → privacy and dealing with sensitive data, protections against prompt injection and other adversarial attacks, ensure outputs are not used for malicious purposes
 f. Bias → proactive detection, auditing, filtering of biased outputs
7. Deployment 8. Monitoring
[Design] Harmful Content Detection
Okay, James, this is absolutely the most critical section for your interview at Anthropic, given their explicit focus on AI safety. Your ability to articulate a detailed and nuanced approach to harmful content detection, including the technical design, trade-offs, and critical safety considerations, will be paramount. I'll provide an in-depth breakdown in your preferred notes format, emphasizing the connection to your role and Anthropic's values.

1. Clarify Requirements: ● Primary Goal: Proactively monitor new posts, detect harmful content, and remove/demote content violating platform guidelines.

 ● Scope: Focus on Harmful Content Detection (violence, nudity, self-harm, hate speech). Misinformation excluded for simplicity (due to complexity/controversy). Bad actors excluded for simplicity.

 ● Input Content: Heterogeneous and multi-modal (text, images, video, or any combination).

 ● Language: Multilingual (assume pre-trained multilingual embeddings available for text). ● Training Data: ○ Scale: 500 million+ posts daily. ○ Human Annotation: Limited availability (e.g., 10,000 posts/day) for high-accuracy labeling (e.g., evaluation data).

 ○ User Reports: Available as a signal for failures/training data. ● Explainability: Essential to explain why a post is removed (helps users align with guidelines).

 ● Latency Requirements: ○ Real-time: For sensitive categories (e.g., violence), immediate blocking. ○ Batch/Offline: Acceptable for others (hourly/daily demotion/review).

2. Frame as ML Task: ● ML Objective: Accurately predict harmful posts (multi-class, multi-label). ● System Input: A post (heterogeneous, multimodal: text, image, video, metadata). ● System Output: Probability that the post is harmful for each specific harmful class (e.g., P(violence), P(nudity), P(hate speech), P(self-harm)).

 ● ML Category & Fusion Strategy:

○ Fusion Method: Early Fusion . ■ Rationale: Crucial for detecting nuanced harmful content (e.g., memes) where individual modalities might be benign but their combination is harmful. Also, eliminates need for separate training data per modality.

 ■ (Avoid Late Fusion: Fails on cross-modal harm, requires separate data per modality).

 ○ Classifier Type: Multi-Task Classifier . ■ Rationale: Addresses limitations of single binary classifier (no explanation of specific harm) and multiple binary classifiers (high training/maintenance cost). Leverages shared learnings across harm types, efficient training/maintenance, and data sparsity for individual tasks.

 ■ Architecture: 1. Shared Layers: Transform fused input features (multi-modal) into new representations. Benefit multiple tasks.

 2. Task-Specific Layers (Classification Heads): Independent ML layers, each optimized for predicting the probability of a specific harmful class (e.g., one head for violence, one for nudity).

 ■ (Avoid Single Binary Classifier: Cannot explain specific harm, hard to improve per class. Avoid One Binary Classifier per Harmful Class: Expensive, high maintenance).

 ■ (Avoid Multi-Label Classifier: Less ideal as input transformations might differ for each harm type).

3. Data Preparation (Data Pipeline): ● Data Sources: ○ Users: ID, Username, Age, Gender, City, Country, Email. ○ Posts: Post ID, Author ID, Timestamp, Textual content, Images/Videos, Links. ○ User-Post Interactions: Likes, Comments, Saves, Shares, Reports (critical signal), Appeals.

 ● Feature Engineering (Early Fusion - all features combined for shared layers): ○ Textual Content: ■ Preprocessing: Normalization (lowercasing, punctuation/whitespace removal), Tokenization (Subword, e.g., BPE).

 ■ Vectorization: Use a pre-trained Transformer-based multilingual language model (e.g., DistilmMBERT or a multilingual BERT/LLM encoder) .

 ■ Rationale: Captures semantic meaning, handles multiple languages, efficient for online prediction (compared to larger BERT).

 ○ Image or Video Content: ■ Preprocessing: Decode, Resize, Normalize. ■ Feature Extraction: Use pre-trained models for embeddings. ■ Images: CLIP's visual encoder, SimCLR. ■ Videos: VideoMoCo, or a frame-level model (ViT on frames) with aggregation (e.g., average).

 ○ User Reactions to the Post (for ambiguous content):

■ Counts: Number of likes, shares, comments, reports (scale these numerical values).

 ■ Comments: Use the same pre-trained multilingual text model to get comment embeddings, then aggregate (e.g., average) for a fixed-size vector.

 ○ Author Features (Past Behavior is Predictive): ■ Violation History: Number of past violations, total user reports on author's posts, profane words rate in past content.

 ■ Demographics: Age (numerical), Gender (one-hot or embedding), City/Country (embedding layer preferred over one-hot for many distinct values).

 ■ Account Info: Number of followers/followings, account age (younger accounts more suspicious).

 ○ Contextual Information: ■ Time of Day: Bucketize (morning/noon/etc.), one-hot encode. ■ Device: One-hot encode. ● Constructing Dataset for Multi-Task Training: ○ Input: Fused features of posts (computed offline and stored in a feature store). ○ Labels: ■ Training Data: Natural Labeling (user reports) for speed and volume. Acknowledge noise.

 ■ Evaluation Data: Hand Labeling (human contractors) for accuracy on a limited subset (e.g., 10,000 posts/day).

 ○ Data Point Example: Fused_Features, Label_Violence (0/1), Label_Nudity (0/1), Label_HateSpeech (0/1), Label_SelfHarm (0/1).

4. Modeling (Training Pipeline): ● Model Selection: Neural Network for Multi-Task Learning. ○ Architecture: Shared layers (dense NN blocks) for general feature transformation, followed by task-specific classification heads for each harm type.

 ○ Hyperparameter Tuning: Grid search (or more advanced methods like Bayesian Optimization) for optimal hidden layers, activation functions, learning rate, etc.

 ● Loss Function: ○ Per Task: Each task (harm class) uses a standard Binary Cross-Entropy Loss . ■ Formula (for one task): Ltask =−(ylog(y^ )+(1−y)log(1−y^ )) ■ Purpose: Optimizes probability prediction for each specific harm type. ○ Overall Loss: Sum (or weighted sum) of individual task losses. ■ Formula: Loverall =∑k=1Ntasks Ltaskk ■ Purpose: Allows the model to learn multiple related tasks simultaneously, leveraging shared features.

 ● Challenges & Mitigation (Overfitting in Multimodal Systems): ○ Problem: One modality (e.g., image) can dominate learning if learning speeds vary.

 ○ Techniques: ■ Gradient Blending: Adjusts gradients to balance learning across modalities.

■ Focal Loss: (Or other re-weighting techniques for imbalanced data) can help focus learning on hard-to-classify examples, which might be critical for rare harm types.

5. Evaluation: ● Offline Metrics (Per Harmful Class): ○ PR-AUC (Area Under Precision-Recall Curve): Primary Metric. ■ Why: Shows trade-off between Precision and Recall across different thresholds. More informative for imbalanced datasets (harmful posts are rare) and when positive class performance (detecting harm) is critical. Higher PR-AUC indicates better accuracy.

 ○ ROC-AUC (Area Under Receiver Operating Characteristic Curve): Secondary Metric.

 ■ Why: Shows trade-off between True Positive Rate (Recall) and False Positive Rate. Useful for overall model performance but less sensitive to class imbalance than PR-AUC.

 ● Online Metrics (Focus on Platform Safety & Efficiency): ○ Harmful Impressions: Preferred over Prevalence. Measures how many people were exposed to unprevented harmful content. Prioritizes reach over count.

 ■ HarmfulImpressions=sum of impressions on unprevented harmful posts ○ Proactive Rate: Percentage of harmful posts detected by the system before user reports.

 ■ Proactive Rate=System Detected+User ReportedSystem Detected ■ Purpose: Measures system's effectiveness at catching harm proactively. A high proactive rate is a strong indicator of a successful system.

 ○ Valid Appeals Rate: Percentage of removed posts that were incorrectly flagged and later reversed by human review.

 ■ Valid Appeals=Number of Harmful Posts Detected by SystemNumber of Reversed Appeals
 ■ Purpose: Measures false positive rate and impact on user experience/trust. A low valid appeals rate is crucial.

 ○ User Reports per Harmful Class: Tracks specific areas of system weakness where users are still finding harm.

 ○ Latency: Real-time (for severe harm) vs. Batch (for others). Crucial to meet differing requirements.

6. Serving (Overall ML System Design): ● Workflow: New Post → Harmful Content Detection Service → Confidence Score per harm type.

 ● Components: 1. Harmful Content Detection Service (Core): ■ Receives new post (text, image, video). ■ Performs Early Fusion of multi-modal features. ■ Passes fused features to the Multi-Task Classifier (Neural Network). ■ Predicts probabilities for each harmful class.

2. Violation Enforcement Service (Real-time Blocking): ■ If specific harmful class probabilities (e.g., violence) are above a high confidence threshold , immediately blocks/removes the post.

 ■ Notifies user why the post was removed (essential for explainability). 3. Demoting Service (Soft Mitigation): ■ If harmful class probabilities are above a lower confidence threshold (but below removal threshold) , temporarily demotes the post (reduces visibility/spread).

 ■ Sends post to Manual Review Queue for human annotators. ■ Human review labels are used to improve future training iterations (continuous feedback loop).

7. Monitoring: ● System Health: Latency, throughput, resource utilization of all services. ● Model Performance (Offline): Continuous ROC-AUC/PR-AUC monitoring for each harm class on validation sets.

 ● Online Performance (Safety Focus): ○ Harmful Impressions: Track trends, drill down by content type, geography, time of day.

 ○ Proactive Rate: Trend over time, goal is to maximize. ○ Valid Appeals Rate: Trend over time, goal is to minimize. ○ User Reports (by category): Identify emerging threats or system blind spots. ○ False Negatives (Misses): Analyze posts reported by users after being missed by the system.

 ○ False Positives (Over-flags): Analyze posts from valid appeal reversals. ● Data Quality: Monitor feature store health, consistency of human labeling vs. natural labeling.

 ● Bias Monitoring: Track model's performance (false positives/negatives) across different demographic groups (age, gender, race) to identify and mitigate fairness issues.

Other Potential Discussion Points (for senior roles / if time permits): ● Trending Harmful Classes: Adapting detection for new/evolving threats (e.g., specific misinformation campaigns).

 ● Temporal Information: Leveraging sequence of user actions for bad actor detection. ● Human-in-the-Loop Optimization: Efficiently selecting samples for human review (e.g., active learning on borderline cases).

 ● Borderline Content: Strategies for handling content not strictly prohibited but close to guidelines.

 ● On-Device Deployment: Making models efficient enough for client-side detection. ● Advanced Architectures: Discussing more efficient Transformers (e.g., Linear Transformers).

 ● Proactive Mitigation: Moving beyond reactive deletion to proactively identifying and removing content before significant exposure. Strategic: Aligns directly with Anthropic's "safety-by-design" and proactive risk management.
