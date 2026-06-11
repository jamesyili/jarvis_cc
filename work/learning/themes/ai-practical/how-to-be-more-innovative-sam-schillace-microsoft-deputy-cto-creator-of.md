# Sam Schillace — How to be more innovative | Sam Schillace (Microsoft deputy CTO, creator of Google Docs)
*Theme: ai-practical | Extracted: 2026-04-04*

## AI as platform — building software around models, not just features

Lenny (01:03:01): You're responsible for some of the cutting-edge work happening at Microsoft in AI. You're spending a lot of time in AI. I'm curious to get your take on just what you find interesting, where you think things are going, what people should know about AI. I'll share a couple of quotes that you put out somewhere that I have here that I think are cool. One is, "AI isn't a feature of your product. Your product is a feature of AI."

Sam Schillace (01:03:01): I love that one. Yeah.

Lenny (01:03:03): Another is, "It'll be possible to add some value by building AI into your product, but really transformative massive value will come from building apps and solutions that won't work at all without it, that treat it as a true platform."

Sam Schillace (01:03:14): Yeah, I think both of those are really true. So what I'm working on is, most of the industry right now is focused on, when you talk about somebody who's working in AI, it's somebody who's creating models, right? It's somebody who's figuring out how to do some new open source model or somebody who's doing some new training or make some model bigger. And I think that's very, it's valid, useful work. It's just not the kind of work I like to do very much. And a lot of people are doing it.

And so I'm an app builder, I'm a tool builder, and so I don't create models, I consume them, right? I want to build things around them. And so when I started with Microsoft, started working on GPT-4 with Microsoft in September of last year, my immediate reaction to it after picking my jaw up off the floor, which we were all doing in the early days, was, "Okay, this is cool, but in some computer science sense, it's just this function, this stochastic pure function that just takes a character array and rearranges it and hands it back to you. That's not much of a building block for building programs. We need state and we need control flow, and orchestration, and call-outs."

So that just started me down this rabbit hole of thinking about building the Semantic Kernel, which we built, and then building Infinite Chatbot, which was next, and these other projects we've been working on. And the more I think about this stuff, the more I do think those two quotes are good quotes. I think what's going to happen over time... I actually think we're at the beginning of this just gigantic disruption in the software industry. I think the way that the internet made distribution of information free, I think AI is going to make pixels free.

So pixels are expensive to produce now, they take programmers and they take lots of infrastructure, and putting a pixel in front of the user is a hard thing to do and lots of software is predicated on that. Lots of business is. The way lots of businesses were predicated on it being hard to distribute information 25 years ago. But you can see this already with things like just images, right? Two years ago, if you wanted a piece of digital art, you had to go invent Photoshop, learn to use Photoshop, use Photoshop to do the drawing, build the skills up. That's a lot of work to produce those pixels. Now it's like, I want a picture of a cat riding a bike eating a banana, done, right? So those pixels got really free.

---

## Future of software — intentional, dynamic, agentic interfaces

Lenny (01:05:28): And the similar things are happening in the business world as well...

Sam Schillace (01:05:28): And the similar things are happening in the business world as well, and I think it's just going to start to happen everywhere. So you can draw... This is what if, let's go ask some what ifs. So what if the models get really good at planning, so they get more independent, they can do longer and complicated things? What if the multimodal stuff gets really good so that they can both consume and produce dynamic UI like I was talking about? What if we figure out a good way to store state, this is my bots or docs thing. So what if do we figure out a good way for you to really highly personalize something so it knows you really well and you trust it with confidential information?

If you have all of those things, you're just going to spend a lot of time talking to that agent. It's like, what would you do... If you imagine you're the richest person in the world, you've got 100 of the best people working for you, and a chief of staff, and they're tireless, and they never fight with each other, they do everything you want. With that staff supporting you, what are you doing with software? What are you doing when you're sitting in front of a screen? Well, you're probably communicating intention and you're probably consuming some either entertainment or some of the products of that intent. And that's about it. You're not messing around with pokey static apps and stuff. That doesn't work, right? You're just telling your staff to deal with stuff for you.

So I think that's where we're headed, I think, in the world of software at least. Things are going to get more dynamic, more intentional, more semantic, more fluid, then more personalized. I think there's a ton of problems to be solved to make that vision real. But I think this feels to me a little bit like seeing the Palm maybe, or the early iPhone, where you're just like, "Okay, I get it. Phones are going to get interesting. That's a new device. Now we got to go do a whole bunch of engineering before they actually are as useful as they're today." Right?

So I get it. I think software is going to change radically now. I had the same feeling when we started doing... This is going back to G Docs again. It's another lesson. It's another one of these category shifts. The second we got Writely up on its feet and I was like, "Ah, the browser is actually a platform that you can actually build real apps in. I get it, the world's going to change." And we had a ton of stuff to do, right? Nobody really understood distributed systems. Nobody understood how to build stuff in multiple places at once or how you deal with replication, how you deal with security, all kinds of hard... All the development patterns had to shift from Waterfall, to Agile, to CI-CD, all this stuff had to change to fully realize that world.

---

## Multi-agent systems — whiteboard memory, debugger agents, self-documenting code

Sam Schillace (01:21:04): And we've done stuff like that in some of the things, the projects I've got going in Microsoft right now, we've got a chatbot thing we've been working on for a while and with memory, long-running memory so that you can have long conversations with it. And they work okay, but they don't work great in some ways. And we were trying to get multiple versions of them working together, like multi-agents working together. And we gave them whiteboard working memory as a shared working memory thing to fix this problem. And that turns out to make them much smarter. Don't know why. It just makes them smarter. So that was one of these nice little bits of discovery where if you're in a pessimistic frame of mind, you might've said, "Well, these don't work that well, let's give up on it." More optimistic frame of mind was like, "Well, let's try to give them a whiteboard just like a person and see if they cooperate better." And it turns out they really do. So another example of that mindset.

Lenny (01:47:59): [Later in the episode on the same thread] And then what goals are you picking?

Sam Schillace (01:45:49): I pick what I call north stars that I think are interesting, useful things to get to rather than just messing around. What's a cool thing that I think might be buildable with this?

So right now we're doing these multi-agent systems. We're trying to figure out how much independent work they can do without a person holding their hand. And so a nice domain to test that out in is programming, because you don't have a whole lot of... You just give something a Python environment and a file system and that's it and that's all it needs. And so you're not distracted by connectivity issues or whatever.

So one of the problems right now is go write the eye in Python. That's a problem I could give to an intern and it would take them a summer to do some halfway decent job of it. It's a thing you could expect a reasonably competent programmer to do, mostly independently. And so it should be possible for the system, if it's independent at all, to go do that. So is that useful by itself? No, because we already have the eye, it doesn't matter. But if we build a system of programming agents that can self-monitor and self-correct and bug themselves, that can build things that are roughly that scale of complexity, that's valuable. That would be a valuable thing to have.

It's kind of interesting too, because that system already, it's produced a bunch of good insights. One of them is its kind of complicated and then hard to debug it. It's this asynchronous system of stochastic agents. That's a lot of stuff to deal with. So we wrote a debugger agent. And debugger agent watches stuff, and when there's a problem somewhere, it goes and figures out what the problem is and then gives you a nice explanation of what you broke and what needs to be fixed. And we haven't turned it loose on actually fixing things yet because we don't trust it, but it's very helpful as an assistant. We had one that documented itself too. That's the other one we did recently. Just turned it loose on documenting the code base and did a pretty good job of it.

---
