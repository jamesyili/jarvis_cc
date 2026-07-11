# Albert Cheng — Finding hidden growth opportunities in your product | Albert Cheng (Duolingo, Grammarly, Chess.com)
*Theme: product-strategy-growth | Extracted: 2026-04-03*

## Explore-exploit framework for finding growth opportunities

Lenny Rachitsky (00:09:42): There's a very specific framework that as we were chatting that I think would be really helpful for people to hear and learn from you. You call it explore and exploit. I think there's a bunch of different ways to think about this. Talk about this framework and how that informs the way you think about growth.

Albert Cheng (00:09:56): Yeah, I initially came up or heard with, heard about explore and exploit through my engineering partner at Grammarly, Nermal, and I think he actually had taken some reforged classes. So maybe the original inventor of it might be Brian Balfour, who I know has been on your pod. But anyway, it's a great concept.

The gist of it is that when you're in exploratory mode, think of it as finding the right mountain to climb. And then when you're in exploitation mode, it's like focusing your resources on climbing that mountain effectively. And certain companies, I think the warning is to basically spend too much of your time on one end of the spectrum. If you do too much exploration, you can have your team feel a little bit too scattershot, just trying a hundred different random ideas.

What's the through line? What's the strategy? How do you pattern match successes across them? And if you do too much in exploitation, which is often the MO of growth teams, it can lead to this saturation and stagnation where you're just locally maximizing a thing. And even though this principle of explore and exploit, it's typically thought of as a macro thing. I like to work with my teams more on the insight level. So I'll give you a concrete example.

So I work at chess.com and one of our priorities is to encourage chess players to improve, to learn and improve. So one of the PMs that we have, Dylan, he works on all the learning features. The most used learning feature in our product is called game review. So you play a game of chess, after the game is over, we have this virtual coach that teaches you about your worst moves, best moves, et cetera. And his job is to improve user engagement and retention.

And so he's in this exploratory phase trying to figure out how do I drive more of that type of activity? And what he observes is that 80% of people that review their games actually do so after a win. And that's really counterintuitive to when we initially built the feature. We thought that people would want to use it after losses or to see their mistakes such they could work on their mistakes. That turned out not to be the truth when it came to the human psychology and the actual data of it. And so we made some changes in the product experience.

When you lose a game now as opposed to surfacing your blunders and your horrible stuff that you did, we flip it on its head and so we show you your brilliant moves, your best moves, and we have coach say something encouraging, "Losing, just part of learning, keep it up." That type of thing. That change alone was pretty dramatic for us.

It grew game reviews by 25%, subscriptions by 20%, user retention by a lot as well. So that was fantastic, but the point is that it doesn't just stop there. You have to take that insight, share it broadly across the company. Now, adjacent product managers like the PM working on puzzles can now think about, "Okay, how do I audit these cold patterns in my product and think about making them more positive?"

I can change the success rating, I could tweak some copy, change the color of some buttons, and so you now can take this experiment win and expand it out 10X across your organization and that's the kind of exploitation phase of it. So when done right, you can oscillate between the two until you saturate out of exploitation mode and then you encourage the teams to brainstorm and get more creative again.

---

## User retention as gold for consumer subscription; resurrection mechanics

Lenny Rachitsky (00:28:03): Let me follow this thread of just consumer subscription products. I feel like this is the category that every indie developer dreams of building a product in because it's easy to build. Cool, I'll build an app, I add a paywall, and then they realize this is a lot harder than I thought. From a perspective of distribution and CAx and growth like that, is that the biggest missing piece that people don't get about building a successful consumer subscription product?

Albert Cheng (00:28:31): Yeah, user retention is gold for consumer subscription companies. If you don't retain your users, then a lot of the onus is on getting them to pay on day one, that's super hard. Then you're dealing with totally different business models where you're paying for users, you're trying to aggressively upsell them before they hit any habitual usage patterns with your product.

A lot of apps naturally do that because that's how they break the mold and get their first users to do it, but I don't know, I've been fortunate to join companies after that initial phase, but especially take Duolingo and Chess.com, these are organic word of mouth driven businesses and in both ways, they grew the market from a much smaller market and as opposed to it being a very competitive space where you're competing and taking market share from others and bidding for higher terms and stuff like that.

Lenny Rachitsky (00:29:26): So what I'm hearing here is you need to find a way to grow through word of mouth for this to have any chance of success and also retention needs to be very high. Do you have a heuristic of what retention needs to be for you to have a chance building a successful consumer subscription business?

Albert Cheng (00:29:42): I think consumer companies tend to track essentially two main types of user retention. There's more of the new user, one, D1, D7, et cetera. I think when you have your D one retention somewhere around the 30 or 40% mark, that's quite solid I think for a consumer app. If it's much lower than that, then sometimes I might question the intent of the user or the ability for that, you to I guess acquire just mathematically acquire enough users such that you can grow a big enough daily active user base.

Lenny Rachitsky (00:30:14): That's surprisingly low.

Albert Cheng (00:30:16): Yeah. It's achievable. It's achievable in theory, but there are so many options out there in the market and people are feeling a lot of app and product bloat. And I think especially if you have a product that has daily frequency, that's actually the retention that matters the most is that of your existing user base that has developed a habitual pattern, how sticky is your product? And it's that retention rate that really compounds and builds that daily habit.

So over time, especially when companies mature a little bit, you actually focus most of your energy on the existing user retention mechanics. You find that that's a much, much bigger lever. One exception is that Grammarly was a different type of product and that you install it and you don't proactively open it every day. So that was interesting to me because I assumed that you should always just focus on existing user retention, but for a product like Grammarly, it's actually the activation installation aha moment that's really, really critical and will carry the user for a very, very long time.

---

## Freemium sampling strategy that doubled Grammarly upgrade rates

Lenny Rachitsky (00:20:42): I want to come back to this topic of how things have changed and how you work as a product person, as a growth person across the companies you've been at. But first of all, I want to talk about another example of finding growth wins and monetization wins. Noam Levinsky, who is Chief Product Officer at Grammarly, you worked with him for a while while you were at Grammarly. He said that I need to ask you about the biggest monetization win that you found at Grammarly and how you discovered the opportunity.

Albert Cheng (00:21:10): I had the pleasure of working with Noam and his product team at Grammarly. Some context first for those that don't use Grammarly. So Grammarly is an AI-powered writing assistant. And so typically, people will use it as a Chrome extension or a downloadable desktop client. And basically what it does is it overlays your writing with a bunch of different corrections.

Grammarly is a freemium business model, which means that over 90% of our users are on the free service and the rest of it pay for subscriptions essentially, right? And so one of the teams, they work on subscriber conversion, PM there is Kayla, that team is great and their job is to figure out the free to paid subscription path.

And so one of the realizations, one, is that we weren't actually tracking the events that well for the types of essentially suggestions that people were getting and how often were users seeing paywalls and stuff like that. That's kind of step number one. We have to put that instrumentation in.

And so the observed behavior from all that tracking and data was that actually a very small percentage of our free users was deciding to accept all of their suggestions. They were more picking and choosing as they go.

And then the second thing, which is I think equally if not more interesting is that I was at this company during this generative AI transformation, which is obviously still going on. And quite frankly, both the company brand as well as the lived product experience for most of the free users was that Grammarly was just a product to fix your spelling and grammar because those were the free suggestions we were showing people.

And so we decided to flip that on its head entirely and we said, "Okay, what if we actually sampled a number of different paid suggestions and interspersed them to free users across their writing?" Such that they were intermingled and we would provide a limited taste of what the paid offering had to provide. And on the surface, even though it's rational, the concern is that if we give too much of this away, then will people want to subscribe?

And we found completely that was not the case all of a sudden, people were seeing Grammarly as a much more powerful tool than they were before and our upgrade rates nearly doubled just through this change. And so I think this is interesting, just modernization learning that especially if you work on a freemium product, try to have your free product be a reflection of everything that your product can offer you. Obviously to an extent there's some costs involved with some of the paid features and things like that, but it generally will pay for itself if you're able to put your best foot forward and go do that.

Lenny Rachitsky (00:24:51): It's basically a reverse free trial but in real time while you're writing as opposed to a time-based one.

Albert Cheng (00:25:04): Yeah, so we adopted some patterns that are in the industry, but molded it to Grammarly's specific use case.

---
