# Will Larson — The engineering mindset | Will Larson (Carta, Stripe, Uber, Calm, Digg)
*Theme: org-strategy-leverage | Extracted: 2026-04-04*

## Engineering strategy: write it down, boring is good

Lenny (00:16:52):
Another thing that I know that you are very passionate about and spend a lot of time thinking about is engineering strategy. I think you have this kind of feeling like engineers don't think enough about the end strategy. Every other function has a strategy and engineers often don't. Talk about what you find there and what your advice is around that.

Will Larson (00:16:52):
First, I start to question whether any function has a strategy at most companies. My general experience is that there's very rarely a written strategy for any company. Sometimes it's a value statement. It's like we build the highest quality products and you're like, "Good. Okay. What do I do with that?" You're like, "Build a high quality product." You're like, "Okay. I don't don't know what that means."

Engineering often has this problem where I think people will make comments in their culture amp or their quarterly surveys or whatever. It's like, "Hey, the strategy is not clear or where's the engineering strategy?" And the biggest thing I tell people when they complain and then engineers complain about the product strategy. The PMs don't have any strategy or the business has no strategy. And the reality is product eng and business always have a strategy. It's just often not written down.

And so the first thing I want to do is I push people not to get caught up on the fact that there's no template out there, which is product strategy that someone has forked and filled in. It doesn't mean you don't have a strategy. You do have a strategy. It's maybe a little bit hard to articulate and maybe it's applied inconsistently across different layers of the product reporting chain because it's not written down. But it's never true that there's no product strategy. There's always a product strategy. Sometimes it's bad, but there's always one. And true for engineering as well. There's always an engineering strategy. Just sometimes it's bad.

The first rule of strategy is that if you write it down, then you can improve it. If it's not written down, it's hard to say if this PM is just not a good PM or if they're trying to apply the strategy that they've misunderstood or if they actually are correctly applying the strategy from the head of product that's just not appropriate to the problems they're working on, how do you debug any of that?

If you have a written document, even if it's not a super compelling strategy, at least you can start debugging. It's like, "Hey, the head of product should improve the clarity of this document. Hey, this DM actually isn't applying it correctly. Hey, the strategy actually isn't appropriate for this one business unit where it makes sense for the others."

So that's the first thing I think about. But the second big theme on strategy I think about is that often good strategy is so boring. It's hard to talk about. For example, on the engineering side of thing, a common strategy that's really good but very boring is we only use the tools we have today. So a lot of times you'll get engineers that want to introduce new programming languages, new databases, new cloud providers. And a really good strategy for almost all companies is like we just use the standard kit we already have today.

And at Carta, when I joined one of the engineers, Eric Vogel wrote the standard kit and that is our strategy of the tools we use. And you know what? Some people are really frustrated by that and I feel for them. It feels like they're losing control, but the power of these boring strategies is that it focuses people's energy on the problems that we value as a company. And so it is painful coming into alignment if you're kind of slightly misaligned over time, but boring strategies that tell you what actually matters and aligns you with what the company actually caress about are really good for you even if they're a little bit annoying at a time.

---

## Shared EM/PM performance ratings to align incentives

Lenny (00:44:05):
On the incentives piece, is there anything you've seen work to fix that problem? Because if PM performance reviews are based on impact engineering, performance reviews are based on interesting projects or uptime, do you just work to change those ladder definitions? What actually can help that situation?

Will Larson (00:44:05):
So my biggest thing has been trying to force this idea that EM/PM pairs are peers and they generally have the same performance rating. And there's exceptions here. It could be the EM is clearly not performing and then it's not the PM's fault if the EM is can't show up to work. The team doesn't respect them. Sometimes there's clear non-performance, but generally hard situations are not situations where one person is obviously terrible. Those are easy to diagnose, those are the easy ones. But in cases where there's two folks who seem to be pretty good, but just the overall execution is not working out, I think this idea that same perf rating for both drives a level of one pain, but the right perspective.

Also, something that I think Carta has experimented a little bit with over time. Henry, our CEO has a blog post about trifectas in doing that, but not just for EM and for PM, but also for that business leadership as well where you all get graded the same score based on your ability to evaluate and solve for the entire set of constraints, not just your functional constraints.

Lenny (00:45:20):
Wow. That's so interesting. So your recommendation, something you're doing, it sounds like is the engineer manager and the PM get the same performance review rating? And so they're discussed in the same meeting.

Will Larson (00:45:33):
Our chief product officer, Vrushali and I spend a fair amount of time calibrating together and making sure... Again, there's cases where there's an exception because there's clear issues happening for someone. But on average that is what's happening. And I think people know that's what's happening because we told them that. And I think that's pretty powerful.

Lenny (00:45:55):
That is so interesting. I've never heard of that approach. That is definitely solving that problem of EM/PM or...

Will Larson (00:46:01):
Yeah, the incentives are shared now, which isn't perfect. It's still hard to balance them. They can still make the wrong trade-offs, but at least they understand the incentives are shared, which I think is a pretty powerful idea.

---

## Measuring engineering productivity: align to business outcomes

Lenny (00:48:44):
An adjacent topic that I wanted to spend some time on is measuring engineering velocity productivity. I think it's probably one of the most common and also maybe the most annoying questions eng leaders get is just how do I know if my engineers are moving as quickly as they can? How do we help them move faster? What advice do you give to eng leaders for eng teams just for how to measure productivity well?

Will Larson (00:48:44):
This is a question that's coming up even more in a moment when we're reducing a lot of the size of teams from the industry when the venture capitalists that are on the board for these venture-backed companies are pushing on the efficiency of engineering. Engineers are trying to figure out how do we represent this? How do we prove that we're appropriately productive for the amount of headcount and funding that we have as an organization?

And man, that's hard. So the first way that people focus on trying to answer these questions is just benchmarking by the amount of funding that you have. And that's pretty straightforward to do is a mechanical exercise. You get a data set from your venture capital funds or whatnot, and you figure out, "Okay. How much should we be spending in R&D? How much should we be spending in engineering? How much should we be sending on infrastructure engineering in R&D?" And you can benchmark this all out and figure out what the correct numbers are there.

The problem is this is a very mechanical and not very insightful, driven way. It'll get you a defensible answer. It's like the old, no one gets fired for buying IBM, which definitely hasn't been true in my career ever. But this idea that if you just have the right benchmarks, DCs won't judge you for spending too much in engineering, but this doesn't actually help you get to the right place. It just helps you get your board to be less angry at you, which is useful because it's hard to do good work when your board is angry at you.

But it's not useful in the sense that it doesn't actually help you run your organization effectively. So then there's the much harder mediator problem of how do you actually know if your R&D team or engineering team is effective? What I find is a couple of things. First, if you're a good leader and you talk to engineers, they will tell you... The engineers know if their teams are effective or not. And if they're not, they'll also tell you why not. And their diagnosis can be wrong, but there's a crumb you can start picking up and you can trace the crumbs to figure out what's wrong.

Often you'll have more experience to analyze the complaints to figure out what kind of the contributing causes are to them. But yeah, if you just go talk to the team on an ongoing basis, you'll know if they're effective or not and you can go work to solve those specific problems.

What I've tried to do is basically two things. One, aligning engineering evaluation to the business and product goals. So I want us to be wholly accountable with the product goals. We did a good job products like screwing up over there. Obviously, a lot of companies find comfort in doing that, but really we're here to support the product, to support our customers in doing something interesting. We're not here to build novel systems unless it supports the customer and the product.

So first try to align heavily there. Second, I think just showing the roadmap of the valuable things we've done in the last six months is really powerful. I think sometimes people are like, "I don't have anything to put there." And you're like, "Yeah, that's a real issue." Or if you have the ton of stuff to put there, that's great. I really find that if you just commit, show the number of meaningful, meaty things that have impact that you're doing and you can explain the impact, people will step back and give you space. If you can't populate that list, people will have concerns and rightly so, they should be concerned about that.

---
