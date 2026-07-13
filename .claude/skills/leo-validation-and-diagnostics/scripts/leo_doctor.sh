#!/usr/bin/env bash
# leo_doctor.sh — read-only health check for the Leo repo.
# Usage: bash .claude/skills/leo-validation-and-diagnostics/scripts/leo_doctor.sh
# Derives repo root from its own location (never hardcode machine paths —
# see the pre-compact.sh counterexample in leo-debugging-playbook).
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
cd "$ROOT" || exit 1
pass=0; warn=0; fail=0
ok()   { echo "PASS  $1"; pass=$((pass+1)); }
wr()   { echo "WARN  $1"; warn=$((warn+1)); }
bad()  { echo "FAIL  $1"; fail=$((fail+1)); }

echo "leo_doctor — $ROOT — $(date '+%Y-%m-%d %H:%M')"
echo "-----------------------------------------------"

# 1. Root shape: exactly the 6 canonical tracked root dirs (dotdirs like .claude are exempt)
roots="$(git ls-tree --name-only HEAD 2>/dev/null | grep -v '^\.' | while read -r e; do [ -d "$e" ] && echo "$e"; done | sort | tr '\n' ' ')"
if [ "$roots" = "kb prompts scripts self system work " ]; then
  ok "root dirs: exactly the canonical 6 (kb prompts scripts self system work)"
else
  bad "root dirs deviate from the 6-root rule: [$roots]"
fi

# 2. GEMINI.md symlink
if [ -L GEMINI.md ] && [ "$(readlink GEMINI.md)" = "AGENTS.md" ]; then
  ok "GEMINI.md -> AGENTS.md symlink intact"
else
  bad "GEMINI.md is not a symlink to AGENTS.md"
fi

# 3. Instinct integrity: files vs INDEX bullets
nfiles=$(find system/instincts -maxdepth 1 -name '*.md' ! -name 'INDEX.md' 2>/dev/null | wc -l | tr -d ' ')
nindex=$(grep -c '^- \*\*' system/instincts/INDEX.md 2>/dev/null || echo 0)
if [ "$nfiles" = "$nindex" ] && [ "$nfiles" != "0" ]; then
  ok "instincts: $nfiles files == $nindex INDEX bullets"
else
  bad "instinct mismatch: $nfiles files vs $nindex INDEX bullets"
fi

# 4. Hooks wired and scripts executable
if [ -f .claude/settings.local.json ]; then
  for h in session-start.sh pre-compact.sh suggest-compact.sh detect-corrections.sh; do
    if grep -q "$h" .claude/settings.local.json && [ -x "scripts/hooks/$h" ]; then
      ok "hook wired + executable: $h"
    else
      bad "hook missing/not executable: $h"
    fi
  done
else
  bad ".claude/settings.local.json missing"
fi
# machine-specific hardcodes (known bug class)
hc=$(grep -l '/home/james/src/leo' scripts/hooks/pre-compact.sh scripts/hooks/detect-corrections.sh 2>/dev/null | tr '\n' ' ')
[ -n "$hc" ] && wr "machine-hardcoded hook paths (degrade off pc-leo): $hc" || ok "no machine-hardcoded hook paths"

# 5. Stale-path scan over LIVE surfaces only (historical dirs excluded by rule;
#    the leo-* skill library documents these strings, so it is excluded too)
stale=$(grep -rln -e '/Users/jamesli' -e 'AIContext/' \
  .claude prompts AGENTS.md CLAUDE.md 2>/dev/null | grep -v '.claude/skills/leo-' | tr '\n' ' ')
[ -n "$stale" ] && wr "stale-path refs on live surfaces: $stale" || ok "no stale paths on live surfaces"

# 6. Search-index freshness
if [ -f kb/.kb/search_index.json ]; then
  newer=$(find kb/hard/raw kb/soft/raw -name '*.md' -newer kb/.kb/search_index.json 2>/dev/null | wc -l | tr -d ' ')
  [ "$newer" -gt 0 ] && wr "search index stale: $newer articles newer than index (run kb_search.py --rebuild)" \
                     || ok "search index fresh"
else
  bad "kb/.kb/search_index.json missing"
fi

# 7. Graph presence + raw_chunks single-copy
[ -f kb/.kb/graph/graph.json ] && ok "graph.json present" || bad "graph.json missing"
nchunks=$(ls kb/.kb/graph/raw_chunks/ 2>/dev/null | wc -l | tr -d ' ')
nchunks_dot=$(find kb/.kb/graph/raw_chunks -name '.graphify_chunk_*' 2>/dev/null | wc -l | tr -d ' ')
total_chunks=$((nchunks + nchunks_dot))
if [ "$total_chunks" -ge 110 ]; then
  wr "raw_chunks: $total_chunks files — single copy, gitignored (back up before any wipe)"
else
  wr "raw_chunks: $total_chunks files (expected >=110) — verify nothing was lost"
fi

# 8. Venvs (machine-dependent -> WARN)
[ -x "$HOME/.venvs/leo/bin/python" ] && ok "leo venv present" || wr "leo venv missing (outbound scripts unusable)"
[ -x "$HOME/.venvs/graphify/bin/python" ] && ok "graphify venv present" || wr "graphify venv missing (graph queries unusable)"

# 9. Credentials (machine-dependent -> WARN)
[ -f "$HOME/.config/leo/google_credentials.json" ] && ok "google credentials present" || wr "google credentials missing (send-me/save-to-drive disabled)"
[ -f "$HOME/.config/leo/google_token.json" ] && ok "google token present" || wr "google token missing (browser auth needed)"

# 10. Lowercase skill.md shadows (shadow-bug class, incident f429fb4)
shadows=$(find .claude/skills -mindepth 2 -maxdepth 2 -name 'skill.md' 2>/dev/null | tr '\n' ' ')
[ -n "$shadows" ] && wr "lowercase skill.md files (shadow risk if an uppercase twin appears): $shadows" \
                  || ok "no lowercase skill.md files"

# 11. Session-log count vs documented ~20 trim rule (unenforced by choice)
nlogs=$(ls system/session-logs/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "INFO  session logs: $nlogs files (documented trim rule ~20 — unenforced by choice)"

# 12. claude CLI
command -v claude >/dev/null 2>&1 && ok "claude CLI on PATH" || wr "claude CLI not on PATH (compile_wiki/build_graph build unusable)"

echo "-----------------------------------------------"
echo "SUMMARY: $pass pass / $warn warn / $fail fail"
[ "$fail" -eq 0 ] || exit 1
