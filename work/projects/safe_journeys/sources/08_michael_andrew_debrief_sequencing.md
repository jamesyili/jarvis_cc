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

## Addendum 2026-08-25 — James's reply (9:44 AM, sent before Leo's pack) + Michael's answers (4:35 / 4:37 PM)

**James, 9:44 AM (verbatim):**
> Thanks Michael! This is very clear and I'm glad that we have such clarity for the next steps. Here's what I'm thinking about doing today around CQ:
> 1. Talk to @J.J Hu and @Dafang He for L1 Utility + how they feel about the current experiments in GenAI vs the longer term plan. Get clear ETAs on planned experiments + get their sense of the prioritization of next set of experiments.
> 2. Start a thread with @Dhruvil Deven Badani @Dafang He @Qinglong Zeng about the next steps to align on the priorities of the training-time efforts, since that seems to be the bulk of discussion items we want to address between the various eng leads.
> ↳ Happy to work with you on the Safe Journeys doc. Let me know what input would be helpful.
> | We should share a Safe Journeys plan with Andrew/Dylan/Faisal by Friday
> SG. Happy to help. Is the goal of this doc just for sharing how the two teams are thinking about the long term framework or will it also include execution and prioritization proposals from the team? If the latter, will the plan also be inclusive of the GenAI work?
> | Andrew wanted me to follow-up to see if we could pull in any Faisal resources to accelerate the long-term CQ aware solution
> This is possible as well. What are your thoughts on this sequencing: first finalize the prioritization and get some clarity on who is doing what by when, then see what concrete asks we can make for Andrey / Faisal?

**Michael, 4:35 PM (verbatim):**
> Thanks James. (1) and (2) make sense to me. I would appreciate help on (3). I'm going to work on a draft tomorrow afternoon, and will share what I have. (It seems like we're NOT going to get TPM support. 😔)
> | Is the goal of this doc just for sharing … will the plan also be inclusive of the GenAI work?
> It's more the latter of execution and prioritization considerations. For the latter, I think we'll have to surface the CQ prioritization mentioned above.
> | What are your thoughts on this sequencing …
> SG. Perhaps I'll structure the doc then around our (a) CQ priorities and (b) Key Safe Journeys Milestones/Deliverables. Then we can get feedback on resourcing and timeline from Andrew/Dylan/Faisal.

**Michael, 4:37 PM (verbatim):**
> On a separate but related topic, have you shared your 'Quality and Safety Levers in the Recommendation Stack' doc with @Anna Kiyantseva? I know incorporating CQ signals into the recommendation stack is still potentially controversial - so would like to make sure she's had a chance to review and give her feedback.
> *(3 replies in thread, last 8:36 PM — James's reply not captured.)*

**What it settles (Leo read, 8/25 PM):**
1. **Michael's Friday plan is structured around James's prioritization work.** (a) CQ priorities = the doc's §9 block + the training-arms decision James's item (2) thread is meant to produce; (b) SJ milestones/deliverables. The plan is execution + prioritization, **inclusive of GenAI** (implied by "surface the CQ prioritization mentioned above" — the GenAI-first sequencing). Michael drafts **Wed 8/26 afternoon**; feedback on resourcing/timeline from Andrew/Dylan/Faisal follows — so the Andrey/Faisal-resources question is deferred behind prioritization, per James's sequencing. **No TPM** — Michael + James carry tracking themselves.
2. **James's three commitments, now public to Michael:** (1) JJ + Dafang L1-utility ETAs + next-experiment prioritization (= the Dafang+JJ note in the 8/25 reply pack — Dafang is L3-first this week per Dylan, so JJ is the realistic respondent); (2) the training-time priorities thread with Dhruvil/Dafang/Qinglong (Qinglong already agreed to the three-way — source 10); (3) help on the SJ doc.
3. **Anna Kiyantseva** — unknown to the repo. She sits in the Anticipation group DM with Andrew + Krystal (8/25), so most likely an Anticipation/Homefeed product lead. Michael's phrasing — "CQ signals in the recommendation stack is still potentially controversial" — says there is a product constituency that reads quality signals in ranking as engagement risk, and he wants her read *before* the doc reaches VJD. The doc's answer to that constituency already exists (D5: regrettable/non-regrettable decomposition, SSv2 guardrail budget, hold-back → derived λ). **Action: identify Anna's role, share the doc with a short note that leads with the guardrails, log her feedback as a source.**
