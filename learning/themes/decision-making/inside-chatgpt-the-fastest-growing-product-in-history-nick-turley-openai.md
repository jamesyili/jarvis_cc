# Nick Turley — Inside ChatGPT: The fastest growing product in history
*Theme: decision-making | Extracted: 2026-04-05*

## Maximally accelerated principle as forcing function

Lenny Rachitsky (00:23:12):
Okay. So, along these same lines, I asked Kevin Weil, your CPO, what to ask you, and he said to ask you about this principle of, "Is it maximally accelerated?" Talk about that.

Nick Turley (00:23:22):
That's funny, we have a Slack emoji, apparently, for this now because I used to say that. Now, I try to paraphrase. Sometimes, I just really want to jump to the punchline of like, "Okay, why can't we do this now?" or, "Why can't we do it tomorrow?" And I think that it's a good way to cut through a huge number of blockers with the team and just instill... especially if you come from a larger company. At some point, we started hiring people from larger tech companies. I think they're used to, "Let's check in on this in a week," or, "Let's circle back next quarter to see if we can go on the plan." And I just, as a thought exercise, always like people asking, "Okay, if this was the most important thing and you wanted to truly maximally accelerate it, what would you do?" That doesn't mean that you go do that, but it's really a good forcing function for understanding what's critical path versus what can happen later. And I've just always felt like execution is incredibly important. These ideas, they're everywhere. Everyone's talking about a personal AI, you might've seen news on that and I really think that execution is one of the most important things in the space and this is a tool. So, it's funny that that became a meme. It's like a little pink Slack emoji that people just put on whatever they're trying to force the question.

Lenny Rachitsky (00:24:53):
Okay. And so, the kind of the culture there is when someone is working on something, the push is, is this maximally accelerated? Is there a way we can do this faster? Is there anything we can unblock?

Nick Turley (00:25:02):
Yeah. And we use that sparingly, right? Because it needs to be appropriate to the context. There's some things where you don't want to accelerate as quickly as possible because you kind of want process. And we're very, very deliberate on that where your process is a tool. And one of the areas where we have an immense amount of process is safety. Because A, the stakes are already really high, especially with these models, GPT-5 which is a frontier in so many different ways. But B, if you believe in the exponential, which I do and most people who work on this stuff do, you have to play practice for a time where you really, really need the process for sure, sure, sure. And that's why I think it's been really important to separate out the product development velocity, which has to be super high from, for things like frontier models, there actually needs to be a rigorous process where you red team, you work on the system card, you get external input, and then you put things out with confidence that it's gone through the right safeguards.

---

## Sycophancy incident: incentives shape model behavior, run toward hard use cases

Lenny Rachitsky (00:56:08):
Along those lines, there was this whole launch of the very sycophantic version of ChatGPT where it was just, "You are the best person in the world. Everything you tell me is amazingly correct." Are you able to tell us just what happened there?

Nick Turley (00:56:08):
Yeah, we have all kinds of collateral online because we really felt like we should over-communicate on how we discovered it, what we did about it, et cetera. So I encourage people to check that out. We have a whole retro on that model release.

But basically what happened is that we pushed out an update that made the model more likely to tell you things that sound good in the moment, "You're totally right. You should break up with your boyfriend" or something like that. That's just really dangerous. We took it more seriously than you even might expect because again, at current technology levels, you can kind of laugh about it. Maybe it's like, "Ha-ha. This thing's always complimenting me. I thought it was just me. I saw all those comments online." But it actually is really important to make sure that these models are optimized for the right things.

And we have an immense, I think, luxury to have a mission that affords us to really help people, a business model that does not incentivize maximizing engagement or time spent in the product, right? So it's really important to us that you feel like this product is helping you with your goals, whether not that's your current goals or even your long-term goals.

And oftentimes being extremely complimentary with the user isn't actually in service of that. So we instilled new measurement techniques. Whenever we put these models in contact with reality and we learn about a problem, we actually go back and make sure we have good metrics for this stuff. So we measure sick efficiency now with every release to make sure we don't regress and actually improve on that metric. GPT-5 is an improvement, which is really exciting for me, but we have more work from there.

And more broadly, it caused us to articulate our point of view. I actually spent a bunch of time on a blog post that we just published on Monday on what we're optimizing ChatGPT for. And it really is to help you thrive and achieve your goals, not to keep you in the product. And so there was a bunch of good outcomes from that incident. It's a good example of how contact for reality is not just important for the use cases, but also for learning what to avoid because you would've never discovered this issue purely in a lab unless you actually heard from physicians.

---
