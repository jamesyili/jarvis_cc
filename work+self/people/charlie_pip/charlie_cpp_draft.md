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

#### SBI — Draft (2026-04-18, addressed to Charlie)

**Situation**

At IC14 level, Impact is measured by hands-on technical work, a track record of completing tasks and projects that meet team and project goals, and delivering production-ready code with minor help from code reviewers.

In H2 2025, your primary deliverables were:

- The PHP training data generation workflow and offline replay pipelines, to be delivered independently with high quality.
- PHP experiments set up on time.
- The PHP model serving layer, to be production-ready.

**Behavior**

1. **The PHP training data and offline replay pipeline you delivered did not work as expected and produced incorrect results.** Alok, another engineer on the team, had to rewrite the pipeline and deliver the critical parts. The rewrite took about a month.

2. **Peer feedback from a previous tech lead flagged overcomplication and low dev velocity on small tasks.** Simple tasks such as tuning the BMI relevance threshold (expected to take a couple of hours) took 3–4 days before a PR or a response. The same tech lead reported repeatedly asking you to simplify work down to the minimum changes required, and for some small tasks said it would have been faster to do the task directly than to support your delivery.

3. **Time spent on adjacent work rather than landing agreed deliverables**, documented in your H1 2025 review. Example cited at the time: time spent setting up the debugger instead of landing the code for the workflow, which delayed progress and visible results.

4. **Overall H2 2025 volume and quality of deliveries was on the lower end for IC14**, as documented in your H2 2025 review.

**Impact**

- The PHP training data and offline replay project was delayed by about a month because Alok had to rewrite and deliver the critical pipeline parts.
- About a month of Alok's engineering time was absorbed by rework that was expected to be your deliverable.
- Peer tech-lead time was absorbed by repeated simplification requests and occasional direct task ownership.
- H2 2025 delivery volume was at the low end for IC14, below role expectation.

### 2. Efficient Execution (Functional Skills) — *did Charlie drive project mechanics with rigor and independence*

**Framework definition:** *Drives successful execution of projects through milestone setting, anticipating risks/uncertainties, and making improvements to team processes.*

**Expected behaviors (at level):**
- **Independently executes** on an unambiguous project with some support and guardrails.
- Sets milestones, breaks up tasks, and runs retros with a little support.
- Presents the technical design or project progress to the team with some help.
- Shares their opinion on existing processes and/or practices of the team, to improve team execution.
- *Absorbed from Technical Excellence:* **Follows and contributes to the evolution of documented best practices for testing and validating code changes.**

#### SBI — Final (2026-04-18, addressed to Charlie, humanized)

**Situation**

You joined the PINvestigator project during the week of March 23, 2026 as your primary assignment under new management. PINvestigator is a new, small codebase that was spun up a few weeks earlier, with a minimal onboarding surface. Two other engineers on the team, Daniel (SWE II) and JJ (Sr. MLE, tech lead), were available to help with your ramp-up.

Assignments during this window:

- **March 24:** Run the Claude Code version of PINvestigator on two engagement-decline investigations (recent window and Oct–early Nov 2025 window). Coordinate with JJ on data backfill. Read the investigation doc and propose investigation angles.
- **April 1:** Speed up PINvestigator runtime. Add more Slack channels to one of the agents.

Expected ramp for an engineer at your level on a codebase of this size and maturity, with AI coding assistance available, was a first PR within about 1 day of active work plus 2–3 days of passive wait for runs. The same benchmark applied to the follow-on simple tasks.

**Behavior**

1. **You submitted two consecutive PRs without testing, without a test plan, and not in draft mode** (March 27 and April 9). You opened both PRs as ready-for-review. Neither recorded local validation, added tests, or described how you verified the change. Reviewers began substantive review on the assumption the change was ready, then had to halt once it became clear the basics were absent.

2. **You required heavy intervention on basic navigation and tooling.** Daniel and JJ spent about 5 combined hours unblocking you on codebase navigation and Jupyter notebook setup. These tasks were expected to be self-serve at your level on a codebase of this size. Slack back-and-forth and in-person unblocking sessions were required for simple tasks.

3. **Your ask-to-PR latency was well beyond expectation on simple, well-scoped work.** The April 1 asks (runtime speedup, Slack channel additions) produced one untested PR on April 9. That is eight calendar days for scope expected to land in 1–2 days of active work. The March 24 data-backfill and initial investigation task followed the same pattern.

4. **You have not made proactive or creative contributions to the project.** You were encouraged to propose investigation angles and improvements. None were surfaced during the review window.

5. **This pattern has been documented previously under prior management.** Your previous manager and tech lead (Bowen) gave you repeated written feedback on the same execution gaps: PR readiness, testing rigor, and independent problem solving. That feedback predated your team transition. Similar patterns have recurred in this review window without observable change.

**Impact**

- About 5 combined hours of senior engineering time (Daniel, SWE II; JJ, Sr. MLE / TL) went to unblocking you on tasks expected to be self-serve.
- Reviewer time was spent on two of your PRs opened as ready-for-review that lacked basic testing fundamentals. Review had to be halted mid-review on both occasions.
- Project velocity has slipped. Simple-task deliverables (runtime speedup, Slack-channel agent addition, initial investigation run) are behind schedule. PINvestigator overall is moving slower than planned.
- Creative direction for the project that was expected from you has come from the rest of the team.

### 3. Communication and Alignment (Functional Skills) — *did Charlie keep the team and stakeholders informed*

**Framework definition:** *Effectively and proactively communicates to ensure alignment, and tailors their message to the audience.*

**Expected behaviors (at level):**
- Communicates with clarity, brevity, and focus, and tailors their message to an audience of their function and project cross-functional partners.
- Actively listens to others and asks clarifying questions. Effectively participates in team discussions, and often brings topics to discuss with the team.
- Proactively communicates relevant information and status of own work to the team and to stakeholders.

#### SBI — Draft (2026-04-18, addressed to Charlie)

**Situation**

At IC14 level, Communication and Alignment is defined as communicating with clarity, brevity, and focus; actively listening and asking clarifying questions; participating in team discussions; and proactively communicating relevant information and work status to the team and to stakeholders. Your day-to-day work requires close collaboration with fellow engineers, tech leads, and cross-functional partners. From early December 2025 through late Q1 2026, your primary collaborator on PHP and Notifications work was Alok.

**Behavior**

1. **Offline replay experiment PR handoff (early Dec 2025 – late Q1 2026).** Alok gave you an unfinished PR where the code was working and only lint was failing; the remaining task was to fix lint, land the PR, and add two additional groups. You asked for 2 days to complete it. By the end of the week the task was not finished and Alok completed it himself and landed the PR. During that week you pushed commits that failed to build but did not surface the block to Alok or in the team channel. Alok met with you daily that week and reported that you "talked over the issue without really providing details about where you were stuck."

2. **Training data collection workflow setup (same period).** Alok provided a working reference workflow, documented the ask in a shared doc, and asked you to write a similar workflow. No progress was made.

3. **Instruction absorption gap.** Alok reported needing to ask you to repeat steps back to confirm understanding, and described a consistent pattern of needing to "spoon-feed" tasks. Compared with another engineer in a similar ramp-up window, the observation was that the other engineer did the homework independently (~80%) and asked targeted questions for the remainder (~20%); your pattern was not doing the independent thinking first.

4. **Technical alignment gaps documented in your H2 2025 review:** *"Teammates reported that your questions and proposals often lacked sufficient context and details, making it difficult to engage efficiently, and there were gaps in alignment on key technical decisions (such as how we should serve PHP models)."* Teammates needed to repeat instructions multiple times to move work forward, including on the BMI relevance filter adjustment.

5. **Question-framing and meeting-preparation gaps documented in your H1 2025 review:** *"Your questions can sometimes meander, making it hard for others to zero in on how to help, and at times, collaboration plans with co-workers haven't been fully fleshed out."* Recommended resources at that time included 1:1s, bravery coaching, reading, practice time, and writing down questions ahead of meetings.

6. **Self-acknowledgment in 1:1 with current manager.** You acknowledged that upfront communication and alignment have not been strong, and that issues surface downstream as a result.

**Impact**

- Alok absorbed tasks assigned to you (offline replay PR finish, training data workflow authoring).
- Daily 1:1 meetings with Alok during the offline replay week did not surface your actual blockers because blocker surfacing and detail articulation were insufficient. Alok's time was absorbed without resolving the underlying blocker.
- Teammates have had to repeat instructions multiple times to move your work forward.
- Alignment gaps on key technical decisions have required additional cycles to close.
- This pattern has been documented across two consecutive formal review cycles (H1 2025, H2 2025) and has continued through the current review window without observable change, consistent with your own acknowledgment in 1:1.

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
