---
name: leo-kb-automation-campaign
description: The executable, decision-gated campaign for Leo's hardest live problem (named by James 2026-07-12) - scheduled jobs that work unattended (arXiv recsys paper scraping as the worked example) plus making the KB pay off for a time-poor user. Load this when working on KB automation, scheduling, cron, arXiv or any new automated source, digests, or when James asks to make the KB more useful / hands-off / scheduled. Contains phased gates with expected numbers, a ranked scheduling menu with costs, and fenced wrong paths. Keywords - schedule, cron, automation, arXiv, scraper, unattended, digest, overnight, remote trigger, KB leverage, time budget.
---

# Leo KB Automation Campaign

**Objective (James, verbatim, 2026-07-12):** "Being able to schedule jobs that does things for me such as scrape arXiv for recsys papers, in addition to figuring out how to leverage kb more efficiently and effectively for my time schedule."

Decision-gated. Do phases in order; every gate has expected observations. Promotion of anything here routes through [leo-change-control]. Status of all phases as of 2026-07-13: **not started** (this document is the plan, not a record).

## Phase 0 — Baseline (30 min, $0 LLM)

```
python3 scripts/kb_search.py --stats          # record doc count BEFORE
python3 scripts/kb_search.py --rebuild        # index was last built 2026-04-05
python3 scripts/kb_search.py --stats          # expect docs > 2,600 (2,417 was the 04-05 count)
python3 scripts/kb_lint.py --json > /tmp/lint_baseline.json
bash .claude/skills/leo-validation-and-diagnostics/scripts/leo_doctor.sh
```
**Gate 0:** index fresh (0 articles newer than index), lint baseline recorded, doctor 0 FAIL. If rebuild fails → [leo-debugging-playbook] before proceeding.

## Phase 1 — arXiv recsys source, done right ($0 LLM)

Design: a `scripts/scrape_arxiv.py` following the house pattern (stdlib `urllib` + `xml.etree`, like `ingest.py` — read it first). arXiv Atom API: `http://export.arxiv.org/api/query?search_query=cat:cs.IR&sortBy=submittedDate&sortOrder=descending&max_results=50`.

Checklist (order matters):
1. Read `scripts/ingest.py` and `scripts/scrape_aman.py` for the article-writing + manifest conventions (frontmatter: Source/Ingested/Tags; dedup via `kb/.ingested_manifest.json`).
2. **Register the slug in BOTH live sets** — `HARD_SLUGS` in `ingest.py` AND the duplicated inline set in `scout.py`. THE TRAP: unregistered sources route to soft silently; drift precedent exists (`simon-willison`). Slug: `arxiv-recsys`, domain hard, dir `kb/hard/raw/arxiv-recsys/`.
3. Scope decision gate: **abstracts only** first (title + abstract + link as the article body). Full-text PDFs are a fenced path (bulk, low marginal value, storage).
4. `--dry-run` gate: expect **tens of cs.IR submissions/week** (order of magnitude; if you see thousands → query too broad; if zero → API/query broken).
5. Real run → `python3 scripts/kb_search.py --rebuild` → search for a paper title you saw in the dry run.

**Gate 1:** one arXiv paper findable end-to-end via `kb_search.py`. Not "the script ran" — *searchable*.

## Phase 2 — Scheduling menu, ranked (cost + mechanism first, per instinct `lead-with-cost-and-mechanism`)

| Rank | Mechanism | Token cost | Machine-on? | Notes |
|---|---|---|---|---|
| (a) | **WSL cron/systemd timer** running `scout.py` + `scrape_arxiv.py` | **$0** (pure-Python scraping, no LLM) | pc-leo must be on | WSL2 needs the cron service enabled — check `service cron status`; document whatever state you find. Simplest honest option |
| (b) | **GitHub Actions scheduled workflow** | $0 | No | Private repo with personal data: scraping-only job, checkout + commit + push of kb/ files; **no secrets, no LLM steps in the workflow, ever** |
| (c) | **Claude Code remote triggers** — two exist, DISABLED for cost (Daily KB Scout `trig_017ew…`, Overnight KB Work `trig_0132A…` per backlog.md) | Real $ | No | **Re-enabling is a spending decision for James** — present cost mechanism, never auto-enable |
| (d) | Local `claude -p` cron jobs | Subscription burn | Yes | Fenced as last resort: rate-limit-death precedent (13 lost chunks; 2026-07-12 workflow death) |

Decision gates: machine-on unacceptable → (b). LLM synthesis needed in-loop → stop, cost analysis first ([leo-proof-and-analysis-toolkit] Recipe 2), then James decides between (c) and local-LLM (see frontier).

**Gate 2:** 5 consecutive weekdays of unattended ingestion (check: new files' Ingested dates + git log or manifest timestamps, not memory).

## Phase 3 — Leverage for a time-poor user (consumption side)

The KB's failure mode is collection without consumption. Build the consumption loop, small:

1. **Digests:** `ingest.py daily` already writes `kb/.digests/<date>.md` — currently idle (no digest files exist → daily mode isn't running; verify the code path by reading ingest.py before relying on it). Scheduled job from Phase 2 should use `daily` mode so digests appear for free.
2. **Surface, don't archive:** a one-line digest pointer in session start (candidate: extend `session-start.sh` to `ls -t kb/.digests | head -1` — a change-control item, keep it read-only) or a /pulse hook.
3. **Weekly 20-minute ritual** (cadence over volume): `scout.py --status` → scan latest digest → ONE search-driven read. That's the whole ritual; more is the collection trap.
4. **Search hygiene:** tie `--rebuild` to the scheduled scout (same job, sequential) so staleness stops being a manual chore.

**Success gate (falsifiable, the campaign's definition of done):** one full week where (i) scheduled ingestion ran unattended ≥5 days AND (ii) James consumed ≥1 digest/synthesis artifact he didn't request mid-session. Measured by digest file dates + James's say-so. Never judged by eye.

## Fenced wrong paths

- **The collection trap** — Karen's documented tripwire (substrate built outpacing consumed slices; `karen_observations.md`; PF cadence-contract precedent in backlog). Scripts-written vs digests-read is the ratio to watch.
- **Re-enabling cloud triggers without the cost conversation** — James-gated, always.
- **graphify full rebuild as a side quest** — 1–3 hrs, token-heavy, rate-limit precedent. Separate decision.
- **Semantic search now** — explicitly deferred pending local-LLM (`system/kb-spec.md`); don't sneak it in.
- **Full-text PDF ingestion from arXiv** — abstracts first; revisit only if abstracts prove insufficient in the weekly ritual.

## When NOT to use this skill

- Routine manual KB ops → [leo-run-and-operate]
- KB data-model questions → [leo-kb-reference]
- Local-LLM / autonomous-synthesis ambitions beyond this campaign → [leo-research-frontier]
- A failing script → [leo-debugging-playbook]

## Provenance & maintenance

Authored 2026-07-13 from James's 2026-07-12 problem statement + repo verification. Volatile facts: trigger IDs and disabled-state are from backlog.md (unverifiable in-repo); digest idleness (`ls kb/.digests/ 2>/dev/null | wc -l` → 0); index staleness date. Re-verify before executing: `grep -n 'HARD_SLUGS' scripts/ingest.py`, `grep -n 'hard_slugs\|HARD' scripts/scout.py`, `service cron status`, `ls kb/.digests/ 2>/dev/null`.
