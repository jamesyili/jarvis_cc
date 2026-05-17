# User-Level Skills Inventory (personal Leo → work-leo)

**Purpose:** Complete list of user-level skills installed in personal Leo at `~/.claude/skills/`. Transfer guidance for work-leo on the work mac.

**Generated:** 2026-04-19. Regenerate when new skills land.

**Scope:** These are skills installed at `~/.claude/skills/` (user-level, available across all projects on the personal mac). To install on work-leo, `scp` or rsync the skill directory to `~/.claude/skills/` on the work mac.

---

## Transfer recommendation key

- **YES** — transfer to work-leo; works out of the box or with trivial path adaptation
- **YES*** — transfer but adapt paths/context-file references to work-leo's structure
- **NO** — depends on personal-Leo context (KB, personal goals, personal stakeholder files) that work-leo doesn't have
- **SKIP** — not useful on work-leo's domain (work mac doesn't do content distribution, media generation, etc.)

---

## Session & Workflow

| Skill | Description | Transfer |
|---|---|---|
| `start-session` | Read prior session context, grill on session goals until aligned — one question at a time. | **YES*** |
| `end-session` | Grill for capture, produce session log, commit, run self-improvement pass. Recently updated (2026-04-19) to ask all capture questions in one consolidated message. | **YES*** |
| `session-log` | Write/update a session log entry. Sub-skill of end-session. | **YES*** |
| `pulse` | 30-second landscape read — goals, open items, tripwires, recent session context. | **YES*** |
| `weekly-review` | Generate a weekly digest — reviews journal entries, context files, goals progress. | **YES*** |
| `context-update` | Guided update of context files when information changes. | **YES*** |
| `debrief` | Daily debrief — James talks through meetings, Leo extracts and synthesizes. | **YES*** |

All session-workflow skills reference context files by relative path. On work-leo they should point to `context/` not `work+self/`. Check each skill file and adapt.

---

## Thinking & Coaching

| Skill | Description | Transfer |
|---|---|---|
| `thinking-partner` | Strategic thought partnership — stakeholder dynamics, technical direction, career moves. | **YES** |
| `grill-me` | Interview relentlessly about a plan or design until reaching shared understanding. | **YES** |
| `coach-check` | Coaching-lens review against James's frameworks — brevity, emotional regulation, executive presence, managing up. | **YES*** |
| `council` | Convene a four-voice council for ambiguous decisions and tradeoff calls. | **YES** |
| `consult-notebook` | Query NotebookLM research notebooks for domain-specific advice. | **NO** — requires NotebookLM MCP credentials not set up on work mac |

---

## Communication

| Skill | Description | Transfer |
|---|---|---|
| `prep` | Pre-meeting preparation — reads stakeholder profiles, generates talking points + watch-fors. | **YES*** |
| `draft-email` | Draft emails/messages calibrated to recipient. | **YES*** |

Both depend on `context/people/stakeholders.md` and related files. Work-leo has its own stakeholders file — adapt paths.

---

## Engineering Patterns (codebase-agnostic)

| Skill | Description | Transfer |
|---|---|---|
| `api-design` | REST API design patterns — resource naming, status codes, pagination, versioning, rate limiting. | **YES** |
| `backend-patterns` | Backend architecture patterns for Node.js, Express, Next.js API routes. | **YES** |
| `frontend-patterns` | Frontend patterns for React, Next.js, state management, performance. | **YES** |
| `design-system` | Generate or audit design systems, check visual consistency, review styling PRs. | **YES** |
| `tdd-workflow` | Test-driven development with 80%+ coverage (unit + integration + E2E). | **YES** |
| `eval-harness` | Formal evaluation framework implementing eval-driven development (EDD) principles. | **YES** — highly relevant for PINvestigator/Pinkerton work |
| `blueprint` | Turn a one-line objective into a multi-session construction plan with adversarial review gate. | **YES** — ideal for Reflex redesign migration phases |
| `cost-aware-llm-pipeline` | Cost optimization patterns for LLM API usage — routing, budget tracking, caching. | **YES** — relevant for Pinkerton/Reflex agent costs |
| `product-lens` | Validate the "why" before building, pressure-test product direction. | **YES** |

All of these are domain-general and transfer cleanly.

---

## Knowledge Base (personal Leo only)

| Skill | Description | Transfer |
|---|---|---|
| `kb-status` | KB dashboard — article counts, index age, wiki compilation state. | **NO** — KB lives in personal repo |
| `kb-ingest` | Ingest content into the KB. | **NO** |
| `kb-scout` | Trigger RSS scout run. | **NO** |
| `kb-lint` | Health checks — thin articles, broken links, duplicates. | **NO** |
| `kb-compile` | Wiki compiler — synthesizes raw KB articles. | **NO** |
| `kb-merge` | Consolidate duplicate/overlapping wiki concepts. | **NO** |
| `kb-reflect` | Cross-cutting synthesis — themes, contradictions, gaps. | **NO** |
| `kb-graph` | Query KB knowledge graph — neighbors, god nodes, communities. | **NO** |
| `graphify` | General input → knowledge graph pipeline. | **YES** if you want graph-ify-ing code at work; otherwise skip |
| `ingest` | Knowledge base content pipeline (older version — sub to `kb-ingest`). | **NO** |
| `search` | KB query across context files and knowledge base. | **NO** |

All KB skills are personal-Leo infrastructure. They won't work on work-leo without the KB itself.

---

## Research & Data

| Skill | Description | Transfer |
|---|---|---|
| `deep-research` | Multi-source research using firecrawl + exa MCPs; cited reports with source attribution. | **YES** if MCP set up on work mac; otherwise skip |
| `data-scraper-agent` | Automated data collection agent for public sources — GitHub Actions cron. | **SKIP** — not needed on work mac |

---

## Content & Writing

| Skill | Description | Transfer |
|---|---|---|
| `content-engine` | Platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters. | **SKIP** |
| `crosspost` | Multi-platform content distribution across X, LinkedIn, Threads, Bluesky. | **SKIP** |
| `brand-voice` | Source-derived writing style profile from real posts/essays. | **SKIP** — unless James starts a work-facing publication strategy |
| `humanizer` | Remove signs of AI-generated writing from text. | **YES** — useful for work comms drafts |

---

## Media Generation

| Skill | Description | Transfer |
|---|---|---|
| `fal-ai-media` | Unified image/video/audio generation via fal.ai MCP. | **SKIP** |
| `videodb` | See/understand/act on video and audio — ingest, index, search, edit. | **SKIP** |
| `video-editing` | AI-assisted video editing (FFmpeg, Remotion, ElevenLabs, fal.ai, Descript). | **SKIP** |

None of these are relevant to work-leo's domain.

---

## Project-specific (personal Leo)

| Skill | Description | Transfer |
|---|---|---|
| `viral-remix-start-session` | Start session in the viral_remix repo. | **NO** |
| `viral-remix-end-session` | End session in the viral_remix repo. | **NO** |

Personal-side projects only.

---

## Recommended transfer set for work-leo

Minimum viable — copy these to `~/.claude/skills/` on the work mac:

**Session workflow (7):**
```
start-session, end-session, session-log, pulse, weekly-review, context-update, debrief
```

**Thinking & coaching (4):**
```
thinking-partner, grill-me, coach-check, council
```

**Communication (2):**
```
prep, draft-email
```

**Engineering patterns (9):**
```
api-design, backend-patterns, frontend-patterns, design-system, tdd-workflow,
eval-harness, blueprint, cost-aware-llm-pipeline, product-lens
```

**Writing hygiene (1):**
```
humanizer
```

**Total: 23 skills** that transfer cleanly or with trivial adaptation.

---

## Install command

Run from the personal mac (adjust host + path to your work mac):

```bash
# Transfer the 23 recommended skills
SKILLS=(
  start-session end-session session-log pulse weekly-review context-update debrief
  thinking-partner grill-me coach-check council
  prep draft-email
  api-design backend-patterns frontend-patterns design-system tdd-workflow
  eval-harness blueprint cost-aware-llm-pipeline product-lens
  humanizer
)

for skill in "${SKILLS[@]}"; do
  rsync -avz "$HOME/.claude/skills/$skill/" "work-mac:~/.claude/skills/$skill/"
done
```

Alternatively, if work-leo is running on the same mac (different project dir), symlink instead of copy:

```bash
for skill in "${SKILLS[@]}"; do
  ln -sf "$HOME/.claude/skills/$skill" "$HOME/.claude/skills/$skill"
done
```

---

## Post-transfer adaptation checklist

Each transferred skill may reference personal-Leo paths. Spot-check and adapt:

- [ ] `context/` vs `work+self/` — work-leo uses `context/`; personal uses `work+self/`
- [ ] `system/session-logs/` — same path on both, no change
- [ ] `backlog.md` — work-leo has `system/backlog.md`; personal has root `backlog.md`
- [ ] Any reference to `kb/` — remove (no KB on work-leo)
- [ ] Stakeholder profile file paths — work-leo's `context/people/` has a subset; check whether the skill references people the work-leo file doesn't have
- [ ] `notebooklm/` references — remove (no NotebookLM MCP on work mac)

---

## Notes

- Skill file naming inconsistency: most use `SKILL.md` (uppercase); a few (`debrief`, `ingest`, `search`) use lowercase `skill.md`. Both work; don't rename unless intentionally consolidating.
- Some skills have outdated descriptions in frontmatter — update when noticed during transfer.
- When Leo adds new user-level skills, regenerate this inventory: `for d in ~/.claude/skills/*/; do ...; done` (see the ad-hoc script used to produce this).
