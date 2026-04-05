# Howie Liu — How we restructured Airtable's entire org for AI | Howie Liu (co-founder and CEO)
*Theme: org-strategy-leverage | Extracted: 2026-04-04*

## Fast vs slow thinking team reorg

Lenny Rachitsky (00:18:55): What's a change you've made to help the company move faster and match that sort of pace?

Howie Liu (00:19:01): Yeah. I mean, we did do a reorg of the EPD org. So before we had ... we've gone through a few different reorgs over the past, call it, four years. The original state as we just proliferated, I think by default or incrementally, was that we had a bunch of groups that were each responsible for a feature or a surface area. So there was a group responsible for search within our table, and there was a group responsible for mobile experience and so on and so forth. And that has its benefits. Obviously, that team can go and get really ramped up on that part of the code base, that part of the product.

But it has the disadvantage of yeah, you tend to think incrementally when everyone's remit is actually a feature that they incrementally improve by definition as opposed to thinking about a mission or a outcome goal that might need to coordinate dramatic changes across a wider set of surface areas instead of just each one incrementally improving. And so, we reorged initially to basically different business units effectively... We did this recent reorg where now we have what I call the fast thinking group, which officially is called AI platform, but it really means we want to just ship a bunch of new capabilities on a near weekly basis. And each of them should be truly awesome value. You should drop your jaw, how awesome it is to use this new capability in Airtable. And then separately, we have the slow thinking group, and that's not meant to be better or worse. It's literally like you need fast and slow thinking in the common sense to operate as a human.

Lenny Rachitsky (00:22:12): I have that book behind me.

Howie Liu (00:22:14): Yeah, I love that book. But slow thinking it's like, it's just a different mode of planning and executing, right? It's like more deliberate that require more premeditation. We can't just ship a new piece of infrastructure that has a lot of data complexity like our data store HyperDB that now can handle multi-hundred million record data sets. That's not something you ship in a week in a hacky prototype. So we now have these two separate parts of the company, and I actually think what's really cool is they actually compliment each other very well, right? Because the fast execution, the AI stuff, that creates the top of funnel excitement that also inspires new use cases and new users to come to Airtable, including in large enterprise, right? Enterprises can use this stuff too. It's not just like a SMB thing, but the slow thinking basically allows those initial seeds of adoption to Sprout and grow into much larger deployments.

---

## Collapsing role silos across all functions

Lenny Rachitsky (01:09:25): Is there anything else that I missed there that you're like, you need to do this too to have a chance?

Howie Liu (01:09:25): I think just to really, really try to break down role silos, and I think that's true certainly for EPND in the typical EPD triangle, but I also think it's probably true even for non-product roles, right? I think it's true in marketing, right? Something I'm really pushing for in marketing and I think our marketing team is really leaning into actually is if you can just do all of the thing yourself ... traditionally how a marketing team might operate is like, okay, you have one person who's responsible for executing the performance marketing part of a campaign... I just think that in the same way that you can collapse the roles in EPD, and the ideal person, maybe they're very specialized and deep in one dimension like engineering, but they're well-rounded enough to be dangerous on the other two, I think that's kind of true in almost every other function, right? Sales as well, I think you should start to be able to play more of an SE role. Traditionally salespeople didn't necessarily know the product that well and relied on the SE to come in and be the product experts. I think it's really hard to sell any kind of AI product now without actually being fluent in the product and be able to demo the product, so AEs need to be SE fluent as well.

So I just think that that concept of collapsing roles, everybody needs to become more full stack to do the ... being more outcome-oriented, right? Your outcome as an AE is to convince customers of the value of your product and close deals, right? Okay, well, in order to do that, you used to have dependencies on having assets created by marketing and an SE to help you demo. Can you collapse more of those dependencies so that if you had to, you could do it all yourself, right? I just think it's a new operating mentality overall for every AI native company or company that wants to compete in this new arena.

---

## Founder mode vs delegation — the costs of fiefdoms

Howie Liu (01:13:02): I heard your interview with Brian Chesky and then later you talked about founder mode in that YC retreat, and the points there really, really resonated with me... I think when you're scaling up... you kind of have to be pretty versatile, right? All these decisions from a technical standpoint to design, to even commercial, and what's the freemium model going to be like?... They're all intertwined, right? You can't compartmentalize and then almost factory produce each of these things separately.

Then I think as you scale up, the default guidance that you often get from operational experts and larger scale company investors is like, okay, you got to industrialize the process of all of this stuff, right? It's kind of like going from a bespoke artisanal, one person made an entire item of clothing to we got to factory produce this thing, right? What that means in an organizational context is you then create these different fiefdoms, you hire all these execs and each exec just manages their own swim lane, and there's relatively looser coupling between all of those different groups, right?... I think what you lose is the magical integrative value of holistic thinking and making the bigger picture bets, right?

I think Brian talked a lot about this on his episode with you, which is like, look, in a company that is really serious about product, first of all, I really liked his point about the CEO has to play a CPO role, you have to care about the product. Ultimately the product is the thing and you can't just coast on scaling up go-to-market around the product forever, you got to keep innovating on the product. By the way, the best way to innovate on the product is not incrementally split over all these different little surface areas, but actually to have a bigger, more step function vision of how this product needs to make a leap.

---
