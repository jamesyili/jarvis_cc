---
name: leo-change-control
description: >
  How changes to the Leo repo are classified, gated, and executed. Load this BEFORE
  moving/renaming/deleting any file or folder, retiring a system, adding a top-level
  directory, editing a SKILL.md that has a prompts/ twin, committing at session end,
  or promoting an instinct. Symptoms that mean you needed this skill: a grep for an
  old path still returns hits after a "complete" reorg; .gitignore patterns silently
  stopped matching; a skill runs outdated instructions; a bulk move silently deleted
  a file; work left uncommitted/unpushed at session end. Keywords: git mv, repoint,
  file move, reorg, rename, commit conventions, Claude-Session trailer, SKILL.md
  casing, prompts sync, migration, retirement, root directory rule, instinct
  promotion, outbound gating, what requires James.
---

# Leo Change Control

How changes to `/home/james/src/leo` are classified, gated, and executed. Every rule below has an incident behind it — the incidents are summarized inline with SHAs; the full chronicle is `leo-failure-archaeology`'s home turf.

Governing law (never contradict): `AGENTS.md`, `CLAUDE.md`, `system/instincts/` (41 instinct files + `INDEX.md` as of 2026-07-12).

## Change classification — what requires James

| Change type | Gate | Source of the rule |
|---|---|---|
| Anything outbound beyond James-to-James (`/send-me` to `jamesyili@gmail.com`, `/save-to-drive` to his Leo Outbox) | **James, always.** `/send-me` hard rule: "Default recipient is always `jamesyili@gmail.com`. Never send elsewhere from this skill." Every send is logged in `system/outbound_log.md` (audit trail: every row to date is gmail-to-James or Drive Leo Outbox — verified 2026-07-12) | `.claude/skills/send-me/SKILL.md` Rules section |
| Deleting files James authored | **James confirms.** Norm evidenced twice, not written as a standalone rule (labeled as such): the 2026-07-10 reorg's accidental deletion was *restored* by Leo "pending James's confirm" (commit `4b29b5c`); the 2026-07-11 deletions (`scheduled/`, `work/anatomy_of_an_ai_agent.png`) happened inside a James-driven `/grill-with-docs` session (commit `cbfcb06`) | commits `4b29b5c`, `cbfcb06`; `system/session-logs/2026-07-10.md`, `2026-07-11c.md` |
| Structural reorgs (moving directories, changing root layout) | James initiates or approves; Leo executes via the move/repoint checklist below. Both July reorgs were James-driven (7/10 by hand, 7/11c via `/grill-with-docs`) | session logs 2026-07-10, 2026-07-11c |
| New top-level directory | Needs a stated reason to exist at root; default home is `system/`. Rule locked 2026-07-11 in `AGENTS.md` §Folder Structure: "root dirs answer 'what is this repo about'... Anything only Leo touches lives inside `system/`." Root = exactly 6 dirs: `work/ self/ kb/ scripts/ prompts/ system/` (+ root files + `inbox` symlink) | `AGENTS.md` §Folder Structure |
| Spending decisions (e.g. re-enabling remote triggers) | **James.** Two remote triggers exist but are disabled for cost — Daily KB Scout + Overnight KB Work, disabled 2026-04-05 "after James decided on-demand over automatic"; backlog says "Re-enable via Leo when ready" — i.e. when *James* is ready | `backlog.md` (Overnight KB automation row), `system/session-logs/2026-04-05-4.md` |
| Promoting an instinct to an AGENTS.md/CLAUDE.md principle | Confidence ≥ 0.8 → *propose*; James must agree (see §Instinct promotion) | `.claude/skills/end-session/SKILL.md` Phase 4b |
| Routine session work (context edits, session log, instinct enrichment, KB ops) | No gate — commit and push at session end | instinct `always-commit-and-push` |

Nothing in this skill routes around these gates. Outbound stays human-gated.

## The move/repoint checklist (the repo's most important discipline)

Codified as instinct `system/instincts/repoint-structure-docs-on-file-moves.md` (created 2026-07-11, confidence 0.7, 2 drift instances as evidence). Applies to ANY file/folder move or rename — whether James did it by hand or Leo executes it.

**The two incidents behind it (both 2026-07-10/11):**
1. The 2026-07-10 hand-reorg (commit `4b29b5c`, 1,572 renames: 1,568 R100 + 2 R099 + 2 R095) re-pointed live prose references but missed `AGENTS.md` §Folder Structure (still showed `interview_prep/learning/sideprojects` under `work/`) and `.gitignore` — the `interview_prep/aman_*.pdf` patterns went silently dead (verifiable: `git show 4b29b5c:.gitignore | grep interview_prep` shows the un-prefixed patterns while the files had moved to `self/interview_prep/`). Both found and fixed a day later in `cbfcb06`.
2. Same cleanup session: moving `notebooklm/` → `system/notebooklm/` surfaced a **stale mac-leo absolute path** (`/Users/jamesli/code/leo/...`) hardcoded in `.claude/agents/search.md`. Machine-local absolute paths are the silent breakage class — they can't be caught by relative-path greps alone.

**The checklist — run all of it, in order:**

1. **`git mv`, never plain `mv`** — history preserved. (Stated in the instinct and in `system/session-logs/2026-07-11c.md`: "All git-mv renames — history preserved.")
2. **Re-point live `.md` references** — but *skip historical docs* (see next section).
3. **`AGENTS.md` §Folder Structure block** — it is a map, and maps go stale silently.
4. **`.gitignore` path patterns** — they rot without any error message.
5. **`.claude/agents/*.md` and `.claude/skills/*/SKILL.md` hardcoded paths** — including *absolute* paths; watch for stale machine-local ones (pc-leo `/home/james/src/leo`, mac-leo `/Users/jamesli/code/leo`).
6. **`system/file_index.md`** — the canonical context-file index, read by `/context-update`.
7. **Grep the old path root-wide to verify zero live refs remain:**

```bash
# covers .md, .gitignore, .claude/, scripts/ — everything tracked
git grep -n "old/path" -- . | grep -v "system/session-logs/" | grep -v "system/memory_archive_2026-06-26/" | grep -v "system/export/" | grep -v "system/monthly-summaries/"
```
Expected result: only hits in historical/archive locations (which are correct as-is) or zero.

8. **After bulk moves, audit for silent deletions** before and after committing:

```bash
# pre-commit: any unexpected deletions in the working tree?
git status --porcelain | grep -E "^.?D"
# post-commit: any D lines hiding among the renames?
git show --name-status -M HEAD | grep "^D"
```

**The incident behind step 8:** the 2026-07-10 reorg silently dropped `work/people/daniel_liu_team_2026-07.md` — deleted, not moved. It was caught during the index-rebuild/re-point pass (inferred from commit-message ordering in `4b29b5c`; the log states it was "restored by Leo pending James's confirm" because `org_design_proposal` references it). The final commit contains zero D lines only because Leo restored the file before committing. In a 1,572-rename diff, one deletion is invisible to eyeballs — grep for it.

## Historical docs stay un-repointed — BY RULE

Only **live** references get re-pointed. These keep old paths deliberately, as historical record:

- `system/session-logs/` (all session logs)
- `system/memory_archive_2026-06-26/` (pre-consolidation memory backup)
- `system/export/` (point-in-time tool-transfer snapshots)
- `system/monthly-summaries/` and any archive/point-in-time doc

Source: instinct `repoint-structure-docs-on-file-moves` ("skip historical docs — session logs, archives, memory archive, point-in-time snapshots describe where things were, correctly") and `system/session-logs/2026-07-11c.md` ("Historical docs (session logs, archives, memory archive, export snapshots) deliberately left as-is"). `system/file_index.md` applies the same rule textually — its pre-split rows carry a banner noting the paths predate the 2026-06-11 work/self split.

Corollary: when your step-7 grep returns hits inside these directories, that is the *correct* end state, not remaining work.

## Commit conventions

From the 262-commit history (count as of 2026-07-12, `git rev-list --count HEAD`).

**Message genres** (verified counts as of 2026-07-12):

| Genre | Pattern | Count | Example |
|---|---|---|---|
| Session log commit | `Session YYYY-MM-DD[b/c/…]: dense summary` | 95 | `Session 2026-07-11c log: root layout cleanup captured; new instinct repoint-structure-docs-on-file-moves` (`2298bd4`) |
| Imperative work commit | `Fix …` / `Add …` / `Phase N: …` / `<Area>: …` | most of the rest | `Root layout cleanup: 6-dir root, Leo-internals consolidated under system/` (`cbfcb06`) |
| Context update | `Context update YYYY-MM-DD: …` | 6 | `Context update 2026-07-07: REORG APPROVED — …` (`563f740`) |

**Trailers** — both, on every Claude-authored commit:

```
Co-Authored-By: Claude <model name> <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_<id>
```

`Co-Authored-By` dates to the April commits (e.g. `26a45ae` carries `Claude Opus 4.6 (1M context)`); the `Claude-Session` URL trailer is standard since **2026-06-23** — earliest occurrence is `702b06f` (verified via `git log --reverse --grep='Claude-Session'`). The model name in the trailer is whatever model actually ran the session (`Claude Fable 5`, `Claude Opus 4.8 (1M context)`, etc.).

**Session-end commit composition:** a session's work + its session log + `system/file_index.md` bump (when context changed) + any new/enriched instincts + their `INDEX.md` lines commit **together** as one commit. Verified pattern: `2298bd4` (backlog + INDEX.md + new instinct + session log in one commit), `2c532b0` (journal + goals + stakeholders + backlog + instinct + INDEX).

**Always commit AND push at session end, even if the log is skipped.** Instinct `always-commit-and-push` (created 2026-06-26, migrated from an 2026-04-01 feedback memory: "Lost work is the high-downside failure this prevents"). Enforcement history: `26a45ae` (2026-04-04) added a MANDATORY label + push-success verification + a final Phase-6 commit to end-session after self-improvement-phase changes went uncommitted. The current `end-session/SKILL.md` Phase 3 carries the surviving form: review `git status`, write a real message (not "end session"), `git add -A`, commit, push.

## Skill-file discipline (SKILL.md casing + prompts/ sync)

**`SKILL.md` uppercase is the source of truth.** A lowercase `skill.md` duplicate in the same directory SHADOWS the real file — the loader picks it up instead.

**The incident:** `f429fb4` (2026-04-04) — "The old skill.md was being loaded instead of the updated SKILL.md, causing end-session to use outdated instructions." Fix was to delete the stale lowercase duplicate.

**Current state (as of 2026-07-12, verified by `find .claude/skills -maxdepth 2 -iname 'skill.md'`):** three skills still have *only* a lowercase `skill.md` — `debrief`, `ingest`, `search`. They are not shadowed (no uppercase twin exists), so they work today; but never create an uppercase twin next to them without deleting the lowercase file, and if you touch them, renaming to uppercase `SKILL.md` (via `git mv`) is the standardizing move.

**prompts/ sync rule:** 8 workflows are flattened into `prompts/` for non-Claude tools (Codex/Gemini/Cursor/Aider): `start-session`, `end-session`, `prep`, `draft-email`, `debrief`, `coach-check`, `grill-me`, `thinking-partner` (per `prompts/README.md`; note the root `CLAUDE.md` says "five most-used" — the README's list of 8 matches the actual directory contents and wins). For Claude Code the canonical source is `.claude/skills/<name>/SKILL.md`; the prompts/ file is **derivative and must be re-synced whenever the SKILL.md changes**. Precedent: `7052047` updated both `.claude/skills/end-session/SKILL.md` *and* `prompts/end-session.md` in one commit.

## Migration rule — retiring a system

When retiring a system (a memory store, a tool, a directory), **grep EVERY skill, agent, hook, and doc for the retired term** before declaring the retirement done.

**The incident:** the 2026-06-26 auto-memory retirement left a straggler — `end-session` still said "save to auto memory" — fixed in `7052047` (2026-06-26): "The memory consolidation retired ~/.claude auto-memory, but end-session (SKILL.md + prompts/ twin) still said 'save to auto memory.'" Same commit also caught a stale `system/leo_backlog.md` path and a dead promotion target — retirement stragglers cluster.

```bash
git grep -ni "retired-term" -- .claude/ prompts/ scripts/ AGENTS.md CLAUDE.md system/
```

Current status of that specific retirement (verified 2026-07-12): `scripts/hooks/detect-corrections.sh` is repointed — it now instructs "capture as an INSTINCT in system/instincts/... The ~/.claude auto-memory store is retired — do NOT save memories there." (A vestigial unused `MEMORY_DIR` variable remains at the top of the script; harmless.) `~/.claude/projects/-home-james-src-leo/memory/MEMORY.md` itself carries the retirement banner.

## Instinct promotion (the ≥0.8 gate)

Mechanics live in `.claude/skills/end-session/SKILL.md` Phase 4b (full lifecycle theory is `leo-research-methodology`'s home). Change-control-relevant facts:

- New instinct starts at confidence **0.3**; corrections bump **+0.15**, confirmations **+0.1**; cap **0.95** ("never fully certain").
- At confidence **≥ 0.8**: flag for promotion to a CLAUDE.md/AGENTS.md operating principle or a skill modification — and **present the candidate to James**: "This instinct has hit 0.8 confidence — ready to promote to [target]. Agree?" Promotion is a proposal, not an auto-apply.
- Every new/enriched instinct also gets a one-line entry in `system/instincts/INDEX.md` (that's what the SessionStart hook injects).
- Only behavioral patterns become instincts — one-time factual corrections route to context files per the AGENTS.md routing guide.

## When NOT to use this skill

- **What happened historically, with full incident narratives** → `leo-failure-archaeology` (this skill only carries the incident kernel behind each rule).
- **Symptom → triage when something is currently broken** → `leo-debugging-playbook`.
- **Hook wiring, permissions, venvs, model pins, credentials** → `leo-config-and-flags`.
- **Day-to-day session lifecycle and KB ops** (running start/end-session, what a normal session commit contains operationally) → `leo-run-and-operate`.
- **Which design decisions are load-bearing and why** → `leo-architecture-contract`.
- **How a hunch becomes an adopted change / full instinct lifecycle & demotion discipline** → `leo-research-methodology`.
- **Docs formats, house style, live-vs-historical writing rule as a *writing* concern** → `leo-docs-and-writing` (this skill owns the *re-pointing* consequence of that rule).

## Provenance & maintenance

Authored 2026-07-12 from live repo state + git archaeology (`git show`/`git log` only; no mutations). All SHAs, counts, and file quotes verified by direct read or read-only command on pc-leo. Two claims labeled as inferred/norm-not-written above: (a) the daniel_liu_team deletion being caught "during the index-rebuild pass" (inferred from commit-message ordering), (b) "deleting James-authored files requires his confirm" (norm from two data points, no written rule).

Re-verification one-liners per fact class:

| Fact class | Re-verify with |
|---|---|
| Commit count (262) & genre counts (95 Session / 6 Context update) | `git rev-list --count HEAD`; `git log --format='%s' \| grep -c '^Session '`; `… \| grep -c '^Context update'` |
| Cited SHAs still say what's claimed | `git show --stat cbfcb06 4b29b5c 702b06f 26a45ae f429fb4 7052047 2298bd4` |
| Earliest Claude-Session trailer | `git log --reverse --format='%h %ad' --grep='Claude-Session' \| head -1` |
| Reorg rename/deletion profile | `git show 4b29b5c --name-status \| awk '{print $1}' \| sort \| uniq -c` |
| .gitignore rot incident | `git show 4b29b5c:.gitignore \| grep interview_prep` vs `grep interview_prep .gitignore` |
| Move/repoint instinct text | `cat system/instincts/repoint-structure-docs-on-file-moves.md` |
| Instinct count (41 + INDEX) | `ls system/instincts/ \| wc -l` (expect 42 files) |
| Lowercase skill.md stragglers (debrief/ingest/search) | `find .claude/skills -maxdepth 2 -iname 'skill.md' \| grep -v SKILL.md` |
| prompts/ flattened set (8) | `ls prompts/` + `cat prompts/README.md` |
| Root-dir rule & 6-dir root | `sed -n '/## Folder Structure/,+3p' AGENTS.md`; `ls -d */` at repo root |
| Promotion gate wording | `grep -n "0.8" .claude/skills/end-session/SKILL.md` |
| Outbound gating | `grep -n "Never send elsewhere" .claude/skills/send-me/SKILL.md`; `head system/outbound_log.md` |
| Remote triggers still disabled | `grep -n "remote trigger" backlog.md` |
| detect-corrections repoint | `tail -15 scripts/hooks/detect-corrections.sh` |
