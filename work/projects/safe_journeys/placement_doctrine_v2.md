# Where Quality and Safety Belong in the Stack

**A placement doctrine for Safe Journeys**

James Li · August 2026 · Draft for comment

> *Draft v2 — Leo-generated from James's dump, 2026-08-14. Supersedes v1. Edit before circulating. Deliberately excluded from this version and kept in `demotion_doctrine.md`: the 7× selection-effect question, advocate framing, and any read on surface politics.*

---

## What this is

Michael's milestones doc asks for "a tech design that is scalable across surfaces and parts of the stack, and surface the tradeoffs." This is the tradeoff half.

It is not a competing design. Content Quality's *Integrating Quality/Safety Objectives into the Recommendation System — Design Options* is a thorough treatment of one region of the space, and most of what follows takes it as given. What this adds is the frame around it: the axes that decide **which mechanism belongs at which layer**, a formulation for the thing we are actually trying to prevent, and the measurement without which none of the parameters can be chosen.

The material comes from having built these systems twice — News Feed Integrity at Facebook, where the demotion stack was the product, and Stories content quality at Snap, where Michael and I shipped the closest analogue to the problem in front of us now.

## 1. Objective quality needs a stated outcome

Demotions and spacing driven by content-quality signals are an *objective* quality intervention. Objective interventions need a stated user outcome to be justified against; without one, every parameter is arbitrary.

For Safe Journeys the outcome is harm prevention: preventing bad experiences that can lead to harm. Every distributional lever should be argued against that.

This is not only a framing preference. As Section 5 shows, the objective/subjective distinction determines the functional form — different classes of signal require different math, and a signal we cannot classify is a signal we cannot correctly apply.

## 2. Engagement and harm prevention converge, with a lag

A recommender exists to produce good experiences, which is to say engagement, retention, and value delivered to users. Harm prevention aims at the same place. Prevent bad experiences and retention should rise.

They are not identical inside a two-week experiment window, and our own history says so: the racy filter cost roughly 4–5% of male impressions, and the vision doc accepts localized SSv2 cost explicitly. The honest statement is that **engagement and harm prevention converge on a longer horizon than the one our experiments measure.**

That has a concrete implication. If the payback period exceeds the test period, the only instrument that can observe it is a **long-running holdout on the safety metric itself.** Michael's doc asks whether we can create and maintain a holdout on USR. That should be the first commitment of the measurement workstream rather than an open question, because without it every safety launch will be judged on the axis where it looks worst.

## 3. All ML makes mistakes. Measuring them is the job.

This is the part I would most like us to over-invest in, because it is the part that decays quietly if nobody owns it.

Every classifier in this program is wrong some of the time, and going from thresholds to graded penalties increases the amount of content our errors touch rather than reducing it. A threshold acted on a small tail. A graded penalty acts on everything. The error surface grows accordingly.

There are three distinct mistakes and they need separate instrumentation:

**Misclassification cost.** Engagement lost because we suppressed content that was fine. This must be separated from the engagement we lost by correctly suppressing content that was not fine — the second is the price of the program, the first is waste. Reporting them as one number makes the program look more expensive than it is and hides whether the classifier is improving.

**Missed harm.** Content that should have been caught and was not, measured at the slate level rather than the item level, since Section 4 is about experiences that no individual item creates.

**Regrettable engagement.** The framing that came up in earlier meetings, and the one I would keep. Not all engagement is good engagement; some of it the user themselves would take back. This is the same idea as collateral damage viewed from the user's side rather than the system's, and it is the concept that makes "we lost engagement" an incomplete sentence. Engagement we should not have had is not a cost.

The design-options doc argues that score-based soft enforcement achieves a better quality-engagement Pareto than filtering. That is very likely right, **and a Pareto claim requires both axes measured.** Without a cost curve, λ is picked rather than derived — by anyone, on any surface, at any layer. Section 6 proposes the instrument that produces the curve.

## 4. What we are actually preventing: a formulation for experience severity

The phenomenon is that an accumulation of low- to moderate-probability bad pins produces a severe experience, while no individual pin in it would trip any threshold. The vision doc's opening image is exactly this: a rope pin is safe alone and unsafe in company.

The obvious formulations do not capture it. Expected count, `S = Σ qᵢ`, says ten pins at q = 0.1 is the same as one pin at q = 1.0. Probability-at-least-one-bad, `S = 1 − Π(1 − qᵢ)`, says the single certain-bad pin is worse, and saturates so that it cannot distinguish twenty bad pins from five. Both treat the slate as independent draws.

The slate is not a bag of independent draws. Its pins are **evidence about the same latent state** — whether this is a self-harm context for this user. Severity should be a function of that posterior, and under conditional independence evidence adds in log-odds:

```
Sₖ  =  Σᵢ [ logit(qᵢ) − logit(πₖ) ]
```

for harm category k with base rate πₖ. Additive in log-odds is multiplicative in odds, which produces the superadditivity we observe. At a 1% base rate, ten pins at q = 0.1 contribute about 2.4 nats each; one pin at q = 0.9 contributes about 6.8. **Ten mildly suspicious pins are stronger evidence than one strongly suspicious pin** — the phenomenon, derived rather than asserted.

This also sharpens the argument for going continuous. Thresholding does not waste signal uniformly. **It destroys precisely the portion of the signal that accumulates.** Content above 0.8 is rare and gets filtered anyway; the mass that composes an unsafe slate is the middle of the distribution, and a threshold sets all of it to zero.

Two corrections the naive form needs:

**Redundancy.** Conditional independence is false — pins in a slate are topically correlated by construction, having come from the same retrieval against the same user embedding. Two near-duplicate depressive quotes are not twice the evidence of one. Discount each contribution by similarity to what has already been counted:

```
Sₖ  =  Σᵢ wᵢ · eᵢ ,     wᵢ decreasing in similarity to already-counted pins
```

That is a submodular set function, the standard structure for slate optimization and tractable greedily at blending time. **It is also spacing, derived.** Spacing stops being a heuristic ("no more than two per twenty") and becomes a budget: a slate may carry at most τ nats of accumulated evidence. Tunable, explainable to policy, and implementable in the blender we already have.

**Category coherence.** Accumulate within category, then combine across, probably by max rather than sum. Ten depressive quotes is a worse experience than five depressive quotes and five weapons pins, because a spiral is coherent. This also keeps the two quantities separate in the way Section 5 requires: `qᵢ` is the classifier's job, `cₖ` — the severity weight of category k — is policy's.

**The temporal case is the same functional at a different window:**

```
S_session(t)  =  Σ_{s ≤ t}  γ^(t−s) · S(slate_s)
```

Accumulated across slates within a session with decay. That is the journey risk signal the vision describes, and "acceleration" is dS/dt. The slate metric and the session metric are one object at two windows, which makes pillars 2 and 3 the same technical program rather than adjacent ones.

**Why this is necessary rather than elegant.** The vision commits models to "learn against Unsafe Slate Rate." We cannot run a GPT-5 judge in a serving path or backpropagate through one. A cheap differentiable surrogate calibrated against USR is therefore the only way that sentence can be made true. `S` is that surrogate: USR is the expensive ground truth, `S` is what we compute and optimize, and calibrating one to the other is a deliverable of the measurement workstream. This makes measurement and modeling mutually dependent rather than sequential.

Known weaknesses, stated up front: conditional independence is still doing work after the redundancy discount, and `πₖ` must be estimated per category and probably per surface. Both are empirical questions.

## 5. Placement axes

### Axis 1 — Where in the funnel: corpus first, then filter early, shape late

Point-wise removal should happen as far upstream as possible, because every layer that scores, retrieves, and ranks a candidate we intend to drop is budget spent on nothing.

The earliest layer is **not L1 utility — it is the corpus.** Inventory selection is where we decide what is eligible to be served at all, and Pinterest already has that layer in pin selection. Starting there means the pool itself is clean of the worst of the worst before any personalization runs. Content with very high report rates belongs in this category: filtered outright, regardless of how engaging it is.

Set-level shaping is the opposite and belongs late, at blending, because it operates on the assembled slate and nothing earlier can see one.

**Corpus first, filter early, shape late.** Three layers, three different jobs.

### Axis 2 — Unit of analysis: point-wise, slate, session

Every mechanism in the current proposals is point-wise: `wᵢ · BCE(predᵢ, labelᵢ)`, per-item utility penalties, per-item quality heads. Each is a good mechanism, and within that column the design-options doc is close to complete. But a point-wise objective cannot optimize a set-level metric. We can improve every item and still serve an unsafe slate.

There are two set-level dimensions, and both are currently unaddressed:

- **Slate (spatial)** — what appears together. This is what USR measures and what spacing controls.
- **Session (temporal)** — what follows what. This is the spiral, and Section 4 shows it is the same functional with a decay.

**Composition applies earlier than the blender.** The strongest objection to acting at L1 is that an engagement-only L2 re-ranks and washes the effect out. That is true of per-item demotion. It is not true of composition control: if a broad swath of a user's candidate pool is harm-adjacent and we reduce that density upstream, no downstream re-ranking resurrects what is not there. Set-level thinking is not confined to blending, and the washout argument is narrower than it has been stated.

### Axis 3 — Mechanism: hard filter, probabilistic sampling, or graded penalty

The program has been framed as gate versus gradient. There is a third option that collapses the choice.

Set `p_keep = 1 − g(q)` and sample. Expected impressions for an item are then proportional to `1 − g(q)` — **which is the multiplicative demotion of Section 5 below, implemented as a gate.** Probabilistic filtering *is* graded demotion in expectation.

That gets us three things at once: full-spectrum use of the classifier, so no score is rounded to zero; the hard-removal property, so nothing downstream can undo it; and graded behavior implemented with binary machinery, which is what corpus selection and retrieval can actually execute.

It is also the instrument Section 3 needs. **A hard threshold gives one point on the cost curve. A sampling rate gives the whole curve.** Sweeping the rate traces the value-versus-harm frontier directly, which is how λ gets derived instead of picked.

Implementation note: hash the draw on (user, item) so it is deterministic per user. Otherwise the same pin appears and vanishes across refreshes.

### Axis 4 — Functional form

Take `q` as the probability an item is harmful and `E` as its engagement utility. If a harmful impression is worth nothing and exposure carries cost `C`:

```
E[U]  =  (1 − q) · E   −   q · C
```

Both terms fall out of one expectation and answer different questions:

| Term | Form | Question | Owned by |
|---|---|---|---|
| `(1 − q) · E` | multiplicative | Is this engagement legitimate? | the classifier — needs calibrated `q` |
| `− q · C` | additive | What does exposure cost? | policy — `C` is severity |

They are complements, not alternatives.

Each half fails differently. **The multiplicative term is invariant to engagement-weight inflation; the additive term is not.** In a utility of the form `Σ wₖpₖ − λq`, every launch that raises some `wₖ` dilutes the penalty's share without anyone touching λ — so additive demotion decays through ordinary good-faith work, and the decay is invisible in attribution because it spreads across many launches. The fix is a maintenance rule: **`C` must be denominated in units of `E` and re-pegged whenever the engagement weights change.**

A point of agreement worth stating explicitly: the design-options doc's loss reweighting — down-weighting positive-engagement examples on low-quality items — is the same idea as the multiplicative term, applied at training time rather than serving time. Engagement purification and `(1 − q) · E` are one mechanism at two stages, and we should treat them as such rather than as separate proposals.

The choice between forms follows from Section 1. **Objective harm takes the multiplicative form or a gate, because suppression is unbounded as `q → 1` and we are asserting that no amount of engagement redeems the item. Subjective quality takes the additive form, because additive penalties are always beatable by a sufficiently high `E`, and for matters of taste that is the behavior we want.**

## 6. Calibration is the prerequisite

Are the classifiers calibrated, and against what — the probability of being bad, or the severity of the badness? These are different objects implying different math. The expected-utility derivation is valid only for a calibrated probability. A severity score implies an additive form scaled by severity. An uncalibrated classifier score with a chosen operating point supports neither and reduces every λ to a hand-tuned constant. The vision doc's footnote defines violative as a self-harm score above 0.193, which reads as a precision/recall operating point rather than a probability.

Section 4 raises the stakes further, since log-odds accumulation requires calibration across the whole range, not just near the cut.

**A threshold requires the score to be correct at one point. A graded penalty requires it to be correct everywhere.** Going continuous raises the bar on signal quality rather than lowering it. Calibration is the first work item the continuous approach creates, not a detail to settle later.

## 7. Relationship to Anticipation

In-session awareness and anticipation are the same machinery aimed at different objectives. Anticipation predicts what a user wants next; spiral detection predicts what will harm them next. Both are user-state problems rather than content problems: both need a representation of the user's trajectory that persists across surfaces, both are sequence-modeling problems over it, and both act by changing what is sourced and how it is arranged rather than by removing individual items.

Three concrete consequences:

**A learned rabbit-hole head, not a rules-based detector.** The vision proposes transparent rules for in-session awareness — repeated unsafe slates, rising density. We can do better with a ranking head built on downstream-reward-term machinery that predicts entry into a bad rabbit hole: the trajectory where a user engages with unsafe content repeatedly and in rapid succession. Its training target is predicted future `S` from Section 4. That is the difference between a safety net that catches spirals and a system that avoids starting them. The dependency is honest and worth naming: it needs trajectory labels, which are scarcer than item labels, and the bootstrap is chaining USR slate judgments into session labels. The modeling work is therefore gated on the measurement workstream, which is an argument for staffing the DS POC first.

**Sequence annotation aimed at the right objective.** Dhruvil has made the point that we can annotate the user sequence in the recommendation models with these signal scores and use it for various objectives. The mechanism is right. Pointed at engagement objectives it is a modest feature; pointed at the rabbit-hole objective above it is the natural input, since the annotated sequence *is* the trajectory whose severity we are trying to predict.

**In-session responsiveness already exists.** JJ led that work in our org. If a user is engaging rapidly with harm-adjacent content, responsiveness within the same session — or at minimum the next — is the intervention, and the machinery is built. How to act deserves design work; whether we have the capability does not.

The surface distribution argues the same direction. With roughly 50% of unsafe slates on Related Pins, 25% on Homefeed, and 24% on board ideas, this is not a Homefeed problem with spillover. A problem distributed that way cannot be solved surface-by-surface at the blender, and the only lever reaching all of them at once is the shared user backbone — the design-options doc's own Phase 2. The surface data is an argument for moving it earlier.

## 8. First bets

**1. Slate-level spacing for teens on Related Pins, measured against USR.** Related Pins is the largest share of the problem. Spacing operates on the unit USR measures, so it is the only proposal that can move the metric for the right reason. The machinery has shipped — the SSD spacing framework and a P2P spacing launch with a DAU lift. No ranker retraining, no new label pipeline, fits inside twelve weeks. If spacing moves USR and topline holds, we have a win and a validated instrument. If it moves USR and topline drops, we have the first real point on the cost curve, which is worth nearly as much.

**2. Probabilistic corpus filtering for teens, swept across sampling rates.** Cheap, upstream, immune to downstream washout, and it produces the value-versus-harm curve that Section 3 says every other decision depends on.

**3. Scope the `S` surrogate and its calibration against USR.** Everything in Section 4 and the rabbit-hole head in Section 7 depends on it, and nothing else on the roadmap produces it.

## Open questions

1. Calibration status of the self-harm and borderline classifiers — probability, severity, or neither.
2. Whether we can stand up a long-running USR holdout, and who owns it.
3. Where the collateral-damage and regrettable-engagement metrics live, and who reports them.
4. Base rates `πₖ` per category and surface — measured or assumed.
5. Who owns board ideas, currently unassigned and roughly a quarter of the problem.
6. Whether the journey risk signal is built on the anticipation substrate or standalone.
