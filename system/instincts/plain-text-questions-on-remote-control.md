---
id: plain-text-questions-on-remote-control
trigger: Session is running via remote-control (phone) and Leo needs to ask James a clarifying question
behavior: Ask in plain prose in the reply, one question at a time. Don't use the AskUserQuestion structured-options UI — on the phone client James dismisses it and answers in text anyway. Structured option pickers are a desktop affordance.
confidence: 0.3
evidence_count: 1
created: 2026-07-29
last_updated: 2026-07-29
status: active
---

## Evidence

- 2026-07-29 (remote-control session, pcleo): Leo raised an AskUserQuestion with 4 candidate referents for an ambiguous ask ("is there a better message we can highlight?"). James denied the tool call without selecting, then supplied the answer as a normal message (pasted the EA's Slack blurb) — one of the offered options had matched, so the friction was the UI itself, not the options.
