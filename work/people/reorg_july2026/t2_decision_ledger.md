# T2 Decision Ledger — what's decided, what's undecided

*Living ledger, dated entries newest-first. Created 2026-08-21 at James's instruction ("write down what's decided and what's undecided"). Scenario analysis stays in `t2_team_setup_scenarios_2026-08-11.md`; the boards themselves in `scenario_boards/`; process discipline in `t2_ownership_ask_timeline_2026-08.md`. This file is the running answer to "where are we?"*

---

## Entry 2026-08-28 (Fri, remote session) — preferences only, nothing decided

**Nothing in this entry is a decision.** These are stated preferences — inputs under published criterion 3 ("preferences are inputs, not claims; everything goes into the design, nothing said now is a commitment"). Recorded here so they can't quietly harden into expectations, and so the trail shows what was known when the fall calls get made.

### STATED PREFERENCES (inputs, not commitments)

| Who | Preference | Source | Weight |
|---|---|---|---|
| **Ryan + Rui** | Want to work together on **LWS + L1 utility** | James-heard | Two-person, mutual. Continuity-flavoured: Ryan's 7/15 workstream line is already "CLR · LWS (dev-velocity focused)" and Rui owns L1/Real-Time, which is where LWS's obligation load runs. |
| **Yichi** | Happy on **CLR**; **eventually wants more UPP**; **fine with Alim** | James-heard | First preference datapoint on file for him. Costs nothing today — it agrees with the settled board. The UPP want is the part to hold. |
| **Roderick** | **Wants to keep reporting to Daniel** | **JJ → James (secondhand)** | Second independent relay pointing the same way as Daniel's 8/19 report. Confound reduced (JJ has no stake in the answer), **not** removed. Own voice still the gate. |

**Roderick — explicit stance (James, 8/28): let him come to James himself.** No summons, no prompting. Undecided question 3 below is unchanged; the 8/10 word ("your deepest priority will always be UEB") still stands, and Roderick → Daniel remains cap-blocked at 13 regardless of what he wants.

### Board work (exploratory)

- **`scenario_boards/scenario_8_2026-08-28.json`** — Sc 6 with Ryan → Daniel/LWS and the Zili backfill seat → Alim, to test whether the Ryan+Rui preference can be honoured inside the caps. It can: **James 4 / Alim 12 / Daniel 12**, LWS lands exactly on its target of 5 (Yali, Hedi, Rui, Ryan, REQ-2) with Ryan replacing the backfill 1-for-1. Costs: UPP+CLR pool 6 → 5 (worst of the eight boards; CLR drops to Devin/Yichi/Nima), and Alim's 12th becomes a req whose existence is dated by Zili's PIP/severance outcome rather than a body. **A scenario, not a proposal.**
- `check_scenarios.py` — fixed a hardcoded absolute path, now auto-discovers `scenario_*.json`, and honours a per-board `workstreams` override so a board that moves someone *into* a workstream is scored on its real shape. Fresh run of all eight boards: `issues_report_2026-08-28.txt`.

### Open capture item

- The **Tue 8/25 1:30 Roderick "choice conversation"** outcome has never been filed (carried unfiled from the 8/25 log). If it happened, an own-voice datapoint may already exist and simply be uncaptured — worth checking before treating JJ's relay as the newest information.

---

## Entry 2026-08-21 (Fri morning, remote session)

### DECIDED — workstreams (the spine)

| Workstream | Owner | People |
|---|---|---|
| UPP | **James** | Piyush, Zihao |
| Reflex | **James** | JJ · Bella (Reflex 1° / RecGPT 2°) |
| LWS | **Daniel** *(settled 8/21; T1 grant confirmed)* | Yali, Hedi, Zili-seat/backfill, Rui, + REQ-2 |
| CLR | **Alim** *(settled 8/21; his own 8/20 lean confirmed)* | Devin, Yichi, Ryan, Nima, Yiping (~9/14) |
| RR | **Alim** *(confirmed 8/21; incumbent-blessed since 8/11)* | Chuxi (ws-TL), Yidi, Alok, Kim (pencil) |
| RB / Collection P13N | **Daniel** *(confirmed 8/21)* | Yongwoo, Felix |

### DECIDED — people & mechanics

- **Bella stays James-direct** on every board (rating-handoff hold); if GenRet moves, the charter matrixes without her.
- **Kim → RR under Alim** (8/21 pencil, her lean). Structure finalized: her choice RR-vs-CLR by **9/11**; reports to a line EM either way; announcement ~9/14 (slide-to-9/21 rec open).
- **Yiping out of RB → the UPP+CLR pool as its 7th** (8/21). Execution = the 8/19 joint decision with Daniel: RB ramp from 8/24, James meets her week 1, transition ~9/14. No promise-ledger cost.
- **Zili's line stays James through the PIP case**; she is severance-seeking — her LWS seat is planned as **backfill (open)**.
- **Rui rides with LWS** · **Nima rides with CLR** · **Ryan full-time CLR** (was secondary).
- **Staffing targets:** UPP+CLR = **7** (Piyush, Zihao + Devin, Yichi, Ryan, Nima + Yiping) · LWS = **5** (Yali, Hedi, Zili/backfill, Rui, +1).

### RULED 2026-08-21 (James)

1. **REQ-2 ↔ Yiping are interchangeable** — both new, both IC13 MLE. One fills the UPP+CLR 7th, one fills the LWS 5th; default assignment = Yiping → CLR pool (her standing want + the 8/19 joint decision), REQ-2 → LWS. Swappable without redesign.
2. **The ≤12 cap counts everything:** a person on leave (Yang) counts, and open reqs count.

### THE ARITHMETIC CONSEQUENCE (falls out of the rulings — check before any move)

With the spine + rulings, the working board is **exactly James 4 / Alim 12 / Daniel 12** (Alim: RR 4 + UEB 3 + CLR 5 · Daniel: LWS 5 + GenRet 2 + IB 2 + RB 2 + Yang). **Both EMs at cap, zero headroom.** Therefore:

- **Roderick → Daniel is arithmetically blocked** (13) unless something displaces — realistically only if the IB gate misses *and* Balaji/Ling redeploy off his line, or a Daniel want yields.
- **GenRet → Alim is arithmetically blocked** (14) — the fork is effectively *Daniel vs. continued park*, no longer Daniel vs. Alim.
- **Any new hedge req must land on James's line** (no cap) — which is where a UPP hedge would sit anyway.
- Kim choosing CLR instead of RR changes nothing: Alim stays 12.

### UNDECIDED — the five questions

1. **GenRet/RecGPT owner.** Daniel wants the scope (senior-growth motivation; not Bella — carve standing). Alim's stated preference "probably isn't RecGPT" — a lean away, **not** a decline (James's 8/21 correction of an earlier overread). Park with James stands procedurally; **November decides** on evidence + the published criteria. Under the cap ruling the live fork is Daniel-vs-park. Yuke's line moves ≥9/14 regardless (peer-validation Aug–Sept).
2. **IB · LLM-pUIC.** Two nested questions at the **~Oct gains-origin gate**: does IB carry forward, and which EM's LLM lane does the Area 9 capability attach to. Balaji + Ling travel as one group; Balaji's L16 line move needs **Dylan sign-off**. This is also where Daniel's cap trade resolves: his wants (LWS-5 + GenRet + RB + Roderick + IB + Yang) sum to 13–14 vs his own ≤12 — the gate decides which want yields.
3. **Roderick.** Contested both directions: Daniel wants to keep him (all 3 of his scenarios); the off-UEB-post-Q3 preference is Daniel-sourced and uncorroborated; moving him off UEB requires James to explicitly walk back the 8/10 word ("your deepest priority will always be UEB") and guts UEB's systems spine on Alim's weakest axis. **Gate: Roderick's own voice — the pending skip-level is the highest-information move left.** *(8/28: JJ relays that Roderick wants to stay with Daniel — a second secondhand source agreeing with Daniel's, which reduces but does not remove the confound. Gate unchanged; James is letting Roderick come to him. See Entry 2026-08-28.)* UEB's shape (intact under Alim vs. split) and Esteban follow his answer. Note: keeping him on Daniel is also cap-blocked at current counts (see above).
4. **Yang's T2 line.** Undecided. Under the strict-count ruling he consumes a cap slot wherever he lands — currently penciled on Daniel (his day-1 line, fits at exactly 12); moving him to Alim would breach. Mid-leave manager changes also carry a people-care flag (he'd return to a manager he's never met).
5. **The UPP hedge.** Piyush is an unhedged SPOF at UPP = 2. Does James open a new req (lands on his own line, no cap issue) — and does it happen inside the free-quota window (~400 candidates, LR mid-Aug, zero L2 cost) before it closes?

### PENDING, NOT CONTESTED (dated waits, no open argument)

- Kim's **9/11** confirmation → announcement **9/14** (Leo rec to slide to Mon 9/21, unratified).
- **Chuxi/Kim named-lanes charter** (Chuxi ws-TL · Kim explorative-pUIC spine) — due before the announcement; Olafur anchor ask attached.
- **Phase-1 symmetric ownership ask** ~9/15 (Leo rec: slide to wk of 9/21 given the offsite collision + Daniel's China-remote window, unratified).
- **LLM×Recs lane sizing/naming** for October brokering: Daniel's bet sized from his own can-merge list; Alim's grant scoped to *LLM-pUIC inside RR*, never "LLM stuff."
- GenRet park comms + Yuke ≥9/14 transfer mechanics, whichever way the fork resolves.
- November = the settle-as-summary, per the published process.
