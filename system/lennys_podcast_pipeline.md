# Lenny's Podcast — Thematic Extraction Pipeline

> Status as of 2026-04-05

---

## Why We're Doing This

Lenny's Podcast has 303 transcripts sitting in a public GitHub repo (`ChatPRD/lennys-podcast-transcripts`). These are among the best long-form conversations on product, growth, leadership, and career in existence — guests include top PMs, founders, growth leads, and executives from Airbnb, Stripe, Figma, Duolingo, and beyond.

The problem: 303 full transcripts is too much raw content to feed into NotebookLM (source limits) or search effectively. The solution: extract the signal, organized by theme, so the content can be queried, concatenated, and loaded into targeted notebooks.

**End state:** Per-theme NotebookLM notebooks containing only the passages most relevant to James's goals — not 303 full transcripts, but the distilled wisdom organized by what actually matters.

---

## What We Built

### 1. Ingestion (`scripts/ingest.py` → `backfill-lenny`)
Fetches all transcripts from the GitHub API and writes them as individual `.md` files to `learning/articles/lennys-podcast/`. Handles Unicode paths (e.g. Gustav Söderström).

- **303 transcripts ingested** (272 unique episodes after deduplication)
- Source registered in `learning/sources.md` as Tier 1

### 2. Thematic Extraction (`scripts/extract_themes.py`)
Processes each transcript through Claude (Sonnet 4.6 via `claude -p`) and extracts 0–3 verbatim passages per seed theme. Results written to `learning/themes/{theme-slug}/{episode-slug}.md`.

**Key design decisions:**
- **Sonnet over Opus** — comparable quality, ~2x faster. Sonnet actually found additional passages Opus missed in side-by-side testing.
- **Resumable** — manifest at `learning/.themes_manifest.json` tracks processed episodes, so crashes/restarts don't re-process work.
- **Verbatim** — passages are preserved exactly as spoken, not summarized. NotebookLM can RAG over the actual words.
- **Discovery pass** — beyond the 11 seed themes, Claude flags novel themes not in the seed list. These accumulate in `learning/themes/_discovered.md`.

---

## Seed Themes

| Theme | Episodes | Passages (est.) |
|-------|----------|-----------------|
| `product-strategy-growth` | 220 | ~450 |
| `org-strategy-leverage` | 217 | ~420 |
| `decision-making` | 209 | ~380 |
| `entrepreneurship-traction` | 172 | ~310 |
| `emotional-regulation-resilience` | 129 | ~220 |
| `ai-practical` | 104 | ~180 |
| `influencing-without-authority` | 115 | ~200 |
| `storytelling` | 59 | ~90 |
| `communication-brevity` | 57 | ~85 |
| `external-personal-branding` | 60 | ~95 |
| `managing-up-exec-presence` | 59 | ~90 |

**681 discovered passages** across novel themes not in the seed list — logged in `_discovered.md` for potential new theme candidates.

---

## Current Status

**272/272 episodes complete.** Finished 2026-04-05. All theme files committed and pushed.

### Pipeline history
- Started 2026-04-03 with Opus 4.6; switched to Sonnet 4.6 after quality comparison showed comparable results at ~2x speed
- Hit silent empty-response bug (returncode=0 but empty stdout) — fixed with retry logic + empty response detection
- Several crashes from laptop lid closes / process suspension — handled via `nohup` + restart from manifest
- Process has been restarted ~3 times total; manifest ensures no duplicate work

---

## What's Next

### 1. ~~Finish the run~~ ✅ Done

### 2. ~~Commit the theme files~~ ✅ Done (committed in two batches, final push 2026-04-05)
Hundreds of untracked files in `Learning/themes/` need to be committed once extraction completes. Run a `git add learning/themes/ && git commit`.

### 3. Review `_discovered.md`
681 passages flagged as novel themes. Worth skimming to identify whether any new seed themes should be added (e.g. `hiring-and-talent`, `culture-building`, `metrics-and-measurement` came up repeatedly in early batches).

### 4. Concatenate themes for NotebookLM
Use `python3 scripts/extract_themes.py --concat {theme-slug}` to merge all files for a theme into a single document. Pipe to a file, then upload to NotebookLM as a source.

Priority order for notebooks (based on James's goals):
1. `managing-up-exec-presence` + `influencing-without-authority` → one notebook (small enough to combine)
2. `communication-brevity` + `storytelling` → one notebook
3. `emotional-regulation-resilience` → standalone or merge with coaching content
4. `decision-making` → standalone (high volume)
5. `product-strategy-growth` + `org-strategy-leverage` → may need to split or sample (very high volume)

### 5. Register notebooks in Leo
Once created, add to `system/notebooklm/notebooks.md` and `CLAUDE.md` notebook table so Leo knows when to query them.

---

## File Locations

| Path | Description |
|------|-------------|
| `learning/articles/lennys-podcast/` | 272 raw transcript `.md` files |
| `learning/themes/{slug}/` | Per-episode extracted passages, organized by theme |
| `learning/themes/_discovered.md` | Novel theme passages not in seed list |
| `learning/themes/_errors/` | Episodes that failed JSON parsing (for debugging) |
| `learning/.themes_manifest.json` | Resumability manifest — tracks processed episodes |
| `scripts/ingest.py` | Ingestion pipeline (`backfill-lenny` command) |
| `scripts/extract_themes.py` | Extraction pipeline (`--status`, `--episode`, `--concat`) |
