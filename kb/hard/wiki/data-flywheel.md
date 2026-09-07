---
concept: Data Flywheel & Feedback Loops
tags: [data-flywheel, feedback-loops, labeling, moat]
sources:
  - kb/hard/raw/eugene-yan/39-lessons-on-building-ml-systems-scaling-execution-and-more.md
  - kb/hard/raw/eugene-yan/bootstrapping-labels-via-supervision-human-in-the-loop.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/ml-production-maintenance|ML Production Maintenance]]"
  - "[[hard/wiki/recommendation-systems|Recommendation Systems]]"
  - "[[hard/wiki/bandits-exploration-exploitation|Bandits & Exploration-Exploitation]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Data Flywheel & Feedback Loops

A data flywheel is a compounding system: better predictions generate more engagement, more engagement generates better labels, better labels train better models, which generate better predictions. When this loop is tight and fast, it becomes a durable competitive advantage. When it's slow, leaky, or broken, it can instead produce vicious cycles that silently degrade performance.

## The Flywheel as Competitive Moat

Data alone is not the moat — data is abundant. The competitive advantage is **who turns the flywheel faster**. A team with 10 million labeled examples but a slow iteration cycle may lose to a team with 1 million examples that can close the prediction-to-outcome loop twice as fast.

The design question is not "how do we collect more data?" but "how do we close the loop between what the model predicts and what actually happens?" Karpathy's description of Tesla Autopilot is the canonical example: the fleet generates billions of prediction opportunities every day, edge cases are automatically identified, curated into training sets, and fed back to retrain the model. Each generation of the model is better than the last not because of smarter algorithms but because of better feedback infrastructure.

Whoever owns the feedback loop owns the moat. This means the flywheel should be a first-order design consideration from the beginning of a system, not an afterthought bolted on after deployment.

## Closing the Prediction-Outcome Loop

Closing the loop requires aligning the time horizon of labels with the action being predicted. This is harder than it sounds:

**Short-term proxies are misleading.** Click-through rate is immediately available and easy to measure, but clicking is not the same as purchasing, watching the whole video, or returning to the platform. Models optimized on short-term proxies can systematically diverge from long-term user value.

**Long-term rewards are delayed and attribution is noisy.** If a recommendation today contributes to a subscription renewal six months from now, how do you attribute credit? Delayed reward structures make feedback loops slow and training signals sparse.

**Labels can become stale.** A predicted fraud flag from three days ago may be reversed when the customer calls in. A hospitalization duration estimated at admission becomes an actual value after discharge. Training on premature labels propagates incorrect signals that can compound into feedback loops of their own. The practical mitigation: be explicit about label maturity windows and refuse to train on labels that could still change.

**Positional bias in feedback data.** In ranking or recommendation, items shown in prominent positions receive more clicks not because they're better but because they're more visible. Training directly on these biased interactions will reinforce the position bias. The standard fix is to include positional features during training (so the model accounts for position effects) and drop or zero out those features at serving time.

## Bootstrapping Labels from Scratch

Before any flywheel can spin, you need seed labels. Most ML tutorials assume labels exist; in practice, getting the first set of labels is one of the hardest parts of building an ML system.

**Weak supervision** is the fastest path to a large number of labels, at the cost of quality. Labeling functions formalize domain heuristics: regex rules on text fields, aggregated statistics, knowledge graph lookups, pre-trained models used as teachers. Multiple labeling functions are combined using a generative model (e.g., Snorkel) that estimates each function's accuracy based on their agreement and disagreement patterns and produces probabilistic labels. Google's Snorkel DryBell applied this at scale: for topic classification, 10 labeling functions matched the performance of 80,000 hand-labeled samples.

Weak supervision works especially well in the early stage when you have no labeled data and need a starting point quickly. The generated labels are imperfect but good enough to train a first-generation model, which can then be used to generate better labels.

**Semi-supervised learning** extends a small labeled seed into a larger pseudo-labeled dataset. The procedure: train a high-precision model on hand-labeled data, predict on unlabeled data, select the most confident predictions as pseudo-labels, add them to training data, repeat. Each cycle expands the effective training set. The risk is error amplification — if the seed model has systematic biases, those biases get scaled up. Controlling pseudo-label quality with a confidence threshold is essential.

**Active learning** identifies which unlabeled samples are most valuable for human annotation. Uncertainty sampling selects examples where the model's confidence is lowest (e.g., predicted probability close to 0.5 for binary classification). Query-by-committee extends this by sampling examples where an ensemble of models disagrees most. Information density adds a second criterion: among uncertain samples, prefer ones that are representative of the overall data distribution rather than outliers.

DoorDash's menu item tagging is an instructive example. They started with a high-precision classifier to generate seed labels, then used active learning to select ambiguous samples for professional annotation. To improve precision, they selected samples where model predictions conflicted with annotator labels; to improve recall, they selected low-confidence predictions. Samples went to Mechanical Turk for a first pass; more ambiguous cases escalated to professional annotators. Cross-rater agreement was the primary quality metric.

Facebook's SEALS approach adds a filtering step before active learning: use nearest neighbor search to identify samples close to existing positives before running uncertainty sampling. This matters when data is heavily imbalanced (1-in-1,000 positives) — without filtering, most selected samples are easy negatives. With nearest neighbor pre-filtering, SEALS matched the performance of full active learning while considering only 2–15% of the candidate pool.

## Designing Labeling Functions

Defining good labeling functions and annotation guidelines is harder than it appears. Andrej Karpathy noted after four years of running Tesla's labeling pipeline: "I still haven't 'solved' labeling workflows." Practical guidelines from DoorDash's experience:

- Make tags mutually exclusive (annotators move on faster, annotation volume decreases).
- Partition the taxonomy at the top level by distinct attribute dimensions (parallelizes annotation tasks).
- Always include an "Other" bucket at each level (captures emerging categories without forcing poor fits).
- Ensure tags are objective, not subjective (avoid labels like "popular" or "convenient" that change with context).

Think beyond HITL annotation. Users often generate implicit labels through their behavior: how they organize bookshelves, what they click on, what they buy and return. GoodReads bookshelf names can seed book attribute tags. Search click data can label semantic search relevance. Creative use of behavioral data as weak supervision dramatically expands labeling throughput at near-zero cost.

## Human-in-the-Loop at Scale

Even with automation, human judgment remains important at the margins. The design pattern is a tiered system:

1. High-confidence predictions are auto-decided.
2. Medium-confidence predictions go to a first-pass annotation tier (e.g., Mechanical Turk).
3. Low-confidence or ambiguous predictions escalate to expert annotators.
4. A small "golden set" of expert-labeled examples is mixed into all annotation queues to monitor annotator quality and catch systematic bias from new vendors.

As the system matures and models improve, the auto-decision threshold rises and the HITL load decreases. The flywheel accelerates.

## Evals as Competitive Infrastructure

Closely related to the data flywheel is the eval infrastructure. Teams that invest early in robust evaluation frameworks can continuously ship reliable improvements; teams that don't spend most of their time unsure whether changes are actually better. Evals — both offline metrics and online A/B tests — are the sensory system of the flywheel. Without them, you cannot measure whether the loop is spinning forward or backward.

## Sources

- Yan, Eugene. "39 Lessons on Building ML Systems, Scaling, Execution, and More." eugeneyan.com, Nov 2024. https://eugeneyan.com/writing/conf-lessons/
- Yan, Eugene. "Bootstrapping Labels via ___ Supervision & Human-In-The-Loop." eugeneyan.com, Aug 2021. https://eugeneyan.com/writing/bootstrapping-data-labels/
