# Matthew Lawhon — Promo Assessment (IC15 → IC16 MLE), July 2026

> Final draft for Workday, 2026-07-09. Form: promotion feedback. Readiness radio: **"Ready now: Consistently operates at the next level across the areas I've observed."**
>
> Sources: James brain dump; prior collaboration assessment letter by James and Dhruvil (transcribed verbatim in the appendix, left untouched); `work/projects/upp/cfm_technical.md`. The CFM ~1% repin early signal is deliberately omitted (marked "snapshot, not verdict" in notes); add a hardened number to the second paragraph of Q1 if one exists.
> Spelling: **Lawhon** (James's dump had "Lawhorn"; repo confirms Lawhon).
>
> 2026-07-10: added the "impact and quality" form question. Per James's direction it avoids CFM (already the Q1 headline) and anchors on UPP: Matthew as ranking TL thinking through the platform's practical concerns. Evidence from `upp_retrieval_em.md` (alignment thread, verbatim quote) and `cross_org_operational_model/` (cross area calibration POC).

---

**Q: Based on your observations, has the nominee demonstrated consistent capability at the next level?**

I strongly support Matthew's promotion to IC16, and I say that as a peer manager whose teams share as much surface with him as anyone. Matthew acts as a primary technical driver across our shared P0 initiatives (UPP, Foundation Models, GPU Serving, L1 Calibration) and works with my Candidate Generation team on retrieval problems continuously.

The clearest IC16 evidence is CFM. Since the last round of feedback, Matthew championed the Conditional Foundation Model and saw it through to fruition. It is already landing strong impact in Homefeed, Notifications, and P2P, and it is on track for much broader reach across Pinterest through the UPP platformization effort. How quickly he made all of this happen, while staying hands on, is the IC16 role summary almost word for word: "a leader who drives the technical solutions and strategic objectives for one or more teams," whose impact "is felt beyond their primary team."

Just as important is how his influence has matured. Matthew has been extremely collaborative with my retrieval team, on lightweight scoring, on advocating continued investment in foundation models and model scaling, and on helping us balance how much scoring belongs in the L1 layer versus L2. He is articulate, and where he once pushed hard on every idea, he now operates with what I would call "influence through restraint": here is my suggestion, take it or leave it, reserving the hard push for the points that are truly critical. That is a visible improvement since prior feedback, and it aligns with the IC16 expectation to influence other teams' roadmaps and win support rather than force it. I expect it to carry his influence a long way across Pinterest.

**Q: How have they demonstrated the impact and quality of their work?**

CFM is the headline above, so here I will point somewhere else: UPP, the cross org effort to unify Pinterest's ranking and retrieval stacks on shared pretrained models. A platform bet like that lives or dies on practical judgment, on model maintenance burden, serving cost, calibration across surfaces, and who owns which seam. As the technical lead on the ranking side, Matthew is consistently the person thinking those concerns through before they become problems. When the cross org alignment discussion was drifting toward a proliferation of bespoke base models, he staked out the position that "there is only one base model per category (ranking or retrieval) and the pretraining is sufficiently general that no other base models are required in the category." That one position carried the maintenance, velocity, and ownership implications of the entire design space, and it became an anchor the broader group aligned around. When terminology across orgs got muddled, he was the one clarifying the technical distinctions between the model layers so teams stopped talking past each other.

The quality of his work shows in how much other teams lean on his judgment. In the UPP operational model, Matthew is the named point of contact for cross area calibration: teams across surfaces are directed to confirm direction with him before making changes at that seam. That kind of trust is earned through work products, and it matches the IC16 Impact expectation that "individual work products (documents, code, analysis) serve as examples for simplicity, quality and impact." Between the platform judgment on UPP and his delivery across our shared P0s in GPU serving and L1 calibration, he has "a track record of successfully guiding, leading and shipping projects that have substantial impact to team level OKRs, or other metrics critical to the organization" many times over.

**Q: Looking at the next level's REG, where does the nominee need to develop to effectively operate at the next level?**

Matthew's development area is less a missing capability than a mode to scale. His default is "high context, high autonomy," which works extremely well with senior peers; with newer engineers it can read as a lack of support until expectations get calibrated. Dhruvil and I have dug into this together before, and the misses were familiarity gaps rather than trust issues. When a gap was surfaced, Matthew adapted quickly and willingly every time, despite a heavy UPP workload. At IC16 the expectation shifts from adapting when asked to setting the contract up front: making his working style legible to newer collaborators from day one, and developing senior engineers who can in turn develop others. Doing that deliberately would remove the last friction from his influence across teams and let the restraint he has built compound into pull across the whole org.

**Q: Based on your experience working with the employee, how would you assess their readiness for the next level?**

☑ Ready now: Consistently operates at the next level across the areas I've observed

---

## Appendix — prior letter (James + Dhruvil, verbatim transcription from screenshot; hyphenation left as written)

Dhruvil and I have reviewed the recent collaboration signals between Matthew and members of Candidate Generation (CG) team. Our assessment is that recent friction points are not structural trust issues, but rather "familiarity gaps" from onboarding new/junior engineers to work with Matt. Matt was also disproportionately helping ramp-up the new engineers on the CG team due to other CG TLs being stretched, so he actually put in a lot of additional effort to make the collaborations smooth and successful. Once expectations are calibrated, Matthew has consistently shown up as a willing partner. Finally, upon deeper discussions with these new/junior team members, they tell us that when Matt is available, he is extremely helpful and patient, including proactive follow ups to check in on status and offer support.

Matthew acts as a primary technical driver for our shared P0 initiatives (UPP, Foundation Models, GPU Serving, L1 Calibration). He brings very deep expertise and direct experience on these projects that are critical to the multiple wins so far and crucial to efforts such as UPP and FM going forward. His default operating mode is "high-context, high-autonomy," which is effective for his senior peers in Ranking. The perceived friction arises almost exclusively when junior engineers (who are new to the domain) interact with this high-velocity style. They often mistake his speed and assumption of competence for a lack of support. Once expectations are calibrated, Matthew has consistently shown up as a willing partner.

One instance is regarding the LWS rollout serves as the primary example of this "Familiarity Gap". Dhruvil and I spent some time digging into this issue, and found that Yali (being newer to the stack) required explicit, step-by-step task tracking to feel secure. Matthew (focused on UPP delivery) operated with the assumption of shared implicit context. We also clarified that this was actually a handoff ambiguity from Piyush to Yali, which left Matthew and Yali with different "contracts" for the project. And Yali was really just requesting for more of Matt's time on this project. It was a process miss, not a person miss. As soon as the gap was highlighted, Matthew agreed to generate the specific task lists Yali needed, despite his heavy UPP workload. A "low-trust" engineer would have pushed back; Matthew adapted.

Another instance is regarding an accidental experiment started after code freeze. Here's what happened in Yidi Wang's own words:

"I want to emphasize that Matt was a huge help throughout the LWS experiment. The timeline was very tight, and he was hands-on and proactive in pushing the process forward. The issue was a misunderstanding regarding Code Freeze. As a new hire, it was my first time experiencing it, and I didn't fully grasp how strict the constraints were. So, when Matt mentioned that a 'slight delay' was okay, I misinterpreted that to mean we could continue to ramp up the experiment in a small way after Code Freeze began.

So, when the experiment ran into an issue and I was pinged by the sms on-call team telling me we shouldn't be ramping during Code Freeze, my immediate reaction was shock, and honestly, I was quite scared. In my mind, I thought I was performing an approved action, and suddenly realizing I had violated a major rule was jarring. As someone new, I was very worried that I had caused a serious problem.

In that moment of panic, I reached out to Matt and didn't get an immediate reply, which did add to my stress. However, I quickly realized afterward that it was already well outside of business hours for him in New York, and it was completely normal for him to be AFK.

Matt did follow up on the experiment afterward. And more importantly, as I've become more familiar with our workflows, I can now look back at the situation with more perspective. I understand now that it wasn't the severe incident that I imagined at the time. He, like me, just wanted to get the experiment live as quickly as possible and he was acting with the goal of pushing the project forward, not to offload responsibility."

To accelerate the "Familiarity Curve" for our junior staff, Dhruvil and I are working a "Role Clarity in Collaborations" framework to explicitly define engagement models between cross team engineers who may have different expectations. This will replace the need for "trial-and-error" relationship building with clear operating standards, preventing these minor stylistic mismatches from being interpreted as performance issues.
