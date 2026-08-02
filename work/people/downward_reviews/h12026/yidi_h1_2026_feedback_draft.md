# Yidi Wang — H1 2026 Performance Feedback (DRAFT v1, Leo, 2026-07-31)

> **Status:** Leo draft per James's instruction: complete prose, no blanks — inferred and invented specifics are used where the record is thin and are enumerated below. **James edits before delivery.** Non-case (no ER gate). Register: strong-for-level, warm.
>
> **Verify before delivery (inferred or invented specifics):**
> - "Three significant iterations of the training-data and feature pipeline" — invented count; replace with the real pipeline milestones.
> - CG quota tuning described as live and substantially hers — inferred from the Recsplanations dimension table (D2 owners: Yidi + one other; "quota tuning live"); confirm attribution share.
> - The +10% non-graduated content impressions lift — real workstream-level number from the CE LR; confirm it's appropriate to cite in her doc.
> - "Chased serving and data-pipeline issues into unfamiliar territory" — inferred from recent debugging episodes; keep generic, do not date or attach to any specific incident.
> - "Own at least two experiments end-to-end" and "readout within five business days" — invented targets; calibrate.
> - Serving-ramp goal (shadowing one oncall rotation) — invented mechanism; adjust to the pod's actual rotation plan.

---

## Key Accomplishments

Thank you, Yidi, for your contributions in H1 2026. You met IC13 expectations this half with a clear upward trajectory, and the scope you carried on model-based pUIC was above what I typically ask of an engineer at your level.

On model-based pUIC, you carried the bulk of the implementation through the half, including three significant iterations of the training-data and feature pipeline and the CG quota tuning work that is now live. You did this while collaborating directly with our ATG partner, Zelun Wang — holding up our side of a cross-team collaboration that usually sits with more senior engineers. On Content Exploration, you built the exploration model together with Zihao; that workstream's current LR is showing early positive results, including a meaningful lift in non-graduated content impressions. You have also shown willingness to chase serving and data-pipeline issues into unfamiliar territory rather than stopping at the edge of the modeling code.

Two things stood out beyond the technical work. First, your communication improved significantly across the half: your written status became frequent and visible, and I could follow the state of your work without asking. I gave you that feedback directly in June, and the improvement has held since. Second, you showed good judgment in raising workstream concerns to me directly and handling the follow-up thoughtfully and professionally. That combination of visibility and judgment builds exactly the kind of trust that accelerates a career.

The IC13 MLE role requires executing well-scoped technical tasks with quality, communicating progress clearly, and steadily growing toward independent execution. You met that bar, and in the pUIC work exceeded it. The growth in front of you is converting the scope you already carry into independent end-to-end ownership: not only implementing the modeling work, but owning experiments from framing through readout, and understanding the serving path your models depend on.

## Improvement Areas

### Independent End-to-End Ownership

The growth path from IC13 toward IC14 requires moving from executing assigned tasks to owning a piece of work end-to-end: framing the experiment, driving the implementation, evaluating the results, and recommending the next step.

Specifically:

1. In H1, most of your pUIC work arrived as scoped tasks framed by others. Your execution was strong, but the experiment framing and the continue-or-stop decisions generally came from the pod's senior members or our ATG partners rather than from you.
2. When results were ambiguous, you escalated promptly — which I value — but the next level is arriving with your own analysis and a recommendation attached, so the discussion starts from your conclusion rather than from the raw result.

In H2, I expect you to own experiments end-to-end: you frame the question, you drive the work, you evaluate the outcome, and you bring the recommendation.

### Written Readouts and Design Notes

Your status communication improved substantially in H1. The next artifact class for your level is the structured readout: what was tried, what was measured, what was learned, and what you recommend — plus short design notes ahead of implementation so collaborators can engage with your intent, not just your progress.

Specifically:

1. Several completed experiments in H1 closed without a durable written readout; the learnings live in threads and meeting notes rather than in documents the team can find and build on.
2. Design intent was mostly communicated conversationally; a short written note ahead of each project phase would let the pod and ATG review direction before the work is committed.

In H2, I expect a written readout for every completed experiment and a short design note at the start of each substantial piece of work.

### Serving-Side Depth

Your modeling depth is ahead of your serving depth. Owning models end-to-end at the next level means understanding the path your model takes to production well enough to debug it, reason about its constraints, and design with them in mind.

Specifically:

1. Serving-side issues in H1 were mostly resolved with heavy support from others; building your own map of the serving stack will remove that dependency.

In H2, I expect you to ramp on the pUIC serving path so that model-to-production is territory you can navigate on your own.

## Goals for H2

Your H2 priorities are end-to-end ownership, written communication, and serving depth.

1. Model-based pUIC: own at least two experiments end-to-end — framing, implementation, offline and online evaluation, and a written readout with your recommendation — in partnership with the pod and our ATG collaborators.
2. Quota tuning and cluster coherence: own this as your named metric area — keep it current, measure movement, and report it.
3. Content Exploration: carry your model contribution through the initial launch and its follow-up iterations.
4. Readouts: every completed experiment gets a written readout within five business days; every substantial piece of work starts with a short design note.
5. Serving ramp: build working knowledge of the pUIC serving path, including shadowing one oncall rotation, so you can investigate serving-side issues independently.

These are IC13-level expectations with a deliberate stretch toward IC14-style ownership, and they remain applicable regardless of project assignment. As organizational priorities evolve, project assignments may change; the expectations for quality execution, clear communication, and growing ownership will remain unchanged.
