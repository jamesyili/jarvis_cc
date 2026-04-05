# Will Larson — The engineering mindset | Will Larson (Carta, Stripe, Uber, Calm, Digg)
*Theme: emotional-regulation-resilience | Extracted: 2026-04-04*

## Digg V4 death march: no way around, just through

Lenny (01:02:11):
Okay, final question. I wanted to visit Failure Corner, something that I've added recently to this podcast where people share a story of failure. And you have this amazing post about your experience with Digg and the rewrite that you all went through. I think it was the version four of Digg. Can you just tell that story and what happened? How much of a mess it ended up being?

Will Larson (01:02:33):
Yeah, Dig V4 is... I mean, it's still something I have a lot of fond memories for. There's one picture that I've kept and there's a picture of a lot of the engineers around this table in the middle of this giant office and they're serving sushi. We had waiters, caterers come in that day. They're serving sushi. They have plates with champagne flutes on it. There was a full bar and we're all around this table because the site is not up.

And so Digg before essentially what Kevin Rose or the board or some combination there realized is that Digg was losing to the social networks and that this idea of aggregated news was going to be outcompeted by the Twitters, the Facebooks, et cetera, if we didn't find a way to move to have a social component for it. So the decision that was done... they needed to do a complete rewrite in order to get there. This is a decision that never works out for anyone.

So we go and the CEO got fired two days before I joined. So the current CEO left and then Kevin Rose came back for about six months, something like that. And we're just on the death march trying to get this thing out.

So we pushed really hard. This was before the cloud for the most part. So we wiped pretty much all of our existing servers to re-image them to the new software. We try to bring the site up and just keeps crashing. And so it basically takes us a month to get it fully functional again. And so that day sitting around that table with champagne and sushi, that's just like day one. And by 30 days in, most people aren't even trying to get the site back up anymore.

There's maybe five of us who are still trying. And we did. I think that was a really powerful moment for me. I think in the first two days myself and Rich Schumacher, one of the other engineers, we had to write a caching system from scratch, which got us half the way up. Really a terrible way to do software on a side note. I'm not recommending this to anyone. This was a series of anti-patterns kludged into a launch. But we got it partially up, but we had to restart it every 12 hours.

Every 12 hours, every server had to be restarted even with the caching mechanism. And then about three weeks after that, I finally figured out what the core bug was, that was bringing us down every 12 hours. It was this incredibly simple issue that had just been hard to debug, basically related to the way that Python initiates variables used as default parameters... We finally figured it out and it was just really remarkable experience pulling through. And you know what? The company still went to zero. So we had this at launch. I think we did this heroic, heroic stretch to get it working.

A couple weeks after that, a new CEO came in, did a round of layoffs. This is back I think 2012. The team nine months after I started was down to 30 people from about a hundred and it went downhill from there, from a business perspective. But we launched a lot of functionality, has really learned just a tremendous amount. And it kind of shaped what I think about in terms of early in your career, getting learning and going into a company that is maybe having a rough time.

I became a manager two and a half years into my career. Basically running the entire engineering team there because everyone who had a lick of sense quit or got laid off, and it was just complete idiot me trying to be the manager for the engineering org, wasn't qualified and no one would've given me that job, but I was the only one dumb enough to take it at that point. I learned so much and I really the kernel that turned into my entire career where it was that opportunity, even though at the time it was pretty grim.

---
