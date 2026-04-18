# Charlie PIP — Project 1: Through Rewards MapReduce → Spark Migration (ER-14763)

**Draft:** 2026-04-18
**Manager:** James Li
**Allocation:** 50% of CPP window (companion to Project 2 — Pipeline docs + Forge.dev integration, which takes the other 50%)
**Duration:** 4 weeks CPP window (plus ~1 week head-start already given on 2026-04-10)
**External deadline:** End of May 2026 (from the April 16 comment on ER-14763 scoping down the broader migration)
**Reference ticket:** ER-14763 — "MapReduce to Spark: UserThroughRewardsToHFileService"

---

## Why this project

Our team owns `migrated.core001.user_through_rewards_builder`, a daily pipeline that produces the Through Rewards HFile used for online KVStore-backed retrieval. One task in this pipeline — `UserThroughRewardsToHFileServiceFVLV3` — still runs as a MapReduce job. As part of the broader 2026 XOrg Monarch cluster retirement (parent epic BDP-31396), remaining MapReduce jobs must move to Scala Spark before end-of-Q2 2026; after that, there will be no deprecation cluster and the job will stop running.

If this migration does not land on time, the Through Rewards pipeline breaks. Downstream, that means the Through Rewards signal stops refreshing in KVStore, which degrades the retrieval path that consumes it. This is a P1 on the ticket for reasons that hold up.

This project is an ideal PIP vehicle because:
- Scope is bounded and observable (one job, one conversion, one success criterion).
- Success is binary and measurable (the Spark job produces the correct HFile output, replaces the MR job, and the downstream KVStore upload succeeds on schedule).
- The pipeline surfaces in the oncall logs several times per quarter — so Project 1 will deepen your operational knowledge of the same pipeline that Project 2 will document and instrument.

---

## Scope

**In scope**
- Migrate the `UserThroughRewardsToHFileServiceFVLV3` task from MapReduce to Scala Spark.
- Validate the Spark output against the current MR output via a parallel-run comparison.
- Cut over production to the Spark implementation; disable the MR job.
- Update any associated runbook entries, workflow configs, and oncall notes.

**Out of scope**
- `BestPinDataManasIndexBuilder` / `BestPinWeeklyWorkflow`. Daniel Dormer is handling that separately (confirmed 2026-04-18).
- Any refactor beyond what the migration requires. Resist the urge to expand scope.
- Other jobs in the `user_through_rewards_builder` DAG that are already Spark-native.

---

## Success criterion

**"MapReduce successfully migrated to Spark"** per the ticket — defined concretely as:

1. The Spark implementation produces HFile output that is **byte-equivalent** (or equivalent under a documented, reviewed diff — e.g., key ordering, known-irrelevant metadata fields) to the MR output on the same input data, across at least 3 consecutive daily runs.
2. The downstream KVStore upload job (`UserThroughRewardsKVStoreHFileConvertAndUploadJobFVLV3`) succeeds using the Spark-produced HFile with no regression vs. the MR-produced HFile.
3. The production Spinner DAG has been cut over to the Spark implementation, the MR task is disabled, and the DAG has run green for at least 3 consecutive scheduled instances post-cutover.

---

## Weekly milestones (self-contained artifacts)

You have already had ~1 week since the 2026-04-10 handoff. Week 1 below assumes the CPP starts ~2026-04-21 and you enter it with that context. If the assessment and design work from the past week are already in progress, fold them into Week 1's exit criterion.

### Week 1 — Assessment + design

**By end of Week 1, deliver all three:**

1. **Deprecate-or-migrate assessment (written).** The ticket description gives a two-branch fork: if the job is no longer needed for high business impact, deprecate (LOE 5 min); if it is needed, migrate (LOE 4 weeks). Confirm the migrate branch is correct by:
    - Identifying downstream consumers of the Through Rewards HFile / KVStore dataset.
    - Confirming at least one live use case that justifies keeping the signal.
    - Writing a 1-page memo with the verdict, evidence, and the name of the stakeholder(s) you confirmed with.

2. **Migration design doc.** Covers:
    - Current MR job: inputs, outputs, logic summary, known edge cases (pulled from the existing MR code + any oncall runbook entries).
    - Proposed Scala Spark implementation: module structure, how the Spark job reads inputs, how it writes HFile output, how it handles partitioning/sort order, how it handles error paths.
    - Dependency and library choices: which Pinterest internal Spark libraries or HFile writers you plan to use, and why.
    - Test plan: unit test coverage, integration test approach, parallel-run comparison strategy.
    - Rollout plan: dark launch → parallel run → cutover sequence with explicit abort criteria.
    - Risk register: what could go wrong, mitigation per risk.

3. **Working local dev environment.** You can run the existing MR job locally against sample data and reproduce its output. If this already works from the head-start week, note it and move on.

**Exit criterion:** Migration design doc is reviewed by James and at least one other engineer (Daniel or JJ). Comments addressed. Go/no-go decision to start implementation.

### Week 2 — Implementation + unit tests

**By end of Week 2:**

1. **Scala Spark implementation of `UserThroughRewardsToHFileServiceFVLV3`** with working end-to-end local run on sample data. PR up in draft mode with a full test plan in the description, unit test coverage, and recorded local validation output.
2. **Spark output sample committed** (or attached to the PR) alongside the MR output sample from the same input date, with a diff summary. Byte-equivalent if possible; documented deltas if not.
3. **PR moves from draft to ready-for-review** once unit tests pass in CI and you have confirmed local output matches expectations. Until then, it stays in draft.

**Exit criterion:** Ready-for-review PR with green CI, test plan documented in the description, and local validation output recorded. Reviewer (James + at least one other) assigned.

### Week 3 — Parallel run + validation

**By end of Week 3:**

1. **Parallel-run configuration landed.** The MR job and the new Spark job run side-by-side in staging (or a shadow production slot) against the same input data for at least 3 consecutive daily runs.
2. **Validation report (written).** For each of the 3+ parallel runs: output comparison, any diffs categorized as (a) acceptable (documented reason) or (b) blocker. No blockers remain open.
3. **Downstream KVStore upload verified** using the Spark output on at least one of the parallel runs: upload succeeds, downstream consumers see no regression vs. the MR path.

**Exit criterion:** Validation report shows 3+ clean parallel runs and one end-to-end KVStore upload success using Spark output. Cutover plan is reviewed and signed off by James.

### Week 4 — Cutover + handoff

**By end of Week 4:**

1. **Production cutover** of the Spinner DAG to the Spark implementation. MR task disabled (not deleted — keep it disabled for 1 cycle in case of rollback). Cutover PR lands during a low-risk window agreed with James.
2. **Post-cutover monitoring** through at least 3 consecutive scheduled DAG instances, all green. Any pager or failure during this window gets root-caused and resolved before declaring done.
3. **Runbook + oncall notes updated.** The HF Triage oncall runbook for `user_through_rewards_builder` reflects the new Spark task name, any new failure signatures, and retirement of the MR-specific troubleshooting steps.
4. **Ticket closed** on ER-14763 with a summary comment of what shipped, PR links, validation evidence, and the cutover date.
5. **Handoff document** covering: what's merged, what's live, post-cutover monitoring results, the rollback procedure (if needed within the next 30 days), and any open follow-ups.

**Exit criterion:** ER-14763 is closed as resolved. 3 consecutive post-cutover DAG runs are green. Handoff document is complete.

---

## Handoff protocol

Same discipline as Project 2. Every weekly deliverable must stand alone.

- **Assessment memo, design doc, validation report, handoff doc** — each lives in its own committed Markdown file in the team documentation repo. No Google Docs as source of truth.
- **Every PR is self-contained.** Clear description, test plan, local validation output, and rollback note.
- **No WIP branches longer than 3 days without a draft-mode PR shared for async visibility.** If Week 2's implementation PR is not in draft mode by day 3 of Week 2, that is a deviation that gets flagged in the Monday status update.

---

## Expectations during this project

These are binding during the CPP window and mirror the Project 2 expectations (not duplicated; same rules apply across both projects).

1. **Monday 10am PT weekly status update** in the team Slack channel covering both Project 1 and Project 2.
2. **Blockers surfaced in < 24 hours** with the specific ask you need. For this project, anticipated blockers include: Spark library availability, Moka onboarding for the new job, parallel-run infrastructure, downstream consumer validation support. Don't sit on any of these.
3. **No PRs opened in ready-for-review state without a test plan and without local validation recorded in the PR description.** Draft mode is the default until those exist. This rule exists because it is the same gap documented in the CPP's Efficient Execution competency; following it during this project is not optional.
4. **Daily 1:1 with James with a written agenda** (shared Project 1 + Project 2 context).
5. **Every Friday, a written weekly retro.**

---

## Resources you will have

- **Ticket context:** ER-14763 description, linked Project Doc and Lookup Doc, and the April 16 comment scoping.
- **Parent epic:** BDP-31396 (XOrg MapReduce deprecation program). The Big Data Query Platform team (Ryan Moll, reporter on the ticket) is the program owner and a potential consultation source on Spark migration patterns others have used.
- **Code owners / reviewers:**
    - James (manager, reviewer).
    - Daniel Dormer — current assignee on ER-14763 pre-handoff, knows the broader migration context and is handling Best Pins separately. Consult on scope questions.
    - JJ (Sr. MLE, tech lead) — available for technical consultation on the Through Rewards pipeline and its downstream consumers.
- **Prior-art migrations:** Other MapReduce → Spark migrations under BDP-31396 have already landed; the Big Data team likely has a reference implementation or guide. Find it before starting to design from scratch.

Use these resources purposefully. Come to Daniel / JJ with specific questions, not general walkthrough requests.

---

## What is explicitly not this project

- Perfect feature parity on dead code paths of the MR job. If the MR job has logic that is never exercised in production (confirm via logs), document it and skip porting it. Note in the design doc.
- Refactoring the rest of the `user_through_rewards_builder` DAG. Other tasks in that DAG are out of scope.
- Performance optimization of the Spark job beyond matching or modestly improving the MR job's runtime. Correctness and on-time delivery first.

---

## Open questions (for James to resolve before Week 1 starts)

1. **Assessment assumption.** Are you assuming the deprecate-branch is not viable (i.e., downstream consumers confirmed), so the assessment is a formality? Or is there a real chance the job should be deprecated instead?
2. **Parallel-run environment.** Does our staging environment support running an MR job and a Spark job against the same input date for direct output comparison? If not, what's the shadow-prod plan?
3. **Cutover window.** Is there a preferred day-of-week / time-of-day for the production cutover (e.g., midweek morning, avoiding weekends)?
4. **Rollback authority.** If post-cutover monitoring surfaces an issue in Week 4, who has authority to trigger rollback to the MR job — Charlie alone, James alone, or joint?

---

## Why this PIP design is coherent across both projects

- **Project 1** deepens Charlie's code-level understanding of one specific pipeline (`user_through_rewards_builder`) while forcing independent execution on a scoped, observable deliverable.
- **Project 2** forces breadth — documenting all ~35 pipelines and building the routing infrastructure that will eventually reduce human oncall burden.
- **Shared pipeline:** The pipeline Charlie migrates in Project 1 is also one of the pipelines he documents in Project 2 — specifically one with a recurring "KVStore upload transient failure" signature that shows up multiple times per quarter. His Project 2 catalog entry for this pipeline will be more informed than anyone else's on the team by the end of the CPP.
- **Communication / EE / Impact gaps** are all stressed across both projects: draft-mode PR discipline, milestone setting, written status updates, blocker surfacing, alignment with upstream teams (Big Data / Forge.dev / KVStore).
