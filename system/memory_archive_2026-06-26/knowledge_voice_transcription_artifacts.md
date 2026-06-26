---
name: James's voice-transcription name artifacts
description: Voice-input sessions produce predictable name mangling on Pinterest-internal terms. When an unfamiliar name appears, ask for clarification early rather than guessing.
type: knowledge
originSessionId: d2b59df2-8d04-44c8-bd1c-4085dc5b00cc
---
James often uses voice input for long context dumps, and voice-transcription mangles specific names/terms that don't match the transcriber's common-word vocabulary. Known mangling patterns observed on 2026-04-11:

| Transcribed | Actual | Notes |
|---|---|---|
| "Retentive Recognitions" | Retentive Recommendations | Common mangling of James's project name |
| "Canada generator" | Candidate Generator (CG) | Technical term mangling |
| "Manus migration" | (unresolved internal name — "MaaS migration"? "Manas"? "MDP"?) | Pinterest-internal term, needs confirmation |
| "Zihal" | Zili | Team member whose name appears on Q2 performance checkpoint list |
| "Zihao" (for a female engineer) | Possible ambiguity with Zihao Chen (UPP Prong 2 driver, male) — name collisions possible | Ask when context is unclear |
| "the hoodie" | (unresolved — possibly "Yu Ke"? or a literal nickname) | Flagged in team dynamics context, never clarified |
| "Yali" | (unresolved — possibly different from Yali who was mentioned) | Flagged alongside "the hoodie" |
| "John" | Rajat (Chaturvedi) | VP skip-level name mangled in voice input 2026-04-16 — don't assume "John" is a new stakeholder, cross-check with current Slack/meeting context first |
| "Rohu" | Rahul | Rahul is the Blending EM under Dylan (James's onboarding buddy, Retentive Recs co-sponsor via Adreanne). Voice-transcription of "Rahul" as "Rohu" observed 2026-04-18. In written artifacts always use Rahul. |
| "Le Pige" | Piyush (Maheshwari) | Piyush is on the UPP working group (cross-org operational model, draft_v3_synthesized.md). Voice-transcription of "Piyush" as "Le Pige" observed 2026-05-11. |

**How to apply:**

1. **When an unfamiliar name appears in a James voice-input message, flag it as a clarification question early** — don't silently assume or guess, and don't wait until 5 messages later to raise the ambiguity. James can confirm in one sentence.
2. **For technical terms** (project/tool/framework names), cross-reference against `work+self/projects/` files, `stakeholders.md`, and the session's existing context before assuming.
3. **For names of team members**, cross-reference against `work+self/people/stakeholders.md` §8 (Key Team Members).
4. **Don't fabricate context** around an unfamiliar term. If "Manus migration" appears and Leo has no record, say so: "I don't have context on what Manus migration refers to — is this a platform migration, a model name, or something else?"
5. **When voice input produces a transliteration variant** (Jiaqing vs Jiaxing, Yuke vs Yu Ke), treat them as the same person unless context disambiguates, but note the ambiguity for future reference.

**Why:** Guessing produces wrong context that pollutes downstream updates (e.g., Leo originally miscategorized Sai as an IC based on stale March UPP data; the voice-transcription error compounded with the stale data). Asking costs one turn; guessing costs a stakeholder profile rewrite.
