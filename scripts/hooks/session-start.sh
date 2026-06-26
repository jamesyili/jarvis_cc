#!/bin/bash
# SessionStart hook: sync the repo from git, then auto-load the two most recent
# session log entries into context. stdout is injected as a system message at
# session start.

# Derive repo root from this script's location so the hook works on any machine
# (was hardcoded to /home/james/src/leo, which broke on the Mac repo at /Users/jamesli/code/leo).
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SESSION_DIR="$REPO_ROOT/system/session-logs"

# --- Auto-pull every session (the reliable "download from git every time" guarantee) ---
# Safe by construction: only fast-forwards a CLEAN tree, never touches uncommitted
# work, and is time-boxed so an offline/slow network can't hang session start.
# A dirty tree is reported (not pulled) — /start-session handles that case via stash.
if git -C "$REPO_ROOT" rev-parse --git-dir >/dev/null 2>&1; then
  echo "=== GIT SYNC (SessionStart) ==="
  if [ -n "$(git -C "$REPO_ROOT" status --porcelain 2>/dev/null)" ]; then
    echo "Working tree is dirty — skipped auto-pull to protect uncommitted work."
    echo "Run /start-session (stash → pull → pop) or commit first to sync."
  else
    PULL_OUT=$(timeout 20 git -C "$REPO_ROOT" pull --ff-only --no-edit 2>&1)
    if [ $? -eq 0 ]; then
      echo "$PULL_OUT" | tail -3
    else
      echo "Auto-pull skipped/failed (offline, non-fast-forward, or timeout):"
      echo "$PULL_OUT" | tail -3
      echo "Repo left untouched; pull manually when ready."
    fi
  fi
  echo "=== END GIT SYNC ==="
  echo ""
fi

# --- Inject the instincts index (behavioral memory; the single system, replacing
# the retired ~/.claude auto-memory). Always runs, even if session logs are absent. ---
INDEX_FILE="$REPO_ROOT/system/instincts/INDEX.md"
if [ -f "$INDEX_FILE" ]; then
  echo "=== INSTINCTS (behavioral memory index — read the full file in system/instincts/ when one applies) ==="
  cat "$INDEX_FILE"
  echo "=== END INSTINCTS ==="
  echo ""
fi

if [ ! -d "$SESSION_DIR" ]; then
  exit 0
fi

# Get the two most recent session files (sorted by name, which is date-based)
LATEST=$(ls -1 "$SESSION_DIR"/*.md 2>/dev/null | sort -r | head -2)

if [ -z "$LATEST" ]; then
  exit 0
fi

echo "=== LAST SESSION CONTEXT (auto-loaded by SessionStart hook) ==="
for f in $LATEST; do
  cat "$f"
  echo ""
  echo "---"
  echo ""
done
echo "=== END LAST SESSION CONTEXT ==="
