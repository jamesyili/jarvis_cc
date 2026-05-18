# Install Public Claude Code Skills on Mac

Generated 2026-05-18. Installs publicly-available Claude Code skill collections on a fresh Mac. Does **not** sync any of your personal/private skills.

## What you'll end up with

| Source | Skills | Install method |
|--------|--------|----------------|
| [Matt Pocock](https://github.com/mattpocock/skills) | 18 skills — full list below, including `tdd`, `grill-me`, `grill-with-docs` | `npx skills@latest` |
| [Humanizer](https://github.com/blader/humanizer) by blader | 1 skill — removes AI writing patterns | `git clone` or copy `SKILL.md` |
| [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) by Affaan Mustafa | 183 skills + 48 agents + 60 slash commands + hooks | Plugin marketplace (preferred) or `install.sh` |

For broader discovery: [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills).

---

## Prerequisites

1. **Claude Code installed on Mac** — verify with `claude --version`. If missing: https://docs.claude.com/en/docs/claude-code/setup
2. **Node.js** — needed for Matt Pocock's installer. `node --version` should print v18+ (install via `brew install node` if missing).
3. **Git** — for Humanizer + ECC. `git --version`.

---

## Step 1 — Matt Pocock skills (18 total)

From terminal:

```bash
npx skills@latest add mattpocock/skills
```

The installer will prompt you. **Select all 18 skills**, pick Claude Code as the agent, and make sure `setup-matt-pocock-skills` is included.

### The full Matt Pocock skill list

**Engineering (10):**
- `diagnose` — root-cause investigation
- `grill-with-docs` — grilling against your project's domain model + existing docs ← what you asked for
- `triage` — sort issues / inbox by priority
- `improve-codebase-architecture` — architectural refactor passes
- `setup-matt-pocock-skills` — one-time config (run this after install)
- `tdd` — red-green-refactor TDD loop ← what you asked for
- `to-issues` — break plans into independently-grabbable GitHub issues
- `to-prd` — turn a rough spec into a PRD
- `zoom-out` — pull back from tactical noise to product-level framing
- `prototype` — quick-and-dirty prototyping mode

**Productivity (4):**
- `caveman` — strip prose to caveman simplicity
- `grill-me` — relentless plan/design interrogation
- `handoff` — clean session handoff to next agent/human
- `write-a-skill` — meta-skill for authoring new skills

**Misc (4):**
- `git-guardrails-claude-code` — guardrails against accidental destructive git ops
- `migrate-to-shoehorn` — migration helper
- `scaffold-exercises` — generate practice exercises
- `setup-pre-commit` — install + configure pre-commit hooks

Then in Claude Code, run once:

```
/setup-matt-pocock-skills
```

This walks you through:
- Issue tracker preference (GitHub / Linear / local files)
- Triage label vocabulary
- Documentation save location

---

## Step 2 — Humanizer (standalone)

From terminal:

```bash
mkdir -p ~/.claude/skills/humanizer
git clone https://github.com/blader/humanizer.git /tmp/humanizer-src
cp /tmp/humanizer-src/SKILL.md ~/.claude/skills/humanizer/
rm -rf /tmp/humanizer-src
```

Or if you want the full repo for easier updating:

```bash
mkdir -p ~/src
git clone https://github.com/blader/humanizer.git ~/src/humanizer
ln -s ~/src/humanizer ~/.claude/skills/humanizer
# Update later with: git -C ~/src/humanizer pull
```

What it does: detects 24 AI writing patterns (em dash overuse, "delve/tapestry/landscape" vocabulary, rule of three, negative parallelisms, sycophantic tone) and rewrites them out. Based on Wikipedia's "Signs of AI writing" guide.

---

## Step 3 — Everything Claude Code (ECC)

Inside a Claude Code session:

```
/plugin marketplace add https://github.com/affaan-m/everything-claude-code
/plugin install ecc@ecc
```

That gets you the agents, skills, commands, and hooks via the plugin system.

### Optional: install ECC's rules

The plugin route doesn't auto-install ECC's rule packs. If you want them:

```bash
mkdir -p ~/src
git clone https://github.com/affaan-m/everything-claude-code ~/src/everything-claude-code

mkdir -p ~/.claude/rules/ecc
cp -r ~/src/everything-claude-code/rules/common ~/.claude/rules/ecc/
cp -r ~/src/everything-claude-code/rules/typescript ~/.claude/rules/ecc/
# Copy only the rule folders you actually want — there are more in the repo.
```

### Fallback: manual install via `install.sh`

If the plugin route gives you trouble:

```bash
cd ~/src/everything-claude-code
./install.sh --profile minimal   # excludes hooks-runtime
./install.sh --profile core      # agents + commands + skills, no hooks
./install.sh --profile full      # everything including hooks
```

**Pick one route only** — don't run both `/plugin install` and `./install.sh`; they'll fight over the same paths.

**Heads-up on overlap with Matt Pocock**: ECC ships its own `tdd` and several skills that overlap with Matt Pocock's set. Skill name collisions are resolved by scope (project-local > user-global > plugin). If both define the same name in the same scope, the last one loaded wins — install order matters. If you want Matt Pocock's `tdd` to win, install ECC first, then Matt Pocock.

---

## Step 4 — Verify

In a fresh Claude Code session:

```
/help
```

You should see new slash commands grouped by source. Expected highlights:
- From Matt Pocock: `/tdd`, `/grill-me`, `/grill-with-docs`, `/triage`, `/to-issues`, `/diagnose`, etc.
- From Humanizer: `/humanizer` (or invoke by name: "Run the humanizer on this text")
- From ECC: a large set of `/`-commands depending on profile

On disk:

```bash
ls ~/.claude/skills/        # Matt Pocock + Humanizer land here
ls ~/.claude/plugins/       # ECC plugin install lands here
```

You should see `humanizer/`, the 18 Matt Pocock skill folders, and an ECC plugin folder.

---

## Notes & gotchas

- **No personal/private skills are synced** by this doc. Your WSL `~/.claude/skills/` contains Leo-specific work skills — those are excluded intentionally.
- **Updates**: 
  - Matt Pocock: `npx skills@latest add mattpocock/skills` (re-run)
  - Humanizer: `git -C ~/src/humanizer pull` (if you used the symlink approach)
  - ECC: `/plugin update` inside Claude Code, or `git pull` if you used `install.sh`
- **MCP servers** are a separate concern. Some skills reference MCP tools (firecrawl, exa, etc.) — install those individually as needed.

---

## TL;DR cheat sheet

```bash
# Prereqs
brew install node git

# Matt Pocock (18 skills)
npx skills@latest add mattpocock/skills
# Then in Claude Code: /setup-matt-pocock-skills

# Humanizer
git clone https://github.com/blader/humanizer.git ~/src/humanizer
ln -s ~/src/humanizer ~/.claude/skills/humanizer

# ECC — in Claude Code:
# /plugin marketplace add https://github.com/affaan-m/everything-claude-code
# /plugin install ecc@ecc
```
