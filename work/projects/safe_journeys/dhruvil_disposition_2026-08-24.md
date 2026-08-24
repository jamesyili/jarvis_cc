# Dhruvil Section — Point-by-Point Disposition (2026-08-24)

> Working artifact for James's Monday editorial pass on `joint_framework_v1.md` (Google Doc). For each of Dhruvil's observations/action items: verdict (**Adjust** / **Already in draft — harden** / **Ignore**), the doc change, and a paste-ready reply. Built from a full read of the 24-page final draft (PDF, pre-comments). Companion to `sources/07_dhruvil_doc_section_2026-08-24.md` and D11 in `joint_doc_plan.md`.
>
> **Pattern (sets the tone):** of 8 observations, one is a real gap (success criteria), one is a half-gap (correlation risk), and the rest are either already in the doc or arguments *for* its P0. His 8b ("controllable distribution in L1 utility") **is** the doc's P0 density control — he re-derived the proposal and offered it back as a question. Answer everything warmly and precisely; the doc does the pushing. Every concession lands *inside the doc's structure* — a new section James authors, a new rubric row, a new P0-eval metric. Nothing survives as a free-floating objection.

**Doc-read facts confirmed (final draft, 24 pp):**
- Rubric already has four dimensions with **delivery and iteration drag listed first** — basis for L1 point-wise demotion at P1/P2, density head as gated research bet with kill criterion, training-time reweighting deprioritized.
- Full calibration section exists; calibrated, versioned outputs = stated **launch standard**.
- Density-control P0 eval already requires candidate-set→served-slate translation + "incremental and combined value with blender diversification."
- Collateral-damage decomposition (regrettable vs. non-regrettable engagement) already defined — gives §0 its measurement vocabulary.
- **Qinglong's slots still open in the final draft**: byline "add your name here," both `<Qinglong Zeng to amend/correct>` inline asks (Shared Diagnosis, filtering). Ask goes out today.
- Diversification trade-offs table does **not** mention offline-online correlation — the one real hole his section found.

---

## Observations

### Obs 1 — Set success criteria & goals
**Verdict: Real gap. Adjust.** Add §0 "Success criteria" (James authors): target outcome metric (served-slate genAI density / interim USR proxy), guardrails (WAU/SSv2 neutrality, regrettable-vs-non-regrettable decomposition), per-phase "done when."
**Reply:** *"Agreed — this is the right first ask and it's a gap. I'll add a success-criteria section defining the target outcome metric, guardrails (including WAU/SSv2 neutrality), and per-phase exit criteria. Note the collateral-damage decomposition in the doc already gives us the measurement vocabulary for it."*

### Obs 2 — "Prioritization only considers effectiveness; add funnel efficiency + risk"
**Verdict: Already in draft. Harden.** Rubric premise is factually wrong about this draft. Genuinely missing: offline-online correlation risk as a named consideration — add to rubric (within iteration drag or as fifth dimension); don't accept the rewrite premise.
**Reply:** *"The prioritization already weighs more than effectiveness — every lever is assessed on delivery/iteration drag, engagement trade-off, and control/scalability (it's why L1 point-wise demotion is P1/P2 and the density head is a gated bet, not a launch dependency). What the rubric doesn't yet name explicitly is offline-online correlation risk — I'll add that so post-L2 levers carry it visibly. With that added, I'd keep the current stack ranking unless a specific lever's assessment changes."*

### Obs 2a — "GenAI is personalization, not safety; late-funnel is a bandaid"
**Verdict: Reframe — partially accept for genAI, reject as general principle.** The load-bearing frame of his section; the one place to push back directly. First application is teen self-harm ("let personalization handle it" unavailable); the core diagnosis is a **composition** problem point-wise stages structurally cannot solve. Add one Shared Diagnosis paragraph: preference-shaped problems (genAI affinity → early-funnel model interventions) vs. composition-shaped problems (concentration/clustering → set-wise levers by construction).
**Reply:** *"Partially agree, and worth being precise about where. To the extent genAI is a preference-learning problem, yes — the funnel should learn it, and that's what the model interventions in §7 target. But the doc's core diagnosis is a composition problem: retrieval, LWS, and ranking are all point-wise, so even a perfect per-item model can't control what a slate looks like in combination. That's not a deficiency masked by blending — it's a decision no earlier stage makes. I'll add a paragraph making the preference-vs-composition distinction explicit, since it determines which levers are 'principled' for which problem."*

### Obs 2b — "Retrieval/LWS/ranking should figure out AI preference"
**Verdict: Covered by 2a + Obs 7.** True for preference in theory; the interventions that make it true in practice are his own §7 menu, which the doc absorbs. No separate reply.

### Obs 2c — "Bias toward principled, funnel-efficient approaches"
**Verdict: Already in draft. Ignore as a change.** It's the doc's stated posture (early-funnel density control at P0; filtering "as early and centrally as practical").

### Obs 3 (a–g) — Post-L2 re-ranking risks HF L2 offline-online correlation
**Verdict: Half-gap. Adjust — absorb as a measured budget.** His strongest technical point; absent from the diversification trade-offs table. Add: (1) correlation-risk row to blender trade-offs; (2) re-rank-rate-vs-control + the correlation measurement to the P0 eval list; (3) frame as **budget with breach-as-rollback**, converting the no-counterfactual argument from a veto into a number.
**Reply:** *"This is a fair and important risk, and I'll add it to the blender section's trade-offs explicitly. Concretely: the P0 diversification experiment will (1) log re-rank rate vs. control as a first-class metric, (2) pair with the offline-online correlation measurement you and Zisis are setting up, and (3) define an acceptable correlation budget up front, with breach as a rollback criterion. That gives us the measurement you're calling for — agreed there's no counterfactual after shipping, which is exactly why the measurement has to ride along with the first experiment rather than gate it."*

### Obs 4 — Combined experiments for marginal late-funnel impact
**Verdict: Mostly already in draft. Harden.** P0 eval already requires combined value between the two P0s; extend to a stacked arm over early-funnel model interventions.
**Reply:** *"Agreed, and the doc already requires this between the two P0s — the density-control evaluation includes 'incremental and combined value with blender diversification.' I'll extend it to cover early-funnel model interventions as well: a stacked design so late-funnel levers are credited only with their marginal impact on top of the early-funnel fixes."*

### Obs 5 — "Slate problem ≠ blending fix; do funnel analysis"
**Verdict: Already in draft (it's the P0's rationale). Harden + accept the diagnostic.** L1 density control *is* the upstream answer to "input to blending is genAI-heavy"; eval already measures candidate→served translation. Funnel analysis = PADS diagnostic that sets operating points.
**Reply:** *"Fully agreed — this is why the recommendation stack puts L1 density control at P0 alongside diversification: if the candidate set entering L2 is genAI-heavy, the fix is upstream composition control, not more blending. The funnel analysis is the right diagnostic to size where load actually concentrates, and its results should set the operating points for the L1 mechanism."*

### Obs 6 — Score sensitivity: (a) measure re-ranking (b) calibration (c) anti-over-sensitivity
**Verdict: (a) = Obs 3. (b) Already in draft — point to it. (c) Accept as small design requirement.**
**Reply:** *"(a) covered by the re-rank-rate metric above. (b) Agreed — this is already a core position of the doc: there's a full calibration section, and calibrated, versioned outputs are the stated launch standard for anything using score bands or probabilistic meaning. (c) Good add — I'll include banding/clamping of the score's influence in the diversification design requirements so small score shifts can't produce large ordering shifts."*

### Obs 7 (a–d) — Model interventions with lower debt (margin loss, VLM in-batch negatives, calibration-layer feature, sequence signals)
**Verdict: Adjust — absorb under the doc's rubric.** New third training-time subsection ("Objective and representation interventions") with the same trade-off table, Akshay's notifications results as evidence. Honest note: lower-debt in *serving complexity*, but training-time = retrain cycle per tuning iteration (the doc's own analysis) → complements, not substitutes.
**Reply:** *"These are strong additions, especially with the notifications evidence — I'll add them to the training-time section with the same trade-off treatment as the other levers, and I'm taking the follow-up with the HF LR and LWS teams. One framing note: these are lower-debt in serving complexity, but as training-time levers each tuning iteration is a retrain cycle, so they complement rather than replace the serving-time mechanisms — we should run them in parallel, not in sequence."*

### Obs 8a — Which CGs drive genAI load; affinity analysis
**Verdict: Accept.** Part of the funnel analysis; already James/Dafang's action item.
**Reply:** *"Good question — folding this into the funnel analysis as a per-CG load and affinity breakdown, so we can see which generators are sending genAI candidates to users with no affinity for them."*

### Obs 8b — "Controllable distribution in L1 utility?"
**Verdict: Already in draft — this IS the P0.** The quiet checkmate; say it plainly and kindly.
**Reply:** *"Yes — this is essentially what the doc proposes as P0: density control at L1 constrains the composition of the candidate set advancing to L2 by calibrated score band, which is controllable distribution before L2/blending. Glad we converged on the same mechanism — let's align on naming so we're describing one lever, not two."*

---

## Action items

- **AI 1–3 (PADS)**: §0 + funnel analysis answer 1–2; confirm Helium-prevalence (3) status.
- **AI 4 (Zisis correlation measurement)**: endorse — it's the instrument the Obs-3 budget depends on.
- **AI 5 (revisit priorities — James/QZ/Dafang/Dhruvil)**: answered by Obs-2 reply; offer to walk the rubric in the Wednesday sync rather than reopening async.
- **AI 6 (early-funnel questions — James/Dafang)**: accept; same work as funnel analysis + 8a.
- **AI 7 (blending-on-L1 stacked experiments — James/Dafang/Dhruvil)**: accept; = Obs-4 stacked design. Propose the 2×2 factorial rather than receive it.
- **AI 8 (Sameer — HF L2 interventions)** / **AI 9 (Rahul — HF blending PoCs)**: not James's; leave.
- **AI 10 (James — HF LR/LWS follow-up)**: accept; rides with the §7 additions.

## Still queued
- Michael's comments — not yet processed (James: Monday-morning editorial pass folds both).
- Qinglong `[QZ]` slot ask — still open in final draft; send today.
- §0 draft text + correlation-budget row — Leo offered to draft; not yet requested.
