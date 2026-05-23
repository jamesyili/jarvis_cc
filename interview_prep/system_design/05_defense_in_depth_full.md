# [Design] Defense-in-Depth ML Classifier (full)

*Source: `interview_prep/system_design_prep.pdf`, pages 32–38. James's prep notebook — extracted text, lightly cleaned.*

---

7. Safety, Security & Bias Mitigation (High Integrity) ● Defense in Depth: Multi-layered approach (input, mid-gen, output, human review) ensures redundancy.

 ● Robustness: Adversarial training, chaos engineering (testing resilience). ● Privacy: End-to-end encryption, PII masking. ● Bias Mitigation: ○ Proactive: Auditing training data for bias (e.g., in constitutional synthetic data), fairness constraints during training, adversarial debiasing.

 ○ Ongoing Monitoring: Real-time demographic breakdown of classifications, regular audits, user community feedback.

 ○ Rapid Response: Protocols for addressing discovered bias issues.

[Design] Defense-in-Depth ML Classifier System Design Blueprint
Clarify Requirements

Business Objectives and Metrics
● Safety KPIs : Jailbreak prevention rate (target: >95%), false positive rate (<1%), time-to-mitigation for new attacks (<24 hours)
 ● User Experience : Response latency (<200ms additional overhead), user satisfaction (maintain >4.5/5), unnecessary refusal rate (<0.5%)
 ● Operational Metrics : System uptime (99.9%), throughput (support 10M+ daily interactions), cost per classification (<$0.001)
 ● Regulatory Compliance : CBRN content blocking (100% for high-confidence cases), policy violation detection (>90% recall)
Core Features
● Multi-modal Classification : Text, image, audio, video content analysis ● Real-time Filtering : Pre-prompt, mid-generation, post-response classification ● Adaptive Learning : Continuous retraining on new attack patterns ● Hierarchical Escalation : Automated blocking → human review → expert analysis ● Context-Aware Analysis : User history, session context, intent understanding
Data Sources
● Synthetic Adversarial Data : Constitutional AI generated harmful/benign examples ● Red Team Outputs : Human adversarial testing results, bug bounty submissions ● Production Logs : User interactions, blocked content, false positive reports ● Threat Intelligence : External security feeds, academic research, industry sharing ● Labeled Datasets : Human-annotated harmful content, expert domain knowledge
Scale and Performance Requirements
● Volume : 50M+ daily user interactions, 100K+ queries per second at peak ● Latency : <50ms input classification, <100ms output classification, <200ms total overhead
 ● Growth : 10x scale growth over 2 years, support for new modalities quarterly ● Availability : 99.99% uptime, graceful degradation under attack, geographic distribution
Frame as ML Task
Task Classification
● Primary : Multi-class discriminative classification (harmful categories: CBRN, fraud, harassment, etc.)
 ● Secondary : Generative synthetic data creation for training augmentation ● Tertiary : Anomaly detection for novel attack pattern identification
Input/Output Design
● Inputs : ○ Text prompts (raw, encoded, multi-language) ○ Generated responses (partial, complete) ○ Context vectors (user history, session data) ○ Multi-modal content (images, audio embeddings)

● Outputs : ○ Classification probabilities per harm category ○ Confidence scores and uncertainty estimates ○ Explanatory features for human review ○ Recommended actions (block, flag, allow)
Model Architecture Strategy
● Multiple Specialized Models : Domain-specific classifiers (CBRN, fraud, etc.) rather than single multi-class
 ● Ensemble Approach : Constitutional classifiers + traditional ML + rule-based systems ● Modality-Specific : Separate models for text, vision, audio with fusion layer ● Multi-Scale : Token-level, sentence-level, document-level classification
Algorithm Selection
● Constitutional Classifiers : Transformer-based models trained on synthetic constitutional data
 ● Traditional ML : Gradient boosting (XGBoost) for structured features, SVMs for high-precision cases
 ● Deep Learning : BERT/RoBERTa variants for text, ConvNets for images, specialized architectures for audio
 ● Ensemble Methods : Weighted voting, stacking, or learned combination strategies
Data Prep
Data Collection Strategy
● Constitutional Synthesis : Use target LLM to generate diverse harmful/benign examples following constitutional principles
 ● Adversarial Augmentation : Transform benign examples with known jailbreak techniques (encoding, role-play, injection)
 ● Real-world Sampling : Carefully curated production examples (anonymized, consent-based)
 ● Expert Annotation : Domain experts label edge cases, provide ground truth for complex scenarios
 ● Continuous Ingestion : Real-time pipeline for new attack patterns, threat intelligence feeds
Data Cleaning and Quality
● Deduplication : Semantic similarity detection to remove near-duplicates across languages/encodings
 ● Quality Filtering : Remove low-quality synthetic examples, ensure human expert validation
 ● Bias Detection : Systematic analysis for demographic, linguistic, cultural biases in training data
 ● Privacy Protection : PII scrubbing, differential privacy techniques, data anonymization ● Version Control : Data lineage tracking, reproducible dataset creation, audit trails

Data Efficiency and Storage
● Columnar Storage : Parquet format with bloom filters for fast harmful content queries ● Hierarchical Sharding : ○ Tier 1: By harm category (CBRN, fraud, etc.) ○ Tier 2: By language/region ○ Tier 3: By time period for temporal analysis ● Semantic Indexing : ○ FAISS vector indices for embedding-based similarity search ○ Elasticsearch for full-text search across harmful content patterns ○ Specialized indices for jailbreak pattern matching ● Caching Strategy : ○ L1: Hot classification results (Redis) ○ L2: Frequently accessed model artifacts ○ L3: Historical attack pattern database Modeling
Model Architecture
Constitutional Classifier Design
● Input Classifier : RoBERTa-large fine-tuned on constitutional synthetic data ● Output Classifier : Similar architecture, optimized for generated text analysis ● Context Encoder : Transformer model encoding user/session context for personalized classification
 ● Fusion Layer : Multi-head attention mechanism combining input, output, and context signals
Ensemble Architecture Input → [Constitutional Classifier] → Score ₁ → [Traditional ML Pipeline] → Score ₂ → [Rule-based System] → Score ₃ → [Anomaly Detector] → Score ₄ → [Meta-Classifier] → Final Decision
Training Process and Datasets
Multi-Stage Training Pipeline
1. Foundation Training : Large-scale pretraining on diverse text corpus 2. Constitutional Training : Fine-tuning on synthetic harmful/benign examples 3. Adversarial Training : Hardening against known jailbreak techniques 4. Domain Adaptation : Specialized training for CBRN, fraud, etc. 5. Continuous Learning : Online learning from production feedback
Dataset Composition
● Constitutional Synthetic : 70% (balanced harmful/benign across categories) ● Real-world Samples : 20% (carefully curated and anonymized)

● Adversarial Examples : 10% (red team outputs, jailbreak attempts)
ML Objectives and Loss Functions
Multi-Objective Optimization
● Primary Loss : Weighted cross-entropy with class balancing for harm categories ● Calibration Loss : Focal loss component to improve confidence calibration ● Robustness Loss : Adversarial training loss to improve jailbreak resistance ● Fairness Loss : Demographic parity constraints to reduce bias
Specialized Loss Components Total_Loss = λ ₁ * CrossEntropy_Loss + λ ₂ * Focal_Loss + λ ₃ * Adversarial_Loss + λ ₄ * Fairness_Loss + λ ₅ * Uncertainty_Loss
Speed Up Model Training
Distributed Training Strategy
● Data Parallelism : Split constitutional synthetic data across 8-16 GPUs ● Model Parallelism : Large transformer layers distributed across multiple devices ● Pipeline Parallelism : Stage different training phases across device clusters ● Gradient Accumulation : Handle large effective batch sizes with memory constraints
Optimization Techniques
● Mixed Precision Training : FP16 for forward pass, FP32 for loss computation ● Gradient Checkpointing : Trade compute for memory in large models ● Dynamic Loss Scaling : Prevent gradient underflow in mixed precision ● Learning Rate Scheduling : Warmup + cosine decay for stable convergence
Model Sampling and Inference
Real-time Classification Strategy
● Greedy Classification : Argmax for high-confidence decisions (>95% certainty) ● Ensemble Sampling : When confidence <95%, sample from multiple model predictions ● Temperature Scaling : Calibrate output probabilities for better uncertainty estimation ● Threshold Optimization : ROC curve analysis to set optimal decision boundaries per harm category
Uncertainty Quantification
● Monte Carlo Dropout : Multiple forward passes with dropout for uncertainty estimation ● Ensemble Disagreement : Measure variance across ensemble member predictions ● Calibration Metrics : Reliability diagrams, Expected Calibration Error (ECE)

Evaluation
Offline Evaluation
Standard Metrics per Harm Category
● Classification Metrics : Precision, Recall, F1-score, AUC-ROC per category ● Calibration Metrics : Brier score, Expected Calibration Error, reliability diagrams ● Robustness Metrics : Attack Success Rate (ASR) on adversarial test sets ● Fairness Metrics : Demographic parity, equalized odds across user groups
Human-in-the-Loop Evaluation
● Expert Review : Domain experts evaluate edge cases and model explanations ● Red Team Assessment : Structured adversarial testing with bounty incentives ● User Study : Representative users attempt to jailbreak system in controlled environment ● Cross-validation : Multiple expert annotators for inter-rater reliability
Specialized Safety Evaluation
● Hallucination Detection : Automated fact-checking of generated explanations ● Jailbreak Resistance : Systematic testing against known attack patterns ● Novel Attack Detection : Anomaly detection evaluation on held-out attack methods ● Multi-modal Robustness : Cross-modal attack resistance (text→image, etc.)
Online Evaluation
Real-time Performance Metrics
● Latency Monitoring : P50, P95, P99 classification latency across geographic regions ● Throughput Tracking : Queries per second, concurrent user handling ● Error Rate Monitoring : Classification failures, timeout rates, system errors ● Resource Utilization : GPU/CPU usage, memory consumption, bandwidth
User Experience Metrics
● False Positive Rate : User appeals, unnecessary blocking reports ● User Satisfaction : Post-interaction surveys, NPS scores ● Task Success Rate : Completion rate for legitimate user requests ● Engagement Impact : Session length, user retention after safety interventions
Safety Effectiveness Metrics
● Harm Prevention : Blocked attacks per day, prevented policy violations ● Attack Detection Time : Time from new attack pattern to successful blocking ● Escalation Rate : Cases requiring human review, expert intervention ● Prevalence Tracking : Harmful content trends, emerging threat patterns
ML System Architecture
Core System Components

Classification Pipeline Input → [Preprocessing] → [Input Classifier] → [LLM] → [Output Classifier] → [Post-processing] → Response
 ↓ ↓ [Context Encoder] [Explanation Generator] ↓ ↓ [User History DB] [Human Review Queue]
Real-time Inference Stack
● Load Balancer : Geographic routing, model version management ● Model Serving : TensorRT optimized models, batch inference optimization ● Feature Store : Real-time context features, user embeddings ● Decision Engine : Ensemble combination, threshold application, action determination ● Monitoring : Performance tracking, drift detection, alert systems
Scalability Architecture
Horizontal Scaling Strategy
● Microservices : Independent scaling of input/output classifiers, context encoders ● Auto-scaling : Kubernetes HPA based on queue depth, latency targets ● Geographic Distribution : Regional deployments for latency optimization ● Model Sharding : Distribute large models across multiple inference servers
Model Management
● A/B Testing : Gradual rollout of new model versions with safety guardrails ● Blue/Green Deployment : Zero-downtime model updates with instant rollback capability ● Model Versioning : Semantic versioning, compatibility tracking, rollback procedures ● Canary Releases : New models tested on small traffic percentage before full deployment
Continuous Learning and Adaptation
Real-time Learning Pipeline
● Attack Detection : Continuous monitoring for novel jailbreak patterns ● Synthetic Data Generation : Automated creation of training data for new attacks ● Model Retraining : Incremental learning, catastrophic forgetting prevention ● Performance Monitoring : Model drift detection, performance degradation alerts
Human Feedback Integration
● Expert Annotation : Streamlined workflow for expert review of edge cases ● User Feedback : Appeal process integration, false positive correction ● Red Team Integration : Continuous adversarial testing, bug bounty programs ● Knowledge Management : Centralized threat intelligence, attack pattern database
Safety and Security
