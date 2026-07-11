# Aishwarya Naresh Reganti + Kiriti Badam — Why most AI products fail: Lessons from 50+ AI deployments at OpenAI, Google & Amazon
*Theme: ai-practical | Extracted: 2026-04-04*

## Non-determinism and agency control tradeoff in AI products

Lenny Rachitsky (00:07:37):
So let me follow that thread. We worked on a guest post together that came out a few months ago. And the thing that stood out to me most that stuck with me most after working on that post is this really key insight that building AI products is very different from building non-AI products. And the thing that you're big on getting across is there's two very big differences. Talk about those two differences.

Aishwarya Naresh Reganti (00:08:01):
Yes. And again, I want to make sure that we drive home the right point. There are tons of similarities of building AI systems and software systems as well, but then there are some things that kind of fundamentally change the way you build software systems versus AI systems. And one of them that most people tend to ignore is the non-determinism. You're pretty much working with a non-deterministic API as compared to traditional software. What does that mean and why does that have to affect us is in traditional software, you pretty much have a very well-mapped decision engine or workflow. Think of something like Booking.com. You have an intention that you want to make a booking in San Francisco for two nights, et cetera. The product has kind of been built so that your intention can be converted into a particular action and you kind of are clicking through a bunch of buttons, options, forms, and all of that, and you finally achieve your intention.

But now that layer in AI products has completely been replaced by a very fluid interface, which is mostly natural language, which means the user can literally come up with a ton of ways of saying or communicating their intentions. And that kind of changes a lot of things because now you don't know how your user's going to be here. That's on the input side. And the output is also that you're working with a non-deterministic probabilistic API, which is your LLM. And LLMs are pretty sensitive to prompt phrasings and they're pretty much black boxes. So you don't even know how the output surface will look like. So you don't know how the user might behave with your product, and you also don't know how the LLM might respond to that. So you're now working with an input, output, and a process. You don't understand all the three very well. You're trying to anticipate behavior and build for it.

And with agentic systems, this kind of gets even harder. And that's where we talk about the second difference, which is the agency control trade-off. What we mean by that, and I'm kind of shocked so many people don't talk about this. They're extremely obsessed with building autonomous systems, agents that can do work for you. But every time you hand over decision-making capabilities or autonomy to agentic systems, you're kind of relinquishing some amount of control on your end. And when you do that, you want to make sure that your agent has gained your trust or it is reliable enough that you can allow it to make decisions. And that's where we talk about this agency controlled trade-off, which is if you give your AI agent or your AI system, whatever it is, more agency, which is the ability to make decisions, you're also losing some control and you want to make sure that the agent or the AI system has earned that ability or has built up trust over time.

---

## CCCD framework: continuous calibration for AI product lifecycle

Lenny Rachitsky (00:45:43):
We've been talking for almost an hour already, and we haven't even covered your extremely powerful software development workflow for building AI products that you two developed that you teach in your course, that you basically combined all the stuff we've been talking about into a step-by-step approach to building AI products. You call it the continuous calibration, continuous development framework. Let's pull up a visual to show people what the heck we're talking about, and then just walk us through what this is, how this works, how teams can shift the way they build their AI products to this approach to help them avoid a lot of pain and suffering.

Aishwarya Naresh Reganti (00:46:18):
Before we go about explaining the life cycle, a quick story on why Kiriti and I came up with this is because there are tons of companies that we keep talking to that have the pressure from their competitors because they're all building agents. We should be building agents that are entirely autonomous. And I did end up working with a few customers where we built these end-to-end agents. And turns out that because you start off at a place where you don't know how the user might interact with your system and what kind of responses or actions the AI might come up with, it's really hard to fix problems when you have this really huge workflow, which is taking four or five steps, making tons of decisions. You just end up debugging so much and then kind of hot fixing to the point where at a time we were building for a customer support use case, which is the example that we give in the newsletter as well. And we had to shut down the product because we were doing so many hot fixes and there was no way we could count all the emerging problems that were coming up.

The idea is pretty simple, which is we have this right side of the loop, which is continuous development, where you scope capability and curate data, essentially get a data set of what your expected inputs are and what your expected outputs should be looking at. This is a very good exercise before you start building any AI product because many times you figure out that a lot of the folks within the team are just not aligned on how the product should behave. And that's where your PMs can really give in a lot more information and your subject matter experts as well. So you have this data set that you know your AI product should be doing really well on. It's not comprehensive, but it lets you get started. And then you set up the application and then design the right kind of evaluation metrics.

And the second part is the continuous calibration, which is the part where you understand what behavior you hadn't expected in the beginning, right? Because when you start the development process, you have this data set that you're optimizing for, but more often than not, you realize that that data set is not comprehensive enough because users start behaving with your systems in ways that you did not predict. And that's where you want to do the calibration piece. I've deployed my system. Now I see that there are patterns that I did not really expect and your evaluation metrics should give you some insight into those patterns, but sometimes you figure out that those metrics were also not enough and you probably have new error patterns that you have not thought about. And that's where you analyze your behavior, spot error patterns. You apply fixes for issues that you see, but you also design newer evaluation metrics to figure out that they are emerging patterns.

And what we specifically also mention is while you're going through these iterations, try to think of lower agency iterations in the beginning and higher control iterations. What that means is constrain the number of decisions your AI systems can make and make sure that they're humans in the loop and then increase that over time because you're kind of building a flywheel of behavior and you're understanding what kind of use cases are coming in or how your users are using the system.

---

## Overrated vs underrated in AI: multi-agents misunderstood, coding agents underrated

Lenny Rachitsky (01:01:24):
What do you think is overhyped in the AI space right now? And even more importantly, what do you think is under-hyped?

Kiriti Badam (01:01:34):
As I said, super optimistic in different things that are going in AI. So I wouldn't say overhyped, but I feel kind of misunderstood is the concept of multi-agents. People have this notion of, "I have this incredibly complex problem. Now I'm going to break it down into, hey, you are this agent. Take care of this. You're this agent. Take care of this." And now if I somehow connect all of these agents, they think they're the agent utopia and it's never the case that there are incredibly successful multi-agent systems that are built. There's no doubt about that. But I feel a lot of it comes in terms of how are you limiting the ways in which the system can go off tracks. For example, if you're building a supervisor agent and there are subagents that actually do the work for the super agent, supervisor agent, that is a very successful pattern. But coming with this notion of I'm going to divide the responsibilities based on functionality and somehow expect all of that to work together in some sort of gossip protocol, that is extremely misunderstood that you could do that. I don't think current ways of building and current model capabilities are right there in terms of building those kind of applications.

Underrated, I feel it's hard to probably believe, but I still feel coding agents are underrated in the sense that I feel like you can go on Twitter and you can go on Reddit and you see a lot of chatter about coding agents, but talking to an engineer in any random company, especially outside of Bay Area, you can see the amount of impact this coding agents can create and the penetration is very low. So I feel like 2025 and 2026 is going to be an incredible year for optimizing all of these processes.

Aishwarya Naresh Reganti (01:04:12):
Can I say evals? Will I be canceled?

Lenny Rachitsky (01:04:15):
In which category? Which bucket do they go?

Aishwarya Naresh Reganti (01:04:18):
Overrated.

Lenny Rachitsky (01:04:20):
Overrated. Okay, go for it. We won't let you get canceled.

Aishwarya Naresh Reganti (01:04:22):
Just kidding. I think evals are misunderstood. They are important, folks. I'm not saying they're not important, but I think just this, I'm going to keep jumping across tools and going to pick up and learn if new tool is overrated. I still am old school and feel like you would really need to be obsessed with the business problem you're trying to solve. AI is only a tool. I try to think of it that way. Of course, you need to be learning about the latest and greatest, but don't be so obsessed with just building so quickly. Building is really cheap today. Design is more expensive, really thinking about your product, what you're going to build. Is it going to really solve a pain point? Is what is way more valuable today? And it will only become more true in the near future. So really obsessing about your problem and design is underrated and just rote building is overrated, I guess.

---
