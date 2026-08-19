# Quality and Safety Levers in the Recommendation Stack

**A joint framework for Safe Journeys Workstreams 2 & 3**

James Li · Qinglong Zeng — Draft v1 for co-iteration, August 2026

> *Draft note (cut before wider circulation): sections marked `[QZ: …]` are open slots for Qinglong — references, dates, and calls that are CQ's to make. Tab 2 (executive summary) is deliberately unwritten; we propose co-drafting it with Dylan and Andrew after their review.*

---

## Tab 1 — Technical Framework

### 1. What this document is

Michael's milestones doc asks Workstream 2 for "a tech design that is scalable across surfaces and parts of the stack, with the tradeoffs surfaced," and Workstream 3 for a plan to catch spirals before they become destinations. This is that design, written jointly by the two eng POCs it names.

Scope: **Workstream 2 (Safety-First Ranking) and Workstream 3 (In-Session Awareness).** Out of scope here: the USR metric definition and productionization (Workstream 1), wellbeing UX features (Workstream 5), and the teen-safe content corpus (Workstream 4, with the Activation team).

One framing choice up front: **this is a framework for quality and safety levers in general, instantiated first on teen-safety self-harm.** The same levers, scaffolding, and measurement apply to GenAI content quality and to the categories the vision doc names next (racy, gross, weapons, substances). Quality-aware ranking is a technical foundation that benefits multiple workstreams; building it once, category-agnostic, is the whole point. Teen safety is the first and most urgent application, not the boundary.

### 2. The shared diagnosis

We arrive at this program from two directions — CQ from years of signal adoption across surfaces, recommendations from ranking-stack ownership — and we agree on the diagnosis.

**Filtering is necessary and insufficient.** CQ's production experience: signals with 50–70% offline recall show far smaller production impact, because removed candidates are back-filled by *adjacent* borderline content the filter missed, not by good content. The recommendation system is not aware of quality; it fills every vacated slot with the next most engaging thing, which lives in the same neighborhood. Hard filtering also produces step-function engagement costs (the racy filter cost ~4–5% of male impressions) while leaving everything below the line untouched.

**The line itself distorts behavior.** External precedent shows what happens with hard policy-line enforcement alone: engagement concentrates just below the line and trends up. The goal is the opposite — borderline-content engagement should trend *down*. `[QZ: add the publication reference]`

**The ranker is structurally biased toward engaging slop.** Negative feedback (hides, reports, short clicks) is sparse; low-quality content still earns long clicks; adding quality features has not been enough. The model has no incentive to prefer safe content — it is told "no" after the fact on a subset of items. Safety must be inbuilt, not band-aided.

Everything below follows from taking those three statements seriously: **quality becomes a first-class objective, at serving time and at training time**, using the full spectrum of the signals rather than a threshold.

### 3. Shared vocabulary

Most disagreements in this space are vocabulary disagreements wearing technical clothes. These are the terms the rest of the document runs on.

**Layers** — where a decision can act:

| Layer | Decides | Granularity |
|---|---|---|
| Corpus / inventory | What is eligible at all | Binary, content-level, universal |
| Retrieval | What is sourced for this user | Set composition, user-conditioned |
| L1 / light ranking | Cheap scoring over the full candidate set | Image-level features; sees the whole set |
| L2 / full ranker | Final ordering | Rich features, full context |
| Blender | Slate assembly | The only layer that sees an assembled slate |

**Units** — what a metric or mechanism is defined on. A metric defined on one unit cannot be optimized by a mechanism defined on another:

| Unit | Mechanisms | Metrics |
|---|---|---|
| **Item** (one pin) | Filter, demotion, per-item penalty | Prevalence, item-level recall |
| **Slate/set** (shown together) | Density control, diversification (SSD) | Density, Unsafe Slate Rate |
| **Session** (slates over time) | Responsiveness, re-seeding, journey risk | Spiral measures, session-level density |

**Quantities, each with one owner:**

| Symbol | Meaning | Owner |
|---|---|---|
| `q` | Classifier score for an item — ideally P(harm-adjacent) | CQ (the classifier) |
| `h` | Realized harm — impression-normalized reports/hides/See-Less | Measurement |
| `cₖ` | Severity of category k | Policy — never the classifier |
| `E` | Engagement utility | Ranking |
| `λ` | Penalty strength | Derived from the cost curve (§7), not picked |
| `ρ(band)` | Density — share of a set whose scores fall in a band | The density-control lever |

**Calibration states**: a score can be probability-calibrated (`q` = P(harmful)), severity-ordinal, or an operating-point score trustworthy only near one cut. Threshold enforcement needs the score correct at one point; **every graded mechanism in this document needs it correct across the range.** Which state our classifiers are in today is an open empirical question (§10) and the first thing to audit.

### 4. Serving-time plan — utility changes

The general form: `utility = f(engagement) − λ · g(quality score)` — a graded penalty, not a gate, shaped per surface and audience.

*A note on how §4–6 are written: each lever ends with a **trade-offs block**. The prose states the properties we are prepared to defend; the pros/cons are deliberately left as placeholders to complete together, and the "to discuss" lines mark the dimensions that need joint discussion or measurement before either team should write the answer alone. Surfacing the tradeoffs is the milestone doc's explicit ask — this is where we do it.*

**P0 — density control at L1, single signal, on Homefeed.**
Cap the share of a candidate set whose score falls in a configured band. Why this is first:

- **It is threshold-free.** It needs a score and a band, not a per-item verdict — it uses the full spectrum of the signal, which is the program's stated direction.
- **It is backfill-proof by construction.** It constrains the *composition* of the set, not the identity of its members; whatever arrives to fill a slot is subject to the same ceiling. Per-item removal invites adjacent backfill (§2); a composition cap cannot be backfilled against.
- **It cannot be washed out downstream.** A per-item demotion at L1 can be re-ranked away by an engagement-only L2. A density cap cannot: if the borderline mass never reaches L2, no downstream re-ranking resurrects it. Composition control and per-item demotion have different washout behavior, and this is the reason to lead with composition.
- **It moves a named success metric directly.** Density ("what fraction of an individual teen's feed is borderline") is already on the table as a candidate metric; this lever enforces a ceiling on exactly that quantity.
- It is cheap, decoupled from the contested blender, and fits L1's per-candidate budget (precomputed content-side scores, O(1) lookup).

**Which signal goes first is CQ's call** `[QZ: name the P0 signal]`. The framework's requirements on whichever signal is chosen: it must be **calibrated** (§7) so the band means something, and its **collateral damage must be measurable** (§7) so the launch can be judged on both axes.

> **Trade-offs — density control** *(placeholders, to complete together)*
> - **Pros:** *[e.g., threshold-free; backfill-proof; moves the density metric directly; …]*
> - **Cons:** *[e.g., needs calibrated bands; coarse relative to per-slot decisions; …]*
> - **To discuss:** the cost model when the cap binds — what replaces the demoted band and for whom (the cost concentrates on users who heavily engage that band, which is also where the regrettable-engagement claim lives); band-setting risk (starving a legitimate interest area); per-request candidate-set unit vs. anything session-shaped; how budgets interact once multiple signals each carry a band (P1).

**P1 — multi-signal density control, and SSD over score vectors.**
- Multi-signal density: the P0 mechanism generalized to several signals with per-band budgets, plus spacing across flagged categories.
- **SSD (sliding spectrum decomposition)** — the diversification machinery already shipped in production — selects greedily on `relevance + γ · diversity`, where diversity is the volume spanned by the item vectors (computed by modified Gram-Schmidt over a sliding window). The mechanism is agnostic to what the vector encodes: fed the **classifier prediction vector** instead of a content embedding, it de-clusters items with similar risk profiles across the full score spectrum, with no threshold anywhere. One design honesty: SSD *de-clusters*; it does not *suppress*. It prevents the pile-up that turns individually-permissible items into an unsafe slate, while suppression itself comes from the quality term and the density cap. The two levers are complements.

> **Trade-offs — SSD over score vectors** *(placeholders, to complete together)*
> - **Pros:** *[e.g., threshold-free; consumes the full prediction vector; machinery already shipped; …]*
> - **Cons:** *[e.g., relevance cost is spread rather than targeted; per-pin attribution ("why did this pin drop") is hard; …]*
> - **To discuss:** the integration shape — extend the deployed SSD's item vector with score dimensions (one pass, but a single γ entangles content-diversity with risk de-clustering and changes current production behavior) vs. a second SSD pass over the score vector alone (independent tuning, but two set-shapers interacting and ordering matters). This choice is the P1 work item.

**L2 utility penalties** remain the highest-precision tool and are already proven: P2P demotion (LQS Rate V2 −0.87%, neutral topline) and Search demotion (UCAN LQS ~−10%, US repins +1.13%) both shipped at L2. Where per-slot precision matters and domain/landing-page signals are needed, L2 is the right home. The L1-vs-L2 question that has consumed prior discussions dissolves under the unit vocabulary: **composition upstream, precision downstream — both, each doing what only it can do.**

> **Trade-offs — L2 utility penalties** *(placeholders, to complete together)*
> - **Pros:** *[e.g., richest features and full-candidate context; proven demotion launches; supports domain/landing-page signals; …]*
> - **Cons:** *[e.g., a serving-time patch — the learned objective is untouched; heavily-tuned utilities are costly to change; …]*
> - **To discuss:** λ transfer across surfaces without calibration (why per-surface tuning currently feels like hand-fitting); how a shared quality score enters surface-owned utilities without each surface re-deriving its own definition.

**Penalty form is a policy statement, made per signal.** The multiplicative form `(1−q)·E` asserts that no amount of engagement redeems the item as `q → 1`; it requires calibrated `q` and is invariant to engagement-weight inflation. The additive form `−q·C` asserts a tradeoff that sufficiently good content may win; it is easier to attribute and tune, but decays silently as engagement weights inflate — so `C` must be denominated in units of `E` and re-pegged whenever the weights change. Choosing per signal, explicitly, keeps "what does your score mean" separate from "what does policy assert."

**Considered and deprioritized, with reasons:**
- **Probabilistic throttling** (keep-probability `1−g(q)`, i.e., graded demotion implemented as a gate at retrieval). Attractive properties — nothing downstream can undo it, and sweeping the rate traces the whole cost curve — but it is a new build, and on this timeline it competes head-to-head with density control for the same slot. Density control wins on time-to-value; throttling stays on the shelf as the retrieval-stage option if density control underdelivers.
- **Corpus/inventory selection for teen safety.** Corpus selection applies universally — there is no cohort-specific treatment — so it cannot carry teen-specific policy. It remains the right home for universal worst-of-the-worst removal, and it is not this program's lever.

### 5. Training-time plan — teaching the model, not just correcting it

Serving-time penalties adjust what is shown; they leave the learned objective untouched. The engagement head still *wants* to promote engaging slop. The question is what to change about what the model learns.

**The push: a quality head that predicts downstream session density.**
Not a per-pin label prediction. The head predicts a **session-level outcome**: does the forward window of this user's session become crowded with flagged content — a session that crosses a configured density of self-harm-adjacent (or GenAI-slop, or racy) impressions is labeled an unsafe session, and the head learns to predict that outcome from the current state and candidate. It rides the **downstream-rewards machinery that already exists** — this is a new target for infrastructure we already run, not a new system. The user-sequence annotation Dhruvil has proposed (annotating the sequence with signal scores) is the natural input: the annotated sequence is the trajectory whose forward risk the head predicts.

Three properties worth stating plainly:

1. **The v0 label is computable today.** Session density over logged classifier scores requires no LLM judge, no human labeling round, no new metric productionization. The training-time path is not gated on the measurement workstream's staffing.
2. **The same head serves Workstream 3.** Predicted downstream density *is* a journey-risk signal — the learned spiral detector §6 needs. One build, both workstreams — and it connects this program to the Anticipation direction: the same user-sequence substrate, predicting what the user will want next and what will harm them next, as two heads on one representation.
3. **It is category-agnostic by construction.** Swap the label's category configuration and the same head serves GenAI quality — the shared-scaffolding argument in concrete form.

**Placement: fine-tune stage**, as a head-adapter on the existing pattern (the hide/report head precedent). How quality objectives should enter *pretraining* is a genuinely deeper topic that this document deliberately does not adjudicate — it goes to open questions (§10), noting that generative-recommender methods may change the answer when that transition matures.

**Assignment:** Dhruvil and Dafang to put the head plan on paper — label definition, features, viability, offline eval design. `[Target: paper by end of Phase 1 — date in §8.]` The head is scoped as a bet with a kill criterion, to be set in that paper: if it cannot beat the transparent rules baseline (§6) on forward-density prediction within the evaluation window, we fold back to serving-time levers and the rules trigger, having lost little.

> **Trade-offs — downstream-density head** *(placeholders, to complete together; several of these belong in the Dhruvil/Dafang paper)*
> - **Pros:** *[e.g., objective matches the harm (a trajectory, not an impression); v0 label available today; serves both workstreams; …]*
> - **Cons:** *[e.g., predicting a rare future event is a genuinely hard learning problem; multi-task interference with engagement heads; …]*
> - **To discuss:** the forward-window choice — rest-of-session vs. next-N-impressions vs. next-session (learnability vs. actionability); the consumption path (a weighted downstream-reward term in utility, with the head's own calibration to establish); v0 label bias — labels from uncalibrated logged scores mean the head learns the classifier's mistakes at session scale (accept for v0 and relabel when calibrated scores land, or wait and re-couple to the calibration path); the base rate of threshold-crossing sessions — unknown, and a Phase-1 measurement task before the paper commits to a target; evaluation under intervention (once we act on predicted density, the label distribution shifts).

**Evaluated alternative: loss/label reweighting** (down-weighting positive engagement on flagged items). We looked at this seriously — it directly attacks the reward loop, and it is cheaper than data cleanup. Two things argue against it as the primary path:

- **Equivalence:** down-weighting engagement on flagged items is the multiplicative penalty `(1−q)·E` applied at training time. The P0 utility change already delivers that same suppression at serving time — where λ is tunable per surface, auditable, and reversible by config. Baked into model weights, the identical intervention becomes none of those things.
- **It deletes signal rather than modeling it.** A criteria test for any training-time intervention: auditable, per-surface tunable, reversible, and it should *model* quality rather than silently discard training examples. The head passes; reweighting fails the first three and half of the fourth.

Reweighting stays available as a cheap baseline in the head's evaluation — if it outperforms the head on the same criteria, that is worth knowing and we will say so.

> **Trade-offs — loss/label reweighting** *(placeholders, to complete together)*
> - **Pros:** *[e.g., attacks the reward loop at its root; no new head, no serving change; cheapest to try; …]*
> - **Cons:** *[e.g., the equivalence and criteria arguments above; over-suppression of legitimately engaging content is easy and hard to detect; …]*
> - **To discuss:** down-weight vs. drop, and what weight schedule; what guardrail detects over-suppression before a launch review does.

### 6. In-session awareness (Workstream 3)

An honest maturity statement first: **this pillar needs dedicated design work that has not happened yet.** What follows is the shape we believe is right and the cheapest defensible v1 — not a finished design.

**V1 — transparent rules, existing knobs.** The trigger is journey risk crossing a threshold, computed from observable session state: repeated flagged slates, rising session density, a sensitive topic recurring across surfaces. The response is not new machinery — it is the §4 levers turned harder for that user: raise λ, tighten the density band, re-seed from declared interests, and stop reintroducing the pattern on other surfaces. Two design requirements from the start: **hysteresis** (different entry and exit thresholds, so the feed doesn't flap between two personalities) and **explicit exit criteria** (time decay and observed healthy engagement — a protected state nobody leaves is the walled garden the vision rejects, and it fails silently).

> **Trade-offs — rules trigger + existing knobs** *(placeholders, to complete together)*
> - **Pros:** *[e.g., explainable and auditable — defensible in a policy review; shippable without new serving machinery; …]*
> - **Cons:** *[e.g., hand-set rules are brittle per category and surface; misses patterns nobody thought to encode; …]*
> - **To discuss:** over-suppression of a legitimate sustained interest (the user genuinely into a sensitive topic); triggered-population size and experiment power (a small protected population is hard to A/B); per-user knob-raising is differential enforcement — mandated posture for teens, but a policy/comms question for adult categories that deserves an explicit answer before launch.

**Next-session before within-session.** Next-session response needs no real-time state store, triggers on accumulated evidence, and likely captures most of the value, since the spirals that matter persist. Build that first, measure the gap to within-session, and let the number justify the real-time build.

> **Trade-offs — next-session vs. within-session response** *(placeholders, to complete together)*
> - **Next-session, pros / cons:** *[e.g., cheap — an offline-computed user feature, no real-time state; evidence has accumulated so the trigger is reliable / does nothing for the session actually going wrong — the case the program is named after; …]*
> - **Within-session, pros / cons:** *[e.g., protects the user whose experience is deteriorating right now / real-time state and latency cost; reacts to thin evidence — one ambiguous tap is not a spiral; …]*
> - **To discuss:** what state exists today at serving time vs. what must be built (the real-time user sequence vs. cross-surface trigger state); what "the gap" is measured on, so the within-session build has a number to justify it.

**V2 — the head as the learned trigger.** Predicted downstream density (§5) replaces hand-set rules as the detector: earlier detection that generalizes across categories, on the same intervention machinery — at the cost of opacity in a policy review, which is a real cost for a safety system. Its trade-offs live with the head (§5); this is the dovetail between the two workstreams, and it is why we are not designing a standalone spiral-detection system.

**Sequencing note:** in-session responsiveness capability in P13N lives with the team that built the recent responsiveness launches, and that capacity is currently committed to NLFU work. Getting Workstream 3 moving at more than V1 pace is a prioritization decision, not an engineering unknown — it appears in §9. JJ is the right person to connect on the responsiveness design when that call is made.

**Scope-outs, answering the milestones doc directly:** UX interventions stay out of this workstream's v1 — visible treatments carry a categorically worse false-positive cost (telling a teen who is not in crisis that we think they are) and belong with Wellbeing (Workstream 5), sequenced after invisible ranking-side response has been measured. User-level seeker work stays out of v1 — this framework addresses in-session and next-session spirals; sustained-intent seekers are a distinct problem with their own PRD.

### 7. Measurement and mutual accountability

This program moves from thresholds to graded mechanisms. That raises, not lowers, the bar on signal quality — a threshold needs the score right at one point; a graded penalty needs it right everywhere. And it grows the error surface: penalties touch everything, so mistakes must be measured, not assumed. Both teams are accountable here, for different things, and this section says which.

**Calibration — CQ-owned, on the critical path.**
Every graded mechanism in §4–6 assumes the score means what it claims. The protocol: calibrate against stratified human labels (equal counts per score band, reweighted — uniform sampling yields nothing above the middle of the range at these base rates), per category and per surface; isotonic regression as the default estimator; reliability reported as per-band ECE, not aggregate (aggregate is dominated by the mass near zero and will look excellent while the operating region is wrong); calibration maps versioned, owned, and re-run on classifier retrain. Severity `cₖ` is elicited from policy separately — calibration produces probabilities, never severity.
**The asks on CQ:** the priority list of signals for teen safety `[QZ]`, and committed dates for calibrated versions landing in Galaxy `[QZ: dates]`. **In parallel and explicitly not blocked on this:** recommendations-side experiments run on uncalibrated signals for learning and scaffolding — with the understanding that launch decisions wait for calibrated bands.

**Collateral damage — jointly instrumented, one mechanism.**
Hold back a small random fraction ε of what the system would have suppressed, serve it, and measure both realized engagement and realized harm on the same population. This yields the false-positive rate per band and the forgone engagement per band — which is the input λ has been missing. **λ derived from a cost curve, not picked**, is what makes the quality↔engagement Pareto we both invoke an operational statement instead of a slogan.
Cost is denominated in **unregrettable engagement**: engagement the user would take back — proxied by hides, reports, See-Less, post-impression abandonment, validated against survey ground truth — is not a loss, and counting it as one overstates the price of every safety launch this program will ever run.

**Governance rule, ours jointly: both axes on the same slide, always.** A quality win reported without its engagement cost is not a result; an engagement cost reported without the harm it bought down is not one either.

**The retention holdout — designed here, decided above us.**
Engagement and harm-prevention converge on horizons longer than any experiment window; every individual launch is judged in the window where it looks worst. The instrument that settles whether this program pays for itself: a population held out from the content-quality stack as a whole, run for quarters, read on retention. Design constraints stated plainly: stack-level not per-launch; quarters not weeks; it cannot ethically include vulnerable users on violative content (the runnable version is adults and/or the borderline tier, with the teen case inferred and labeled as inferred); and the readout — metric, window, decision rule — is pre-registered so the number means something whichever way it lands. This is an org-level commitment and appears in §9 as a leadership decision.

**Who is accountable for what:**

| | CQ | Recommendations (HF) | Joint |
|---|---|---|---|
| Signal quality, coverage, priority list | ● | | |
| Calibration maps in Galaxy (versioned, re-run on retrain) | ● | | |
| Label pipelines | ● | | |
| Density control at L1, utility integration, SSD adaptation | | ● | |
| Downstream-density head (plan: Dhruvil + Dafang) | | ● | |
| Experiment scaffolding; engagement outcomes of enforcement | | ● | |
| Metric definitions; both-axes reporting; λ derivation | | | ● |

### 8. Sequencing — a 12-week shape

Hard commitments only where we own the work and hold the inputs; gates named where we don't. This plan commits **Homefeed and CQ signal work** — the two things its authors own. Other surfaces (Related Pins, Search, Notifications, board ideas) get adoption paths: the framework is surface-agnostic by design, shared definitions make adoption cheap, and each surface team sequences its own roadmap.

**Phase 1 — weeks 1–4 (committed on signing):**
- Experiment scaffolding + uncalibrated-signal experiments on HF (recs team).
- Density-control mechanism built at L1 on HF, band configuration ready for a calibrated signal (recs team).
- Head plan on paper — label, features, viability, eval, kill criterion (Dhruvil + Dafang).
- Calibration protocol stood up; priority signal list and Galaxy landing dates committed (CQ) `[QZ]`.
- Leadership decisions in §9 surfaced and routed.

**Phase 2 — weeks 5–8 (gated on: calibrated P0 signal in Galaxy; head paper approved):**
- Single-signal density control launched on HF with calibrated bands; hold-back instrumentation live from day one.
- Head v0 trained on logged-score labels; offline eval vs. rules baseline.
- SSD score-vector adaptation validated offline.

**Phase 3 — weeks 9–12 (gated on Phase 2 results):**
- Head consumed in HF ranking (downstream-reward term); v1 rules trigger for next-session responsiveness.
- Multi-signal density control; SSD online experiment.
- Adoption invitations with results in hand: shared definitions, calibration maps, and the density mechanism packaged for other surfaces.

### 9. Decisions we need from leadership

Four calls gate the timeline above, and none of them are ours to make. Stating them is the point of a timeline — a plan that hides its resource conflicts is not a plan.

1. **Relative priority: GenAI content quality vs. teen safety.** The recommendations-side scaffolding in this document serves both — that work is shared and starts now regardless. CQ-side calibration is per-signal extra work: which signals calibrate first follows directly from this call.
2. **NLFU vs. in-session responsiveness.** The responsiveness capacity Workstream 3 needs is currently committed to the NLFU push. V1 (rules + existing knobs) proceeds regardless; anything faster is a re-prioritization decision.
3. **Measurement staffing (Workstream 1 DS POC).** The head's v0 routes around this gap; launch-grade USR measurement and judge calibration do not. Every week this stays unstaffed moves Workstream 1's deliverables right.
4. **The retention holdout.** Quarters-long, stack-level, org-visible (§7). It is the only instrument that settles whether this program is an investment rather than a cost — we recommend it, and it needs a decision above the two of us.

### 10. Open questions

1. Calibration state of the current self-harm and borderline classifiers — probability, severity, or operating-point. Audit first; everything graded depends on the answer.
2. How quality objectives enter **pretraining** — deliberately unadjudicated here; revisit with fine-tune results in hand, and again as generative-recommender methods mature.
3. **Board ideas** — roughly a quarter of unsafe slates, and no owner anywhere in the program.
4. Journey-risk state: built on the shared user-sequence substrate (our recommendation, per §5–6) or standalone — decided with the substrate owners; the interface (substrate owns the representation; the safety head owns its target and thresholds) matters more than the placement.
5. The external precedent publication `[QZ: reference + what transfers]`.
6. USR holdout creation and maintenance (Workstream 1 dependency).

---

## Tab 2 — Executive Summary *(placeholder — to co-draft with Dylan + Andrew after Friday review)*

- The problem in one paragraph, in the program's own numbers
- What we will do, in three sentences (serve safer sets · teach the model · catch spirals)
- The 12-week timeline with its gates
- The four decisions we need
- What this buys beyond teen safety
