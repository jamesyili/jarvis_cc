# Amjad Masad — Behind the product: Replit | Amjad Masad (co-founder and CEO)
*Theme: ai-practical | Extracted: 2026-04-03*

## Live demo: AI builds full-stack app in minutes

Lenny Rachitsky (00:10:49): Amazing, and that's why you're here. Let's do a demo. While you're pulling it up, you're going to share your screen and show us what this product can do. And the reason I am excited about doing a demo, and this is an experiment, kind of a new type of podcast episode I'm doing where we're diving into specific products and what they can do, I feel like there's so much talk about AI and what it's doing and people keep reading about, oh, AI can do this and AI can do that, and I feel like not many people actually see this stuff in action, especially the most cutting edge stuff. I think people are unaware of just how far things have gone and how much is actually possible, especially when someone that knows what they're doing is using the product. So I'm excited to show people what is actually possible and especially because this is going to impact the future of product management and product teams. So I'll turn that over to you. Give us a demo.

Amjad Masad (00:11:37): Awesome. So this is Replit's homepage. You can create what's called a Repl, which is a project. We have all sorts of languages. You can pick from really in the hundreds, but most recently, and this is how Replit became a thousand times easier, is you can just describe what you want to make. So you go on this home page, we have this text box, and you can write something like make me a cool app or what have you, but a more descriptive prompt is better.

Amjad Masad (00:14:50): So as you see, as the prototype is starting, you can see this progress pane where we can watch the AI doing its thing here. It's created a Postgres database. Obviously, when we're building a full-stack application, you need to be able to save things. This is one of the cool things about Replit. We have all these services, storage, database. So now it's coding, it's building the database schema. Now, it's building the home page, and it's actually quite fun and edifying to watch it build this, because you can really start to learn how to structure web apps.

Lenny Rachitsky (00:20:16): How long would you say it would take an engineer to build this? A typical engineer?

Amjad Masad (00:20:22): A few days, I would say to a week. I mean, if you're really good, it might be hours but it probably would take me a few days. I would say I'm like decent engineer, it'll take you a few days.

Lenny Rachitsky (00:20:40): And it took how much? 5 to 10 minutes.

Amjad Masad (00:20:43): Yeah, and it probably cost us something in the sense.

Lenny Rachitsky (00:20:50): Wow, in terms of compute.

Amjad Masad (00:20:52): In terms of compute, yeah. Probably, I would estimate it like 15 cents or something like that.

---

## AI computer interfaces — designing tools for LLMs not humans

Lenny Rachitsky (00:35:40): I want to talk about implications, but I want to come back to something you mentioned that is incredible that people may have missed. You basically built a computer specifically designed for the AI agent to use that is a different version of a computer specifically optimized for how AI wants to use a computer.

Amjad Masad (00:36:00): Yeah. So there's an entire discipline called like HCI, right? It's like how do you do that-

Lenny Rachitsky (00:36:07): Human-computer interaction.

Amjad Masad (00:36:08): Yeah. So now there are papers about AI computer interfaces and interactions. And so large language models are trained on large stacks of corpus from the internet, but they're still kind of alien creatures. So they're not like humans, so they have different behaviors. It's unclear what's the best way to give it an editor. So there's so many experimentation about what's the best way to give it a view on what's editing, how many files can you show it before it starts to hallucinate. And right now, it's more of an art than science, but it's becoming more and more like a science.

Lenny Rachitsky (00:36:55): This is insane. So it's a simple way to think about it. There's this foundational model, here's what I want you to build, and here's a computer to use to build it.

Amjad Masad (00:37:05): Yes. Here's a computer with a set of tools. Here's a tool to install a package. Here's a tool to edit the code. Here's the tool to run a SQL query and also services. Here's a bunch of services you can graph from. Here's a database service, here's an object source service, here's an auth service. So you can think about it as a bunch of external services, the computer with a bunch of tools, and they're all interfacing with the foundation model.

---

## Real-world AI use cases: PMs, marketers, sales engineers building with Replit

Lenny Rachitsky (00:25:05): So to follow that thread, what are you seeing inside of startups or even big companies in terms of how folks are already using this knowing this is the worst it will be and it will only become smarter and better these days? How are people actually using this that are say product managers or just non-technical people within startups or bigger companies?

Amjad Masad (00:25:26): On the SMB side of things, a lot of people are building kind of back office tools. So we have real estate agents that have a lot of data, have a lot of things they want to manage in their business that building a lot of these tools, that they otherwise would have to buy, but typically when you buy, it's actually not exactly what you need. And that's kind of the problem with SaaS, like one size fits all. And so a lot of people are seeing it as sort of a SaaS replacement for in-house tools and things like that. And then when you go to the bigger companies, it's anywhere from prototyping to actually production apps to tools as well. So we've seen product managers build, like I said, like a v1 of an app and actually go out and test it with users. I can't name the company, but there's a public company that have used Replit to test a v1 of an app.

Amjad Masad (00:26:35): And obviously after that sort of works, they take it to the engineers and they're like, 'Okay, we built this thing. We think it's a great thing. We test it with some users. Let's go actually put it on the roadmap and build it into the actual product.' So you are instead of unblocking product managers from having to need engineers for everything that they want to build so they can really build the v0 or v1 of the product. And that's super empowering for them. We saw it also with marketing departments like SpotHero has a head of marketing that actually can code decently well but use Replit to build these apps, and they built a competitive analysis application that looks at a competitor's pricing and makes sure that they're benchmarked correctly. And so it's a full stack app use database and everything and it runs on a continuous fashion. And we see sales engineers use Replit to spin up prototypes really quickly.

---
