# [Design] Brief: Defense-in-Depth

*Source: `interview_prep/system_design_prep.pdf`, pages 25–31. James's prep notebook — extracted text, lightly cleaned.*

---

be flagged as an anomaly. These can help understand latent representations for interpretability purposes.

 Tiered System 1. Tier 1 Defense (Fast Rules & Filters): a. Keyword list, regex filters, potentially simple on-device classifier b. Very low latency c. Goal: Drop obviously harmful content fast 2. Tier 2 Defense (Lightweight Models): a. Features fetched from pre-computed embeddings in a NoSQL store b. Models trained using data prepared from the Data Lake c. Near-real-time scoring 3. Tier 3 Defense (Heavy ML Inference): a. Deep models for nuanced cases (e.g., multimodal harmful meme detection) b. Training on multi-terabyte datasets prepared from the Data Lake c. Possibly async or deferred scoring For Generating Synthetic Harmful Data (Red Teaming): "We'd likely use Top-P Sampling with a higher temperature on our internal LLMs. This is because we need to generate a diverse range of subtle, creative, and novel 'jailbreak' attempts or harmful scenarios that humans might not easily conceive. Maximizing diversity helps our safety classifiers learn to detect a broader spectrum of threats, rather than just the most obvious ones. We'd want the generative model to explore the 'edges' of harmful content generation."
 For Internal Debugging/Reproducibility: "If we're debugging a specific safety incident or trying to reproduce a harmful output, we might temporarily use Greedy Search or Beam Search to see the most probable (and thus often most common) failure modes of the model. This offers deterministic outputs for analysis."
 For Real-time User-Facing Interactions (where safety filters are applied): "The core LLM generating content for users would likely use a combination of Top-P sampling with an optimally tuned temperature . The goal here is to balance user experience (creativity, helpfulness) with adherence to alignment (harmlessness). Our real-time Constitutional Classifiers and token-level filtering would act as a crucial 'post-sampling' safety layer, analyzing the generated sequence regardless of the sampling method used, potentially even blocking or re-sampling problematic tokens on the fly, as per Anthropic's multi-layered defense strategy."
[Design] Brief: Defense-in-Depth

1. Clarify Requirements (My Strategic Approach) ● Business Objective: Ensure AI system safety and integrity , maximizing user trust and adherence to platform guidelines (like Anthropic's Responsible Scaling Policy).

 ○ KPIs: ■ Jailbreak Prevention Rate: Target >95% (critical for input safety). ■ False Positive Rate (Unnecessary Refusal): <0.5% (crucial for user experience).

 ■ Time-to-Mitigation for New Attacks: <24 hours (adaptive learning). ■ Harmful Content Blocking: 100% for high-confidence, severe cases (e.g., CBRN, child safety).

 ● Core Features: ○ Multi-modal: Text (prompts, responses), Image (if model is multi-modal), Audio (if model handles speech).

 ○ Real-time Filters (Different Latencies):

■ Pre-prompt (Input): Block malicious user input before LLM inference. ■ Mid-generation (Streaming/Token-level): Intervene during LLM output generation.

 ■ Post-response (Output): Final check on complete LLM response. ○ Adaptive Learning: Continuous updates for new attacks. ○ Hierarchical Escalation: Automated → Human Review → Expert. ○ Explainability: Provide reasons for blocking/demotion to users. ● Data Sources: ○ Synthetic Adversarial Data: Crucial for zero-shot detection of new threats (e.g., Constitutional AI generated for diverse harmful/benign pairs).

 ○ Red Team Outputs: From ongoing adversarial testing. ○ Production Logs: User interactions, blocked content, false positive reports. ○ Threat Intelligence: External feeds on new attack patterns. ● Scale & Performance: ○ Volume: 50M+ daily interactions, 100K+ QPS peak (massive scale). ○ Latency: ■ Input classification: <50ms (to prevent prompt injection before LLM compute).

 ■ Output classification: <100ms (for post-processing, potentially higher for full video analysis).

 ■ Token-level (mid-generation): <10ms per token (for blocking/steering). ■ Total overhead: <200ms (minimal impact on core LLM response time). ○ Availability: 99.99% uptime, graceful degradation.

2. Frame as ML Task (My "Catalytic Clarity" Framing) ● Primary Task: Multi-Task, Multi-Modal Discriminative Classification. ○ Input: User prompt (text, image, audio), partial/full LLM response. ○ Output: Probabilities for specific harm categories (e.g., Violence, Nudity, Hate Speech, Self-Harm, Fraud), with confidence scores.

 ○ Goal: Pinpoint type of harm for explainability and specific mitigation. ● Secondary Tasks: ○ Generative Synthetic Data Creation: Using LLMs (e.g., Constitutional AI principles) to create training data for classifiers.

 ○ Anomaly Detection: Identify novel jailbreak patterns or emerging threats.

3. Data Preparation (Operational Excellence) ● Strategy: Continuous, Automated Data Pipelines supplemented by expert human feedback.

 ● Key Data Sources: ○ Constitutional Synthesis: Automatically generate vast, diverse harmful/benign examples (prompts/responses) based on defined safety principles using internal LLMs. This is the scalable solution for data.

○ Adversarial Augmentation: Apply known jailbreak techniques (e.g., base64 encoding, role-play, prompt injection variations) to benign data to create adversarial training examples.

 ○ Red Team Outputs: High-quality, real-world adversarial examples from dedicated security teams and bug bounty programs.

 ○ Production Feedback: User reports (positive and negative), model predictions, human review outcomes.

 ● Data Quality & Safety: ○ Deduplication: Remove near-duplicates across modalities/languages. ○ Bias Detection: Proactively audit datasets for demographic, linguistic biases. Crucial for fair system.

 ○ Privacy: PII scrubbing, anonymization (GDPR, etc.). ○ Version Control: Ensure reproducibility of datasets. ● Efficiency: ○ Columnar Storage (Parquet): For efficient storage and querying of features and large datasets.

 ○ Semantic Indexing (FAISS/Elasticsearch): For fast similarity search of embeddings (for prompt/response vectors) and full-text search of attack patterns.

 ○ Caching: Hot classification results (Redis), frequently accessed model artifacts, historical attack patterns.

4. Modeling (Strategic Realignment) ● Overall Architecture: Defense-in-Depth Ensemble. ○ Multiple specialized models, each with specific roles and latency profiles. ○ Final decision through a meta-classifier or rule-based engine. ● Key Model Types & Latency Constraints: ○ Input Classifier (Pre-Prompt): ■ Purpose: Detect immediate jailbreaks, policy violations in user's input before the LLM even processes it. Prevents costly LLM inference on malicious prompts.

 ■ Latency: <50ms. Must be extremely fast. ■ Type: ■ Lightweight Transformer (e.g., DistilmMBERT/custom small BERT-like model): Optimized for low latency, multilingual.

 ■ Rule-based System: For immediate blocking of known explicit keywords/patterns (high precision, low recall but very fast).

 ■ Simple ML (e.g., SVMs/XGBoost on extracted features): For high-precision, low-compute cases.

 ■ Output: Binary flag (block/allow) + confidence score. ○ Output Stream Classifier (Mid-Generation / Token-Level): ■ Purpose: Detect harmful content as it's being generated , allowing for immediate interruption or steering of the LLM. Prevents exposure to full harmful responses.

 ■ Latency: <10ms per token. Extremely critical for real-time interaction. ■ Type:

■ Very Lightweight ML Classifiers (e.g., small RNNs, shallow feed-forward nets) or Rule-based filters: Operate directly on token logits or small contextual windows.

 ■ Quantized Models: For maximal speed. ■ Output: Binary flag (block/continue) per token, or probability adjustment. ○ Output Post-Response Classifier (Full Response): ■ Purpose: Final, comprehensive check on the complete LLM generated response (text, and potentially images/videos if multi-modal). Catches complex, subtle harms.

 ■ Latency: <100ms. More compute-intensive than input/stream. ■ Type: ■ Robust Transformer-based (e.g., RoBERTa-large, fine-tuned custom LLM) for text.

 ■ Pre-trained Vision/Video Models (e.g., CLIP-based, ViT for images, Temporal/3D ConvNets for video): For multi-modal outputs.

 ■ Multi-Task Classifier: To classify specific harm types (e.g., violence, nudity, hate speech).

 ■ Output: Probabilities for all harm categories + confidence. ○ Context Encoder: ■ Purpose: Provide user history, session context to classifiers for personalized or context-aware classification.

 ■ Latency: Flexible (can be pre-computed/cached). ■ Type: Transformer model (e.g., fine-tuned BERT/LLM for session context encoding).

 ○ Anomaly Detector: ■ Purpose: Identify novel jailbreak patterns or emerging threats that existing classifiers might miss. Operates more offline/batch.

 ■ Latency: Batch, hourly/daily. ■ Type: Autoencoders, Isolation Forests, statistical models on embedding space.

 ○ Meta-Classifier / Decision Engine: ■ Purpose: Combines scores from all classifiers, applies thresholds, business rules, and confidence estimates to make a final block/demote/allow decision.

 ■ Latency: Very low (<5ms, rule-based or shallow NN). ■ Type: Weighted voting, stacking, or simple learned NN. ● Training Objectives & Losses (Multi-Objective Optimization): ○ Primary: Weighted Cross-Entropy Loss per harm category (for multi-task classification), handling class imbalance.

 ○ Calibration Loss (e.g., Focal Loss): Improves confidence calibration, crucial for setting reliable thresholds and managing false positives/negatives.

 ○ Robustness Loss (Adversarial Training): Hardens models against jailbreaks by training on adversarial examples.

 ○ Fairness Loss: Constraints (e.g., demographic parity) to reduce bias in predictions across sensitive attributes.

 ● Speed Up Training: ○ Distributed Training: Data, model, and pipeline parallelism across H100 GPUs.

○ Optimization Techniques: Mixed precision, gradient checkpointing, dynamic loss scaling.

5. Evaluation (Diagnostic Mirroring) ● Offline Evaluation (Per Harm Category): ○ Metrics: PR-AUC and ROC-AUC for each harm category. PR-AUC is especially critical for rare, positive classes (harm).

 ○ Calibration Metrics: Brier Score, Expected Calibration Error (ECE) for robust thresholding.

 ○ Robustness Metrics: Attack Success Rate (ASR) on new/held-out adversarial test sets (jailbreaks).

 ○ Fairness Metrics: Demographic parity, equalized odds (ensure consistent performance across user groups).

 ● Human-in-the-Loop Evaluation: ○ Expert Review: Domain experts review edge cases, provide ground truth, and evaluate model explanations.

 ○ Red Team Assessment: Continuous, structured adversarial testing (with bug bounties) to proactively find system vulnerabilities.

 ○ User Studies: Controlled environments to assess real-world jailbreak attempts. ● Specialized Safety Evaluation: ○ Hallucination Detection: For LLM-generated explanations or safety reasoning. ○ Novel Attack Detection: Evaluate anomaly detector's performance. ● Online Evaluation (Real-time Feedback & Safety KPIs): ○ Harmful Impressions: (Key Metric) Total exposure to harmful content. Directly measures platform safety impact.

 ○ Proactive Rate: % of harm detected by system vs. user reports. Higher is better.

 ○ Valid Appeals Rate: % of correct user appeals. Lower is better (indicates fewer false positives).

 ○ Latency Monitoring: P50, P95, P99 for all classification stages. ○ User Satisfaction: Surveys, NPS scores (monitor impact of safety interventions). ○ Attack Detection Time: Track time from new attack observed to full mitigation deployment.

 ○ Escalation Rate: Monitor frequency of human review/expert intervention.

6. ML System Architecture (Strategic Brevity) ● Overall System Design: ○ User Input (Prompt/Response) → Real-time Filters → LLM (for generation) → Post-Processing Filters → Final Output to User ○ Parallel Monitoring & Feedback Loops: All stages feed into logging, anomaly detection, and human review.

 ● Core Components (Inference Stack): ○ Input Preprocessing: Normalization, tokenization, embedding. ○ Input Classifier(s): Fast, lightweight models for immediate prompt safety.

○ LLM: The core generative model (Claude/ChatGPT). ○ Output Stream Classifier: Token-level, ultra-low latency. ○ Output Post-Response Classifier: Comprehensive check on full response. ○ Context Encoder: Enriches classification with user/session data (features store). ○ Decision Engine: Combines classifier outputs, applies policy rules. ○ Explanation Generator: Provides user-facing reasons for blocking. ○ Violation Enforcement Service: Takes action (block, demote, alert human). ● Scalability: ○ Microservices: Decoupled classification services for independent scaling. ○ Auto-scaling (Kubernetes HPA): Based on latency/queue depth. ○ Geographic Distribution: Low-latency regional deployments. ○ Model Sharding: Distribute large models (e.g., if LLM is part of classifier itself). ● Model Management: ○ A/B Testing / Canary Releases: Gradual, safety-guarded rollouts of new classifier versions.

 ○ Blue/Green Deployments: For zero-downtime updates with quick rollback. ○ Model Versioning: Clear lineage for audits. ● Continuous Learning & Adaptation: ○ Real-time Learning Pipeline: Detects new jailbreaks, generates synthetic data, triggers incremental model retraining.

 ○ Human Feedback Integration: Streamlined expert review, user appeal process, red team data feed into retraining loops.

 ○ Knowledge Management: Centralized database of threat intelligence and attack patterns.
