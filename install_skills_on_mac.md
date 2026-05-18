# Install Public Claude Code Skills on Mac

Generated 2026-05-18. Installs the three major **publicly-available** Claude Code skill collections on a fresh Mac. Does **not** sync any of your personal/private skills (`~/.claude/skills/` on WSL is excluded by design).

## What you'll end up with

| Source | What it ships | Stars | Install method |
|--------|---------------|-------|----------------|
| [Anthropic official](https://github.com/anthropics/skills) | 17 official skills — document handlers (PDF/DOCX/XLSX/PPTX), design, engineering examples | 135K+ | Claude Code plugin marketplace |
| [Matt Pocock](https://github.com/mattpocock/skills) | ~18 skills — TDD, grill-me, to-issues, triage, diagnose, prototype, etc. ("Skills for Real Engineers") | 48K+ | `npx skills@latest` |
| [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) by Affaan Mustafa | 183 skills + 48 agents + 60 slash commands + hooks (huge harness) | 163K+ | Plugin marketplace (preferred) or `install.sh` |

For discovery beyond these three: [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) curates the broader ecosystem.

---

## Prerequisites

1. **Claude Code installed on Mac** — verify with `claude --version`. If missing: https://docs.claude.com/en/docs/claude-code/setup
2. **Node.js** — needed for Matt Pocock's installer. `node --version` should print v18+ (install via `brew install node` if missing).
3. **Git** — for ECC's optional rules + fallback install. `git --version`.

---

## Step 1 — Anthropic official skills

Inside a Claude Code session:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

After install you can invoke skills like:

```
Use the PDF skill to extract form fields from path/to/file.pdf
```

`document-skills` = source-available document handlers; `example-skills` = Apache-2.0 reference patterns.

---

## Step 2 — Matt Pocock skills

From terminal:

```bash
npx skills@latest add mattpocock/skills
```

Follow the prompts:
1. Select which skills to install (or take all).
2. Choose your coding agent (pick Claude Code).
3. **Make sure `setup-matt-pocock-skills` is included in your selection.**

Then in Claude Code, run once:

```
/setup-matt-pocock-skills
```

This walks you through:
- Issue tracker preference (GitHub / Linear / local files)
- Triage label vocabulary
- Documentation save location

**Heads-up on overlap**: Matt's `grill-me` and `tdd` overlap with skills you already use. When two skills share a name, the more locally-scoped one wins — so Matt's versions will load in any project that doesn't define its own.

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

If the plugin route gives you trouble, ECC ships a shell installer with three profiles:

```bash
cd ~/src/everything-claude-code
./install.sh --profile minimal   # excludes hooks-runtime
./install.sh --profile core      # agents + commands + skills, no hooks
./install.sh --profile full      # everything including hooks
```

**Pick one route only** — don't run both `/plugin install` and `./install.sh`; they'll fight over the same paths.

---

## Step 4 — Verify

In a fresh Claude Code session:

```
/help
```

You should see new slash commands grouped by source (e.g., `/tdd`, `/triage`, `/to-issues` from Matt Pocock; `/plugin`-managed entries from Anthropic + ECC).

On disk:

```bash
ls ~/.claude/plugins/    # Anthropic + ECC plugin installs land here
ls ~/.claude/skills/     # Matt Pocock's npx installer drops skills here
```

---

## Notes & gotchas

- **No personal/private skills are synced by this doc.** Your WSL `~/.claude/skills/` contains Leo-specific work skills (coach-check, prep, debrief, kb-*, viral-remix-*, etc.) — those are excluded intentionally.
- **Skill name collisions** are resolved by scope. Project-local skills (`.claude/skills/` in a repo) shadow user-global (`~/.claude/skills/`) which shadow plugin-installed. If you want a public version to win, delete the local override.
- **MCP servers, hooks, and venvs** are separate concerns. ECC's plugin install handles its own hooks. Anthropic's skills don't require MCP. Some skills reference MCP tools — install those separately as you need them.
- **Updates**: Plugin-installed skills update via `/plugin update`. Matt Pocock's are vendored copies — re-run `npx skills@latest add mattpocock/skills` to refresh. ECC clone is a normal `git pull`.

---

## TL;DR cheat sheet

```bash
# Prereqs (one-time)
brew install node                                      # if missing

# In Claude Code:
# /plugin marketplace add anthropics/skills
# /plugin install document-skills@anthropic-agent-skills
# /plugin install example-skills@anthropic-agent-skills

# From terminal:
npx skills@latest add mattpocock/skills

# Back in Claude Code:
# /setup-matt-pocock-skills
# /plugin marketplace add https://github.com/affaan-m/everything-claude-code
# /plugin install ecc@ecc
```
