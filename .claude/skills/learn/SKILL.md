---
name: learn
description: "Teach James from his active learning agenda and resume the exact saved lesson, question, and demonstrated progress. Use for learning sessions, continue learning, next lesson, or pausing a lesson."
user_invocable: true
---

# Learn

Resolve the Leo checkout from this canonical skill (three directories above its
directory) or its generated entry point. All paths below are relative to that
checkout. Use the shared start-session orientation floor once per fresh session;
do not repeat it on each learning turn.

## Resume before teaching

Read `self/learning/learning_progress.md` first. It owns the active course,
lesson/block, pending question, answer evidence, and next action. Read only the
relevant section of `self/learning/learning_agenda.md` and the lesson it names.
The current agenda selects the course; older workspace plans supply prior
knowledge, not a competing sequence. Calendar weeks are planning labels, not
evidence of completion.

On first use or a new topic, read the matching prior-knowledge record and
workspace NOTES, plus relevant teaching instincts. For the LLM/recsys course:
`self/interview_prep/fundamentals/transformers/learning-records/0001-prior-knowledge.md`
and its parent workspace's `NOTES.md`. Preserve nuances: positional-encoding
exposure is not demonstrated RoPE mastery. Do not restart attention basics.

If the progress file is absent, initialize it from the newest relevant records.
Mark missing evidence as unassessed. If records conflict, preserve the conflict
and resolve the one fact that determines the next lesson; do not invent progress.

Open with one sentence locating the exact saved point. If a question is pending,
resume that question before adding another. A direct topic change from James
overrides the cursor; preserve the prior stopping point in the history.

## Teach in small turns

- Use the current session's time and device constraints; do not re-ask them.
  On phone, default to one short explanation, a useful diagram or worked example,
  then one plain-text question. Let answers determine pace. Keep real mechanism,
  math, and failure modes; concise does not mean superficial.
- Reuse the existing lesson in small blocks. Grade sources before teaching them;
  distinguish primary results from interpretation and reported claims from
  independent validation. Check changing or disputed facts in primary sources.
  Do not propagate a known defect from an old lesson because it is on file.
- Keep one name per object. For W1, semantic-ID retrieval, sequence modeling,
  and cascade integration are overlapping design choices, not exclusive camps.
- Evaluate James's actual answer: what was correct, the specific gap, and the
  next useful explanation or transfer question. A displayed page, a tapped tab,
  or silence is not mastery. If he wants to skip, advance with assessment pending.
- Use the relevant notebook workflow when James requests it; offer a consultation
  when it would materially resolve a question, without delaying ordinary teaching.

## Display on the current device

Put essential teaching text in the conversation. Test one compact interactive
visual on a new client using the available visualize skill, and ask whether it
renders and responds to touch. Store that result for this client only. A local
browser test or successful desktop panel open does not prove phone visibility.

When interaction helps, use the available visualization capability and its output
contract. Otherwise use Markdown or a simple diagram. If the phone cannot show a
visual, continue in chat; do not spend the learning block building hosting or
publishing private material. Local paths and localhost URLs are not verified
phone delivery channels. Original lesson links are optional references.

Visual selection stays local unless explicitly sent into conversation. Do not
claim to observe taps or save browser-only answers. Ask James to answer in chat
for assessed work; use a supported explicit submission only if tested. Recreate
visuals from the lesson and saved state when returning in another task.

## Checkpoint each substantive learning turn

Update `self/learning/learning_progress.md` after receiving an answer, changing
topic, or preparing the next block. Save before replying so an interruption does
not lose the cursor; mark the next response as prepared/awaiting confirmation,
not read or learned. Record:

- Active course, lesson source, exact block, and timestamp in Pacific time.
- Last observed answer (verbatim when brief), assessment, misconceptions or
  uncertainties, and any demonstrated transfer. Separate prior-record evidence
  from this session's evidence.
- Exact pending prompt and the action after it is answered. Use stable block IDs
  such as `W01-map-01`; never just "continue W1."
- Device/display result, source defects affecting the next block, and deferred
  work. Keep a concise dated history of answered blocks and transitions.

Do not overwrite other active-course entries or changes from another session;
re-read before updating if the file may have changed. Only mark a lesson complete
and update the agenda checkbox when its exit criteria have evidence, or record
James's explicit completion claim with attribution. On pause, preserve the exact
pending question; on resume, use it rather than inventing a new quiz. Session logs
can summarize the session but do not replace the learning cursor. Follow the
normal session-end commit/push workflow; never claim cross-machine sync until it
actually succeeds.
