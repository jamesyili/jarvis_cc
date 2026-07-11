# Vijay Iyengar — An inside look at Mixpanel's product journey | Vijay Iyengar
*Theme: product-strategy-growth | Extracted: 2026-04-03*

## Mixpanel's journey: focus, churn, and refocusing on core

Lenny (06:35):
So, I know it started as kind of a very simple product analytics product back in the day. And then as you do with ambitious companies, you look for more problems to solve... So as I understand it, you guys added a lot more products to the suite of Mixpanel products. And then I know that there are some challenges with scaling that, and maybe the products didn't stick as much as you're hoping... recently, you moved back to just the single core analytics product. And so I'd love to just hear that journey of what that process was like, what you learned as a product leader and as a company about scaling, expanding, trying to solve a lot of problems, and then coming back to one core straightforward problem.

Vijay Iyengar (07:15):
Mixpanel started in 2009 as provide product analytics to EPD teams... the first wave of explosive growth, because product analytics was a really burning problem at the time... And I think because we had this SDK that was installed in so many apps and we had this really scalable event collection and analytic interface, it was just natural to expand into a few adjacencies... The first one was messaging... The other aspect that we've added into was data infrastructure...

And what ended up happening was that by 2018, we had this big churn problem. We had something like 40% churn, revenue churn, our core product. And when we dug into, it wasn't that people were churning because they didn't need product analytics anymore. They had the need. They were just churning to competition because we were just not up to the market in terms of the features we had in our core. And when we dug into why that was, it was just that we had a 50% engineering team that was building products across three domains, product analytics, messaging, and data engineering stuff.

Our engineering team was just spread too thin to address all of those core gaps in functionality. And so we made a really hard call at the time. We said the hard no to those two other categories and decided to focus our entire engineering team on closing the gap on product analytics and innovating there. And from a process standpoint, how we operationalize this was we threw away all our planning and all the execution and that we work that we'd planned to do so far, and we did something very simple. We took all the churn reasons that our customer success and sales teams had been painstakingly collecting for years, grouped them by category, which was roughly product features we needed to build, sorted descending by ARR, took the top 10 things and made that our roadmap, just give every engineer direct access to customers and give them a bucket to go work on... in that first year we moved really quickly and we shipped something like a hundred features in that year and closed a lot of gaps.

So, we moved really fast shipping all these features and instantly saw the improvements to win rate and to retention... the end result of that phase, which is from 2018 to maybe late 2021, 2022, was our retention went from about 60% to 90%, and our NPS went from 16 to 50.

---

## Six-month planning cycles and anatomy of a bet

Lenny (19:51):
The first is just like, how do you plan? How do you plan? I know it evolves, but just how do you plan currently? How long are your planning cycles? How far ahead do you plan in detail? Do you use OKRs?

Vijay Iyengar (20:04):
We have these unsolved problems and analytics that we're going after. For us that's like, people always want more power, more simplicity, better data trust, faster onboarding, better collaboration, better price performance. And so we largely organize our teams around those problems and those missions. One quick aside there is that some of those problems have attention with each other. Power and simplicity, there's a trade off there, right? And we want one team to own both, so that they're kind of forced to confront that tension and beat that trade off.

In terms of planning, the way it works is that we plan on a six month time horizon... basically it started out with this strategy memo that our leadership team wrote that basically just conveys this is where we want to go as a company in the next year, and here's how the product team can contribute most of that and just established these key pillars. We shared that with the teams, and they took that and also combined that with all the quantitative and qualitative context they're constantly consuming about the problem they're working on and our customers, and ideated and developed the series of bets for the next six months, which I think are some extent similar to OKRs, where ABET... The anatomy of ABET is that it's problem we want to solve, our hypothesis on the solution, and then some plan to win, some plan to actually get there and a way to measure that you got there.

And I think one of the unique things that we did relative to other companies that do planning is... I think it usually is sort of this W process of there's the strategy memo, and then teams generate bets and there's a review, and then they go back and I iterate and then they finalize. And we kind of collapsed the middle part of the W where myself and our head of design actually spend time with each of the teams actually ideating on the bets and participating in the solution discovery process, going into the jam sessions and adding fig must keys ourselves with ideas and thoughts on things, which we did because we aren't a huge product team, and we are not going to do 50 things and a half. We're going to do maybe 10 to 12 things.

---
