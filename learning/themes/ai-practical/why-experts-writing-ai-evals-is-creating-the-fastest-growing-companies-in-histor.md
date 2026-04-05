# Brendan Foody — Why experts writing AI evals is creating the fastest-growing companies in history
*Theme: ai-practical | Extracted: 2026-04-04*

## What evals are and why they matter

Lenny Rachitsky (00:06:19): The reason this caught my attention is that's one of the most recurring trends on this podcast, people talking about the increasing value of learning how to do evals well and the value of evals for companies. It feels like still people don't know what the hell this is what we're talking about, why this is so important. Talk about just what you think people are still missing, what they need to know, what this era of evals means.

Brendan Foody (00:06:39): If the model is the product, then the eval is the product requirement document. And the way that researchers' day-to-day looks is that they'll run dozens of experiments where they'll make small improvements on an eval set. And reinforcement learning is becoming so effective that once they have an eval, they can help climb it. If you look at just how fast people were able to saturate Olympiad Math once they focused on it, how fast we're even saturating SWE-bench once we focus on it. And so in many ways, the barrier to applying agents the entire economy to automate every workflow is how do we measure success? How do we eval it? And write the PRDs for everything that we want agents to do, which Mercor is obviously a huge part of doing.

Lenny Rachitsky (00:07:25): So people hearing this, they're like, "Oh, yeah. Okay, shit. I got to really pay attention to this eval stuff." Any advice about learning how to do this well? What companies that are doing this well are doing differently? Help people get better at this thing.

Brendan Foody (00:07:39): Yeah. I think that for enterprises especially, the core way to think about it is how can they build a test or systematic way to measure how well AI automates their core value chain? So if it's an architecture firm that's producing these architecture diagrams of what they provide to their end customer, how can they effectively measure that? And each company has its own value chain or maybe a handful of them if it's a multi-product company. And just thinking about how they measure that is the prerequisite to really effectively applying AI throughout their entire business.

---

## What experts actually do writing evals day-to-day

Lenny Rachitsky (00:13:12): Okay, what are these people actually doing? So what's an example of a kind of person that is sought after? And then what are they doing sitting there at the computer?

Brendan Foody (00:13:19): Effectively, the market is bound by the amount of things where humans can do something that models can't. So I'll make that very concrete. Say you have a model that you want to write a red line for a contract in the way that a lawyer would, and it makes a handful of mistakes, misses a bunch of key points in doing so. What you could do is have a lawyer create a rubric similar to how a professor might create a rubric to create a deliverable for what are the things we want the model to be able to do? So it can effectively score that, right? Plus however much of it identifies this or XYZ key point. And that's really the foundation to measuring what does progress look like for models? Is this model achieving the capabilities that these professionals want? As well as how do we use this as training data to reward and to reinforce a lot of the capabilities that people want models to achieve.

Lenny Rachitsky (00:14:19): Okay, so they're essentially writing evals just to connect it back to original conversation.

Brendan Foody (00:14:23): Exactly. Well, that's an interesting thing is everyone talks about RL environment. I feel like the two hot button things are like RL environments and evals, but one thing like Andrej Karpathy's tweeted out about a bunch is there's not actually a nuance. It's in the data type. It's more just a different semantic way of describing what it's being used for. But ultimately, it's just some stasis point for how do you measure what good looks like? And you can use that either as the benchmark to the sales collateral, as Sarah was saying, to say, here is why are models the best model in the world and here's the capabilities that we've been working towards, or you can use it on the post-training side to reward certain model trajectories and achieve those capabilities.

---

## AI as thought partner — voice mode, day-to-day workflows

Lenny Rachitsky (01:00:41): So I'll use that as a segue to a final question. I'm going to take us to AI Corner, which is a recurring segment on the podcast. What's some way that you personally use AI to do better work to help you in life?

Brendan Foody (01:00:52): Well, let's see. I use it a lot to write documents, as you would expect. I also talk to get advice on problems. I find it helpful to just reason through almost as a thought partner because, yeah, I don't know. I find I think better sometimes when I'm talking something through, but I can't talk through everything with colleagues or people around me.

Lenny Rachitsky (01:01:15): And so this is like ChatGPT Voice Mode mostly or something else.

Brendan Foody (01:01:16): Yeah, I like ChatGPT Voice Mode a lot. There's stuff— or room for improvement, but I am very excited about the future of Voice.

---
