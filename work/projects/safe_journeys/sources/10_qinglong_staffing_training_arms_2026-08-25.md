# Source 10 — Qinglong DM, 8/24–8/25: doc-edit ask, CQ staffing on the merged workstream, the five training-time arms, "start lightweight"

> **Source of record.** Slack DM screenshots from James, Tue 2026-08-25 evening. Two exchanges: Mon 8/24 (James's ask that Qinglong write directly into the doc + address Sari Wang's and Michael's feedback) and Tue 8/25 (James's three questions; Qinglong's answers).

## Mon 8/24

**James, 11:39 AM:**
> Hi Qinglong! Thanks again for all the wonderful comments on the Quality levers doc and I look forward to our team's collaborations.
> I'm wondering if you can add to the doc more directly in the text, e.g. starting from the few places I tagged you.
> And also addressing the feedback from @Sari Wang and @Michael Weissinger where possible.
> I'll also do a pass throughout the rest of today as well 🙂

**Qinglong, 11:01 PM:**
> Sure, just addressed some comments on the doc. I will also spend some time tomorrow adding new ideas/suggestions directly into the doc. Thank you!

## Tue 8/25

**James, 10:59 AM:**
> Thank you Qinglong! Some quick questions:
> 1. How many engineers on your team are you expecting to be involved in this workstream (GenAI merged with Safe Journeys)?
> 2. Serving-side interventions: do we need to discuss the specifics here more between You Me @Dafang He @Dhruvil Deven Badani?
> 3. Training-side interventions: I think we need more clarity on 1) which ones are worth trying, 2) which ones are prioritized, and 3) who is working on what?

**Qinglong, 12:32 PM:**
> | How many engineers on your team …
> 2 TLs (@Yilei Wu and @Jianing Sun) and 1 full-time ICs @Rohit Pillai. I might be able to find more engineering resource from CQ side if it's necessary but it also depends on the plan.
> | Serving-side interventions …
> sounds good to me
> | Training-side interventions …
> right, I feel we might have to test different arms (1) re-weighting (2) margin loss (3) density head (4) in-batch negative (5) user sequence
> | 1) which ones are worth trying, 2) which ones are prioritized, and 3) who is working on what
> +1 those will also require discussions from you, me and @Dhruvil Deven Badani, right? (edited)
> I think we should start with some lightweight options? things like density head sounds great but might take more efforts to implement and tune? I'm not an expert so open to alternative suggestions

## Leo read (8/25 PM)

1. **CQ's commitment on the merged workstream is now a number: 2 TLs (Yilei Wu, Jianing Sun) + 1 FT IC (Rohit Pillai), more "depends on the plan."** That last clause makes the joint doc the resourcing instrument — a plan with named CQ deliverables and dates is how James gets the "more." Jianing on the doc since 8/20; Yilei Wu and Rohit Pillai are new names to file.
2. **"GenAI merged with Safe Journeys" — James's phrase, unchallenged.** The merged workstream is now named in the CQ channel; matches Michael's sequencing (source 08) and D12.
3. **The five training-time arms, in Qinglong's list:** (1) re-weighting (2) margin loss (3) density head (4) in-batch negative (5) user sequence = the doc's §5 (head + reweighting baseline) plus Dhruvil's §7 menu. He is asking for exactly the prioritization the doc's rubric exists to produce — and the three-way (James/Qinglong/Dhruvil) is agreed. **Carry into that discussion:** arm (5) has already been run — GenAI v3 in the user tower via sequence embeddings was negative offline (Lily's one-pager, source 09) — so it needs a new hypothesis before it's re-run; arm (1) is the doc's stated cheap baseline; arm (2) carries Akshay's notifications evidence.
4. **"Start with lightweight options; the density head might take more effort"** — a gentle deprioritization of D3's centerpiece. Not a fight to have: the doc already scopes the head as a **gated bet with a kill criterion, not a launch dependency**, so "lightweight first, head as the Phase-2 bet" is the doc's own sequencing. Accept in those words; keep the head's *why* (objective change, not feature add — the v3-feature-flat history) on record so it doesn't get dropped as "too hard."
5. **Serving-side specifics → James / Qinglong / Dafang / Dhruvil** — agreed. With Dafang L3-first for a few weeks (Dylan, 8/25), JJ is the practical HF L1-utility voice in that room.
6. **Sari Wang commented on the doc** (8/24) — DS on the GenAI ablation consolidation (source 09, Lily's one-pager). Her comments are not yet filed here; neither are Michael's.
