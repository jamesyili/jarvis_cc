# Source 08 — Michael's DM after debriefing Andrew: the CQ sequencing call + who drives the plan

> **Source of record.** Two Slack screenshots from James, captured Mon 2026-08-24 AM. Thread dated "Today" 1:22 PM (James) → 2:04 PM ack → 3:57 PM (Michael) — ⟨day not confirmed: Fri 8/21 or the weekend⟩. James's opener: "curious what the next steps are in terms of creating a joint prioritization for the next steps for Safe Journeys and GenAI workstreams? Happy to help in any way."

## Michael, verbatim (3:57 PM)

> Hey - I just got a chance to debrief with Andrew on this. A few points. Interested in your thoughts.
> - From an **Anticipation** perspective, the most important priority is UICs as multiple projects are dependent on those. So from a resourcing perspective that should take priority.
> - When it comes to Content Quality prioritization, here's how we discussed sequencing it.
>   - **GenAI** - Start with GenAI being the first use case for CQ aware ranking. I believe this is already part of the 12-week Sprint experimentation plan, so no change here.
>   - **Teen Aware AI Pod (Racy)** - Complete rollout of what the team is working on, and then see which of those solutions can be similarly applied to Self-Harm in the short term before the long-term CQ aware solution is built.
>   - **Safe Journeys (Self-Harm)** - We should opportunistically see which of the tests run with the Teen Aware AI Pod could be applied to the Self-Harm signal, but generally we should be leaning on the long-term CQ aware solution.
>
> Next Steps
> - We should share a Safe Journeys plan with Andrew/Dylan/Faisal by Friday, and then we would follow-up with sharing it with VJD next week. I can drive this, but will need your continued input. (Due to the code red, a lot of Bill reviews have been pushed out so the plan would be to circle back with VJD first before going to Bill.)
> - Andrew wanted me to follow-up to see if we could pull in any Faisal resources to accelerate the long-term CQ aware solution - but aren't we already working with the right POC (@Qinglong Zeng)? Do you think I should reach out to @Andrey Gusev as well?

## What it settles (Leo read, 8/24)

1. **The genAI-vs-teen-safety priority call — the one the doc's §9 asked leadership for and the Dylan-prep addendum said "hasn't been made" — has now been made on the PM side (Andrew + Michael): GenAI first as the CQ-aware-ranking use case; self-harm rides the long-term solution, with only opportunistic short-term borrowing from the Racy pod.** Eng-side ratification (Dylan) is the missing half; today's 1:1 §2 should carry it as "Andrew and Michael have sequenced it this way — are you aligned?" rather than as an open escalation.
2. **"Racy" defined at last: the Teen Aware AI Pod** — an existing pod rolling out racy-content interventions; its tests are the short-term self-harm candidates. (Closes the 8/22 open item "Racy — not defined anywhere.")
3. **Michael drives the plan; James is input.** The PM owns the Safe Journeys *plan*; James keeps the pen on the technical framework (the doc Qinglong called the starting point). Good for load; the watch is that "plan" and "framework" stay distinct artifacts so the framework isn't re-authored under a PM plan.
4. **Timeline slipped, and it's not James's slip:** the plan's Bill-ready 8/26 → Bill review 8/28 is gone ("code red pushed Bill reviews out"). New shape: Andrew/Dylan/Faisal by Friday (8/28 if the message is 8/21) → VJD the week after → Bill later. Tab 2 (exec summary, headers-only per D7) now has more runway and a different first reader (VJD).
5. **UICs named the org's top Anticipation priority ("multiple projects are dependent")** — this is James's RR/pUIC line (Yuke, Chuxi, Yidi, Zelun's CLR design, the model-based pUIC + UPP base-model sync). It is *leverage* in the prioritization conversation: the dependency chain runs through James's team, so CQ time comes out of something and Michael has just said which thing must not give.
6. **The Faisal-resources question is a trap to step around, not a favor to accept.** Qinglong reports to Faisal and owns CQ; the critical path the doc names is *his* (calibrated classifiers in Galaxy, signal coverage, label pipelines). "Pull in Faisal resources" routed through anyone other than Qinglong reads as going around the co-author two days after he publicly adopted the doc. The correct acceleration ask is to Faisal *for* Qinglong's lane: a committed calibration date + the measurement DS POC (WS1's own open need). **Andrey Gusev is unknown to the repo** — before endorsing an outreach, James needs to know whether he sits in Faisal's org (then: only with Qinglong looped) or elsewhere.

## Open

- Which day the thread is from (fixes "by Friday").
- **VJD = Vicky, Jeff, Dana** (James, 8/24) — the exec read before Bill. Andrey Gusev still unidentified.
- Which "multiple projects" depend on UICs, and their dates — worth getting from Michael/Andrew in writing; it's the roadmap justification for protecting the pUIC line.
