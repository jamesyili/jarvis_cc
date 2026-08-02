# Hanlin Lu — H1 2026 Performance Feedback (DRAFT v1, Leo, 2026-07-31)

> **Status:** Leo draft, non-case, no ER gate. Content is partly inferred per James's instruction ("infer from project allocation and sentiment; make up stuff if needed") — James edits before delivery.
>
> **Verify before delivery:** (1) that the ME GPU serving launch completion date and his specific share of the rollout work are stated fairly (his execution vs. Unity-side work owned by others); (2) the "neutral cost" characterization of the impression-share doubling; (3) which migration pieces (Manas, UserEventsView) were specifically assigned to him vs. the workstream generally; (4) the inferred communication examples in Improvement Area 2 — no specific dated incidents exist in the record; (5) H2 milestone dates are placeholders by design (end-of-quarter framing), set real dates before delivery.

---

## Key Accomplishments

Thank you, Hanlin, for your contributions in H1 2026. You were a consistent delivery engineer on RecGPT through the half, and several of the workstream's most concrete outcomes have your name on them.

The clearest was multi-embedding GPU serving: you carried the model deployment work through to launch, working through a serving stack that was new to you and closing out the remaining rollout issues so the change actually shipped. Separately, when we prioritized increasing RecGPT's share of candidate impressions, you executed the change with Bella and we doubled the impression share at neutral cost — a direct unlock for measuring the value of the modeling work. Through the half you also kept the RecGPT delivery machinery running: data jobs, the model training pipeline, and the experiment plumbing that the rest of the workstream builds on.

The IC14 MLE role requires independently executing well-scoped technical projects: driving assigned work through obstacles to completion, debugging your own blockers, and communicating status so the team always knows where things stand. Your H1 delivery record shows you can execute and ship. What I also observed is that on some assigned work, progress stalled for extended periods until someone outside the work — myself or a technical lead — stepped in to push it forward, and that status and blockers tended to surface when asked rather than proactively.

Taken together, your H1 performance met expectations on delivered execution, with two areas — independent momentum and proactive communication — that need to improve for your work to have the impact it should.

## Improvement Areas

### Independent Momentum

The IC14 MLE role requires driving your assigned work through obstacles without waiting for intervention: when something stalls, the expectation is that you diagnose why, try the obvious paths, escalate with specifics, and keep the work visibly moving.

Specifically:

1. The Manas migration work assigned to you stalled for an extended period during Q2. Momentum returned only after I stepped in directly. The blockers were real, but the gap was that weeks passed without you generating movement on them — no written diagnosis of what was stuck, no escalation with specifics, no proposed path around the obstacle.
2. On the ME GPU rollout, the final stretch needed sustained follow-up from outside the work to keep moving. The rollout had a long history that was not yours to own, and you ultimately landed it, but on your pieces the pattern was similar: progress came in response to pushes rather than from your own drive.

The difference between the work you shipped and the work that stalled was not difficulty. It was whether you treated the obstacle as yours to break through. In H2, I expect stalled work to be the exception and, when it happens, to be visible immediately: what is blocked, what you tried, what you need, and from whom.

### Proactive Written Communication

The IC14 MLE role requires keeping the team informed without being polled: status, risks, and blockers surfaced when they arise, in writing, so that your TL and I learn about problems from you rather than from the dashboards.

Specifically:

1. Through Q2, I most often learned the state of your migration and serving work by asking. Updates were accurate when requested, but the requesting was mine to do.
2. Blockers tended to surface in 1:1s or standups days after they began, which delayed help that could have been immediate.

In H2, I expect a concise written update every week — completed work, what's next, risks, and anything blocked — sent without prompting, and blockers flagged in writing the day they bite, with your own investigation attached.

## Goals for H2

Your H2 priorities are end-to-end experiment delivery on RecGPT, closing out the migration work, and making your progress visible by default.

1. RecGPT experiments: drive at least two experiments end-to-end as the delivery pair on the workstream — implementation, offline evaluation, online experiment, and a written readout with the result and the learning.
2. Migrations: complete the Manas migration and the UserEventsView migration, with dates committed at the start of the quarter and slips flagged in writing when known, not at the deadline.
3. Independent blocker resolution: every escalation arrives with your written investigation — what you observed, what you tried, what you ruled out, and your current hypothesis.
4. Weekly written update: completed work, upcoming milestones, risks, and blockers, every week, without prompting.

Your surface area on RecGPT is growing, and the workstream increasingly depends on the delivery engine you have become. The execution is there; pairing it with self-generated momentum and default visibility is what turns it into a record that speaks for itself. These are IC14-level expectations and remain applicable regardless of project assignment. As organizational priorities evolve, project assignments may change; the expectations for independent drive, communication, and delivery will remain unchanged.
