# Demotion Doctrine — the why, the math, and what it implies for Safe Journeys

> **James Li, drafted with Leo 2026-08-14.** Working doctrine memo for the Safe Journeys program (teen safety / self-harm spirals). Source of the argument: James's Facebook News Feed Integrity work (2015–2021: clickbait, actor quality, distributional incentives, sentiment/human values) and Snap (Content Understanding EM → Head of Stories Ranking, incl. the suggestive-content work with Michael Weissinger).
>
> **Mandate note:** Dylan asked James to hold Content Quality accountable, and used similar language in the joint sync. The accountability framing below is sponsor-directed, not freelanced — but *delivery* still has to land as shared infrastructure rather than policing.
>
> Companion sources: `sources/01_vision_acp_safe_journeys.md` (Faisal/Michael vision + CTO comments) · `sources/02_teen_aware_experience_faisal.md` · `sources/03_milestones_timeline_2026-08-14.md` (the execution doc asking James for ETAs) · `sources/04_cq_design_options_qinglong.md` (CQ's design-options doc).

---

## 1. Start with the why: objective vs. subjective content quality

Demotions and spacing driven by content-quality signals are an **objective** content-quality intervention, not a subjective one. Objective interventions require a stated **why**: *what user outcome are we trying to produce?*

For teen safety the answer is **harm prevention** — preventing bad experiences that can lead to harm. That is the right framing, and it is the thing every distributional measure should be justified against.

This matters because it determines everything downstream, including the math (§6). **If you cannot say whether a signal is objective or subjective, you cannot say what functional form to apply to it.**

## 2. The recommender and the safety system are aiming at the same thing — with a lag

A recommendation system exists to increase good experiences: engagement, therefore retention, therefore utility and value to users. Harm prevention aims at the same place. Prevent bad experiences and retention should go **up**. These are not fundamentally different objectives in their ultimate outcome.

**But do not claim they are identical, because the docs on the table already concede otherwise:**
- The racy filter cost **~4–5% male impressions** (CQ's own number, `04_`).
- Faisal wrote: *"drive it down, even with localized SSv2 cost. This is the engagement we do not need on Pinterest."*

If the claim is stated as identity, someone produces the 4–5% and the argument is over. The defensible version:

> **Engagement and harm prevention converge on a long enough horizon. The entire measurement problem is that our experiment windows are shorter than the horizon on which harm prevention pays back.**

That reframe does real work: it makes **holdouts** the answer rather than a nice-to-have. Michael's execution doc already asks *"Can we create and maintain a holdout using this new metric?"* and does not answer it. That question is the load-bearing one, and it is the natural place to plant a flag.

## 3. Collateral damage is not an accusation — it is the second axis of a Pareto claim

CQ's own doc claims that *"score-based soft enforcement achieves a better quality↔engagement **Pareto** across Notif/HF/Search."*

**A Pareto claim requires both axes measured.** So the ask is not "prove you're not hurting engagement" — it is "you invoked a frontier; show the frontier." Concretely:

- Measure the **engagement loss attributable to misclassification** — the collateral damage from imperfect classifiers, separated from the intended loss from correctly-demoted content.
- Without a cost curve, **nobody can choose λ.** Not CQ, not the surface teams, not policy. Picking a demotion strength without a measured cost axis is picking a number.

Faisal is right that we should not throw away most of a classifier's information by thresholding it. The symmetric obligation is that a graded penalty applied across the whole score spectrum touches vastly more content than a threshold did — so the collateral-damage surface is *larger*, not smaller, under soft enforcement.

## 4. The calibration question — and why it gates everything

**Are the classifiers calibrated? And calibrated against what — the *probability* of being bad, or the *severity* of the badness?**

These are different objects and they imply different math:
- **q = P(harmful)** → the correct treatment is expected-utility, which produces a multiplicative form (see §6).
- **q = severity** (ordinal, not probabilistic) → an additive penalty scaled by severity is the natural form.
- **q = an uncalibrated classifier score with a chosen operating point** → neither derivation is valid, and every λ is a hand-tuned magic number.

The evidence points at the third case. The vision doc's own footnote defines violative as **"self-harm model score ≥ 0.193 (decision = 2)."** A 0.193 operating point is a precision/recall choice, not a probability. So the likely honest answer is *"neither, cleanly."*

**This is the gating dependency on the entire safety-as-a-signal program**, and it is a question CQ can answer this week. It should be asked first, not last.

## 5. Distributional principles from Facebook and Snap

### 5a. Filter early — as far upstream as possible

Any point-wise filtering should happen **as upstream and as early as possible**, so the effort is not wasted. The reasoning is concrete: you have spent compute, retrieval budget, and ranking capacity pushing content all the way downstream only to demote or drop it at the end. That is waste of your own internal effort, at every layer it traversed.

Where possible: **expose the signal and threshold-filter upstream — the worst of the worst.** Even for content that is not policy-violating, we should have an opinion on when the probability of a bad experience is high enough, and/or the severity bad enough, that it warrants point-wise removal.

### 5b. Shape late — spacing is a set-level problem, not an item-level one

**This is the core insight from the Snap suggestive-content work (James + Michael).** One or two bikini pictures is fine. Condensed together, the feed becomes entirely suggestive. **It was never a per-item problem — it was a slate problem.**

The intervention is spacing: what is the optimal spread? How do you keep this class of content from overwhelming the experience? That happens at the **late/blending stage**, where spacing between items is what you control.

**Filter early, shape late.** Two different objectives at two different layers — point-wise removal upstream, set-level shaping downstream. Stated that way, §5a and §5b are complementary rather than contradictory.

> **Direct read on the docs:** this is exactly the rope-pin image that opens Faisal's vision — safe alone, unsafe in company — and exactly what **Unsafe Slate Rate** was built to measure. It is also the structural gap in CQ's design-options doc: **that doc is entirely pointwise** (`w_i · BCE(pred_i, label_i)`, per-item utility penalties, per-item quality heads). **A pointwise loss cannot optimize a set-level objective.** USR is a property of the slate. Faisal citing SlateQ is the tell that he knows the unit of analysis is the point; the tactics doc reverted to per-item without noticing.

### 5c. Additive vs. multiplicative demotion

The third principle from Facebook, stated as the trade-off James has carried:

- **Additive demotions** (`U = E − λ·q`) are attractive because they **decompose** the objective content-quality objective from the engagement objective. You can point at the term and attribute it.
- **But additive is mutually assured destruction.** One side simply adds more weight over time to overwhelm the effect of the other. That is the incentive problem.
- **Multiplicative demotions** (`U = E · (1 − λ·q)`) work synergistically with the engagement objective rather than against it — but they slow down engagement-moving teams.
- **For something severe — teen safety — multiplicative is likely warranted**, because it wraps the whole utility and guarantees the outcome is accounted for.

**The conclusion is right. §6 replaces the argument with something that survives contact with a technical room.**

## 6. The sharper version of §5c

Three problems with the argument as stated, and the derivation that fixes them.

### Problem 1 — "additive decomposes the objectives" is only true in linear space

Multiplicative decomposes just as cleanly in log space:

```
log U  =  log E  +  log(1 − λ·q)
```

You get the attribution/accountability benefit **and** scale-free behavior. The real question is not *separable vs. entangled* — it is **which space you are separable in.** Once framed that way, additive's claimed advantage largely evaporates.

### Problem 2 — additive's failure mode is worse than "one side adds more weight"

It does not require anyone to *try*. In a utility of the form

```
U = Σ_k w_k · p_k  −  λ · q
```

every engagement launch that raises some `w_k` mechanically dilutes λ·q's share of the budget **without anyone touching λ**.

> **Additive demotion decays by default, through ordinary good-faith work, and the decay is invisible in attribution** — no single launch shows up as a quality regression, because the damage is spread across fifty of them.

That is a much stronger indictment than an incentive story about bad actors, because it needs no bad actor. And multiplicative is structurally immune to it: a proportional haircut is **invariant to engagement-weight inflation**.

### Problem 3 — "synergistic" is not a property

Here is the derivation. Let `q = P(item is harmful)` and assume the engagement value of a harmful impression is zero, with an absolute cost `C` to exposing harm:

```
E[U]  =  (1 − q) · E   −   q · C
```

**Both terms fall out of one expectation, and each answers a different question:**

| Term | Form | What it means | Who owns it |
|---|---|---|---|
| `(1 − q) · E` | **multiplicative** | Discount engagement by the probability it is illegitimate. **This is the degaming / engagement-purification term.** | The classifier — needs calibrated `q` |
| `− q · C` | **additive** | The absolute externality of exposing harm. | **Policy** — `C` is severity |

So the answer to *"additive or multiplicative?"* is **both — and they are not competing, they answer different questions.** The multiplicative factor asks *is this engagement real?* The additive term asks *what does exposure cost?*

**Why this framing wins the room:** it converts the debate from "safety team vs. engagement team" into "what does your score actually mean." That is a question no one can read as a turf move, and it is the question Faisal — very technical, KDD chair — will engage with on the merits.

**It also yields a governance rule rather than just a diagnosis.** `C` is in absolute units, so unlike the multiplicative factor it *does* get diluted by engagement-weight inflation. Therefore:

> **`C` must be denominated in units of `E`, and re-pegged whenever the engagement weights change.**

That is the concrete fix for the mutually-assured-destruction problem, and it can be written into a design doc as a maintenance requirement.

**And it makes §4 load-bearing:** this math is only valid if `q` is a calibrated probability. Given the 0.193 operating point, it currently is not.

### The doctrine sentence

> **The functional form should follow from the objective/subjective split.** Objective harm gets multiplicative (or a gate), because we are asserting that no amount of engagement redeems it — multiplicative suppression is unbounded as `q → 1`. Subjective quality gets additive, because we are asserting it is a trade-off that sufficiently good content is allowed to win — additive penalties are always beatable by a high enough `E`. **If you cannot say which one a signal is, you cannot say what math to apply to it.**

## 7. What this implies for the three docs on the table

1. **The metric is slate-level; the proposed mechanism is pointwise.** The vision commits models to "learn against Unsafe Slate Rate, not only Pin-level labels." CQ's design options are entirely per-item. That gap has to be closed before any of the sequencing questions matter — and spacing/blending (§5b) is the mechanism that already exists to close it.
2. **The L1-vs-L2 argument is scoped to the wrong surface.** Michael's own reply to the CTO: **~50% of unsafe slates are Related Pins, ~25% Homefeed, ~24% board ideas.** Homefeed-first optimizes a quarter of the problem. On RP, CQ already has a shipped L2 demotion win. A problem split 50/25/24 across three surfaces cannot be fixed surface-by-surface at L2 — **the only lever that touches all surfaces at once is the shared pretrain backbone (CFM/UPP)**, which is CQ's own Phase 2, currently gated behind a Phase 1 on notif/search. The CTO's "all surfaces?" question plus Michael's own data are the argument for pulling Phase 2 forward.
3. **"Board ideas" is 24% of the problem and has no owner** anywhere in the milestones doc.
4. **Safe Cold Start has Eng POC = TBD**, and new-user enablement is already James's charter.
5. **Measurement has no DS POC**, an uncalibrated LLM judge, and a headline "7× spiral" number that conditions on a tap — i.e. selection, not causation. Teens who tap an unsafe slate are different teens. If the mandate rests on 7×, that needs a causal check before it is load-bearing in front of the CTO. *(Michael conversation, not a joint-room conversation.)*
6. **The CTO asked to "tie this back to Anticipation"** — on the In-Session Awareness pillar specifically. The technical substance is real: **in-session awareness and anticipation are the same machinery pointed at different objectives.** Anticipation predicts the user's next want; spiral detection predicts the user's next harm. Same user-state representation, same sequence model, same cross-surface trajectory object.

## 8. Still to capture (James's dump, in progress)

- **Actor quality / creator-level layer.** CQ's doc has *no* actor layer at all — it is 100% content-scoring. Facebook's integrity stack was substantially actor-level. Missing axis in their entire design space.
- The Snap suggestive-content work with Michael, in full.
- Measurement under headline pressure: sampling, human calibration, what was reported up vs. what was steered on.
- Curated-corpus / allowlist inversion (Faisal's Idea 2) — did it ever survive, and what did it cost in breadth?
- What went wrong / what James would never do again.
