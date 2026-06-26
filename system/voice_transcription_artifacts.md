# Voice-Transcription Name Artifacts

James often uses voice input for long context dumps, and voice-transcription mangles Pinterest-internal names/terms that don't match the transcriber's common-word vocabulary. **When an unfamiliar name appears in a voice-input message, ask for clarification early rather than guessing** — guessing produces wrong context that pollutes downstream updates. (Migrated from auto-memory 2026-06-26.)

## Known mangling patterns (observed 2026-04-11 onward)

| Transcribed | Actual | Notes |
|---|---|---|
| "Retentive Recognitions" | Retentive Recommendations | Common mangling of James's project name |
| "Canada generator" | Candidate Generator (CG) | Technical term mangling |
| "Manus migration" | (unresolved — "MaaS migration"? "Manas"? "MDP"?) | Pinterest-internal term, needs confirmation |
| "Zihal" | Zili | Team member on Q2 performance checkpoint list |
| "Zihao" (for a female engineer) | Possible collision with Zihao Chen (UPP Prong 2, male) | Ask when context is unclear |
| "the hoodie" | (unresolved — possibly "Yu Ke"?) | Flagged in team dynamics, never clarified |
| "Yali" | (unresolved) | Flagged alongside "the hoodie" |
| "John" | Rajat (Chaturvedi) | VP skip-level name mangled 2026-04-16 — don't assume "John" is a new stakeholder; cross-check Slack/meeting context |
| "Rohu" | Rahul | Rahul = Blending EM under Dylan (James's onboarding buddy, Retentive Recs co-sponsor via Adreanne). In written artifacts always use Rahul. |
| "Le Pige" | Piyush (Maheshwari) | Piyush is on the UPP working group. Observed 2026-05-11. |

## How to apply

1. **Unfamiliar name in a James voice-input message → flag it as a clarification question early.** Don't silently assume, don't wait 5 messages to raise it. James confirms in one sentence.
2. **Technical terms** (project/tool/framework names) — cross-reference `work/projects/`, `work/people/stakeholders.md`, and the session's existing context before assuming.
3. **Team-member names** — cross-reference `work/people/stakeholders.md` + `work/people/team_members.md`.
4. **Don't fabricate context** around an unfamiliar term. If "Manus migration" appears with no record, say so and ask.
5. **Transliteration variants** (Jiaqing vs Jiaxing, Yuke vs Yu Ke) — treat as the same person unless context disambiguates, but note the ambiguity.

**Why:** Guessing costs a stakeholder-profile rewrite (Leo once miscategorized Sai as IC from stale data compounded by a transcription error). Asking costs one turn.
