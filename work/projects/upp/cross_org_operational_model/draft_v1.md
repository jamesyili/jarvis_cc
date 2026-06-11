# UPP Cross-Org Operational Model — v1 Draft

**Author:** James Li
**Date:** 2026-04-25
**Status:** Working draft — pre-review against Wes Kao + Ethan Evans frameworks
**Audience (eventual):** Dylan first; then Dimitra / Zhenyu; then Sai / Jinfeng; then Rajat as forcing function if needed.

---

## Why this exists now

UPP is approaching its first real operational handoff: **Notifications-on-Retrieval moves from "ATG-driven, James-shadowing" to "Notif-team-driven, James-out-of-execution-loop"** in April–May 2026. Hongtao Lin (ATG) has been the operational driver; Rui (Notif ML) is stepping up; Dimitra (Notif EM) is the receiving lead; Zhenyu Tan is likely the receiving manager.

This is the first of three handoffs the next 12 months will demand:

1. **Notif-on-Retrieval** (April–May 2026) — the precedent. If this lands clean, it becomes the template.
2. **P2P-on-Retrieval** (Q3 2026, conditional on UPP CLR co-design success) — Sai's team has staffed up, Jinfeng is genuine, Jiaxing co-owns the co-design.
3. **Search-on-Retrieval** (H2 2026) — Kurchi's team. Hardest political handoff. Relevance is the gate.

Without a clear operational model, every handoff becomes a one-off negotiation. The model below is what the precedent should be.

## Operating principles

1. **The base team is a platform team, not a product team.** UPP/CLR is a base model with cross-surface architecture, training infrastructure, and feature plumbing. After handoff, base team owns the platform; surface team owns its product. Confusing those two roles is the failure mode.

2. **Handoff means surface-team-owns-FT, base-team-owns-pretraining.** This is the line. Surface team owns: feature choices, fine-tuning recipes, surface-specific labels, launch decisions, online experimentation, on-call. Base team owns: pretraining loop, base architecture, cross-surface dataloader, foundation-model integration, base evaluation infra.

3. **The base team does not approve surface launches.** If we're approving launches, we're still a product team. Surface launches go through surface team's normal gates.

4. **Co-design at architecture changes, not at every iteration.** When the base model changes (new architecture, new pretraining data composition, new objective), surface teams co-design. When the surface team is iterating on its FT, base team is silent unless asked.

5. **Hands-off on execution. Lightweight visibility only.** Default touch point is one shared doc + one weekly sync. Anything more is a tripwire signal. Re-engaging too fast cues the surface team that the base team is still in the operator seat — and they start deferring decisions back.

6. **Credit propagates outward.** Surface team's wins are surface team's. Base team gets credit by being cited as the platform that made the wins possible — and by surface teams choosing the platform. Trying to claim surface wins is the fastest way to lose surface trust.

## Roles and ownership boundaries

| Layer | Owner after handoff | What that means |
|-------|---------------------|-----------------|
| Foundation model + pretraining loop | Base team (UPP/ATG) | Cross-surface data composition, pretraining objective, scale-up, GPU serving |
| Base model architecture (UPP CLR / UBR) | Base team, with surface co-design rights at architecture-change moments | Surface teams have a seat at architecture review; do not own architecture decisions |
| Cross-surface dataloader + feature plumbing | Base team | Multi-source DL, sampling-ratio decisions, feature remapping infra |
| Surface fine-tuning recipe | Surface team | Which features to add at FT, FT loss config, FT data window, FT hyperparameters |
| Surface-specific features and labels | Surface team | Adding download/screenshot/revisitation labels; surface context features; condition tower for that surface |
| Launch decisions, A/B experiments, on-call | Surface team | Base team gets pinged on platform-level issues; surface team owns their funnel |
| Cross-surface eval infra (recall@k per surface) | Base team builds, surface teams interpret | Base team owns the metric infra; surface teams own how to use it |
| Architecture change reviews | Base team proposes, surface teams sign off | Quarterly review cadence sufficient for stable platform |

## Coordination mechanisms

**Steady-state (post-handoff, no architecture changes pending):**

- **One shared doc** per surface partnership with current state, recent FT results, open questions, and named owners on both sides. Updated weekly by surface team. Read-only for base team unless asked to contribute.
- **One weekly sync** with surface ML lead + base TL + their direct reports. 30 minutes max. Surface team drives agenda. Base team listens unless asked.
- **One Slack channel** for the partnership. Async-first. Replies expected within one business day, not faster.
- **Quarterly architecture review** where base team presents proposed platform changes; surface teams give input; decisions documented.

**Architecture-change moments (base model changes, new pretraining objective, new architecture variant):**

- **Co-design working sessions** for the duration of the architecture change. Named POCs from each surface team. Time-boxed: typically 2–6 weeks of intensive work, then back to steady-state.
- **Shared design doc** with named co-authors from each side. The UBR design doc with Piyush + Jiaxing as co-authors is the template — not James + Piyush + Hongtao alone.
- **Decisions made at the working session level, not escalated to directors** unless co-authors disagree. This is the test of whether co-design is real or theater.

**Escalation path:**

- Surface IC ↔ base IC — first line, async.
- Surface ML lead ↔ base TL — second line, sync as needed.
- Surface EM ↔ base EM (James) — third line, only when ML-lead level is stuck.
- Surface director ↔ Dylan — fourth line, only when EM-level can't unblock and the issue is structural (resource conflict, scope dispute, milestone risk).

If escalation reaches the director level more than once per quarter, the operational model is broken and needs a structural fix, not another escalation.

## Tripwires (any one fires → re-engage)

These are inherited from `upp_retrieval.md` and adapted for the surface-handoff specifically:

1. **Two-week stall on any active surface workstream.** Silence on an active workstream is the earliest signal of a hidden blocker.
2. **Surface team asks base team to make a surface-level decision** (e.g., "should we launch?" or "should we add this feature?"). If they're asking, they're not yet owning. Either coach them through the decision or accept the handoff isn't done.
3. **Surface metric regression that surface team can't diagnose.** Base team should be on-call for *platform-level* issues but not for surface debugging. If surface team can't diagnose a regression, the handoff was premature on tooling/observability.
4. **Director asks about surface status in 1:1 and base EM can't answer.** Visibility degradation. Lightweight visibility ≠ no visibility. Monday review of surface team's shared doc is the hedge.
5. **Cross-surface architectural inconsistency.** If two surfaces start diverging on architecture in ways that fracture the platform thesis, base team must re-engage on architecture review, not surface-by-surface negotiation.
6. **Quarterly architecture review skipped.** If the cadence slips, the base team is at risk of being framed as a tools team rather than a platform team. Hold the cadence even if the agenda is light.

## Quality gates for "clean handoff"

For the Notif handoff specifically (April–May 2026 target), "clean" means:

- [ ] Notif team has driven at least one full FT iteration end-to-end (data → train → eval → launch decision) without base-team execution involvement.
- [ ] Surface Tower v2 result has landed (positive or negative) with Notif-team-led analysis.
- [ ] Shared doc has been Notif-team-updated for at least 4 consecutive weeks.
- [ ] Weekly sync has had at least 2 weeks where surface team drove the agenda end-to-end.
- [ ] Hongtao + Rui + Dimitra + Zhenyu have a written agreement (1-pager) on roles, including James's name removed from the FT execution path.
- [ ] Dimitra has named the next FT initiative herself, without prompting from base team.

If 5 of 6 land by end of May, handoff is clean. If 3 of 6 land, handoff is in progress. If <3 land, the operational model needs revisiting before the P2P handoff can be scoped.

## What this is NOT

- **Not a control mechanism.** This is not how the base team controls surface teams. Surface teams own their products. The model is how the partnership scales without ambiguity.
- **Not a contract.** Operating models are calibrated by experience, not enforced by document. The Notif handoff is the empirical test.
- **Not surface-specific.** P2P and Search will need surface-specific adaptations (relevance gating for Search, query-pin context for P2P). The principles transfer; the specifics adapt.
- **Not a replacement for trust.** Sai proactively staffing engineers is worth more than any operational model document. The model lives inside trust relationships, not instead of them.

## Open questions

1. **Is Zhenyu Tan the right Notif ML manager counterpart**, or is the relationship better routed through Dimitra alone? The pre-handoff conversation should clarify.
2. **What's the cadence for the quarterly architecture review** — and who chairs it? Default proposal: base team chairs, all surface ML leads attend.
3. **How does this interact with the Reflex / Anticipation Vision** which builds on the UPP base? Reflex is downstream of UPP, not a surface partner. Treat it separately for now.
4. **Does Dylan see this operational model the same way?** Specifically: would she cite the same line on "base team is platform team, not product team," or does she still expect base team to own surface launches in some scenarios? Worth surfacing in next 1:1.
5. **What's the right framing when the operational model creates conflict with surface team's preferences?** E.g., a surface team wants base team to do their FT for them. Default answer: "we'll teach you, not do it for you." But this needs a Dylan-aligned answer.
6. **Where does this document live long-term?** Likely needs a Pinterest-internal home, not just Leo. Either Confluence in the UPP space, or as an appendix to the UBR design doc, or as a standalone "UPP Platform Partnership Charter."

## Why this matters for the Director case

A platform that surface teams *choose* is fundamentally different from a platform that surface teams are *forced into*. The operational model is what makes the choice attractive: clear ownership, low friction, surface teams keep their wins, base team is the architect they want to work with rather than a dependency they tolerate.

If Notif handoff lands clean, it's the proof point that UPP scales without James as the operator. That's the Director-altitude signal — not "James shipped UPP" but "UPP is a platform that runs without James, and Notif is the first surface team to demonstrate that."
