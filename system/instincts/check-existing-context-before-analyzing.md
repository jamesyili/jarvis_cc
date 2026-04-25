---
id: check-existing-context-before-analyzing
trigger: When about to analyze or recommend anything about a known stakeholder, project, dynamic, or recurring situation that has documented history in the repo (stakeholders.md, projects/, dylan_1on1_log.md, etc.)
behavior: Before reasoning from first principles, GREP or read the existing context files for documented playbooks, prior decisions, historical incidents, or relationship analysis. Work WITH existing context, not around it. Surface the existing playbook first; only propose reinventing if James explicitly asks OR if new information genuinely invalidates the prior playbook.
confidence: 0.55
evidence_count: 2
created: 2026-04-23
last_updated: 2026-04-25
status: active
---

## Evidence

### 2026-04-23
> "You should already look back at Roberto's incidents to get a context on how he has reacted to potential collaboration attempts in the past, which is to say that he was very actively against it. Take a look at that context so you should know."

Context: James asked about the Roberto-vs-Pinsight dynamic. Leo proposed a "compete / cede / negotiate joint ownership" framework, recommending Option C (negotiate). James corrected directly: existing context at `stakeholders.md:913` and `projects/pinsight/strategic_next_steps_april.md:27` was already explicit. The documented playbook (from 2026-04-09) was: do NOT re-outreach to Roberto, structural Kurchi-Dylan proxy not peer-fixable, bypass via Reflex. James had explicitly tried collaboration in March 2026 (warm peer DM congratulating Roberto on Search Debugger). Roberto went silent for 9 days. Then territorially interrupted James's pitch at Brian Lee's forum 4/09 PM. The playbook concluded: "direct peer outreach is unlikely to resolve the friction." Leo's Option C recommendation was functionally re-proposing the March 2026 move that already failed — visible only by reading the context.

Signal: correction (explicit redirect to existing documented context; Leo's analysis was proposing something that contradicted the known playbook).

### 2026-04-25
> "And I have already demonstrated PINvestigator"

Context: James was preparing for Jeff office hours. Leo recommended *"open PINvestigator and demo it on a real investigation"* as the lead move for the OH. James corrected with one short sentence — he'd already demoed PINvestigator to Jeff (per `backlog.md` item: *"PINvestigator — 5 next steps from Jeff demo — all done as of 2026-04-17"*). Leo had not grepped the backlog before recommending the demo. Same pattern as the Roberto incident — analyzing without checking documented history. Caused Leo to revise the entire Jeff OH strategy (no PINvestigator re-demo; lead with three NEW associations: RR business impact + Pinsight cross-org adoption + Reflex-CTO demo teaser).

Signal: correction (terse but unambiguous). Two evidence points in 2 days on the same pattern. Heuristic: when proposing concrete tactical moves on known stakeholders, GREP the backlog + relevant project files + recent session logs first.

## Pattern

This is distinct from `corrections-interrupt-by-design` (which is about factual corrections that interrupt workflow). This instinct is about **analytical laziness that reinvents what's already documented.** Symptom: Leo reasons from first principles when existing context contains a better-grounded answer. Cost: James has to redirect, and in high-stakes strategic conversations (like stakeholder strategy), the wrong framework wastes decision cycles.

**Heuristics for when this fires:**

1. **Known-stakeholder questions** ("what should I do about Roberto / Andrew / Dylan / Rajat / Jeff?") — always grep `work+self/people/stakeholders.md` + `dylan_archive.md` first.
2. **Ongoing-project dynamics** ("how should I position Pinsight / RR / UPP?") — grep `work+self/projects/` + recent session logs.
3. **Recurring-situation patterns** ("how should I handle this 1:1 / skip-level / office hours?") — check `communication.md` playbooks and `dylan_1on1_log.md` for prior instances.
4. **When about to offer a multi-option framework** (A / B / C) on a known topic — pause and verify no option is known-failed. Leo's Option C re-proposed the March 2026 failed move.

**What Leo should do instead when the pattern might fire:**

- Spend one Grep before the analysis, not after.
- If documented playbook exists, SURFACE it first: "Existing playbook in `stakeholders.md:913` says [X]. Does that still apply, or has something changed?"
- If the playbook feels stale, name the staleness: "The 4/09 playbook assumed [X]. Given [new info], worth updating?"
- Only propose reinvention if James explicitly asks OR the existing playbook is obviously broken by new data.
