# Reflex Context Instructions (for work-leo)

> Paste the block below into a fresh work-leo conversation. work-leo has Pinterest code + internal doc access that main-Leo does not. The output is a `context.md` that Andrew Yaroshevsky's Reflex agent will load as grounding context for autonomous HF recsys hypothesis generation.

Last updated: 2026-04-14

---

## Background (for James — don't paste this part)

This is the artifact James promised Andrew during the 2026-04-09 escalation: *"point Claude Code at the HF CG codepaths + share the table of HF CG engagement rates so Reflex can join survey labels (relevance) with engagement results."*

Andrew's bias going forward: **engagement data over relevance signals.** The survey × engagement join is the specific unlock that lets Reflex reason about both axes together.

Output: `~/reflex-context/context.md` on the work laptop. James reviews before anything reaches Andrew.

---

## Prompt to paste into work-leo

```
Task: Produce a context.md document that Andrew Yaroshevsky's Reflex agent will
load as grounding context for autonomous HF recsys hypothesis generation.

This is the artifact I promised Andrew when co-dev starts — "point Claude Code
at the HF CG codepaths + share the engagement rate table so Reflex can join
survey labels with engagement." This document IS that artifact.

Audience:
  (a) The Reflex agent at runtime — loads this every run, tokens cost money
  (b) Andrew reviews before ingestion

Output file: ~/reflex-context/context.md (create directory if needed)

Strict rules:
  - Tables > prose. Reflex is an agent, not a reader.
  - Every codepath reference must be a REAL file path. No hallucinations.
  - Every table reference must be a REAL warehouse location.
  - If you don't know something, mark it [GAP: need X] — do NOT invent.
  - No section longer than 40 lines.
  - No TODO/TBD text reaches Andrew. Fill or flag.

Required structure (follow exactly):

# Reflex Context: HF Candidate Generation
Version: v0.1 | Owner: James Li | Co-dev: Andrew Yaroshevsky
Last updated: [date]

## 1. HF CG Codepath Map
Table per active CG: name | one-line purpose | codepath | input signals |
output shape | known failure modes | owner.
Pull from: HF CG codebase, recent design docs, PINvestigator eval set.

## 2. Engagement Rate Table
- Table name + warehouse location
- Full schema: column | type | meaning | grain
- Join keys (specifically: what joins to survey labels)
- 3-5 canonical queries with SQL
- Caveats: sampling, staleness, missing segments

## 3. Survey × Engagement Join (Reflex's core unlock)
- Specific table paths enabling relevance-label × engagement join
- Why this matters: Andrew's bias is engagement > relevance; this join
  lets Reflex reason about both axes together
- Worked example: "for candidate X from CG Y, survey rating + engagement rate"

## 4. Known Failure Mode Library (seed — don't let Reflex rediscover)
- DS Agent CG signal decay: what happened, reframe after James+Dylan feedback
- Non-English CTR gap (CJK 83%): 9.5B impressions scope, MoE I18N at 0%
- [Any others from Pinsight M0 logs, PINvestigator runs, postmortems]

## 5. RLHF Feedback Protocol (how James corrects Reflex)
- Where feedback lands: [channel/file/ticket]
- Schema: {hypothesis_id, rating 1-5, failure_mode_tag, correction_text}
- Worked examples: 2-3 past Reflex cards + what expert correction looks like

## 6. Glossary (HF-specific)
Terms Reflex must use correctly: CG, pUIC, SSD, MoE, UPP, BMI, UIC, OmniSage,
RecGPT, I18N MoE, Retentive Recs. One-line def + system location per term.

## 7. Boundaries & Constraints
- PII: never surface raw user IDs, raw queries, raw content in cards
- Cost caps: max $X per hypothesis card; sample size ceilings
- Scope: HF CG only until extended — do NOT hypothesize on ads, moderation,
  P2P ranking, or Search until flagged

Process:
  1. Read Pinterest code + internal docs to fill each section
  2. Flag gaps explicitly (do not paper over)
  3. Show me the draft before anything reaches Andrew
  4. Prefer terse: Reflex is loading this, not reading it

Quality gate before you hand it to me:
  - Every file path exists (verify)
  - Every table name resolves (verify)
  - Section lengths within budget
  - No invented field names anywhere
```
