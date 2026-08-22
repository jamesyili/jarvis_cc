#!/usr/bin/env python3
"""T2 scenario checker — runs all 7 boards against the accumulated rulebook (as of 2026-08-21).

Rule vintage tags:
  [settled]  — settled rules/promises on file (caps, T1 grants, perf-case mechanics, Kim constraint)
  [8/21]     — this week's evidence: Alim's RecGPT relinquishment (8/20), Daniel's full thoughts
               (keep Roderick x3, wants GenRet-not-Bella), James's 8/21 staffing (UPP+CLR=7 w/ Yiping,
               LWS=5, Kim->RR)
Severity: BLOCKER (violates settled rule) / FORK (contradicts current evidence or 8/21 decisions)
          / WATCH (design debt, optics, timing)
"""
import json, sys
from collections import Counter

FULL2SHORT = {
    "Piyush Maheshwari":"Piyush","Bella Huang":"Bella","Balaji Rengarajan":"Balaji",
    "Devin Kreuzer":"Devin","Ryan Kam":"Ryan","J.J. Hu":"JJ","Yali Bian":"Yali",
    "Hedi Xia":"Hedi","Yuke Yan":"Yuke","Zihao Chen":"Zihao","Roderick Gao":"Roderick",
    "Esteban Zavala":"Esteban","Yiping Wang":"Yiping","Yang Liu":"Yang","Kim Toy":"Kim",
    "Yongwoo Noh":"Yongwoo","Nima Sheikholeslami":"Nima","Rui Wang":"Rui","Alok Malik":"Alok",
    "Zili Li":"Zili","Hanlin Lu":"Hanlin","Chuxi Wang":"Chuxi","Lionel Bewa":"Lionel",
    "Ling Lan":"Ling","Felix Yang":"Felix","Yichi Wang":"Yichi","Yidi Wang":"Yidi",
    "REQ-2 (open)":"REQ2",
}
ROSTER = set(FULL2SHORT.values())

# current workstream membership (for charter-split checks)
WS = {
    "UPP":["Piyush","Zihao"], "Reflex":["JJ","Bella"],
    "RR":["Chuxi","Yidi","Alok"], "UEB":["Roderick","Lionel","Esteban"],
    "CLR":["Devin","Yichi","Ryan","Nima"], "GenRet":["Yuke","Hanlin"],
    "LWS":["Yali","Hedi","Zili","Rui"], "IB":["Balaji","Ling"],
    "RB":["Yongwoo","Felix","Yiping"],
}
FRAGILE = {"Yuke":"active perf case (peer-validation Aug-Sept)","Alok":"high-maintenance",
           "Lionel":"triple-fragility","Chuxi":"ramping first-time ws-TL","Zili":"PIP live / severance-seeking"}
DAY1_DANIEL = {"Balaji","Kim","Ling","Felix","Yongwoo","Roderick","Esteban","Yang"}

def board(name, assign, capacity=None, note=""):
    return {"name":name, "assign":assign, "capacity":capacity or {}, "note":note}

def mk(james, alim, daniel):
    a={}
    for p in james: a[p]="James"
    for p in alim: a[p]="Alim"
    for p in daniel: a[p]="Daniel"
    assert set(a)==ROSTER, ("roster mismatch", set(a)^ROSTER)
    return a

J4=["Piyush","Zihao","Bella","JJ"]
boards=[]
boards.append(board("Sc 1 (By Stages, 8/15)", mk(J4,
    ["Chuxi","Yidi","Alok","Kim","Roderick","Lionel","Esteban","Devin","Yichi","Ryan","Nima","Yuke","Hanlin"],
    ["Yali","Hedi","Zili","Rui","Balaji","Ling","Yongwoo","Felix","Yiping","Yang","REQ2"])))
boards.append(board("Sc 2 (Barbell/spine, 8/15)", mk(J4,
    ["Chuxi","Yidi","Alok","Kim","Roderick","Lionel","Esteban","Devin","Yichi","Ryan","Nima"],
    ["Yali","Hedi","Zili","Rui","Yuke","Hanlin","Balaji","Ling","Yongwoo","Felix","Yiping","Yang","REQ2"])))
boards.append(board("Sc 3 (LWS<->CLR swap, 8/15)", mk(J4,
    ["Yali","Hedi","Zili","Rui","Chuxi","Yidi","Alok","Kim","Roderick","Lionel","Esteban"],
    ["Devin","Yichi","Ryan","Nima","Yuke","Hanlin","Balaji","Ling","Yongwoo","Felix","Yiping","Yang","REQ2"])))
boards.append(board("Sc 4 (IB->Alim, 8/15)", mk(J4+["Kim"],
    ["Chuxi","Yidi","Alok","Roderick","Lionel","Esteban","Devin","Yichi","Ryan","Nima","Balaji","Ling"],
    ["Yali","Hedi","Zili","Rui","Yuke","Hanlin","Yongwoo","Felix","Yiping","Yang","REQ2"])))

for path,nm in [("scenario_5_2026-08-21.json","Sc 5 (new 8/21)"),
                ("scenario_6_2026-08-21.json","Sc 6 (new 8/21)"),
                ("scenario_7_2026-08-21.json","Sc 7 (new 8/21)")]:
    with open(f"/home/james/src/leo/work/people/reorg_july2026/scenario_boards/{path}") as f:
        d=json.load(f)
    assign={FULL2SHORT[k]:v for k,v in d["assign"].items()}
    cap={FULL2SHORT.get(k,k):v for k,v in d.get("capacity",{}).items()}
    assert set(assign)==ROSTER, ("roster mismatch", set(assign)^ROSTER)
    boards.append(board(nm, assign, cap))

def mgr_of(a, ppl):
    return {p:a[p] for p in ppl}

def check(b):
    a=b["assign"]; issues=[]
    def add(sev,rule,msg): issues.append((sev,rule,msg))
    cnt=Counter(a.values())
    james=[p for p in a if a[p]=="James"]; alim=[p for p in a if a[p]=="Alim"]; daniel=[p for p in a if a[p]=="Daniel"]

    # --- James column [settled] ---
    extra=set(james)-set(J4); missing=set(J4)-set(james)
    for p in missing: add("BLOCKER","james-core",f"{p} off James's column — settled: Piyush/Zihao/Bella/JJ stay James (Bella = rating-handoff hold)")
    for p in extra:
        if p=="Kim": add("FORK","kim-seat","Kim on James = 100%-UPP-shaped seat — violates her stated not-100%-UPP line AND the 8/21 decision (Kim -> RR under Alim)")
        else: add("WATCH","james-core",f"{p} on James beyond the fixed four — James end-state = UPP + Reflex only")

    # --- EM caps [settled 8/19, both EMs' own words] ---
    for em in ("Alim","Daniel"):
        n=cnt[em]
        if n>12: add("BLOCKER","cap-12",f"{em} at {n} — breaches his own <=12 cap (8/19)")
        elif n==12: add("WATCH","cap-12",f"{em} at exactly 12 — zero headroom (LWS +1 req, Zili backfill, or any future add breaches)")

    # --- Kim [settled + 8/21] ---
    if a["Kim"]=="Daniel": add("BLOCKER","kim-notD","Kim -> Daniel — off the table (confidential manager-fit datapoint, 8/11)")
    elif a["Kim"]=="Alim":
        add("WATCH","kim-lanes","Kim on Alim/RR: Chuxi/Kim named-lanes charter (Chuxi ws-TL, Kim explorative-pUIC spine) due before ~9/14 announcement; Olafur anchor ask attached; Kim's own 9/11 confirmation still gates")

    # --- Zili [settled] ---
    if a["Zili"]!="James": add("WATCH","zili-case",f"Zili -> {a['Zili']}: her line stays James through the PIP case — placement is post-resolution only, and she is severance-seeking, so this seat is really 'backfill (open)'")

    # --- LWS: T1 grant + Rui rides + staffing [settled + 8/21] ---
    lws_mgrs=mgr_of(a,["Yali","Hedi"])
    lws_home=Counter(lws_mgrs.values()).most_common(1)[0][0]
    if set(lws_mgrs.values())!={lws_home}: add("WATCH","lws-split","LWS core (Yali/Hedi) split across managers")
    if lws_home!="Daniel": add("FORK","lws-grant",f"LWS -> {lws_home}: reverses the announced T1 grant (Daniel's #1 keep, oncall moved) — needs an explicit walk-back, effectively fenced")
    if a["Rui"]!=lws_home: add("BLOCKER","rui-rides",f"Rui -> {a['Rui']} but LWS sits with {lws_home} — settled: Rui rides with LWS wherever it lands")
    lws_ppl=[p for p in ["Yali","Hedi","Zili","Rui"] if a[p]==lws_home]
    req_lws = (a["REQ2"]==lws_home)
    eff=len(lws_ppl)-(1 if a["Zili"]==lws_home else 0)+(1 if a["Zili"]==lws_home else 0)  # count Zili seat as backfill seat
    staffed=len(lws_ppl)+(1 if req_lws else 0)
    if staffed<5: add("FORK","lws-5",f"LWS staffed at {staffed} incl. req ({'REQ-2 elsewhere' if not req_lws else 'REQ-2 counted'}) — 8/21 target is 5 (Yali, Hedi, Zili/backfill, Rui, +1 MLE); 8/19 note said +2-3 needed (highest Pinterest-wide obligation load)")

    # --- GenRet fork [8/21] ---
    g=mgr_of(a,["Yuke","Hanlin"])
    gh=set(g.values())
    if len(gh)>1: add("WATCH","genret-split",f"GenRet lines split ({g}) — charter travels as a unit (Bella matrixes, stays James)")
    home=g["Yuke"]
    if home=="Alim": add("FORK","genret-fork","GenRet -> Alim: contradicts BOTH 8/20-21 positions — Alim relinquished RecGPT in writing; Daniel wants the scope (senior-growth motivation, not-Bella; Bella carve already standing)")
    elif home=="James": add("FORK","genret-fork","GenRet stays James end-state — retired 8/15 (charter leaves James on every board) and James's keep-it urge was worked and dropped 8/21 morning")
    if a["Yuke"]!="Daniel" and a["Yuke"]!="James":
        add("WATCH","yuke-timing","Yuke's move lands on a new-to-him manager mid perf-arc — any transfer >=9/14 only (peer-validation Aug-Sept load-bearing)")
    elif a["Yuke"]=="Daniel":
        add("WATCH","yuke-timing","Yuke -> Daniel: transfer >=9/14 only (peer-validation Aug-Sept)")

    # --- UEB unit + Roderick [settled + 8/21] ---
    ueb=mgr_of(a,["Roderick","Lionel","Esteban"])
    if len(set(ueb.values()))>1: add("WATCH","ueb-split",f"UEB split {ueb} — 8/15: Esteban moves with UEB; Roderick is the systems spine; a split leaves the charter ambiguous (who owns UEB?) and orphans the remainder")
    if a["Roderick"]=="Daniel":
        add("FORK","roderick","Roderick -> Daniel honors Daniel's keep-him-in-all-3 want BUT: (a) needs Roderick's own voice — the off-UEB-post-Q3 row is Daniel-sourced, uncorroborated, skip-level pending; (b) requires James to explicitly walk back his 8/10 word to Roderick ('your deepest priority will always be UEB'); (c) guts UEB's systems spine on Alim's weakest axis")
    elif a["Roderick"]=="Alim":
        add("FORK","roderick","Roderick -> Alim holds the 8/10 UEB-priority word and the UEB spine BUT contradicts Daniel's 8/21 stated want (keep Roderick in all 3 scenarios) — corroborate with Roderick before adjudicating")

    # --- UPP+CLR = 7 pool [8/21: James/Devin agreement + Yiping as the 7th] ---
    clr_mgrs=mgr_of(a,["Devin","Yichi"])
    clr_home=Counter(clr_mgrs.values()).most_common(1)[0][0]
    pool=[p for p in ["Devin","Yichi","Ryan","Nima"] if a[p]==clr_home]
    pool_n=2+len(pool)+(1 if a["Yiping"]==clr_home else 0)
    if pool_n!=7: add("FORK","pool-7",f"UPP+CLR pool = {pool_n}, target 7 (James/Devin agreement; Piyush+Zihao stay James, rest report to the CLR owner) — Yiping is the designated 7th per 8/21")
    if a["Yiping"]!=clr_home: add("FORK","yiping",f"Yiping -> {a['Yiping']}: contradicts 8/21 'pull Yiping out of RB' + the 8/19 joint decision (RB ramp from 8/24, transition to other efforts ~9/14, standing want = CLR)")
    if a["Nima"]!=clr_home: add("WATCH","nima-clr",f"Nima -> {a['Nima']} but CLR sits with {clr_home} — Nima was hired into CLR and rides with it")

    # --- Alim engine ballast (R3) [settled] ---
    alim_engine = (clr_home=="Alim") or (lws_home=="Alim")
    if not alim_engine: add("BLOCKER","alim-engine","Alim holds no delivering engine (no CLR, no LWS) — R3 violated: all-bets column, no floor if bets stall")

    # --- Alim senior/TL seat [settled 8/12 spec] ---
    seniors=[p for p in ["Nima","Balaji","Roderick"] if a[p]=="Alim"]
    if not seniors:
        if a["Kim"]=="Alim": add("WATCH","alim-senior","Alim's systems-TL seat spec unmet — Kim (L15) present but the spec wants a systems-strong pushback TL (Nima/Balaji/Roderick profile)")
        else: add("BLOCKER","alim-senior","No senior on Alim's leg at all — his own named gap")

    # --- fragile-stack on Alim [settled worry] ---
    frag=[f"{p} ({FRAGILE[p]})" for p in FRAGILE if a[p]=="Alim"]
    if len(frag)>=3: add("WATCH","fragile-stack",f"Fragile stack on the day-~180 remote EM: {len(frag)} — "+"; ".join(frag))

    # --- Yang [settled: on leave, out of H2] ---
    if a["Yang"]!="Daniel": add("WATCH","yang-leave",f"Yang -> {a['Yang']}: manager change executed mid-leave — he is out of H2 entirely, returns to a manager he has never met; also inflates {a['Yang']}'s paper headcount with zero H2 capacity")
    if b["capacity"].get("Yang")==1: add("WATCH","yang-cap","Board counts Yang at capacity 1.0 — overstates real H2 capacity (he is out of H2)")

    # --- Balaji+Ling pairing [8/15: IB.LLM-pUIC one group] ---
    if a["Balaji"]!=a["Ling"]: add("WATCH","ib-pair",f"Balaji ({a['Balaji']}) and Ling ({a['Ling']}) split — IB.LLM-pUIC is one group; they carry both, and the LLM x RecSys fold-back travels with them")

    # --- Daniel carve optics [tool's own banner precedent] ---
    leavers=sorted(DAY1_DANIEL-{p for p in DAY1_DANIEL if a[p]=="Daniel"})
    if len(leavers)>=4: add("WATCH","carve-optics",f"{len(leavers)} of Daniel's day-1 roster leave his line ({', '.join(leavers)}) — the planner's own bad-optics banner fired at 4 (Kim's exit is forced by the confidential constraint; still counts in the optics)")

    # --- Daniel cap vs IB visibility [8/21] ---
    if cnt["Daniel"]>=12 and a["Balaji"]=="Daniel":
        add("WATCH","ib-cap","Daniel >=12 with IB (Balaji+Ling) on his line: his own scenarios fit the cap only by pre-deleting IB, which James ruled stays visible through the ~Oct gate — the gate now resolves both IB's home and Daniel's cap")

    # --- RB thinning [8/21] ---
    rb=[p for p in ["Yongwoo","Felix","Yiping"] if a[p]==a["Yongwoo"]]
    if len(rb)<=2 or a["Yiping"]!=a["Yongwoo"]:
        add("WATCH","rb-thesis","RB at ~2 (Yongwoo, Felix) after the Yiping pull — blessed 8/19, but name Collection P13N as Daniel's funded investment thesis explicitly so it doesn't read as quiet defunding of his one argued-for want")
    return issues

SEV_ORDER={"BLOCKER":0,"FORK":1,"WATCH":2}
report=[]
for b in boards:
    a=b["assign"]; cnt=Counter(a.values())
    issues=sorted(check(b), key=lambda x:SEV_ORDER[x[0]])
    report.append((b,cnt,issues))

for b,cnt,issues in report:
    print("="*100)
    print(f"{b['name']}   —   James {cnt['James']} / Alim {cnt['Alim']} / Daniel {cnt['Daniel']}"
          + (f"   capacity overrides: {b['capacity']}" if b['capacity'] else ""))
    ic=Counter(s for s,_,_ in issues)
    print(f"   issues: {ic.get('BLOCKER',0)} blocker / {ic.get('FORK',0)} fork / {ic.get('WATCH',0)} watch")
    for sev,rule,msg in issues:
        print(f"   [{sev:7}] ({rule}) {msg}")
print("="*100)
print("SUMMARY  (blockers / forks / watches)")
for b,cnt,issues in report:
    ic=Counter(s for s,_,_ in issues)
    print(f"  {b['name']:32} J{cnt['James']}/A{cnt['Alim']}/D{cnt['Daniel']}   {ic.get('BLOCKER',0)} / {ic.get('FORK',0)} / {ic.get('WATCH',0)}")
