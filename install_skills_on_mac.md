# Install Claude Code Skills on Mac

Generated 2026-05-18. Installs the 30 public skills currently on your WSL machine plus 2 personal Leo skills for the viral_remix repo. **32 skills total.**

## Summary

| Source | Skills | Install method |
|--------|--------|----------------|
| [Matt Pocock](https://github.com/mattpocock/skills) | 11 (10 engineering + `grill-me`) | `npx skills@latest` (selective) |
| [Humanizer](https://github.com/blader/humanizer) by blader | 1 | `git clone` + symlink |
| [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) | 18 selected (subset of ECC's 232) | `git clone` + selective symlink |
| **Personal — viral_remix Leo skills** | 2 (`viral-remix-start-session`, `viral-remix-end-session`) | Paste verbatim content (Step 4) |

---

## Prerequisites

1. **Claude Code installed on Mac** — verify with `claude --version`. If missing: https://docs.claude.com/en/docs/claude-code/setup
2. **Node.js** — `node --version` should print v18+. Install via `brew install node`.
3. **Git** — `git --version`.

---

## Step 1 — Matt Pocock (11 skills)

```bash
npx skills@latest add mattpocock/skills
```

At the prompt, **check exactly these 11 and uncheck everything else**:

### Engineering (all 10)
1. `diagnose`
2. `grill-with-docs`
3. `triage`
4. `improve-codebase-architecture`
5. `setup-matt-pocock-skills`
6. `tdd`
7. `to-issues`
8. `to-prd`
9. `zoom-out`
10. `prototype`

### Productivity (1 only)
11. `grill-me`

Pick Claude Code as the agent. After install, in Claude Code:

```
/setup-matt-pocock-skills
```

Configures issue tracker preference, triage label vocabulary, docs save location.

---

## Step 2 — Humanizer (1 skill)

```bash
mkdir -p ~/src
git clone https://github.com/blader/humanizer.git ~/src/humanizer
ln -s ~/src/humanizer ~/.claude/skills/humanizer
```

Update later: `git -C ~/src/humanizer pull` (symlink picks it up automatically).

---

## Step 3 — ECC (18 skills only — NOT the whole plugin)

```bash
git clone https://github.com/affaan-m/everything-claude-code ~/src/everything-claude-code

mkdir -p ~/.claude/skills

for skill in \
  api-design \
  backend-patterns \
  blueprint \
  brand-voice \
  content-engine \
  cost-aware-llm-pipeline \
  council \
  crosspost \
  data-scraper-agent \
  deep-research \
  design-system \
  eval-harness \
  fal-ai-media \
  frontend-patterns \
  product-lens \
  tdd-workflow \
  video-editing \
  videodb \
; do
  ln -sf ~/src/everything-claude-code/skills/$skill ~/.claude/skills/$skill
done
```

Updates later: `git -C ~/src/everything-claude-code pull` — all 18 symlinks pick up changes automatically.

### The 18 ECC skills

| Skill | What it's for |
|-------|---------------|
| `api-design` | REST API design patterns — resource naming, status codes, pagination, errors |
| `backend-patterns` | Backend architecture, API design, DB optimization (Node/Express/Next.js) |
| `blueprint` | One-line objective → multi-session step-by-step construction plan |
| `brand-voice` | Build source-derived writing style profile from real material |
| `content-engine` | Platform-native content systems for X/LinkedIn/TikTok/YouTube/newsletter |
| `cost-aware-llm-pipeline` | LLM cost optimization — model routing, budget tracking, prompt caching |
| `council` | Four-voice council for ambiguous decisions / go-no-go calls |
| `crosspost` | Multi-platform distribution adapter (X/LinkedIn/Threads/Bluesky) |
| `data-scraper-agent` | Build automated AI-powered public-data collection agents (GH Actions free) |
| `deep-research` | Multi-source deep research using firecrawl + exa MCPs, cited reports |
| `design-system` | Generate/audit design systems, visual consistency, styling PR review |
| `eval-harness` | Formal evaluation framework for Claude Code sessions (EDD principles) |
| `fal-ai-media` | Unified media generation via fal.ai MCP — image/video/audio |
| `frontend-patterns` | React/Next.js patterns, state management, UI best practices |
| `product-lens` | Validate "why" before building; pressure-test product direction |
| `tdd-workflow` | 80%+ coverage TDD with unit + integration + E2E (distinct from Matt's `tdd`) |
| `video-editing` | AI-assisted video editing — FFmpeg, Remotion, ElevenLabs, fal.ai, Descript |
| `videodb` | See/understand/act on video and audio — ingest, index, edit, alert |

**No name collisions**: Matt Pocock's `tdd` and ECC's `tdd-workflow` have different names.

---

## Step 4 — Personal viral-remix skills (2 skills)

These two skills aren't in any public marketplace — they're personal Leo skills for the `viral_remix` repo workflow. Create the two folders and paste the content below into each `SKILL.md`.

```bash
mkdir -p ~/.claude/skills/viral-remix-start-session
mkdir -p ~/.claude/skills/viral-remix-end-session
# Then create SKILL.md inside each folder with the content blocks below.
```

**Path-substitution heads-up**: Both skills reference WSL paths verbatim:
- `/home/james/src/viral_remix` → on Mac becomes `~/src/viral_remix` (or `/Users/james/src/viral_remix`)
- `/home/james/.claude/projects/-home-james-src-viral-remix/memory/` → on Mac becomes `~/.claude/projects/-Users-james-src-viral-remix/memory/` (Claude Code derives the project memory path from cwd, so this changes automatically based on where you run `claude`)

Decide whether to leave the paths verbatim and rely on Claude to handle them, or do a find-and-replace before saving. The content below is the **verbatim** version from WSL.

---

### File 1: `~/.claude/skills/viral-remix-start-session/SKILL.md`

```markdown
---
name: viral-remix-start-session
description: Start a working session in the viral_remix repo. Reads prior session logs, the step-based sequencing plan, memory, CLAUDE.md invariants, and recent git history, then grills James on what he wants to accomplish — one question at a time — until fully aligned. Use at the beginning of any viral_remix working session, when James says hello or wants to start working, or when starting a new conversation in the viral_remix directory.
user_invocable: true
---

# Viral Remix Start Session

You are starting a working session in the `viral_remix` codebase (`/home/james/src/viral_remix`). Your job is to get fully aligned on what James wants to accomplish before doing any work. James is the primary owner of this repo — he's the sole developer on the faceless short-form video pipeline (scrape → segment → annotate/transcribe → embed → retrieve → TTS → Remotion stitch → QC + publish).

## Process

### Phase 1: Load Context (silent)

Do all of this silently — don't dump findings at James. Use them to inform your questions. If the shell is not already in `/home/james/src/viral_remix`, operate with absolute paths; don't `cd` unless needed.

1. **Session logs.** Read the latest 2 files from `docs/session-logs/` (sorted by filename descending — dated files only, named `YYYY-MM-DD.md`, sometimes with a time-of-day suffix; skip `backlog.md` and `README.md`). Note `## Next` and `## Blockers` items. Some logs have multiple `## Continuation` sections within one file — scan the most recent continuation, not just the top.
2. **Backlog.** Read `docs/session-logs/backlog.md` — this is the prioritized list of what's on James's plate. Note active, owed, paused, and parked items. Gitignored, local-only.
3. **Active step state.** Read `docs/codebase-sequencing.md` — this is the canonical step-by-step working plan. Each step has a `**Status:**` marker. Cross-check against the backlog; they should agree on what's active.
4. **Build plan & gaps.** Skim `docs/viral_remix_build_plan.md` (spec) and `docs/gaps.md` (adversarial review with per-gap status) only if the active step references them or a gap is near the current work.
5. **Memory.** Read `MEMORY.md` from `/home/james/.claude/projects/-home-james-src-viral-remix/memory/` and any referenced files that seem relevant to active work.
6. **CLAUDE.md invariants.** Re-read the repo-root `CLAUDE.md` for the non-negotiable invariants (no `rekko_server` imports, single guardrails impl, run_id cost tagging, voice ID in config, ADRs on non-obvious choices) and the per-step skill invocations table. If today's work is in an area with a recommended skill, remember to suggest it.
7. **Recent git history.** Run `git log --oneline -15` to see what's been shipping. Note the current branch (viral_remix uses branch-per-step — `step-N-slug`). If on a feature branch with uncommitted work, note it.
8. **Date/time awareness.** Check today's date and time of day. Cross-reference session log dates:
   - If the most recent session was **today**, don't ask "did X happen" — it likely hasn't. Reference `## Next` items as forward-looking plans.
   - If the session was **yesterday or earlier**, those items may have happened — fair to ask.
   - Time of day matters: evening energy ≠ morning energy. Don't ask about things that couldn't have happened yet.

### Phase 2: Grill for Alignment

Ask **one question at a time**. For each, provide your recommended answer based on what you learned in Phase 1. Resolve before moving on.

**Core questions (in order — skip any you can confidently answer from context):**

1. **What's the goal for this session?** What does "done" look like when James walks away?
   - If the backlog has active items, reference them: "Your backlog has [X] as the top item. Still the priority?"
   - If the active step in `docs/codebase-sequencing.md` has clear remaining substeps, reference them: "Step N is in progress — the next substep is [X]. Still the plan?"
   - If session logs have `## Next` items and enough time has passed, reference them: "Last session you said you'd [X]. Still the plan, or has something changed?"
   - If the last session was today, treat `## Next` items as the standing plan unless James signals otherwise.

2. **What's top of mind?** Anything happening — research signals, content performance, architectural doubts, external blockers — that should shape the session?

3. **Scope check.** If the goal feels too big for one session, say so and push for prioritization. "If we only get one thing done, what matters most?" Viral Remix steps are often multi-session; splitting is expected.

4. **Constraints.** Time box, pending external signals (e.g., real YouTube ingest to validate a spike), blockers, energy level?

5. **Mode check.** What does James need today? (Building code, spike/validation, architectural decision via ADR, doc/plan work, reviewing output quality, etc.)

### Phase 3: Confirm and Go

Once aligned, summarize in 2-3 lines:
- Session goal(s)
- Mode / approach
- First thing to tackle (including which step branch to be on, if applicable)

If the per-step skills table in CLAUDE.md recommends a skill for today's area (e.g., `cost-aware-llm-pipeline` for VLM work, `eval-harness` for retrieval, `tdd-workflow` for anything new), mention it as a one-liner — don't auto-invoke.

Then get to work. No ceremony.

## Rules

- **Read the energy.** If James comes in hot with a specific task and clearly knows what he wants, don't over-grill. One or two quick alignment questions is enough.
- **Full grill when unfocused.** If James is scattered or has too many things, that's when the full question set matters. Help him prioritize.
- **Reference specific items.** Cite specific `## Next` items from session logs, specific step numbers from `codebase-sequencing.md`, or specific gap IDs from `gaps.md` — that's the whole point of continuity.
- **One question at a time.** Provide your recommended answer. Resolve before moving on.
- **Don't recite context.** Never say "I read your session log and it says..." — just use the information naturally in your questions and recommendations.
- **Invariant awareness.** If the session is about to touch an area gated by a non-negotiable invariant (cost tagging, guardrails, voice config, ADRs), note it up front so James doesn't have to remind you.
- **Branch hygiene.** If the current branch is a step branch and the proposed work is for a different step, flag it — James may want to merge/stash before switching.
```

---

### File 2: `~/.claude/skills/viral-remix-end-session/SKILL.md`

```markdown
---
name: viral-remix-end-session
description: End a working session in the viral_remix repo. Grills James on what was accomplished, captures decisions (filing ADRs when non-obvious), produces the session log entry in docs/session-logs/, updates codebase-sequencing.md step state, and commits. Use when wrapping up work in viral_remix, saying goodbye, or ending a viral_remix session.
user_invocable: true
---

# Viral Remix End Session

You are closing out a working session in the `viral_remix` codebase. Your job is to make sure everything important gets captured before James walks away, then produce the session log entry, update step state, file any required ADRs, and commit.

## Process

### Phase 1: Grill for Capture

Ask **one question at a time**. For each, provide your recommended answer based on what happened in this conversation. You were here — lead with what you know.

**Core questions (in order — skip any you can answer from the conversation):**

1. **Did we hit the goal?** Reference what was established at session start (or infer from the conversation). Did we get there? If not, what's still open?

2. **Decisions made.** "Here's what I captured as decisions: [list]. Anything missing or anything you're second-guessing?"
   - **ADR check:** For each non-obvious architectural decision, flag whether it warrants a `docs/decisions/NNNN-slug.md` entry per the CLAUDE.md invariant. Recommend yes/no with one-line rationale; if yes, offer to draft it in Phase 3.

3. **Anything unfinished?** Things that got started but not completed. Things that came up but got deferred.

4. **What's actually next?** Not "continue working on X" — what's the specific next action? Push for concreteness.
   - If there are natural next steps from the work done, recommend them.
   - If a step from `docs/codebase-sequencing.md` was completed or advanced, name the next substep explicitly.

5. **Invariant audit.** If the session touched paid APIs (cost tagging via run_id), guardrails, voice config, or `rekko_server` port risk — confirm the invariants held. Don't belabor if obviously clean; do surface if anything smells off.

### Phase 2: Update Backlog, Step State, and ADRs

Before writing the session log, reconcile canonical docs:

1. **`docs/session-logs/backlog.md`.** Move completed items to the Done section with date + commit hash. Add new items that emerged this session. Update priorities if they shifted. Cross-check "Next time" items you're about to write against the backlog — don't list items that were deprioritized or cut; don't omit items that are still active.
2. **`docs/session-logs/viral_remix_explainer.md`.** If this session shipped a pipeline step or introduced a new architectural pattern, append a section explaining it in plain English at the same level as the existing sections (analogies over jargon, "why this exists" not just "what it does", call out surprising choices). Short paragraphs + one code snippet max per concept. This is the onboarding doc a newcomer reads before the formal docs — keep that audience in mind. Update the coverage line at the top. Gitignored, local-only.
3. **`docs/codebase-sequencing.md`.** If a step was completed, a substep shipped, a blocker was lifted, or scope shifted, update the relevant step's `**Status:**` marker.
4. **`docs/viral_remix_build_plan.md`.** Mirror the step-status update if the step crossed a ship boundary (Pending → Shipped).
5. **`docs/gaps.md`.** If this session closed (or opened) a gap, flip its status line.
6. **ADRs.** For any decision tagged in Phase 1 as ADR-worthy, create `docs/decisions/NNNN-slug.md` (next available N, zero-padded to 4 digits). Follow the format of the existing `0001-initial-architecture.md`. Keep it short — context, decision, consequences.
7. If you find a mismatch between what was discussed and what's in these docs, fix it and flag: "Caught a missed update — [what was fixed]."

### Phase 3: Produce Session Log

Once aligned, write or extend the session log in `docs/session-logs/`:

1. **Naming.** Check existing files. If no entry exists for today, create `YYYY-MM-DD.md`. If one exists, prefer **appending a `## Continuation — <topic>` section** to the existing file (viral_remix convention per `2026-04-18.md`) rather than creating a time-of-day suffix file. Only use a `YYYY-MM-DD-afternoon.md` style file if the existing log is already long enough that appending would hurt readability.
2. **Template** (matches existing viral_remix logs):

```markdown
# YYYY-MM-DD

**Focus:** <one-line summary>

## Done
- concrete accomplishment
- concrete accomplishment

## Decisions
- <decision> → see `docs/decisions/NNNN-slug.md` (if filed)

## Next
- specific, actionable next step

## Blockers
- unfinished item, blocker, or pending external signal (or "None")
```

For continuations within the same file, use `## Continuation — <short topic>` as the top-level section, then sub-sections (`### Done`, `### Decisions`, `### Next`, `### Blockers`) or the inline narrative style visible in `2026-04-18.md`. Match whatever style the existing file uses.

3. **Keep the directory lean.** Target ~20 files max. Delete the oldest if needed.

### Phase 4: Commit and Push

**Do not skip this step.**

1. Run `git status` and `git branch --show-current` to see what's being committed and where.
2. **Session logs + backlog are gitignored.** `docs/session-logs/` is fully ignored — session logs AND `backlog.md` live locally only. Do NOT attempt to `git add` anything from that directory. If something shows up staged somehow, unstage it.
3. **Branch awareness.**
   - If on a step branch (`step-N-slug`) and the session worked on that step's code: commit code changes + canonical doc updates (`codebase-sequencing.md`, `gaps.md`, ADRs) to the branch. They'll ride along on squash-merge.
   - If on `main` and the session worked directly on main: commit everything together.
4. Stage relevant files by name — never `git add -A`. Include: any updated canonical docs (`codebase-sequencing.md`, `viral_remix_build_plan.md`, `gaps.md`), new ADRs, and code changes. **Not** the session log or backlog.
5. Write a concise commit message summarizing the session's work. If on a step branch, reference the step number per `CONTRIBUTING.md`.
6. Commit and `git push` to remote (`-u origin <branch>` if the branch has no upstream).
7. Verify the push succeeded. If it fails, diagnose and retry.
8. If there were no code or canonical-doc changes this session (pure thinking/planning that only touched the session log), skip commit entirely — nothing to push.

### Phase 5: Memory Check

Quick scan of the conversation for things worth persisting to auto-memory (`/home/james/.claude/projects/-home-james-src-viral-remix/memory/`). Only save things that will matter in future conversations:

- Corrections James made to your approach (feedback memories)
- New project context that isn't captured in the session log or canonical docs (project memories)
- Preferences or workflow details you learned about James (user memories)
- External references James surfaced (reference memories)

If nothing notable, say "No memory updates" and move on. Don't force it.

## Rules

- **You were in the session** — lead with your recommended answers. Don't make James reconstruct everything from scratch.
- **Trivial sessions get a pass.** If the session was a quick one-off with no project impact, ask: "This felt like a quick one-off. Worth logging, or skip it?" If skipped, still commit any code changes.
- **One question at a time** in Phase 1. Resolve before moving on.
- **Capture, not ceremony.** If James confirms your summary is right, write the log and move on.
- **Don't fabricate.** If you lost context due to compaction, say what you're unsure about rather than guessing.
- **Invariants are load-bearing.** ADRs on non-obvious choices, run_id cost tagging, single-impl guardrails, voice ID in config — these aren't cosmetic. If the session created drift, fix it before ending.
- **Port hygiene.** If the session added code under `src/`, a quick mental check (or explicit `scripts/port-hygiene.sh`) that no `rekko_server` imports slipped in is worth the ten seconds.
```

---

## Step 5 — Verify

In a fresh Claude Code session:

```
/help
```

On disk:

```bash
ls ~/.claude/skills/ | wc -l    # expect 32
```

You should see all 11 Matt Pocock skills, `humanizer`, the 18 ECC skills, and the 2 viral-remix skills — 32 folders/symlinks total.

In a Claude Code session inside `~/src/viral_remix`, you should be able to invoke `/viral-remix-start-session` and `/viral-remix-end-session`.

---

## Notes & gotchas

- **Updates**:
  - Matt Pocock: re-run `npx skills@latest add mattpocock/skills`
  - Humanizer: `git -C ~/src/humanizer pull`
  - ECC: `git -C ~/src/everything-claude-code pull`
  - viral-remix skills: edit the `SKILL.md` files directly when you want to tune behavior
- **MCP servers**: Several skills depend on MCP tools — `deep-research` (firecrawl + exa), `fal-ai-media` (fal.ai), `videodb` (videodb MCP), `data-scraper-agent` (various). Install those MCP servers separately as needed.
- **viral_remix repo itself**: The two personal skills assume the `viral_remix` repo is cloned at `~/src/viral_remix` on Mac. Clone separately if it isn't yet.

---

## TL;DR cheat sheet

```bash
# Prereqs
brew install node git

# Matt Pocock — select only the 11 skills listed above
npx skills@latest add mattpocock/skills

# Humanizer
git clone https://github.com/blader/humanizer.git ~/src/humanizer
ln -s ~/src/humanizer ~/.claude/skills/humanizer

# ECC — clone once, symlink the 18 you want
git clone https://github.com/affaan-m/everything-claude-code ~/src/everything-claude-code
for skill in api-design backend-patterns blueprint brand-voice content-engine \
             cost-aware-llm-pipeline council crosspost data-scraper-agent \
             deep-research design-system eval-harness fal-ai-media \
             frontend-patterns product-lens tdd-workflow video-editing videodb; do
  ln -sf ~/src/everything-claude-code/skills/$skill ~/.claude/skills/$skill
done

# viral-remix personal skills — create dirs, then paste content from Step 4
mkdir -p ~/.claude/skills/viral-remix-start-session
mkdir -p ~/.claude/skills/viral-remix-end-session
# Save the two SKILL.md files from Step 4 above into these folders.

# Finalize Matt Pocock config — in Claude Code:
# /setup-matt-pocock-skills
```
