# Nabeel S. Qureshi — How Palantir built the ultimate founder factory | Nabeel S. Qureshi (founder, writer, ex-Palantir)
*Theme: product-strategy-growth | Extracted: 2026-04-04*

## Customer problem becomes core platform feature — Airbus to Ontology

Lenny Rachitsky (00:32:36): Okay. Amazing. The example you gave of what you worked on at Airbus, you described it as basically a sauna for making planes. Is that right?

Nabeel S. Qureshi (00:32:44): Yes.

Lenny Rachitsky (00:32:45): So how much of that does becomes a part of this core product versus stays this one-off thing? Is it elements, that's a cool innovation, let's put that into Foundry. How does that work?

Nabeel S. Qureshi (00:32:55): This was a really interesting story actually. So the initial problem that we came into with Airbus was that they had a new aircraft called the A350 beautiful aircraft... their mandate to us was, "Okay. We need to ramp up production of this really fast," much faster than we've ever done it before. So it's like the numbers are very approximate, but it's like, "Okay. We're producing 4 this month, we need to do 8 the next month, 16 the month after, and so forth, and you are going to help us do it."

So we went in, scoped out the problem. There were a bunch of different things that we could build that helped accelerate this, but one of the basic problems that we figured out was that without getting too much into the weeds, the way the factory would work, is that there's a bunch of stations and you can think of the plane as literally moving between each station and then each station would do a certain set of work on it...

All that data was stored in SAP and SAP is like established software. It's good at what it does, but it's not the most user-friendly necessarily, especially if you're not an expert in how it stores data. The table names are very hard to understand and read. So one of the things we figured out was just if you can pull in these tables that may as well be written in completely alien language, the table name would just be like S3, F1_Z or something like that... If you could pull in those tables and join them in the right ways, and then just map them to human concepts that humans can understand, so things like a part a work order, an aircraft, et cetera, and basically build a hierarchy or mapping between them, then what you can do is, a user can just log in and say, "Okay. Aircraft 79, where is that?"

So the thing we built, I slightly flippantly described it as Asana. It's a little different. But basically that's what it did, was it gave you a unified view of, okay, this is what's going on inside the factory... Did this directly become a part of Foundry? Not exactly, because the way that other companies work is not going to be using this same set of concepts, but the overall idea of taking a bunch of tables, and then mapping them to human understandable concepts was a very powerful one.

So this actually resulted in a big piece of Foundry now, which they call Ontology. You've probably heard this term as you've seen... If you see Palantir presentations, they always talk about Ontology. This is what they actually mean by that, is it is a set of concepts that is understandable to you as a human and you are not having to go and dig around and do. You're just able to say, "Where is the aircraft now and where is it going next?" So the ontology became a huge piece of Foundry. It was directly informed by the learnings that we had from building that application inside that factory. And I would say it's still a very big differentiator today. I don't think too many other companies ship this kind of stuff yet.

---

## Retool: same product, different framing unlocked PMF

Nabeel S. Qureshi (00:44:48): In other scenarios, it's actually the right call to pivot and just put everything on that big problem instead and then go and find other customers for that thing. There's no hard and fast rule. I remember reading a really interesting post by, I think it was David Hsu from Retool who had this exact thing. I think he worked at Palantir for a while too. He said that they had the Retool product and it wasn't getting any traction at all. And then he tried an outbound email campaign where he literally just changed the subject line to build internal tools easily. And then suddenly they started getting all these replies from CTOs who were just like, "Yeah. This is actually a huge pain point for me."

But the exact same solution, they were previously framing it as, I think it was supercharged Excel or something like that, and nobody was biting. So they just changed the way they framed it and found a different set of buyers and succeeded that way. So yeah, no hard and fast rule, but I think it's always you need to have this matrix of options in your mind and be very deliberate about which one you are going with and why.

Lenny Rachitsky (00:45:53): I think your piece of advice is really important there. Usually in your experience, you're saying people index too far too? Like now, what they're asking me to do is not what I think they need or what customers will need. You're saying it's actually more likely they're right, and that's maybe where you should be focusing more versus this abstract vision and original idea you had?

Nabeel S. Qureshi (00:46:14): I think so, yeah. I think it's very hard to not be anchored to your own experience and your conceptions as a problem. And one thing I've seen in really strong founders is they're able to drop a bunch of those assumptions and almost treat a new opportunity as a completely blank slate. And then just figure out how to reshape things so that you're taking advantage of that, and that's how you don't get stuck at a local maximum.

---
