# Ramesh Johari — Marketplace lessons from Uber, Airbnb, Bumble, and more | Ramesh Johari (Stanford professor)
*Theme: org-strategy-leverage | Extracted: 2026-04-04*

## Experimentation incentives create risk-averse incremental culture

Lenny (00:52:42):
I wanted to come back to this idea you're sharing of maybe you should run experiments more quickly, not wait for stat sig, have a culture of learning versus impact. In practice, it's very difficult, because people are measured by impact. There's performance reviews, there's promotions, there's how much impact did this team drive, are going to look at their experiment results? You've worked with a lot of marketplace companies, a lot of different companies. Is there anything you've seen about something you could do to help the company shift and actually work this way, while also recognizing success, and who's doing great, who's not, which team's driving impact, who's not?

Ramesh Johari (00:53:22):
Interestingly, it's actually an active area of research for me now. What I mean by active area of research is I care a lot about the incentives that we create for data science through how we set up reward mechanisms. So there's a couple things I think that could be helpful, that are maybe there may be a little bit less about... I think there's a cultural issue here that's really critical.

One of the things I often find is that my PhD students, our PhD students here often go off and get great data scientist jobs. And in one sense, they're doing amazing stuff. They apply really technically sophisticated methods. But when I look at the problems they're working on, they're often more at the margins of the business than they should be.

And it's a cultural thing. It's basically because if you're measured narrowly on impact and that's all anyone sees around you, then it's very hard to engage with the creative aspect of business change and the strategic aspects of business change.

So the cultural aspect there is, I think it's partly incumbent on the leaders to expect something more of their data scientists. And what I mean by expect more is that you expect them to do more than deliver narrowly defined, statistically rigorous results to you in their reports. You're actually expecting them to talk also about what they're learning about the business in the process. So where that's headed is there's this concept of being hypothesis driven, which is like the technical phrase. What does that mean? Again, in a more lay sense.

What it means is tests aren't going to be defined only in terms of winners and losers, that each test should also say something about what will we learn about a business flow, a funnel, preferences of the guests, preferences of the hosts. What will we learn about their demand elasticity if we're changing prices around? These kinds of things. So it's possible to articulate in an experiment doc, a launch doc, what are the hypotheses that are being tested? So that's one thing I would say is just culturally, setting the norms that learning is part of the discourse, and it's expected actually I think is important.

But the other thing I would say that's maybe a little bit more about programmatically, what could a data science platform team do? A funny thing about experiments is that we throw past learning away effectively. And this is just an artifact of how we analyze experiments, that the statistical methods used typically, P-values, confidence intervals, these fall into a branch of statistics known as frequentist statistics. And the idea behind frequentist statistics without being overly technical is just I let the data speak for itself. There's no beliefs brought to the table about where that data came from.

But if you think about this in a company, in A/B testing a company, it's a weird thing, right? Because I might've run 1,000 A/B tests in the past on this exact same button, or call to action, or color, and now I am going to completely ignore that and focus only on this. So there's ways to take the past into account, to build what's called a prior belief before I run an experiment, and now take the data from the experiment, connect it with the prior, to come up with a conclusion of, "Okay, in light of the past plus this experiment, what's it telling me about the future?" And that falls broadly under the category of what's called Bayesian A/B testing.

---
