---
name: ingest
description: "Ingest a paper James passes (arXiv id/URL, PDF, or .md translation) into kb/hard/raw/arxiv/, record what it says about his understanding, and rebuild search. Also the manual entry point for the RSS/scout pipeline. Use when James says 'ingest this', 'add this paper to the KB', pastes an arXiv link, or drops a PDF."
user_invocable: true
---

# Ingest — papers James passes, plus the source pipeline

Resolve the Leo checkout from this canonical skill (three directories above its
directory) or its generated entry point; run every command with that root as the
working directory. Stdlib Python (`python3` on Linux/WSL, `python` on native
Windows) — no LLM calls inside the scripts, so this works identically from Codex
and Claude Code.

**Scope (James, 2026-09-07):** the KB's second consumer is a paper inbox he feeds by
hand. Ingest what he passes; do not scrape, schedule, or suggest reading lists from
here (those paths are fenced in `leo-kb-automation-campaign`). Soft-side content is
out of scope for this flow.

## Ingest one paper

```bash
# arXiv id or URL — fetches metadata, tries to download + extract the PDF, falls back to abstract
python3 scripts/ingest_paper.py 2507.22224 --tags semantic-ids,generative-retrieval,codebook

# Local PDF or a .md translation James made
python3 scripts/ingest_paper.py ~/Downloads/paper.pdf --title "Exact Title" --tags kv-cache,serving-cost
python3 scripts/ingest_paper.py notes/paper.md --url https://arxiv.org/abs/XXXX --tags ...

# Preview without writing
python3 scripts/ingest_paper.py 2507.22224 --dry-run
```

Steps, in order:

1. **Tag for inheritance.** Tags are how the article inherits James's understanding and
   relevance from concepts (`kb_knowledge_state.py article <path>` shows the match).
   Prefer concept slugs and wiki tags — `semantic-ids`, `kv-cache`, `scaling-laws`,
   `agent-harness`, `pre-ranking`, `offline-online` — over generic ones. If the output
   says "none matched — add tags", re-run with better tags before moving on.
2. **Record the evidence, if any.** A paper he co-authored: add `--evidence authored`.
   A paper he has already walked Leo through: `--evidence discussed --note "..."`.
   Both raise the matched concepts to understanding ≥ 3 with a dated evidence entry.
   A paper he merely sent to read is evidence of nothing — no flag.
3. **Read the result line.** It prints the file, whether full text or abstract-only was
   captured, and the inherited levels. Abstract-only means no PDF extractor was
   available; on a machine with `pypdf` or poppler, re-run with `--pdf <file>`.
4. **Skim the article** for garbage extraction (two-column PDFs interleave). If the body is
   unreadable, ask James for the PDF or a .md translation rather than leaving noise in the KB.
5. **Commit** the article, `kb/.ingested_manifest.json`, and `kb/.kb/search_index.json`
   (the script rebuilt it). If `--evidence` was used, also `kb/.kb/knowledge_state.json`,
   the rendered wiki articles, and `self/learning/knowledge_state.md`.

Privacy invariant: nothing Pinterest-internal enters `kb/`. Papers are public; James's
notes about how they relate to his team's work belong in `work/`, not in the article.

## Source pipeline (unchanged, manual)

```bash
python3 scripts/ingest.py status        # counts + last sync per source
python3 scripts/ingest.py check-rss     # pull new items from RSS_SOURCES (hard + soft)
python3 scripts/ingest.py daily         # check-rss + digest (digests are idle by design)
python3 scripts/kb_search.py --rebuild  # if you ingested without the paper script
python3 scripts/build_index.py          # catalogs (_index.md) with the U/R columns
```

Adding a source means registering its slug in **both** `HARD_SLUGS` in `ingest.py` and
the inline set in `scout.py` — an unregistered source routes to soft silently
(`leo-config-and-flags` has the checklist). Output lands under `kb/<domain>/raw/<slug>/`,
never under `self/learning/` (the pre-2026-04 layout this skill used to describe).

## Related

- `knowledge-state` skill — the learner model these articles inherit from
- `leo-kb-reference` — data model, frontmatter convention, index staleness
- `leo-kb-automation-campaign` — the fenced scheduled/scraping paths
