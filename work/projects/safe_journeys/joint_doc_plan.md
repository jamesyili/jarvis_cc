# Joint CQ×P13N Doc — Build Plan (grill session 2026-08-18)

> Working decisions for the co-authored James+Qinglong doc (draft to Qinglong Wed 8/19 → Dylan+Andrew Fri 8/21/Mon 8/24 → Bill Ready deliverable Wed 8/26 → Bill review 8/28). Spine = `placement_doctrine_v2.md` (Option 1, ratified 8/16d). Public commitment (WG thread 8/17): "a framework around safety/quality levers that can be applied to topics 2 and 3" of Michael's milestones doc.

## Decisions

**D1 (2026-08-18): One Google Doc, two tabs.**
- **Tab 1 — Technical alignment.** Audience: Qinglong, Dhruvil, Dafang (+ Dylan/Andrew read deep). The doctrine-derived framework; carries the key-alignment points.
- **Tab 2 — Executive summary.** Audience: leadership chain up to Bill Ready. Timelines are the centerpiece (James: "the biggest ask from leadership is timelines").
- One substrate, two reading depths — not two documents. Rejected: separate exec doc (fork risk, double maintenance on a 1-week fuse).

**D2 (provisional): phased/gate-based timeline shape liked** (12-week, hard dates only where ungated) — details deferred until technical scope is settled. Timeline derives from the technical plan.

**D7 (2026-08-18, revises D1): Tab 1 carries the decisions + timeline; Tab 2 deferred to post-Friday co-writing.**
- **Tab 1** (Wednesday to Qinglong = Friday to Dylan/Andrew — same tab): technical alignment + the **prioritization-decisions block** (GenAI-vs-teen-safety · NLFU-vs-responsiveness · measurement DS staffing · retention holdout) + the **phased timeline**.
- **Tab 2** (exec summary for Bill): NOT drafted now — headers-only placeholder; **co-written with Dylan + Andrew after their Friday review** so they co-own the Bill framing (Andrew has the 8/28 slot). James: drafting it ourselves now is not a good use of time.

**D3 (2026-08-18): Training-time section structure — ratified.**
1. Shared diagnosis first (engagement-only ranker structurally biased — Qinglong's + Faisal's words, credited).
2. **The push: quality head predicting downstream session density** (session crowded with unsafe/GenAI content = unsafe session) on downstream-rewards machinery — NOT per-pin. Three payoffs stated in the doc: (a) v0 label computable from existing logged classifier scores — decoupled from judge calibration; (b) topic-2/topic-3 bridge — the head is simultaneously the training-time quality objective and the spiral predictor (+ Anticipation tie-back); (c) reuses downstream-rewards machinery — new target, not new system. Assignment: **Dhruvil + Dafang put the head plan on paper** (label def, features, viability), dated. Scoped as a bet with a kill criterion.
3. **Reweighting = evaluated-alternative, one paragraph**: §4.5 equivalence (reweighting ≡ multiplicative penalty at training time; the P0 utility change already delivers that suppression tunably at serving) → training budget goes to what serving can't do. Criteria: auditability, per-surface tunability, reversibility, signal preservation. Kept available as cheap baseline. Not deleted, not centered.

**D4 (2026-08-18): The head lives at FINE-TUNE** (James: "fine-tuned for sure") — head-adapter pattern on the UPP/CFM framework, per the existing hide/report-head precedent. **Baking quality objectives into pretraining = explicitly open research** ("a deeper topic," no position) — listed in the doc's open questions, tied to Qinglong's own note that generative-recsys-era methods (RecGPT) may reopen it. Doc does NOT adjudicate CQ Phase 2; it defers it honestly.

**D5 (2026-08-18): Ask 2 survives, reframed as mutual accountability with named owners.**
- All three instruments stay: (1) suppressed-set hold-back → "deriving λ instead of picking it" (operationalizes CQ's own Pareto claim); (2) unregrettable-engagement denominator (protects safety launches from over-billing — a gift to CQ); (3) **retention holdout: designed in technical tab, asked for in exec tab** (org-level resourcing decision for leadership).
- **Accountability is two-sided and explicit** (James: "both teams should be accountable... clarity about who's accountable for what"). The doc carries an ownership split: **CQ accountable for** signal quality/coverage, calibration maps (versioned, per category+surface, re-calibrated on schedule) landing in Galaxy, teen-safety signal prioritization, label pipelines. **Recsys accountable for** integration (density control, utility penalties, SSD adaptation), the downstream-density head, experiment scaffolding, engagement outcomes of enforcement. **Joint:** metric definitions, both-axes-on-the-same-slide reporting (voiced first-person-plural), λ derivation.
- Seed = doctrine §1.4 quantities table (every quantity already has an owner); extend to work items.
- Calibration = CQ-owned critical path; the doc asks CQ to commit the date ("when do calibrated classifiers land in Galaxy" — James's own first sequencing question).

**D6 (2026-08-18): Topic 3 = lean, dovetailed with the head, honest about maturity.**
- Detect with transparent rules first (repeated unsafe slates, rising density, cross-surface recurrence); respond by turning topic-2 knobs harder (raise λ, tighten density band, gate notif sends, re-seed); the density head becomes the learned detector later (the dovetail).
- Scope-outs answering Michael's WS3 questions: UX interventions out (Wellbeing/WS5 owns visible treatments); user-level seeker work out of v1.
- **Stated plainly in the doc: this pillar needs real design work to get going** — depth doesn't exist yet. **JJ = the named person to connect on responsiveness design** (he led in-session responsiveness; NLFU×Responsiveness launch landed).
- **New trade-off surfaced: in-session responsiveness rides on NLFU work** — prioritizing it means re-prioritizing against the NLFU H2 push (Vicky/Jeff-approved Q3 SSv2 scope, Growth-driven). Goes in the prioritization asks.

**D8 (2026-08-18): Workplan blanks resolved.**
- **P0 density-control signal: CQ's decision, not the doc's.** The doc states requirements on whatever they pick: calibrated, and collateral damage measurable (regrettable-engagement instrumentation). Hands CQ a real decision on their own turf.
- **First head consumer: Homefeed.** James: "we are the HF team — we shouldn't be asking the work to be started on another surface." Doc principle: **commit only what the authors own** (HF work = James's, signal/calibration work = CQ's); other surfaces (RP, Search, Notif, board ideas) get adoption paths, not commitments. ⚠️ Leo correction absorbed: never propose starting work on a surface/team the principals don't own.
- **Zisis Petrou: reports to Dhruvil; ignore for now** (no role in the doc's ownership table).
- Deprioritized, stated in doc: probabilistic throttling (timeline trade-off; retrieval-stage fallback), corpus selection for teen cohorts (universal-only).

**D9 (2026-08-18): Frame + outline ratified; draft v1 written and sent.**
- Frame: general quality/safety-levers framework, instantiated first on teen-safety self-harm (GenAI next). Outline = 10 sections per grill Q11.
- `joint_framework_v1.md` drafted (fresh prose, circulation-safe by construction, `[QZ: …]` slots as Qinglong's co-author entry points), emailed to James 8/18 (msg_id=1a015ceddd78f038).
- `placement_doctrine_v2.md` header now carries **private master — do not circulate** status.

## Remaining before Wednesday send

- James reviews/edits v1 (esp. §5 Anticipation framing, §8 week numbers, §9 wording of the NLFU ask)
- Paste into Google Doc, two tabs; send to Qinglong by Wed 8/19
- Key technical alignment points for Tab 1 (James: discuss later in session)
- Circulation-safety cut list application (§7 + internal blockquotes §3/§5.4) — mandatory before Wednesday send

**D10 (2026-08-20, James — supersedes D6's lean-section plan): Topic 3 scoped OUT of the doc entirely.**
- James attempted the section post-send ("sweeping changes" pass), judged the real depth unreachable as of now — not a writing problem, a design-maturity problem. Decision: don't write it at all; **tell Michael topic 3 isn't ready to present** — needs actual design time + an ROI assessment of the responsiveness efforts before it goes in front of leadership.
- Rationale on record: presenting knob-turning dressed as design to a Bill-bound doc costs more credibility than an honest "not yet." The NLFU-vs-responsiveness bandwidth trade-off (D6) is *why* the design work hasn't happened — it survives as context for the follow-up scoping, whether or not it stays in the doc's decisions block.
- Explicitly rejected: dumping authorship on JJ (three lanes already: L1 utility · responsiveness-for-growth · Reflex).
- ⚠️ Public-commitment delta: the 8/17 WG thread promised a framework "applied to topics 2 **and 3**." The Michael message narrows that — proactive framing is the mitigation. Co-author note: Qinglong should hear the scope change from James, not discover it (doc is joint; he's deep-reading it 8/20).

## Status — post-send (updated 2026-08-20 from James's Slack screenshot)

**Wednesday send: DONE 8/19.** Google Doc live; James was still editing the training-time levers section ~11 PM (Qinglong noticed the live edits).

**Qinglong's response (8/19 11:09 PM DM): warm + specific.** "Expands my original doc with a lot more technical depth/details… genuinely a pleasure to read." Aligned on: score calibration · **L1-vs-L2 framing for demotion** (the old clash point, now conceded in James's framing) · additive-vs-multiplicative demotion trade-offs · pass-through + iteration-cost implications. Committed to a proper read of the training-time section **8/20** with thoughts to follow — **D3 (density head) reaction + `[QZ]` slot-filling still pending = the live co-authorship test.**

**Circulation (agreed in-thread):**
- **8/20:** share with **Dafang He + Dhruvil** (James proposed, Qinglong agreed) — the Tab-1 audience and the D3 head-plan owners.
- **Jianing Sun added** (Qinglong's ask, James approved): his TL, drove SSD spacing for CQ + demotion on other surfaces. CQ committing senior IC bandwidth = co-ownership signal. *Watch:* D5 has SSD adaptation under recsys accountability — keep that line clean as he reads.
- James reciprocating with shares on his own side ("I will do the same and encourage…" — recipients TBC, presumably JJ/Rui-side).

**Next gates unchanged:** Dylan + Andrew review Fri 8/21 / Mon 8/24 → Bill deliverable Wed 8/26 → Bill review 8/28 (Andrew's slot). Tab 2 still headers-only until the post-Friday co-write (D7).

## Status — Dhruvil's section lands (2026-08-24, Monday)

**Dhruvil wrote a full review section directly into the doc** — summary, observations, ten action items — following Qinglong's 8/21 commitment to add his ideas. Verbatim + full Leo read: `sources/07_dhruvil_doc_section_2026-08-24.md`.

**The structural read:** 80% correct, 100% consequential. Two moves stacked — (A) a new prioritization rubric (*effectiveness × funnel efficiency × risk*, "most importantly risk"), where the risk axis is **HF L2 offline-online correlation**, a quantity only his pillar measures; (B) the work relocates upstream into James's pillar while blending (his pillar post-reorg) becomes the thing protected from intervention. Four of ten action items name James Li, including all three open-ended ones; Dhruvil is never a sole owner. The summary line — *"many of these things will need to be addressed before LR approval / shipping"* — makes the section function as a **launch-review gate written in advance**.

**D11 (2026-08-24, proposed — unratified): integrate, don't append.** Fold Dhruvil's section into the existing spine before the Wed 8/26 Bill deliverable rather than let it stand as a block: success criteria → new §0/§4.0 · three-axis rubric → §4, *applied* to the lever list · model-intervention menu (margin loss, VLM-positives-as-in-batch-negatives, genAI in impression sequence, bucketed calibration/offline eval) → §5, credited to Dhruvil/Akshay · offline-online correlation as a **measured budget** + blending holdout → §7 · funnel analysis + Helium prevalence → §8 Phase 1 · genAI-vs-teen-safety sequencing pushed back to **§9 decision #1** rather than resolved silently · the two early-funnel questions → §10 with James as owner and a date. Rationale: whoever integrates owns the frame, and a doc with three appended author blocks has no author.

**Three counters on record** (all sourced, none territorial):
1. **"All upstream" is not currently available for genAI** — genAI-domain is a domain/landing-page-level signal and **L1 cannot consume it today** (CQ's own doc, source 04, 1A-i cons + their L2-preference rationale). Fork: L1 gains domain-signal capability (a build, needs date + owner), or genAI enforcement stays at L2/blending near-term.
2. **Washout (CQ's argument) and dilution (Dhruvil's X*K argument) are the same phenomenon** — wherever the quality objective is absent, that layer reverses the layer that has it. Both resolve to the doc's §5 spine: put the objective in the model. His section is an argument *for* §5.
3. **"No counterfactual" is false** — §7 already carries the ε hold-back and the retention holdout; a blending-intervention holdout supplies exactly the counterfactual he says can't exist.

**D10 precedent applies to Tab 2:** present the framework + teen-safety timeline, with **genAI as the second instantiation gated on the funnel analysis and success criteria**. Honest "not yet" over a workplan whose priorities aren't settled — the same call that earned credibility on topic 3.

**Timing risk:** Bill deliverable Wed 8/26, review Fri 8/28, Tab 2 still headers-only. Raw, the section gives the exec tab an action list reading "James Li owes four answers" plus an unsettled-and-risky genAI story — the opposite of D1/D7's timelines-are-the-centerpiece.

**Open:** D11 unratified · CG-level genAI load + affinity analysis (the best deliverable James can put on the table this week; doubles as the funnel analysis) · 2×2 L1×blending factorial design (item 7 — propose, don't receive) · HF L2 PoC pick (Dylan's read first, then coordinate with Dhruvil) · the concession-and-forks message to Dhruvil.
