# Alexander Embiricos — How to drive word of mouth | Nilan Peiris (CPO of Wise)
*Theme: product-strategy-growth | Extracted: 2026-04-04*

## What unlocked 20x growth: cloud to local IDE

Lenny Rachitsky (00:16:55):
You hinted at this, what unlocked this growth, I'm extremely interested in hearing that. It felt like before, I don't know, maybe this was before you joined the team, it just felt like Cloud Code was killing it. Just everyone was sitting on top of Cloud Code. It was by far the best way to code. And then all of a sudden Codex comes around. I remember Karpathy tweeted that he just has never seen a model like this. I think the tweet was the gnarliest bugs that he runs into that he just spends hours trying to figure out nothing else has solved, he gives it to Codex, lets it run for an hour and it solves it. What'd you guys do?

Alexander Embiricos (00:17:30):
We have this strong sort of mission here at OpenAI basically to build AGI. And so we think a lot about how can we shape the product so that it can scale. Earlier I was mentioning like, "Hey, if you're an engineer, you should be getting help from AI thousands of times per day," and so we thought a lot about the primitives for that when we launched our first version of Codex, which was Codex Cloud. And that was basically a product that had its own computer, lived in the cloud, you could delegate to it. And the coolest part about that is you could run many, many tasks in parallel. But some of the challenges that we saw are that it's a little bit harder to set that up, both in terms of environment configuration, like giving the model the tools it needs to validate its changes and to learn how to prompt in that way.

My analogy for this is, going back to this teammate analogy, it's like if you hired a teammate, but you're never allowed to get on a call with them and you can only go back and forth asynchronously over time. That works for some teammates and eventually that's actually how you want to spend most of your time. So that's still the future, but it's hard to initially adopt. And so we still have that vision of like, that's what we're trying to get you to, a teammate that you delegate to and then is proactive, and we're seeing that growing. But the key unlock is actually first you need to land with users in a way that's much more intuitive and trivial to get value from.

So the way that most people discover, the vast majority of users discover Codex today is either they download an IDE extension or they run it in their CLI and the agent works there with you on your computer interactively. And it works within a sandbox, which is actually a really cool piece of tech to help that be safe and secure, but it has access to all those dependencies. So if the agent needs to do something, it needs to run a command, it can do so within the sandbox. We don't have to set up any environment. And if it's a command that doesn't work in the sandbox, it can just ask you. And so you can get into this really strong feedback loop using the model. And then over time, our team's job is to help turn that feedback loop into you as a byproduct of using the product, configuring it so that you can then be delegating to it down the line.

Lenny Rachitsky (00:20:01):
So what I'm hearing is the initial version of Codex was almost too far in the future. It's like a remote in the cloud agent that's coding for you asynchronously. And what you did is, "Okay, let's actually come back a little bit, let's integrate into the way engineers already integrate into IDs and locally and help them on ramp to this new world."

Alexander Embiricos (00:20:21):
Totally. And it was quite interesting because we dogfood product a ton at OpenAI. So dogfood as in we use our own product. And so Codex has been accelerating OpenAI over the course of the entire year, and the cloud product was a massive accelerant to the company as well. It just turns out that this was one of those places where the signal we got from dogfooding is a little bit different from the signal you get from the general market because at OpenAI, we train reasoning models all day and so we're very used to this kind of prompting and think upfront, run things massively in parallel and it would take some time and then come back to it later asynchronously. And so now when we build, we still get a ton of signal from dogfooding internally, but we're also very cognizant of the different ways that different audiences use the product.

---

## D7 retention and Reddit as product signal

Lenny Rachitsky (00:55:36):
When you think about progress on Codex, I imagine you have a bunch of evals and there's all these public benchmarks. What's something you look at to tell you, "Okay, we're making really good progress," I imagine it's not going to be the one thing, but what do you focus on? What's something you're trying to push? What's a KPI or two?

Alexander Embiricos (00:55:51):
One of the things that I'm constantly reminding myself of is that a tool like Codex naturally is a tool that you would become a power user of. So we can accidentally spend a lot of our time thinking about features that are very deep in the user adoption journey. And so we can kind of end up oversolving for that. And so I think it's just critically important to go look at your D7 retention. Just go try the product, sign up from scratch again. I have a few too many ChatGPT Pro accounts that I've, in order to maximally correctly dogfood, signed up for on my Gmail and they charge me 200 bucks a month. I need to expense those. But I think just the feeling of being end user and the early retention stats are still super important for us because as much as this category is taking off, I think we're still in the very early days of people using them.

Another thing that we do that I think we might be the most user feedback/social media pilled team out there in this space is like a few of us are constantly on Reddit and Twitter, and there's praise up there and there's a lot of complaints, but we take the complaints very seriously and look at them. And I think that, again, because you can use a coding agent for so many different things, it often is kind of broken in many sort of ways for specific behaviors. So we actually monitor a lot just what the vibes are on social media pretty often, especially I think for Twitter/X, it's a little bit more hypey and then Reddit is a little more negative but real actually. So I've started increasingly paying attention to how people are talking about using Codex on Reddit actually.

---

## Distribution and customer understanding now the key differentiator

Lenny Rachitsky (00:53:51):
I'm curious just the second order effects of this sort of thing, just how quickly it is to build stuff. What does that do? Does that mean distribution becomes much, much more important? Does it mean ideas are just worth a lot more? It's interesting to think about how quick how that changes.

Alexander Embiricos (00:53:51):
I'm curious what you think. I still don't think ideas are worth as much as maybe a lot of people think. I still think execution is really hard. You can build something fast, but you still need to execute well on it, still needs to make sense and be a coherent thing overall, yeah, and distribution is massive.

Lenny Rachitsky (00:54:08):
Yeah. Just feels like everything else is now more important. Everything that isn't the building piece, which is coming up with an idea, getting to market, profit, all that kind of stuff.

Alexander Embiricos (00:54:18):
Yeah. I think we might've been in this weird temporary phase where, for a while, it was so hard to build product that you mostly just had to be really good at building product and it maybe didn't matter if you had an intimate understanding of a specific customer. But now I think we're getting to this point where actually if I could only choose one thing to understand, it would be really meaningful understanding of the problems that a certain customer has. If I could only go in with one core competency.

So I think that's ultimately still what's going to matter most. If you're starting a new company today and you have a really good understanding and network of customers that are currently underserved by AI tools, I think you're set. Whereas if you're good at building websites, but you don't have any specific customer to build for, I think you're in for a much harder time.

---
