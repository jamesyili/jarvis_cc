# Where Quality and Safety Belong in the Stack

**A placement doctrine for Safe Journeys**

James Li · August 2026 · Draft for comment

> *Draft v5 — Leo, 2026-08-14. **NOT circulation-safe:** §7 and the flagged blockquotes inside §3 and §5.4 are internal. Cut before sharing. `demotion_doctrine.md` retained on disk as the original thinking file.*

Michael's milestones doc asks for a tech design scalable across surfaces, with the tradeoffs surfaced. This is that. It is not a competing design — Content Quality's *Design Options* doc is a thorough treatment of one region of the space and most of what follows takes it as given.

The material comes from building these systems twice: News Feed Integrity at Facebook, where the demotion stack was the product, and Stories content quality at Snap, where Michael and I shipped the closest analogue to the problem in front of us.

---

## 1. Definitions

Most disagreements in this program so far have been vocabulary disagreements wearing technical clothes. This section is the shared vocabulary; everything after it is built on these terms.

**Harm-adjacent (borderline)** — content that is not violating on its own, but raises the probability or severity of a harmful experience through accumulation or through the engagement it invites. Racy as adult-adjacent, depressive as self-harm-adjacent. This is the scope of the program.

### 1.1 The layers

| Layer | What it decides | Granularity available |
|---|---|---|
| **Corpus / inventory** (pin selection) | What is eligible to be served at all | Binary keep/drop; content-level |
| **Retrieval / candidate generation** | What is sourced for this user | Set composition; user-conditioned |
| **L1 / light ranking** | Cheap scoring over a large candidate set | Image-level features today; sees the whole candidate set |
| **L2 / full ranker** | Final ordering | Rich features, full candidate context |
| **Blender** | Slate assembly | The only layer that can see an assembled slate |

Orthogonal to layer: an intervention acts at **serving time** (changes what is shown now) or **training time** (changes what the model learns).

### 1.2 The units of analysis

The unit matters because **a metric defined on one unit cannot be optimized by a mechanism defined on another.** Each unit has its own mechanisms and its own layer:

| Unit | What it is | Mechanisms that operate on it | Where |
|---|---|---|---|
| **Item** | One pin | Filter, demotion, probabilistic sampling | Corpus → L2 |
| **Slate** | The set shown together | Diversity, density control, spacing | L1 (candidate set), blender (final slate) |
| **Session** | The sequence of slates over time | Responsiveness, re-seeding, journey risk signal | Cross-surface, cross-request |

**On whether session earns its place.** It does, on the test of whether it changes what we build. The slate mechanisms are all *compositional* — they act on a set that exists right now, inside one request. The session mechanisms are *reactive* — they require carrying state between requests and across surfaces, which is a different system with different latency and different ownership. Pillar 3 of the vision is entirely session-unit, the 7× spiral statistic is a session-unit observation, and the trajectory head in §5.2 predicts a session-unit outcome. If we collapse session into slate we lose the distinction between "this screen is bad" and "this user's trajectory is bad," and the second is the one the program was named after.

### 1.3 The mechanisms

**Item-unit:**
- **Filter / gate** — binary removal of a single pin at a threshold on one or more signals (§4.2).
- **Demotion** — reduce a single pin's ranking score. Additive or multiplicative (§4.5).
- **Probabilistic sampling** — stochastic removal of a single pin, keep-probability a function of its score (§4.4).

**Slate-unit.** Three distinct mechanisms, and the distinction between them is load-bearing:

- **Spacing** — separate flagged items so they do not cluster. **Threshold-dependent**: something must first be declared bad before it can be spaced from other bad things.
- **Diversity (SSD)** — a modified Gram-Schmidt decorrelation over the set, already implemented today. **Threshold-free**: it consumes the *entire* classifier prediction vector and diversifies against it, with no prior determination that any individual pin is unsafe.
- **Density control (L1 composition)** — cap how much of a candidate set falls within a given classifier-score range. **Threshold-free**: it needs a score, not a verdict. Concretely: take the pins whose classifier scores fall in a band and hold that population to a fixed budget.

**We prefer diversity and density control over spacing.** Spacing reintroduces the threshold at the set level, which throws away the same information Faisal's argument says we should stop throwing away. Diversity and density control consume the full score distribution, which means the choice of set-level mechanism follows from the same principle as the choice of item-level mechanism.

**Session-unit:**
- **Responsiveness** — change behavior within or across sessions in reaction to observed trajectory.
- **Re-seeding** — fall back to declared interests or safe candidate sources.

**Training-time (any unit):**
- **Loss reweighting** — change training-example weights.
- **Objective / head** — add a predicted target to the model.

### 1.4 The quantities

| Symbol | Meaning | Owned by |
|---|---|---|
| `q` | Score for a single item. Ideally `P(harm-adjacent in category k)` | the classifier |
| `πₖ` | Base rate of category k | measurement |
| `cₖ`, `C` | Severity weight of category k | **policy**, not the classifier |
| `h` | **Realized harm** — impression-normalized report / hide / See-Less rate for an item | measurement |
| `E` | Engagement utility of an item | ranking |
| `λ` | Demotion strength | derived from the cost curve (§3) |
| `ρ(band)` | **Density** — share of a candidate set whose scores fall in a given band | the density-control lever |

`ρ` is the set-level quantity this doctrine actually runs on. It needs no verdict about any individual pin — only a score and a band.

### 1.5 The metrics

- **Prevalence** — share of impressions that are violative. *Average exposure, item unit.* ~0.03% for self-harm.
- **User reach** — count of users seeing ≥1 violative item.
- **Density** — share of an individual's feed that is borderline or violative.
- **Unsafe Slate Rate (USR)** — share of slates an LLM judge rates unsafe. *Slate unit.* North star. 0.45% for teens, ~300× prevalence.
- **Collateral damage** — engagement lost to *misclassification*, held separate from engagement lost to correct suppression.
- **Regrettable engagement** — engagement the user themselves would take back.

### 1.6 Calibration states

- **Probability-calibrated** — the score equals `P(harmful)`. Required by §4.5 and by any band-based density control.
- **Severity-calibrated** — the score is ordinal in harm magnitude.
- **Operating-point score** — neither; trustworthy only near a chosen cut. **This appears to be what we have.**

---

## 2. Ask 1 — Calibrate the classifiers

### Why this comes first

Everything downstream of a threshold is a policy question. Everything downstream of a *graded* signal is a math question, and the math is only valid if the number means what it claims to mean.

**A threshold requires the score to be correct at one point. A graded penalty requires it to be correct everywhere.** Moving from gate to gradient does not reduce our dependence on signal quality — it raises the bar across the entire range. That is the work item the continuous approach creates, and it is currently unowned.

Three specific things break without it:

1. **The expected-utility form (§4.5) is invalid.** `(1 − q) · E` is only "discount engagement by the probability it is illegitimate" if `q` is that probability. Otherwise it is an arbitrary rescaling.
2. **Band-based density control breaks worse.** Capping the mass of a candidate set inside a score band assumes the band *means* something — that "0.3 to 0.5" is a real region of risk rather than an artifact of where the model happened to put its scores. Miscalibration in the middle of the range is exactly where this bites, and the middle is where the accumulating mass lives. Enforcement never cared about it because enforcement only ever looked at the tail.
3. **λ cannot be transferred.** A λ tuned on one surface means nothing on another if the score distributions differ, which is why per-surface λ tuning currently feels like hand-fitting. It is.

The evidence that we are in the third state of §1.6: the vision doc defines violative as a self-harm score **above 0.193**. A 0.193 cut is a precision/recall operating point, not a probability.

**This also strengthens rather than challenges Faisal's argument.** His "filter-thresholding uses under 20% of the signal's strength" is right, and it *depends on calibration* — using the full spectrum requires the full spectrum to be meaningful. Otherwise we are not recovering 80% of the information, we are amplifying 80% of the noise.

### How to do it

**Isotonic regression against human labels** is the right default. It is monotone and non-parametric, so it corrects arbitrary miscalibration shapes without assuming the distortion is a sigmoid. Platt scaling (a logistic fit) is the cheaper alternative when the label budget is small, but it imposes a shape we have no reason to believe.

The design decisions that matter more than the estimator choice:

- **Stratify the label sample by score band, then reweight.** Uniform sampling is useless here — at a 0.03% base rate, a random sample yields almost no labels above the middle of the range. Draw equal counts per band and correct with sampling weights. This is also the fix for the fact that nobody currently labels the middle: enforcement only ever cared about the tail, so the region that matters most for accumulation is the region with the least ground truth.
- **Calibrate per category and per surface.** `πₖ` differs by category, and score distributions differ by surface. One global calibration map will be wrong everywhere in a different direction.
- **Report reliability diagrams and expected calibration error per band, not aggregate.** Aggregate ECE is dominated by the enormous mass near zero and will look excellent while the operating region is badly wrong.
- **Re-calibrate on a schedule.** Classifier retrains silently break calibration; a calibration map is a versioned artifact with an owner, not a one-time exercise.
- **Keep `q` and `cₖ` separate.** Calibration produces `q` — a probability. Severity `cₖ` is elicited from **policy**, through a rubric or pairwise comparisons, not read off a classifier. Conflating them is how "severity" quietly becomes "whatever the model was confident about."

**The LLM judge needs the same treatment.** Their own footnote says "LLM judge results not human calibrated." USR is the north star; an uncalibrated north star is a heading, not a position. The same protocol applies — a stratified human-labeled slate sample, agreement reported as Cohen's κ rather than raw accuracy, and a calibration pass on the judge's own scores. This is a prerequisite for the USR holdout in §3, since a drifting judge and a real effect are indistinguishable without it.

**Then distill it.** A calibrated judge is a measurement instrument, not a serving component — we cannot run GPT-5 in a ranking path or backpropagate through it. The way USR becomes something models can actually learn against is to **train a small model to predict the judge's slate-level label**, and use that as the optimization target and the online metric. This is the concrete answer to the vision's commitment that "models will learn against Unsafe Slate Rate," and it is why calibrating the judge is upstream of everything: a distilled model inherits whatever bias its teacher has. Judge → calibrate → distill → optimize.

---

## 3. Ask 2 — Measure the mistakes

### Why

All ML makes mistakes. Every classifier in this program is wrong some of the time, and **moving from thresholds to graded penalties increases the amount of content our errors touch.** A threshold acted on a small tail; a graded penalty acts on everything. The error surface grows precisely as we adopt the approach the program is built on.

This is also the part that decays quietly if nobody owns it, because the mistakes are invisible by construction: suppressed content generates no engagement to miss.

Three distinct mistakes, each needing separate instrumentation:

**Misclassification cost.** Engagement lost because we suppressed content that was fine. This must be held separate from engagement lost by correctly suppressing content that was not fine — **the second is the price of the program, the first is waste.** Reported as one number, it makes the program look more expensive than it is and hides whether the classifier is improving. Every classifier improvement should show up as this number falling while the quality win holds.

**Missed harm.** Content that should have been caught and was not — measured at the **slate** level rather than the item level, because the experiences we care about are ones no individual item creates. Their own numbers already establish this: prevalence is 0.03% while USR is 0.45%, a 300× gap. **That gap is the accumulation effect, already measured** — most unsafe experiences are not a single enforcement miss but a composition our item-level instruments cannot see.

**Regrettable engagement.** Not all engagement is good engagement; some of it the user themselves would take back. This is collateral damage viewed from the user's side rather than the system's, and it is what makes "we lost engagement" an incomplete sentence. **Engagement we should not have had is not a cost.**

**On the Pareto claim.** The Design Options doc argues that score-based soft enforcement achieves a better quality-engagement Pareto than filtering. That is very likely right — **and a Pareto claim requires both axes measured.** Without a cost curve, λ is picked rather than derived, by anyone, at any layer, on any surface.

### How to do it

**The instrument is a hold-back inside the suppressed set.** Let a small random fraction ε of the items we would have suppressed through anyway, and measure both their realized engagement and their realized harm. This gives both axes on the *same* population, which no other design does — comparing suppressed content to general corpus content compares different distributions and answers a different question.

This is the same mechanism as probabilistic sampling (§4.4), which is the point: **a hard threshold gives one point on the cost curve; a sampling rate gives the whole curve.** The measurement apparatus and the enforcement mechanism are the same object operated at different rates. Build it once.

Concretely:

- **Sample from what the system actually suppressed**, stratified by score band, and human-label it. That yields a false-positive rate per band, which is the missing input to λ.
- **Multiply FP rate by forgone engagement** on the held-back items to get misclassification cost in engagement units — the same units the other axis is reported in.
- **For regrettable engagement**, start with behavioral proxies: hides, reports, See Less, session abandonment following the impression, and next-session return rate. Then validate the proxy against survey ground truth on a sample, and model it. The proxy alone will be biased toward users who bother to signal.
- **Governance rule: both axes on the same slide, always.** A quality win reported without its cost is not a result. This is cheap to enforce and it is the thing that prevents the metric from drifting once the program has attention.

### The holdout, and why the horizon argument matters

A recommender exists to produce good experiences; harm prevention aims at the same place. But they are not identical inside a two-week window, and our own record says so — the racy filter cost ~4–5% of male impressions, and the vision doc accepts localized SSv2 cost explicitly.

The honest statement is that **engagement and harm prevention converge on a longer horizon than our experiments measure.** If the payback period exceeds the test period, the only instrument that can observe it is a **long-running holdout on the safety metric itself.** Michael's doc asks whether we can create and maintain a USR holdout; that should be the measurement workstream's first commitment rather than an open question, because without it every safety launch will be judged on the axis where it looks worst, in the window where it looks worst.

> *[Internal — cut before circulating] Dylan asked James to hold CQ accountable and used similar language in the joint sync, so the accountability framing is sponsor-directed. Delivery still has to land as shared infrastructure rather than policing: use their own word — they invoked a Pareto, and a Pareto has two axes.*

---

## 4. Designing an intervention: five choices

### 4.1 Act early — corpus, retrieval and L1 are all early funnel

Point-wise removal belongs as far upstream as possible, because every layer that scores, retrieves, and ranks a candidate we intend to drop is budget spent on nothing.

**The early funnel is three layers, not one**, and all three are in scope before anyone touches the blender:

- **Corpus / inventory selection** — the earliest, and the one currently underused.
- **Retrieval / candidate generation** — what gets sourced for this user at all.
- **L1 utility** — the first place a score shapes ordering, and the first place the whole candidate set is visible.

**Start with the corpus pipeline.** Inventory selection today runs as a **daily batch data pipeline**, and that is the best available place to begin adding trust-and-safety and content-quality signals. The properties are unusually favourable: no serving latency budget to respect, no ranking experiment to destabilize, changes are auditable and reversible by rerunning the job, and — the important one — **a batch pipeline can join against signals that are not computable online.** Aggregated report and hide rates over a trailing window, cross-day accumulations, and expensive classifiers all live naturally in a daily job and nowhere else. That is precisely where the realized-harm dimension of §4.2 has to be computed.

Starting there means the pool is clean of the worst of the worst before any personalization runs, and it costs the serving path nothing.

Set-level shaping is the opposite and belongs late. **Composition control belongs at L1, where the whole candidate set is visible; diversity belongs at the blender, where the assembled slate is.**

**Corpus first, filter early, shape late.**

### 4.2 Act on more than the classifier score

Removal should not be a function of the classifier score alone. A single model output carries one kind of information, and the decision to take content out of the corpus entirely deserves more than one kind.

Three independent dimensions, each from a different source and owned by a different party:

| Dimension | The question it answers | Source | Owner |
|---|---|---|---|
| **`q`** — classifier score | How likely is this content bad? | the model's belief about the content | the classifier |
| **`h`** — realized harm | How much damage has it already done? | observed user response: reports, hides, See Less | measurement |
| **`cₖ`** — category severity | How bad is this *kind* of harm if it is real? | policy assertion | **policy** |

None of the three is derivable from the others. A confidently-scored pin may have caused no observed harm because it has barely been distributed. A weakly-scored pin may be generating reports at ten times the normal rate. And a moderate probability of self-harm content is not the same decision as a moderate probability of gross content, no matter what either classifier says.

**Combine them as independent triggers, not as a weighted average.** This is the load-bearing point. If the three are blended into a single score, a strong signal on one dimension gets outvoted by weak signals on the other two — which is the same washout failure we identify between L1 and L2, one level down. Concretely, removal should fire if *any* of the following holds:

- `q` is above the confident-bad threshold for the category, **or**
- `h` is extreme — impression-normalized report or hide rate far above baseline — **regardless of what the classifier says**, **or**
- `cₖ` is at the highest severity tier *and* `q` is moderate rather than high.

The second clause matters most and is the cheapest to ship. **Content with a very high report rate should come out of the corpus no matter how engaging it is and no matter what the model believes**, because the users have already told us. Two implementation notes: normalize by impressions rather than using raw counts, since raw report counts mostly measure reach; and guard against brigading with a floor on distinct reporters and some rate-limiting per reporter.

Read another way, `h` is a second and largely independent read on the same question the classifier is answering — the classifier looks at the content, users look at the experience. Where the two agree, confidence is much higher than either alone. Where they disagree, that is the highest-value labeling queue we have, and it should feed the calibration work in §2 directly.

### 4.3 Match the mechanism to the unit

Every mechanism in the current proposals is point-wise: `wᵢ · BCE(predᵢ, labelᵢ)`, per-item utility penalties, per-item quality heads. Each is good, and within that column the Design Options doc is close to complete. But a point-wise objective cannot optimize a set-level metric. **We can improve every item and still serve an unsafe slate.**

**Composition applies earlier than the blender.** The strongest objection to acting at L1 is that an engagement-only L2 re-ranks and washes the effect out. That is true of per-item demotion. It is **not** true of composition control: if a broad swath of a user's candidate pool is harm-adjacent and we cap that density upstream, no downstream re-ranking resurrects what is not there. Set-level thinking is not confined to blending, and the washout argument is narrower than it has been stated.

### 4.4 Remove, sample, or penalize

The program has been framed as gate versus gradient. A third option collapses the choice.

Set `p_keep = 1 − g(q)` and sample. Expected impressions are then proportional to `1 − g(q)` — **which is the multiplicative demotion of §4.5, implemented as a gate.** Probabilistic filtering *is* graded demotion in expectation.

Three things at once: full-spectrum use of the classifier, so no score is rounded to zero; the hard-removal property, so nothing downstream can undo it; and graded behavior implemented with binary machinery, which is what corpus selection and retrieval can actually execute. Plus the cost curve of §3.

*Implementation note:* hash the draw on (user, item) so it is deterministic per user. Otherwise the same pin appears and vanishes across refreshes.

### 4.5 How the penalty meets engagement

Take `q` as `P(harmful)` and `E` as engagement utility. If a harmful impression is worth nothing and exposure carries cost `C`:

```
E[U]  =  (1 − q) · E   −   q · C
```

| Term | Form | Question | Owned by |
|---|---|---|---|
| `(1 − q) · E` | multiplicative | Is this engagement legitimate? | the classifier — needs calibrated `q` |
| `− q · C` | additive | What does exposure cost? | policy — `C` is severity |

They are complements, not alternatives. This reframes the usual argument from *safety team versus engagement team* into *what does your score actually mean*.

**Each half fails differently.** The multiplicative term is invariant to engagement-weight inflation; the additive term is not. In a utility of the form `Σ wₖpₖ − λq`, every launch that raises some `wₖ` dilutes the penalty's share without anyone touching λ. **Additive demotion therefore decays through ordinary good-faith work, and the decay is invisible in attribution**, spreading across many launches rather than concentrating in one. No bad actor is required. The fix is a maintenance rule: **`C` must be denominated in units of `E` and re-pegged whenever the engagement weights change.**

Two notes on the older framing. Additive's claimed advantage — that it decomposes quality from engagement — holds only in linear space; multiplicative decomposes just as cleanly in log space (`log U = log E + log(1 − λq)`). And the Design Options doc's loss reweighting is **the same idea as the multiplicative term, applied at training time rather than serving time.** Engagement purification and `(1 − q) · E` are one mechanism at two stages.

**Choosing between them.** Where we are asserting that no amount of engagement redeems an item, the multiplicative form or a gate is correct, because suppression is unbounded as `q → 1`. Where we are asserting a tradeoff that sufficiently good content is allowed to win, the additive form is correct, because additive penalties are always beatable by a high enough `E`. The choice is a policy statement, and it should be made explicitly per signal rather than inherited from whichever mechanism was easiest to ship.

---

## 5. Preventing rabbit holes

The program's own framing for this is *"catch a spiral before it becomes a destination."* The thing being prevented is a **trajectory**, not an impression. Everything in this section follows from taking that literally.

### 5.1 A journey problem, not a surface problem

The surface distribution settles this on its own. Roughly **50% of unsafe slates are on Related Pins, 25% on Homefeed, and 24% on board ideas.** This is not a Homefeed problem with spillover; Homefeed is the minority case.

The mechanism behind that split is worth naming, because it tells us where to look. **The closeup → Related Pins loop is the tightest feedback loop in the product.** A single tap returns an immediate slate of near-neighbours of the thing just engaged with — on that surface, similarity *is* the product. Any system that reads engagement as intent will read one ambiguous tap as a request for more of the same, and Related Pins is where that reading gets acted on fastest and most literally. A 50% share is what we should expect, not a surprise.

Real sessions cross surfaces continuously: a notification pulls the user in, a closeup leads to Related Pins, a search leads to more closeups, and Homefeed absorbs whatever the other three taught the system. **If each surface implements its own quality logic, three things break.** The user's trajectory is invisible to every one of them, because each sees only its own slice. Suppression on one surface is quietly undone by another that never heard about it. And USR cannot be compared across surfaces, because each surface is measuring against its own definition.

The vision already asks for the right behavior — "stop reintroducing the pattern on another surface," "cross-surface loops" — but nothing in the current design makes that possible. Being able to honor it is a structural property, not a feature.

**What has to be shared, and what may vary.** The distinction is the whole design:

| Shared across surfaces | May be tuned per surface |
|---|---|
| Signal definitions and their calibration maps | Penalty strength λ |
| Severity weights `cₖ` (policy, not per-team) | Band cutoffs for density control |
| The journey-risk state object | Which mechanisms exist at all — there is a blender on Homefeed, none on notifications |
| The judge and its distilled model | Latency budget |
| Metric definitions | Rollout sequencing |

Per-surface *strength* is legitimate and expected. Per-surface *definitions* are how a program like this fails quietly: the same pin gets three different verdicts, and nobody can tell whether the metric moved because the system improved or because a threshold drifted somewhere upstream.

**Notifications deserve specific attention** and are usually left out of quality conversations because they are not a feed. They should not be. Notifications are the only surface where **we** initiate contact — a notification that re-enters a harm-adjacent context restarts a spiral that had already ended on its own. They are also the cheapest place to apply journey risk: it is a send / do-not-send decision with a long latency budget and no ranking pipeline to destabilize.

This is also the direct answer to the question asked of the vision doc — Homefeed only, or all surfaces. All of them, and the only lever that reaches all of them at once is the shared user backbone, which is the Design Options doc's own Phase 2. **The surface data is an argument for moving that phase earlier.**

### 5.2 Training the ranker on the right objective

Faisal has already made the core argument, and it is the strongest one in the program:

> "Today, safety lives outside the ranker — candidates are scored for engagement, ranked, and then filtered by T&S signals at the end of the pipeline. **The model itself has no incentive to prefer safe content; it just gets told 'no' after the fact on a subset of items.**"

And, on the same point from the other side:

> Recommenders are **"quality-unaware at training time,"** producing **"lopsided train-vs-inference incentives"** — safety **"must be inbuilt, not band-aided."**

This is correct, and CQ's doc independently reaches the same diagnosis: an engagement-only ranker is structurally biased because negative feedback is sparse and low-quality content still earns long clicks, so the model learns to amplify it. There is no disagreement to resolve here. The question is only *which* objective gets inbuilt.

**Every proposal on the table is per-item** — a quality head, or reweighting of individual training examples. That corrects the item-level bias, and it should be done. But it does not correct the trajectory, because no per-item objective contains the concept of one.

**The objective that matches the harm is a trajectory objective.** Not "is this pin harm-adjacent" — the classifier already answers that, and answers it better than a ranking head will. The question nothing currently answers is: *does showing this item, to this user, in this state, make the next ten minutes worse?*

Concretely, a head on downstream-reward-term machinery predicting the judged unsafe-slate outcome over a forward window. We already have machinery for delayed and downstream targets; this is a new target for it, not a new system. And Faisal's own gradient-not-gate argument applies here with more force than anywhere else: **imperfect signals are perfectly adequate as trajectory supervision, because errors average out over a window in a way they never do on a single item.**

Two things fold into this cleanly:

**Decoupled engagement weights.** Faisal: *"a click/repin from a teen on borderline content shouldn't carry the same training weight as a click from an adult on benign content."* That is loss reweighting, and it is **the training-time twin of the `(1 − q) · E` term in §4.5** — the same statement, once about what we serve and once about what we learn. Worth saying explicitly, because CQ's doc proposes the training-time half and this doctrine proposes the serving-time half, and they have been read as competing when they are the same idea at two stages.

**Sequence annotation.** Dhruvil has made the point that we can annotate the user sequence in the recommendation models with these signal scores and use it for various objectives. The mechanism is right. Pointed at engagement objectives it is a modest feature; pointed at the trajectory objective above it is the natural input, since **the annotated sequence *is* the trajectory whose risk we are trying to predict.**

**Why L2.** Final ordering is decided there, the features are richest, and — the reason that actually matters — the user sequence is available there. A trajectory objective needs trajectory context, and L1 does not have it. On this specific point CQ's preference for L2 is right, and we should say so plainly.

**The honest dependency:** trajectory labels are scarcer than item labels. The bootstrap is chaining the distilled judge's slate labels into session-level labels, which makes this work downstream of §2 and §3 and is another reason the measurement DS role should be staffed before the modeling starts.

### 5.3 In-session responsiveness

JJ led in-session responsiveness in our org, so the capability question is settled. **What is missing is the trigger and the policy, not the machinery.**

The trigger is journey risk crossing a threshold — concentration, density, acceleration, and recurrence of a sensitive topic across surfaces. The response levers are already named in the vision: raise the safety weight in ranking, tighten diversity and density, stop reintroducing the pattern on other surfaces, re-seed from declared interests.

Four design questions deserve real thought before anything ships:

**Latency.** Within-session response requires real-time state and is the expensive version. Next-session response is dramatically cheaper and may capture most of the value, since spirals that matter tend to persist across sessions. Start with next-session, measure the gap to within-session, and let that number justify the cost rather than assuming it.

**Hysteresis.** Entry and exit need different thresholds. With one threshold the system flaps, and the user experiences a feed that lurches between two personalities — which is worse than either state.

**Exit criteria.** How does a user leave the protected state? Time decay, or observed healthy engagement, or both. Getting this wrong produces the permanent walled garden the vision explicitly rejects, and it produces it silently, because nobody instruments the users who never got out.

**Invisible before visible.** The vision's standard is to *"restore agency, not punish curiosity."* Ranking-side responses are invisible to the user and carry no risk of shaming someone for what they searched. UX interventions are visible and carry that risk directly. Sequence accordingly: ranking-side first, measure, then decide whether a visible treatment adds anything the invisible one did not.

The rules-based version described in the vision is a good V1 and a poor V2. The strong version conditions responsiveness on the trajectory head from §5.2 rather than on hand-set rules — same intervention, learned trigger.

### 5.4 The same machinery as Anticipation

In-session awareness and anticipation are the same machinery aimed at different objectives. Anticipation predicts what a user wants next; spiral detection predicts what will harm them next. Both are user-state problems rather than content problems: both need a representation of the user's trajectory that persists across surfaces, both are sequence-modeling problems over that representation, and both act by changing what gets sourced and how it is arranged rather than by removing individual items.

The journey-risk signal §5.3 needs is a user-state object of exactly the kind the anticipation substrate already produces. Building it as a second head on that substrate, rather than as a standalone safety system, is the difference between a teen-safety feature and a capability any future objective can use — which is the stated ambition: build the muscle so that **any** business objective, whether quality, safety, or credibility, can be added to the stack.

> *[Internal — cut before circulating] Matt Madrigal commented "Let's tie this back to Anticipation as well" on the In-Session Awareness section, 8/12. Whoever writes this section owns the connection; Andrew Y co-authored both the Anticipation Vision and this doc and can write it just as easily.*

---

## 6. Open questions

1. Calibration status of the self-harm and borderline classifiers — probability, severity, or neither.
2. Whether we can stand up a long-running USR holdout, and who owns it.
3. Where the collateral-damage and regrettable-engagement metrics live, and who reports them.
4. Base rates `πₖ` per category and surface — measured or assumed.
5. Who owns board ideas, currently unassigned and roughly a quarter of the problem.
6. Whether the journey risk signal is built on the anticipation substrate or standalone.

---

## 7. Internal notes — NOT FOR CIRCULATION

*James only. Delete before the doc leaves his hands.*

**The 7× number is a selection effect.** "After a teen taps one unsafe slate, their USR rises 7× (0.45% → 3.2%)" conditions on a tap. Teens who tap an unsafe slate are different teens; this is selection, not causation. Combined with an uncalibrated GPT-5 judge at n = 2K and no holdout, it is a credibility risk under the whole program if the CTO mandate rests on it. **Michael conversation, one-on-one — not a joint-room conversation.**

**The L1-vs-L2 fight is the wrong fight.** CQ's doc argues "CQ's preference is L2," demoting L1 Utility — James's system — to an optional density lever, while its Phase 2 puts the quality objective into the CFM/UPP backbone, also James's, on CQ's sequencing. Net: enforcement moves out of James's L1 and into James's UPP with CQ holding the definition and timeline. **But L1-vs-L2 is a fight over Homefeed, which is 25% of the problem.** The available position is not "L1 not L2" — it is that the metric is slate-level, the problem is cross-surface, and both point at the shared backbone. That is Faisal's thesis, the CTO's question, and James's platform converging.

**Qinglong.** Offer co-authorship on Monday. Converts a potential rebuttal into a joint artifact and does the cordiality repair in the same move; James stays first author. Concede the corpus layer generously — pin selection is correctly placed, it needs a teen threshold policy, not relocation. Hand him the agreement in §4.5 (his loss reweighting = the multiplicative term at training time) explicitly.

**Unclaimed ground.** Safe Cold Start Eng POC = TBD, and new-user enablement is already James's charter. Measurement DS POC = TBD. Board ideas (24%) unowned. Claiming an unowned workstream that is already his by right costs nothing politically; fighting over L1 costs a lot.

**Scope discipline.** Write the doc, do not run the program. Do not accept "a tech design scalable across surfaces and parts of the stack" as a personal deliverable — that is multi-week work wearing a bullet point. JJ writes the L1 experiment plan underneath this doctrine.

**Still missing from James's dump** (needed to make §1.3 and §4.2 land with Michael): the Snap suggestive-content case in detail — numbers, mechanism name, actual spacing window. Also: measurement under headline pressure, the curated-corpus experience, and what he would never do again.
