# Tomer Cohen — Why AI is disrupting traditional product management | Tomer Cohen (LinkedIn CPO)
*Theme: ai-practical | Extracted: 2026-04-04*

## Full Stack Builder model: AI collapsing product development stack

Lenny Rachitsky (00:09:47): Wow. Okay. And there's so much here. We're going to be showing the visuals as you talk to help people see what you're explaining here. And all of this is very rational. If you have 15 sources of information, why not pull from it? Why miss out on that stuff? And what you're describing here is as you get more power and more specialized... It all makes sense rationally, but when you start to step back and look at this like, holy shit, it takes six months to launch one feature.

Tomer Cohen (00:12:03): Yeah. So we call it the full stack builder model. And the goal, always start with the goal. The goal itself is to empower great builders to take their idea and to take it to market, regardless of their role and the stack and specifically which team they're on. And the idea ultimately is to be able for that builder is to develop experiences end to end, to combine skills and expertise across what was traditionally distinct domains to bring it all together. And it's not a sequence of steps. It's really a fluid interaction between human and machine. That's how the way I see it. And then when you look back at that product development life cycle from the idea, the insight all the way to launch, the key trait that I'm emphasizing for builders is where I want them to spend their time is where I think great builders should shine in.

So the idea of vision. Coming up with a compelling sense about the future. Empathy, super critical, right? Having a profound understanding of an unmet need. Communication is critical. And we see this a lot in job descriptions right now for almost every role, but ability for you to align and rally others around an idea. Creativity, which for me is about coming up with possibilities beyond the obvious. For example, I don't think AI yet is great at creativity. I think it's kind of, in many ways, brings back the things you might not know about, but it's not the kind of next level creativity, which I think still humans are much better at.

And then ultimately what I think is the most important trait for a builder is judgment. Some people call it test making, but it's making high quality decisions in what is complex ambiguous situations. Everything else, I'm working really hard to automate. Really, really hard.

---

## Building LinkedIn's internal AI agents: trust, growth, research, analyst

Lenny Rachitsky (00:19:17): Got it. Okay. Oh yeah, Copilot. Microsoft. I get it. I get it. Okay. Okay. So that's the platform. So that's an investment that you guys have to make to make AI effective at building and doing all these things.

Tomer Cohen (00:19:17): And then you have tools. So tools is where you really build the agents. I mentioned I want to automate everything outside of those five trades that we talked about, and then we're building the tools for that. And then for that, actually very similarly, I can't just bring a tool from the outside and work. So I'll give you an example. One of our biggest things is building a trust agent. Trust is really important for us at LinkedIn. There's a lot of unique vectors which trust plays at LinkedIn doesn't place it anywhere else. So we need to bring all of that know how and context and information base into that agent. So we ended up building our own trust agent at LinkedIn.

Lenny Rachitsky (00:19:53): And so what is this trust agent doing? Telling you when you're maybe exposing information that you shouldn't be?

Tomer Cohen (00:19:58): So when you build a spec, you build an idea, you walk through the trust agent and it'll basically tell you what are your vulnerabilities, what harm vectors potentially you're introducing or will be introduced as a result of that. And I had our head of trust build it. So the head of craft for every area is building their own agent. As an example, we have one of our features for job seekers is called Open to Work. If you're looking for a job, you can put an open to work.

Lenny Rachitsky (00:20:24): Yeah, a little green loading thing on the circle.

Tomer Cohen (00:20:25): Exactly. And actually it's a great signal. I've seen some great success from it. People are helping each other. The community really thrives around helping each other. But at the same time, it introduces a trust vector for bad actors because they're open to work. People who are looking for a job are potentially more vulnerable to scams than other folks. So being able to think about how do we prevent all of those ahead of time. So we walked that spec from a couple of years ago through the trust agent. Not only was it able to find all the stuff we initiated at the beginning, but all the holes that we did not catch until later. So that's a great example of something that actually worked really well.

That's one. The other one is a growth agent, as an example. Again, LinkedIn has a very unique... Actually, we have an incredible growth team, growth process. We've kind of funneled all of our unique loops, our funnels, our tests of the past, everything into this growth agent, and now you can basically rock your respect for it, your idea for it. And it would not just allow you to do it better. It would actually critique how good is your idea. This is something you cannot bring off the shelf. It's very unique to LinkedIn. So we had to invest dramatically in it. And one team which is using it right now, which is almost... I wasn't thinking about it at the beginning, but our UXR team, our UER team, the user research team is usually using that growth agent to understand out of all the things that are basically surfacing for members, which one has the biggest growth opportunity to have the biggest impact? That was not in the cards when we thought about that idea, but teams are basically funneling those ideas into this one.

An example is our research agent. So research agent basically is trained on the personas of our members. You can think about a small business owner, a job seeker and so on. And it's using not just world knowledge, it's using all the research we've done in the past, all the support tickets coming in. So it's pretty good at understanding that persona at LinkedIn. So one examples we had is a team came out with a spec. They weren't aware we had the research agent yet. I asked the research agent for a small business owner, wanted to think about the marketing spec we had, and it critiqued it extremely well. Actually, in many ways shifted the direction of the team to focus on other integrations tools we can focus on, but it's very hard to have that visibility all to all that corpus of knowledge inside of the company.

That's another example. We have an analyst agent trained on all how you basically can query the entire LinkedIn graph, which is enormous. And instead of relying on your SQL queries or data science teams, you can use the analyst agent. All of those I would say are, I would call them still MVP+. The goal for us in the next couple of months to basically roll them out externally. Externally, I mean, internally at LinkedIn.

---

## Critical lesson: don't give AI access to everything, curate golden examples

Lenny Rachitsky (00:28:54): Yeah, that makes sense. There may be just like a researcher with a strong opinion about something that you disagree with and it wouldn't know. It's like, oh, of course, this is data, this is fact.

Tomer Cohen (00:29:03): Exactly. And then it doesn't always understand ties to original specs to success. You have to actually build... This is a really interesting way. When you think about how you bring those tools in, you can't just bring them in. You have to know what you feed them with. And what you feed them with is not just access. I see a lot to just focus on the connectivity and integration and it reminds me of the... This is almost like, this is actually more than 10 years ago when I was co-rebuilding the team, co-rebuilding the feed at LinkedIn and we started from scratch and I had to literally sit down and filter through examples of what is a good professional post on LinkedIn and what is not. And this was like weeks of work getting up that golden sample of examples, but it wasn't... The most important part was feeding at the right data, not all the data.

So it requires work. This is where I would say for many companies who are thinking about this phase, and I do a lot of sessions today with CPOs and COs on this process. You have to put this initial work to get the gains after. When I think about it, I think there's a takeaway there in generally with AI, even if you're learning it for the first time and so on, whether it's Cursor or whether it's design, if it's Figma or other tools or Lovable, you should be ready to invest those hours before you start seeing yourself pick up in velocity and quality, which will come up, but you have to invest that time.

---
