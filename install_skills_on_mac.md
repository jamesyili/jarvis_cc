# Install Public Claude Code Skills on Mac

Generated 2026-05-18. Mirrors the **public skills currently installed on your WSL machine** to a fresh Mac. Excludes personal/private skills.

## Summary — 30 skills total

| Source | Skills | Install method |
|--------|--------|----------------|
| [Matt Pocock](https://github.com/mattpocock/skills) | 11 (10 engineering + `grill-me`) | `npx skills@latest` |
| [Humanizer](https://github.com/blader/humanizer) by blader | 1 | `git clone` + symlink |
| [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) | 18 selected (subset of ECC's 232) | `git clone` + selective symlink |

**Total: 30 skills.** Not the whole ECC plugin (232) — only the specific ones you actively use.

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

Clone the ECC repo once, then symlink only the 18 skills you want into `~/.claude/skills/`.

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

### The 18 ECC skills with descriptions

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

**Heads-up — two `tdd` skills**: Matt Pocock's `tdd` and ECC's `tdd-workflow` have different names, so no collision. Both will be available.

---

## Step 4 — Verify

In a fresh Claude Code session:

```
/help
```

You should see slash commands from all three sources. On disk:

```bash
ls ~/.claude/skills/ | wc -l    # expect 30
```

You should see all 11 Matt Pocock skills, `humanizer`, and the 18 ECC skills — 30 folders/symlinks total.

---

## Notes & gotchas

- **No personal/private skills are synced.** Your WSL Leo-specific skills are excluded intentionally.
- **Symlink approach for ECC + Humanizer** means `git pull` updates everything in one command — no per-skill maintenance.
- **MCP servers**: Several skills here depend on MCP tools — `deep-research` (firecrawl + exa), `fal-ai-media` (fal.ai), `videodb` (videodb MCP), `data-scraper-agent` (various). Install those MCP servers separately as you need them.

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

# Finalize Matt Pocock config — in Claude Code:
# /setup-matt-pocock-skills
```
