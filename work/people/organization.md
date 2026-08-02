# organization.md — Org Structure & Cross-Org Context

Last updated: 2026-08-01 (people-folder reorg: James's-org people/project/scope content moved to [`team_members_scope.md`](team_members_scope.md); this file now covers org structure and teams **outside** James's org. Leadership chain updated to the approved July-reorg state — announcement Wed 8/5. Prior: 2026-05-23 Slack-verified org chart.)

---

## Purpose
Canonical org-structure reference: the leadership chain, Dylan's org layout, and context for teams outside James's org (SSJ/Search, peer EMs, cross-org partners).

**For James's own org — roster, per-person context, charters, workstreams, scope boundaries, canonical outcomes — see [`team_members_scope.md`](team_members_scope.md)** (source of truth since 2026-08-01; absorbed this file's team-structure/scope/2025-2026 sections).

Tier1 rule: **no raw docs here**. Point to them.

---

## Org / Team Overview
- **Company:** Pinterest
- **Org:** Discovery → Homefeed Relevance (Dylan Wang, Sr. Director)
- **James's org:** **P13N Retrieval** (announcement Wed 8/5 — retires "HF Candidate Generation"; details in `team_members_scope.md`). Peer ML org: **P13N Ranking** (Dhruvil).

---

## Leadership Chain

> Updated 2026-08-01 to the **approved post-reorg state** (Dylan's reorg, aligned with Rajat + HR; org-wide announcement **Wed Aug 5**; Dylan tells Daniel/Yan Mon 8/3). Report counts marked pre-reorg where not re-verified.

```
Bill Ready (CEO)
└── Matt Madrigal (CTO)
    └── Jeff Harrell (VP, Engineering - Core)
        ├── Rajat Chaturvedi (VP, Engineering)
        │   ├── Dylan Wang (Sr. Director, ML — Homefeed Relevance) — ~132 reports (pre-reorg count)
        │   │   ├── James Li (Sr. Manager M17, ML — P13N Retrieval) — org ≈ 2 EMs + ~24 ICs (+2 open reqs, 1 intern)
        │   │   │   ├── Daniel Liu (Manager II M16, ML — Curation ML) — 7 ICs — lateral re-parent from Yan eff. 8/5; team intact under Daniel in the interim
        │   │   │   └── Alim Virani (Manager II M16, ML — Retrieval Modeling [T1; was "Anticipation Modeling" in July design]) — started 7/27; day-1 pod Chuxi/Yidi/Alok/Lionel
        │   │   ├── Dhruvil Deven Badani (Sr. Manager M17, ML — P13N Ranking)
        │   │   │   ├── Rahul Goutam (Manager II M16, ML — Blender) — moves under Dhruvil with the blending team (~5–6 eng) in the same reorg; was direct to Dylan
        │   │   │   └── Zisis Petrou (EM — GULP)
        │   │   ├── Yan Li (Sr. Manager M17, Eng — P13N-Experiences) — sheds Daniel's Curation ML to James; Curation Revisitation stays in his org
        │   │   │   └── Edward Zhuang (Manager I L15, Eng) — 7 reports — backend SWE pool
        │   │   ├── Tim Leung (Manager M16→**M17** per 7/14, Eng — Presentation: ngAPI + Android/iOS client) — stays under Dylan; non-ML
        │   │   ├── Francisco Navarrete (Sr. Manager L17, Eng — Platform/Labeling) — 16 reports — exiting to Kurchi
        │   │   ├── Olafur Gudmundsson (Sr. Staff MLE — IC, direct to Dylan)
        │   │   └── Dafang He (Sr. Staff MLE — IC, direct to Dylan) — Search CLR lead; Reflex overall TL
        │   ├── Kurchi Subhra Hazra (Sr. Director, ML — Search/SSJ) — 114 reports
        │   │   └── Vasil Kasmitski (Manager II, Eng)
        │   ├── Kaanon MacFarlane (Director, Eng) — 34 reports
        │   │   └── (Frontend/backend, no ML. Working with Karina on AI initiative for Rajat)
        │   └── Karina Sobhani (Director, Eng) — 15 reports
        │       └── (Frontend/backend, no ML. Team has shrunk. Working on AI initiative with Kaanon)
        ├── Faisal Farooq (VP, Engineering — Trust & Safety, Signals) — 200 reports
        ├── Shipeng Yu (Sr. Director, ML — Growth) — 122 reports
        ├── Manu Sharma (Sr. Director, Data Science) — 27 reports
        └── Phil Price (Distinguished Engineer)

Other CTO direct reports (outside Jeff's chain):
├── Matthias Zenger (VP, Engineering)
├── Vik Gupta (VP, G&I Monetization)
├── Vicky Gkiza (VP, Product Management)
├── Carmen Maierean (VP, EPD Strat & Ops)
├── Chuck Rosenberg (VP, Engineering)
├── Ken Cushman (CIO)
├── Dana Cho (VP, Design)
├── Andy Steingruebl (CSO)
├── Brittan Bushman (Sr. Director, Corporate Strategy)
└── Kartik Paramasivam (Chief Architect)
```

*Pre-reorg chain (Daniel under Yan; Rahul direct to Dylan; James = "HF Candidate Generation, 17 reports") is in git history if needed.*

## Key people / stakeholders outside James's org (canonical)

> Full profiles live in [`stakeholders.md`](stakeholders.md) — this is the quick structural map. James's own team members (Piyush etc.) → `team_members_scope.md`.

- **Dylan Wang:** Sr. Director of Homefeed Relevance
  - Style: values accuracy and exec-ready comms; peak trust with James
  - Direct reports post-reorg: James, Dhruvil, Yan, Tim, Francisco (exiting), Olafur, Dafang
- **Rajat C:** VP of Engineering under Jeff
  - Joined from leading Alexa at Amazon
  - Direct reports: Dylan, Kurchi, Kaanon, Karina
- **Jeff Harrell:** VP of Engineering - Core (Rajat's manager)
  - High-I/D profile. Loves demos, "cool work," and engineering culture modernization.
- **Dhruvil:** Sr EM for P13N Ranking (peer under Dylan). Sub-EMs: **Rahul Goutam** (Blender — moves under him with the blending team in the reorg) + **Zisis Petrou** (GULP — Dylan named Zisis's team as GULP owner, 6/1)
- **Yan Li:** Sr EM for P13N-Experiences (peer under Dylan). Frontend + backend SWE (Edward Zhuang). Owns Explore/IB surfaces on the experience side; Curation Revisitation stays with him post-reorg.
- **Tim Leung:** Manager under Dylan (M16→M17 per 7/14 intel; 13 reports). Presentation: ngAPI + Android/iOS client. James mentors him. TL Yu Zhao is one of the best engineers in the org.
- **Francisco Navarrete:** Sr Manager under Dylan (16 reports). Team primarily in Mexico. Labeling + foundational platform work. Exiting to Kurchi. Good relationship with James.
- **Olafur Gudmundsson:** Sr. Staff MLE under Dylan. IC. Involved in ownership boundary discussions; looped into pUIC architecture reviews.
- **Dafang He:** Sr. Staff MLE under Dylan. Search CLR lead; **Reflex overall TL** (Dylan-named POC trio: James/Dafang/Tim-PM).
- **Kartik Paramasivam:** Chief Architect, reports to CTO. Fan of James's work. Has connected with Dylan about James. Dylan has hinted Kartik's support is important for James's future.
- **Faisal Farooq:** VP Eng under Jeff. Owns T&S + Signals (content understanding, user understanding). Very technical, KDD chair. Open supporter of UPP.
- **Shipeng Yu:** Sr. Director ML (Growth) under Jeff (122 reports). Close to Dylan. Org was pushed into UPP by Jeff — now supportive. Brian Lee and Tingting (Notifications) report to him.
- **Cross-org partners (non-exhaustive):** ATG, ML Infra/Core Infra, Notifications ML, Growth/Activation, UU (User Understanding), Search/Related Pins surfaces

### Notable: Raymond Hsu
Reports to Tim Leung. Was the previous HF CG manager before James joined above him. Transitioned back to IC unwillingly. Holds resentment toward James. Not an active risk but worth tracking. (Now also the SM/SL pairing alongside Yali — staffed 7/25.)

### SSJ reorg (Kurchi's org) — effective 2026-05-01

Announced 2026-04-23 by Kurchi. Key changes relevant to James's strategic landscape:

- **Text Search Relevance → Roberto Konow.** Gets end-to-end scope: query understanding + rewriting + retrieval + light-weight ranking + final relevance/blending. Absorbs Query Understanding team (An/John Jiang, Ishita Dasgupta, Aakanksha Sanctis). **Major position strengthening for Roberto.** Full-stack text search owner now. *(2026-07 note: Roberto also runs Shifu, the SSJ agent platform — Shifu↔Reflex integration thread opened 7/29.)*
- **Semantic Relevance → Xi Chen** (Search Ranking and Blending). Han Wang, Austin Jenkins, Mukuntha Narayanan, Bonnie Liu move under Xi.
- **Closeup Relevance → Huizhong Duan** (renamed to Closeup and Multimodal Relevance). Zhenjie Zhang joins leadership bench.
- **Multimodal Search → Sai Xiao** (unified Closeup Retrieval and Multimodal Search).
- **Krishna Kamath → new SSJ Intent Navigation and Platform org.** This is the cautionary case. Krishna was non-promoted at Director EOY 2025 (feedback: "lacked visibility outside org"). Asked Kurchi for how to improve and try again in July; Kurchi pushed timeline to "a year." Reorg then moved his flagship scope (Text Search Relevance) to Roberto; Krishna now runs Query Recommendations (Madhur Kapoor reporting in) + new SSJ Platform team (platform optimizations, ML efficiencies, observability). Kurchi's framing: *"forming the connective tissue for our experience and relevance teams."* Krishna's read: graveyard. Taking weeks off in India, then starting to look externally. Warned James explicitly to be cautious. **This is the empirical "Kurchi move" pattern: failed promo → timeline pushed → scope rebalanced away → flight.**

### Name normalization (must preserve in outputs)
- Hong Tao → **Hongtao**
- Jay Wong / Jay → **Jaewon**
- RecGBT → **RecGPT** (also known as **PinRec**)
- "Ray" → **Rui Wang** (dictation artifact; corrected 2026-07-15)
- Raymond Su → **Raymond Hsu** (canonical spelling, 2026-07-22)

---

## Review cadence
- Last Updated: 2026-08-01
- Next Review: monthly (or on the next reorg-state change — e.g., post-announcement verification of the 8/5 lines)
