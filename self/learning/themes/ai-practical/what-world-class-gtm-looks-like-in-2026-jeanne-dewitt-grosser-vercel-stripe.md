# Jeanne DeWitt Grosser — What world-class GTM looks like in 2026 | Jeanne DeWitt Grosser (Vercel, Stripe, Google)
*Theme: ai-practical | Extracted: 2026-04-04*

## GTM engineer role origin story at Stripe

Lenny Rachitsky (00:11:23):
Amazing. Okay, let's follow the thread on this go-to-market engineer, so what was it like before and what are these engineers doing at companies?

Jeanne DeWitt Grosser (00:11:33):
So I think maybe an interesting story to tell. When I was at Stripe, we went to launch an outbound SDR function. So outbound prospecting and Stripe always ran lean. The company at that time had an operating principle which was efficiency is leverage. And so if you looked at the sales organization I was running, most companies out there probably would've had 30 SDRs and I was going to get four. So there's no way I was going to do the typical SDR approach and be successful. And so we thought to ourselves, okay, what can we do? We'll be super data-driven. And so we went and we started building project Rosland. Rosland is the scientist who originally mapped A-DNA. And what this was was effectively a company universe. So you can think of this as a massive database. Every row was a different company on the planet and every column was an attribute about that company that would help you sell to them in a more targeted fashion.

So at Stripe an example would be knowing that their business model was a marketplace was super helpful, because that would mean you wanted to sell Stripe Connect versus vanilla payments. And so the goal was basically, hey, can we create a mad Libs where I will come up with sort of a predefined email template, but 80% of it will be fill in the blank based on the different attributes of that customer. So if they're this industry or this business model, then pull this customer, reference this value prop, send it to this persona, not that. And we were trying to do this in 2017 and it was very hard and didn't actually totally work our ability to the false positive rate and we worked deeply with DSI and it just never really got there. And now that we're literally redoing here at Vercel as we speak and it actually works and you can bring AI to bear on it.

And so what's different is we now, I have a data scientist just like I did back in 2017, but I have a go-to-market engineer whereas before I just had someone in systems that was helping me configure outreach or sales off and my go-to-market engineer is helping me build an agent where we're coming up with, okay, well what's the human workflow that you would've done? And then how do you encode that using Vercel workflows as an example in actual code that's both deterministic and less so where an agent's going out and trying to replicate what a human might've done to produce that, fill in the blank, matlit.

Lenny Rachitsky (00:14:21):
I love the ambition of that project. What is this, like eight years ago?

Jeanne DeWitt Grosser (00:14:25):
Yes.

Lenny Rachitsky (00:14:26):
I love the big thinking there. We're going to map the entire universe of companies and then here's how we sell to them. And then just I'm trying to picture doing that without AI. It's like crazy to imagine trying that without AI and that's so much simpler to even imagine.

Jeanne DeWitt Grosser (00:14:38):
Well the thing that's amazing about that, just to geek out on a second, so I was working on that with a bunch of folks at Stripe on my team, obviously at a gentleman named Ben Salzman who went on to go to ZoomInfo and then actually recently just founded a go-to-market startup that is basically sort of productizing that concept of a company universe and then layering AI on it on top of it. And ultimately his view is actually AI will get to the point that you won't have to do outbound prospecting because it will just sort of company and product match. So it's fun to sort of see back in 2017 some of the folks doing that now work at OpenAI, they work at Anthropic, they also are doing GTM Eng. You've got him starting a totally AI native GTM company and then here I'm at Vercel trying to do the same.

---

## Lead agent reduces 10 SDRs to 1 at Vercel

Lenny Rachitsky (00:18:51):
Our processes all always have human in the loop. And so basically where we'll start is we take a go to market engineer and we have them shadow the highest performing individual in that function. And so you can go and you shadow an SDR and you can see, oh wow, they've got seven tabs open. They're looking up the person on LinkedIn, they're reading about the company, they're doing chatGPT on this, they're looking in this database to get these sets of attributes. And so that's how you sort of inform the initial workflow. And then what we do is we let the agent make a call. So in the specific example with inbound, you have to determine whether or not you think the lead is likely to be qualified and then you have to determine what to say to it. And so we'll let the agent make those two calls.

Jeanne DeWitt Grosser:
It ultimately then does some deep research, pulls in a bunch of information from our databases and crafts a response, but we have a human review all of those and actually hit send. Now for us, we had 10 SDRs doing this inbound workflow and now we just have one that is effectively QA-ing the agent. The other nine we deployed on outbound, so we got to move them up the value chain. At some point I think we'll get to a place where we feel like, "Hey, the human reviewer is saying yes enough of the time that we feel confident that these will be on brand targeted, et cetera," but right now we're still trying to train the agent and it incorporates feedback on what we choose to reject, edit, et cetera.

Lenny Rachitsky (00:20:31):
And you shared that it's already having a lot of impact. Like you said, you had 10 SDRs and now one can do the job of 10.

Jeanne DeWitt Grosser (00:20:39):
So before we did that move, I mean the other thing that's just incredible about this is the person who built the lead agent was a single GTM engineer. He spent maybe 25-30% of his time on this. It was six weeks before we felt confident going from 10 to one. So it wasn't like this was a multi-quarter process, it actually moved super quickly and then again now we just sort of keep that agent manager working with the agent to get it to a point where we say, "Hey, we're ready to roll." Actually throughout the process we also tracked all of the KPIs that you typically would hold an SDR accountable to. We were looking at our lead to opportunity conversion rate, we're looking at the number of touches it takes the time to convert, and basically what we were able to do is hold that lead to opportunity conversion rate flat. So the agent is as good as our humans were, but it's actually condensed the number of touches it takes to convert because it's so much quicker at responding relative to leads inevitably sitting in the queue or coming in at nighttime and no one can get to it, that type of deal. So that's sort of when we knew it was ready to pull nine people off and shift them into outbound.

---

## Deal-bott: AI reveals what humans miss in lost deals

Lenny Rachitsky (00:34:33):
Zooming out a little bit in terms of you mentioned tools and tools that you use. I'm curious just what are kind of the state of the art tools within the go-to-market stack that you love that you'd recommend?

Jeanne DeWitt Grosser (00:34:33):
Well, so I'm going to have an interesting answer to this, so I'll give you one. And it's not state-of-the-art per se, although I don't mean that disparagingly, it's just that it's been around for a while now and a lot of folks use it, but I think Gong has gotten just meaningfully more interesting in the last year. And then second half of my question I will get into, I think the calculus on build versus buy is changing. So all right, Gong. Gong is incredible because you can run agents against it now. So we take all of our Gong transcripts and we dump them into an agent called the deal-bott, and that deal-bott then can do a bunch of things. So the first thing we had it do was lost opportunity review. So we had just finished Q2, we had a list of our top losses for the quarter sorted by deal size, and we ran it against that and it was incredibly interesting.

So the biggest loss that quarter according to the account executive was lost on price. And when you ran the agent over every Slack interaction, every email, every GONG call, it said actually you lost because you never really got in touch with an economic buyer. And when you talked to somebody about ROI and total cost of ownership, it was clear from their reaction that they didn't really buy your mass. And so really the reason we lost was an inability to demonstrate value, which upon reflection I've got work to do to build out how we quantify the value of Vercel, which actually is very easily quantifiable. It's one of the things I love about selling this product, but we got to codify that for the go-to-market team. So that was incredibly interesting and now we run it against all of our lost opportunities and actually do a much better job of categorizing why it was we really, really lost.

And then either feeding that back into the engineering team or back into marketing sales leadership on, hey, where are we falling short in the sales process? And so that was awesome, but then we're like, well, it's not very fun to lose, so why don't we pull that forward? And so we went from lost bot to deal-bott and now the deal-bott is running in real time and we basically feed insights into Slack. Vercel is incredibly heavy users of Slack, so we have a channel for every single customer, either opportunity or existing one. And so now we're feeding insights into that Slack channel which is, "Hey, you're this far into the sales process and you haven't talked to an economic buyer, you should think about that." Or, "Hey, you just got off that call with an economic buyer, didn't sound like it went that well. Here's some things to consider and how you might follow-up."

And last thing before I pause, the other thing that's really interesting and how we're using this too is we are in this moment where I have never seen an iteration velocity exists now in my career. My 20 plus year career has all been in tech. And so for go-to-market teams, that's really hard. If you are launching something every other day, the ability to be enabled on that is actually quite challenging. And so this bot agent is now also letting us, where we're starting to go with it is we'll release something, we'll do our best to enable the team, then we'll go run the agent across calls, interactions, and we'll diagnose where we did a bad job of objection handling, where we're getting stuck. And then at the end of the week we can have a huddle and say, okay, what are all the places that our agent would suggest we aren't selling effectively? And then almost like an engineering team, we'll now run sprints, which is like those are just bugs. They're bugs in your go-to-market process, so you should not have them. And by the next week we're going to add content to our objection handling to guide. We're going to add content to a discovery guide, we're going to figure out something we need to change about our demo, so on and so forth.

Lenny Rachitsky (00:39:00):
Jeanne, you're blowing my mind in so many ways, it just sounds so fun and just you guys are going to win is what I'm feeling when I hear all this. Incredible. What I love about this is this AI tool, this agent you built sees things that humans were not seeing. The fact that you were surprised of just like this is a completely different conclusion is such a big deal. This is the whole promise of ai, it's going to do things we aren't even thinking about or capable of.

Jeanne DeWitt Grosser (00:39:26):
It is. We had a really interesting, one of the things we're doing at Vercel, we have an AI cloud, so people use that to put AI-native features into their customer-facing applications, but they're also using it to build internal applications to improve productivity or outcomes. And we are talking to a very large airline and that airline obviously gets tons and tons of support queries. So of course they would want to go apply AI to hey, how can we have AI answer these so that our cost to support goes down, sort of the obvious thing. But the more interesting conversation was actually with one of the C-level executives who said, we also actually transcribe every single one of those support calls. And so what I really want to know is why are they calling and how do I make it so that fewer people call the next week? And so again, this is now with AI, you can rapidly go through all of that content and actually be able to much more quickly than having a human in your CRM sort of pick some status why it was that folks were calling the airline this week and what if anything you can do to make it less the case next week.

---
