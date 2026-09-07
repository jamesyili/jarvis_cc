---
concept: Data Quality & Curation
tags: [data-quality, labeling, semi-supervised, active-learning, annotation]
sources:
  - kb/hard/raw/lilian-weng/thinking-about-high-quality-human-data.md
  - kb/hard/raw/lilian-weng/learning-with-not-enough-data-part-1-semi-supervised-learning.md
  - kb/hard/raw/cameron-wolfe/a-guide-for-debugging-llm-training-data.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/synthetic-data|Synthetic Data for Fine-Tuning]]"
  - "[[hard/wiki/llm-post-training|LLM Post-Training]]"
  - "[[hard/wiki/neural-network-training|Neural Network Training]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Data Quality & Curation

The persistent underappreciation of data work in ML is well-documented. "Everyone wants to do the model work, not the data work" (Sambasivan et al., 2021). Yet in LLM development, the primary factor distinguishing success from failure is the quality of the training dataset. Data curation is not a prerequisite to the real work — it is the work. Cameron Wolfe's guide observes that the majority of interventions in any LLM training cycle are data-related: tweak the data, leave everything else fixed, retrain, measure.

## The Data-Centric AI Movement

The shift from model-centric to data-centric AI recognizes that holding architecture and training procedure constant and improving data quality reliably improves model performance more predictably than architectural search. For LLMs specifically, this has manifested in: sophisticated data mixtures, quality classifiers, deduplication pipelines, and model-guided filtering. The Llama 2 report describes multiple post-training stages, each collecting additional data — the data pipeline is continuous, not a one-time setup.

## Human Raters and Data Quality

High-quality human annotation involves three operational stages: task design, rater selection and training, and aggregation with quality control. Each introduces failure modes.

**Task design**: Detailed guidelines help but impose a learning overhead. Long guidelines reduce rater variance but require substantial training investment. A common failure mode is guidelines that are clear to authors but ambiguous to raters encountering edge cases.

**Rater selection and calibration**: Annotators need matched skillsets and ongoing calibration sessions. Agreement with a gold set of examples is the standard proxy for competence.

**Aggregation methods:**

- **Majority voting**: Simple mode of labels, treats all annotators equally.
- **Raw agreement**: Percentage of annotators agreeing with a given annotation; biased toward majority class.
- **Cohen's Kappa**: The canonical inter-rater agreement metric. Corrects for chance agreement via: κ = (p_o − p_e) / (1 − p_e), where p_o is observed agreement and p_e is expected agreement by chance. More reliable than raw agreement, but the chance correction can be overestimated when one label is heavily prevalent.
- **Probabilistic graph models (MACE)**: Model annotator reliability as a latent variable. MACE models each annotator's trustworthiness θ_j and spamming behavior. EM or Variational Bayes maximizes marginal likelihood over annotations. Outputs trust-weighted majority vote. Identifies spammers who game annotation volume incentives.

**The two annotation paradigms** (Rottger et al., 2021):

| Paradigm | Goal | Use case |
|---|---|---|
| Prescriptive | Apply one consistent standard; minimize subjectivity | Safety classifiers, factuality labels |
| Descriptive | Capture diverse perspectives; embrace disagreement | Toxicity detection, sentiment on social topics |

The descriptive paradigm is essential when annotator identity matters. Research shows that agreement rates on toxicity vary dramatically by topic (0.96 on violence vs. 0.25 on personal topics), and annotator demographics (African American, LGBTQ identity) significantly affect labeling of identity-related content. Forcing a single gold label in these contexts produces a model that encodes one group's perspective as universal.

**Disagreement deconvolution** (Gordon et al., 2021): Disentangles stable opinions from stochastic annotation errors by anchoring labels to each annotator's primary label. The model estimates p_flip (probability of non-primary label per sample), adjusts the label distribution to remove noise, and produces a cleaner test set. This preserves genuine disagreement while removing individual inconsistency.

**Jury Learning**: Models the full jury-selection process — train on annotator characteristics (demographics, behavior), learn to predict each individual's labels, then at decision time specify jury composition for targeted aggregation. Built on a Deep & Cross Network with shared BERT text encoding and annotator embeddings.

## Detecting Mislabeled Data via Training Dynamics

Once a dataset is assembled, several techniques identify potentially mislabeled examples using model training behavior.

**Influence functions** (Koh & Liang, 2017): Measure the impact of each training point on model parameters and predictions via the inverse Hessian. Approximating leave-one-out retraining without actually running it: I_up_loss(z, z_test) = −∇θL(z_test)^T H^−1 ∇θL(z, θ̂). High negative influence on a sample's own prediction suggests mislabeling. Computationally expensive at scale; EK-FAC approximations make it practical for large models.

**Data Maps** (Swayamdipta et al., 2020): Track per-sample model confidence (mean probability of true label across epochs) and variability (standard deviation). Hard-to-learn samples (low confidence, low variability) are more likely mislabeled. Ambiguous samples (high variability) contain useful OOD generalization signal — don't remove them. A simple noise classifier trained on confidence scores can identify mislabeled instances.

**AUM (Area Under the Margin)** (Pleiss et al., 2020): Tracks the margin between the assigned label's logit and the next-highest logit across training. Mislabeled samples have systematically lower AUM due to gradient tension between generalization signal and wrong label. "Threshold samples" with deliberately flipped labels calibrate the AUM threshold for detection.

**Noisy Cross-Validation (NCV/INCV)**: Splits dataset in half, trains on one half, identifies samples where the predicted label matches the actual label from the held-out model. Iteratively builds a clean trusted set. Simple and scalable without needing training dynamics access.

**Forgettable examples** (Toneva et al., 2019): Track whether a correctly classified sample gets later misclassified (a "forgetting event"). Unforgettable examples are never forgotten once learned — these can often be safely removed without model degradation. Forgettable examples tend to be mislabeled or visually unusual.

## Semi-Supervised Learning

Semi-supervised learning (SSL) learns from both labeled and unlabeled data simultaneously via a joint loss: L = L_s + μ(t) · L_u. The unsupervised loss L_u is designed around consistency regularization or pseudo-labeling.

**Consistency training** assumes that the model should give the same prediction for an input and its augmented version (or two random augmented views). Methods:

- **Π-model**: Two stochastic passes of the same input must yield consistent predictions. MSE between two outputs.
- **Temporal Ensembling**: Maintains an EMA of predictions per sample as the consistency target — reduces compute vs. Π-model by avoiding double-pass.
- **Mean Teacher**: EMA over model *weights* rather than outputs. Faster-updating teacher provides more accurate targets. Requires input augmentation or student dropout.
- **UDA (Unsupervised Data Augmentation)**: Uses high-quality augmentations (RandAugment for images, back-translation + TF-IDF replacement for text) for consistency. Key training tricks: mask low-confidence unlabeled examples (threshold τ), sharpen prediction distributions (temperature T), filter for in-domain data.
- **ICT (Interpolation Consistency Training)**: Applies MixUp to unlabeled pairs, expects the model's prediction on the mixture to match the interpolation of predictions on each component. Operates near class decision boundaries per the low-density separation assumption.
- **VAT (Virtual Adversarial Training)**: Perturbs inputs in the direction that most changes the model's prediction; trains the model to be robust to this worst-case perturbation on unlabeled data.

**Pseudo-labeling**: Assign the model's argmax prediction as a soft label for unlabeled examples, then train on all data in a supervised manner. Equivalent to entropy regularization — minimizes conditional entropy of predictions, pushing decision boundaries to low-density regions. Requires iterative refinement; the teacher/student distinction is conceptual, not architectural.

**FixMatch and MixMatch** (not in source but common implementations): Combine confidence-thresholded pseudo-labels with strong augmentation, essentially unifying pseudo-labeling and consistency training. These represent the practical state of SSL for vision tasks.

The key SSL hypotheses are:
- **Smoothness**: Close points in high-density regions share labels.
- **Cluster assumption**: Dense clusters share a label.
- **Low-density separation**: Decision boundaries live in sparse regions.
- **Manifold assumption**: High-dimensional data lies on low-dimensional manifolds.

These assumptions motivate why consistency training on unlabeled data helps: it enforces that the model respects the data's inherent cluster structure.

## Debugging LLM Training Data

For LLMs specifically, Cameron Wolfe identifies two complementary debugging modes:

**Data-focused curation** (independent of model training):
- Manual inspection — time-consuming but irreplaceable. LLM researchers report spending a large fraction of their time here. Pattern recognition from manual inspection seeds the heuristics.
- Heuristic filtering — string matching, regex, format validation, source-based quality scoring.
- Model-based filtering — fastText classifiers for language ID and toxicity detection at pretraining scale; LLM-as-judge for post-training. Llama 4 removed 50%+ of SFT data tagged as "easy" by a Llama judge, focusing training on harder examples.

**Model-focused curation** (using a trained model to find data issues):
- Identify poor model outputs through evaluation (human or automatic).
- Search for training examples contributing to those outputs via lexical search (BM25/inverted index) or semantic search (bi-encoder + vector database + HNSW).
- Modern hybrid systems combine BM25 retrieval with cross-encoder re-ranking.
- OLMoTrace (AI2): Efficient suffix-array based approach to trace LLM outputs back to training data at scale.

The iteration loop is: evaluate → identify failures → trace to data → curate → retrain. Most performance gains come from this cycle, not from architecture changes.

## The Active Learning Connection

Active learning — selecting the most informative unlabeled examples to label next — is the data-centric complement to SSL. While SSL exploits all unlabeled data, active learning focuses the labeling budget. The two approaches compose naturally: use SSL to extract signal from cheap unlabeled data, use active learning to prioritize which examples are worth expensive human annotation. Data Maps (confidence + variability) directly inform active learning: hard-to-learn and ambiguous examples are both informative candidates.

## Sources

- Lilian Weng, "Thinking about High-Quality Human Data" (Feb 2024) — `kb/hard/raw/lilian-weng/thinking-about-high-quality-human-data.md`
- Lilian Weng, "Learning with Not Enough Data Part 1: Semi-Supervised Learning" (Dec 2021) — `kb/hard/raw/lilian-weng/learning-with-not-enough-data-part-1-semi-supervised-learning.md`
- Cameron Wolfe, "A Guide for Debugging LLM Training Data" (2025) — `kb/hard/raw/cameron-wolfe/a-guide-for-debugging-llm-training-data.md`
