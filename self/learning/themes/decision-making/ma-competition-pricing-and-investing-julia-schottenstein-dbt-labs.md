# Julia Schottenstein — M&A, competition, pricing, and investing | Julia Schottenstein (dbt Labs)
*Theme: decision-making | Extracted: 2026-04-04*

## Open source vs. proprietary: what to charge for

Lenny (00:29:50): I want to come back to your chatting about open source versus not open source. So some part of dbt was is open source and some isn't. I'm curious how the team decides what is open source and what should be open source, what isn't open source and what to charge for?

Julia Schottenstein (00:29:50): We think about dbt open source. It's really the guts of the data transformation. It's where you describe your business logic. And then on the cloud side we build proprietary software that supercharges the development life cycle and the productionization of dbt at scale. So what we think about as leaving for our cloud offering is we deal with state, so stateful interactions and also any cross team or structural collaboration. We want to reserve that for our proprietary offering. And I think it's really important to have that distinction of what do you believe should be open source or what is the open standard that really matters? And ecosystem to us is really important. So it's important that that remains open source, but then we want to supercharge that experience with an open core model and build proprietary software that makes people much more successful at using dbt.

---

## Ship early: worse is better, tech debt is a champagne problem

Lenny (00:52:02): Is there any other frameworks or just general processes that you found to be really useful in building awesome product running teams?

Julia Schottenstein (00:52:10): I'm not a big framework person, but there's two sayings that I find myself repeating or I either to myself or to others. And it's worse is better and tech debt is a champagne problem. And what do I mean by that? It's really to help me combat this perfectionism because perfect doesn't exist and you should instead go with good enough because when you ship, that's the moment when you get to learn a lot from your users and you just can't anticipate it. You try very hard to understand exactly how people will use the product and get all the edges ironed out. But you can't until you ship. And I'll share an example. So my team helps support the dbt cloud scheduler and the initial version of the dbt cloud scheduler was pretty naive. We were a little embarrassed by it.

It was a big old for loop over a big old jobs table. So we would look like is it time for this job to run? Okay. Yes, run this job. Okay. It's not time for this job to run next, continue on. Is it time? Yes, run this job. And it would just loop over and it's extremely naive and very simple, but it got the job done. And I try to remind the engineers, we would be so lucky to have tech debt because that means people are using the product. And now we've had to rebuild our scheduler several times over because we do have meaningful scale. We have 8,000 companies using our scheduler. We have to manage 10 million runs per month. But what we didn't need at launch was a distributed scheduler with coworkers and RabbitMQ. We just didn't need it because we had no users. So these two sayings that worse is better and tech debt is a champagne problem, just really reminds people like, let's ship, let's get it out into the user's hands and then we'll learn and iterate and it'll be a better experience for them.

---
