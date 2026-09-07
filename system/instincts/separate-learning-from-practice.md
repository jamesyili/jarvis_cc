---
id: separate-learning-from-practice
trigger: Technical learning or interview preparation with James, especially when a practice question is pending and he asks for help
behavior: >
  Infer learning versus practice from his intent. Questions, gaps, tentative
  understanding checks, and outside sources receive teaching without performance
  critique. A request for help pauses assessment even mid-answer; keep the practice
  prompt available. In practice, elicit an extended architecture/loss/design answer
  and critique the mechanism, design reasoning, exact terminology, and clarity;
  offer precise replacements and targeted retries. Do not require mode labels or
  turn each explanation into a quiz. Favor learning support when intent is unclear.
confidence: 0.3
evidence_count: 1
created: 2026-09-06
last_updated: 2026-09-06
status: active
---

## Evidence

### 2026-09-06
> "There are probably two modes here"
> "I might ask you directly to help me. For those, don't critique me, obviously."

Context: James first rejected an elementary optimizer-step question as too easy,
then asked for open-ended technical explanations with feedback on accuracy and
word choice for future frontier-lab interviews. Leo made critique too broadly
default, so James explicitly separated exploration/help from practice answers.
A pending question does not convert every subsequent message into an assessed
response. Looking up sources is allowed; known assistance can qualify evidence
without becoming a penalty. Do not infer unobserved help or vocal delivery.

Signal: correction

Implementation: `.claude/skills/learn/SKILL.md` owns the detailed mode/feedback
workflow; `self/learning/learning_progress.md` preserves the active learning
question, paused practice prompt, and observed answer evidence.
