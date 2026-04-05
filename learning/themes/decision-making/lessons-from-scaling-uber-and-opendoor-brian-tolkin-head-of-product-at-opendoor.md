# Brian Tolkin — Lessons from scaling Uber and Opendoor | Brian Tolkin (Head of Product at Opendoor, ex-Uber)
*Theme: decision-making | Extracted: 2026-04-04*

## Experimentation under low-volume constraints

Lenny Rachitsky (00:40:00):
You mentioned that Uber, there's a million transactions happening every second, it's massive scale. Opendoor is completely different. You have very few very large transactions. Yeah. I'm curious how you do experiments, if you do experiments, do you do A/B tests? What have you learned about just how to think through low sample sizes plus A/B testing?

Brian Tolkin (00:40:29):
Yeah, very hot topic of conversation. We do A/B test. It is obviously the gold standard. And so we do as much as we can. Of A/B testing there are parts of our funnel and flow that have more volume than others. So top of quality testing easier than down funnels, A/B testing purely product or tech features easier than A/B testing processes, operational processes. But you're totally right. We are not doing hundreds of millions of transactions a year. And so experimentation can be more challenging. And so I think one way to think about it is A, acknowledge the problem, which just to say don't, and we've made this mistake many, many times, but don't just force yourself into A/B testing without running the power analysis and say like, hey, are we going to get results? What is the size that will detect and what is the runtime of that experiment?

And be honest, is that acceptable? A second lesson here, is there certain experiments that are important enough and it's hard to triangulate signal in any other way that you may say a six-month runtime is an acceptable outcome and we are going to start it in June and we will be smarter for it for 2025 planning and we're going to set it and forget it and we're grateful we did, and that's okay. But the only mistake here is thinking you'll get an answer in a month when you won't, and then pretending you do and then waking up a month later and being like, 'Well, it was insignificant and this and that.' We could have known that. And then the third thing is, and experimentation is all about increasing your conviction in the problem or the solution. So the generalized version of the statement is, if there are parts of your funnel or flow that are low end and you can't run a canonical A/B test, how might you otherwise increase your conviction in the solution that you're building?

And there turns out there are a decent number of other ways to do that. The first best, most obvious is talk to more customers. But there are other statistical techniques that again, aren't as rigorous or good, but may be possible. You may be able to use observational data, you review with diff and diff, you may be able to look at sister cities or twin cities. You may be able to segment by geo, you may be able to reduce your power and say, hey, we're going to run at 80% confidence for all of our experiments instead of this traditional 95% because that's a worthy trade-off. And if we're wrong one more time out of 10, that's okay.

You can do a long-term holdout to match your intuition. And so there's a lot of other techniques to hone your intuition. There's a lot of other techniques to build conviction and confidence. And so we try to be very creative on doing that. And then the last bit I would say is if you're not going to get significance, if there's no other techniques at your disposal, then sometimes you just got to trust your intuition and ship it. And if that's what you believe, then that's what you believed and you shouldn't spend time trying to get false precision.

---

## When to trust intuition vs. data

Lenny Rachitsky (00:45:06):
So, at Airbnb we went through the same thing where there was all these local ops teams driving supply, finding homes, bringing out the platform, and then there's this tipping point where the product in organic growth or word of mouth ended up driving more and then orders of magnitude more. So there was no need for these folks to spend time doing these things. Can you just maybe share an example, either we Opendoor, when you talk about there's a time and a place and a skillset for ops, how that evolved? What was the team doing initially and then what did they end up doing as things grew?

Brian Tolkin (00:45:06):
So, at Opendoor, for example, I'd say on the relative spectrum, we're quite data-driven. And then it's when we come into this challenge where we say, okay, that is another technique or tool in the toolbox. I think the generalized version of that is customers, products, people can surprise you. And so this happens all the time for people who build products. I'm sure you've got great stories from Airbnb where you saw something, put it out there just was very-

Lenny Rachitsky (00:45:35):
All the time.

Brian Tolkin (00:45:36):
All the time. And so I think there's definitely a humility to say if you can, if it's relatively easy to test your assumptions or test your hypotheses. That is always better to gut check yourself. And that takes a little bit of humility to say that, but we've all been wrong plenty of times. But if that's just not on the table, I think the reality is you can't pretend it is. And sometimes you got to use taste and judgment and then you say, okay, what is my conviction level and do I have just medium, low or high conviction? And if I have anything low or medium conviction and it's a decision of consequence, I should talk to more customers, check it with another person and see if their intuition matches. Something that gets me personally to the high bucket category.

And then I think the last part, which is some part of experimentation is if you just ship something because it's your intuition or it's where you want to see the product go, do you have a reasonable feedback loop to understand whether or not you are correct? So that could be customer support or ticket volume or feature adoption, whatever the case is, it may not be an output metric in the traditional A/B test, but some more rigorous system that says, hey, I had this hypothesis, we just shipped it for x, y, z constraint reason for red.

---
