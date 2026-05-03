# [LR] UPP Base Retriever — Release Cycle + Cross-Org Operational Model

**Author:** James Li (with input from Hongtao Lin, Rui Liu, Piyush Maheshwari, Zihao Chen, Jaewon Yang, Dimitra, Matt Chun)
**Status:** Working draft for working-group review
**Date:** 2026-04-25 (v4 — rewritten 2026-04-25b after grounded Wes Kao + Ethan Evans reviews)
**Companion doc:** [LR] [UPP Base Model] Release Cycle TDD (Matt Chun, ranking-side). This doc is the retriever counterpart and adds the cross-org operational/partnership layer.

---

## BLUF

This charter solves the scaling bottleneck for our ML infrastructure: it establishes a repeatable pattern that lets any surface team integrate the latest base retriever in 2–4 weeks instead of multi-month re-implementations.

> **Goal.** Align on a scalable post-launch ML handoff architecture that supports 4 surface teams running their own fine-tuning loops by Q4 2026.
>
> **Data.** Notifications is the V0 test case (handoff lands by end of May 2026). P2P and Search adapt the same template in Q3 and H2.
>
> **Ask.** Review the proposed accountability boundaries (§3, §7), the release cadence (§4), the version-maintenance defaults (§6), and the working-group baselines (§10). Flag blocking objections by [date TBD with working group].

---

## 1. Why this charter, why now

**This charter accelerates our current handoff process and removes the friction that's costing us velocity.** Right now, base team is still partly driving Notif fine-tuning (Hongtao on his ATG hat) while Rui is stepping up. Without an explicit handoff, that hybrid state persists — base team gets pulled into surface decisions that aren't ours to make, surface team doesn't fully own the surface, and the cost compounds the next time we change architecture.

**This charter is a one-time investment that saves three handoffs of work.** P2P adoption is in active co-design; Search adoption follows in H2. Treating Notif as a one-off means re-litigating the operational model three times. Treating Notif as the first instance of a model means each subsequent handoff inherits the precedent and ships faster.

The companion artifacts that this builds on:

- **[LR] [UPP Base Model] Release Cycle TDD** (Matt Chun, ranking) — the parallel for ranking. Structurally aligned on §4 Release Cycle and §6 Version Maintenance. Diverges where retriever-specific mechanics demand it.
- **[LR] UBR Design Doc** (Piyush, Jiaxing) — the technical architecture. Referenced; not duplicated.
- **[LR] Unified CLR: Conditioned User Sequence Module** — V-1 architecture reference.

---

## 2. Background

UPP base retriever (UBR) is in real operational adoption: V-1 is in active use on Notifications via ARF + fine-tuning (Rui Liu, Hongtao Lin), and V0 is in co-design with HF, Notif, and P2P as the first cross-surface release.

The first surface handoff — Notifications-on-Retrieval moving from "ATG-driven, James-shadowing" to "Notif-team-driven, James-out-of-execution-loop" — is targeted for April–May 2026.

---

## 3. Operational Model — Roles and Ownership Boundaries

After a surface adopts a base retriever release, ownership splits cleanly:

| Layer | Owner | What that means |
|-------|-------|-----------------|
| Foundation model + pretraining loop | Base team (UPP/ATG) | Cross-surface data composition, pretraining objective, scale-up, GPU serving |
| Base retriever architecture (UBR) | Base team, with surface co-design at architecture-change moments | Surface teams have a seat at architecture review; do not own architecture decisions |
| Cross-surface dataloader + feature plumbing | Base team | Multi-source DL, sampling-ratio decisions, feature remapping infra |
| Per-surface condition tower | Surface team (defined by surface, integrated by base team) | Each surface defines its condition features; base team integrates into pretraining |
| Surface fine-tuning recipe | Surface team | Which features to add at FT, FT loss config, FT data window, FT hyperparameters |
| Surface-specific labels (download, screenshot, revisitation, etc.) | Surface team | Add at FT stage; do not contaminate base pretraining |
| Launch decisions, A/B experiments, on-call | Surface team | Base team is on call for platform-level issues; surface team owns its funnel |
| Cross-surface eval infra (recall@k per surface) | Base team builds, surface teams interpret | Base team owns the metric infra; surface teams own how to use it |
| Architecture change reviews | Base team proposes, surface teams sign off | Default cadence: at each major release (V0 → V1 → V2…) |

**Operating principles behind this split:**

1. **Base team is a platform team, not a product team.** Base team's product is the pretrained model + tooling + release cadence. Surface team's product is the surface experience.
2. **Co-design at architecture changes; hands-off during steady-state.** When the base architecture changes, surface teams co-design. When surface team is iterating on its FT, base team is silent unless asked.
3. **Base team does not approve surface launches.** Surface launches go through surface team's normal launch gates.
4. **Credit propagates outward.** Surface team's wins are surface team's. Base team gets credit by being the platform that made surface wins possible — not by claiming surface wins.

### 3.5 What surface teams get (the partnership win)

Surface teams choose UPP because:

1. **Pretrained capability they couldn't build alone.** Cross-surface data, foundation model integration, scale — for free, with a 2-week SLA to start FT.
2. **Surface team owns the product.** Features, FT recipe, labels, launch decisions — all surface team's. Base team is platform, not gatekeeper.
3. **Quarterly upgrades.** New base retrievers ship 1–2× per quarter. Surface teams get fresh capability without doing the platform work.
4. **Co-design seat at architecture changes.** When the base architecture changes, surface teams have a named POC and decision rights on how it lands for their surface.
5. **Integration time drops from multi-month to 2–4 weeks.** Once the operational model is in steady state, the marginal cost of consuming a new base release is bounded.

---

## 4. Release Cycle (mechanics)

Structurally aligned with Matt's ranking-side TDD; retriever specifics noted.

**Cadence.** Base team releases a new UPP Base Retriever 1–2 times per quarter to start, calibrated empirically over the first 2–3 cycles. Lengthen the cycle when surface adoption is lagging — slow down to give surfaces time to absorb each release. Shorten the cycle when pinners are waiting on capability the next release ships and surface adoption is keeping pace.

**Version count.** We support at most 2 base retrievers in production (stable + nightly). We avoid maintaining multiple stable versions. When we deviate, the deviation is time-boxed (§6).

**Naming.**
- **Stable:** the current production base retriever, deployed across adopted surfaces.
- **Nightly:** the upcoming release in active development. Surface teams may evaluate against nightly during their FT iterations.
- **WIP branch:** the dev branch where IC contributions to the upcoming release stack up.

**IC contribution flow** (mirrors Matt's ranking TDD; retriever-specific tooling noted):

1. Confirm direction with a relevant POC (Piyush Maheshwari, Jaewon Yang, Hongtao Lin, Zihao Chen, or Matt Lawhon for cross-area calibration).
2. Iterate on top of the latest WIP version as your control branch. Add your change to the *Upcoming Release* table for the model. If no WIP version exists, create one.
3. Train control + treatment base retrievers. If an experimental branch exists for the WIP, that's your control. Ensure train/eval dates align. **Retriever launch command (TBD — to confirm in working group):** target a `ml_resources.mlenv.upp_base_retriever.configs.UBRTrainerConfigBundle` once the V0 codebase split lands; until V0, share Notif/HF codebase.
4. Validate the hypothesis on control/treatment, ping a POC for approval.
5. If another branch was approved during 2–4, repeat on the latest branch. Ping folks with unapproved-but-added changes for their timeline.

**Consumer team handling.**

1. Once a new base retriever release is available, the release doc is shared with consumer surface teams (Notif, HF, P2P, future Search) for review.
2. Latency testing is prioritized when increase is expected. Each surface runs its own latency test on its serving infra.
3. SLA: 2 weeks to begin a surface FT experiment with the updated base retriever. Help is available from base contributors for non-trivial pretraining changes.
4. Target: 2–4 weeks from experiment start to ship, pending LR changes and surface-specific FT recipe iteration.

**Why the cadence matters.** A published release cadence lets surface teams plan their FT iteration cycles around known release windows. Base team plans deprecations rather than reacting. Without it, surface teams wait on ad-hoc base updates and base team gets pulled into surface schedules.

---

## 5. Retriever-Specific Releases (V-1, V0)

> *Filled in by James + working group. Please correct anything wrong below.*

### V-1 (current)

- **Architecture:** [LR] Unified CLR: Conditioned User Sequence Module. HF current production model.
- **Components:** Condition tower per-surface, surface tower per-surface, shared user tower with conditioned user sequence transformer.
- **Adoption surface:** Notif. Notif ARF first-pretrains a base model and then fine-tunes — driven by Rui Liu + Hongtao Lin.
- **Operational state:** Live. This is the version Notif operates on for the imminent handoff.

### V0 (upcoming)

- **Architecture:** V-1 base + the cross-surface co-design changes from the UBR design doc (Piyush + Jiaxing). Each surface defines its own condition tower; surface tower per-surface; shared user tower; multi-source dataloader for cross-surface pretraining data.
- **Code change:** Notif and HF currently share codebase. V0 splits surface teams into separate FT codepaths so each surface adds features independently without coupling. **This unblocks surface teams from each other** — Notif's feature additions no longer affect HF's, and vice versa.
- **Adoption surfaces:** HF, Notif, P2P at V0 release.
- **Surface FT pattern:** Surface teams load the base model as a module into their FT codepath (Approach 2 in the UBR design doc — User Tower Module pattern). Surface team owns its condition tower, FT data, FT labels.

### Beyond V0

To be designed in subsequent release cycles. Likely candidates:
- Search adoption (with relevance gating).
- BMI adoption.
- Architectural ablations: unified backbone (transformer-only or sparse-MoE per UBR design doc); FM-as-backbone integration.

---

## 6. Version Maintenance — three scenarios, three defaults

The aspiration is one stable base model per category. The reality is sometimes more than one. The defaults below define what we do when reality diverges.

### Scenario A: Engagement / retention negative

**The situation.** Surface FT-on-new-base shows engagement or retention regression vs surface FT-on-old-base.

**Default.** Surface stays on old base. Base team treats the new release as a release-blocker — *the platform owns release-quality, not the surface.* Multi-version maintained ≤1 quarter. If the new base can't catch up within a quarter, base team rolls back the release or holds the surface back from upgrading until the next release.

**Decision owner.** Base team owns the release-or-block call. Surface team owns the adoption-or-skip call. If the call diverges, escalate base-EM ↔ surface-EM (James ↔ Dimitra for Notif).

### Scenario B: Engagement / retention neutral, infra cost negative

**The situation.** Surface FT-on-new-base is engagement-neutral and retention-neutral, but the new base costs more to serve.

**Default.** Don't ship. Base team must justify the new base on grounds other than engagement (reduced surface code complexity, simpler architecture, future-proofing for V1, cross-surface infrastructure consolidation). When those grounds are explicit, ship. When they're not, block on the next release that reduces infra cost. Multi-version maintenance is avoided — fix the infra cost or wait.

**Decision owner.** Base team owns the release-or-block call. Surface team owns adoption. Diverging calls escalate to base-EM ↔ surface-EM.

### Scenario C: Neutral overall (engagement, retention, infra)

**The situation.** Surface FT-on-new-base is fully neutral — no regression, no improvement, no infra delta.

**Default.** Ship. Even neutral A/B is positive when amortized over (a) maintenance cost reduction (one stable version vs two), (b) future improvements riding on the new base, (c) consistency with cross-surface platform thesis. Exception: when the new base requires non-trivial surface code change to adopt, hold for next release.

**Decision owner.** Surface team. Base team publishes the maintenance-cost benefit explicitly to inform the call.

### Cross-cutting principle

The goal of "exactly one stable base model per category" is aspirational, not absolute. When we deviate:
- Time-boxed (default: 1 quarter max per surface).
- Documented in the release doc with an explicit deprecation plan.
- Monitored — base team publishes maintenance cost monthly when more than one stable version exists.

---

## 7. Notif Handoff — Live Test Case

Notif is the first real test of the operational model. It serves as both the working precedent and the quality benchmark for the model itself.

### Accountability state, end of April 2026

| Role | Owner | Accountable for |
|------|-------|----------------|
| Notif FT execution lead | **Rui Liu** (Notif ML) | FT recipe selection, A/B test setup, launch decisions |
| Cross-team execution support | **Hongtao Lin** (ATG) | ATG-side support; **NOT** accountable for driving Notif FT decisions |
| Notif platform-engineering owner | **Dimitra** (Notif EM) | Surface-team capacity, broader Notif strategy |
| Base-team execution support | **Piyush Maheshwari** (TL), **James Li** (EM) | Platform tooling and base model release cadence; **NOT** accountable for Notif FT execution |

### "Clean handoff" criteria — by end of May 2026

1. Notif team has driven at least one full FT iteration end-to-end (data → train → eval → launch decision) without base-team execution involvement.
2. Surface Tower v2 result has landed (positive or negative) with Notif-team-led analysis.
3. Shared partnership doc has been Notif-team-updated for at least 4 consecutive weeks.
4. Weekly sync has had at least 2 weeks where Notif team drove the agenda end-to-end.
5. Notif team (Rui + Dimitra + Zhenyu) and base team (James + Hongtao + Piyush) have a written 1-pager agreeing on roles, with base-team execution responsibility explicitly removed.
6. Dimitra has named the next FT initiative for Notif herself, without prompting.

If 5 of 6 land, handoff is clean. If 3–4 land, handoff is in progress. If <3 land, the operational model needs revisiting before the P2P handoff is scoped.

### How we get there — week by week

1. **Week 1 (May 5):** James + Dimitra meet to align on the criteria above and the role split. James drafts the 1-pager (criterion 5).
2. **Week 2:** Rui leads the first weekly sync agenda end-to-end. Hongtao supports but does not drive.
3. **Week 3:** Surface Tower v2 result lands. Notif team owns the analysis writeup. James + Piyush review only if asked.
4. **Week 4:** Notif team updates shared doc independently. James does not write in the doc this week.
5. **End of May:** Dimitra names the next FT initiative without prompting; James stops attending the weekly sync.

---

## 7.5 Required content for surface-team operational plans (review checklist)

> Review checklist for the *Notif Retrieval FT V0 Operational Plan* (Piyush Maheshwari, Rui Liu, Devin Kreuzer, Hongtao Lin) and a spec for future P2P / Search surface-team ops docs.

This charter defines the **cross-org governance layer** (§§3–8). Each surface team produces a complementary **operational plan** covering surface-team-side mechanics: who runs what within the surface team, how failures are handled, what the contract with base team is. The Notif V0 ops plan is the first instance — and reviewing it against this checklist surfaced significant gaps. Captured here as a spec for both the immediate Notif V0 doc revision AND future adopters.

### The single most useful reframe (do this first)

The current Notif V0 doc reads as a productionization sketch + future-flexibility memo. It's authors-narrating (*"we will set up ARF, manually retrain"*), not a two-team operational contract.

**Reshape it from *"what we will do"* to *"what notif team owns / what base team owns / what the contract is between us / what happens when things break."*** That single shape change forces most of the missing content below to surface naturally.

### Required sections (ranked by priority)

#### 1. Ownership / RACI in the post-handoff state
The single biggest gap. The current draft says *"we will set up a base model ARF with help from the notif team"* — never defines who *we* is, never defines steady-state ownership. This charter's §3 establishes the cross-org RACI matrix; the surface ops plan must specify the within-surface and contract-with-base details:
- Who owns base retraining cadence (Rui? Hongtao on ATG hat? Base team?)
- Who owns notif FT retraining cadence
- Named POCs on each side
- Go/no-go on accepting a new base release into notif's pipeline
- On-call routing (base team for platform-level; notif for funnel — but who specifically?)

#### 2. Failure modes + rollback
**Zero coverage in the V0 draft. Operational table stakes.**
- What happens if a new base retrain regresses notif metrics?
- Rollback mechanism (revert base? revert FT? both?)
- Rollback SLA
- Break-glass path
- Comms protocol when something breaks
- Behavior when base model is unavailable during a notif retrain

#### 3. Versioning + compatibility contract
The V0 draft asserts: *"we only load the lower layers weights of base model during finetuning. The feature crossing and output layers don't need to be the same as base."* That's a load-bearing claim with no contract behind it:
- What guarantees lower-layer stability across base versions?
- If base team changes lower-layer architecture, does notif FT auto-break? How is that surfaced?
- Base model version tracking + lineage
- Compatibility matrix: which notif FT versions work with which base versions?
- Deprecation policy when base ships a breaking change

#### 4. Make the "Future Development Plan" section concrete (currently hollow)
The V0 draft lists three flexibility examples but no *HOW*:
- *"Updating notif training data is not blocked"* — what's the workflow? Self-serve? PR to where? Where does the data live? Approval needed?
- *"Adding new features can be tried on notif surface tower first"* — what's the API/contract for adding features at FT stage? Who reviews? How does it get promoted to base if it works cross-surface?
- *"New model architectures can be tried on notif directly"* — if architecture diverges, how is base layer alignment maintained? What's the divergence policy? When does notif need to coordinate with base team?

#### 5. Eval + sign-off bar
What's the gate to promote a new FT model to prod?
- Required metrics (recall@k offline? online A/B? Both?)
- Bar / threshold per metric
- Who signs off
- Behavior on regression
- Eval suite / golden sets

#### 6. Cadence + triggers
The V0 draft mentions *"biweekly ARF cadence"* in passing. Missing:
- Actual schedule (every other Monday? Aligned with notif's deploy schedule?)
- Triggers for off-cycle retrain (drift? feature change? new architecture?)
- Lag between base retrain and FT retrain
- Notif's deploy-schedule alignment

#### 7. Migration plan from current state to steady state
The V0 draft jumps straight to *"we will productionize."* Missing:
- Current state (V-1 ARF + FT per §2)
- Migration sequence
- Cutover mechanism
- Bake-in / parallel-run period before full cutover
- Validation gates at each milestone

#### 8. Manual-retrain-of-base runbook
*"Before [base ARF is] implemented, we will manually retrain the base model which is acceptable given the biweekly ARF cadence."* — that's a sentence, not a runbook:
- Who runs the manual retrain
- What steps
- Time required
- Validation before promotion
- Behavior on failure
- When does the manual retrain stop being needed (when does ARF land?)

### Lower-priority but worth flagging in the V0 doc

- **Cross-surface implications** — notif is one of multiple surfaces. The V0 draft doesn't acknowledge that notif-team decisions might cascade or conflict with base team's plans for HF / P2P / Search.
- **Cost / resource accounting** — manual base retrains aren't free. Who pays? Quota allocation?
- **SLOs** — latency, throughput, freshness, availability targets for notif retrieval.
- **Monitoring + drift detection** — what's the ongoing health check? Drift on inputs, base, FT? Alerting?
- **Coordination model between teams** — sync cadence, comms channel, escalation path beyond named POCs (this charter's §8 establishes the cross-org pattern; surface ops plan should specify the partnership-level instance).
- **June OOO coverage** — if something breaks during James's June OOO, who responds? Not the engineer's responsibility to put in their doc, but worth flagging as a contract item the broader doc must cover.

### How this checklist evolves

When P2P and Search produce their own surface ops plans, this checklist should be the starting spec. After two more surfaces ship plans against it, revisit and prune anything that turned out not to be load-bearing. **The goal is a reusable template, not eight unique surface ops docs.**

---

## 8. Coordination Mechanisms

**Steady-state per surface partnership:**

- **One shared doc** with current state, recent FT results, open questions, named owners on both sides. Updated weekly by the surface team. Base team is read-only unless asked.
- **One weekly sync.** 30 minutes max. Surface team drives the agenda. Base team listens unless asked.
- **One Slack channel** per partnership. Async-first; replies expected within one business day.
- **Quarterly architecture review** — base team presents proposed platform changes, surface teams give input, decisions documented.

**Architecture-change moments (release cycles):**

- **Co-design working sessions** for the duration of the architecture change. Named POCs from each surface team. Time-boxed: 2–6 weeks of intensive work, then back to steady-state.
- **Shared design doc** with named co-authors from each side (the UBR design doc with Piyush + Jiaxing as co-authors is the template).
- **Decisions made at the working session level**, not escalated to directors unless co-authors disagree. This is the test of whether co-design is real or theater.

**Escalation path:**

- Surface IC ↔ base IC — first line, async.
- Surface ML lead ↔ base TL — second line, sync as needed.
- Surface EM ↔ base EM — third line, only when ML-lead level is stuck.
- Surface director ↔ Dylan — fourth line, only when EM-level can't unblock and the issue is structural.

If escalation reaches director level more than once per quarter, the operational model is broken and needs structural fix, not another escalation.

### 8.5 Monthly Handoff Review (MHR) — the mechanism that keeps this alive

The operational model is only as durable as the mechanism that enforces it. Once steady state lands, the base team runs a **Monthly Handoff Review** to keep all surface partnerships visible and prevent silent drift.

**Format:** 30-minute monthly meeting, base team chairs. Each adopted surface gives a 5-minute scorecard update.

**Standard scorecard per surface:**
- Stable + nightly version status (which surface is on which version).
- Active release cycle progress (V0 → V1 → V2 timeline).
- Surface partnership health: last sync date, last shared-doc update date, any tripwire signals fired.
- Cost of multi-version maintenance, when applicable (per §6 cross-cutting principle).

**Audience:** working group + leads. **Distribution:** standardized scorecard logged to the partnership shared doc. **Owner:** base team TL.

**Why the MHR matters.** Without a forcing mechanism, the operational model becomes shelfware. The MHR is the difference between "we wrote a charter" and "we run a platform." It surfaces drift early and gives leads (Dylan, Dimitra, Sai) a single monthly artifact to review without needing to chase status.

---

## 9. Tripwires (any one fires → re-engage)

These apply both during release cycles and in post-handoff steady-state:

1. **Two-week stall on any active surface workstream.** Silence is the earliest signal of a hidden blocker.
2. **Surface team asks base team to make a surface-level decision** ("should we launch?"). If they're asking, the handoff is not done. Coach them through the decision; do not make it for them.
3. **Surface metric regression that surface team cannot diagnose.** Base team is on call for *platform-level* issues, not surface debugging. If surface team can't diagnose, the handoff was premature on tooling/observability.
4. **Cross-surface architectural inconsistency.** If two surfaces start diverging on architecture in ways that fracture the platform thesis, base team re-engages on architecture review, not surface-by-surface negotiation.
5. **MHR scorecard skipped or stale.** If the cadence slips, base team is at risk of being framed as a tools team rather than a platform team. Hold cadence even when the agenda is light.
6. **More than 2 stable versions for >1 quarter.** Per §6; deviation must be time-boxed.

---

## 10. Working Group — proposed baselines

Each item below is a **proposed baseline** with one alternative we considered. We will proceed with these baselines unless data, production experience, or surface-team capacity proves any of them block downstream surface integrations.

> **Flag blocking objections by [date TBD with working group].** Disagree-and-commit applies after that date — the operational model needs to be in motion before Notif handoff lands at end of May.

| # | Proposed baseline | Alternative considered |
|---|------------------|----------------------|
| 1 | §6 Scenario A: surface stays on old base; multi-version maintained ≤1 quarter; rollback required if new base can't catch up. | Block surface from upgrading until base is fixed. More conservative; surface friction. |
| 2 | §6 Scenario B: don't ship engagement-neutral / infra-negative releases by default; require explicit non-engagement justification. | Allow architectural-future-proofing as sufficient ship reason even on surface-team disagreement. |
| 3 | §6 Scenario C: ship engagement-neutral / infra-neutral releases by default; surface team migrates absent non-trivial code-change adoption cost. | Surface-team-discretion default ("don't migrate just for migration's sake"). |
| 4 | §7 clean-handoff criteria: 6 criteria; 5 of 6 land = clean handoff for Notif by end of May. | Smaller criteria set (3–4) with all required. |
| 5 | §4 release cadence: 1–2 base retriever releases per quarter. | Same cadence as ranking (set by Matt's TDD); or empirical-only ("first cycle, then calibrate"). |
| 6 | §8 escalation path: IC → ML-lead → EM → director, with director-escalation rare (<1/quarter). | Skip ML-lead step (IC → EM) for tighter loops. |
| 7 | §5 V0 codebase split: Notif and HF split into separate FT codepaths at V0. | Keep shared longer; split at V1 or later. |
| 8 | §9 tripwire set: 6 tripwires above. | Add a tripwire for "surface team launch decisions diverge from base team's stated direction." |

---

## 11. Open questions for resolution

1. **Where does this doc live long-term?** Likely Confluence in the UPP space, alongside Matt's ranking TDD as a sibling page.
2. **Cadence for the quarterly architecture review** — and who chairs? Default proposal: base team chairs; all surface ML leads attend.
3. **Reflex / Anticipation Vision interaction.** Reflex is downstream of UPP, not a surface partner. Treat separately for now; flag for revisit when the boundary blurs.
4. **Naming consistency.** UBR / UPP CLR / Base CLR — Zihao's terminology in the March 2026 Wednesday meeting was "Base CLR" for current HF and "UPP CLR" for the co-designed redesign. Working group should converge on one term per release.
5. **Per-surface engineering details this doc punts on:** github repo ownership, on-call alarm routing, bug-report routing, cross-team PR review. These get filled in per-partnership in the shared partnership doc (§8), not standardized at this level. Working group should confirm.
6. **Confirmed objection date for §10.** Set with working group at v4 circulation.

---

## 12. What this doc does NOT do

- It does not prescribe specific FT recipes, training data windows, or hyperparameters. Those live in surface-team-owned recipes.
- It does not prescribe specific architecture decisions. Those live in the UBR design doc.
- It does not replace the launch process. Launches go through surface team's normal launch gates.
- It does not assume Search and P2P will adopt the same model verbatim. Specific adaptations are expected (relevance gating for Search; query-pin context for P2P). The principles transfer; the specifics adapt.
- It does not replace trust. Sai's proactive engineer staffing for P2P is worth more than any operational model document. The model lives inside trust relationships, not instead of them.
