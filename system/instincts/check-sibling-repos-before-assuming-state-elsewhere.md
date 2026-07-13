---
id: check-sibling-repos-before-assuming-state-elsewhere
trigger: James references a side project's state as unknown, elsewhere, or "on the other computer" (Folio, PF, or any named build)
behavior: Before recording that state is inaccessible, check the sibling-repo dir for this machine (pc ~/src/, mac ~/code/), then read its CONTEXT/BACKLOG/session logs. But verify freshness before building deliverables on the data — a sibling repo existing does not make it canonical; ask which machine holds the accurate copy. Known — pc ~/src/pf (PF, canonical), ~/src/viral_remix (Folio); mac ~/code/pf DELETED 2026-07-13 (was stale, Feb-2026 data).
confidence: 0.55
evidence_count: 2
created: 2026-07-03
last_updated: 2026-07-13
status: active
---

## Evidence

### 2026-07-03
> "check out @../pf/ for PF"
Context: The 7/3 afternoon session logged "the actual state lives on his other computer" for both Folio and PF. Evening session: PF was at `~/src/pf` on this machine the whole time, with a fully self-documenting repo (CONTEXT.md, BACKLOG.md, LAB.md, session logs) — the planned "James walks Leo through the state" was unnecessary; reading the repo answered everything. Known sibling repos: `~/src/pf` (PF), `~/src/viral_remix` (Folio, pre-extraction).
Signal: observed inefficiency (wrong fact recorded in the afternoon log; walkthrough session mis-scoped)

### 2026-07-13
> "Move those in the leo repo actually. I forgot you don't have my most accurate numbers based on my pc paths. I also want you to delete the pf repo on the ma[c]."
Context: Retirement plan built from the mac's ~/code/pf copy (Feb-2026 snapshot). The sibling repo existed and was read correctly — but it was stale; canonical financial data lives on the PC. The flip side of this instinct: found ≠ fresh. James then had the mac pf repo deleted (untracked data/ folder and uncommitted financial_strategy.md edits went with it, flagged pre-deletion).
Signal: correction
