---
concept: Counterfactual & Offline Policy Evaluation
tags: [counterfactual, ips, off-policy-evaluation, position-bias]
sources:
  - kb/hard/raw/eugene-yan/counterfactual-evaluation-for-recommendation-systems.md
  - kb/hard/raw/eugene-yan/how-to-measure-and-mitigate-position-bias.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/recsys-evaluation|RecSys Evaluation]]"
  - "[[hard/wiki/bandits-exploration-exploitation|Bandits & Exploration-Exploitation]]"
  - "[[hard/wiki/a-b-testing|A/B Testing]]"
---

# Counterfactual & Offline Policy Evaluation

Standard offline evaluation of recommendation systems has a fundamental flaw: it treats recommendations as an observational problem when they are actually interventional. Counterfactual evaluation addresses this by asking "what would have happened if we had shown different recommendations?" — enabling offline estimation of A/B test outcomes without running the experiment.

## The Observational vs. Interventional Problem

In supervised ML, we learn `P(label | features)` — given an input, predict an output. The model doesn't affect what inputs it sees. This is an **observational problem**.

Recommendations are different. We want to learn `P(click=True | recommend=iphone, user_context)` — the probability of a good outcome given a specific intervention (showing iPhone). But when we train on logged data, we observe only what users did with the recommendations that were actually shown, not what they would have done with different recommendations. **Our recommendations changed the data we collected.** This is an **interventional problem**.

The practical consequence: standard offline evaluation measures how well new recommendations fit logged data, not whether they would actually improve user behavior. This is why offline metrics and online A/B test results frequently diverge. A model that ranks well on historical data may not produce better outcomes — it may just be predicting what the old model already showed.

## Inverse Propensity Scoring (IPS)

IPS reweights logged rewards by how much more or less the new policy would make each recommendation relative to the old policy:

```
IPS estimate = (1/N) * Σ [ (πe(a|x) / π0(a|x)) * r ]
```

Where:
- `πe(a|x)` = new policy's probability of recommending item a given context x
- `π0(a|x)` = old (logging) policy's probability of recommending item a given context x
- `r` = observed reward (click=1, no-click=0) in logged data
- `N` = number of logged observations

**Intuition**: If the new model recommends iPhone on the Pixel page 60% of the time (`πe = 0.6`) but the old model only recommended it 40% of the time (`π0 = 0.4`), then iPhone is shown 1.5x more often under the new policy. When we see a click on iPhone in the logs, we upweight it by 1.5 to account for the new policy's higher recommendation rate. When the new policy recommends something rarely shown before, the importance weight is large; when it rarely shows something the old policy showed often, the weight is small.

**Getting propensity scores**: Three approaches:
1. Normalize raw recommendation scores via Plackett-Luce to get probabilities
2. Count recommendation frequency in the recommendation store
3. Use impression counts (Eugene Yan's preferred approach — most direct measure of recommendation probability, best adjusts for presentation bias)

## Variants and Improvements

### Clipped IPS (CIPS)

IPS can have high variance when the new policy differs substantially from the logging policy. If `π0(a|x) = 0.001` and we observe a single click, reweighting by `πe(a|x) / π0(a|x)` could multiply by 1000x — severe overestimation.

CIPS caps the importance weight at a threshold τ:
```
CIPS weight = min(πe(a|x) / π0(a|x), τ)
```

Reduces variance but introduces bias (clipped weights underestimate policy value for tail recommendations). Requires tuning τ.

### Self-Normalized IPS (SNIPS)

SNIPS divides the IPS estimate by the sum of importance weights:
```
SNIPS = Σ [weight * r] / Σ [weight]
```

This rescaling prevents overinflated estimates without requiring a clipping parameter. In Yuta Saito's RecSys 2021 experiments (synthetic data, 10 arms), SNIPS had the lowest estimation error of all methods. The downside: SNIPS requires computing importance weights for all observations (including non-rewarded ones), not just those with `r > 0`. Since most recommendations have zero reward (CTR < 10%), this increases storage and compute by ~10x.

### Doubly Robust (DR) Estimator

Combines IPS with the Direct Method (DM). DM trains a reward model to impute missing rewards. DR: `DM_estimate + (1/N) * Σ [weight * (r - reward_model(x, a))]`. IPS corrects bias when the reward model is wrong; when the reward model is accurate, variance is reduced. DR gets the best of both approaches — lower variance than IPS, lower bias than DM.

## Insufficient Support Problem

IPS breaks down when the new policy recommends items that the logging policy never showed — `π0(a|x) = 0` means no logged data exists for that recommendation. The importance weight is undefined.

**Mitigations**:
- Show random samples of non-recommended items on a small fraction of traffic to collect interaction data for unseen recommendations (operationally, PMs often resist this)
- Ensure all eligible items have a small non-zero recommendation probability (epsilon-floor policy)
- Accept that IPS estimates are only valid for items with logged support — new items need online evaluation

## Off-Policy Evaluation via Replay

For bandit policies, the **replay method** (Li et al., 2011) is widely used. It requires logged data from a (approximately) uniform random policy. For each event in the log: if the new policy's chosen action matches the logged action, count the reward; otherwise, discard the event.

Replay provides an unbiased estimate of new policy value under uniform random logging. Netflix, Yahoo, and Spotify have all used variants of this approach.

## Position Bias

Position bias is a specific, pervasive form of bias in recommendation evaluation: items ranked higher receive more clicks simply because they're more visible, not because they're more relevant.

On Google Search, position 1 receives ~10x more clicks than position 10. Netflix recommendations are scanned left-to-right. Any model trained on this data will learn to predict what was shown prominently, not what was actually most relevant. Training on position-biased data creates a self-reinforcing feedback loop.

### Measuring Position Bias

**RandTopN**: Shuffle top results randomly, holding items constant to isolate position effect. Clean identification but degrades UX.

**Inherent randomness**: Exploit natural position variation across ranker versions or multiple widgets. Netflix's carousels showing the same item at different positions across widgets provide this signal without experiments.

**Expectation-maximization**: Model clicks as product of examination (position-dependent) × relevance (item-dependent). Fit EM on logged data to separate the two effects. Google demonstrated this on email and storage search logs.

**Pair swaps (FairPairs, RandPair)**: Swap items at positions k and k+1, keeping relevance constant. Lighter UX impact than full shuffling.

**Boltzmann exploration**: Normalize raw scores to probabilities, sample to populate positions. Anchors items near their original position while enabling measurement.

### Mitigating Position Bias in Training

**Position as a feature**: Include position as a model input during training; set to 1 for all items at serving time. Model learns and then cancels the position effect. Recommended in Google's Rules of Machine Learning.

**Propensity-weighted training**: Inverse-propensity-weight the training loss using measured examination probabilities. Lower-position items get higher weight, counteracting their underrepresentation.

## Why Interventional Evaluation Matters for Production ML

The interventional framing resolves a common confusion in recsys teams: "our offline metrics improved but A/B test showed no gain." Both observations can be true simultaneously:
- The new model fits historical logged data better (higher offline NDCG)
- The new model doesn't change behavior because users can only interact with what's shown, and the logged data doesn't represent counterfactual clicks

IPS/SNIPS closes this gap by asking the right causal question. Teams that only look at observational offline metrics are measuring model fit to biased history, not policy value. The asymptotic solution is running A/B tests; counterfactual evaluation is the practical bridge for offline development cycles.

## Sources

- Eugene Yan: [Counterfactual Evaluation for Recommendation Systems](https://eugeneyan.com/writing/counterfactual-evaluation/)
- Eugene Yan: [How to Measure and Mitigate Position Bias](https://eugeneyan.com/writing/position-bias/)
