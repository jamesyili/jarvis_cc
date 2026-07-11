# Eric Simons — Inside Bolt: From near-death to one of the fastest-growing products in history
*Theme: entrepreneurship-traction | Extracted: 2026-04-05*

## Near-death to overnight success: the 7-year tech bet that paid off

Lenny Rachitsky (00:19:09):
You made a really important point, that you worked on this for seven years before you launched Bolt. A lot of people see these stats, zero to 40 million ARR in five-ish months, and they sometimes don't see that there was also years and years of work before that. And the reason that you guys have been so successful is all the work you did that allowed, that built this WebContainer technology, it sounds like. Is there anything there that's worth sharing, you think, of just that part of the journey? I know we'll go through the origin that all, where Bolt came from, but I guess just that WebContainer component specifically. That feels like a huge deal.

Eric Simons (00:19:44):
A hundred percent it is, yeah. And I would say this is, surprisingly to me, it's still one of the contrarian viewpoints of our company. Because over the years it was like, when we first... And that, the WebContainer was the bet, that we made the company on. Just to be clear. StackBlitz was a browser-based, deep technology play on, "Can we make a web assembly based operating system that can boot in a browser, in like a hundred milliseconds, and run full on development tool chains?" That was really it.

And we'd gotten the idea for this, and the insight that this might be possible, because back when my co-founder and I came out to the Valley, he and I grew up down the street from each other in Chicago, we wrote code together at 13, and been building stuff ever since. And we came out to the Valley in 2012, and we just had the good fortune of bumping into Dylan Field and Evan Wallace when they were building Figma, in the early days. And that was, I don't think a lot of people know that Figma was also a browser-based deep technology play. Their first pitch for Figma, they didn't have a design tool. Their first pitch was this 3D ball dropping into water, inside of a browser town.

And the pitch basically was, "Browsers have this new capability called WebGL," the predecessor to WebAssembly, "and with these things, for the first time, you could actually create a graphics rendering engine, that you could then build a design tool on top of. But you're going to have to write that rendering engine from scratch, because nothing exists that can just compile into WebGL, or whatever. And if you want the performance you need, et cetera, it's going to take us years to do, but if we do it, we think this will change everything for design."

And obviously, we know how that story has panned out now. And back in 2017, 2016, 2017, Albert, my co-founder and I, saw the same sort of story begin to play out, but for web development and development environments. And specifically there was some stuff that landed in browsers like WebAssembly, shared memory, service workers, these different APIs. And we were like, "Oh, wow. It should be possible, theoretically, to write an operating system in WebAssembly that could run Node.js, and NPM and all the tool chains on top of it, that you need to do web development."

---

## Conservative burn rate during the exuberance years saved the company

Lenny Rachitsky (00:25:04):
There's a lot of really interesting lessons from this journey, that I think are counterintuitive. One is, you basically were building a tech first, and then looking for a problem to solve later. Which is often what people tell you not to do. And it worked out, in this case.

The other interesting takeaway here is, it feels like it's a similar moment to when AJAX came out and then everyone's just like, "Wow, you can build new things here." So it feels like there's a lesson here of just, "If there's a new technology that has enabled, something big that we think may, let's just work there for a while, and see if something comes up."

And then I think the other lesson here is just, as a founder, just survive as long as you can. Because you may find something that works.

Eric Simons (00:25:43):
All great points, all great points. Because you're dead right. And fortunately, my co-founder and I had, we had built a lot of unsuccessful stars before this. We spend most of the, or 20 times, churning through ideas on things. So when we had conviction, I was like, "This seems like a technology that will be important." It seems like, the web is the most ubiquitous... The pitch or the theory in our head was like, "The web is the most ubiquitous platform in the world, but yet it has no, you can't use the web to build the web."

Every other platform, Mac has Xcode. Windows has Visual Studio. The web had nothing. And we were like, "At a minimum, Google should probably buy this thing from us. It seems like it should probably be part of Chrome," at a minimum. And we thought, "Hey, this could be a huge enabler." The vision of just making it as easy to build full stack applications as using Canva, it just seemed really compelling.

But when you do that sort of risky deep technology play, you need to... And we were very good about this, like the previous company Albert and I did, we bootstrapped it all the way through to acquisition, so we understood and we were living hand-to-mouth, to bootstrap that thing. So we understood out of it how to have a low burn rate, and take a lot of shots on goal, and make every dollar stretch beyond what anyone would think is reasonable or possible. And that's how we played our hands with StackBlitz. We didn't raise money for the first two or three years of the company's life. We were bootstrapping it. When we did raise money, we barely spent it. Largely because it was like, "We need to just take a lot of smart bets, and it doesn't make sense."

And I would just say generally, until you see pull, just people pulling the product out of your hands, you don't want to be spending money. You should be like, default, no. And when you go and buy software, you should be going, "We're a tiny startup. Can you sell it for half?" Everything you buy, just keep the burn rate as low as possible, because you need as many shots on goal as you can possibly get. Because you have no idea. I think just generally, for startups, that's the right way in my view, to approach it. Unless you're seeing, again, immediate demand and pull, or whatever.

But yeah, I think that'd be, maybe the extra context I'd add on top is, I think that we ended up doing a good job of being extremely conservative. During a time in which, during 2020, through 2020 and 2021, which were times where exuberance and growing headcount was like, KPIs of companies. And were things that were being... With lot of emotional force of like, "Hey, you guys ought to be doing this." And I'm glad that we didn't heed the advice, because if we had tripled the company and kicked up the burn rate, there would be no Bolt. We would've gone out of business a lot of time ago.

So I think that's the hard thing about being an entrepreneur, I think is you kind of have to... There are periods of time where you have to make judgment calls that are not going to be the consensus view. Maybe years later, it'll become the consensus view, but you got to have confidence in your convictions on how to best play the hand.

---

## Launch day: 60K ARR on day one, then 80K the next — reading genuine pull vs. launch spike

Lenny Rachitsky (00:29:37):
Maybe talk about that moment of just, after launch, signs that, "Okay, this is working. Something's different."

Eric Simons (00:29:43):
Yeah, yeah. So day one it was like, there's great reception to the tweet. We were like, "Wow, this is one of the biggest things, launch day reception we've ever seen." And I think on the first day, I think we added 60K of ARR, or something. Which was like, I mean, crazy. Again, we were at 600, so we added 10% in a day. And I remember our dev ops engineer, he was the one who would flag me. He was like, "Guys, we got 60K today. This is crazy." And I was like, "Yeah, yeah. But this is launch day."

There's the tech crunch, peak of initiation, in the classic startup-

I was like, "Listen, guys." I'm trying to temper enthusiasm for the team. I'm like, "This is great. Got a lot of work to do." And then the next day we added 80K, or whatever it was, and it just kind of kept going. And all the while, the product we put out, we built a thing in 90 days. We built Bolt in 90. So there's a lot of things that were missing in the product. Like, basic stuff, basic stuff. And which, again, we cut the right corners on the thing to get it online, but we had this just growing influx of people using it, going, "How is there not a mobile responsive view? How are chat messages not," we got to 20 million of ARR without a mobile responsive view, by the way. Just throwing that out there. It was like the iPhone not having copy and paste until iPhone 5, or whatever. That was that, this was that for us, it was like, no mobile. You looked at it on mobile, it was terrible.

But there was stuff like that, so we had to just... And then, we're a small team and so, we were completely unprepared for just the growing traffic. And there was a whole bunch, I mean, the list of problems that were happening every single day was nuts. I mean, to start, we had never had a plan on stackblitz.com for more than $9.00. We had one price, nine bucks. And so when we launched Bolt we were like, "Again, we don't think, hopefully people like this, but nine bucks doesn't get you a lot of inference." And so people burn through nine bucks in 48 hours. And they're like, "I want to buy more. How do I buy more? Why won't you take my money?"

So it was like, within the week we rolled out just completely new pricing plans, where you could upgrade, which ended up, has kind of now become the standard. All the other guys in the space have copied this. Where prior to Bolt going online, Copilot, all these previous AI things, everyone wanted this Netflix model where there's one price, it's like all you can eat, or whatever. And the problem is, if you do that, you want the inference cost to be kind of low, because you're expecting people to use it a lot. And so you can't do these agentic experience things, it would be too expensive.

And what we ended up stumbling into is that, "Okay, actually, people are willing to pay more. People want to pay for more inference, because we've crossed this threshold where you can get a very tangible ROI." You know that this is providing a tremendous amount of value to you.

---
