# Install Leo + Personal Skills on Mac

Generated 2026-05-18. Use this to mirror your Claude Code skills from WSL to a fresh macOS install.

## What you have on WSL (source)

| Source | Path | Count | In git? |
|--------|------|-------|---------|
| Leo project skills | `/home/james/src/leo/.claude/skills/` | 15 | Yes — `github.com:jamesyili/leo.git` |
| Personal / global skills | `/home/james/.claude/skills/` | 46 | No |
| viral_remix project skills | `/home/james/src/viral_remix/.claude/skills/` | 0 | n/a — folder doesn't exist |

The `viral-remix-start-session` and `viral-remix-end-session` skills you use in the viral_remix repo are actually **personal/global** skills (they live in `~/.claude/skills/`), so they come over with Step 3 below.

## What you'll end up with on Mac (target)

| Destination | Source | Method |
|-------------|--------|--------|
| `~/src/leo/.claude/skills/` (15 skills) | leo repo | `git clone` |
| `~/.claude/skills/` (46 skills) | WSL personal | rsync / tarball / private repo |

Claude Code reads user-scope skills from `~/.claude/skills/` on macOS just like on Linux.

---

## Step 1 — Install Claude Code on Mac

If not already installed: https://docs.claude.com/en/docs/claude-code/setup

Verify:
```bash
claude --version
```

## Step 2 — Clone the Leo repo (gets 15 project skills + everything else)

```bash
mkdir -p ~/src
cd ~/src
git clone git@github.com:jamesyili/leo.git
```

This brings down `.claude/skills/` plus all of Leo's context files, KB, scripts, etc. When you `cd ~/src/leo` and run `claude`, the project skills are auto-detected.

## Step 3 — Sync the 46 personal/global skills from WSL → Mac

Pick **one** option. Option A is fastest if you can SSH into WSL; Option C is best for ongoing sync.

### Option A — rsync over SSH (recommended one-shot)

From the **Mac**:

```bash
mkdir -p ~/.claude/skills

# Replace <wsl-host> with WSL's reachable hostname or IP
rsync -avh --delete \
  james@<wsl-host>:/home/james/.claude/skills/ \
  ~/.claude/skills/
```

If WSL isn't directly reachable, ssh into the Windows host first or use Option B.

### Option B — Tarball + manual transfer

On **WSL**:

```bash
tar -czf ~/personal-skills-$(date +%Y%m%d).tar.gz -C /home/james/.claude skills
```

Move the tarball to the Mac (AirDrop via Windows, scp, Dropbox, USB, whatever works).

On **Mac**:

```bash
mkdir -p ~/.claude
tar -xzf ~/Downloads/personal-skills-YYYYMMDD.tar.gz -C ~/.claude/
```

### Option C — Private GitHub repo (best for ongoing two-way sync)

One-time, on **WSL**:

```bash
cd ~/.claude/skills
git init
git add .
git commit -m "Initial personal skills snapshot"
gh repo create jamesyili/claude-skills --private --source=. --remote=origin --push
```

On **Mac**:

```bash
mkdir -p ~/.claude
git clone git@github.com:jamesyili/claude-skills.git ~/.claude/skills
```

After that, `git pull` / `git push` from either machine to stay in sync. (If you do this, add `.gitignore` entries for anything sensitive — see Caveats.)

## Step 4 — Verify

On Mac:

```bash
ls ~/.claude/skills | wc -l          # expect ~46
ls ~/src/leo/.claude/skills | wc -l  # expect 15

cd ~/src/leo
claude
```

In the Claude Code session, the skill list at startup should include both sets. Project skills shadow personal ones with the same name when you're inside `~/src/leo` — that's intentional.

---

## Caveats — things that are NOT skills but you may want too

The 46 personal skills are self-contained, but some of them call out to external pieces. If you want full feature parity:

1. **Hooks** — Leo's session hooks live in `scripts/hooks/` inside the leo repo (so they ride along with Step 2). They're wired up by `~/.claude/settings.json`, which is **not** in this sync. Inspect that file on WSL first; if you copy it, fix any Linux-only paths.

2. **MCP servers** — Several skills depend on MCP tools (notebooklm, firecrawl, exa, fal-ai-media, videodb, Gmail/Calendar/Drive). Each MCP server needs its own install + auth on the Mac. Check your existing `~/.claude/mcp.json` or equivalent for the current set.

3. **Python venvs** — `/kb-graph` and other KB scripts use `~/.venvs/graphify/`. Recreate on Mac with:
   ```bash
   python3 -m venv ~/.venvs/graphify
   ~/.venvs/graphify/bin/pip install graphifyy
   ```

4. **Global CLAUDE.md** — Your `~/.claude/CLAUDE.md` (private global instructions) is also not skills but is part of your Claude Code setup. Copy it separately if you want the same global behavior on Mac.

5. **Sensitive content check** — Before pushing personal skills to any git remote (Option C), scan for hardcoded paths, API keys, or stakeholder names. Some skills under `~/.claude/skills/` reference James-specific context that's fine on a private repo but should never go public.

---

## TL;DR cheat sheet

```bash
# On Mac, once Claude Code is installed:

git clone git@github.com:jamesyili/leo.git ~/src/leo

mkdir -p ~/.claude/skills
rsync -avh james@<wsl-host>:/home/james/.claude/skills/ ~/.claude/skills/

# Optional but recommended:
cp ~/src/leo/install_skills_on_mac.md ~/Documents/  # keep these instructions handy
```
