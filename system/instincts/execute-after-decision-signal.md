---
id: execute-after-decision-signal
trigger: When James has signaled a decision, evaluation outcome, or rejection ("he did well," "looks good," "ship it," "this is stupid don't do this," "no don't do this") and Leo has already given a recommendation, proposal, or summary — OR when James says a task/plan/design is being handled elsewhere (separate session, separate instance, or by someone else)
behavior: Execute the next step or drop the rejected sub-proposal silently. Do not ask further confirmation questions, do not re-litigate the comparison, do not pose "sound right?" check-ins, do not defend the rejected proposal. The decision is made — capture and move (or move past). When James scopes a topic to a separate session/instance/person, acknowledge briefly and move on — do not elaborate, design, or offer unsolicited depth on the delegated topic.
confidence: 0.75
evidence_count: 5
created: 2026-04-05
last_updated: 2026-06-26
status: active
---

## Evidence

### 2026-04-05 (absorbed from dont-elaborate-on-delegated-work, 2026-06-26)
> "I am already planning for how to do this exactly in a separate instance of leo, so no need to go too detailed about that."

Context: James mentioned building a Karpathy-style personal KB system. Leo was about to elaborate on the architecture. James scoped it — he had a plan elsewhere.

Signal: correction (the "handled elsewhere" variant — same root as the rest of this instinct: the decision/ownership is set, stop deliberating).

### 2026-05-01
> "Just shut up and log this"

Context: End-session for Ali Rahmati EM candidate eval. James had already said "I think he did well" and asked for a summary. Leo produced the summary, then in /end-session phase asked an additional confirmation question ("Advance / Lean Yes — sound right? Anything from your in-room read I should capture?"). James pushed back hard.

Signal: correction.

### 2026-05-02
> "This is stupid. Don't do this." / "No don't do this." / [in response to 8 workflow-design improvements Leo proposed for the Ethan parallel-chat workflow, James kept ~3 and rejected 5 with terse one-line dismissals]

Context: Setup of `work+self/Ethan Evans questions/` parallel-chat workflow. Leo proposed 8 specific design improvements (canonical brief, cross-thread mention, standardized response shape, hybrid runtime, prioritization step, meta-prompt, anonymization, synthesis pre-define). James went down the list and rejected several explicitly — standardized response shape ("stupid"), synthesis pre-define ("don't do this"), anonymization ("don't"), Ethan-roleplay priming. Leo dropped each rejected proposal silently without re-litigating, then executed the trimmed plan.

Signal: correction (multi-instance within one turn — 5 rejections, all handled without pushback or defense).

Related: the "handled elsewhere" case (don't keep designing once James has scoped a task to another session/instance/person) was absorbed into this instinct on 2026-06-26 — see the 2026-04-05 evidence above; both are "the decision is made, stop deliberating." This instinct fires (a) in evaluation/recommendation contexts where Leo is tempted to second-confirm even after James has stated his call, AND (b) when James rejects a specific sub-proposal during a workflow review — Leo should drop without arguing, not try to reframe or defend. /end-session protocol's "grill one question at a time" should be skipped when the decision content is already clear from the conversation — go straight to capture.

### 2026-05-19
> "Don't read too much into the SSv2 numbers with incremental hc ask. It's not all that important in this context." / "You should already know why UPP is 0%."

Context: During the HF CG scope inventory walkthrough for Dylan team-design input. Leo kept asking clarifying questions about specific SSv2 marginal math + UPP attribution logic. James gave terse corrections — both signaling "stop chasing this thread, move on" + a soft signal that Leo should have known the UPP-is-substrate point from context.

Signal: correction (twice in one turn).

### 2026-05-20
> "Stop questioning me about that, or we can worry about that later. Let's just play this through and then try to come up with a couple of scenarios for us to walk through together." / "I think you need to take it easy a little bit, maybe not make such drastic jumps every time." / "Let's not worry too much about lightweight scoring and Rahul's intersection as much as just keeping in mind that these two things could also be variables to consider, if that makes sense. I think you're reading too much into it, so let's back up a little bit and just note these two variables."

Context: Three distinct moments during the Dylan team-design grill-with-docs session where Leo kept asking sub-questions / over-analyzing when James wanted to move forward. First: Leo kept proposing variations on "should we ask Dylan directly" after James said no. Second: Leo synthesized a clean "Yan-UX-consolidation hypothesis" as "the read." Third: Leo built out V1/V2/V3 deep analysis on LWS+Blending+Rahul-as-Director-track when James wanted them held as open variables.

Signal: correction (multi-instance, same session). The pattern: when James gives a directive to drop a line of inquiry OR signals "just note this as a variable," scrub that line from forward analysis — do not re-introduce as sleeper variable or re-analyze later in the session. Adjacent to the `feedback_garbled_transcripts_scrub` memory and `feedback_hold_hypotheses_loosely` memory.
