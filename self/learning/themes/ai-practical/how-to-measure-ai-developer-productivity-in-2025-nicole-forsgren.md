# Nicole Forsgren — How to measure AI developer productivity in 2025
*Theme: ai-practical | Extracted: 2026-04-04*

## Senior engineer agentic workflow for parallel AI coding

Lenny Rachitsky (00:10:34):
Is there anything more you could say about this engineer that figured out this really cool workflow, about just what that looks like?

Nicole Forsgren (00:10:39):
I've spoken with a handful of them, and I've kind of watched them work. I haven't built it myself yet. It's on my list. They've been able to set up this really incredible workspace and workflow where... Right now, a lot of us play around with tools and... We'll put in a prompt and we'll get a few lines back or maybe we'll put in a prompt and we'll get whole programs back. Well, what they can do is they can... Many times I'll see them say, to help prime it, "This is what I want to build. It needs to have these basic architectural components. It needs to have this kind of a stack. It needs to follow this general workflow. Help me think that through," and it'll kind of design it for it. And then for each piece, it'll assign an agent to go work on each pace in parallel, and then it'll say and upfront, "These need to be able to work together, make sure it's architected correctly. Make sure we use appropriate APIs and conventions."

Then at the end, they can let it run for a few minutes. They can think through something else that's interesting or they anticipate is going to be hairy, and they come back to something that's probably a little better than vibe coded. Because they were so systematic about it upfront, they're much closer to something that looks like production code.

Lenny Rachitsky (00:11:51):
So what I'm hearing is spending a little time upfront planning, what all these AI engineers are doing, versus just powering through and just figuring out as you go.

Nicole Forsgren (00:12:02):
Yeah.

---

## AI impact on flow state and restructuring work blocks

Lenny Rachitsky (00:18:31):
Can you say more about that? Just what is that? What are you thinking will be happening? Where do you think things go? What are you seeing working?

Nicole Forsgren (00:18:37):
This is purely speculative. But for example, Gloria Mark has done some really good work on attention and deep work, and humans can get about four hours of good deep work a day. That's about it.

Lenny Rachitsky (00:18:52):
Yeah,. I feel that.

Nicole Forsgren (00:18:54):
That's kind of the upper limit-ish for the most part, and I'm sure people are going to be like, "Well, I am superhuman and I can do-

Lenny Rachitsky (00:18:59):
What if you take 20 grams of creatine?

Nicole Forsgren (00:19:01):
Right. What if we microdose?

Lenny Rachitsky (00:19:06):
Yeah. So in the context of knowing we have about four hours of good deep work... I'm sure many of us have probably hit this, right? We have good periods. Maybe it's morning, maybe it's afternoon for folks. And then you hit a time where you're like, "I'm going to clean up my inbox because that is all I can do right now. I can be functional, but I'm not going to come up with my best innovative, problem solving, authoring, code writing work." A lot of times, the way to do that and to get into it is to have these long chunks to get into flow and to get that deep work. Usually, I'm [inaudible 00:19:43] two hours-ish. An hour can be tricky because it could take time to get into that state. Okay. Well, when we think about what it used to be like, back in the old days, three years ago, three and a half years ago, we could block off four hours of time and we could probably get two or three hours of really good work done. Because we were just focused, right? There were no interruptions, minimal interruptions.

Now, the nature of writing code and systems itself is interrupt driven or full of interruptions, at least, because you start something and then it interjects. So how do we think about that? Does that mean that a four-hour word block is still useful? Probably. But does that mean that now we can also make a 45-minute work block useful? Because getting into the flow is actually kind of handed off, at least, in part to the machine or the machine can help us get back into the flow by reminding us of context and generating diagrams of the system and all the things. So I think that's a really, really interesting area that's just ripe for questions and opportunity. And please, folks, do this research and come back to me because... It might not make my list, but it's such a great question.

Lenny Rachitsky (00:20:52):
That is so interesting. Essentially, every engineer is turning into an EM, engineering manager, coordinating all of these junior AI engineers. So your point is even if you have a 30-hour block, you can get deep into code, but you can unblock all these AI engineers that are running off doing tasks. Plus, your point is they remind you of just like, "Here's where you left off. Okay. You can just jump into this code, maybe make some tweaks."

Nicole Forsgren (00:21:17):
Yeah.

---

## Trust in AI-generated code and hallucination risk

Lenny Rachitsky (00:17:38):
We're going to get to your current thinking on the best way to do this stuff. You have a book coming out that explains how to do this well, so we're going to get to that. One thing I wanted to highlight in our last chat that we had, you highlighted that one of the biggest issues we're going to probably have with AI is trust, understanding and learning how much to trust the code that it generates, and also how much... you said this, two and a half years ago, that so much of the time is now going to be spent reviewing code versus writing code. That's exactly what I'm hearing.

Nicole Forsgren (00:18:10):
I think it'll be interesting to see how that impacts the way we structure work moving forward. We were talking about flow state and cognitive load. Now that our attention has to focus on things at certain times and it's broken up from how we used to do it, I think there's some real opportunity there to, not just rethink workflows, but rethink how we structure our days and how we structure our work.

Lenny Rachitsky (00:16:50):
And then efficiency and flow, "Can people get in the flow? How much time does it take to do things? What is the flow like through our system?" Here, I would probably add a couple of dimensions. So chatting with some of the early authors to say trust. Not to say trust wasn't important before, but now it's very, very front of mind. Right? Before you build your code, if the compile comes back, you're fine. And that's the way it is. LLMs are non-deterministic. Right now, we can't just put in a command and guess something back and accept it. We really need to evaluate it, so, "Are we seeing hallucinations? What's the reliability? Does it meet the style that we would typically write? And if it doesn't meet, is that fine?" So it depends on... Prescriptive. You got to make sure you're using it fit for purpose. Right?

---
