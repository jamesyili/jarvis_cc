# Charlie PIP — Project 2: Pipeline Documentation + Forge.dev Integration

**Draft:** 2026-04-18
**Manager:** James Li
**Allocation:** 50% of CPP window (companion to Project 1 — Through Rewards MR→Spark migration, which takes the other 50%)
**Duration:** 4 weeks (CPP window)
**Deliverable format:** Weekly self-contained artifacts (see Handoff Protocol)

---

## Why this project

Our team owns roughly 35 active pipelines in the HF Triage oncall rotation. Over the past 13 weeks of oncall logs, a large share of pager volume is transient, retry-safe, or cascaded from a single intentional upstream stoppage — yet each pager still wakes or interrupts a human engineer. Separately, Forge.dev is an AI oncall agent another team is building to absorb this class of work.

Two team-level gaps this project addresses:

1. **Pipeline documentation is scattered.** What each pipeline generates, who consumes it downstream, and what its characteristic failure modes are — this knowledge lives in people's heads and in Slack threads, not in a single authoritative document. Every new oncall spends significant time re-deriving it.

2. **No systematic plan to reduce pager-to-human noise.** We have no explicit target for "of all pagers that reach a human, what fraction are actually something a human needed to see?" We don't know the current ratio, and we have no programmatic path to improve it.

This project produces the documentation and the integration to close both gaps.

---

## Scope

**In scope**
- Pipeline catalog covering all HF Triage oncall pipelines (~35 DAGs).
- Failure mode taxonomy derived from the past quarter of oncall logs.
- Plan of attack to achieve **≥ 90% actionable-pager-to-human ratio** by routing retry-safe and cascade-noise pagers through Forge.dev before a human sees them.
- Documentation of Forge.dev integration points.
- New PagerDuty service + oncall rotation `ai_hf_recs_oncall` that routes eligible pagers to Forge.dev first, with human HF triage oncall as the escalation path when Forge.dev cannot resolve.
- Landed integration code: at least the highest-ROI Tier 1 auto-actions (transient retry, S3 FileAlreadyExists, KV store heartbeat) wired up end-to-end.

**Routing architecture (target state)**
- Eligible pagers route to `ai_hf_recs_oncall` (Forge.dev) first.
- Forge.dev classifies and either auto-resolves (Tier 1) or drafts a recommended action (Tier 2).
- If Forge.dev cannot resolve within its SLA, or if classification falls into Tier 3, the pager escalates to the human HF triage oncall.
- The 90% actionable ratio is measured against what reaches the human — after Forge.dev has absorbed Tier 1 noise.

**Out of scope**
- Cross-team coordination on upstream data dependencies (Ranking, Zen, etc.) — these get classified and flagged, not resolved by this project.
- Model deployment / teletraan failures — these require SMS/Notifs cross-team work, deferred.
- Net new pipeline creation — this project documents what exists.

---

## Success metric (the North Star)

**Actionable-pager-to-human ratio ≥ 90%.**

Definition: of all pagers that reach a human oncall engineer during a one-week measurement window, ≥ 90% must require human action (not auto-retry, not cascade-from-known-stoppage, not auto-resolve-on-next-run).

- **Baseline** (to be measured in Week 1 from the past-quarter logs): likely 40–60% actionable based on the sample, to be confirmed.
- **Target** at end of CPP: ≥ 90% actionable in the first full week after final Tier 1 auto-actions are live.
- **Fallback measurement** if end-of-CPP timing doesn't allow a full measurement window: projected ratio based on which Tier 1 actions are live, calculated against the past-quarter log sample.

---

## Weekly milestones (self-contained artifacts)

### Week 1 — Catalog + taxonomy + plan of attack

**By end of Week 1, deliver all three of the following as standalone artifacts:**

1. **Pipeline catalog** — one Markdown doc with ~35 entries, organized by pipeline family. Each entry contains:
    - Pipeline name (DAG id)
    - What the pipeline generates (output tables / signals / indexes, concrete names)
    - Main downstream consumers (what breaks if this pipeline breaks)
    - Known failure signatures from the past-quarter logs (exemplar incident per signature, with date + resolution)
    - Runbook pointer (wiki link if one exists; "none — to write" if not)
    - Current owner / primary POC (individual or team)

2. **Failure mode taxonomy** — ranked list of the ~10–12 recurring failure patterns with: signature, typical root cause category (transient / upstream / OOM / validation / capacity / expected-stoppage / etc.), standard resolution, frequency in the past-quarter logs, and automation tier (Tier 1 = auto-handle safely; Tier 2 = classify + draft for human approval; Tier 3 = human-only).

3. **Plan of attack for ≥ 90% actionable ratio.** This is a written plan, not code. It must contain:
    - Measured baseline from the past-quarter logs (what fraction of resolved pagers needed human action vs. would have been better handled by Tier 1 automation).
    - The specific set of Tier 1 auto-actions that, if live, would move the baseline toward 90%.
    - Ordering of Tier 1 actions by ROI (volume × safety × implementation effort).
    - Acceptance criteria per Tier 1 action ("before auto-marking success on a manas perf_test false positive, require: runbook condition X matches AND no concurrent critical pager on dependent index").
    - Risk register: what could go wrong if automation fires incorrectly, and mitigation per risk.

**Exit criterion:** The catalog, taxonomy, and plan are readable by an engineer who has not worked on this project. A reviewer can confirm the plan's projected ratio arithmetic against the past-quarter log sample.

### Week 2 — Forge.dev integration documentation + PagerDuty routing + first landed actions

**By end of Week 2:**

1. **Forge.dev integration documentation.** A thorough written spec covering:
    - Architectural overview: how Forge.dev intercepts pagers, what classification signals it accepts, what actions it can take.
    - Every integration point: API endpoints, webhook contracts, data schemas, auth model, failure handling, observability hooks.
    - Contact protocol with the Forge.dev team: who the POC is, how changes are reviewed, how issues are filed.
    - Integration-level test plan: how we verify Forge.dev is acting correctly in staging, how we validate in prod, how we roll back if it misbehaves.

2. **PagerDuty PRs landed** creating and configuring the new AI oncall routing layer:
    - New PagerDuty service `ai_hf_recs_oncall` created (PR landed in the PagerDuty-config repo).
    - New escalation policy for `ai_hf_recs_oncall` → human HF triage oncall on timeout or unresolved Tier 3 classification.
    - Routing rules landed to direct eligible pager categories (per the Week 1 taxonomy's Tier 1 + Tier 2 sets) to `ai_hf_recs_oncall` as the first responder.
    - Runbook entry (at least a stub) for `ai_hf_recs_oncall` explaining what it is, what it handles, what it escalates, and how a human oncall should interpret a pager that has already been touched by it.

3. **At least two Tier 1 auto-actions landed end-to-end.** "Landed" = code merged, tests passing, deployed to staging at minimum. Recommended set:
    - Moka/Celeborn transient retry
    - S3 FileAlreadyExistsException auto-mark-success-wait-next
    - KV store heartbeat-timeout auto-retry
    Pick the two highest-ROI from the Week 1 ordering.

**Exit criteria (all three):**
- Forge.dev team lead has reviewed the integration doc and signed off.
- `ai_hf_recs_oncall` PagerDuty service is live (can receive test pagers end-to-end from a synthetic pager through the new routing path to Forge.dev and back to the human escalation).
- Both landed auto-actions have working PRs with green CI and a staging smoke test.

### Week 3 — Additional landed deliverables

**By end of Week 3:**

1. **At least two additional Tier 1 or Tier 2 actions landed.** Continue the Week 1 ROI-ordered list.
2. **First production rollout** of at least one Tier 1 action behind a kill-switch / manual enable flag. Pick the safest one. Rollout uses the `ai_hf_recs_oncall` routing path stood up in Week 2.
3. **Observability dashboard** for the live Tier 1 actions: pager classification counts, auto-action success/failure rates, human-intervention fallback rates, and `ai_hf_recs_oncall` → human escalation rate.

**Exit criterion:** At least one auto-action is running in prod behind a flag, with observability confirming correct behavior on a real incident (or a synthetic one if no real incident fired).

### Week 4 — Measurement + handoff

**By end of Week 4:**

1. **Additional landed actions** from the remaining ROI-ordered list (continue rolling through Tier 1 → Tier 2 as time allows).
2. **Measurement against the ≥ 90% target**: either a full-week measurement window if timing allows, or the projected-ratio fallback calculation against the past-quarter log sample.
3. **Complete handoff document**: state of all deliverables, what's merged vs. in-flight, known issues, next steps for whoever picks up the project.

**Exit criterion:** The handoff document is complete enough that James or another engineer can pick up where you left off without needing to re-read your Slack history.

---

## Handoff protocol

This project is designed so that every weekly deliverable is usable standalone. If you do not finish, James (or another engineer) can pick up cleanly.

- **Each artifact lives in its own committed file** in the team documentation repo (pipeline catalog, taxonomy, plan, Forge.dev integration spec, observability dashboard config).
- **Each landed auto-action is its own PR**, self-contained, with a clear description of what it does, what it doesn't do, and what the next increment would be.
- **No WIP branches longer than 3 days without a draft-mode PR shared for async visibility.**

---

## Expectations during this project

These expectations are binding during the CPP window and directly reflect the gaps being addressed.

1. **Monday 10am PT weekly status update** in the team Slack channel. Format: what shipped last week, what's on deck this week, what's blocked and who you've asked to unblock. Written, not verbal.
2. **Blockers surfaced in < 24 hours** of hitting them, with the specific ask you need.
3. **No PRs opened in ready-for-review state without a test plan and without local validation recorded in the PR description.** Draft mode is the default when a PR is not ready for substantive review.
4. **Daily 1:1 with James with a written agenda.** Agenda delivered by 9am PT; James reviews and confirms before the 1:1. After each 1:1, you write up action items with owners and due dates in the shared doc.
5. **Every Friday, a written weekly retro** (3-5 sentences) covering: what I shipped, where I needed help, what I'd do differently, one concrete commitment for next week.

---

## Resources you will have

- **Source material:** HF Triage oncall logs (past quarter) at `work/people/charlie_pip_project2_oncall_source.md` on your manager's machine — James will hand you the needed extracts.
- **Forge.dev access:** James to broker the initial connection with the Forge.dev team lead. Recurring sync TBD by end of Week 1.
- **Daniel, JJ:** available for technical consultation on specific pipelines (both are listed as code owners on pipelines in the catalog). Use their time purposefully — come with specific questions, not general "can you walk me through X."

---

## What is explicitly not this project

- Perfect coverage of every edge case of every pipeline. 80/20 is fine — the catalog needs to be usable, not exhaustive.
- Solving every Forge.dev integration concern at the architectural level. Document the integration as it exists, propose what we need from Forge.dev, and land what you can.
- Writing new runbooks for every pipeline. Point to existing runbooks; flag pipelines missing runbooks so the team can address as follow-ups.

---

## Open questions (for James to resolve before kickoff)

1. **Baseline measurement methodology.** Exact definition of "actionable" for the baseline count — e.g., does "upstream data delay that auto-resolved" count as actionable-but-automatable, or non-actionable?
2. **Forge.dev team POC.** Confirm who the Forge.dev team lead is and whether David Sun is the right first contact.
3. **Team repo location for deliverables.** Where do the pipeline catalog and Forge.dev integration docs live — team wiki, shared Google Doc folder, or a repo?
4. **Production rollout authority.** Who signs off on a Tier 1 auto-action going live in prod — James alone, or does this need a broader team + oncall review?
