---
name: leo-architecture-contract
description: >
  The load-bearing design decisions of the Leo repo, WHY each exists (the incident behind it),
  the invariants that must stay true, and the known-weak points. Load this skill BEFORE
  proposing any structural change to Leo — moving directories, changing where memory lives,
  adding a root dir, touching hooks wiring, changing what goes in kb/ vs work//self/, adding
  a new machine or tool, or "simplifying" anything that looks redundant. Also load when you
  need to answer: "why is it built this way?", "can I put X in kb/?", "why not use Claude's
  auto-memory?", "why is there both AGENTS.md and CLAUDE.md?", "is it safe to delete/move
  this?", "why does a hook do this instead of the model?". Keywords: architecture, invariant,
  design decision, contract, memory system, instincts, portability, multi-machine, privacy,
  6-root rule, folder structure, weak points, drift.
---

# Leo Architecture Contract

This is the constitution, not a runbook. Eight decisions, each paid for by a real incident;
the invariants they imply; and the weak points stated plainly so you don't rediscover them
the hard way. Full incident stories with diffs live in **leo-failure-archaeology** — this file
carries only enough history to make each rule stick.

Nothing here overrides AGENTS.md, CLAUDE.md, or `system/instincts/` — those are the law;
this skill explains why the law reads the way it does. Structural changes go through the
move/repoint checklist in **leo-change-control** (and the instinct
`system/instincts/repoint-structure-docs-on-file-moves.md`). Do not route around it.

All paths are repo-relative to the Leo repo root unless marked machine-specific.
On pc-leo (this machine, WSL2) the root is `/home/james/src/leo`; on mac-leo it is
`/Users/jamesli/code/leo` (per the comment in `scripts/hooks/session-start.sh`).

---

## Decision 1 — Repo-tracked memory beats platform-store memory

**The rule:** ALL of Leo's persistent state — behavioral memory, facts, session logs — lives
in git-tracked files inside this repo. Never in a tool's private store.

**The incident:** Behavioral memory lived in Claude Code's auto-memory store
(`~/.claude/projects/-home-james-src-leo/memory/`, indexed by `MEMORY.md`) from roughly early
April 2026 (exact start date unverified — the store is outside this repo's git history) until
2026-06-26, when it was fully reversed back into the repo. The audit
(`system/memory_audit_2026-06-26.md`) tiered all 91 memory files and found the store "bloated
with near-duplicates" — ~13 of 21 then-existing instincts had a direct memory twin, because two
parallel memory systems had grown side by side. The consolidation ran as a commit sequence on
2026-06-26: audit `d0620e1` → make instincts the single system + SessionStart loader `f04649c`
→ archive all 91 files `4dc8020` → migrate 31 feedback memories into instincts `d4fb026` →
route 19 fact memories into repo context files `e784384` → retire the store `2ce769e` →
repoint end-session `7052047` → session log `098706a` (plus `9ca6865`, `472f764`, `14270bf`
in the same arc).

**Why:** platform stores aren't git-tracked (no history, no multi-machine sync) and aren't
cross-tool (Codex/Gemini/Cursor can't see them). Both properties are non-negotiable given
Decisions 3 and 7.

**Standing state (verified 2026-07-12):**
- `~/.claude/projects/-home-james-src-leo/memory/MEMORY.md` is a **retirement stub** — it says
  "empty by design — do not add new memories here." Believe it. Never write there.
- Pre-consolidation backup: `system/memory_archive_2026-06-26/` (91 `feedback_*`/fact files +
  the old MEMORY.md).
- The `detect-corrections.sh` hook's output prompt explicitly says the auto-memory store is
  retired and routes captures to `system/instincts/`.

**Invariant:** if a future harness offers a shiny built-in memory feature, the answer is
still no. Anything worth remembering becomes an instinct file or a context-file edit,
committed and pushed.

## Decision 2 — Hooks enforce what models forget

**The rule:** anything that must happen *every session without fail* is done by a shell hook,
not by asking the model to remember to do it.

**The founding incident (2026-04-04):** decisions made mid-conversation were not surviving to
the next conversation. Commit `d45e7a0` ("Fix decision persistence: three-layer safeguard for
state management") added real-time source-file updates, memory backup, and an end-session
backlog-reconciliation phase; `26a45ae` ("Fix end-session: enforce commit/push") hardened
end-session the same day. This is the day Leo learned that model intent does not persist —
only enforced process does.

**The confirming incident (2026-06-26):** git sync was a model responsibility ("pull at
session start") and on one machine it silently never ran, so the machines diverged. Commit
`14270bf` moved sync into the SessionStart hook itself — the "reliable download-from-git-every-
time guarantee" (its own comment, `scripts/hooks/session-start.sh`).

**Standing state (verified 2026-07-12):** four hooks, wired in the repo's
`.claude/settings.local.json` (NOT `~/.claude/settings.json`), scripts in `scripts/hooks/`:
SessionStart `session-start.sh` (git sync + inject instincts INDEX + last 2 session logs),
PreCompact `pre-compact.sh`, Stop `suggest-compact.sh` + `detect-corrections.sh`. Full wiring
detail is **leo-config-and-flags**' home.

**Invariant:** when you find yourself writing "Leo should always remember to X" into a skill
or context file, stop — that's a hook (or a hook-injected reminder), or it will eventually
not happen.

## Decision 3 — Layered base context: the portability architecture

**The rule:** base context is tool-neutral; tool-specific machinery is layered on top, never
mixed in.

| Layer | File | Role |
|-------|------|------|
| Base | `AGENTS.md` | Tool-neutral entry point: who James is, modes, principles, folder structure, routing. Every tool reads this. |
| Claude Code extensions | `CLAUDE.md` | Skill registry, sub-agents, hooks, memory system — things with no equivalent in Codex/Gemini/Cursor/Aider. Points to AGENTS.md as base. |
| Gemini | `GEMINI.md` | A symlink to `AGENTS.md` (verified: `GEMINI.md -> AGENTS.md`). |
| Workflows for non-Claude tools | `prompts/` | The most-used skills flattened into tool-neutral prose (8 workflow files as of 2026-07-12: start-session, end-session, prep, draft-email, debrief, coach-check, grill-me, thinking-partner + README). `.claude/skills/*/SKILL.md` stays the source of truth for Claude Code. |

**Why:** Leo predates any single harness surviving. The consolidation in Decision 1 only paid
off because the repo, not Claude, is the system of record — same logic here. A rebuilt machine
or a different agent CLI gets a working Leo from `AGENTS.md` + `prompts/` alone.

**Invariant:** never put Claude-Code-only mechanics into `AGENTS.md`; never put base identity/
routing content only into `CLAUDE.md`. When a workflow skill changes materially, its
`prompts/` flat version needs the same change (this is a known manual-sync burden — see weak
points).

## Decision 4 — The 6-root rule (locked 2026-07-11)

Quoted verbatim from `AGENTS.md` §Folder Structure:

> Six root directories. The rule (locked 2026-07-11): **root dirs answer "what is this repo
> about" — James's work, James's self, knowledge, and the machinery. Anything only Leo touches
> lives inside `system/`.** New top-level directories need a reason to exist at root; the
> default home for infra, outputs, and tool-transfer material is `system/`.

The six: `work/ self/ kb/ scripts/ prompts/ system/` (verified 2026-07-12; the `inbox/`
symlink at root is gitignored and doesn't count — it's a Google Drive mount, see Decision 8).
Root files: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `backlog.md`.

**The incident:** the root had accreted Leo-internal directories; commit `cbfcb06`
(2026-07-11, "Root layout cleanup: 6-dir root, Leo-internals consolidated under system/")
collapsed them into `system/` and the rule was locked into AGENTS.md the same day. The
companion instinct `repoint-structure-docs-on-file-moves` (created from that cleanup's
corrections) is why moves now carry a repoint checklist.

**Invariant:** a proposal to add a seventh root directory is wrong by default. Put it in
`system/` and move on; escalate to James only if it genuinely answers "what is this repo
about."

## Decision 5 — Instincts vs facts: behaviors and facts live in different systems

**The rule:**
- **Behaviors** (trigger → behavior corrections that should change how Leo acts) →
  `system/instincts/` — one file per instinct with frontmatter
  (id/trigger/behavior/confidence/evidence_count/created/last_updated/status) and dated
  evidence, plus one line in `system/instincts/INDEX.md`. The INDEX (41 instincts as of
  2026-07-12; 42 files counting INDEX.md) is injected into every session by the SessionStart
  hook.
- **Facts** (stakeholder intel, project state, profile, infra) → context files per the
  AGENTS.md routing guide: Dylan → `work/people/dylan_archive.md`, other stakeholders →
  `work/people/stakeholders.md`, direct reports → `work/people/team_members.md`, projects →
  `work/projects/`, goals → `self/goals.md`, coaching → `work/coaching.md`, infra →
  `system/leo-overview.md`.

**Why:** the 2026-06-26 audit (Decision 1) showed that when one store holds both, you get
near-duplicate sprawl and neither loads reliably. Instincts must load *every* session (hence
hook-injected INDEX, Decision 2); facts must load *contextually* (hence the routing guide and
Context Loading Guide in AGENTS.md).

**Invariant:** a correction from James that applies to future sessions becomes an instinct
(enrich existing before creating new — check INDEX.md first). A one-off factual correction
goes to the owning context file. Never both, never neither. Lifecycle discipline (confidence,
demotion) is **leo-research-methodology**'s home.

## Decision 6 — Agent isolation for verbose and adversarial work

**The rule:** work that would pollute or bias the main context runs in sub-agents
(`.claude/agents/` — 4 as of 2026-07-12: consult-notebook, karen, code-planner, search).

- **consult-notebook** (Sonnet, background): NotebookLM RAG output is verbose; only the
  distilled synthesis returns to main context. The full raw response is appended to
  `system/notebooklm/query_log.md` as an audit trail. That audit trail exists because a prior
  version of the agent **fabricated plausible syntheses without calling NotebookLM at all** —
  confirmed twice (2026-04-07, 2026-04-09), rewritten 2026-04-11 with a fail-loudly ERROR
  contract and a mandatory log append ("the audit trail is the mechanism that catches
  regressions" — the agent file's own words). Full story: **leo-failure-archaeology**.
- **karen** (Opus, background, ~every 20% of context window): adversarial advisor with her own
  institutional memory at `system/karen_observations.md`. Isolated so the main thread stays
  agreeable-by-design while she doesn't. Her blind-spot rule (CLAUDE.md): verify real-world
  status with James before building an avoidance narrative — work-leo activity is invisible
  here (Decision 7).

**Invariant:** don't inline NotebookLM queries or adversarial reviews into main context to
"save a spawn." The isolation is the feature. Counter-invariant (instinct
`main-context-for-sequential-writes`): 5+ sequential query-then-edit steps run in MAIN
context — spawned agents don't persist edits reliably.

## Decision 7 — Multi-machine: git is the spine; work-leo is another country

**The machines:**

| Machine | Repo root | Relationship |
|---------|-----------|--------------|
| pc-leo | `/home/james/src/leo` (WSL2) | this repo |
| mac-leo | `/Users/jamesli/code/leo` | same repo, synced via git |
| work-leo | Pinterest laptop, **separate repo** | separate source of truth — NOT synced |

**The sync contract** (read it in `scripts/hooks/session-start.sh`, verified 2026-07-12):
SessionStart auto-pull is safe by construction — repo root derived from the script's own
location (it was once hardcoded to the pc-leo path and broke on the Mac); pulls ONLY a clean
tree; `--ff-only`; `timeout 20`; a dirty tree is **reported, not pulled** (/start-session
handles that via stash); failure leaves the repo untouched. The behavioral complement is the
instinct `always-commit-and-push` — session end always commits and pushes, even if the log is
skipped. Pull is a hook; push is an instinct; together they are the spine.

**work-leo is invisible by design:** per instinct
`system/instincts/work-leo-execution-scope.md`, the two instances don't share state. When
James says something is handled on work-leo, the first hypothesis is "work-leo is handling
it," never "it's not getting done." Do not flag work-leo tasks as unfinished from here, and do
not build accumulation narratives on their absence (Karen's blind-spot rule, CLAUDE.md).

**Invariant:** never weaken the hook's clean-tree/--ff-only/timeout guards to "make sync more
aggressive." Every guard is load-bearing: the alternative is silently clobbered uncommitted
work or a hung session start when offline.

## Decision 8 — Privacy invariants (hard rules, no judgment calls)

1. **Pinterest internals never go in `kb/`.** The KB is potentially indexable/shareable;
   files naming Pinterest stakeholders or situational context live under `work/` (or `self/`),
   never `kb/`. Source: instinct `system/instincts/pinterest-internals-not-in-kb.md` (a hard
   placement rule, distinct from the felt-ownership taxonomy).
2. **`inbox/` is ls-only.** It's a gitignored symlink to the Google Drive "Leo Inbox" folder.
   `ls` is fine; reading file bodies is not (pollutes context). An explicit "read inbox/X"
   from James overrides. Source: instinct `system/instincts/never-read-inbox-contents.md`.
3. **Credentials live outside the repo** in `~/.config/leo/` (machine-specific; on pc-leo
   contains `google_credentials.json`, `google_token.json`, `drive_folders.json` — verified
   2026-07-12). `.gitignore` also blocks those filenames inside the repo as defense in depth,
   plus `notebooklm_cookies.txt`.
4. **Outbound is human-gated.** Drafts stage in `system/outbound_drafts/`;
   `system/outbound_log.md` is the send audit trail (per AGENTS.md §Folder Structure). No
   skill may auto-send externally.

**Invariant:** these are not preferences to weigh — a violation is an incident. When in doubt
about placement, `work/` is the safe default for anything Pinterest-flavored.

---

## The invariants, in one table

| # | Invariant | Enforced by | Breaks if you... |
|---|-----------|-------------|-------------------|
| 1 | All persistent state is repo-tracked | Retirement stub in old MEMORY.md; detect-corrections prompt | write to any platform memory store |
| 2 | Must-happen-every-session ⇒ hook, not model intent | `.claude/settings.local.json` + `scripts/hooks/` | encode a guarantee as prose in a skill |
| 3 | AGENTS.md tool-neutral / CLAUDE.md Claude-only / prompts/ flattened | file layering + GEMINI.md symlink | mix layers, or edit a skill without its prompts/ twin |
| 4 | Exactly six root dirs; Leo-internal ⇒ `system/` | AGENTS.md §Folder Structure (locked 2026-07-11) | add a root dir |
| 5 | Behaviors ⇒ instincts; facts ⇒ context files | SessionStart INDEX injection + AGENTS.md routing guide | save a fact as an instinct or a behavior as a note |
| 6 | Verbose/adversarial work is agent-isolated; 5+ sequential edits are not | agent definitions + instinct `main-context-for-sequential-writes` | inline RAG output, or delegate bulk edits to a spawn |
| 7 | Sync = clean-tree + --ff-only + timeout pull, always-push; work-leo separate | `session-start.sh` + instincts `always-commit-and-push`, `work-leo-execution-scope` | force-pull, skip push, or reason about work-leo state |
| 8 | Pinterest ∉ kb/; inbox ls-only; creds in `~/.config/leo/`; outbound human-gated | instincts + .gitignore + outbound staging | shortcut any of the four |

---

## Known-weak points (stated plainly, as of 2026-07-12)

The dominant failure class is **drift after structural change**: the repo moves, and
hardcoded paths in skills/agents/docs silently keep pointing at the old world. The instinct
`repoint-structure-docs-on-file-moves` is the countermeasure, but it only covers moves made
*after* it existed (2026-07-11). Current confirmed drift, verified by direct read 2026-07-12:

1. **`.claude/agents/search.md` is stale on three axes:** its Knowledge Locations block mixes
   mac-leo absolute paths (`/Users/jamesli/code/leo/...`) with one pc-leo path (line 23); it
   points articles at `self/learning/articles/` ("~945+ articles") — that directory does not
   exist (the KB lives at `kb/`, 2,600+ articles per AGENTS.md). The agent degrades to
   searching only whichever paths happen to resolve on the current machine.
2. **`.claude/skills/weekly-review/SKILL.md` reads dead paths:** lines 14–19 reference
   `AIContext/journal.md`, `AIContext/goals.md`, etc. No `AIContext/` directory exists at
   root. The skill will come up empty or hallucinate around missing files.
3. **`.claude/skills/consult-notebook/SKILL.md` has a stale notebook table:** it lists 4
   notebooks with raw UUID IDs (lines 13–18) and still references "AIContext" (line 56). The
   correct registry is **5** notebooks with slug IDs (`wes-kao-frameworks`,
   `coaching-patterns`, `decisive-framework`, `ml-ai-system-design`,
   `ethan-evans-frameworks`) — source of truth `system/notebooklm/notebooks.md`, correctly
   mirrored in `.claude/agents/consult-notebook.md`. The skill's table is missing Ethan Evans
   entirely.
4. **`system/leo-overview.md` says "Last updated: 2026-04-05"** — ~3 months stale. It claims
   "5 agents" (now 4) and is billed as the portable self-description handed to repo-less
   Claude instances, so its staleness exports.
5. **The session-log trim rule is documented but unenforced:** `prompts/end-session.md:36`
   and `.claude/skills/session-log/SKILL.md:49` both say keep ~20 files/entries;
   `system/session-logs/` holds **125** files. Nothing mechanical enforces it (Decision 2
   says this will therefore keep not happening).
6. **Two hooks and one agent silently degrade off pc-leo:** `pre-compact.sh:6` hardcodes
   `/home/james/src/leo/system/compaction-log.md`; `detect-corrections.sh` hardcodes the
   transcript dir `$HOME/.claude/projects/-home-james-src-leo` (the path-encoding of the
   pc-leo repo root — wrong encoding on mac-leo, so it exits 0 without scanning); and
   `.claude/agents/consult-notebook.md` hardcodes the pc-leo absolute path to
   `query_log.md` (~line 69). Only `session-start.sh` derives its root portably. Net effect:
   on mac-leo, compaction logging, correction detection, and possibly the NLM audit append
   are silently off.
7. **`kb/.kb/graph/raw_chunks/` is the only copy of the raw extraction chunks** and it is
   gitignored (verified via `git check-ignore`; the `.gitignore` comment says it's ~7MB,
   "preserved for compute-surprising regeneration"). A machine loss loses it; regeneration
   means re-running extraction. Same for `kb/.kb/graph/cache/`.
8. **The search index never auto-invalidates:** `scripts/kb_search.py` `load_index()` checks
   only that `kb/.kb/search_index.json` exists and parses — no mtime/content check (the
   docstring says "stale/missing" but the code doesn't check staleness). After any KB
   ingest, results are silently stale until `python3 scripts/kb_search.py --rebuild` runs.
   Operational handling: **leo-run-and-operate**; diagnosis: **leo-debugging-playbook**.

Items 1–4 are repair candidates, not repaired — fixing them is a structural-docs change and
goes through the repoint checklist in **leo-change-control**. Do not "helpfully" fix them
mid-unrelated-session without flagging.

---

## When NOT to use this skill

| You actually need... | Go to |
|----------------------|-------|
| The full incident stories with SHAs and diffs | **leo-failure-archaeology** |
| How to classify/gate a change; the move/repoint checklist; commit conventions | **leo-change-control** |
| Symptom → triage for a live failure | **leo-debugging-playbook** |
| Hooks wiring detail, permissions, venvs, model pins, credentials setup | **leo-config-and-flags** |
| Rebuilding the environment on a fresh machine | **leo-build-and-env** |
| Day-to-day session lifecycle and KB ops | **leo-run-and-operate** |
| KB data model, counts, graph concepts | **leo-kb-reference** |
| What counts as evidence; golden inventory | **leo-validation-and-diagnostics** |
| Instinct lifecycle / how a hunch becomes an adopted change | **leo-research-methodology** |
| Docs of record and house style | **leo-docs-and-writing** |
| Open problems (evals-on-Leo, autonomous KB, portability) | **leo-research-frontier** |

---

## Provenance & maintenance

Authored 2026-07-12 from direct reads of repo state at HEAD `2298bd4` plus git archaeology
(`git log`/`git show` on `d45e7a0`, `26a45ae`, `14270bf`, `cbfcb06`, and the 2026-06-26
consolidation sequence `d0620e1`→`098706a`). One explicitly-unverified item: the exact start
date of the retired auto-memory store (outside repo git history).

Re-verification one-liners (run from repo root):

| Fact class | Command |
|------------|---------|
| Six root dirs, no seventh | `ls -d */` (expect work self kb scripts prompts system + gitignored inbox symlink) |
| 6-root rule wording | `grep -A2 'Six root directories' AGENTS.md` |
| GEMINI symlink | `ls -la GEMINI.md` (→ AGENTS.md) |
| prompts/ flattened set | `ls prompts/` |
| Hooks wiring | `cat .claude/settings.local.json` (hooks block; NOT ~/.claude/settings.json) |
| Sync contract | `sed -n '11,32p' scripts/hooks/session-start.sh` (clean-tree, --ff-only, timeout 20) |
| Instinct count | `ls system/instincts/ \| wc -l` (files = instincts + INDEX.md) |
| Memory store still retired | `head -3 ~/.claude/projects/-home-james-src-leo/memory/MEMORY.md` |
| Archive intact | `ls system/memory_archive_2026-06-26/ \| wc -l` |
| Cited commits | `git show --stat --format='%h %ad %s' --date=short d45e7a0 26a45ae 14270bf cbfcb06` |
| Agent roster | `ls .claude/agents/` |
| Notebook registry (5, slugs) | `grep -c '^## ' system/notebooklm/notebooks.md` |
| Weak pt 1 (search agent drift) | `grep -nE '/Users/jamesli\|/home/james\|945' .claude/agents/search.md` |
| Weak pt 2 (weekly-review) | `grep -n AIContext .claude/skills/weekly-review/SKILL.md` |
| Weak pt 3 (consult-notebook skill) | `grep -c '^| \*\*' .claude/skills/consult-notebook/SKILL.md` vs registry |
| Weak pt 4 (overview staleness) | `grep 'Last updated' system/leo-overview.md` |
| Weak pt 5 (log count vs rule) | `ls system/session-logs/*.md \| wc -l` vs `grep -n '~20' prompts/end-session.md` |
| Weak pt 6 (hardcoded paths) | `grep -n '/home/james' scripts/hooks/*.sh .claude/agents/consult-notebook.md` |
| Weak pt 7 (raw_chunks ignored) | `git check-ignore kb/.kb/graph/raw_chunks/ && echo IGNORED` |
| Weak pt 8 (no index invalidation) | `sed -n '201,215p' scripts/kb_search.py` (load_index has no staleness check) |

If any re-verification fails, the drift itself is the finding — update this contract AND check
whether a weak point got fixed (celebrate, then delete it here) or a new one appeared.
