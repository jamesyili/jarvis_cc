# Ronny Kohavi — The ultimate guide to A/B testing | Ronny Kohavi (Airbnb, Microsoft, Amazon)
*Theme: decision-making | Extracted: 2026-04-04*

## Portfolio thinking: incremental vs. high-risk bets

Lenny (00:20:45): It's a good segue to something I wanted to touch on, which is there's often, I guess a weariness of running too many experiments and being too data-driven, and the sense that experimentation just leads you to these micro optimizations, and you don't really innovate and do big things. What's your perspective on that? And then, can you be too experiment driven in your experience?

Ronny Kohavi (00:21:07): I'm very clear that I'm a big fan of test everything, which is any code change that you make, any feature that you introduce has to be in some experiment. Because again, I've observed this surprising result that even small bug fixes, even small changes can sometimes have surprising unexpected impact.

And so I don't think it's possible to experiment too much. I think it is possible to focus on incremental changes because some people say, "Well, if we only tested 17 things around this," you have to think about, it's like in stock. You need a portfolio. You need some experiments that are incremental that move you in the direction that you know you're going to be successful over time if you just try enough. But some experiments, you have to allocate sometimes to these high risk, high reward ideas. We're going to try something that's most likely to fail, but if it does win, it's going to be a home run.

And so you have to allocate some efforts to that, and you have to be ready to understand and agree that most will fail. And I've amazing how many times I've seen people come up with new designs, or a radical new idea, and they believe in it, and that's okay. I'm just cautioning them all the time to say, "Hey, if you go for something big, try it out, but be ready to fail 80% of the time."

And one true example, that again, I'm able to talk about because we put it in my book, is we were at Bing trying to change the landscape of search. And one of the ideas, the big ideas was we are going to integrate with social. So we hooked into the Twitter fire hose feed and we hooked into Facebook, and we spent 100 person years on this idea.

And it failed. You don't see it anymore. It existed for about a year and a half, and all the experiments were just negative to flat. And it was an attempt. It was fair to try it. I think it took us a little long to fail, to decide that this is a failure. But at least we had the data. We had hundreds of experiments that we tried. None of them were a breakthrough. And I remember mailing Qi Lu with some statistics showing that it's time to abort, it's time to fail on this. And he decided to continue more. And it's a million dollar question. Do you continue, and then maybe the breakthrough will come next month, or do you abort? And a few months later, we aborted.

---

## OEC: defining what you're actually optimizing for

Lenny (00:28:00): Love it. Coming back to this kind of concern people have of experimentation, keeps you from innovating and taking big bets, I know you have this framework overall evaluation criterion, and I think that helps with this. Can you talk a bit about that?

Ronny Kohavi (00:28:14): The OEC or the overall evaluation criterion is something that I think many people that start to dabble in A/B testing miss. And the question is, what are you optimizing for? And it's a much harder question that people think because it's very easy to say we're going to optimize for money, revenue. But that's the wrong question, because you can do a lot of bad things that will improve revenue. So there has to be some countervailing metric that tells you, how do I improve revenue without hurting the user experience?

So let's take a good example with search. You can put more ads on a page and you will make more money. There's no doubt about it. You will make more money in the short term. The question is, what happens to the user experience, and how is that going to impact you in the long term?

So we've run those experiments, and we were able to map out this number of ads causes this much increase to churn, this number of ads causes this much increase to the time that users take to find a successful result. And we came up with an OEC that is based on all these metrics that allows you to say, "Okay, I'm willing to take this additional money if I'm not hurting the user experience by more than this much." So there's a trade-off there.

One of the nice ways to phrase this, as a constraint optimization problem. I want you to increase revenue, but I'm going to give you a fixed amount of average real estate that you can use. So for one query, you can have zero ads. For another query, you can have three ads. For a third query, you can have wider, bigger ads. I'm just going to count the pixels that you take, the vertical pixels. And I will give you some budget. And if you can under the same budget make more money, you're good to go.

So that to me turns the problem from a badly defined, let's just make more money. Any page can start plastering more ads and make more money short term, but that's not the goal. The goal is long-term growth and revenue. Then you need to insert these other criteria, and what am I doing to the user experience?

Lenny (00:32:05): To me, the key word is lifetime value, which is you have to define the OEC such that it is causally predictive of the lifetime value of the user. And that's what causes you to think about things properly, which is, am I doing something that just helps me short term, or am I doing something that will help me in the long term? Once you put that model of lifetime value, people say, "Okay, what about retention rates? We can measure that. What about the time to achieve a task? We can measure that." And those are these countervailing metrics that make the OEC useful.

---

## Sunk cost fallacy in product decisions

Lenny (00:36:31): This makes me think about how every time I've done a full redesign of a product, I don't think ever, has it ever been a positive result. And then the team always ends up having to claw back what they just hurt and try to figure out what they messed up. Is that your experience too?

Ronny Kohavi (00:36:47): Absolutely, yeah. In fact, I've published some of these in LinkedIn posts showing a large set of big launches and redesigns that dramatically failed, and it happens very often. So the right way to do this is to say, "Yes, we want to do a redesign, but let's do it in steps and test on the way and adjust," so you don't need to take 17 new changes, that many of them are going to fail. Start to move incrementally in a direction that you believe is beneficial. Adjust on the way.

Lenny (00:37:24): The worst part of those experiences I find is it took three to six months to build it. And by the time it's launched, it's just like, "We're not going to unlaunch this. Everyone's been working in this direction. All the new features are assuming this is going to work," and you're basically stuck.

Ronny Kohavi (00:37:41): I mean, this is a sunk cost fallacy. We invested so many years in it. Let's launch this, even though it's bad for the user. No, that's terrible. Yeah. Yeah. So this is the other advantage of recognizing this humble reality that most ideas fail. If you believe in that statistics that I published, then doing 17 changes together is more likely to be negative. Do them in smaller increments, learn from, it's called OFAT one-factor-at-a-time. Do one factor, learn from it, and adjust. Of the 17, maybe you have four good ideas. Those are the ones that will launch and be positive.

---
