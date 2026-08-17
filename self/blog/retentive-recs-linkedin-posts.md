# Retentive Recs — LinkedIn amplification drafts

Source post: *Pinner Progression: Better Use-Case Representation Driving Weekly Active User Growth at Pinterest* (Pinterest Engineering, Medium) — Part 1 of 2.
Link: https://medium.com/pinterest-engineering/pinner-progression-better-use-case-representation-driving-weekly-active-user-growth-at-pinterest-bd2131ab238a

Register: amplify-the-team (warm, credit-forward, substance-first). Not an exec altitude memo.
Accuracy guardrail: Part 1 publishes NO quantified WAU/retention numbers — kept qualitative. Add a cleared number if you have one (see how-to).

---

## Option 1 — FINAL (humanized 2026-08-16; adds village/XFN, hardest-problem, hiring close)

"A user can save ten sourdough recipes today and churn next month anyway."

That line is from a post my team just published, and it's the whole problem in one sentence. Recommender systems are very good at predicting your next click. Whether you'll still be around next month is a different question, and most of the field just optimizes engagement and hopes retention follows. It usually doesn't. This is genuinely one of the hardest open problems in recommendations, and I'm proud the team went straight at it.

The idea: stop treating a user as a pile of recent clicks. Model the use-cases underneath instead. Furnishing a first apartment and planning a wedding are different jobs, each with its own lifecycle, so we built persistent representations of them (User Interest Clusters) and wired them into every layer of the stack: retrieval, utility scoring, ranking, diversity.

Here's the thing about a change that deep: nobody ships it alone. Four layers, owned by different teams. Personalization, User Understanding, and Data Science had to land their pieces in sync, from the embedding space all the way to the feed. It takes a village, and I got to watch this one pull it off. [tag: Yuke Yan, Chuxi Wang, Simin Li, Sufyan Suliman, Armando Ordorica + others]

This is Part 1 of 2. Part 2 tackles the question I find hardest: how do you recommend a use-case someone hasn't shown you yet?

Link in the comments. Oh, and we're hiring! If this is the kind of problem you want to lose sleep over, my DMs are open.

*(Note: "genuinely" conflicts with James's style guide — swap for "easily" if preferred. Original pre-humanizer Option 1 retired; Options 2–3 below are still pre-humanizer drafts.)*

---

## Option 2 — Punchy / shortest (humanized 2026-08-16)

"A user can save ten sourdough recipes today and churn next month anyway."

That one line reframed how my team thinks about recommendations. Engagement is not retention, and retention is the harder problem by a mile. Most of the field ignores it.

So we stopped modeling people as a stream of recent clicks and started modeling the use-cases underneath: furnishing an apartment, planning a wedding. Each one now has its own lifecycle in the system, and that idea runs through retrieval, ranking, and diversity. The write-up just went live on Pinterest Engineering, and it took Personalization, User Understanding, and Data Science all shipping in sync to pull off. It takes a village.

Part 1 of 2. Link in the comments. And yes, we're hiring.

---

## Option 3 — First-person leader angle (humanized 2026-08-16)

My team has been chasing a question that sounds simple and isn't: how do you recommend things that bring someone back next month, not just get a click today?

Most recommender work optimizes engagement and assumes retention follows. It mostly doesn't, which is what makes this one of the hardest open problems in the field. Our answer just went live on Pinterest Engineering: model each user as a set of evolving use-cases instead of a stream of actions. A new interest gets curiosity and exploration. A mature one gets depth. The feed starts growing with the person.

I want to be clear about what shipping this took. The representation cuts through retrieval, utility scoring, ranking, and diversity, and those layers are owned by different teams. Personalization, User Understanding, and Data Science all had to move together, and they did. It takes a village to change something this deep in the stack. My job was mostly to hold the map. [tag: Yuke Yan, Chuxi Wang, Simin Li, Sufyan Suliman, Armando Ordorica + others]

This is Part 1 of 2. Part 2 gets into the question I find hardest: predicting the use-cases someone hasn't shown us yet.

Link in the comments. And yes, we're hiring. If you want to work on retention instead of clickbait, my DMs are open.

---

## How to post (LinkedIn mechanics)

1. **Hook lives above the fold.** Only the first ~2–3 lines show before "…see more." All three options front-load the hook — don't add a preamble above them.
2. **Link in the first comment, not the body.** LinkedIn suppresses reach on posts with external links. Post with "Link below 👇", then drop the Medium URL as your own first comment. (Or accept the reach hit and inline it — your call.)
3. **@-tag the real contributors.** Tagging 4–6 named authors (Yuke Yan, Chuxi Wang, Simin Li, Sufyan Suliman, Armando Ordorica, etc.) pulls their networks in and reads as generous leadership. Swap "the Personalization, User Understanding, and Data Science teams" for @-mentions where you can.
4. **Add a real number if cleared.** The post is qualitative; a single public retention/WAU figure ("+X% 4-week retention on treated cohorts") would be the strongest line in any of these. Only if it's cleared for public.
5. **Timing:** Tue–Thu, ~8–10am PT lands best for a technical audience.
6. **Reply to load-bearing comments in the first hour** — early engagement drives distribution.
