# Noah Weiss — The 10 traits of great PMs, AI, and Slack's approach to product | Noah Weiss
*Theme: ai-practical | Extracted: 2026-04-05*

## UI promise must match AI data quality; virtuous feedback loops

Lenny (00:19:32): Shifting a little bit. I know you guys have been working on a bunch of AI stuff at Slack. I believe you've been working on AI related stuff for many years. I think at Google you worked on a lot of AI related products. I feel like a lot of people are just getting into this and trying to figure out, "How do we integrate AI and ML and LLMs into our product and how do we not just waste our time chasing things?"

I want to ask you just in your time working with AI over the many years you've been doing it and share a little bit about what you've been doing there. What are some things you've learned about how to be actually effective and build valuable products and not just fall for the shiny object issue and trap?

Noah Weiss (00:20:11): I mean, it's almost 15 years ago now that I was working at Google in search on what later became called the knowledge graph. This idea of building a canonical repository of information of people, places, things in the world and relationships between them. Back then, it was a lot of the same ideas, but obviously the techniques. I have got a lot more mature.

We used natural language processing to extract all this information from the web and try to build this database of facts. An idea then was could you take queries, people have like, "What are the tallest fountains in Europe or what of the most popular beaches in Southern California?" Be able to actually give answers not just 10 blue links.

I think the thing that's really changed, it's super exciting in the last 6, 12 months with LMs and chat GPT and everything else is the idea that now you can take not just knowledge about the world but actually have natural language generation where suddenly the computer can talk back to you in a way that feels extremely human. Then the creative applications of that are pretty massive and exciting.

That's, I guess, the lineage there. I think from over the years back at Google at Foursquare, we did a lot of personalization and recommendations at Slack we have search and ML that's coming infused throughout the product. I think a couple things come out as ... I guess the principles that we've used over the years, back then at Google, one of the big ones, was that the promise of the UI has to match the quality of the underlying data, which is to say ... I think this is actually one of the failings of the various LMs right now is they all appear supremely confident even when they're completely hallucinating.

I think that's going to be something that people are going to have to work on a lot, which is to figure out how to be not so faultless, to acknowledge when you're not sure, because otherwise, it undermines the trust people have in the system. Using a lot of transparency about where the data comes from so people can actually build credibility and the tools is really important.

Then I think making sure that as you're designing the products that you have virtuous cycles that are naturally part of the product experience where you can get training data as a byproduct of people naturally using the software and then can make the model that you're building behind the scenes smarter, more accurate, more predictive.

A classic example of that would be Netflix back in the day, their rating system, they actually have a feedback loop from their customers then make the system better at predicting. I think people you are still trying to figure out what does that look like in this world in LLMs?

---

## Hybrid AI team structure: central infra plus parallel prototype squads

Lenny (00:25:12): On that topic, how do you think about creating teams within Slack and AI specifically? Are you recommending each team think about how AI can make their stuff better or are you dedicating, "Here's the AI team and they're going to work on stuff" and you guys just keep ship what you're shipping and keep moving your metrics?

Noah Weiss (00:25:29): I mean the unfair answer is a hybrid of the two, which is to say we have a central machine learning and search team. But a lot of people have expertise in this field to build infrastructure that everybody can use. What we've done is because the space is evolving so quickly, literally every month, the capabilities are evolving, the risks and tradeoffs are evolving a ton.

What we want to do is actually spin up a couple different teams that are focused on prototyping, using that common infrastructure but in specific directions that are all a little bit different. We've got a common ML, let's say in search team and now we have a bunch of teams that are working in parallel and different customer problems that we're trying to solve using that shared infrastructure.

I think this isn't the steady state. I think over time, what it'll probably look like is that all the existing product areas, as soon as we know more of the shape of what the technology is capable of will just have AI capabilities as part of their roadmaps. Just like every product team is responsible for their own mobile roadmap. They don't outsource it to someone else.

But I think today when things are moving so quickly, you actually want a little bit of a more ad hoc, flexible approach to move quickly and that's what we're doing.

---
