# Vijay Iyengar — An inside look at Mixpanel's product journey | Vijay Iyengar
*Theme: org-strategy-leverage | Extracted: 2026-04-03*

## Design-led phase: giving design breathing room to set architecture

Lenny (14:59):
I'm trying to think about being at a company that goes through this phase of, 'Hey, we're just going to build a bunch of stuff that we know we need.' And it feels like hearing it, it's like, 'Oh yeah, and then we're just going to make it all look great and connect and work well.' I imagine that wasn't planned, and I imagine that wasn't easy to get people to maybe slow down on just building more products and features or push it in a direction where it's all going to make sense. Can you talk at all about what that process was, how hard it was to shift from we're just going to knock through all this checklist of things to let's just bigger, let's slow down, let's spend a lot of time designing?

Vijay Iyengar (15:35):
It was definitely more messy internally than I described it. One of the key junctures was when we had this really talented design team and we were putting them on these very tactical projects that was, frankly, that was very engineering led, right? And design would often come in at the end and be asked like, 'Hey, can you just make this look nice and put some pixels on it?' And it's just such a waste of your design team to have them do that. But at the same time, the pace was so high that they didn't have time to come up for air and do anything else. And so there's actually this moment where I was an engineering manager at part of this.

And had a meeting with our BM and our head of design at the time, and we said, 'Hey, we can actually do the next three months of projects about any design,' which was a kind of controversial thing to say, 'but we're doing this so that you can take three months with a set of designers and go think about the system architecture of the product, and we'll wait for that to be done before we do any architectural things that might impact the architecture.' And I think that gave designers a bit of breathing room to go do that, just separating them for a bit from the tactical fire. Because what was happening instead was we would get towards the end of the project, bring design in, and they would use each project as an opportunity to squeeze in like, oh, and we can simplify here. And that's just a classic way to blow up scope at the end of the project because there wasn't a dedicated space for design led projects.

And I think that that was kind of a key friction point that we ultimately had to decouple for a bit, and then regroup and say, 'Okay, now we'll look what's our strategy,' and just take on projects purely for the sake of improving consistency, reach depth of our UX.

---

## Engineers reading raw customer feedback — no PM gatekeeper

Lenny (30:01):
You mentioned that you have a unique approach to keeping product teams close to customers. And I'm curious what you've learned there, what you found to be helpful and just kind of keeping product teams close to your customers.

Vijay Iyengar (30:15):
I think this is one thing that is something we invested in pretty early on at Mixpanel. Actually around that time, in 2018, when we refocused on our core product, one of our sales engineers, Aaron, built this automation where he piped all these customer gaps that we got that were reported by our customer success and sales teams, piped that into Slack and just a feed. And what this created was this culture where all engineers and designers could consume that raw feed of direct points of customer with no gatekeeper, no process to access it, no pre-aggregation, right? And I think this scale's pretty far. At a product team of our scale and with our reach of customers, we don't get so much feedback that someone couldn't read it in 20 minutes every day. And for four or five years in engineering, every day I would read all the gaps that we got, and many engineers would do that.

And one of the rituals that it's enabled is we'll find that engineers will go into that channel and react with a message with an email emoji, which means I'm going to email this customer and find out more, right? And they'll just email the customer and say, 'Hey, I'm the engineer that built this feature. I saw you said this specific thing. Can you tell me more? I'd love to understand.' They ask the five why's, and then they improve the product on their own. And I think that culture is just so important, and it just empowers all engineers and designers to think a PM a little bit, which I think takes a little bit of a load off on the PM to be the gatekeeper of all that information.

And then over time, we've evolved it quite a bit as our data stack stack's involved. So, we now not just take customer requests, but we take things that are posted on Twitter and NPS survey feedback and win loss notes from our competitive deals and pipe them both into Slack and into Notion so that we can both get the realtime feed, and then we can sort and aggregate and tag things accordingly. But the key artifact of this is that it's all open. There's no gatekeeper behind that process.

---
