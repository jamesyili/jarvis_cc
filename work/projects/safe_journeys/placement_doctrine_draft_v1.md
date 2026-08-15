# Where Quality and Safety Belong in the Stack

**A placement doctrine for Safe Journeys**

James Li · August 2026 · Draft for comment

> *Draft v1 — Leo-generated from James's dump, 2026-08-14. Edit before circulating. Political reads, the 7× selection-effect question, and the advocate framing are deliberately NOT in here — those live in `demotion_doctrine.md` and stay off the circulating version.*

---

## What this is

Michael's milestones doc asks for "a tech design that is scalable across surfaces and parts of the stack, and surface the tradeoffs." This is the tradeoff half.

It is not a competing design. Content Quality's *Integrating Quality/Safety Objectives into the Recommendation System — Design Options* is a thorough treatment of one region of the space, and most of what follows takes it as given. What this adds is the frame around it: a small set of axes that decide **which mechanism belongs at which layer**, and the two prerequisites that determine whether any of them will work.

The content comes from having built these systems twice — News Feed Integrity at Facebook, where the demotion stack was the product, and Stories content quality at Snap, where Michael and I shipped the closest analogue to the teen problem in front of us now.

## 1. Objective quality needs a stated outcome

Demotions and spacing driven by content-quality signals are an *objective* quality intervention. Objective interventions need a stated user outcome to be justified against; without one, every parameter is arbitrary.

For Safe Journeys the outcome is harm prevention: preventing bad experiences that can lead to harm. That is the right north star, and it should be the thing every distributional lever is argued against.

This is not a framing preference. As Section 4 shows, the objective/subjective distinction determines the *math* — different classes of signal require different functional forms, and a signal we cannot classify is a signal we cannot correctly apply.

## 2. Engagement and harm prevention converge, with a lag

A recommender exists to produce good experiences, which is to say engagement, retention, and value delivered to users. Harm prevention aims at the same place. Prevent bad experiences and retention should rise.

They are not, however, identical inside a two-week experiment window. Our own history says so: the racy filter cost roughly 4–5% of male impressions, and the vision doc accepts localized SSv2 cost explicitly. The honest statement is that **engagement and harm prevention converge on a longer horizon than the one our experiments measure.**

That has a concrete implication. If the payback period is longer than the test period, the only instrument that can observe it is a **long-running holdout on the safety metric itself.** Michael's doc already asks whether we can create and maintain a holdout on USR. We should treat that as the first commitment of the measurement workstream rather than an open question, because without it every safety launch will be evaluated on the axis where it looks worst.

## 3. Four placement axes

### Axis 1 — Where in the funnel: filter early, shape late

Point-wise removal should happen as far upstream as possible. The reasoning is mechanical: every layer that scores, retrieves, and ranks a candidate we intend to drop is compute and budget spent on nothing. Where we can expose a signal early, we should threshold it early, and we should be willing to have an opinion about the worst of the worst even where content is not policy-violating — if the probability of a bad experience is high enough, or the severity great enough, point-wise removal upstream is correct.

Set-level shaping is the opposite. It belongs late, at blending, because it operates on the assembled slate and nothing earlier in the funnel can see one.

**Filter early, shape late.** These are not competing recommendations about a single lever; they are two different levers with two different units of analysis.

### Axis 2 — Unit of analysis: point-wise or set-level

This is the axis the current proposals do not cover, and it is the one the north-star metric lives on.

At Snap, the suggestive-content problem Michael and I worked on had exactly this shape. One or two bikini pins in a feed is unremarkable. The same pins concentrated together produce a feed that reads as entirely suggestive. No per-item classifier could see it, because no individual item was the problem — the problem was the arrangement. What fixed it was spacing: controlling how much of this class of content can appear in a given window, and how far apart.

The vision doc opens with the same observation in different clothing. The rope pin is safe alone and unsafe in company. **Unsafe Slate Rate is a property of the set, not of any item in it.**

This creates a specific gap. The design-options doc is entirely point-wise: `w_i · BCE(pred_i, label_i)`, per-item utility penalties, per-item quality heads. Each of those is a good mechanism, and within the point-wise column that doc is close to complete. But **a point-wise objective cannot optimize a set-level metric.** We can improve every item in the slate and still serve an unsafe slate, and we can serve a slate of individually-borderline items that no per-item threshold would ever catch.

Spacing, diversity floors, and slate-aware blending are the mechanisms that operate on the right unit. We already have the machinery — the SSD spacing framework, and a P2P spacing launch that removed roughly 32M low-quality impressions with a DAU lift. Pointing it at teen safety is a short path.

### Axis 3 — Functional form: additive, multiplicative, or both

Take `q` as the probability an item is harmful and `E` as its engagement utility. If a harmful impression is worth nothing, expected utility is:

```
E[U]  =  (1 − q) · E   −   q · C
```

Both terms fall out of one expectation, and they answer different questions:

| Term | Form | Question it answers | Owned by |
|---|---|---|---|
| `(1 − q) · E` | multiplicative | Is this engagement legitimate? | the classifier — requires calibrated `q` |
| `− q · C` | additive | What does exposure cost? | policy — `C` is severity |

The two are complements rather than alternatives, which resolves what is usually posed as a choice.

It also identifies where each half is fragile. **The multiplicative term is invariant to engagement-weight inflation; the additive term is not.** In a utility of the form `Σ wₖpₖ − λq`, every launch that raises some `wₖ` dilutes the penalty's share of the budget without anyone touching λ. Additive demotion therefore decays through ordinary good-faith work, and the decay is invisible in attribution because it is spread across many launches rather than concentrated in one. The fix is a maintenance rule: **`C` must be denominated in units of `E` and re-pegged whenever the engagement weights change.**

Worth naming a point of agreement here. The design-options doc's loss reweighting — down-weighting positive-engagement examples on low-quality items — is the same idea as the multiplicative term, applied at training time rather than serving time. Engagement purification and `(1 − q) · E` are one mechanism at two stages. We should say that explicitly rather than treating them as separate proposals.

The choice between forms then follows from Section 1. **Objective harm takes the multiplicative form or a gate, because suppression is unbounded as `q → 1` and we are asserting that no amount of engagement redeems the item. Subjective quality takes the additive form, because additive penalties are always beatable by a high enough `E`, and for taste that is the behavior we want.** If we cannot say which kind a signal is, we cannot say which form to apply.

### Axis 4 — What the signal is about: content or actor

Every signal in the current proposals scores content. Nothing scores the creator, the domain owner, or the board.

At Facebook, the actor layer carried a large share of the integrity stack, for a reason that applies directly here: **content-level enforcement is a treadmill, and actor-level enforcement is a ratchet.** Repeat producers of harm-adjacent content are far more predictable than any individual piece of their content, and acting on the producer generalizes to material we have not classified yet — including material we have not seen.

Faisal's curated-pool proposal is the positive form of the same idea, and his "graduated trust" mechanic is explicitly actor-level. Board-level signals matter too, given that board ideas account for roughly a quarter of unsafe slates. This dimension should be on the map even if we do not build it first.

## 4. Two prerequisites

**Calibration.** Are the classifiers calibrated, and against what — the probability of being bad, or the severity of the badness? These are different objects and they imply different math. The expected-utility derivation above is only valid for a calibrated probability; a severity score implies an additive form scaled by severity; an uncalibrated classifier score with a chosen operating point supports neither, and reduces every λ to a hand-tuned constant. The measurement footnote in the vision doc defines violative as a self-harm score above 0.193, which reads as a precision/recall operating point rather than a probability.

This sharpens rather than contradicts the argument for going continuous. **A threshold only requires the score to be correct at one point. A graded penalty requires it to be correct across the whole range.** Moving from gate to gradient raises the bar on signal quality; it does not lower it. Calibration is therefore the first work item the continuous approach creates, not a detail to settle later.

**Collateral damage.** The design-options doc argues that score-based soft enforcement achieves a better quality-engagement Pareto than filtering. That is very likely right, and a Pareto claim needs both axes measured. We should be measuring engagement loss attributable to *misclassification* — separated from the intended loss on correctly-demoted content — as a standing metric alongside the quality win. Without a cost curve, no one can choose λ; the number is picked rather than derived. This matters more under soft enforcement than under filtering, because a graded penalty touches far more content than a threshold did.

## 5. Relationship to Anticipation

In-session awareness and anticipation are the same machinery aimed at different objectives. Anticipation predicts what a user wants next. Spiral detection predicts what will harm them next. Both are user-state problems rather than content problems: both need a representation of the user's trajectory that persists across surfaces, both are sequence-modeling problems over that trajectory, and both act by changing what gets sourced and how it is arranged rather than by removing individual items.

This is not only a conceptual alignment. The journey risk signal the vision describes — risk concentration, sensitive-topic density, acceleration, cross-surface loops — is a user-state object of exactly the kind the anticipation substrate already produces. Building it as a second head on that substrate rather than as a standalone system is the difference between a teen-safety feature and a capability that any future objective can use, which is the stated ambition.

The surface distribution argues the same way. With roughly 50% of unsafe slates on Related Pins, 25% on Homefeed, and 24% on board ideas, this is not a Homefeed problem with spillover. A problem distributed that way cannot be solved surface-by-surface at the blender; the only lever that reaches all of them at once is the shared user backbone. That is the design-options doc's own Phase 2, and the surface data is an argument for moving it earlier.

## 6. The first bet

**Slate-level spacing for teens on Related Pins, measured against USR.**

Related Pins is the largest share of the problem. Spacing is the only mechanism on the table that operates on the unit USR measures, so it is the only one that can move the metric for the right reason rather than incidentally. The machinery exists and has shipped — the SSD spacing framework, and a P2P spacing launch with a DAU lift. It requires no ranker retraining and no new label pipeline, which means it fits inside a twelve-week window when the modeling work does not.

It is also the fastest way to learn whether USR behaves like a metric we can optimize. If spacing moves USR and topline holds, we have both a win and a validated instrument. If spacing moves USR and topline drops, we have the first real point on the cost curve, which is worth nearly as much.

## Open questions

1. Calibration status of the self-harm and borderline classifiers — probability, severity, or neither.
2. Whether we can stand up a long-running USR holdout, and who owns it.
3. Where the collateral-damage metric lives and who reports it.
4. Whether the actor layer is in scope for this phase or explicitly deferred.
5. Who owns board ideas, currently unassigned and roughly a quarter of the problem.
6. Whether the journey risk signal is built on the anticipation substrate or standalone.
