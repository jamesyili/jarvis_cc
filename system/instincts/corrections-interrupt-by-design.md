---
id: corrections-interrupt-by-design
trigger: When James interrupts an in-flight workflow with "before you do X, fix Y" — a factual correction (level, team size, name, role, date)
behavior: Treat the correction as the new top priority. Stop the workflow, fix the fact(s) across all relevant files, confirm with James, then resume the original workflow. Do NOT push through the workflow "and then correct after" — the correction is higher priority for a reason (James is about to act or ask Leo to act on information that would otherwise be wrong).
confidence: 0.4
evidence_count: 2
created: 2026-04-21
last_updated: 2026-04-21
status: active
---

## Evidence

### 2026-04-21
> "Before you run it across Wes Kao, I would like you to first correct a few things: 1. I'm M17, not M16. 2. My org size is around 20. Dhruvil is around 25, and Yan's is around 30."

Context: Leo had just offered to run the Dylan career conversation framing through the Wes Kao notebook. James paused the workflow to correct two factual errors in context files (James's level and team size assignments for peer EMs) that had propagated from a prior session's prep pack. These errors were load-bearing — the Wes Kao consult would have used wrong numbers. Leo stopped, fixed the files, confirmed, then continued. Correction interrupt was the right call.

Signal: correction (explicit; James used "before you [do next thing], first [fix this]" construction).

### 2026-04-21
> "Before you update, change the name Jingfeng to Dafang."

Context: Leo had just proposed updating `dylan_1on1_log.md` and `H1_career_convo.md` with today's 1:1 data. James paused the workflow to correct the name of the Senior Staff MLE Dylan inserted into Reflex. Leo had been using "Jingfeng" (conflating with Jinfeng/Jaewon who works on UPP CLR). James corrected to "Dafang" before the updates landed. Getting the name right in the context files prevents the error from compounding into future sessions.

Signal: correction (same "before you [next action], first [fix this]" pattern).

## Pattern

James uses this construction deliberately. When he sees Leo about to act on wrong data, he pauses the action rather than letting Leo ship the work and correct later. This is because:

1. Some actions are hard to undo (notebook consults with wrong context; files updated with wrong names that then get referenced downstream).
2. Correction-after is more expensive than correction-before (multiple files to fix, git history to clean, downstream readers already misled).
3. James's time is limited; catching once and fixing once is faster than correcting multiple times.

When Leo recognizes the "before you [next thing], fix [fact]" pattern, the right response is: confirm the correction scope ("fixing across X, Y, Z files"), execute, confirm completion, then resume the original workflow.
