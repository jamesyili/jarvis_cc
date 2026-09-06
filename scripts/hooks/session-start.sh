#!/usr/bin/env bash
# POSIX adapter to the shared Windows/Linux lifecycle implementation.
LEO_REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
if command -v python3 >/dev/null 2>&1; then
  exec python3 "$LEO_REPO_ROOT/scripts/leo_runtime.py" session-start "$@"
fi
exec python "$LEO_REPO_ROOT/scripts/leo_runtime.py" session-start "$@"
