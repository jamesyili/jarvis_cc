---
name: knowledge-state
description: "James's learner model over the KB — per-concept understanding (1–4) and relevance (0/2/3), inherited by every article. Use to see the learning queue, record evidence when James demonstrates depth in dialogue or practice, mark a paper he authored, check what he already knows before teaching, or run the diagnostic quiz. Works from Codex and Claude Code."
user_invocable: true
---

# Knowledge state — what James knows, how deeply, how relevant

Resolve the Leo checkout from this canonical skill (three directories above its
directory) or its generated entry point; run commands with that root as the working
directory. Stdlib Python only (`python3` on Linux/WSL, `python` on native Windows).

## What it is (James, 2026-09-07)

The KB is the map of the field; this is the map of James. Two dimensions on every
hard-side **concept** (65 wiki articles + 7 the wiki predates, 72 total), inherited
by every raw article through its tags and title:

| Understanding | | Relevance | |
|---|---|---|---|
| 1 | very little exposure / unknown — the **default** for most things | 0 | not obviously relevant |
| 2 | basic — **assumed** wherever his background applies (PhD statistical ML; 12 yrs recsys; 4–5 on content quality/integrity; 5 on content understanding) | 2 | somewhat / potentially relevant |
| 3 | proven depth — demonstrated to Leo/Codex in dialogue or practice, or authored | 3 | very relevant to the role and the 2027 agenda |
| 4 | boundary pushing | | |

Rules that keep it honest:
- **Mostly inferred, corrected by evidence.** Levels move up only when dialogue, a practice
  answer, a paper he authored, or a work decision shows it. Reading is not evidence.
- **The skills write it, James doesn't hand-edit.** `learn` writes after a practice block or a
  learning exchange that shows depth; `context-update` writes when work evidence surfaces;
  `ingest --evidence` writes for authored/discussed papers. Every write appends a dated,
  attributed evidence entry.
- **Relevance changes only when the agenda changes** (`work/projects/personalization_retrieval_org_2027_agenda.md`).
- **Levels can go down** when a practice answer shows the assumption was wrong — say so in the note.

Source of truth: `kb/.kb/knowledge_state.json`. Human view (regenerated on every write):
`self/learning/knowledge_state.md`. Rendered into each wiki article's frontmatter
(`understanding:`, `relevance:`, `knowledge_updated:`) and as U/R columns in both `_index.md` catalogs.

## Commands

```bash
python3 scripts/kb_knowledge_state.py queue                    # relevance 3 & understanding <= 2 — the learning queue
python3 scripts/kb_knowledge_state.py list                     # everything, by relevance then understanding
python3 scripts/kb_knowledge_state.py get generative-recommendation
python3 scripts/kb_knowledge_state.py article kb/hard/raw/louis-wang/<file>.md   # what an article inherits

# Record evidence (the only way levels move) — note is required
python3 scripts/kb_knowledge_state.py set semantic-id-tokenization --understanding 3 \
    --kind practice --by codex --note "W02: explained RQ-VAE residual quantization and why collisions rise with corpus churn; defended dense-fallback"
python3 scripts/kb_knowledge_state.py set recsys-scaling-laws --understanding 2 \
    --kind dialogue --by claude --note "2026-09-xx: restated the fixed-FT-compute framing and the embedding-vs-dense allocation question unprompted"

python3 scripts/kb_knowledge_state.py init      # after new wiki articles appear (adds them at defaults)
python3 scripts/kb_knowledge_state.py check     # drift between wiki and sidecar (exit 1 if any)
python3 scripts/kb_knowledge_state.py render && python3 scripts/kb_knowledge_state.py export
```

`--kind` is one of `dialogue | practice | work | authored | seed | manual`; `--by` is `codex | claude | james`.

## How the learn skill uses it

Before selecting or building a block: run `queue`, and read the current concept's entry
(`get`). Teach at the level the model says, not the level the lesson assumes; skip
elementary checks on understanding-2 material. After a practice answer that clearly shows
depth (mechanism explained, trade-off defended, counterexample produced), `set` the concept
to 3 with the specific evidence in the note. After an answer that shows the assumed level 2
was wrong, `set` it to 1 and say why. Then continue; the export refreshes itself.

## How context-update uses it

When a session surfaces work evidence — James designed or defended the mechanism in a
real decision, co-authored a paper, ran the experiment himself — `set ... --kind work`
(or `authored`) with the artifact named in the note. Team members' work is not James's
evidence unless he did the technical reasoning in front of Leo.

## The diagnostic quiz

`self/learning/diagnostic_quiz_2026-09.md` — a broad, adaptive quiz over the relevance-3
and relevance-2 concepts, taken with Leo or Codex as the evaluator in practice mode, in two
or three ~45-minute sittings when James has time. Each answer is graded against the rubric
in the file and written back with `set --kind practice`. Do not administer it unprompted;
James opens it when he wants to.

## Extending the concept list

New wiki articles are picked up by `init`. Concepts without a wiki article live in
`EXTRA_CONCEPTS` inside `scripts/kb_knowledge_state.py` (name + tags) — add there, run
`init`, then `set` the levels with a `seed`/`manual` note. The seed pass of 2026-09-07 is
preserved in `self/learning/knowledge_state_seed_2026-09-07.json` for the record.

## Related

- `learn` skill (primary writer) · `context-update` skill (work evidence) · `ingest` skill (papers, `--evidence`)
- `leo-kb-reference` (data model) · `work/projects/personalization_retrieval_org_2027_agenda.md` (what "relevant" means)
