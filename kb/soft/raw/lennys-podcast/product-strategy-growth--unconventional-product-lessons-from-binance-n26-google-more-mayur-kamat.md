# Mayur Kamat — Unconventional product lessons from Binance, N26, Google, more
*Theme: product-strategy-growth | Extracted: 2026-04-03*

## Strategy is overrated; hypothesis-to-data is the real game

Lenny Rachitsky (00:41:41):
There's so much there. There's I think an important point that I'll add, and I'm curious if you agree. A lot of new people or new people in their career, like, "Oh, I just want to think about strategy. I'm going to think about the big picture. I don't want to just sit there and optimize the roadmap and be in Jira." But it's actually, that's your job when you're just starting out. You need to earn the right to contribute to the vision, to the strategy.

Mayur Kamat (00:42:04):
There's one of the, and as a pre-conversation we talk about contrary and view, product strategy by definition seems like a... This is going to be controversial.

Lenny Rachitsky (00:42:16):
Great.

Mayur Kamat (00:42:17):
Not really... Those two words feel very at odds with each other for me. A product, you have hypotheses and if you can test it, you don't need a strategy. Right? If I say, "Hey, if I build this and I know this will add this much users and this time with this conversion rate, this customer acquisition cost and this LTV," that's your hypothesis and you could test it in the market very quickly. And if it works, you have your strategy. Keep doing more of it. Strategy is always keep doing more of it or don't do it, right? That's all that is to strategy. The key part is just figuring out which one goes in which bucket. And if you're really executing fast enough in a kind of structured, experimentation-driven manner, your strategy becomes a largely solved problem. So, for most, and that's a challenge.

A lot of people think strategy is about looking at Porter's forces, a lot of slides, we're looking at some data and slicing it and saying, "We need to go here or there." All of it is largely in some sort of package intuition. And the challenge with that is, usually you go with the loudest voice in the room. And if you're a junior in your career, it's a very frustrating exercise because you think you know the strategy better. But it's all it is. It's a sense of package intuition, and then the guy with the loudest, biggest title or the loudest voice is going to go do it. It was very early in my career, Jonathan Rosenberg, he was the head of, he was the CPO at Google.

All the PMs reported to him. He was not called the CPO back then. And he had this one thing he would say all the time that, "Come to me with data. If you come to me with ideas, we'll go with mine." Right? That was the saying. You can come with any ideas, we're just going to do what I think, but unless you come with strong sense of proof to override me. So again, strategy is a little bit overrated for product. For market expansions, for investments, for licenses, compliance, there's several areas where it makes sense and it's kind of useful. But for most product managers, your strategy should be, how fast can I go from hypothesis to data, right? The faster you can go there, the easier your strategy gets.

---

## Cohort-level data and compounding small wins at Booking.com

Lenny Rachitsky (01:01:13):
That tells you you really don't need from a strategy perspective to do something completely different if you can truly compound your growth by optimizing every single thing really, really well.

Mayur Kamat (01:02:02):
It's an incredible growth story. And that tells you you really don't need from a strategy perspective to do something completely different if you can truly compound your growth by optimizing every single thing really, really well. So there are the pros that come with, as I said, when you move, most of the time you're building products that are global, especially if you're based in the US. Very few times you're building product that just work in the US. Now, that's not true for a lot of the countries. Like in India, a lot of products are only designed for Indian market, a lot of products in China only designed for Chinese market, but from the US you're designing product for the world and a lot of the times you don't experience the same constraints or you don't empathize with the user at the same level because you just haven't lived that user's life.

Lenny Rachitsky (01:44:48):
That is certainly a hot take. So the idea here, I'm curious how you operationalize this with folks at N26. Is it just like, "I don't need to see a whole strategy for the year. Just give me, here's the plan, here's what we're going to test, here's our hypothesis?" Are you actually, what do you tell your PM team?

Mayur Kamat (01:45:05):
We use this tool. I'm going to give a shout-out to Statsig because they're awesome. Vijay used to run the experimentation at Facebook and has this tool. There's several of those. But if you're running proper experiments, I just look at the Statsig dashboards, right? And I'm looking at experiments, I'm looking at what metrics they're moving, I'm looking at the P-value, I'm looking at how quickly can they get to statistical significance. And I'm like, "Oh, this is working. Let's do more of these." Right? So, now there's some areas where you can't do it, like in compliance, in legal aspects, in Europe, especially pricing. In US, you can run pricing tests. In Europe, it's a little bit different. So, those areas, you would need to have a lot more kind of deeper thinking, understanding of your cohorts. You're coming up with more structured reason for why you should do it, but you can't really test and know within a couple of days or a couple of weeks at max whether this was a good idea or not.

Those, if there are either irreversible decisions or they're just extremely time-consuming to find out, then do some pre-work. We look at largely, find a lot of companies that really look at data without looking at cohorts that make completely bad decisions, right, because if you look at your dashboard as a mixture of users over 10 years, 20 years, even six months, and they all behave differently. If you look at a cohort level development of certain users, you generally end up making better decisions. But even over there, it's still lot more, there's a lot of noise between the moment you start tracking it than moment you start making decisions based on it. The world has changed in that meantime. By now, this was kind of a very foreign concept when I brought this in. I'm like, oh, the conversions down now, even though the product's done really well because Bitcoin has crashed, right?

Nobody wants to go sign up for an Exchange account. So, if you just measure pre and post, you would think that you have done something wrong in the product. If you measure it as an experiment, you would know that, yeah, between the variant and control, it's still doing great, even though overall conversion is down.

---
