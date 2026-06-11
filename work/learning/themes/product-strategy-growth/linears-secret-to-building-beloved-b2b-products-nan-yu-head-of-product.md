# Nan Yu — Linear's secret to building beloved B2B products | Nan Yu (Head of Product)
*Theme: product-strategy-growth | Extracted: 2026-04-04*

## Speed and quality are not a trade-off

Lenny Rachitsky (00:07:52):
First question I want to get into is something that I think you see and the team at Linear sees that a lot of people don't see, which is that there's not actually a trade-off between speed and quality. I think a lot of people think this is just an innate fact and something I've heard you talk about is that's not actually true. I actually saw Patrick Collison tweet this exact point that I'll read after you... I want to hear your thoughts, but talk about what you've learned about how there's maybe not actually this trade-off between speed and quality.

Nan Yu (00:08:20):
People talk about this as if there were a trade-off almost in a naive way because when they think about speed, the thing they over index on is rushing or being sloppy, and what they should be indexing on is being really competent or being like an expert. So, if you look at people who are at the pinnacle of their craft, it could be anything. It could be like a chef or a programmer or someone building houses or something. You can basically tell how good the output is going to be of their work product by how fast they're going. If they're going really fast, and they're obviously not being sloppy and then leaving a mess all over the place, it's like, "Yeah. Well, they got there because this is just second nature to them," and they're able to go at a really rapid pace and try stuff. And when we're building software, that's such a big component of how good the product is on the other side of it, which is like, "How many iterations were you able to do?" So, the only way you're going to get a bunch of iterations done and try different things and really feel out these different variations is by just going very fast.

Lenny Rachitsky (00:09:25):
In terms of speed, is the speed there moving quickly on each of iterations? Like what does speed look like when you say, "It can be done quickly and high quality"? What does speed look like?

Nan Yu (00:09:36):
Speed... What it really looks like is you have some rough time budget for how long you think something's going to take, and by the time 10% of it has passed, you have a workable solution. It's not like, "Oh, at the halfway point, we have something that is maybe a candidate that we can play around with." It's like, no, no, no. After week one you have something that works that tests some kind of key hypothesis internally so that you can feel like is this thing actually panning out the way we expect it to or did we have some crazy incorrect assumption? And you don't want to wait until you're 80% done to be able to make that kind of judgment because then it's just too late. Then you're pushing deadlines out, and you're making your marketing team very sad.

Lenny Rachitsky (00:10:18):
Amazing. Okay, so the way you think is, "We're going to spend a month on this feature. Let's get something workable. We can start testing with potential users even internally in the first few days, essentially in the first week"?

Nan Yu (00:10:30):
Yes. Yeah.

Lenny Rachitsky (00:10:32):
Yeah. I guess how can you do that? Because most teams can't do that. Most teams need to research, design, build. "Okay, cool. We have something," and once a month later, what allows you to do that?

Nan Yu (00:10:43):
Yeah, I mean, there's a lot of components of it. I think having really good talent really helps. Having engineers who don't get blocked by every single little design choice, they're happy to just make something workable. Even if they don't feel comfortable with that particular solution, they'll just bust through it and make something happen there. Part of it is intent. We don't have any expectation that the first version of it is going to be great. That is not in the cards. Look, the first version of it is our best guess in the general direction of what we want to actually ship in the end, and sometimes it works out. Sometimes, it's like, "Wow, this first version was pretty good. Let's make some minor adjustments, and we're good to go," but there's no expectation there. So, no one feels like they have to be a perfectionist and get everything, like all sanded down and really in tip-top shape. It just has to work and get the job done and validate or invalidate our major assumptions.

---

## Prioritizing ICs over middle managers to avoid bloat

Lenny Rachitsky (00:15:31):
I imagine a criticism you all get. People are like, "Yes, Linear is so great, so beautiful, so much better than what's been out there for decades," but over time you'll probably become a bloated piece of software as well. That's just the fate of enterprise software. You have to check all these checkboxes. IT teams need all these features. So, there's always this like, "Oh, yeah, sure, you guys can operate this way for now. You have an amazing product for now, but it'll get ugly and bloated." How do you think about avoiding that? I know it's something you spent a lot of time thinking about. Maybe give us a glimpse into some of the conversations you have internally when there's these feature requests like, "Oh, I need single sign-on with this thing and this button here." How do you think about what to add, what not to add, and how to add these features to not make it bloated?

Nan Yu (00:16:14):
This question actually comes to us a lot from candidates that are interviewing with us. When you go like, "Hey, do you have any questions for us?" This is the question that we're going to get. So, we hear it quite a lot, and it's very sensible for them to ask it because they see history being littered with the corpses of startups trying to compete in this space and not making it, and I think when we examine this problem, we look at, "Well, what kind of feature requests can we debate and what kind of feature requests do we absolutely have to say no to?" And the stuff that we absolutely have to say no to is also the exact kind of thing that leads to this bloatedness that makes ICs hate their lives, and it's very specific. It's customization features requested by middle managers in order to make reporting a little bit easier at the cost of making IC workflows worse.

It's like if it fits that description, we're just saying, "No." There's no debate because we've already thought about it and this is the thing that we can't take a single step down this path. So, I think that's honestly one of the core promises of Linear is that we will not make this particular trade-off. So, when you see people saying like, "Wow, Linear is so much faster. It's so much easier to use and it makes my work so much more enjoyable." This is the reason because we have not taken a single step in this direction. It's very easy for a PM to say yes to this kind of request because often they're talking with buyers. Any kind of B2B type of space, they're talking with whoever the gatekeeper is and sales is putting pressure on them, and they're saying like, "Hey, we really want this one feature. It's going to make our reporting nicer."

So, the director's going to be really excited by this, and we'll definitely make a buying decision based off of this, and we have to convince them that this is a false trade-off. The whole premise is wrong because the moment you start going down this path, and you make the IC user experience worse, they're just going to disengage. No one has to do this. If I'm an engineer, I get paid to write code. My performance review is based on my code contribution. It's not based on like, "Did I fill in all the tickets right?" So, I'm just not going to do that part, or I'm going to do it very sporadically, and then I'm going to just focus on my actual job.

And then all your reporting is wrong because all the data is wrong, and it's sparse, and you get situations where people will... They'll say like, "Well, here's a dropdown field that someone put in here that's required." There's nine choices. I don't know what any of them meet, so I'm just going to pick one at random. I'm still going to pick the first one. Also, I'm going to pray that my boss is not actually using this data to do any kind of reporting and that has consequence because the data can't possibly be correct. So, I think for us, it's a very easy decision when it comes to that particular category of feature request.

---

## Deadlines as P0: scope-cutting over estimating

Nan Yu (00:09:38):
I have a very specific point of view on deadlines. I don't know if that's something you care.

Lenny Rachitsky (00:09:34):
Let's do it. Fire away.

Nan Yu (00:09:38):
I think what often happens is people get depressed about deadlines. It's like, "Hey, here's the ship date," and then you never make it. I don't know if you've had this feeling before.

Lenny Rachitsky (00:09:47):
Absolutely, with some deadlines.

Nan Yu (00:09:49):
You were an engineer before too, right? So, it's just like engineers is basically like, "Oh, yeah. Yeah, deadlines, they're complete fabrications," and the only way to make deadlines real is to take them so seriously that they are basically like a P0 problem, and everything else has to not matter in comparison to the deadline because that's the only way you're going to be able to signal to the team and also to all the stakeholders that you're actually taking it seriously. So, my feeling on deadlines is don't have too many of them, and when you do, it's a P0. So, the engineer is working on it. They don't get to work on anything else.

It's like, "Oh, I need them for this," like nope. Nope. You're not pulling them off of anything. We're doing this. As a PM, your job is to just cut as much scope as possible to make it possible to hit that deadline. Like what are the things actually blocking us from doing it? Because what you want to do is at the moment where you have to make the go, no-go call on whether to ship, you want to be able to actually have a product that you can say yes to. It might not have all the features you had wanted or whatever, and you can say no. You can make that choice, but you want to set yourself up to be in a position where you can actually say yes or no to something, because what often happens is like we want this thing. Well, it's not even close to being done yet, so there's no possible way we can say yes. I can't ship it. It's half broken. It's like, "No, no, no. You want to get to a point where it works. It might not be the product that you want, but it is an actual real product that you can conceivably ship."

Lenny Rachitsky (00:11:19):
So, you said that don't have too many deadlines, but when you do, make sure you... Everyone understands these are actual deadlines. When do you decide it's worth having a deadline? Is it like a marketing launch sort of thing? What's worthy of a deadline in your experience?

Nan Yu (00:11:32):
Yeah, it's usually having to do with some kind of external marketing type of exercise that you're try to hit. And I think that that's the other thing that I think. As builders, we can often look at launch dates and stuff like that. It's like, "Oh, who cares if it's a little bit later or we skip this change log," or whatever it is, and I think that that's really a... I don't know. It makes me go crazy when I hear people say that in all honesty. With marketing and communication with customers, you basically have a limited amount of opportunities to do so. A year is 365 days. There are 12 months. Each of those months has about four weeks. There's some rhythm where you get to have 50-ish weeks to say something to your audience once a week, or you get to have 12 months to say something really big or four quarters to say something huge. If you miss one of those opportunities, you don't get it back again. You can't time travel back and say like, "Okay, actually, let's redo first quarter and say this message that we wish we could have gotten into the field."

---
