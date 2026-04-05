# Howie Liu — How we restructured Airtable's entire org for AI | Howie Liu (co-founder and CEO)
*Theme: ai-practical | Extracted: 2026-04-04*

## CEO as heaviest AI user — inference cost as signal

Lenny Rachitsky (00:13:48): And I feel like you're describing exactly, hourly,

Howie Liu (00:13:51): Literally hourly, or you could even have a measure of inference costs, right? Like the equivalent underlying inference compute cycles, right?

Lenny Rachitsky (00:14:02): How many tokens you use?

Howie Liu (00:14:03): Yeah, I mean, I'm proud to say I am pretty sure I'm still the ... I just checked this recently, but I take pride in being the number one most expensive in inference cost user of Airtable AI, not just within our own company, but I think for a long time I was globally across all our customers vault. I mean, I'm extremely intentionally wasteful. Wasteful in the sense of I'll do something that costs maybe hundreds of dollars of actual inference costs. For instance, doing a lot of LLM calls against long transcripts of let's say, sales calls to extract different types of insights like here's the product apps, identify or here's summaries, et cetera.

And we also have now a capability that's basically like an LLM map reduce. So effectively, even if you can't fit the entire corpus of content into one LLM call, because the context window limitations, we'll map through all of this content and break it up into chunks and then perform an LLM call on each one and then perform an aggregation LLM call on those chunks. Very expensive, because you're basically running a highly expensive model against a lot of data and then running it again on the aggregates of that. But for me, hundreds of dollars spent on this exercise is trivial compared to the potential strategic value of having better insights.

It's as if a really, really smart chief of staff has gone through and read every single sales call transcript that we've had in the past year and giving me very astute product insights, marketing insights, kind of positioning insights and segmentation insights. That's invaluable. You could pay a consulting firm literally millions of dollars to get that quality of work. So to me, I still think the value versus the actual cost of AI when applied greedily but smartly, it's a crazy ratio. And more people should be aggressively throwing compute cycles at these very high value problems.

---

## Play as a learning methodology for AI tools

Howie Liu (00:47:02): One is really, really, really stressing this idea of go play with this stuff. And I mean, when I say play, I really mean play in the psychological sense of there's a difference when you go in and you're kind of just trying to check the box and get a job done. There's a difference when you come in with a curiosity and you're kind of exploring, right. And it's both more fun and energizing, but also, I think you learn more through that. And so I've really tried to stress the value of play with these AI products.

And I kind of try to lead by example, by literally going and sharing out links or screenshots of the things that I'm doing in these various products. So, as an example, I will go into one of the prototyping tools and show, 'Hey, I built a marketing landing page for this new capability we're launching.' I created a landing page for it in Replit, let's say, and now I'm sharing that link... really trying to encourage everyone to go and just play with these products. And I've even said, 'Look, if anyone wants to just literally block out a day or frankly even a week and have the ultimate excuse, you could use... you could say that I told you to do it, right. If you want to cancel all your meetings for a day or for an entire week and just go play around with every product, AI product that you can find that you think could be relevant to Airtable, go do it. Period. So I think that's the most important thing is this play, this experimentation.

I think there's also a lot of other kind of shifts in how we execute prototypes over decks. I want to see actual interactive demos because, again, it's hard to... In a deck or in a PRD, you could say, 'Okay. Well, we're going to make Omni really good at handling this kind of app building.' Okay, those are just words. The real proof is in the pudding of like, 'Okay, let me try it out on a few realistic prompts that I can imagine.' And in a demo, in a real prototype, you can instantly try it out on unrealistic rather than golden pathy scenarios and see how it feels too.

---

## Vibes before evals — open-ended discovery first

Lenny Rachitsky (01:03:33): There's one more skill I wanted to talk about real quick. This comes up a lot in these conversations is evals. The power of getting good at evals, I know that's something you value highly. Talk about just why you think this is something people need to get good at.

Howie Liu (01:03:50): Yeah, and I listened to your episodes with [inaudible] and Mike who talked about this. I think it's interesting that both heads of OpenAI and Anthropic have converged on this point. I mean, look, I think I would add a slightly different or additive take though, which is I think for a completely novel product experience or form factor, you should actually not start with evals and you should start with vibes, right? Meaning you need to go and just test in a much more open-ended way, like, does this even work in kind of a broad sense?

So as an example, for our custom code generation capability, instead of defining evals that get repeatably tested as you vary the prompt or the model or the agentic workflow used to generate these outputs... I would first start with a much more open-ended and ad hoc style of just throw stuff against the wall, try different prompts and see how well it does.

To me, evals are more useful, A, once you've converged on the basic scaffold of the form factor and you kind of know what are the use cases you want it to work well for and what you want to test against it. Whereas in the early days, especially if your product market fit finding either for an entirely new company or for a pretty dramatically new or bold new capability... I think you have to just be a little bit more creative initially and throwing stuff at it, seeing what works... I kind of think it's more useful as a way to iterate your way to improvement, and you can start really testing stuff empirically, right? You can A/B test, especially if you have the scale of a really large product like Anthropic or OpenAI... but I think early on you don't have that luxury and you're in a much more open-ended discovery process.

---
