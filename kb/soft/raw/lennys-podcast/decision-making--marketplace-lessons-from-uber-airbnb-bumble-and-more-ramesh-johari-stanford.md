# Ramesh Johari — Marketplace lessons from Uber, Airbnb, Bumble, and more | Ramesh Johari (Stanford professor)
*Theme: decision-making | Extracted: 2026-04-04*

## Causation vs correlation: prediction isn't decision-making

Ramesh Johari (00:32:32):
So to give another example that's similar to this, when you're a marketing manager, and you've got a cracked data science team that's built a long-term value, lifetime value model for you, you're not going to get in trouble with anyone if you send your highest value promotions to the highest LTV customers, right? Who's going to blame you for that? Because you're like, "This person is worth a lot, and I sent them this promotion." Say that in your monthly report, nobody's going to give you a hard time.

But the problem with that way of thinking is actually predicting what their lifetime value is isn't really the question. The question is, how much more are they going to spend on my platform because I sent them that promotion?

That's a very different thing. It's a differential rather than an absolute. I'm not interested in their absolute LTV. I'm absolutely interested in the difference in their LTV because I sent them this promotion.

And when you look at it that way, what you realize can happen is picking up on patterns because of good predictions, right? Finding the people that have high LTV because you predicted that is very different than making good decisions, which is about saying the difference in their LTV is going to be higher because I sent them this promotion.

I love this example, because I taught a class here at Stanford. It was like an executive education class. We had all the executives from a company in the room, and one of the people in the room was the chief marketing officer. And I just asked this question like, "Hey, okay, let's say you got this great LTV model, who would you send the promotions to?" It's like, "Definitely the highest LTV people," and there's a CMO in the room. And so it's a little bit of a delicate situation, like pushing back a little bit, right?

I do want to be clear, there's reputational reasons you might do that anyway. I mean, I'm not trying to get away from that. But just to make the narrow point that predicting is about picking up patterns, but making decisions, it's about thinking about these differences.

Now, why is that important? Because we learn in high school, correlation is not causation. That's a phrase everybody has heard all over the place. What does that have to do with this? Well, when we teach people to build machine learning models, we're asking them to make predictions, we're asking them to find correlations. Prediction is inherently about correlation. But when we ask people to make decisions, we're asking them to think about causation. "If I make this decision, then will I actually increase the net value of my business? Will I have by sending the promotion, increased the likelihood that this person is going to spend more on my platform?"

And so the first and most important thing that I feel very strongly about in what would I get a data scientist to do is no matter who they are, even if it was that person in the weeds thinking about building this prediction model for hiring, get them to be thinking in the back of their mind always that their goal is to help the business make decisions. And that the distinction between causation and correlation matters a lot.

---

## Learning costs money: the holdout group anecdote

Lenny (00:57:50):
This touches on a really interesting concept that you shared with me around how, just learning isn't free. People think that they could just learn a bunch of stuff and there's not a cost to it. I'd love for you to just chat a bit about what that means.

Ramesh Johari (00:58:02):
Let me start with an anecdote, that I just absolutely love this anecdote. I use it every year in class. So I was talking to a real estate platform, and they had a marketing data science manager who's basically responsible, as many marketing managers are, for allocation of ad spend across different channels.

And what they discovered had happened at the end of the year is in one hand, the team had done great, but the manager had held out some subset of arriving visitors, not showing them any of the innovations they were making.

Lenny (00:58:39):
Like a holdout group?

Ramesh Johari (00:58:40):
Yeah, exactly. What's called a holdout group in experimentation. And one thing about this holdout is it wasn't authorized. That's not the way things are supposed to work. They've got their ad spend, allocate out your ad spend, great. So at the end of the year, they looked at the hold out and they're like, "Wow, that cost us a couple million dollars, something in that range, and it's not a trivial amount of money. What's the deal? What were you thinking?" Basically. And of course the answer was, "Well, I get that I cost you that much, but number one, now you know what my team's worth. And number two, you would never have had that answer unless I'd done that on my own."

Now, why is that so powerful? I think what I find so interesting about experiments is that when you don't know something, it seems not even a question that you would allocate some of your samples to all options, right? Treatment and control. I have two different ways of doing something. I don't know which one's better, so of course I'll give some samples to each. After the fact you're like, "Treatment was better. What the heck were we thinking? Why'd we give all those samples to control? That doesn't make any sense now." There's this great Seinfeld clip where he mentions getting a bill at the end of a large luxurious meal, and people stare at the bill like, "We're not hungry now. Why'd we order all this food?" So it's the same thing. I mean, you know treatment's better now. Why'd you waste all those samples on control?

And I think that is such a powerful observation that you have to put yourself in the frame of reference of when you didn't have the answer. And at that moment, what you're essentially saying to yourself is that it's worth paying to learn the answer. I think it sounds obvious the way we're saying it now, or this anecdote of the marketing manager and the holdout sounds obvious. What's culturally not baked in I think is that idea. And the reason I say it's not culturally baked in, by the way, is because of the language of winners and losers. Because if we use that language, we're implicitly saying is that we wasted time when we ran an A/B test on loser. If I reward you for shipping winners, then what I'm really telling you is all the time that you spent testing out failures was wasted time.

And I think, of course, you don't want to keep data scientists around who regularly are just generating failures. That's not my point. But my point is there's a disconnect there. On one hand, we can all look at the story of this marketing manager and chuckle at it. And yet, every day we're instantiating language and processes that are reinforcing that same theme, which is essentially trying to say to you, "If you're wasting samples on things that don't ultimately end up being a winner, then the act of doing so is a failure."

---
