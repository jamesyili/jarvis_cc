# Kevin Weil — OpenAI's CPO on how AI changes must-have skills, moats, coding, startup playbooks, more | Kevin Weil
*Theme: ai-practical | Extracted: 2026-04-04*

## Writing evals as core skill for product builders

Lenny Rachitsky (00:18:45): Let's actually follow this thread on evals... The thing that I heard that kind of stuck with people from that panel was a comment you made where you said that writing evals is going to become a core skill for product managers, and I feel like that probably applies further than just product managers... So could you just briefly explain what is an eval and then just why do you think this is going to be so important for people building products in the future?

Kevin Weil (00:19:23): Yeah, sure. I think the easiest way to think about it is almost like a quiz for a model, a test to gauge how well it knows a certain set of subject material or how good it is at responding to a certain set of questions. So in the same way you take a calculus class and then you have calculus tests that see if you've learned what you're supposed to learn. You have evals that test how good is the model at creative writing? How good is the model at graduate level science? How good is the model at competitive coding?

Lenny Rachitsky (00:20:04): Is it a simple way to think about it, like unit tests for model?

Kevin Weil (00:20:07): Yeah, unit tests, tests in general for models. Totally.

Lenny Rachitsky (00:20:10): Great, great. Okay. And then why is this so important for people that don't totally understand what the hell's going on here with evals? Why is this so key to building AI products?

Kevin Weil (00:20:20): Well, it gets back to what I was saying. You need to know whether your model is going to... There are certain things that models will get right. 99.95% of the time and you can just be confident. There are things that they're going to be 95% right on and things they're going to be 60% right on. If the model's 60% right on something, you're going to need to build your product totally differently. And by the way, these things aren't static either. So a big part of evals is if you know you're building for some use case. So let's take our deep research product... The idea is with deep research for people who haven't used it, you can give ChatGPT now an arbitrarily complex query... it might go work for 25, 30 minutes and do work that would've taken you a week. So as we were building that product, we were designing evals at the same time as we were thinking about how this product was going to work and we were trying to go through hero use cases.

Here's a question you want to be able to ask. Here's an amazing answer for that question. And then turning those into evals and then hill climbing on those evals. So it's not just that the model is static and we hope it does okay on a certain set of things, you can teach the model. You can make this a continuous learning process.

---

## Vibe coding and AI-augmented product workflows today

Lenny Rachitsky (00:53:52): ... how do you and the team, say engineers, PMs, use AI in your work? Is there anything that's really interesting or things that you think people are sleeping on in how you use AI in your day-to-day work?

Kevin Weil (00:53:52): We use it a lot. I mean, every one of us is in Chat GPT all the time summarizing docs, using it to help write docs with GPTs that write product specs and things like that, all the stuff that you would imagine. I mean talk about writing evals, you can actually use models to help you write evals and they're pretty good at it. That all said, I'm still sort of disappointed by us, and I really mean me, in, if I were to just teleport my five-year-old self leading product at some other company into my day job, I would recognize it still. And I think we should be in a world, certainly a year from now, probably even more now, where I almost wouldn't recognize it because the workflows are so different and I'm using AI so heavily, and I'd still recognize it today. So I think in some sense, I'm not doing a good enough job of that.

Just to give an example, why shouldn't we be vibe coding demos right, left and center? Instead of showing stuff in Figma, we should be showing prototypes that people are vibe coding over the course of 30 minutes to illustrate proofs of concept and to explore ideas. That's totally possible today, and we're not doing it enough. Actually, our chief people officer, Julia, was telling me the other day, she vibe coded an internal tool that she had at a previous job that she really wanted to have here at Open AI and she opened, I don't know, Windsurf or something, and vibe coded it. How cool is that? And if our chief people officer is doing it, we have no excuse to not be doing it more.

Lenny Rachitsky (00:55:34): That's an awesome story. And some people may not have heard this term vibe coding. Can you describe what that means?

Kevin Weil (00:55:40): Yeah, I think this was Andrej's term... So you have these tools like Cursor and Windsurf and GitHub Copilot that are very good at suggesting what code you might want to write... As the models are getting better and as people are getting more used to it, you can kind of just let go of the wheel a little bit. And when the model's suggesting stuff, it's just like, tap, tap, tap, tap, tap. Keep going. Yes, yes, yes, yes, yes.

And of course the model makes mistakes or it does something that doesn't compile, but when it doesn't compile, you paste the error in and you say, go, go, go, go, go. And then you test it out and it does one thing that you don't want it to do, so you enter in an instruction and say, go, go, go, go, go, and you just let the model do its thing. And it's not that you would do that for production code that needed to be super tight today yet, but for so many things, you're trying to get to a proof of concept, you're getting to a demo and you can really take your hands off the wheel and the model will do an amazing job, and that's vibe coding.

---

## Fine-tuning and ensemble models as the future of every product team

Lenny Rachitsky (00:57:19): So let me just ask, I guess, when you look at product teams in the future, you talked about how you guys should be doing this more, instead of designs, having prototypes, what do you think might be the biggest changes in how product teams are structured or built?

Kevin Weil (00:57:36): I think you're definitely going to live in a world where you have researchers built into every product team. And I don't even mean just at foundation model companies because I think the future... Actually, frankly one thing that I'm sort of surprised about about our industry in general is that there's not a greater use of fine-tuned models. A lot of people... These models are very good, so our API does a lot of things really well, but when you have particular use cases, you can always make the model perform better on a particular use case by fine-tuning it. It's probably just a matter of time. Folks aren't quite comfortable yet with doing that in every case. But to me, there's no question that that's the future. Models are going to be everywhere just like transistors are everywhere, AI is going to be just a part of the fabric of everything we do, but I think there are going to be a lot of fine-tuned models because why would you not want to more specifically customize a model against a particular use case?

And so I think you're going to want sort of quasi researcher machine learning engineer types as part of pretty much every team because fine-tuning a model is just going to be part of the core workflow for building most products... We use ensembles of models much more internally than people might think. So it's not, "I have 10 different problems. I'll just ask baseline GPT four oh about a bunch of these things." If we have 10 different problems, we might solve them using 20 different model calls, some of which are using specialized fine-tuned models, they're using models of different sizes because maybe you have different latency requirements or cost requirements for different questions... you want to break the problem down into more specific tasks versus some broader set of high level tasks. And then you can use models very specifically to get very good at each individual thing. And then you have an ensemble that tackles the whole thing.

---
