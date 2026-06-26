# Memory System Audit — 2026-06-26

Audit of all **91** auto-memory files at `~/.claude/projects/-home-james-src-leo/memory/` (indexed by `MEMORY.md`, the only part loaded into every session). Produced via 4 parallel digest agents, reconciled to one consistent bar.

## Headline

| Tier | Count | Meaning |
|------|-------|---------|
| **T1 — Important** | 50 | Broad/frequent or high-downside; load-bearing keepers |
| **T2 — Potentially important** | 38 | Real but narrower/situational/aging, or a merge-cluster member |
| **T3 — Likely not important** | 3 | Stale, superseded, or niche one-off — prune candidates |

**The honest finding: this corpus is mostly genuinely-live.** Only 3 files are outright prune candidates. The store isn't bloated with junk — it's bloated with *near-duplicates*. The real shrink levers are:
1. **Merge clusters** — ~7 feedback clusters + ~5 project chains collapse ~25 files into ~9 (see Merge Map). That alone takes 91 → ~65.
2. **The two-system overlap** — ~13 of the 21 instincts have a direct memory twin (see Instinct↔Memory Map). Consolidating instincts + memories into one system (the stated goal) is the larger structural win and removes the duplication at its root.

Tier definitions: **T1** = fires across many session types AND (high-frequency OR high-downside-if-violated). **T2** = real but narrow/situational/lower-frequency, currently-true-but-aging, or a member of a merge cluster. **T3** = stale/superseded/resolved/niche.

---

## Tier 1 — Important (50)

### Feedback — standing behavioral rules (31)
- `persist_decisions_immediately` — edit source-of-truth in the same response when status changes
- `stop_scope_checking` — after alignment, execute; don't ask "too much for one session?"
- `first_person` — say "I", never third-person "Leo"
- `always_commit` — commit+push at session end even if log skipped
- `write_artifacts_to_files` — substantive drafts (~50+ lines) get persisted with a proposed path
- `update_in_place_not_companion` — edit the original artifact, don't spawn parallel docs
- `priority_list_bare` — ranked list only; no tiers/hours/schedules/validation
- `dont_reask_unanswered` — after 1 unanswered ask, note as open input and proceed
- `explain_cost_mechanism` — lead with token cost + machine-on + free local alt for automation
- `inbox_no_read` — never read `inbox/` file bodies (Drive sync; pollutes context)
- `email_md_files_by_default` — new substantive `.md` under user dirs → auto `/send-me`
- `pinterest_internals_not_in_kb` — stakeholder/situational files go in `work+self/`, never `kb/`
- `james_role_altitude` — hold James as Sr EM M17 → Director M18; not M16, not IC
- `check_team_context_first` — read `team_members.md` before any team-interaction analysis
- `stakeholders_before_strategic_analysis` — read `stakeholders.md` before 3+-stakeholder analysis
- `verify_load_bearing_facts` — surface load-bearing facts (level/timing/manager-state) before anchoring
- `main_context_for_sequential_writes` — 5+ query-then-edit steps run in main context, not agents
- `work_leo_execution_scope` — don't flag work-leo tasks as unfinished in personal Leo
- `stop_ratchet_count_on_pushback` — drop "Nth consecutive session" counting on pushback
- `engagement_over_structure_in_thinking_partner` — lead with substance, not folder restructures
- `drop_sponsor_frame_on_technical_asks` — on technical-design asks, drop sponsor/narrative framing
- `coaching_register_before_strategic_grilling` — offer Coaching Patterns before tactical grilling
- `tactical_reality_check_works_in_rumination` — lead with evidence-marshaling per fear, not body-first
- `read_recent_files_before_critiquing_artifacts` — `ls -lat` the dir for the longer companion doc first
- `humble_instinct_flagged_as_insecurity` — push back on "humble" exec framing; replacement = OAV
- `ask_for_spine_before_drafting` — ask James for his structure before multi-beat narrative spines
- `dont_impose_fork_on_both_and` — hold both-and on reflective material; read literal caveats first
- `dont_inventory_speculative_artifacts` — list only what exists + the extension pattern
- `surface_structural_reality_on_peer_friction` — ask "what's happening structurally?" before pushback
- `credit_in_trust_relationships` — in high-trust sponsor circles, let the work speak; no credit framing
- `dont_over_fortify_on_sensitive_intel` — don't over-build defensive scripts; check structural fix first

### Project — live, load-bearing (11)
- `pinkerton_reflex_substrate` (5/27) — **current source of truth** for Pinkerton positioning
- `andrew_reflex_pm_hire` (5/27) — live Reflex escalation; 3 active pre-OOO asks
- `reflex_bill_ceo_altitude` (6/3) — Bill (CEO) review landed; feeds Director business case
- `jj_promo_dylan_parked` (6/3) — the live parked decision awaiting Dylan's ~7/6 return
- `kurchi_active_block` (6/3) — live block on CST/CFM; UPP co-ownership unwinding
- `dylan_director_commitment` (4/30) — Dylan named James+Dhruvil Director-next; hates hand-forced
- `dylan_staying_not_transitioning` (5/9) — Dylan NOT leaving; OOO 6/13→~7/6 only (live now)
- `director_timing_reframe` (5/9) — Director target 2027, not 2026 cycles (currency anchor)
- `dylan_action_sponsor` (5/5) — Dylan's lever = forward/resource/unblock, not co-thinking
- `rajat_complementary_sponsor` (5/3) — Director path under Dylan; Rajat complementary only
- `expectation_gap_engine` (4/30) — unhappiness runs on expectation-reality gap (durable anchor)

### Reference / Knowledge / User — durable facts (8)
- `user_james_profile` — core identity profile ⚠️ (stale: lists Rodney as active coach — see Verify Queue)
- `dylan_managerial_patterns` — 6 decoded Dylan patterns; high-frequency in prep
- `dylan_pronouns` — Dylan Wang = she/her; disambiguate from Darren's-team Dylan
- `andrew_yaroshevsky_seniority` — Andrew Y = Sr. Director Product, Reflex sponsor; comms calibration
- `external_systems` — NotebookLM UUIDs, work-leo loc, Rekko repo, Leo remote, graphify paths
- `gcp_leo_project` — `leo-api` GCP IDs powering /send-me + /save-to-drive
- `knowledge_upp_is_pretraining` — UPP = foundation pretraining, NOT a downstream consumer
- `knowledge_voice_transcription_artifacts` — predictable voice-mangling table + ask-early protocol

---

## Tier 2 — Potentially important (38)

### Feedback — situational / narrow / merge-cluster members (22)
- `active_grounding_default` — active sequence for post-trigger emotional disambiguation *(merge: emotional cluster)*
- `engagement_gap_vs_asking_gap` — manager-initiated career convo = engagement gap, not asking gap
- `channeled_review_caveat` — mark channeled (non-RAG) reviews explicitly; re-run when notebook lands
- `cross_framework_convergence` — two grounded frameworks converging = ship, stop iterating
- `bibliography_diff_pattern` — structured diff agent for paper-citation reviews
- `decisive_interview_feedback` — commit to the evidence-based call on interview writeups
- `factor_compounding` — score compounding into adjacent goals on "was it worth it?"
- `peer_register_in_open_channels` — peer-agreement gift framing in open senior channels *(merge: senior-comms)*
- `substance_over_handoff_first_contact` — substantive co-think on first senior contact *(merge: senior-comms)*
- `subtle_homage_to_seniors` — lineage attribution, not performative thanks *(merge: senior-comms)*
- `verify_stakeholder_text` — flag missing verbatim before synthesizing a reply *(merge: verify family)*
- `verify_stakeholder_baseline` — verify recipient's baseline knowledge before naming tools *(merge: verify family)*
- `verify_competitor_mapping` — verify the senior is actually racing candidates *(merge: verify family)*
- `verify_explore_stats` — treat agent-reported web stats as unverified *(merge: verify family)*
- `under_claim_in_flight_technical` — distinguish proven vs in-flight in sponsor material *(merge: verify family)*
- `silent_anchor_group_settings` — silent anchor in group settings the week after being featured
- `subfolder_for_multifile_sessions` — propose a subfolder at the 2nd file *(merge: artifact-handling)*
- `send_me_html_default` — `/send-me` always renders `.md`→HTML
- `project_memories_for_decisions` — backup project-memory for big decisions *(merge: into persist_decisions)*
- `task_list_in_flow` — no TaskCreate lists mid-flow *(merge: with priority_list_bare)*
- `next_time_items` — "Next time" = Leo-session work only *(merge: with work_leo_execution_scope)*
- `dont_over_pivot_to_seat_domain` — lead with obsession not seat domain ⚠️ near-dup of instinct `dont-over-rotate-identity`

### Project — background / aging / needs status check (14)
- `april_3_consensus_operating_frame` (4/3) — CG/Yan/Dhruvil ownership frame ⚠️ tension w/ yan_ib_redeployment
- `yan_ib_redeployment_live` (5/15) — Yan's IB maybe cut, engs to James ⚠️ unapproved, verify
- `jeff_mental_model_shift_5_7` (5/7) — Jeff 0-10%→55-65%; verbatim durable, % snapshot moved
- `charlie_pip_decision` (4/7) — Charlie PIP; CPP window + end-May deadlines elapsed ⚠️ verify outcome
- `kanan_karina_reorg_pattern` (5/3) — reorg = lost scope counter-anchor *(merge: with rajat_complementary)*
- `dylan_as_shield_rajat` (4/25) — Dylan POC-shield + cell-phone channel *(merge: Dylan operating-mode)*
- `reflex_4stage_pipeline` (4/15) — Detect/Build/Simulate/Prove vocab durable; status aged
- `pinkerton_agentic_commitment` (4/5) — Fork-A bet; blog 4/11 tripwire long past ⚠️ fold into Reflex history
- `active_coach_david_only` (4/29) — Rodney archived; David sole coach
- `initiate_dont_react` (4/2) — James reacts where Dhruvil initiates (durable lens)
- `technical_foundations_corpus` (5/31) — study corpus pointer
- `track3_promoted` (4/5) — ML system-design prep = P1, optionality *(merge: goals.md housekeeping)*
- `agents_md_split` (5/23) — repo structure reference
- `folio_rename` (5/23) — Viral Remix → Folio, personal side-project

### Reference — narrow / could-stale (2)
- `aman_ai_primers` — read converted markdown not PDFs (interview-prep only)
- `claude_code_rate_limit` — 7pm PT reset; preserve outputs on long subprocess runs

---

## Tier 3 — Likely not important (3)
- `project_graphify_phase1` (4/8) — Phase-1 ship snapshot + 3 known issues; issues likely resolved/abandoned, and the graph.json paths are already in CLAUDE.md. **Prune or fold into CLAUDE.md.**
- `project_networking_goal_dropped` (4/5) — records that Goal 6 was removed from goals.md; a settled, closed housekeeping fact. **Prune** (goals.md already reflects it).
- `feedback_screenshot_page_labeling` (4/25) — label stacked screenshots by visible page-range; niche, tied to one extraction mishap, rarely fires. **Prune or fold into a general "handling shared images" note.**

---

## Merge Map (the shrink lever within memories)

**Feedback clusters (≈18 files → ≈6):**
1. **Verify-before-building** → one memory w/ named sub-cases: `verify_load_bearing_facts` (hub) + `verify_stakeholder_baseline` + `verify_stakeholder_text` + `verify_competitor_mapping` + `verify_explore_stats` + `under_claim_in_flight_technical`
2. **Read-the-context-stack-first** → `check_team_context_first` + `stakeholders_before_strategic_analysis` + `read_recent_files` + `dont_over_fortify_on_sensitive_intel` (bridges into #1 via verify_load_bearing)
3. **Senior-cultivation comms** → `substance_over_handoff_first_contact` (first contact) + `peer_register_in_open_channels` (follow-up) + `subtle_homage_to_seniors` (credit)
4. **Engage substance, don't pre-structure** → `engagement_over_structure` + `ask_for_spine_before_drafting` + `dont_impose_fork_on_both_and` + `dont_inventory_speculative_artifacts`
5. **Emotional/coaching register first** → `coaching_register` + `active_grounding_default` + `tactical_reality_check` + `engagement_gap_vs_asking_gap`
6. **Drop sponsor/credit framing** → `drop_sponsor_frame_on_technical_asks` + `credit_in_trust_relationships`
7. Small pairs: `persist_decisions` + `project_memories_for_decisions`; `priority_list_bare` + `task_list_in_flow`; `write_artifacts` + `update_in_place` + `subfolder_for_multifile`; `work_leo_execution_scope` + `next_time_items`; `channeled_review_caveat` + `cross_framework_convergence` + `humble_instinct` (grounded-review discipline).

**Project chains (≈11 files → ≈4):**
1. **Reflex/Pinkerton** → `pinkerton_reflex_substrate` (current truth) carries live state; `andrew_reflex_pm_hire` shares the identical "3 pre-OOO asks" (merge); fold `pinkerton_agentic_commitment` + `reflex_4stage_pipeline` into one "Reflex genesis" history note.
2. **Dylan/Director state** → `dylan_director_commitment` + `director_timing_reframe` + `dylan_staying_not_transitioning` (complementary, resolve together).
3. **Dylan operating-mode** → `dylan_action_sponsor` + `dylan_as_shield_rajat`.
4. **Sponsor anchors** → `rajat_complementary_sponsor` + `kanan_karina_reorg_pattern` (the file says "pair these").
5. **goals.md housekeeping** → `track3_promoted` + `networking_goal_dropped`.

---

## Instinct ↔ Memory overlap (the root of "two systems")

~13 of the 21 instincts have a direct memory twin. The clearest:

| Instinct | Memory twin(s) |
|----------|----------------|
| `check-existing-context-before-analyzing` | check_team_context_first, stakeholders_before_strategic_analysis, read_recent_files, dont_over_fortify_on_sensitive_intel, work_leo_execution_scope |
| `execute-after-decision-signal` | persist_decisions_immediately, stop_scope_checking |
| `hold-hypotheses-loosely` | verify_load_bearing_facts, verify_competitor_mapping, surface_structural_reality |
| `plain-language-on-emotional-topics` | coaching_register, active_grounding_default, tactical_reality_check |
| `calibrate-exec-artifact-reads` | humble_instinct_flagged_as_insecurity, under_claim_in_flight, verify_stakeholder_baseline |
| `respect-scope-containment-signal` | stop_scope_checking, dont_reask_unanswered, drop_sponsor_frame, inbox_no_read |
| `separate-real-seed-from-engine-embellishment` | dont_inventory_speculative_artifacts, under_claim_in_flight, verify_stakeholder_text |
| `dont-over-rotate-identity-to-fit-target` | **dont_over_pivot_to_seat_domain** (near-identical) |
| `honor-explicit-preference-ask` | priority_list_bare, send_me_html_default |
| `synthesize-dont-deflect` | decisive_interview_feedback, engagement_over_structure |
| `clean-concrete-rosters` | priority_list_bare, stakeholders_before_strategic_analysis |
| `personal-taxonomy-over-content-type` | pinterest_internals_not_in_kb, subfolder_for_multifile, next_time_items |
| `prefer-chat-synthesis-during-iteration` | ask_for_spine_before_drafting, write_artifacts (inverse) |

This is the duplication to resolve when unifying the two systems.

---

## Verify / staleness queue (needs James's status check)

- `user_james_profile` — **lists Rodney as an active coach**; contradicts `active_coach_david_only` (Rodney archived 4/29). Also "~17 reports" + "hiring EM backfill" may have moved with the recent org redesign. Reconcile.
- `external_systems` — lists 4 NotebookLM notebooks; MEMORY.md/CLAUDE.md reference a **5th (Ethan Evans Frameworks)**. Add it.
- `charlie_pip_decision` — CPP window + end-May deadlines elapsed; what was the outcome?
- `yan_ib_redeployment_live` ↔ `april_3_consensus_operating_frame` — did the IB redeployment land? If so, the 4/3 ownership split is partly void. Reconcile these two into current reality.
- `jeff_mental_model_shift_5_7` — the % snapshot (55-65%) and 48h SLAs have moved; the must-win presentation has since happened.
- `andrew_yaroshevsky_seniority` — 72-day-old level claim; per James's own verify-load-bearing rule, spot-check.
- Reference IDs worth a one-time spot-check: NotebookLM UUIDs + graphify version/paths (`external_systems`), GCP project id (`gcp_leo_project`), the aman markdown dir path (`aman_ai_primers`).

---

*Audit only — no files changed. Next step (separate pass): act on the merge map + unify instincts/memories into one system.*
