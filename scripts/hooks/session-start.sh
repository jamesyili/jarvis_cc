#!/bin/bash
# SessionStart hook: Auto-load the two most recent session log entries into context.
# stdout is injected as a system message at session start.

# Derive repo root from this script's location so the hook works on any machine
# (was hardcoded to /home/james/src/leo, which broke on the Mac repo at /Users/jamesli/code/leo).
SESSION_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/system/session-logs"

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
