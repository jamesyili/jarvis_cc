# Charlie CPP Draft

**Status:** Draft in progress — work session 2026-04-18 AM
**Context:** Charlie moving to formal CPP (Corrective Performance Plan) April 2026. Headcount-back agreed, Dylan aligned.

---

## Template Structure (from prior CPP sample, via James)

Pinterest People Experience CPP table. Five columns per competency row.

| Column | Content |
|--------|---------|
| **Competency/OKR** | Name of the competency being addressed (e.g., Impact, ML Technical Excellence, Communication and Alignment) |
| **Situation, Behavior, and Impact** | SBI narrative. Three labeled sub-sections. |
| **Action Plan** | Specific, observable actions Charlie must take |
| **Due Date** | Dated milestones tied to each action |
| **Action Plan Results** | Weekly tracking notes (Week 1 / Week 2 / Week 3 / Week 4), each tagged **On Track** / **Mixed** / **Off Track** with evidence links |

### SBI sub-structure

- **Situation:** Factual framing. Project name, assignment date, expected outcome, current state (e.g., "overdue by N weeks").
- **Behavior:** What Charlie has or has not done. Concrete, observable. Reference specific instances, feedback from team members, patterns across time.
- **Impact:** Downstream consequence — team engagement goals, topline metrics, reallocated work load on other engineers, delayed deliverables.

### Action Plan sub-structure

- Anchor each action to a **demonstrable outcome** (not an activity). Example: "Demonstrate proactive ownership of your projects and independently drive progress on improving [models]" — then decompose into dated sub-steps.
- Each sub-step has its own **Due Date**. Milestones are specific (code landed, experiment started, write-up delivered, launch review drafted).
- Mix leading indicators (plan/write-up due by X) with lagging indicators (experiment results, launch review ready).

### Action Plan Results sub-structure

- One entry per week across the review period.
- Status badge: **On Track** (green) / **Mixed** (yellow) / **Off Track** (red).
- Notes: what happened this week, what evidence supports the status, what's blocked, ETA for blocked items.
- Evidence links: Slack threads, PR links, docs, experiment dashboards.

---

## Competencies for Charlie's CPP (rough plan)

Per James (2026-04-17), three competencies selected. Technical Excellence dissolved: code-output expectations fold into **Impact**, testing/validation rigor folds into **Efficient Execution**. Communication and Alignment added as the third pillar. Split rationale: avoid overlap between Impact and Efficient Execution by making Impact = *did the work land with value* and Efficient Execution = *did Charlie drive the mechanics with rigor and independence*.

Each SBI narrative should cite the gap between the expected behavior and Charlie's observed behavior. Evidence + specifics to be filled in 2026-04-18 AM.

### 1. Impact (Responsibilities) — *did the work land with value*

**Framework definition:** *Delivers impact through hands-on technical work and has a track record of completing tasks, projects, etc. that have impact to team and project goals.*

**Expected behaviors (at level):**
- Hands-on technical work is the primary measure of impact.
- Has a track record of **successfully meeting project goals**.
- Contributes to meaningful team-level initiatives as a member of project teams.
- Leads team-level initiatives of limited impact and scope (minor feature iterations, code improvements, dependency upgrades).
- *Absorbed from Technical Excellence:* **Delivers production-ready code with minor help from code reviewers.**
- *Absorbed from Technical Excellence:* **Trusted code reviewer** — contributes to team-level code quality as a reviewer.

**SBI framing angle (to develop tomorrow):**
- Situation — specific project assignments with expected outcomes; specific production code / reviewer incidents.
- Behavior — where Charlie failed to meet project goals; where code shipped required more than "minor help" to become production-ready; where reviewer trust was not established.
- Impact — team initiatives that stalled; topline/engagement metrics missed; reviewer burden absorbed by others; production incidents.

### 2. Efficient Execution (Functional Skills) — *did Charlie drive project mechanics with rigor and independence*

**Framework definition:** *Drives successful execution of projects through milestone setting, anticipating risks/uncertainties, and making improvements to team processes.*

**Expected behaviors (at level):**
- **Independently executes** on an unambiguous project with some support and guardrails.
- Sets milestones, breaks up tasks, and runs retros with a little support.
- Presents the technical design or project progress to the team with some help.
- Shares their opinion on existing processes and/or practices of the team, to improve team execution.
- *Absorbed from Technical Excellence:* **Follows and contributes to the evolution of documented best practices for testing and validating code changes.**

**SBI framing angle (to develop tomorrow):**
- Situation — projects where independent execution, milestone setting, and risk anticipation were the explicit expectation; specific testing/validation gaps that preceded production issues.
- Behavior — where Charlie needed more than "a little support" to sequence milestones or break up tasks; where testing rigor was skipped and caused downstream breakage; where re-planning was required.
- Impact — slipped milestones, reallocated tasks, re-planning burden on manager, rework caused by weak validation, other engineers pulled in to unblock.

### 3. Communication and Alignment (Functional Skills) — *did Charlie keep the team and stakeholders informed*

**Framework definition:** *Effectively and proactively communicates to ensure alignment, and tailors their message to the audience.*

**Expected behaviors (at level):**
- Communicates with clarity, brevity, and focus, and tailors their message to an audience of their function and project cross-functional partners.
- Actively listens to others and asks clarifying questions. Effectively participates in team discussions, and often brings topics to discuss with the team.
- Proactively communicates relevant information and status of own work to the team and to stakeholders.

**SBI framing angle (to develop tomorrow):**
- Situation — expected update cadence (Slack channels, 1:1 cadence, project status); specific cross-functional touchpoints where alignment was needed.
- Behavior — missed update cadence; blockers surfaced without context or too late; insufficient clarifying questions / passive in team discussions; status not proactively shared.
- Impact — manager and team members pinging for updates; blockers diagnosed by others; cross-functional partners operating on stale information; delayed delivery because alignment slipped.

---

## Why the Split Works

| Competency | Core question | Main evidence types |
|------------|---------------|---------------------|
| **Impact** | Did the work land with value? | Project outcomes, shipped code quality, reviewer trust, team-initiative contribution |
| **Efficient Execution** | Did Charlie drive the mechanics independently and rigorously? | Milestone setting, task decomposition, testing/validation rigor, independent problem solving |
| **Communication and Alignment** | Did Charlie keep the team and stakeholders informed? | Slack cadence, blocker surfacing, status updates, cross-functional alignment |

Impact is about *outcomes*. Efficient Execution is about *process and independence*. Communication is about *information flow*. Each SBI should stay in its lane — if evidence could go under two competencies, pick the one that captures the primary gap, not both.

---

## Tomorrow's Working Session — Open Questions

1. **Which competencies apply to Charlie?** Same three as the sample, or different?
2. **What's the review period?** 4 weeks (sample) or different?
3. **Specific projects / deliverables** to anchor the SBIs?
4. **Evidence already collected** — Slack threads, 1:1 notes, peer feedback from Dylan, team members, skip-level?
5. **Tone calibration** — this is Pinterest's formal template; SBI language must be factual, non-editorial. Check against HRBP guidance.

---

## Process Notes

- Pinterest People Experience has an HRBP-reviewed template — confirm Charlie's version matches current 2026 formatting before drafting content.
- Prior CPPs (per sample) used dated, observable milestones — avoid vague actions like "improve communication."
- Weekly tracking is the proof artifact: Charlie's performance is judged on week-over-week status, not a single endpoint assessment.
