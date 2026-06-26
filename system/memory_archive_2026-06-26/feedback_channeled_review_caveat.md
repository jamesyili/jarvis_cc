---
name: Channeled review must be marked, not trusted
description: When NotebookLM is unavailable and a review is channeled from training knowledge, mark it explicitly as not-RAG-grounded and re-run when the notebook is available — channeled output captures vocabulary but misses asymmetric-application rules
type: feedback
originSessionId: 8a82b336-94a0-40ca-b514-4a07a67cc9b8
---
When a NotebookLM consult fails (auth, network, agent-stall) and you fall back to channeling the framework from training knowledge, do NOT pretend the review is RAG-grounded. The channeled output captures the framework vocabulary correctly but routinely misses the asymmetric-application rules that distinguish good advice from bad.

**How to apply:**

1. **Mark every channeled review explicitly.** Header should include `**⚠️ NOT RAG-grounded**` with a one-line note about why (e.g., "auth failed," "notebook not registered locally"). Treat the channeled review as a draft, not a verdict.
2. **Re-run when the notebook becomes available.** After any auth fix or notebook registration, immediately re-query the impacted reviews and replace channeled with grounded.
3. **Document where grounded ≠ channeled.** Add a comparison table at the bottom of the regenerated review showing where the grounded review flipped channeled-review judgments. This makes the value of grounding visible and protects future you from over-trusting channeled output.
4. **Never use channeled output to make irreversible recommendations.** If the work involves a doc that will be circulated, a recommendation that locks in a structural choice, or a verdict on someone's work, channeled-only is not enough — wait for grounded or flag the gap.

**Why:**

Session 2026-04-25e produced two case studies:
- **Wes Kao channeled vs grounded:** channeled review *praised* the §10 "pushback we want" structure as the right invitation shape; grounded review flagged it as Insecure Vibes via over-explanation. Channeled review *recommended* adding §1 with verbatim "Doesn't this already work?" phrasing as a MOO move; grounded review flagged it as the most common Wes Kao mistake — incepting negative ideas. Channeled review *praised* the "What changes when this doc lands" opener as Magical Thinking; grounded review flagged it as Sales-Not-Logistics inversion.
- **Ethan Evans channeled vs grounded:** channeled review used "Magical Thinking" framing for the opener, but Magical Thinking is actually a Wes Kao framework, not Ethan's — Ethan's actual move is 10x Problem framing. Channeled review used "OAR" (Ownership/Accountability/Results) for the accountability table; OAR is not in Ethan's source material per the notebook — the actual framework is "Scaled-and-Deep via Mechanisms." Channeled review framed §10 as "questions vs bets-with-alternatives"; grounded review named it as a 70% Rule decisiveness/altitude problem.

In both cases the channeled review's *gaps were correct* — the doc did need an opener fix, an accountability table, and a §10 reframe — but the *frameworks attributed* and the *altitude diagnosis* were materially wrong. Acting on the channeled review alone would have produced a worse v3 than the v4 the grounded reviews enabled.

The pattern: training captures the surface-level "this framework exists and applies here" mapping. Training routinely fails on:
- Whether a framework belongs to one author or another (cross-author confusion).
- Whether a specific application is actually right or specifically wrong under that framework.
- The altitude / decisiveness layer (which only shows up when the framework is grounded against the source author's full position).

Channeling is a useful fallback. It is not a substitute for grounding.
