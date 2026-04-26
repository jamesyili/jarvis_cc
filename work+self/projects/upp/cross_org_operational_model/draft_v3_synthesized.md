# [LR] UPP Base Retriever — Release Cycle + Cross-Org Operational Model

**Author:** James Li (with input from Hongtao Lin, Rui Liu, Piyush Maheshwari, Zihao Chen, Jaewon Yang, Dimitra, Matt Chun)
**Status:** Working draft for working-group review
**Date:** 2026-04-25
**Companion doc:** [LR] [UPP Base Model] Release Cycle TDD (Matt Chun, ranking-side). This doc is the retriever counterpart and adds the cross-org operational/partnership layer.

---

## What changes when this doc lands

By Q4 2026, UPP runs on a quarterly release cadence with 2–4 surface teams operating their own fine-tuning loops. Notifications goes first this quarter; P2P and Search follow as their co-design work matures.

Specifically:

- **Surface teams own their fine-tuning end-to-end.** Feature choice, FT recipe, A/B configuration, launch decision, on-call. Base team is platform, not gatekeeper.
- **Base team owns the platform.** Release cadence (1–2 base retrievers per quarter, 2 stable versions max), base architecture, cross-surface dataloader, infra.
- **Co-design at architecture changes; hands-off in steady-state.** Surface teams have a seat at architecture review; do not own architecture decisions.
- **Notif is the first instance.** By end of May, Rui drives Notif FT decisions, James and Hongtao step out of the execution loop, and the formal release cadence is published. P2P and Search adapt the same template.

This is the retriever counterpart to Matt Chun's ranking release-cycle TDD, structurally aligned where it makes sense, and extending into the cross-org operational layer that ranking will also need.

---

## For leads (Dylan, Dimitra, Sai, Matt Chun)

If you read three lines of this doc, read these:

- **The model.** Base team owns the platform (release cycle, architecture, infra). Surface teams own their fine-tuning, launches, and on-call. Co-design at architecture changes; hands-off at steady-state.
- **The cadence.** 1–2 base retriever releases per quarter; 2 stable versions max; 2-week SLA for surface adoption start; 2–4 weeks from experiment start to ship.
- **The first test.** Notif handoff lands clean by end of May 2026. If it does, P2P and Search use the same template.

---

## 1. Anticipating two objections

> **"Why a charter when we just need a Notif handoff plan?"**
>
> Because Notif is the first of three handoffs in 12 months. P2P adoption is in active co-design; Search adoption follows in H2 2026. Treating Notif as a one-off means re-litigating the operational model three times. Treating it as the first instance of a model means each subsequent handoff inherits the precedent.

> **"Doesn't this already work in practice?"**
>
> In practice, base team is still partly driving Notif FT (Hongtao on his ATG hat). Rui is stepping up but does not yet own launch decisions. Without an explicit handoff, base team keeps getting pulled into surface decisions, and surface team does not fully own the surface. The cost shows up next time we change architecture and discover surface team had not been making the FT decisions on its own.

---

## 2. Background

UPP base retriever (UBR) is in real operational adoption: V-1 is in active use on Notifications via ARF + fine-tuning (Rui Liu, Hongtao Lin), and V0 is in co-design with HF, Notif, and P2P as the first cross-surface release.

The first surface handoff — Notifications-on-Retrieval moving from "ATG-driven, James-shadowing" to "Notif-team-driven, James-out-of-execution-loop" — is targeted for April–May 2026.

This doc is companion to:

- **[LR] [UPP Base Model] Release Cycle TDD** (Matt Chun, ranking) — the parallel for ranking. Structurally aligned on §4 Release Cycle and §6 Version Maintenance. Diverges where retriever-specific mechanics demand it.
- **[LR] UBR Design Doc** (Piyush, Jiaxing) — the technical architecture. Referenced; not duplicated.
- **[LR] Unified CLR: Conditioned User Sequence Module** — V-1 architecture reference.

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

### 3.5 What surface teams get

**Why a surface team chooses UPP:**

1. **Pretrained capability they couldn't build alone.** Cross-surface data, foundation model integration, scale — surface teams get this for free, with a 2-week SLA to start FT.
2. **Surface team owns the product.** Features, FT recipe, labels, launch decisions — all surface team's. Base team is platform, not gatekeeper.
3. **Quarterly upgrades.** New base retrievers ship 1–2× per quarter. Surface teams get fresh capability without doing the platform work.
4. **Co-design seat at architecture changes.** When the base architecture changes, surface teams have a named POC and decision rights on how it lands for their surface.

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

**Why the cadence matters.** A published release cadence lets surface teams plan their FT iteration cycles around known release windows. Base team can plan deprecations rather than reacting. Without it, surface teams wait on ad-hoc base updates and base team gets pulled into surface schedules.

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

## 6. Version Maintenance — bets on Matt Chun's three scenarios

The aspiration is one stable base model per category. The reality is sometimes more than one. The §6 bets below define what we do when reality diverges from aspiration.

> **§9 has the explicit invitation to push back on these bets. The bets are sharp on purpose.**

### Scenario A: Engagement / retention negative

**The situation.** Surface FT-on-new-base shows engagement or retention regression vs surface FT-on-old-base.

**Bet.** Surface stays on old base. Base team treats the new release as a release-blocker — *the platform owns release-quality, not the surface.* Multi-version maintained ≤1 quarter. If the new base can't catch up within a quarter, base team rolls back the release or holds the surface back from upgrading until the next release.

**Alternative considered.** Block surface from upgrading until base is fixed. More conservative for the platform; creates surface friction.

**Decision owner.** Base team owns the release-or-block call. Surface team owns the adoption-or-skip call. If the call diverges, escalate base-EM ↔ surface-EM (James ↔ Dimitra for Notif).

### Scenario B: Engagement / retention neutral, infra cost negative

**The situation.** Surface FT-on-new-base is engagement-neutral and retention-neutral, but the new base costs more to serve.

**Bet.** Don't ship by default. Base team must justify the new base on grounds other than engagement (reduced surface code complexity, simpler architecture, future-proofing for V1, cross-surface infrastructure consolidation). When those grounds are explicit, ship. When they're not, block on the next release that reduces infra cost. Multi-version maintenance is avoided — fix the infra cost or wait.

**Alternative considered.** Allow architectural-future-proofing as a sufficient ship reason even when surface team disagrees on cost grounds. Less surface-team-friendly; gets the platform unstuck faster.

**Decision owner.** Base team owns the release-or-block call. Surface team owns adoption. Diverging calls escalate to base-EM ↔ surface-EM.

### Scenario C: Neutral overall (engagement, retention, infra)

**The situation.** Surface FT-on-new-base is fully neutral — no regression, no improvement, no infra delta.

**Bet.** Ship by default. Even neutral A/B is positive when amortized over (a) maintenance cost reduction (one stable version vs two), (b) future improvements riding on the new base, (c) consistency with cross-surface platform thesis. Exception: when the new base requires non-trivial surface code change to adopt, hold for next release.

**Alternative considered.** Surface-team-discretion default ("we don't migrate just for migration's sake"). More respectful of surface team time; risks platform fragmentation.

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

### 8.5 Operational rhythm — monthly snapshot

Once the model is in steady state, base team publishes a monthly snapshot covering:
- Stable + nightly version status (which surface is on which version).
- Active release cycle progress (V0 → V1 → V2 timeline).
- Surface partnership health (last sync date per surface, last shared-doc update date, any tripwire signals).
- Cost of multi-version maintenance, when applicable.

**Audience:** working group + leads. **Distribution:** the same Slack channel and shared doc. **Owner:** base team TL.

The monthly snapshot prevents the operational model from becoming shelfware. Without it, the model lives in this doc but not in the operating reality.

---

## 9. Tripwires (any one fires → re-engage)

These apply both during release cycles and in post-handoff steady-state:

1. **Two-week stall on any active surface workstream.** Silence is the earliest signal of a hidden blocker.
2. **Surface team asks base team to make a surface-level decision** ("should we launch?"). If they're asking, the handoff is not done. Coach them through the decision; do not make it for them.
3. **Surface metric regression that surface team cannot diagnose.** Base team is on call for *platform-level* issues, not surface debugging. If surface team can't diagnose, the handoff was premature on tooling/observability.
4. **Cross-surface architectural inconsistency.** If two surfaces start diverging on architecture in ways that fracture the platform thesis, base team re-engages on architecture review, not surface-by-surface negotiation.
5. **Quarterly architecture review skipped.** If the cadence slips, base team is at risk of being framed as a tools team rather than a platform team. Hold cadence even when the agenda is light.
6. **More than 2 stable versions for >1 quarter.** Per §6; deviation must be time-boxed.

---

## 10. Working Group Input — bets we want pushback on

Each item below is a **bet** with a named alternative we considered. We are not asking for an up-or-down vote. We are asking the working group to either (a) sharpen the bet, (b) argue for the named alternative with rationale, or (c) propose a third option we didn't consider.

### Bet 1 — §6 Scenario A (engagement-negative)
- **The bet.** Surface stays on old base; multi-version maintained ≤1 quarter; rollback required if new base can't catch up.
- **Alternative considered.** Block surface from upgrading until base is fixed (more conservative; surface friction).
- **Pushback we want.** Production case studies where time-box should be tighter or looser. Specific cases where blocking the surface upgrade is the right call.

### Bet 2 — §6 Scenario B (neutral + infra-negative)
- **The bet.** Don't ship by default; require explicit non-engagement justification.
- **Alternative considered.** Allow architectural-future-proofing as sufficient ship reason even on surface-team disagreement.
- **Pushback we want.** Cases where waiting for an infra-fix release blocked a strategically important architecture transition.

### Bet 3 — §6 Scenario C (neutral overall)
- **The bet.** Ship by default; surface team migrates absent non-trivial code-change adoption cost.
- **Alternative considered.** Surface-team-discretion default ("don't migrate just for migration's sake").
- **Pushback we want.** Surface teams' actual cost models for adoption and migration.

### Bet 4 — §7 clean-handoff criteria
- **The bet.** 6 criteria; 5 of 6 = clean handoff for Notif by end of May.
- **Alternative considered.** Smaller criteria set (3–4) with all required.
- **Pushback we want.** Whether criterion 5 (written 1-pager removing base-team execution responsibility) is overengineered or appropriate.

### Bet 5 — §4 release cadence
- **The bet.** 1–2 base retriever releases per quarter.
- **Alternative considered.** Same cadence as ranking (set by Matt's TDD); or empirical-only ("first cycle, then calibrate").
- **Pushback we want.** Specific surface team capacity reasons to go faster or slower.

### Bet 6 — §8 escalation path
- **The bet.** IC → ML-lead → EM → director, with director-escalation rare (<1/quarter).
- **Alternative considered.** Skip ML-lead step (IC → EM) for tighter loops.
- **Pushback we want.** Whether the ML-lead step adds value or adds latency.

### Bet 7 — §5 V0 codebase split
- **The bet.** Notif and HF split into separate FT codepaths at V0.
- **Alternative considered.** Keep shared longer; split at V1 or later.
- **Pushback we want.** Specific cases where shared codebase is currently helping vs hurting cross-surface velocity.

### Bet 8 — §9 tripwire set
- **The bet.** 6 tripwires above.
- **Alternative considered.** Add a tripwire for "surface team launch decisions diverge from base team's stated direction."
- **Pushback we want.** Tripwires we missed; tripwires that look right on paper but won't fire in practice.

---

## 11. Open questions for resolution

1. **Where does this doc live long-term?** Likely Confluence in the UPP space, alongside Matt's ranking TDD as a sibling page.
2. **Cadence for the quarterly architecture review** — and who chairs? Default proposal: base team chairs; all surface ML leads attend.
3. **Reflex / Anticipation Vision interaction.** Reflex is downstream of UPP, not a surface partner. Treat separately for now; flag for revisit when the boundary blurs.
4. **Naming consistency.** UBR / UPP CLR / Base CLR — Zihao's terminology in the March 2026 Wednesday meeting was "Base CLR" for current HF and "UPP CLR" for the co-designed redesign. Working group should converge on one term per release.
5. **Per-surface engineering details this doc punts on:** github repo ownership, on-call alarm routing, bug-report routing, cross-team PR review. These get filled in per-partnership in the shared partnership doc (§8), not standardized at this level. Working group should confirm.

---

## 12. What this doc does NOT do

- It does not prescribe specific FT recipes, training data windows, or hyperparameters. Those live in surface-team-owned recipes.
- It does not prescribe specific architecture decisions. Those live in the UBR design doc.
- It does not replace the launch process. Launches go through surface team's normal launch gates.
- It does not assume Search and P2P will adopt the same model verbatim. Specific adaptations are expected (relevance gating for Search; query-pin context for P2P). The principles transfer; the specifics adapt.
- It does not replace trust. Sai's proactive engineer staffing for P2P is worth more than any operational model document. The model lives inside trust relationships, not instead of them.
