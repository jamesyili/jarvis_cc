---
id: execute-after-decision-signal
trigger: When James has signaled a decision, evaluation outcome, or rejection ("he did well," "looks good," "ship it," "this is stupid don't do this," "no don't do this") and Leo has already given a recommendation, proposal, or summary
behavior: Execute the next step or drop the rejected sub-proposal silently. Do not ask further confirmation questions, do not re-litigate the comparison, do not pose "sound right?" check-ins, do not defend the rejected proposal. The decision is made — capture and move (or move past).
confidence: 0.6
evidence_count: 2
created: 2026-05-01
last_updated: 2026-05-02
status: active
---

## Evidence

### 2026-05-01
> "Just shut up and log this"

Context: End-session for Ali Rahmati EM candidate eval. James had already said "I think he did well" and asked for a summary. Leo produced the summary, then in /end-session phase asked an additional confirmation question ("Advance / Lean Yes — sound right? Anything from your in-room read I should capture?"). James pushed back hard.

Signal: correction.

### 2026-05-02
> "This is stupid. Don't do this." / "No don't do this." / [in response to 8 workflow-design improvements Leo proposed for the Ethan parallel-chat workflow, James kept ~3 and rejected 5 with terse one-line dismissals]

Context: Setup of `work+self/Ethan Evans questions/` parallel-chat workflow. Leo proposed 8 specific design improvements (canonical brief, cross-thread mention, standardized response shape, hybrid runtime, prioritization step, meta-prompt, anonymization, synthesis pre-define). James went down the list and rejected several explicitly — standardized response shape ("stupid"), synthesis pre-define ("don't do this"), anonymization ("don't"), Ethan-roleplay priming. Leo dropped each rejected proposal silently without re-litigating, then executed the trimmed plan.

Signal: correction (multi-instance within one turn — 5 rejections, all handled without pushback or defense).

Related: this overlaps with `dont-elaborate-on-delegated-work.md` (don't keep designing once James has scoped a task elsewhere) — both are "the decision is made, stop deliberating." The distinction: this one fires (a) in evaluation/recommendation contexts where Leo is tempted to second-confirm even after James has stated his call, AND (b) when James rejects a specific sub-proposal during a workflow review — Leo should drop without arguing, not try to reframe or defend. /end-session protocol's "grill one question at a time" should be skipped when the decision content is already clear from the conversation — go straight to capture.
