# Mayur Kamat — Unconventional product lessons from Binance, N26, Google, more
*Theme: org-strategy-leverage | Extracted: 2026-04-03*

## Highest leverage problems and the moving desk metaphor

Lenny Rachitsky (01:06:32):
I want to come back to one piece of advice that we were chatting about before we started recording that I think might be helpful to people, which is, and this is kind in a different direction, but I want to make sure we touch on it, is Shreyas Doshi's point about leverage. I know this is something that you think a lot about. He has this really good advice and we'll point to the episode if people want to dig deeper around finding the highest leverage opportunities for you to work on as a PM. Can you just share that advice for folks that haven't heard this before?

Mayur Kamat (01:07:00):
This is true for no matter what level of career you are in, but you have a finite amount of time and largely you have more problems than you have time to solve them. The question is which ones you work on. And this becomes even harder, let's say you're a CPO now because all of them are important, otherwise they will not come to you in the first place. The question is, which one do you work on? And the principle is simple. You work on problems that have a 10X positive or a negative impact. I mean the number can be 10, 5, 300, depending on finance it would be a hundred, some companies might be three. And in most FinTech companies one of two problems, it's a growth problem or a compliance problem because both of them can have a negative or positive 10X impact and that's what you focus on. That's what you spend bulk of your time. What was interesting for me, my first executive roles, that was Google, I was a product manager.

I joined what was White Pages back then as a VP of product. I was my first kind of... And White Pages, Alex Allgood, Seattle, founding legend, three companies, all unicorns now. Incredible, very good personal friend and mentor. What was truly interesting when I joined it, they're like, "Okay, this is your desk, this is the product area. So we had two offices, this is when everybody worked in office five days a week." And I'm like, "Okay, where does Alex sit?" And he's like, "Oh, he's sitting with accounting." And I'm like, I didn't think about it because I thought his office is near accounting. Then I find out he doesn't have office, he has a floating desk. So all the other desks were fixed, but he had a movable desk and he would move his desk to one of the departments, which I think had the highest leverage opportunity. And he would sit there at that desk when that department till that either problem was solved or the opportunity was realized, and then he would literally move his desk and then go to product or tech or finance.

And that was his way of... You could literally visualize him working on the highest leverage problem by his desk moving. And then that combines that with what we talked before about details and a little bit, I think I didn't mention it about the humility that you need to have to be working in the detail. A lot of the times, especially later in your career, you're like, hey, this is beyond me. This is below me. Why do I need to do that? I have so many PMs or data analysts or somebody should do it. Why would I do it?

So again, he moved his desk to where that product team sat, and for the next three months he was the product manager on that scrum. So he would come to my product team meetings, give us update on what's happening with the SEO scrum, and then an hour later I would be in the leadership meeting giving my update to him, and truly he was operating it saying, this is high leverage area for the company, high leverage for my yards. It should be high leverage for me. I'm the best person to do it. I'm going to be in the details and do it. CZ, same at Binance, there were a lot of products that he would just sit on himself. There were very few people at Binance who would say no to CZ, but one of my lead PMs who worked on the products that CZ worked on, he would tell them no all the time. They would just baffle all the other executives, how is he saying no to CZ and none of us are doing it? Hey, that was his product area that CZ was working on, and there was that mutual respect there that, hey, we know this thing and he is going to say no to me because probably not a good idea. So that humility and attention to detail is required to work on the high leverage problems.

A lot of the high leverage problems are not, as I said, not strategy decisions. They're not language markets to go after and stuff. A lot of them are like, why is this thing not working as well as it needs to be? And a lot of time the devil is in the details and you need to be over there. I think combining that, knowing what is high leverage or not, and two, both having the humility and the patience to be able to go dig deeper and solve that.

Some of them are quick ones. Like if I'm looking today at, let's say how many of our signed up users convert into a long-term monthly daily active user, that could be something I focus on for a month. Because we're running a lot of experiments on early onboarding screens, early rewards, early incentives, early loyalty program, and at some point it might be like, oh, the team's got it. I've given all my... What I could do there. It's functioning. We have great PMs. I trust their execution on this. Let me just go focus on some of the compliance challenges that we have or fraud issues that we have in France.

Those kind of being able to kind of... The only way that works for me is I keep a very three calendar because you cannot do this without that. If you have hundreds of meetings, hundreds of one-on-ones daily standards, a lot of recurring meetings, you just can't find time to go work on high leverage problems. So that would be my kind of other stuff is you should have plenty of open spaces on your calendar. A full calendar is a badge of shame, not a badge of honor.

---

## Binance flat structure: daily leadership meetings and extreme ownership

Lenny Rachitsky (00:10:34):
Good grief. This idea of a flat structure, yeah, it's interesting, because I imagine that's not necessarily great for other reasons and then this idea of being in the details. Let me ask about that, actually. What does that actually look like? I think a lot of people, a lot of leaders are like, "Oh, yeah. I'm in the details, we should be in the details." What does that actually look like in real life at Binance?

Mayur Kamat (00:10:55):
Let me give an example. One of the areas, when I joined, one of the biggest product problem we had was, crypto before was fairly unregulated, so you could just sign up with an email address or even just a wallet and start trading. There was almost zero friction. Then it suddenly became regulated, where you would almost have a full KYC flow like a bank. That just meant that the conversion rate dropped from, let's say, 100% to 2%. Now we had to solve this problem. This was the daily meeting level problem. It's okay if you're operating in one country. You can do it easily. If you're operating in 200 countries where there's not even a standard for what a document acceptance criteria might look like, now you have a significantly larger problem. You cannot say, "Let's work with the KYC vendor and do the onboarding."

We had to, literally have this, the top 50 countries, the top 10 document types, this spreadsheet of basically 500 cells, the conversion rate at each level. Then we are looking at, okay, a passport in Kazakhstan has very low level of conversion. What can we do about that? Do we need a new vendor? Do we need better imaging technology? Do we need a new SDK from a vendor? Then we go cell by cell based on, let's say if I was running a typical product team, I would say, okay, let's just look at maybe the top 90 percentile of our users, but this was Binance and then CZ is like, "No user left behind. Even that one user in Congo is important because this is financial inclusion for them." Then all of those 500 sales matter, no matter how low their impact to the conversion rate is.

That's a little bit of Binance flavor there. It's extreme customer focus and it doesn't really matter. Customers are not a number. It's a person at the end of the screen and we care about them, so you would need to know, you would get questions like, why is the driver's license acceptance rate in Kenya falling suddenly? When you have, and that's just one piece of the problem in a large product with 80 different products. You, of course, cannot do it for every single product, but the concept of, what is the most leveraged decision you could be working on right now? If it is for your growth, it's the onboarding, then you'd better know exact every single screen of the flow, why is there a drop-off and what are your teams doing for it? That level of detail, and you just do it on different products at different parts of your journey.

Lenny Rachitsky (00:13:43):
I imagine there's people listening where they're like, there's the team responsible for the onboarding flow and the KYC flow of their product and it's so hard. They're like, oh, there's all these problems with our flow. Imagine that for 100 different versions of the flow across 100 different countries. Good God.

Mayur Kamat (00:14:01):
And documents. It gets very tricky. It gets very tricky, but we also had resources. At one point in time we said, we had a team of 20 people working on KYC and we said, "For the next three months, we want 500."

Lenny Rachitsky (00:14:16):
Which has its own downsides, too.

Mayur Kamat (00:14:18):
Has its downside, but if you're running in this extreme mode and you're less, not as worried about just the team's stress and personal development aspects of it, you're just purely looking at the execution of the product, there's a surprising amount of power that comes with it.

---
