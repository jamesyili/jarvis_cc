# Aishwarya Naresh Reganti + Kiriti Badam — Why most AI products fail: Lessons from 50+ AI deployments at OpenAI, Google & Amazon
*Theme: product-strategy-growth | Extracted: 2026-04-04*

## Problem-first approach: don't let solution complexity bury the problem

Lenny Rachitsky (00:13:20):
Okay. So let's actually follow that because that's a really important component of how you recommend people build AI stuff, AI products, AI agents, all the AI things. So give us an example of what you're talking about here, this idea of starting slow with agency and control and then moving up this rung.

Kiriti Badam (00:20:08):
Exactly. I feel there's a bunch of things that you actually have to get confidence in before you get to V3. And it's easy to get overwhelmed that, oh, my AI agent is doing these things wrong in a hundred different ways and you're not going to actually tabulate all of them and fix it. Even though you've learned how do you deal with the evaluation practices and stuff like that, if you're starting on the wrong spot, you are actually going to have a hard time correcting things from there. And when you start small and when you start with building a very minimalistic version with high human control and low agency, it also forces you to think about what is the problem that I'm going to solve. We use this term called problem first. And to me, it was obvious in the sense that that I do need to think about the problem, but it's incredible how well it resonates with the people that in all this advancements of the AI that we are seeing, one easy, slippery slope is to just keep thinking about complexities of the solution and forget the problem that you're trying to solve.

So when you're trying to start at a smaller scale of autonomy, you start to really think about what is the problem that I'm trying to solve and how do I break it down into levels of autonomy that I can build later? So that is incredibly useful and we keep repeating this part and over and over with everyone we talk to.

Lenny Rachitsky (00:21:31):
And there's so many other benefits to limiting autonomy because there's just danger also of the thing doing too much for you and just messing up your, I don't know, your database, sending out all these emails you never expected. And there's like so many reasons this is a good idea.

Aishwarya Naresh Reganti (00:21:45):
Yep. I recently read this paper from a bunch of folks at UC Berkeley. Basically Matei Zaharia and the folks at Databricks and it said about 74% or 75% of the enterprises that they had spoken to, their biggest problem was reliability. And that's also why they weren't comfortable deploying products to their end users or building customer facing products because they just weren't sure or they just weren't comfortable doing that and exposing their users to a bunch of these risks. And that's also why they think a lot of AI products today have to do with productivity because it's much low autonomy versus end-to-end agents that would replace workflows.

---

## Building AI flywheels over time vs. one-click agent hype

Aishwarya Naresh Reganti (00:29:18):
I think folks that are successful are incredibly obsessed about understanding their workflows very well and augmenting parts that could be ripe for AI versus the ones that might need human in the loop somewhere, et cetera. Whenever you're trying to automate some part of a workflow, it's never the case that you could use an AI agent and that will solve your problems. It's always, you probably have a machine learning model that's going to do some part of the job. You have deterministic code doing some part of the job. So you really need to be obsessed with understanding that workflow so you can choose the right tool for the problem instead of being obsessed with the technology itself. And another pattern I see is also folks really understand this idea of working with a non-deterministic API, which is your LLM. And what that means is they also understand the AI development lifecycle looks very different and they iterate pretty quickly, which is can I build something iterate quickly in a way that it doesn't ruin my customer experience at the same time gives me enough amount of data so that I can estimate behavior.

So they build that flywheel very quickly. As of today, it's not about being the first company to have an agent among your competitors. It's about, have you built the right flywheels in place so that you can improve over time? When someone comes up to me and says, "We have this one click agent, it's going to be deployed in your system." And then in two or three days, it'll start showing you significant gains. I would almost be skeptical because it's just not possible. And that's not because the models aren't there, but because enterprise data and infrastructure is very messy and you need a bit to ... Even the agent needs a bit to understand how these systems work. There are very messy taxonomies everywhere.

So most of the times, if you're obsessed with the problem itself and you understand your workflows very well, you will know how to improve your agents over time instead of just slapping an agent and assuming that it'll work from day one. I probably will go as far to say that if someone's selling you one click-agents, it's pure marketing. You don't want to buy into that. I would rather go with a company that says, "We're going to build this pipeline for you," and that will learn over time and build a flywheel to improve than something that's going to work out of the box. To replace any critical workflow or to build something that can give you significant ROI, it easily takes four to six months of work, even if you have the best data layer and infrastructure layer.

---
