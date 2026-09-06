# Leo on Windows, Linux, and WSL

Leo can live in any checkout folder, including paths with spaces. The workflow bodies
remain in `.claude/skills/`; `.agents/skills/` contains generated Codex entry points
that resolve the local checkout and read those bodies. They are ordinary files, so
Windows does not need Developer Mode, administrator symlink rights, or `core.symlinks`.

## One-time setup per operating-system user

Install Python 3.10+ and Git in the environment where the agent runs. Open the Leo
checkout in Codex to use its project skills immediately. To make the same skills
available from other folders, run:

```powershell
# Native Windows / PowerShell, from any directory; use your actual checkout path.
python 'C:\Users\james\leo\scripts\leo_setup.py' --user
python 'C:\Users\james\leo\scripts\leo_runtime.py' check
```

```bash
# Linux, WSL, or macOS; substitute wherever this checkout lives.
python3 '/path/to/leo/scripts/leo_setup.py' --user
python3 '/path/to/leo/scripts/leo_runtime.py' check
```

The installer writes small managed entry points to the current user's
`~/.agents/skills/<name>/SKILL.md`. It preserves unrelated skills and stops on naming
conflicts. Rerunning is safe; after relocating the registered checkout, rerun it
with the script at the new path. Workflow-body edits take effect directly because
the entry points read the canonical files. After adding/renaming skills or changing
discovery metadata, regenerate project entries with `--project` and user entries
with `--user`. `--check` checks either installation without writing.

In Codex, type `$start-session` or `$end-session`. Restart Codex if a previously
open picker does not refresh. Project and user installations can both appear under
the same skill name; both route to the same canonical workflow for the active Leo
checkout. The user entry prefers a Leo checkout containing the current directory,
then falls back to the checkout registered by the installer. It never treats an
unrelated current repository as Leo. Tool permissions still apply: a task opened
outside Leo may need access to the Leo directory for writes.

For the CLI, the launcher starts a task with the correct repo as its working root:

```powershell
python 'C:\Users\james\leo\scripts\leo_runtime.py' launch
```

```bash
python3 '/path/to/leo/scripts/leo_runtime.py' launch
# Optional Codex flags go after --, e.g. launch -- --no-alt-screen
```

This invokes `codex -C <resolved-checkout> '$start-session'`. Codex must be installed
on PATH in that OS. The launcher does not change shell profiles or global permissions.

## What start-session checks

Before sync or context loading, identify the actual OS, active tool shell, resolved
repo, Python interpreter, and skill installation. `scripts/leo_runtime.py check`
performs the read-only checks; the skill selects syntax for its active shell.
Always use an explicit repo working directory or `git -C <root>` when invoked from
elsewhere. End-session uses that same root for logs, staging, commit, and push.

Native Windows Python and WSL Python are separate installations. A path under
`/mnt/c/` is still running in Linux when the tool shell is WSL. Run the installer
once in each environment you use; Windows user skills do not install WSL user
skills. Virtual environments use `Scripts/python.exe` on Windows and `bin/python`
on Linux. Optional Google/NotebookLM authentication and runtime dependencies remain
machine-local and are not installed or copied by this setup.

## Hooks

Codex's additive `developer_instructions` in `.codex/config.toml` requires reading
`.codex/LEO.md` and the shared `system/instincts/INDEX.md` before substantive advice.
AGENTS.md, start-session, and installed skill entries carry the same fallback for
untrusted/missing hooks and invocation from another folder. The `.codex` briefing
adapts the existing instincts; the 102 canonical instinct files remain in `system/`.
Corrections are enriched there, not in a second Codex memory store.

`.codex/hooks.json` uses Python 3 on POSIX and a `commandWindows` override on Windows.
Both locate the repo from the current Git checkout, so nested working folders work.
The existing Bash hook paths are adapters to the same Python implementation for
Claude/POSIX callers. SessionStart reports the environment, pulls only a clean tree
with `--ff-only` and a 20-second timeout, then reads the instinct index and latest
two logs. PreCompact writes its record relative to the script's own checkout.

Codex SessionStart uses `--codex` to return explicit additional-context JSON with
the Leo briefing, complete instinct index, and logs. A separate `compact` matcher
reloads that context with `--no-sync`; PreCompact's plain stdout is not used as a
recovery channel. The current conversation remains authoritative over old logs.

Review and trust project hooks through Codex's `/hooks` interface on each machine
when requested by Codex. Editing a hook may require renewed trust. Setup does not
grant trust or disable sandbox checks. Skills work even if hooks have not run;
start-session then performs the sync explicitly. Hooks are project-scoped and will
not auto-load Leo context in unrelated projects just because user skills are installed.

For a local smoke check without a network fetch:

```powershell
python scripts/leo_runtime.py session-start --no-sync
python -m unittest discover -s scripts/tests -p 'test_leo_portability.py'
```

Use `python3` for those same commands on Linux/WSL. Full optional-integration setup
is in `.claude/skills/leo-build-and-env/SKILL.md`.

## Why the earlier Windows bridge failed

The previous `.agents/skills` was a Git symlink to `../.claude/skills`. With
`core.symlinks=false`, this Windows checkout held a text file containing that target,
not a traversable skill directory. No Leo skills were installed in the Windows
user discovery directory either. The generated entry points remove both dependencies.

Official references: [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills)
and [hook commands and Windows overrides](https://learn.chatgpt.com/docs/hooks).

## Verification on 2026-09-05

Portability suite: 13 passed on native Windows (one Linux-symlink test skipped),
14 passed on Ubuntu/WSL. All 34 generated Codex entries passed the official skill
validator. Codex's local `skills/list` API reported start-session and end-session
enabled at both project and user scope, with no discovery errors; user scope was
also verified from the Windows home folder outside Leo. Both platform startup
commands loaded context from a nested working folder. Automatic hook execution
after app reload remains dependent on Codex hook trust.

The broader, Claude-oriented `leo_doctor.sh` run from WSL against this Windows
checkout reported 8 pass / 5 warnings / 2 failures: `GEMINI.md` is still a Windows
Git symlink text stub, and `.claude/settings.local.json` is absent here. Its warnings
cover older search paths/index freshness, graph raw chunks, lowercase legacy skills,
and Claude CLI availability. This change verifies the Codex path; it does not
establish a fully configured native-Windows Claude or Gemini installation.

Behavioral integration follow-up: Codex's local `config/read` API confirmed the
Leo bootstrap in the effective project instructions. The native Windows compact
command delivered the briefing and complete 102-instinct index without syncing.
The expanded regression suite passed 15 tests on Windows (one Linux-only skip)
and all 16 on Ubuntu. These verify configuration and delivery, not future judgment;
James's next substantive interaction is the behavioral acceptance check. Hook trust
on reload remains a host requirement.
