# Brian Tolkin — Lessons from scaling Uber and Opendoor | Brian Tolkin (Head of Product at Opendoor, ex-Uber)
*Theme: org-strategy-leverage | Extracted: 2026-04-04*

## Tech leverage and when to invest in ops vs. technology

Lenny Rachitsky (00:18:15):
You've worked at two businesses that have done incredibly well combining product and ops. Are there any just broad lessons you've taken away from how to make these two teams and functions work well together and to build a business that's very ops heavy but also offer driven?

Brian Tolkin (00:18:15):
The first one we touched on, which is a, there's just got to be mutual respect. Both functions have their time and their place and their skillsets, and you just don't build big businesses of this type without respecting the fact that that both need to exist. The second, particularly on the product and engineering side, is really understanding where and how the technology leverage comes from the business and then being really focused on making sure generally, especially in the earlier days, you are more limited on the technical resourcing side than you might be on the operational resourcing side. And so how do you be really focused on where to invest your time, effort, and energy technically, which is why most of the engineering effort for Uber was on the dispatching system and the pricing system. That's just where the leverage was at the time, given the scarcity of resources.

And so I think the second one is being really intentional about where those techs are and then being really forthcoming and saying, hey, that means all these other places where yes, it can make things easier, more efficient, et cetera, et cetera. We are okay not investing in right now, and that needs to be an explicit decision and very transparent. But then the last bit I would say is a deep understanding that the real world has entropy and it's hard and it's messy for us at Opendoor, we go into homes, someone may not be home, scheduling may be off, at Uber the driver may cancel the radio GPS. All these things happen, right? Computers are deterministic, but humans aren't, right? And so building products that have a little bit more flex or a little bit more fail safes in case those things happen becomes a little bit more of a paramount.

---

## Ops-to-tech graduation: scaling driver onboarding at Uber

Lenny Rachitsky (00:21:25):
Yeah, I mean, maybe a very easy good example to pick just one part of the Uber process in the early days is at small scale, actually back when it was Uber black drivers, every driver was individually onboarded in a 90 minute to a two-hour in-person in the office onboarding with deep setting of expectations. The next version of that... So that's obviously very ops driven. The next version of that is a small classroom type setting of three or five or six drivers at a given time. Also, very ops driven. And then as we got into more mass market products like Uber Taxi or UberX, it was like, okay, maybe 20 or 30 at a time. So now it's a little bit bigger classroom setting. And we said, okay, let's make a video. Instead of giving verbally the same presentation, let's just make an onboarding video and that was the next set of scale, but now suddenly we have a different problem, which is okay, you have to validate all of these credentials.

So most driver's license who they are, all that stuff at one person, easy at three to four at a time, easy, 10 at a time, a little more challenging but fine. At 20 at a time, okay, you're starting to run up onto it now you fast-forward six months and you're doing a thousand a week or whatever, suddenly your system breaks and it's like, okay, we have reached the point where operational system improvements is no longer viable. So, you say, okay, we have gone from the iteration stage to the scale stage and technology is uniquely good at scaling. So now we say, okay, instead of having a bunch of folks around the world taking pictures of driver's licenses and validating and doing all that stuff, how do we integrate with some type of OCR technology or auto recognition of driver's licenses that feeds to a system that knows what a driver's license is or can do automatic validation and suddenly you've done two things.

One, you've scaled your system, and two, you've just created a ton of time for what at the time was probably dozens if not hundreds of people running these onboarding sessions all over the country, the world at the time to do other stuff. And so now you can level that up and say, okay, do we do more analytics? Do we do more figure out the next process that needs optimization or whatever the case may be in that virtuous cycle just continues.

Lenny Rachitsky (00:23:53):
The way I like to think about this is do things that don't scale and then scale the things that you're doing. That's the phrase I always come back to.

Brian Tolkin (00:23:58):
Exactly.

---
