---
name: leo-research-methodology
description: >
  The epistemics of the Leo repo — how a hunch becomes an adopted change, and how
  changes get demoted or retired without losing the trail. Load this skill when you are:
  creating, enriching, or promoting an instinct (system/instincts/); responding to a
  "CORRECTION SIGNAL DETECTED" nudge from the detect-corrections.sh Stop hook; running
  end-session Phase 4b (instinct extraction / confidence bumps / promotion check);
  deciding whether to build, defer, demote, or retire something (backlog.md priority
  changes); opening or closing a "verify next session/next spawn" item; judging whether
  evidence is sufficient before asserting a behavioral pattern about James (Karen-style
  accumulation/avoidance narratives); or hunting for where the next good Leo idea should
  come from. Keywords: instinct lifecycle, confidence 0.3/0.15/0.1/0.8/0.95, promotion
  gate, enrich don't duplicate, demotion, tool-builder trap, collection trap,
  verification debt, carried item, seventh carry, evidence bar, backlog etiquette,
  lab notebook, retire loudly, forwarding address.
---

# Leo Research Methodology — how a hunch becomes an adopted change

This is the repo's discipline for turning observations into durable behavior, and for
un-adopting things without amnesia. Facts below are grounded in repo state and git
history **as of 2026-07-12**; volatile counts are date-stamped. Nothing in this skill
overrides AGENTS.md, CLAUDE.md, or `system/instincts/` — those are law. Promotions into
AGENTS.md require James's explicit agreement (see §1.5); structural file moves go
through the repoint checklist (home: **leo-change-control**); outbound communication
stays human-gated.

---

## 1. The instinct lifecycle (behavioral changes)

The single richest idea source in this repo is James correcting Leo mid-session.
The pipeline that turns a correction into permanent behavior:

```
correction in-session
  → detect-corrections.sh nudge (Stop hook) AND/OR end-session Phase 4b sweep
  → instinct file in system/instincts/ (or enrichment of an existing one)
  → one line added to system/instincts/INDEX.md
  → INDEX.md injected into EVERY session by scripts/hooks/session-start.sh
  → evidence accumulates across sessions (confidence arithmetic below)
  → ≥0.8: flag for promotion to AGENTS.md operating principle / workflow mod
  → promotion happens ONLY with James's explicit agreement
```

**41 instinct files + INDEX.md as of 2026-07-12, all `status: active`**
(`ls system/instincts/*.md | grep -v INDEX | wc -l`).

### 1.1 Detection — two channels

**Channel A: the Stop hook.** `scripts/hooks/detect-corrections.sh` (wired in
`.claude/settings.local.json`, NOT `~/.claude/settings.json`) scans the newest
transcript `*.jsonl` under `~/.claude/projects/-home-james-src-leo/` (machine-specific
absolute — this is the pc-leo path; the project dir name differs on mac-leo).
Incremental scan via marker file `/tmp/leo-correction-marker`; user messages only;
skips `<command-name>`/`<system-reminder>` content. The 13 regex classes (verbatim
from the script, verified 2026-07-12) include:

```
\bno[,.]?\s+(not |don.t |stop )     \bi told you        \bthat.s not what
\bstop (doing|adding|saying)         \bi said            \bplease don.t
\bdon.t (do |add |say |include |summarize|guess)         \byou keep
\bnot like that     \bwrong\b        \bstop\b.*\bing\b   \bagain\b.*\bwrong
\bi already
```

On a hit it prints `=== CORRECTION SIGNAL DETECTED ===` plus instructions: check
INDEX.md first, enrich if a match exists, only capture behavioral patterns (not
one-off factual corrections), never write to the retired `~/.claude` auto-memory.

**Channel B: end-session Phase 4b.** Source of truth: `prompts/end-session.md`
(tool-neutral) mirrored in `.claude/skills/end-session/SKILL.md`. Phase 4b sweeps
the whole conversation for **corrections** (pushback, redirects) AND
**confirmations** (James accepting a non-obvious approach, "yes exactly", or not
pushing back where he easily could have).

### 1.2 The instinct file schema (verified against live files)

```markdown
---
id: kebab-case-name
trigger: When [specific situation where this behavior applies]
behavior: [What Leo should do / not do]
confidence: 0.3
evidence_count: 1
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
status: active
---

## Evidence

### YYYY-MM-DD
> "[Quote or paraphrase]"
Context: [what was happening]
Signal: [correction | confirmation]
```

Observed extensions in real files (all legitimate):

- `Signal: direct instruction` — when James explicitly asks for the instinct
  (`lead-with-next-best-move`, created 2026-07-11 **at confidence 0.7**, not 0.3 —
  a direct instruction warrants a higher start than an inferred pattern).
- `Signal: correction (by edit)` — pattern inferred from James editing Leo's output
  rather than saying anything (`avoid-ai-prose-tells`, 2026-07-10 evidence: James cut
  Leo's epigram sentence in the JJ promo package final pass).
- `Lesson:` lines under evidence entries — scope refinements
  (`avoid-ai-prose-tells` 2026-07-09: "he says 'hyphens' to mean em-dashes AND
  hyphenated compounds").
- `## Related` section cross-linking sibling instincts (`lead-with-next-best-move`
  links 4 others, including how they interact).
- `## Absorbed from auto-memory (2026-06-26)` — provenance from the retired memory
  store (see §5).

### 1.3 Confidence arithmetic (from prompts/end-session.md Phase 4b, verified)

| Event | Delta |
|---|---|
| New instinct (inferred from correction) | start **0.3** |
| New instinct (direct instruction) | higher start is precedented (0.7 observed) |
| Correction (pattern fired again, Leo got it wrong) | **+0.15**, `evidence_count += 1`, append dated evidence |
| Confirmation (Leo applied it, James accepted) | **+0.1**, same bookkeeping |
| Cap | **0.95** — never fully certain, room for edge cases |

Distribution as of 2026-07-12 (from `grep -h "^confidence:" system/instincts/*.md`):
7×0.3, 9×0.4, 1×0.45, 9×0.5, 6×0.6, 1×0.65, 5×0.7, 2×0.75, 1×0.85.

### 1.4 Enrich, don't duplicate

The default on any new signal is: **check INDEX.md first, enrich an existing instinct
if one matches.** Both detection channels say this explicitly. Canonical enrichment
arc: `avoid-ai-prose-tells` — created 2026-06-11 from a North Star drafting correction,
then extended 2026-07-09 to workplace deliverables (correction), confirmed 2026-07-09
evening (proactive application accepted), extended again 2026-07-10 (epigram tell,
correction-by-edit). One instinct, 5 evidence entries, scope sharpened each time —
instead of four overlapping files.

### 1.5 The promotion gate — ≥0.8 flags, James decides

Phase 4b, verbatim mechanic: at confidence ≥0.8, present the candidate to James —
"This instinct has hit 0.8 confidence — ready to promote to [target]. Agree?" Target
is an AGENTS.md operating principle or a workflow modification (the Claude-skill
mirror says "CLAUDE.md / AGENTS.md operating principle or a skill modification").

**The gate flags; it does not auto-promote.** Live proof:
`check-existing-context-before-analyzing` sits at **0.85** (4 evidence entries,
last updated 2026-05-07) and remains an instinct, not an operating principle, as of
2026-07-12. Do not "helpfully" promote it — that requires James in the loop.

A promotion that DID land: AGENTS.md Operating Principle 11 ("Frame career and
stakeholder work from org-needs first") cites its own provenance — "load-bearing in
the 4/22 Dylan prep landing — see `work/journals_and_growth.md` Lesson 6." Adopted
principles carry their evidence trail with them.

### 1.6 Instincts hold behaviors, not facts

Stakeholder intel, project state, and profile facts route to repo context files per
the AGENTS.md routing guide (Dylan → `work/people/dylan_archive.md`, other
stakeholders → `work/people/stakeholders.md`, projects → `work/projects/`, Leo infra →
`system/leo-overview.md`). One-off factual corrections get fixed in the relevant file,
not memorialized as instincts. The old `~/.claude` auto-memory store is retired
(2026-06-26) — never write there (§5 has the retirement anatomy).

---

## 2. The demotion discipline — not-building is a first-class result

Leo treats "we chose not to build this" as a research finding that must be recorded
with the same rigor as a build.

**Rule: every demotion/deferral records WHY + revisit-when, in the backlog row itself.**

Canonical example (backlog.md, graphify Phase 2 row, verified verbatim):

> **Demoted 2026-04-09**: tool-builder trap risk; wiki isn't load-bearing for
> day-to-day thinking yet. Revisit when blog posts + interview prep ladder is underway.

Progress cell reads "Not started — demoted from P1", priority now P2. The session log
(`system/session-logs/2026-04-09.md`) records the same call: "Demoted graphify Phase 2
to P2 (tool-builder trap acknowledged), Phase 3/4 to P3, soft-wiki compile to P2."
This is a working capability frozen by explicit choice **with reversal criteria** —
not abandoned by failure. Anyone reading the row later knows exactly what would
reopen it.

### 2.1 The tripwires that motivate the discipline

The demotion discipline exists because the repo has a named, longitudinally-tracked
failure mode: **building collection/ingestion infrastructure as avoidance of the
harder synthesis work** (the "collection trap" / "tool-builder trap").

- **Karen** (background adversarial agent, spawned ~every 20% of context window;
  writes `system/karen_observations.md`) tracks this under "Avoidance Patterns."
  Documented win condition from the 2026-04-06 entry, verbatim: "no cron
  infrastructure built, no overnight content factories scoped." Her file also
  records when she was only partially right and James's rebuttal inline (2026-04-04
  entry) — the adversarial channel is itself accountable.
- **The PF cadence contract** (backlog.md PF row, verified): "~2–3 hrs once a week,
  don't gas... **watch scripts-vs-forecasts ratio for the collection trap**" — a
  quantitative tell registered in advance. Also the stack discipline in the same row:
  "if it takes the blog's slot, that gets chosen, not drifted into." Priority changes
  are decisions, not drift.
- **Karen's blind-spot rule** (CLAUDE.md, Karen section — law): before building an
  accumulation/avoidance/workstream-count narrative, verify real-world status with
  James. Repo absence ≠ not done; work-leo activity and live stakeholder
  conversations are systematically invisible to personal Leo. Ask first, or state
  the uncertainty explicitly.

When you propose new Leo infrastructure, run it against this section first: what
existing P0 does it displace, what's the reversal criterion, and would Karen call
it avoidance?

---

## 3. The verification-debt convention

Docs in this repo may legitimately write "verify next session / next spawn" — a
claim shipped before its confirmation. These are **first-class open items**, not
loose ends:

- They live in session-log **Open**/**Next time** sections and/or backlog Progress
  cells until closed.
- Example (both ends verified): backlog row "Fix consult-notebook agent live
  querying" — "Done 2026-04-11. **Verification mechanism: check `query_log.md` grows
  on next real spawn.**" Re-opened after the 2026-07-11c file moves:
  `system/session-logs/2026-07-11c.md` → "Verify next real consult-notebook spawn
  writes to `system/notebooklm/query_log.md`." Still open as of 2026-07-12.
- Example of open→closed: 2026-07-02 session registered four unanswered
  verifications (energy / dailies / blog ship-vs-park / work-leo blind spots);
  the 2026-07-05 entry in backlog.md's header blob explicitly closes one: "7/2
  work-leo-blind-spot verification CLOSED" (team held during OOO). Closure is
  written down, with the evidence.

**Recurrence of a carry IS signal.** Session logs count carries out loud, verified
trail: "Folio walkthrough — now thrice-carried" (2026-07-08) → "fourth" (07-09) →
"fifth" (07-09b) → "sixth" (07-10) → "**seventh carry**" (07-11, 07-11b). Same
pattern earlier: "H1 Daniel/ATG doc update slipped a third time... If it slips again
without strong reason, that's a watch flag" (2026-04-29 log). A 7×-carried item is
no longer a to-do; it's data about priorities or avoidance, and gets discussed as
such (per §2.1, verify with James before concluding which).

Start-session reconciles the session-log Next-time queue against backlog.md
(AGENTS.md §Backlog: "Both start-session and end-session read and reconcile against
this file").

---

## 4. The evidence bar

What counts as "established" before Leo asserts a mechanism, a pattern, or a fix:

1. **One mechanism must explain ALL observations, including the negatives.**
   In-repo exemplar: the consult-notebook agent failure (backlog row, fixed
   2026-04-11) wasn't closed on the first plausible cause — the recorded root cause
   names all three co-existing defects (nonexistent MCP tool name
   `mcp__notebooklm-mcp__notebook_query`, macOS paths on Linux, no hard tool-call
   instruction), and a separate 2026-04-25b diagnosis correction re-attributed a
   later failure to expired Google session cookies, explicitly noting the original
   framing was wrong ("Originally framed as 'Subagent tool-exposure fix'...
   Diagnosis corrected"). Wrong diagnoses get corrected on the record, not
   overwritten.
2. **Sweeps verify by count, grep-to-zero.** The Pinsight→Pinkerton rebrand recorded
   its scope numerically ("9 files renamed, 103 repo files + 10 memory files
   content-rewritten... Zero residual references" — backlog header blob 2026-05-16);
   the `repoint-structure-docs-on-file-moves` instinct ends its checklist with
   "grep the old path root-wide to verify." State expected counts before a sweep and
   reconcile after — the worked recipes (hypothesis-predicts-numbers-before-running)
   are the home turf of **leo-proof-and-analysis-toolkit** (Recipe 2, per that
   skill).
3. **Survive adversarial refutation.** The standing adversarial channel is Karen
   (Opus-pinned background agent; reads full conversation + `self/goals.md` + her
   own `system/karen_observations.md` + instincts INDEX; output = sharp observation
   + 2-3 alternatives + one question, surfaced as-is). Her observations file is
   organized by pattern type with dated entries, and includes James's pushback when
   she over-reached — a pattern that can't survive his rebuttal doesn't graduate.
4. **The blind-spot constraint bounds every inference** (§2.1): this repo cannot see
   work-leo or live conversations. Negative evidence from file-tree absence is
   inadmissible for "James didn't do X" claims. Ask James.

---

## 5. Idea lifecycle through backlog.md — the lab notebook

`backlog.md` (repo root) is both the priority queue and the experimental record.
Conventions, all verified against the live file:

- **Row format:** `Item | Why / Goal | Description / Subtasks | Rough Time |
  Progress | Priority`, grouped in four sections: Write, Learn, Build, Work.
  Priorities P0–P4.
- **Every idea enters with Why/Goal.** Goals reference James's goal IDs (G0–G5) —
  an item that can't name its goal is suspect (see §2).
- **History stays in the row.** Promotions, demotions, supersessions, and status
  flips accumulate in the Progress/Description cells with dates — the graphify rows
  carry their whole arc ("Done 2026-04-08 — commits `8f8222d` + `d917b4e`" /
  "demoted from P1" / "blocked on graphify Phase 2 (now P2)"). Never rewrite a row
  to look like the current state was always the plan.
- **Done rows are kept, with dates** ("Done 2026-04-05", "Done — verified
  2026-07-09", "Done per James 5/23 sweep"). Note the epistemic gradation there:
  *verified* vs *per James* are different evidence classes, and the rows say which.
- **Dropped/closed rows record the reason** ("Dropped 2026-04-19 — James and Darren
  already aligned politically"; "CLOSED 5/23 sweep — convo executed").
- **The `Last updated:` header blob** is a reverse-chronological session-by-session
  narrative — effectively the lab notebook's running abstract. New sessions prepend.
- **Near-term queue** = the most recent session log's "Next time" section;
  start-session reconciles it against the backlog (AGENTS.md §Backlog).

---

## 6. Where good ideas historically came from (provenance map)

Mined from git + session logs, 2026-07-12. Use this as a prior when hunting for the
next improvement — the hit-rate ranking is roughly the row order:

| Source | Mechanism | Verified examples |
|---|---|---|
| **Corrections in real sessions** | detect-corrections.sh + Phase 4b → instincts | The single richest source: 41 instincts. E.g. `check-existing-context-before-analyzing` grew from 3 stakeholder-analysis misses in 3 days (2026-04-23/25/25c); `avoid-ai-prose-tells` from drafting corrections across 5 dated evidence entries. |
| **Incidents → infrastructure** | Something broke; the fix became permanent plumbing | Decisions not persisting across conversations (2026-04-04-evening log) → three-layer persistence + the hooks-and-instincts commit (`fa0730e`, 2026-04-03, "Cross-session self-improvement: hooks, instinct system"); two overlapping memory systems → the 2026-06-26 consolidation (9-commit sequence `d0620e1`→`7052047`); git-sync gap → deterministic SessionStart auto-pull (`9ca6865`); reorg file-move reference drops → `repoint-structure-docs-on-file-moves` instinct (2026-07-11). Full chronicle: **leo-failure-archaeology**. |
| **James's direct asks** | "Build me X" mid-session → skill same day | `/send-me` + `/save-to-drive` built and smoke-tested in the 2026-05-21b session (backlog blob: "built TWO new Leo skills... New GCP project `leo-api`"). |
| **External repos studied** | Clone/read → patterns adopted | Backlog Build rows: kuberwastaken/claude-code (cloned at `/home/james/src/claude-code-reference/`), coleam00/Archon, alejandrobalderas/claude-code-from-source. **Honest status: all three rows "Not started" as of 2026-07-12** — candidate sources, not yet mined. This skill library itself originates from a GitHub meta-prompt James brought in on 2026-07-12 (current-session provenance; unverified beyond the assignment). |
| **Coaching frameworks → operating principles** | External coaching insight, tested in a real stakeholder landing, then codified | AGENTS.md OP11 org-needs-first framing, citing "the 4/22 Dylan prep landing — see `work/journals_and_growth.md` Lesson 6" (note: AGENTS.md's path may predate the journals move to `self/`; cite AGENTS.md, don't silently fix — path fixes go through the repoint checklist in **leo-change-control**). |

---

## 7. Retirement — retire loudly, leave a forwarding address

Systems and ideas in this repo get **documented retirement, never silent deletion.**
The pattern, with verified exemplars:

1. **Backup** — full pre-retirement snapshot. Auto-memory store: 92 files preserved
   at `system/memory_archive_2026-06-26/`.
2. **Audit** — why, tiered, on the record. `system/memory_audit_2026-06-26.md`
   tiered all 91 memories (T1 50 / T2 38 / T3 3) and named the honest finding:
   "this corpus is mostly genuinely-live... bloated with near-duplicates," which is
   why the fix was consolidation into instincts, not deletion.
3. **Redirect stub at the old address** — the live
   `~/.claude/projects/-home-james-src-leo/memory/MEMORY.md` now contains only a
   "RETIRED (2026-06-26) — do not add new memories here" pointer to instincts + the
   routing guide, so any tool that still lands there gets forwarded.
4. **Repoint the callers** — phased commits (Phase 2 migrate `d4fb026`, Phase 3
   route facts `e784384`, Phase 4 retire + repoint `2ce769e`, skill repoint
   `7052047`), all 2026-06-26.

Other verified instances of the same shape:

- **Rodney coaching channel archived 2026-04-29** (session log title says
  "archived", not deleted): five files updated in one pass; the frameworks Rodney
  built (Rumination, Tool 8, Inquiry Questions, etc.) explicitly "preserved as
  historical record + remain in toolkit as self-applied tools"; a watch-rule
  recorded ("don't recommend Rodney sessions out of habit").
- **Blog item superseded with a pointer** — backlog "EM growth in age of AI" row:
  "SUPERSEDED by personal blog launch effort — see `blogs/topic_ideas.md`," including
  a mapping of exactly which new topics absorbed which content.
- Retired docs elsewhere say where the live version went (2026-06-30 log: "retired
  the 6/17 proposal doc" upon producing its successor).

When you retire anything: backup if stateful, record why, leave a stub or pointer at
the old location, repoint live callers, and note it in the session log. Historical
docs (session logs, archives) keep their old paths/wording by design — see the
live-vs-historical rule in **leo-docs-and-writing** and the repoint checklist's
"skip historical docs" clause in `system/instincts/repoint-structure-docs-on-file-moves.md`.

---

## When NOT to use this skill

- **Executing the mechanics of a session** (start/end lifecycle, KB ops, output
  conventions) → **leo-run-and-operate**. This skill covers *why* Phase 4b works the
  way it does; that one covers running it.
- **Classifying/gating a specific change, commit conventions, the move/repoint
  checklist** → **leo-change-control**.
- **Symptom→fix triage on a live failure** → **leo-debugging-playbook**; the settled
  incident history with SHAs → **leo-failure-archaeology**.
- **What counts as run-evidence for a script/pipeline, golden inventory, doctor
  checks** → **leo-validation-and-diagnostics**.
- **Worked analysis recipes (predict-then-count sweeps, git archaeology how-tos)** →
  **leo-proof-and-analysis-toolkit**.
- **Which open problems are worth researching next** (evals-on-Leo, autonomous KB,
  portability) → **leo-research-frontier** — that skill ranks the problems; this one
  supplies the discipline any of them must clear to become adopted change.
- **Design invariants and load-bearing decisions** → **leo-architecture-contract**.
- Sibling skills above are the planned taxonomy of this knowledge-transfer library;
  as of 2026-07-12 `.claude/skills/` also holds Leo's 17 operational skills
  (start-session, end-session, kb-*, etc.) — those are workflows, not references.

---

## Provenance & maintenance

Authored 2026-07-12 from direct reads of repo state + git archaeology (no facts
copied from discovery notes without verification, except two items explicitly
labeled: the GitHub-meta-prompt origin of this skill library, and the
Recipe-2 pointer into leo-proof-and-analysis-toolkit).

Re-verification one-liners (run from repo root):

| Fact class | Command |
|---|---|
| Instinct count + all-active | `ls system/instincts/*.md \| grep -v INDEX \| wc -l; grep -h "^status:" system/instincts/*.md \| sort \| uniq -c` |
| Confidence distribution / promotion candidates | `grep -h "^confidence:" system/instincts/*.md \| sort \| uniq -c; grep -l "confidence: 0.8" system/instincts/*.md` |
| Correction regex classes | `sed -n '36,50p' scripts/hooks/detect-corrections.sh` |
| Phase 4b arithmetic + promotion gate | `grep -n "0.15\|0.8\|0.95" prompts/end-session.md .claude/skills/end-session/SKILL.md` |
| INDEX injection wiring | `grep -n "INDEX" scripts/hooks/session-start.sh; grep -n "hooks" .claude/settings.local.json` |
| graphify demotion text | `grep -n "Demoted 2026-04-09" backlog.md` |
| PF cadence contract / collection-trap tell | `grep -n "scripts-vs-forecasts" backlog.md` |
| Karen blind-spot rule + tripwire | `grep -n "Blind-spot" CLAUDE.md; grep -n "overnight content factories" system/karen_observations.md` |
| Open verification debts | `grep -rn "Verify next\|verification mechanism\|Verification mechanism" system/session-logs/ backlog.md` |
| Carry counting | `grep -rn "carry\|carried" system/session-logs/ \| grep -i folio` |
| Memory retirement artifacts | `ls system/memory_archive_2026-06-26 \| wc -l; head -5 system/memory_audit_2026-06-26.md` |
| Hooks/instincts origin commit | `git show -s --format="%h %ad %s" --date=short fa0730e` |
| 2026-06-26 consolidation sequence | `git log --oneline --since=2026-06-25 --until=2026-06-27` |
| Rodney archival | `head -1 system/session-logs/2026-04-29.md` |
| OP11 provenance | `grep -n "org-needs first" AGENTS.md` |

Drift watchpoints: instinct count and confidence numbers move every few sessions;
the 0.85 unpromoted example (§1.5) may promote at any time; backlog row numbers are
not stable identifiers (grep by row text, not line number); the detect-corrections
transcript path is machine-specific.
