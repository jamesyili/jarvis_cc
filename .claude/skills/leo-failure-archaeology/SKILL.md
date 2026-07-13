---
name: leo-failure-archaeology
description: The Leo repo's incident chronicle - every major investigation, dead end, revert, and repair as symptom, root cause, evidence (commit SHAs), status. Load this before re-investigating anything that feels familiar, before proposing a system that may have been tried and reversed (platform memory stores, cloud automation), when a debugging session needs the full story behind a rule, or when writing anything that cites Leo's history. Keywords - incident, revert, reversal, post-mortem, why is there a rule about, has this happened before, memory migration, auto-memory, reorg, dropped file, rate limit death, settled battle.
---

# Leo Failure Archaeology

The chronicle, in incident order. Format: symptom → root cause → evidence → status. Repo history: 262+ commits since 2026-03-27. Fast triage of a live problem → [leo-debugging-playbook]; the design lessons distilled → [leo-architecture-contract].

## Settled battles — do not re-fight

| # | Incident | Lesson now encoded as |
|---|---|---|
| A | Decision-persistence crisis | Hook-enforced persistence + mandatory push-verify |
| B | consult-notebook miswire | ERROR failsafe + query_log audit trail |
| D | Pinsight→Pinkerton rebrand | Clean-sweep rename pattern (grep residuals to zero) |
| F | SessionStart sync gap | Hook-enforced auto-pull (clean-tree, ff-only) |
| G | Memory round-trip | Repo-tracked over platform store, permanently |
| H | Reorg dropped file | Repoint checklist instinct + name-status D-line audit |

## A. Decision-persistence crisis (2026-04-04)

- **Symptom:** prioritization decisions didn't survive across conversations.
- **Root cause:** decisions lived only in volatile context; end-session didn't enforce commit/push; a stale lowercase `skill.md` shadowed the updated `SKILL.md` so end-session ran outdated instructions.
- **Evidence:** `d45e7a0` (three-layer safeguard), `26a45ae` (mandatory push-verify), `f429fb4` (removed the shadow duplicate) — all within ~40 minutes.
- **Status:** SETTLED. Became the hook architecture. Residue: three lowercase `skill.md` files still exist (debrief, ingest, search) — the shadow-bug class is live if anyone adds an uppercase twin.

## B. consult-notebook miswire (2026-04-11)

- **Symptom:** /consult-notebook returned plausible answers with no real NotebookLM call behind them.
- **Root cause:** agent file had a nonexistent MCP tool name, macOS paths on Linux, no hard "must call the tool" instruction.
- **Evidence:** `b99c388`; backlog Build row "Fix consult-notebook agent live querying."
- **Status:** SETTLED (agent side: ERROR failsafe, slug ids, audit trail to `system/notebooklm/query_log.md`). The **skill** side has drifted stale again (4 notebooks, UUID ids) as of 2026-07-13.

## C. NotebookLM auth churn (recurring)

- **Symptom:** consults fail every ~3 weeks.
- **Root cause:** cookie/session expiry; re-auth is manual (`setup_auth`, browser).
- **Evidence:** `3870b23` (04-25 fix); failures logged 04-21, 05-02, 07-02 in `query_log.md`; 07-02 also surfaced the UUID-vs-slug bug.
- **Status:** OPEN — proactive re-auth unbuilt; manual cadence accepted.

## D. Pinsight → Pinkerton rebrand (2026-05-16)

- **What:** 9 files renamed (git-mv form, history kept), 103 repo files + 10 memory files rewritten, zero residual references.
- **Near-miss:** same session, a strategy doc inventoried speculative sensor hardware; James caught it → instinct `dont-inventory-speculative-artifacts` (speak only to what exists + the extension pattern).
- **Evidence:** `a5559d4`.
- **Status:** SETTLED. The rename pattern to copy; the risk is fabricated content, not the mechanics.

## E. Path drift after prompts/ split (2026-05-23)

- **Symptom:** draft-email pointed at moved paths after `prompts/` was created.
- **Evidence:** `d233cdb` ("sync draft-email path drift"), `cfcef7c`.
- **Status:** SETTLED as an instance; the *class* (drift after structural change) is Leo's dominant failure mode — recurs in F, H, and the K catalog.

## F. SessionStart sync gap (2026-06-26)

- **Symptom:** one machine silently never pulled — sessions ran on stale context.
- **Root cause:** git sync was model-executed inside /start-session (skippable), and hooks were mis-documented (`~/.claude/settings.json`, whose hooks block is empty, instead of repo `settings.local.json`).
- **Evidence:** `14270bf` (hook auto-pull), `9ca6865` (doc fix). Same day: a stash-pop collision (stashed deletion vs incoming edit) forced stash→pull→pop hardening in start-session.
- **Status:** SETTLED. Contract: clean-tree-only, `--ff-only`, `timeout 20`, dirty tree reported not pulled.

## G. The big reversal — memory round-trip (2026-04-04 → 2026-06-26)

The repo's deepest lesson. A ~12-week detour, fully undone:

- 2026-04-04 `2468264`: deleted `system/instincts/`, moved behavioral memory into Claude's `~/.claude` auto-memory store. Ran ~2.5 months; 91 memory files accumulated.
- 2026-06-26 (12 commits, 02:48–04:26): full reversal. `4dc8020` archive all 91 → `system/memory_archive_2026-06-26/`; `d0620e1` tiering; `f04649c` instincts become the single system; `d4fb026` 31 feedback memories → 12 new + 6 enriched instincts; `e784384` 19 fact memories → context files; `2ce769e` retire auto-memory (MEMORY.md becomes a redirect stub); `7052047` straggler — end-session still said "save to auto-memory."
- **Root cause of the reversal:** two parallel memory systems, no single source of truth; the platform store wasn't git-tracked or usable by non-Claude tools.
- **Status:** SETTLED, permanently. Lessons: never move a git-tracked transferable system into an opaque platform store; running two memory systems means paying to merge them later; migrations leave stragglers — **grep every skill for the retired term** (`7052047`).

## H. The 1,572-file reorg drop (2026-07-10/11)

- **What:** hand-reorg moved interview_prep/learning/sideprojects/writing_style into `self/` etc. Commit `4b29b5c`: 1,572 renames + 13 modifies ("~1,585" in prose is the rounded figure).
- **Incident:** `work/people/daniel_liu_team_2026-07.md` came out **deleted, not moved**. Caught by the file-index rebuild / cross-reference pass; restored within the same commit (git log --follow shows a no-op). James's explicit confirm was never logged; file exists at HEAD.
- **Next-day repairs (`cbfcb06`, root 13→6 cleanup):** `.gitignore` still carried pre-reorg paths (patterns silently dead); AGENTS.md §Folder Structure had gone stale; another stale macOS absolute path found in the consult-notebook agent.
- **Status:** SETTLED as discipline → instinct `repoint-structure-docs-on-file-moves` (checklist: AGENTS.md structure block, .gitignore, .claude hardcoded paths, file_index, git mv, grep old path). After any bulk move: audit `git diff --name-status` for unexpected `D` lines.

## I. send-me str/Path crash (2026-07-10)

`append_outbound_log` requires `Path` objects; a `str` crashed it. `04656a0`; documented in send-me SKILL.md. SETTLED.

## J. graphify rate-limit death (2026-04-08)

- **Symptom:** graph Phase 1 build died mid-run on the subscription session limit; 13 of 123 chunks never extracted (verified missing set: 104, 109, 111, 112, 113, 116–123 — mostly Lenny's tail).
- **Aftermath:** SHA256 cache empty → naive `--update` would re-extract everything; `/tmp` originals gone; `kb/.kb/graph/raw_chunks/` (110 files, manifest says `phase1-salvage`) is now the **only copy** and is **gitignored**. Backlog row "Preserve raw chunks — Not started" is stale: it happened.
- **Status:** OPEN (13-chunk backfill needs a missing-file-only strategy). No dedicated commit — the event lives only in backlog prose. Same failure mode recurred 2026-07-12: a 17-agent authoring workflow died wholesale on session limits. Rule: forecast cost, checkpoint, resume.

## K. Standing staleness debt (as of 2026-07-13)

Known-stale, not yet repaired: `system/leo-overview.md` (dated 2026-04-05 — describes the retired auto-memory as live, 4 notebooks not 5, "24 skills", "25 sessions"); `.claude/agents/search.md` (macOS paths); `.claude/skills/weekly-review/SKILL.md` (`AIContext/` paths); `.claude/skills/consult-notebook/SKILL.md` (4 notebooks, UUIDs); session-log trim rule (~20 files documented, 125+ on disk, unenforced by choice); `search_index.json` (2026-04-05) vs corpus growth; two security instincts still say `work+self/` (pre-split name; rule itself still correct).

## When NOT to use this skill

- Live triage of a current failure → [leo-debugging-playbook]
- The design principles these incidents produced → [leo-architecture-contract]
- Executing a move/migration correctly today → [leo-change-control]

## Provenance & maintenance

Authored 2026-07-13; SHAs verified against `git show --stat` during 2026-07-11/12 discovery. Re-verify:
- Any SHA: `git show --stat <sha> | head -5`
- Reorg counts: `git show 4b29b5c --name-status | awk '{print $1}' | sort | uniq -c`
- raw_chunks state: `ls kb/.kb/graph/raw_chunks/ | wc -l` (expect 110)
- Staleness catalog K: `grep -n 'Last updated' system/leo-overview.md; grep -n AIContext .claude/skills/weekly-review/SKILL.md; ls system/session-logs | wc -l`
