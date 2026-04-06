# Ronny Kohavi — The ultimate guide to A/B testing | Ronny Kohavi (Airbnb, Microsoft, Amazon)
*Theme: product-strategy-growth | Extracted: 2026-04-04*

## Email campaigns: lifetime value vs. short-term revenue

Ronny Kohavi (00:33:16): The other thing is you can just build models that use some of our background knowledge or use some data science to look at historical... I'll give you another good example of this. When I came to Amazon, one of the teams that reported to me was the email team that it was not the transactional emails when you buy something, you get an email. But it was the team that sent these recommendations. "Here's a book by an author that you bought. Here's a product that we recommend." And the question is, how do we give credit to that team?

And the initial version was, whenever a user comes from the email and purchases something on Amazon, we're going to give that email credit. Well, it turned out this had no countervailing metric. The more emails you send, the more money you're going to credit the team. And so that led to spam. Literally a really interesting problem. The team just ramped up the number of emails that they were sending out, and claimed to make more money, and their fitness function improved.

So then we backed up and then we said, "Okay, we can either phrase this as a constraint satisfaction problem. You're allowed to send user an email every X days or," which is what we ended up doing is, "Let's model the cost of spamming the users."

What's that cost? Well, when they unsubscribe, we can't mail them. So we did some data science study on the side and we said, "What is the value that we're losing from an unsubscribe?" And we came up with a number, it was a few dollars. But the point was, now we have this countervailing metric. We say, "Here's the money that we generate from the emails. Here's the money that we're losing on long-term value. What's the trade-off?" And then when we started to incorporate those formula, more than half the campaigns that were being sent were negative.

So it was a huge insight at Amazon about how to send the right campaigns. And this is what I like about these discoveries. This fact that we integrated the unsubscribe led us to a new feature to say, "Well, let's not lose their future lifetime value through email. When they unsubscribe, let's offer them by default to unsubscribe from this campaign."

So when you get an email, there's a new book by the author. The default to unsubscribe would be unsubscribe me from author emails. And so now, the negative, the countervailing metric is much smaller. And so again, this was a breakthrough in our ability to send more emails, and understand based on what users were unsubscribing from, which ones are really beneficial.

---

## When to start A/B testing: user count thresholds

Lenny (00:26:28): You talked about how you may be too small to run A/B tests, and this is a constant question for startups is, when should we start running A/B tests? Do you have kind of a heuristic or a rule of thumb of, here's a time you should really start thinking about running an A/B test?

Ronny Kohavi (00:26:42): Yeah, a dollar question that everybody asks. So actually, we'll put this in the notes, but I gave a talk last year, what I called it is practical defaults. And one of the things I show there is that unless you have at least tens of thousands of users, the math, the statistics just don't work out for most of the metrics that you're interested in.

In fact, I gave an actual practical number of a retail site with some conversion rate, trying to detect changes that are at least 5% beneficial, which is something that startups should focus on. They shouldn't focus on the 1%, they should focus on the 5 and 10%. Then you need something like 200,000 users.

So start experimenting when you're in the tens of thousands of users. You'll only be able to detect large effects. And then once you get to 200,000 users, then the magic starts happening. Then you can start testing a lot more. Then you have the ability to test everything and make sure that you're not degrading and getting value out of experimentation. So you ask for rule of thumb, 200,000 users, you're magical. Below that, start building the culture, start building the platform, start integrating. So that as you scale, you start to see the value.

---
