# Alexander Embiricos — How to drive word of mouth | Nilan Peiris (CPO of Wise)
*Theme: ai-practical | Extracted: 2026-04-04*

## Codex as proactive teammate, not just coding tool

Lenny Rachitsky (00:14:54):
When people think about Cursor and even Cloud Code, it's like a IDE that helps you code and auto completes code and maybe does some agentic work. What I'm hearing here is the vision is different, which is it's a teammate. It's like a remote teammate, a building code for you that you talk to and ask to do things. And that also does IDE, auto complete and things like that. Is that a kind of a differentiator in the way you think about Codex?

Alexander Embiricos (00:15:18):
It's basically this idea that if you're a developer and you're trying to get something done, we want you to just feel like you have superpowers and you're able to move much, much faster. But we don't think that in order for you to reap those benefits, you need to be sitting there constantly thinking about, "How can I invoke AI at this point to do this thing?" We want you to be able to plug it in to the way that you work and have it just start to do stuff without you having to think about it.

Lenny Rachitsky (00:13:21):
I thought the point about not reading Slack and Datadog was it's just not distracted, it's just constantly focused and is always in flow. But I get what you're saying there is it doesn't have all the context on everything that's going on.

Alexander Embiricos (00:13:31):
Yeah. And that's not only true when it's performing a task, but again, if you think of the best team and teammates, you don't tell them what to do. Maybe when you first hire them, you have a couple meetings and you're like, "Hey," you learn, "Okay, these prompts work for this teammate, these prompts don't. This is how to communicate with this person." Then eventually you give them some starter tasks, you delegate a few tasks. But then eventually you just say like, "Hey, great. Okay, you're working with this set of people in this area of the code base. Feel free to work with other people on other parts of the code base too, even. And yeah, you tell me what you think makes sense to be done." And so we think of this as proactivity and one of our major goals with Codex is to get to proactivity.

I think this is critically important to achieve the mission of OpenAI, which is to deliver the benefits of AGI to all humanity. I like to joke today that AI products, and it's a half joke, they're actually really hard to use because you have to be very thoughtful about when it could help you. And if you're not prompting a model to help you, it's probably not helping you at that time. And if you think of how many times the average user is prompting AI today, it's probably tens of times. But if you think of how many times people could actually get benefit from a really intelligent entity, it's thousands of times per day. And so a large part of our goal with Codex is to figure out what is the shape of an actual teammate agent that is helpful by default.

---

## Every agent should be a coding agent — the theory

Lenny Rachitsky (00:28:08):
Yeah. So we're getting to the one-year time horizon conversation. A lot of this might happen sooner, but in terms of fuzziness, I think we're at the one year. So I'll give you a contention and a plausible way we get there, but as for how it happens, who knows? So basically, if we're going to build a super assistant, it has to be able to do things. So we're going to have a model and it's going to be able to do stuff affecting your world. And one of the learnings I think we've seen over the past year or so is that for models to do stuff, they're much more effective when they can use a computer.

Right, okay, so now we're like, okay, we need the super assistant that can use a computer, or many computers. And now the question is, okay, well, how should it use the computer? And there's lots of ways to use a computer. You could try to hack the OS and use accessibility APIs, maybe a bit easier as you could point and click. That's a little slow and unpredictable sometimes. And another way, it turns out the best way for models to use computers is simply to write code. So we're kind of getting to this idea where, well, if you want to build any agent, maybe you should be building a coding agent and maybe to the user, a non-technical user, they won't even know they're using a coding agent, the same way that no one thinks about are they using the internet or not, which is they're more just like, "Is WiFi on?"

So I think that what we're doing with Codex is we're building a software engineering teammate, and as part of that, we're kind of building an agent that can use a computer by writing code. And so we're already seeing some pull for this. It's quite early, but we're starting to see people who are using Codex for coding adjacent product purposes. And so as that develops, I think we'll just naturally see that, oh, it turns out we should just always have the agent write code if there is a coding way to solve a problem instead of... Even if you're doing a financial analysis, maybe write some code for that.

---

## Sora Android app: 28 days, #1 app store, 2-3 engineers

Lenny Rachitsky (00:44:08):
What has the impact of Codex been on the way you operate as a product person as a PM? It's clear how engineering is impacted, code is written for you. What has it done to the way you operate and the way PMs operate at OpenAI?

Alexander Embiricos (00:44:24):
Yeah, I mean, I think mostly I just feel much more empowered. I've always been sort of more technical leaning PM, and especially when I'm working on products for engineers, I feel like it's necessary to dogfood the product. But even beyond that, I just feel like I can do much, much more as a PM. And Scott Belsky talks about this idea of compressing the talent stack. I'm not sure if I've phrased that right. But it's basically this idea that maybe the boundaries between these roles are a little bit less needed than before because people can just do much more. And every time someone can do more, you can skip one communication boundary and make the team that much more efficient.

We recently shipped the Sora Android app, and that was one of the most mind-blowing examples of acceleration, actually, because usage of Codex internally at OpenAI is obviously really, really high, but it's been growing over the course of the year, both in terms of now it's basically all technical staff use it, but even the intensity and know how of how to make the most of coding agents has gone up by a ton. And so the Sora Android app, a fully new app, we built it in 18 days. It went from zero to launch to employees, and then 10 days later, so 28 days total, we went to just GA, to the public, and that was done just with the help of Codex. So pretty insane velocity.

I would say it was a little bit... I don't want to say easy mode, but there is one thing that Codex is really good at if you're a company that's building software on multiple platforms, so you've already figured out some of the underlying APIs or systems, asking Codex to port things over is really effective because it has something you can go look at. And so the engineers on that team were basically having Codex go look at the iOS app, produce plans of work that needed to be done, and then go implement those. And it was looking at iOS and Android at the same time. And so basically it was two weeks to launch to employees, four weeks total. Insanely fast.

Lenny Rachitsky (00:48:31):
What makes that even more insane is it became the number one app in the app store. This just boggles the mind. Okay, so 28 days?

Alexander Embiricos (00:48:39):
Yeah, so imagine number one app in the app store with a handful of engineers. I think it was two or three possibly in a handful of weeks.

---
