# [LR] UPP Base Retriever — Release Cycle + Cross-Org Operational Model

**Author:** James Li (with input from Hongtao Lin, Rui Liu, Piyush Maheshwari, Zihao Chen, Jaewon Yang, Dimitra, Matt Chun)
**Status:** Working draft for working-group review
**Date:** 2026-04-25
**Companion doc:** [LR] [UPP Base Model] Release Cycle TDD (Matt Chun, ranking-side). This doc is the retriever counterpart and adds the cross-org operational/partnership layer.

> **What this doc is for.** This is a working draft to align the UPP Base Retriever working group on (1) how we run the release cycle, (2) how the partnership between base and surface teams operates after a surface adopts a base retriever, and (3) what defines a "clean" surface handoff using Notif as the live first case. **Please push back, add scenarios I missed, and propose alternative answers in-line.** The places I most want input on are flagged in **§9 Working Group Input** at the bottom.

---

## 1. Background

UPP base retriever (UBR) is approaching real operational adoption: V-1 is in active use on Notifications via ARF + fine-tuning (Rui Liu, Hongtao Lin), and V0 is in co-design with HF, Notif, and P2P as the first cross-surface release.

The first surface handoff — **Notifications-on-Retrieval moving from "ATG-driven, James-shadowing" to "Notif-team-driven, James-out-of-execution-loop"** — is targeted for April–May 2026. This handoff is the precedent. P2P and Search will follow in Q3 and H2 2026 respectively, conditional on UBR co-design success.

We need an operational model for two reasons:

1. **The release cycle is moving from ad-hoc to scheduled.** Without a published cadence, surface teams can't plan FT iterations, and base team can't plan deprecations. Matt Chun's ranking TDD is the parallel; this doc is the retriever counterpart, structurally aligned where it makes sense.
2. **The base–surface partnership shape needs to be explicit.** Right now Notif is partly base-team-driven on FT (Hongtao on his ATG hat). Rui is stepping up. Without an explicit handoff definition, there's risk of (a) Notif team thinking the handoff is done while base team still feels operational responsibility, or (b) the reverse. The cost of getting this wrong compounds across P2P and Search.

This doc is companion to:

- **[LR] [UPP Base Model] Release Cycle TDD** (Matt Chun, ranking) — the parallel for ranking. Structurally aligned on §3 Release Cycle and §5 Version Maintenance. Diverges where retriever-specific mechanics demand it.
- **[LR] UBR Design Doc** (Piyush, Jiaxing) — the technical architecture. This doc references it; doesn't duplicate it.
- **[LR] Unified CLR: Conditioned User Sequence Module** — V-1 architecture reference.

---

## 2. Operational Model — Roles and Ownership Boundaries

After a surface adopts a base retriever release, ownership splits cleanly:

| Layer | Owner | What that means |
|-------|-------|-----------------|
| Foundation model + pretraining loop | Base team (UPP/ATG) | Cross-surface data composition, pretraining objective, scale-up, GPU serving |
| Base retriever architecture (UBR) | Base team, with surface co-design at architecture-change moments | Surface teams have a seat at architecture review; do not own architecture decisions |
| Cross-surface dataloader + feature plumbing | Base team | Multi-source DL, sampling-ratio decisions, feature remapping infra |
| Per-surface condition tower | Surface team (defined by surface, integrated by base team) | Each surface defines its condition features; base team integrates into pretraining |
| Surface fine-tuning recipe | Surface team | Which features to add at FT, FT loss config, FT data window, FT hyperparameters |
| Surface-specific labels (download, screenshot, revisitation, etc.) | Surface team | Add at FT stage; do not contaminate base pretraining |
| Launch decisions, A/B experiments, on-call | Surface team | Base team gets pinged on platform-level issues; surface team owns their funnel |
| Cross-surface eval infra (recall@k per surface) | Base team builds, surface teams interpret | Base team owns the metric infra; surface teams own how to use it for launch decisions |
| Architecture change reviews | Base team proposes, surface teams sign off | Default cadence: at each major release (V0 → V1 → V2…) |

**Operating principles behind this split:**

1. **Base team is a platform team, not a product team.** Base team's product is the pretrained model + tooling + release cadence. Surface team's product is the surface experience.
2. **Co-design at architecture changes; hands-off during steady-state.** When the base architecture changes (new condition modeling, new pretraining objective, new feature plumbing), surface teams co-design. When surface team is iterating on its FT, base team is silent unless asked.
3. **Base team does not approve surface launches.** Surface launches go through surface team's normal launch gates.
4. **Credit propagates outward.** Surface team's wins are surface team's. Base team gets credit by being the platform that made surface wins possible — not by claiming surface wins.

---

## 3. Release Cycle (mechanics)

Structurally aligned with Matt's ranking-side TDD; retriever specifics noted.

**Cadence:** Aim to release a new UPP Base Retriever 1–2 times per quarter to start. Calibrate based on the first 2–3 cycles. Lengthen if surface adoption lags; shorten if pinner-first urgency is clear and adoption is healthy.

**Version count:** Target supporting **at most 2 base retrievers at a time (stable + nightly)**. A primary goal is to avoid maintaining multiple stable versions. We acknowledge this won't always be achievable — see §5 for what we do when it isn't.

**Naming:**
- **Stable:** the current production base retriever, deployed across adopted surfaces.
- **Nightly:** the upcoming release in active development. Surface teams may choose to evaluate against nightly during their FT iterations.
- **WIP branch:** the dev branch where IC contributions to the upcoming release stack up.

**IC contribution flow (mirrors Matt's ranking TDD; retriever-specific tooling noted):**

1. **Confirm direction with a relevant POC** (Piyush Maheshwari, Jaewon Yang, Hongtao Lin, Zihao Chen, or Matt Lawhon for cross-area calibration).
2. **Iterate on top of the latest WIP version** as your control branch. Add your change to the *Upcoming Release* table for the model in question.
   - If no WIP version exists yet, create one.
3. **Train control + treatment base retrievers.**
   - If an experimental branch already exists for the WIP version, that's your control.
   - Ensure train/eval dates align across control and treatment.
   - **Retriever launch command (TBD — to confirm in working group):** target a `ml_resources.mlenv.upp_base_retriever.configs.UBRTrainerConfigBundle` or equivalent once the V0 codebase split lands. Until V0, share Notif/HF codebase.
4. **Validate the hypothesis** on the control/treatment, ping a POC for approval.
5. **If another branch was approved during 2–4, repeat** on the latest branch. Ping folks with unapproved-but-added changes for their timeline.

**Consumer team handling:**

1. Once a new base retriever release is available, **release doc shared with consumer surface teams** (Notif, HF, P2P, future Search) for review.
2. **Latency testing prioritized** if increase is expected. Each surface runs its own latency test on its serving infra.
3. **SLA: ~2 weeks to begin a surface FT experiment** with the updated base retriever. Help available from base contributors for non-trivial pretraining changes.
4. **Target: 2–4 weeks from experiment start to ship**, pending LR changes and surface-specific FT recipe iteration.

---

## 4. Retriever-Specific Releases (V-1, V0)

> **Filled in by James + working group. Please correct anything wrong below.**

### V-1 (current)

- **Architecture:** [LR] Unified CLR: Conditioned User Sequence Module. HF current production model.
- **Components:** Condition tower per-surface, surface tower per-surface, shared user tower with conditioned user sequence transformer.
- **Adoption surface:** **Notif.** Notif ARF currently first-pretrains a base model and then fine-tunes — driven by **Rui Liu** + **Hongtao Lin**.
- **Operational state:** Live. This is the version Notif is operating on for the imminent handoff.

### V0 (upcoming)

- **Architecture:** Same V-1 base + the cross-surface co-design changes from the UBR design doc (Piyush + Jiaxing). Each surface defines its own condition tower; surface tower per-surface; shared user tower; multi-source dataloader for cross-surface pretraining data.
- **Code change:** Notif and HF currently share codebase. **V0 will split surface teams into separate FT codepaths** so each surface can independently add features without coupling.
- **Adoption surfaces:** **HF, Notif, P2P** at V0 release.
- **Surface FT pattern:** Surface teams **load the base model as a module** into their FT codepath (Approach 2 in the UBR design doc — User Tower Module pattern). Surface team owns its condition tower, FT data, FT labels.

### Beyond V0

To be designed in subsequent release cycles. Likely candidates surfaced in working group:
- Search adoption (with relevance gating).
- BMI adoption.
- Architectural ablations: unified backbone (transformer-only or sparse-MoE per UBR design doc); FM-as-backbone integration.

---

## 5. Version Maintenance Policy — Matt Chun's Three Scenarios

> **This is the section I most want working group to push on.** Each scenario below has a *proposed* default decision. The defaults are starting points, not final answers.

When a surface FTs on the latest base retriever and runs an A/B test, three outcomes are operationally distinct:

### Scenario A: Engagement / retention negative

**Surface FT-on-new-base shows engagement or retention regression vs surface FT-on-old-base.**

**Proposed default:** Surface stays on old base. Base team does not deprecate the old base. Base team treats this as a release-blocker and either fixes the next release or marks the new base as not-ready-for-this-surface.

**Multi-version maintenance:** *Yes, temporarily*, but with a hard deadline. We do not allow more than 2 stable base retrievers in production for >1 quarter. If the new base can't catch up within a quarter, we either roll back the release or hold the surface back from upgrading until the next release.

**Decision owner:** Base team (release-level), surface team (adoption-level), Dylan / Dimitra escalation if disagreement.

### Scenario B: Engagement / retention neutral, infra cost negative

**Surface FT-on-new-base is engagement-neutral and retention-neutral, but the new base costs more to serve.**

**Proposed default:** **Don't ship by default.** Base team must justify the new base on grounds other than engagement (e.g., reduced surface code complexity, simpler architecture, future-proofing for V1, cross-surface infrastructure consolidation). If those grounds exist and are explicit, ship. If they don't, block on the next release that reduces infra cost.

**Multi-version maintenance:** Avoid. If the new base is engagement-neutral, the cost-of-multi-version maintenance dominates. Either fix the infra cost or wait.

**Decision owner:** Base team owns the release-or-block call. Surface team owns the adoption-or-skip call. If the call diverges, resolve at base-EM ↔ surface-EM (James ↔ Dimitra for Notif).

### Scenario C: Neutral overall (engagement, retention, infra)

**Surface FT-on-new-base is fully neutral — no regression, no improvement, no infra delta.**

**Proposed default:** **Ship by default.** Even neutral A/B is positive when amortized over: (a) maintenance cost reduction (one stable version vs two), (b) future improvements riding on the new base, (c) consistency with cross-surface platform thesis. The exception: if the new base requires non-trivial surface code change to adopt, the cost of adoption may exceed the maintenance benefit. In that case, hold for next release.

**Multi-version maintenance:** No. Default is to migrate.

**Decision owner:** Surface team. Base team should publish the maintenance-cost benefit explicitly to inform the call.

### Cross-cutting principle

**We acknowledge the goal of "exactly one stable base model per category" is aspirational, not absolute.** When we deviate, it should be:
- Time-boxed (default: 1 quarter max per surface).
- Documented in the release doc with an explicit deprecation plan.
- Monitored for cost — base team publishes maintenance cost monthly when >1 stable version exists.

---

## 6. Notif Handoff — Live Test Case

The Notif handoff is the first real test of this operational model. We're using it both as a working precedent and as a quality benchmark for the model itself. If the handoff lands cleanly, the same template applies to P2P (Q3) and Search (H2).

### Current state

- **V-1 in production on Notif.** Notif ARF pretrains a base model, then fine-tunes. Driven by Rui Liu + Hongtao Lin.
- **Hongtao's role:** Currently driving FT on the ATG side. Notif FT confirmed as Hongtao's major Q2 project.
- **Rui's role:** Stepping up on FT iterations from the Notif ML side. Healthy-handoff signal.
- **Surface Tower v2 A/B in flight.** Result will inform whether handoff timeline holds.

### "Clean handoff" criteria (proposed — please push back)

For the handoff to be considered clean by end of May 2026:

1. Notif team has driven at least one full FT iteration end-to-end (data → train → eval → launch decision) without base-team execution involvement.
2. Surface Tower v2 result has landed (positive or negative) with Notif-team-led analysis.
3. Shared partnership doc has been Notif-team-updated for at least 4 consecutive weeks.
4. Weekly sync has had at least 2 weeks where Notif team drove the agenda end-to-end.
5. Notif team (Rui + Dimitra + Zhenyu) and base team (James + Hongtao + Piyush) have a written 1-pager agreeing on roles, with base-team execution responsibility explicitly removed.
6. Dimitra has named the next FT initiative for Notif herself, without prompting.

If 5 of 6 land, handoff is clean. If 3–4 land, handoff is in progress. If <3 land, the operational model needs revisiting before the P2P handoff can be scoped.

---

## 7. Coordination Mechanisms

**Steady-state per surface partnership:**

- **One shared doc** with current state, recent FT results, open questions, named owners on both sides. Updated weekly by the surface team. Base team is read-only unless asked.
- **One weekly sync.** 30 minutes max. Surface team drives the agenda. Base team listens unless asked.
- **One Slack channel** per partnership. Async-first; replies expected within one business day, not faster.
- **Quarterly architecture review** — base team presents proposed platform changes, surface teams give input, decisions documented.

**Architecture-change moments (release cycles):**

- **Co-design working sessions** for the duration of the architecture change. Named POCs from each surface team. Time-boxed: 2–6 weeks of intensive work, then back to steady-state.
- **Shared design doc** with named co-authors from each side (the UBR design doc with Piyush + Jiaxing as co-authors is the template).
- **Decisions made at the working session level**, not escalated to directors unless co-authors disagree. This is the test of whether co-design is real or theater.

**Escalation path:**

- Surface IC ↔ base IC — first line, async.
- Surface ML lead ↔ base TL — second line, sync as needed.
- Surface EM ↔ base EM — third line, only when ML-lead level is stuck.
- Surface director ↔ Dylan — fourth line, only when EM-level can't unblock and the issue is structural (resource conflict, scope dispute, milestone risk).

If escalation reaches director-level more than once per quarter, the operational model is broken and needs structural fix, not another escalation.

---

## 8. Tripwires (any one fires → re-engage)

These apply both to the active release cycle and to a post-handoff steady-state:

1. **Two-week stall on any active surface workstream.** Silence is the earliest signal of a hidden blocker.
2. **Surface team asks base team to make a surface-level decision** ("should we launch?"). If they're asking, they're not yet owning. Either coach them through it or accept the handoff isn't done.
3. **Surface metric regression that surface team can't diagnose.** Base team should be on-call for *platform-level* issues, not surface debugging. If surface team can't diagnose, the handoff was premature on tooling/observability.
4. **Cross-surface architectural inconsistency.** If two surfaces start diverging on architecture in ways that fracture the platform thesis, base team must re-engage on architecture review, not surface-by-surface negotiation.
5. **Quarterly architecture review skipped.** If the cadence slips, base team is at risk of being framed as a tools team rather than a platform team. Hold cadence even if the agenda is light.
6. **More than 2 stable versions for >1 quarter.** Per §5; deviation must be time-boxed.

---

## 9. Working Group Input — places I most want pushback

> **The following are the highest-leverage places where I want working-group input. If you have an opinion on any of these, please add it inline or reply on the thread.**

1. **§5 Scenario A (engagement-negative).** Is "stays on old base, time-boxed multi-version" the right default? Or is there a case for blocking the surface from upgrading until the new base is fixed?
2. **§5 Scenario B (neutral + infra-negative).** Is "don't ship by default" too conservative? Should base team be able to override on architectural-future-proofing grounds even when surface team disagrees?
3. **§5 Scenario C (neutral overall).** Is "ship by default" too aggressive? Surface teams may have a legitimate "we don't want to migrate just for migration's sake" position.
4. **§6 clean-handoff criteria for Notif.** Are the 6 criteria the right set, and is "5 of 6" the right threshold? In particular: criterion 5 (written 1-pager agreeing on roles, base-team execution removed) is unusual — is this overengineered or appropriate?
5. **§3 release cadence.** 1–2 per quarter — is that right for retriever specifically? Ranking has its own pace; retriever could go faster or slower.
6. **§7 escalation path.** Does the IC → ML-lead → EM → director ladder match how Notif (and later P2P) actually operate? Is anyone in this chain redundant or missing?
7. **§4 V0 codebase split.** The decision to split Notif/HF into separate codepaths at V0 is in the UBR design doc; is it the right call, or should we keep them shared longer?
8. **§8 tripwires.** Is anything missing? Specifically: should there be a tripwire on "surface team's launch decisions diverge from base team's stated direction"?

---

## 10. Open questions for resolution

1. **Where does this doc live long-term?** Likely Confluence in the UPP space, but exact location TBD. Should it sit alongside Matt's ranking TDD as a sibling page?
2. **Cadence for the quarterly architecture review** — and who chairs? Default proposal: base team chairs, all surface ML leads attend.
3. **How does this operational model interact with Reflex / Anticipation Vision** — Reflex is downstream of UPP, not a surface partner. Treat separately for now, but flag for revisit if the boundary blurs.
4. **Naming consistency:** UBR / UPP CLR / Base CLR — Zihao's terminology in the March 2026 Wednesday meeting was "Base CLR" for current HF and "UPP CLR" for the co-designed redesign. The UBR design doc uses "UBR" / "Unified Cross Surface Retrieval." Working group should converge on one term per release.
5. **Per-Surface engineering details** that this doc punts on: who owns the github repo, who's on-call for what alarms, where do bug reports go, how PR review works across teams. The intent is that these get filled in per-partnership in the shared partnership doc (§7), not standardized at this level. Working group should confirm.

---

## 11. What this doc does NOT do

- It does not prescribe specific FT recipes, training data windows, or hyperparameters. Those live in surface-team-owned recipes.
- It does not prescribe specific architecture decisions. Those live in the UBR design doc.
- It does not replace the launch-process. Launches go through surface-team's normal launch gates.
- It does not assume Search and P2P will adopt the same model verbatim. Specific adaptations expected (relevance gating for Search; query-pin context for P2P). The principles transfer; the specifics adapt.
- It does not replace trust. Sai's proactive engineer staffing for P2P is worth more than any operational model document. The model lives inside trust relationships, not instead of them.
