# Will Larson — The engineering mindset | Will Larson (Carta, Stripe, Uber, Calm, Digg)
*Theme: decision-making | Extracted: 2026-04-04*

## Strategy as diagnosis + guiding policies; most decisions won't matter in 6 months

Lenny (00:20:31):
Well, maybe what might be helpful is what are some other examples of engineering strategies that you've seen just to give people even more just like, "Oh yeah, maybe this should be part of our strategy."

Will Larson (00:20:31):
So first, what is a definition of strategy? And the best one I've ever seen is from Richard Rumelt. He wrote Good Strategy, Bad Strategy.

Richard Rumelt, definition of strategy is basically three components. There's a diagnosis. What is the current status quo? What are the things that are real today? There are guiding policies which are basically based on the diagnoses, how do you want to address them? And there's actions. And actions are how are we going to implement these guiding policies. He talks a lot about actions because concerned about this idea of inert strategy where you have like, "We're going to deprecate our old product features we don't use, but no one deprecates any of them."

So he's really concerned about this non implementation kind of useless strategy that doesn't do anything. On engineering, I'm a little bit less worried about that. I think strategy is more interesting on engineering in terms of clarifying how we make future decisions. And so what are a few examples of that? At Uber, we only used our own data centers. We didn't use the cloud. And this was annoying because we had to indent everything ourselves or run copies of everything ourselves.

But it also meant that we were able to spin up in China in literally three months... And Uber wasn't in China for very long, so in some ways you're like, we did all that just a leave? But they left with a nice stake of Didi Kuaidi and not a bad outcome overall. But I think that strategy, we run everything in data centers. We don't use the cloud, meant we were able to move in and out of different geopolitical constraints and companies that relied on cloud presence simply can't.

Another good example at Stripe was this idea of we run a Ruby monolith and that's what we did... that policy really focused the engineers on building innovative features for our users rather than building different tooling to support different programming languages. And so in both cases, both the Uber policy around running our own data centers and the Stripe policy around Ruby monoliths, a lot of engineers hated these.

But the goal of good strategy is not to appease everyone. The goal of good strategy is to dictate how we invest the limited capacities we have or the limited capabilities we have into the problems we care about. And I think both of them were really effective towards that end.

Lenny (00:24:17):
A common theme across all these examples is essentially constraint, deciding we will constrain our options to move faster and focus on the things that really matter.

Will Larson (00:24:28):
In solving the constraints is to me, I think the most interesting thing that strategy really does, and I think when we talk about bad strategy usually is because the diagnosis is bad and it's usually because people are exerting what they want to be true on constraints where it's like, "Hey, we can do all of these projects at once." And often that's just not true, but it's hard to convince people that when they're the CEO or they are really committed to believing it, but almost all bad strategies basically come down from a willful disbelief of what an accurate diagnosis is, which means then your guiding policies are kind of incoherent to begin with.

---

## Will anyone remember this decision in 6 months?

Lenny (00:13:40):
Do you have a favorite life motto that you often come back to share with friends, find useful either in work or in life?

Will Larson (01:13:40):
No mottos, but I can think of two things I thought about a lot. At Uber is something I talk to people a lot because it was a challenging time for much of it. It was there's no way around, just through. And that was like, "Hey, we're not going to dodge around this. We're going to gut through it and we're going to get to the other side and then we're going to be there." What I think about a lot more now is, will anyone remember what we decided in six months? Because I think people stress out about a lot of decisions, but I increasingly believe most decisions people stress out about just aren't that important.

So I'm like, "Will anyone care in six months what we did here?" And the answer is no. Just do something reasonable and let's move on to the next more important thing.

---
