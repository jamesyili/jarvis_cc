---
name: leo-research-frontier
description: Where Leo could advance the state of the art, ranked by James (2026-07-12) - (1) an eval harness for the assistant itself, (2) autonomous KB at near-zero cost, (3) full tool portability. For each - why current SOTA fails, Leo's specific assets, the first three concrete steps in this repo, and a falsifiable result-when milestone. Load this when planning ambitious Leo work beyond maintenance, when James asks what's next for Leo or wants a stretch project, or before starting anything that smells like one of these three frontiers (so you build on the mapped assets instead of freelancing). Also lists the fenced graveyard - deferred paths and their reversal criteria. Keywords - frontier, open problem, eval harness, EDD, self-evaluation, autonomous KB, local LLM, ollama, portability, tool-agnostic, milestone, result when.
---

# Leo Research Frontier

Ranked by James, 2026-07-12. Everything here is **open/candidate — nothing is built.** Each frontier: why SOTA fails, Leo's assets, first three steps in this repo, and a falsifiable milestone. Execution discipline (demotions, collection-trap fences) → [leo-research-methodology].

## Frontier 1 — An eval harness for the assistant itself

**Why SOTA fails:** eval tooling (incl. the global eval-harness skill's EDD framing) targets apps and agents with task-level ground truth. No established harness evaluates a chief-of-staff assistant's *adherence to a personal behavioral contract* across sessions — which is exactly what Leo's 41 instincts are.

**Leo's assets:** instincts with confidence/evidence structure (labels), 125+ session logs and full transcripts under `~/.claude/projects/-home-james-src-leo/` (traces), `detect-corrections.sh` (a primitive online eval — regex correction detector already in production), `system/karen_observations.md` (adversarial channel), James's evals learning anchor + the in-flight eval-harness blog post (backlog Write — the work doubles as blog material).

**First three steps:**
1. Pick 5 mechanically checkable instincts (e.g. `never-read-inbox-contents`, `always-commit-and-push`, `give-bare-ranked-lists`) and write grep/replay checks over a session transcript.
2. Run against the last 10 transcripts; record a violation-rate baseline.
3. Wire as an end-session report phase (report, not gate — earn trust first).

**Result when:** an automated check catches a real instinct violation before James does, and it's logged in a session log.

## Frontier 2 — Autonomous KB at near-zero marginal cost

**Why SOTA fails:** cloud automation exists and is priced accordingly (Leo's two remote triggers sit disabled for cost); local-first autonomous ingestion+synthesis is unproven here — the local-LLM backlog row has been unstarted since inception, VRAM never assessed.

**Leo's assets:** the entire scraping pipeline is $0-token pure Python; `kb/.digests/` code path exists (idle); 16-video YouTube backlog queued; [leo-kb-automation-campaign] covers the scheduling mechanics — this frontier is the synthesis layer above it.

**First three steps:**
1. `nvidia-smi` / `free -g` — assess the hardware; pick a candidate model.
2. ollama + digest-summarization-only trial on one day's scout output (summarize, don't extract — lowest bar, failure is cheap).
3. One-week cron trial per the campaign's Phase 2(a), with the local model writing the digest.

**Result when:** 7 consecutive unattended days of ingestion + ≥1 locally generated digest James actually reads (the campaign's success gate, extended by local synthesis).

## Frontier 3 — Full tool portability (any model, any harness, at parity)

**Why SOTA fails:** assistant setups are harness-locked. Leo's skills/agents/hooks are Claude-Code-only; AGENTS.md-style portability is emerging industry-wide, but nobody demonstrates *full-parity operation* of a personal OS across harnesses.

**Leo's assets:** layered context (AGENTS.md base / CLAUDE.md extensions / GEMINI.md symlink), 8 flattened prompts/, repo-tracked instincts (already tool-neutral — the 2026-06-26 consolidation was done for exactly this), `system/export/work-leo-setup/` as a bootstrap precedent, and this leo-* library (harness-agnostic knowledge). **Honest gaps:** 9 workflow skills unflattened; no prose equivalents of the agents (karen, consult-notebook); hooks unreplicable outside Claude Code (a manual-checklist equivalent is needed).

**First three steps:**
1. Flatten the remaining workflow skills into prompts/.
2. Write `prompts/agents.md` — prose protocols for karen-style adversarial review and NLM consultation with the query-log discipline.
3. Run one full session cycle (start → work → end) in a non-Claude tool, producing a session log + commit.

**Result when:** a non-Claude session's log + commit is indistinguishable in form from a Claude one — format-valid, instincts honored, pushed.

## The fenced graveyard (deferred, with reversal criteria)

| Path | Status | Reverses when |
|---|---|---|
| Semantic search fallback | Deferred pending local LLM (`system/kb-spec.md`) | Frontier 2 step 2 succeeds |
| graphify Phases 2–4 | Frozen by tool-builder-trap demotion (2026-04-09, backlog) | The wiki becomes load-bearing for daily work |
| Overnight cloud triggers | Disabled for cost; James-gated | James decides the spend is worth it |

## When NOT to use this skill

- Scheduling/scraping execution → [leo-kb-automation-campaign]
- Deciding whether to build at all → [leo-research-methodology]
- Maintenance work → the core skills; frontiers are opt-in ambition, not upkeep

## Provenance & maintenance

Authored 2026-07-13 from James's ranking (2026-07-12) + asset verification. Re-verify assets: `ls system/instincts | wc -l`; `ls ~/.claude/projects/-home-james-src-leo/*.jsonl 2>/dev/null | wc -l` (transcripts, pc-leo only); `ls kb/.digests/ 2>/dev/null`; `ls prompts/`; backlog rows for local-LLM and triggers. If a frontier starts, move its live state to backlog.md and note the start date here.
