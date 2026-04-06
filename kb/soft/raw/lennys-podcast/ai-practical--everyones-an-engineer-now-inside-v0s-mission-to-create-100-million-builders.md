# Guillermo Rauch — Everyone's an engineer now: Inside v0's mission to create 100 million builders
*Theme: ai-practical | Extracted: 2026-04-03*

## Tips for using v0 effectively + live demo walkthrough

Lenny Rachitsky (00:36:42): Let's help people be successful with v0. And then let's also do a demo. But before we get there, let me ask you this. Imagine you could magically sit next to someone who's about to use v0 for the first time and whisper a tip in their ear to be successful with v0. What would a couple tips be?

Guillermo Rauch (00:36:59): Number one is you can be as ambitious as you want in terms of what you ask the tool. If you can steer the tool towards some kind of inspiration that you have, you're always going to get better results. If you don't have ideas on what to build or what to prompt, I would recommend using the v0 community so that you can find something to fork to get started. I would say in some ways, if you have technical skills, this one is interesting, have some suspension of disbelief. It humbled me, I was saying about accessibility. So be open-minded about whether the tool actually knows some things that you might not know, and so focus more on the product description, focus more on what do you want the end user to experience? What do you want the product to do? And try to be open-minded about how well the tool can implement it. Those would be my main wants.

You also have to have a sense of iteration, I guess. Think of it this way, if you were working with a design firm or an agency that you've hired, you will go back and forth and say, "Try something else." If you were coaching an engineer that's getting stuck in something, you would say, "Try something else." It's amazing how many times I've gotten unstuck in v0 by just saying, "Just try something else."

Lenny Rachitsky (00:38:35): Just saying that as the prompt, not even giving direct-

Guillermo Rauch (00:38:37): Just saying that. I mean, the chat is like- It's like, "Yeah." Like you have a one-on-one performance review with a tool. "Hey, way to talk, try something else. What you're doing so far is not working. And it's amazing." One fitness function that I'm keeping in my head is I really want to find the thing that it cannot build with v0. So as part of the v0 community, I have my own profile. We'll share the link with people. You can see six or seven things that I've built that I consider to be pretty impressive. So for example, I was flying from Tokyo to San Francisco. The internet was horrible. What I like to do during flights is I like to monitor our own flight while I'm on the flight. So I open Flightradar or whatever, and I was extremely bored as well.

And I noticed that Flightradar, I don't know which one it was, Flightradar, there's like four or five of them. They were very bloated. They had ads. They were not what I wanted the flight radar to look like. So I built my own during the flight with the worst internet connection that you could imagine in the world, integrated into a flight data API called Edge Aviation. So this is what I told v0, "You're going to build the best flight radar on the planet." I wasn't prescriptive at how, so it used a tool called Mapbox and a JavaScript library called Leaflet. I didn't tell him that, or her, I don't know, v0, what it is. And subsequently, once we cooked on the design, which looks, I would say beautiful, I then got more ambitious and I said, "All right, let's make it real now."

And by the way, that's actually how I would work. So it's how I like to work. I like to work experience first, and that's also how Vercel was built. "Let's start with the front end. Let's start with the planes on the screen." And by the way, there's a lot of subtleties, here. For example, there's so many flights going on at any given time that there's just too many. So I had to work with v0 on improving performance. And once again, I wasn't prescriptive. I just said, "We have a lot of flights, chief. Let's-"

Lenny Rachitsky (00:41:02): Did you say, "Chief?"

Guillermo Rauch (00:41:03): Yeah, I do say that a lot. And this is, I think when I shared it on X, it blew a lot of engineers' minds, because it created a canvas-based, canvas is the sort of underlying rendering surface that very sophisticated products use like Figma. And it created this awesome overlay on top of the map that can render tens of thousands of flights at any given time. And then I told it, "Let's make it a full stack application. Okay, plug into the flights' API." So that's an example of we cooked and there was no limit.

Lenny Rachitsky (00:42:00): And how much did this cost, how much time does this take to make something like this?

Guillermo Rauch (00:42:11): I mean, that one probably took less than two hours with the worst internet.

Lenny Rachitsky (00:42:24): And what did that cost? Like 10 bucks? What would you estimate?

Guillermo Rauch (00:42:24): I mean, I pay for the $20 v0 subscription.

Lenny Rachitsky (00:42:36): If you had engineers building this, how much do you think that would cost? How long do you think that would take?

Guillermo Rauch (00:42:36): I mean, weeks, easily. Easily.

Lenny Rachitsky (00:42:40): And that's like tens of thousands of dollars.

Guillermo Rauch (00:42:42): Maybe the most cracked engineer at Vercel could knock it out in ... without using any AI, could knock it out in a couple days. But then what about the design? What about me? Because I'm the bottleneck, not the engineer.

---

## AI equals software: v0 changing how teams work day-to-day

Lenny Rachitsky (01:22:38): How is AI changing the way they work? Is there anything there? Because I feel like you guys are the cutting edge of how products are built. What's happening? Is it just everyone's on Cursor and v0 to build stuff?

Guillermo Rauch (01:22:55): Yeah. Yes, but actually it's more profound. I think it's the, everybody can ship, it's the, we build with AI principles in mind. I actually give a shout-out to the Lumalabs engineer who said, "Well, I'll use AI for everything. I'll use AI also to generate the images for the website." And I'm seeing, for example, our designers that are working on our next conference generate all of the animations with video models. I'm looking at, our marketing team are creating demos of how the infrastructure works with v0 that are better than any static diagram or landing page that I've ever seen. One of my most viral xeets or X posts is something that one of our designers created, which explains how our compute infrastructure works with an interactive demo. And until he created that, by the way he designed, it and created, and we shipped it all in the tool, first of all, it wasn't part of his day-to-day job to do that.

v0 is making you such a powerful generalist that you can step out of your comfort zone of like, "Well, my job was to do only this." You can just create. We have a ritual every Friday, we had it this morning, called Demo Fridays. And so it's very important to create the space for people to step out of that comfort zone and use AI. So us giving permission to people to build and ship things is part of that cultural backdrop that makes these things possible.

We had a demo today as part of the Demo Friday of our VP of sales engineering also creating an amazing tool that he's going to use to help prospects understand Vercel with v0. So I've heard from DevOps and infrastructure engineers how much they use tools like Cursor to work on the low levels of the Vercel infrastructure. So I think very quickly we're seeing AI being embedded everywhere. I just heard a product request from a customer that was saying, "Okay, Vercel, you sell domain names. Let me come up with new domain ideas with AI." So I just see a future where AI becomes synonymous with software. I do look forward to it because we need to stop talking about AI at some point. I foresee, it's probably not going to happen, but it is useful to remind people that AI equals software now, and we are a software company. We build software, and we use software to build software.

Lenny Rachitsky (01:25:41): And AI is just a part of that.

Guillermo Rauch (01:25:42): Yeah.

---

## Programming translation tasks going away; what engineers should learn

Lenny Rachitsky (00:19:07): Let me follow the thread on engineers. A lot of people are wondering, "Do we need engineers in the future? What happens to engineers? Should I learn how to code?" Your long-time engineer thoughts for folks that are trying to decide the career for themselves?

Guillermo Rauch (00:19:21): Yeah, I think knowing how things work is the most important skill in the world. I foresee a lot of people becoming incredibly impactful in building and shipping amazing products, and building gigantic companies, and everything you could imagine, where a single person can do the job of a hundred different people in a hundred different specializations. Take the example of one skill set that's really important to build a front-end product is you need to know how to use CSS or Tailwind to style it. And once upon a time, I would hire people that were truly specialists in this task, the task of there's a Figma design or there is some kind of sketch, and translating that into reality because they knew really well how to manipulate layouts, layout code, box model code, we call it, and borders, paddings, margins, flex box, all these technologies for styling.

And notice, I actually use the word translation very intentionally, because the origin of the LLM or the transform architecture at least, goes as far back as the architecture for systems like Google Translate. They were generative LLM techniques, basically. That's how they cross that chasm of, remember when translating tools were horrible and then one day the problem was just solved? And I look at a lot of the programming jobs to be done that used to be specializations, that I think are going away, in a way, or the tasks to be done, they're translation tasks. We were translating from a screenshot, or intent, or a design into a React, and Tailwind, and CSS implementation.

And right now, v0 is incredibly good at doing that. It's so good that every time we put a new generation of the model out, I run this test of converting my own website and try to generate it with v0. Last time I did it, it had taken me like 10 prompts to replicate it. Keep in mind I'm an expert front-end engineer that's been in the arena since I'm like 10 years old and I'm 35 now. And so I do that test because it's almost like a test of self-imposed humility of, like, "I remember exactly how long it took me to build my website with Next.js, the framework that I created, and ship it." And so with the last model, it took me maybe 10, 15 prompts? With the most recent model, it took me two prompts.

And so that translation from the design intent into working implementation, another anecdote that I like to share with people is the model, because v0 tries to embed all of the best practices of the web, the model output more accessible code than what I wrote. It follows the accessibility guidelines that the web standards consortiums put out better than I did, because it just knows everything. And so those tasks where you can almost model it to a translation task, definitely going away. But knowing how things work under the hood, notice all the ... I'm using specific tokens in this conversation. I'm saying, "CSS," I'm saying, "Layout." I'm naming styles. Knowing those tokens is going to be very important for you because you're going to be able to influence the model and make it follow your intention a lot better.

And so the TLDR would be knowing how things work, the symbolic systems, and that will mean that you have to probably go into each subject with less depth. I have engineers at Vercel that know every single CSS property by heart. They know when they became available in a certain web browser, they've been tracking this specification. It's almost like you're an encyclopedia of knowledge of each CSS property. You probably won't need that in the future, and probably that's good, because you'll free up your mind for more ambitious things.

---
