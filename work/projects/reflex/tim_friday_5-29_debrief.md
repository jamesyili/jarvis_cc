# Tim Friday 5/29 Debrief — what actually emerged

**Source:** James's read-out (5/31). Convo itself went well: *"He will run with this and Dafang is excited to drive this as TL."*

Companion to: `tim_friday_5-29_roadmap.md` (the pre-convo roadmap).

---

## Structural decisions confirmed

- **Reflex overall TL: Dafang He.** Operational ownership sits with Dafang, not James. James's altitude moves up — architect / sponsor / cross-org orchestrator, not program manager.
- **PM: Tim** (⟨surname pending⟩ — see stakeholders §36). Tim picked up the platform PM role cleanly; ran with the roadmap framing.
- **Sponsor: Andrew.**

## Goal-setting axes (Reflex success metrics)

1. **SSv2 & WAU** — topline business metrics
2. **System deliverables** — the platform shape itself
3. **XFN acceleration** — *"PMs / Designers can ship ideas"* — XFN throughput is now a first-class goal, not a side effect

**Note for James:** the Foundation layer from the pre-convo roadmap (RLHF/Curator + Prove-loop + Velocity, framed as un-staffed funding ask) **did not survive as a standalone workstream.** It got dissolved into "System deliverables" — closer to "platform underpinnings" framing. The funding-cash-out move now rides on whatever System Deliverables get prioritized rather than a separately-named ask.

## Workstreams (4, not 5 — Foundation absorbed into Goals)

### 1. Build Agent Expansion
- **Goal:** expand the current build stack (mostly Java / Optimus / Unity) to broader use cases. Andrew's direction: **"go wild."**
- **Driver:** **JJ Hu** (already heavy lifting; will continue as main driver)
- **Support needed:** Blending team
- **Note:** JJ brings clear perspectives — has been thinking deeply about this problem

### 2. Simulate Agent
- **Goal:** Simulate (Shopify SimGym style — Persona + Intent)
- **Driver:** **Bella Huang**
  - Already started building scaffold in codebase
  - Iterating on VLM connection → initial simulate agents
  - Strong ATG trust (extensive collaboration); also driving RecGPT with ATG
- **Foundational tie-in:** Pinkerton (James-led agentic feed debugging) framed as upstream foundation
- **Open architectural fork (deferred for serious discussion):**
  - **Option 1:** Merge Pinkerton under Reflex — requires Dimitra onboard
  - **Option 2:** Agent-to-Agent delegation from Reflex → Pinkerton
  - **James's commitment (per 5/27 strategy):** option (2). Federated, not subsumed. Dimitra co-lead standing preserved; substrate-with-multiple-consumers pattern intact.

### 3. Modeling Agent (NEW — wasn't in pre-convo roadmap)
- **Goal:** kick off build agents on L2 / L1 / L0 models — PyTorch code + configs + MLEnv
- **Driver:** **Matthew Lawhon** (with Infra folks)
- **Status:** MLEnv integration ~2 weeks out
- **Loop-in candidates:** CG modeling folks working on LWS and CLR
- **For James:** this absorbs the "model-based integration" workstream from the original sketch; now has a named driver and a clear technical anchor (MLEnv).

### 4. Agent-to-Agent
- **Goal:** define how Reflex works with the rest of the company; how other agent systems connect with Reflex
- **Driver:** **Dafang He** — already in discussion with **Keqiang Li**
- **System Design ownership:** Dafang will drive a Reflex System Design (consensus on this)
- **Other agentic systems to connect with:**
  - **Dash:** Manu Sharma, Rahul Chaudhary
  - **ForgeDev:** Abhishek Tayal, David Sun
  - **Evaluation:** Darren Reger's team + Anna Kiyantseva
  - **Observability** (placeholder owner)
  - **Reinforcement Learning** (future — Dafang excited about this direction)

## What James needs to think about / track

- **The TL handoff to Dafang is the structural move.** James's pre-OOO sequencing now centers on setting Dafang up to run, not on James running.
- **Foundation-layer funding ask reshape.** The original frame (un-staffed 5th workstream → Andrew's "funded for my team" cash-out) didn't survive. Funding ask now needs to route through "System Deliverables" prioritization OR through staffing the 4 named workstreams (especially Modeling Agent, which is closest to ML-Infra and where James's team has natural pull). Worth thinking about with Dylan before OOO.
- **Pinkerton federation question is now on the explicit Reflex agenda.** James's committed answer (option 2, A2A delegation) needs to be propagated when "serious discussion" opens — likely via Tim + Dafang as forwarding agents, not directly to Andrew. Dimitra co-lead conversation also needs prep before the merge-vs-A2A debate opens.
- **New names entering James's stakeholder map** (skeletons not yet created): Keqiang Li, Manu Sharma, Rahul Chaudhary, Abhishek Tayal, Bob D (people-side, see coaching log).
- **Matthew Lawhon scope upgrade.** Previously known as KDD-paper co-author; now Modeling Agent driver for Reflex. Re-read his stakeholder posture once active.

## How this changes the original Tim roadmap doc

The pre-convo roadmap (`tim_friday_5-29_roadmap.md`) is now superseded for structure but still valid as the *opening artifact* — it shaped the convo and Tim ran with it. Treat as historical record of the framing; this debrief is the operating-state-of-the-world.

Key delta from pre-convo to post-convo:
- ✅ 4 workstreams confirmed (Build / Simulate / Modeling / A2A) — close to original sketch
- ❌ Foundation layer didn't land as separate workstream — absorbed into Goal-setting axes
- ✅ Capability-led Pinkerton framing held — option 2 (A2A delegation) is the path forward
- ✅ Drivers identified for each stream (JJ / Bella / Matt / Dafang) — much more concrete than pre-convo

## Open / next

- Where does the Foundation-layer ask actually live now? — needs a one-liner before next Andrew touchpoint
- Dimitra prep before merge-vs-A2A debate opens
- New stakeholder skeletons (Keqiang, Manu, Rahul C, Abhishek, Matthew Lawhon scope upgrade)
- Dafang §28 stakeholder upgrade (Reflex TL is a major scope change vs current Search CLR framing)
- Dylan funding-ask circle-back (5/27 carry-over) — still open, now with reshape signal
