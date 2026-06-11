# Hamel Husain & Shreya Shankar — Why AI evals are the hottest new skill for product builders
*Theme: ai-practical | Extracted: 2026-04-04*

## What evals are and the full spectrum

Lenny Rachitsky (00:05:49):
I'm even more excited. Okay, so a couple years ago, I had never heard the term evals. Now it's one of the most trending topics on my podcast, essentially, that to build great AI products, you need to be really good at building evals. Also, it turns out some of the fastest-growing companies in the world are basically building and selling and creating evals for AI labs. I just had the CEO of Mercor on the podcast. So there's something really big happening here. I want to use this conversation to basically help people understand this space deeply, but let's start with the basics. Just what the heck are evals? For folks that have no idea what we're talking about, give us just a quick understanding of what an eval is, and let's start with Hamel.

Hamel Husain (00:05:49):
Sure. Evals is a way to systematically measure and improve an AI application, and it really doesn't have to be scary or unapproachable at all. It really is, at its core, data analytics on your LLM application and a systematic way of looking at that data, and where necessary, creating metrics around things so you can measure what's happening, and then so you can iterate and do experiments and improve.

Lenny Rachitsky (00:06:22):
So that's a really good broad way of thinking about it. If you go one level deeper just to give people a very, even more concrete way of imagining and visualizing what we're talking about, even if you have a example to show would be even better, what's an even deeper way of understanding what an eval is?

Hamel Husain (00:06:36):
Let's say you have a real estate assistant application and it's not working the way you want. It's not writing emails to customers the way you want, or it's not calling the right tools, or any number of errors. And before evals, you would be left with guessing. You would maybe fix a prompt and hope that you're not breaking anything else with that prompt, and you might rely on vibe checks, which is totally fine.

And vibe checks are good and you should do vibe checks initially, but it can become very unmanageable very fast because as your application grows, it's really hard to rely on vibe checks. You just feel lost. And so evals help you create metrics that you can use to measure how your application is doing and kind of give you a way to improve your application with confidence. That you have a feedback signal in which to iterate against.

Lenny Rachitsky (00:07:44):
So just to make very real, so imagining this real estate agent, maybe they're helping you book a listing or go see an open house. The idea here is you have this agent talking to people, it's answering questions, pointing them to things. As a builder of that agent, how do you know if it's giving them good advice, good answers? Is it telling them things that are completely wrong?

So the idea of evals, essentially, is to build a set of tests that tell you, how often is this agent doing something wrong that you don't want it to do? And there's a bunch of ways you could define wrong. It could be just making up stuff. It could be just answering in a really strange way. The way I think about evals, and tell me if this is wrong, just simply is like unit tests for code. You're smiling. You're like, "No, you idiot."

Shreya Shankar (00:08:29):
No, that's not what I was thinking.

Lenny Rachitsky (00:08:31):
Okay. Okay, okay, tell me. Tell me, how does that feel as a metaphor?

Shreya Shankar (00:08:35):
Okay. I like what you said first, which is we had a very broad definition. Evals is a big spectrum of ways to measure application quality. Now, unit tests are one way of doing this. Maybe there are some non-negotiable functionalities that you want your AI assistant to have, and unit tests are going to be able to check that. Now, maybe you also, because these AI assistants are doing such open-ended tasks, you kind of also want to measure how good are they at very vague or ambiguous things like responding to new types of user requests or figuring out if there's new distributions of data like new users are coming and using your real estate agent that you didn't even know would use your product. And then all of a sudden, you think, "Oh, there's a different way you want to kind of accommodate this new group of people."

So evals could also be a way of looking at your data regularly to find these new cohorts of people. Evals could also be like metrics that you just want to track over time, like you want to track people saying, "Yes. Thumbs up. I liked your message." You want very, very basic things that are not necessarily AI-related but can go back into this flywheel of improving your product. So I would say, overall, unit tests are a very small part of that very big puzzle.

---

## Error analysis and open coding walkthrough

Hamel Husain (00:17:07):
So it turns out there is a way to do it that is completely manageable, and it's not something that we invented. It's been around in machine learning and data science for a really long time, and it's called error analysis. And what you do is, the first step in conquering data like this is just to write notes. Okay? So you got to put your product hat on, which is why we're talking to you, because product people have to be in the room and they have to be involved in sort of doing this. Usually a developer is not suited to do this, especially if it's not a coding application.

Lenny Rachitsky (00:17:47):
And just to mirror back, why I think you're saying that is because this is the user experience of your product. People talking to this agent is the entire product essentially, and so it makes sense for the product person to be super involved in this.

Hamel Husain (00:17:59):
Yeah. So let's reflect on this conversation. Okay, a user asked about availability. The AI said, "Oh, we don't really have that. Have a nice day." Now, for a product that is helping you with lead management, is that good? Do you feel like this is the way we want it to go?

Lenny Rachitsky (00:18:30):
Not ideal.

Hamel Husain (00:18:32):
Yes, not ideal, and I'm glad you said that. A lot of people would say, "Oh, it's great. The AI did the right thing. It looked, it said, 'We didn't have available,' and it's not available." But with your product hat on, you know that's not correct. And so what you would do is you would just write a quick note here. You would say, "Okay." You might pop in here, and you can write a note. So every observability application has ability to write notes, and you wouldn't try to figure out if something is wrong. In this case, it's kind of not doing the right thing, but you just write a quick note, "Should have handed off to a human."

Lenny Rachitsky (00:19:19):
And as we watch this happening, it's like you mention this and you'll explain more. You're doing this, this feels very manual and unscalable, but as you said, this is just one step of the process and there's a system to this. That was just the first one.

Hamel Husain (00:19:30):
Yeah, and you don't have to do it for all of your data. You sample your data and just take a look, and it's surprising how much you learn when you do this. Everyone that does this immediately gets addicted to it and they say, "This is the greatest thing that you can do when you're building an AI application." You just learn a lot and you're like, "Hmm, this is not how I want it to work. Okay."

Shreya Shankar (00:23:55):
One common question that we get from people at this stage is, "Okay, I understand what's going on. Can I ask an LLM to do this process for me?"

Lenny Rachitsky (00:24:04):
Mm, great question.

Shreya Shankar (00:24:04):
And I loved Hamel's most recent example because what we usually find when we try to ask an LLM to do this error analysis is it just says the trace looks good because it doesn't have the context needed to understand whether something might be bad product smell or not. For example, the hallucination about scheduling the tour, right? I can guarantee you, I would bet money on this, if I put that into chat GPT and asked, "Is there an error?" it would say, "No, did a great job."

But Hamel had the context of knowing, "Oh, we don't actually have this virtual tour functionality," right? So I think, in these cases, it's so important to make sure you are manually doing this yourself. And we can talk a little bit more about when to use LLMs in the process later, but number one pitfall right here is people are like, "Let me automate this with an LLM."

Lenny Rachitsky (00:24:55):
Do you think we'll get to a place where an agent can do this, where it has that context?

Shreya Shankar (00:24:58):
Oh, no. No, no, no. Sorry. There are parts of error analysis that an LLM is suited for, which we could talk about later in this podcast. But right now, in this stage of free form, note-taking is not the place for an LLM.

---

## LLM as judge: code-based vs LLM evaluation

Lenny Rachitsky (00:48:31):
Before we get into that actually, just to make sure people know exactly what you're describing there, these two types of evals. One is you said it's code-based and one is LLM as judge. Maybe Shreya, just help us understand what code-based eval even is? It's essentially a unit test? Is that a simple way to think about it?

Shreya Shankar (00:48:46):
Yeah. Maybe eval is not the right term here, but think automated evaluator. So when we find these failure modes, one of the things we want is, "Okay. Can we now go check the prevalence of that failure mode in an automated way without me manually labeling and doing all the coding and the grouping, and I want to run it on thousands and thousands of traces, I want to run it every week." That is, okay. You should probably build an automated evaluator to check for that failure mode.

Now, when we're saying code-based versus LLM-based, we're saying, "Okay. So maybe I could write a Python function or a piece of code to check whether that failure mode is present in a trace or not." And that's possible to do for certain things like checking the output is JSON, or checking that it's markdown, or checking that it's short. These are all things you can capture in code or you could approximately capture in code.

When we're talking about LLM judge here, we're saying that this is a complex failure mode and we don't know how to evaluate in an automated way. So maybe we will try to use an LLM to evaluate this very, very narrow, specific failure mode of handoffs.

Lenny Rachitsky (00:49:56):
So just to try to mirror back what you're describing, you want to test what your, say, agent or AI product is doing. You ask it a question, it gets back with something.

One way to test if it's giving you the right answer is if it's consistently doing the same thing, that you could write a code to tell you this is true or false. For example, will it ever say there's a virtual tour? So you could ask it.

Shreya Shankar (00:50:18):
Yes.

Lenny Rachitsky (00:50:18):
"Do you provide virtual tours?" It says yes or no, and then you could write code to tell you if it's correct based on that specific answer.

But if you're asking about something more complicated and it's not binary, in one world, you need a human to tell you this is correct. The solution to avoid humans having to review all this every time automatically is LLMs replacing human judgment, and you'd call it an LLM as judge. The LLM as being the judge if this is correct or not.

Shreya Shankar (00:50:47):
Absolutely. You nailed it.

Lenny Rachitsky (00:50:48):
Great.

Shreya Shankar (00:50:49):
So people always think, "Oh, this is at least as hard as my problem of creating the original agent." And it's not, because you're asking the judge to do one thing, evaluate one failure mode, so the scope of the problem is very small and the output of this LLM judge is pass or fail. So it is a very, very tightly scoped thing that LLM judges are very capable of doing very reliably.

Lenny Rachitsky (00:51:18):
And the goal here is just to have a suite of tests that run before you ship to production that tell you things are going the way you want them to? The way your agent is interacting is correct?

Shreya Shankar (00:51:28):
The beautiful thing about LLM judges, you can use them in unit tests or CI, sure, but you could also use it online for monitoring, right? I can sample 1000 traces every day, run my LLM judge, real production traces, and see what the failure rate is there. This is not a unit test, but still now we get an extremely specific measure of application quality.

Lenny Rachitsky (00:51:53):
Cool. That's a really great point because a lot of people just see evals for being this not-real-life thing. It's a thing that you test before it's actually in the real world. And what's actually happening in the real world, you're saying you should actually do exactly that?

Shreya Shankar (00:52:04):
Yeah.

Lenny Rachitsky (00:52:04):
Test your real thing running in production? And it's a daily, hourly sort of thing you could be running?

Shreya Shankar (00:52:09):
Totally.

---
