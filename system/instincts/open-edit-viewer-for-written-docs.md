---
id: open-edit-viewer-for-written-docs
trigger: Leo writes (or substantially rewrites) a .md doc deliverable for James in a session — a repo artifact James will read/review, not routine context-file updates
behavior: Launch the doc-viewer edit server for each such doc by default — background, one server per doc on a unique port, report the URL — unless James says not to. Local only, nothing emailed.
confidence: 0.8
evidence_count: 2
created: 2026-07-27
last_updated: 2026-07-28
status: active
---

# open-edit-viewer-for-written-docs

When a session produces doc deliverables, James reads and edits them in the
browser via the doc-viewer edit server — don't wait to be asked.

**Mechanics:**
```bash
~/.venvs/leo/bin/python scripts/doc_viewer.py --edit --port <unique> <file.md>
```
(run_in_background; one file per server; pick distinct ports, e.g. 8765+n;
confirm with a curl 200 before reporting the URL.)

**Scope boundary:** fires for deliverable artifacts (prep docs, proposals,
drafts, reference docs James asked for). Does NOT fire for context-file filing
(team_members.md, stakeholders.md, session logs, backlog) — opening editors for
every context update is noise.

**Conflict discipline:** while a doc is open in the edit server, Leo does not
edit that file mid-review (the 409 guard catches it, but don't create the
collision). Ask James to save first, or wait.

**Cleanup:** stop servers at session end — `pkill -f "doc_viewer.py --edit"`.

**Remote-control is not an exemption:** don't infer "James is on his phone /
away from the desk" from remote-control mode or photo uploads and skip the
launch. Launching is cheap; launch by default and report the URL — he'll use it
when he's at the machine.

**Interpreter:** always `~/.venvs/leo/bin/python`, never system `python3`
(no `markdown` module — fails at import, verified 2026-07-28).

## Evidence

- **2026-07-27** — after the doc-viewer `--edit` build, James: "Remember this
  for all docs you write going forward, to always open the --edit doc_viewer by
  default. Open one for each doc that's being written unless I tell you not to."
  Direct standing instruction → 0.8.
- **2026-07-28** — Leo skipped the auto-launch on a remote-control session
  (assumed phone-only from photo uploads); James had to ask "open the .md
  file". Also first launched with system `python3` → ModuleNotFoundError;
  the skill documents the venv interpreter. Both codified above.
