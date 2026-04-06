# Albert Cheng — Finding hidden growth opportunities in your product | Albert Cheng (Duolingo, Grammarly, Chess.com)
*Theme: ai-practical | Extracted: 2026-04-03*

## AI-powered text-to-SQL Slack bot democratizing data access

Lenny Rachitsky (00:16:34): Well, let me follow this thread on AI and how you're using AI to help you figure this out. That is very cool. Talk about that.

Albert Cheng (00:16:40): I think one of the latest things that we've been tinkering around with is this text to SQL capability. It's actually pretty powerful. We have this data request Slack channel where for the longest time, and this is still true today, people will toss in all sorts of just one-off questions. How many subscribers do we have in South Africa? Or how long did somebody play puzzles last month or something?

And these ad hoc questions, they often take a lot of human time to just go in and a data analyst needs to prioritize it and find time to go run the query. And yes, you can invest in self-serve tooling to improve at this, but also I found that AI is quite good at doing that first pass answer as well. And so we're working on training some of these Slack bots to essentially be the first party provider of a lot of these answers, which makes the company as a whole lot more data informed, I guess.

And I think what's also kind of interesting is that just human nature is that if you have a question that you feel like you might be a bit embarrassed to ask or you don't want to bother someone, you just don't ask the question. And so by the nature of having these tools, you get actually a pretty large explosion of questions being asked. And I think you see this in ChatGPT too, right? It's like just having a thing that you can converse with that you feel comfortable in makes a huge difference.

Lenny Rachitsky (00:18:03): Okay, this is extremely cool. So is this something you build basically it's a Slack bot that gives you the SQL query or does it actually do the analysis for you?

Albert Cheng (00:18:12): No, it does the analysis. Yeah.

Lenny Rachitsky (00:18:32): Are there other examples of that kind of stuff that you've done or seen?

Albert Cheng (00:18:32): An adjacent example is a lot of the product managers, we're tinkering around with all sorts of different prototyping tools right now. It's just like go from an idea to a representative solution. Today, there's a lot of humans involved in taking an idea, writing up a spec, doing a review, doing design, et cetera.

And so for us, we've invested a bit in at least carving out the main screens of our product experience, things like our onboarding flow, our home screen, our chessboard as an example, and building essentially AI prototypes of those using tools like a V0 or a Lovable. And when you have those foundational pieces, you can then share them with the rest of the company and they can use that as a starting point and then they can try to put their ideas on top of that and then they become a lot more discussable and hopefully testable relatively soon.

Lenny Rachitsky (00:19:25): What's in your AI stack along those lines?

Albert Cheng (00:19:27): The PMs are mostly using V0. The designers love Figmas, they're using Figma Make. The engineers are using a combination of tools right now. So Cursor, Cloud Code, GitHub, Copilot. Marketing teams use all sorts of tools for translation, subtitles, content adaptations, et cetera. Customers support uses Intercom then. So there's quite a lot of tools that are used across the company.

I would say though that something that is annoying to me is that we haven't yet figured out the bridging from the tinkering to the workflow quite as seamlessly as I would like. And so each sub-function, even though the common I guess wisdom now is that AI is going to strip away these functional titles. It is true that based on your experience, you may gravitate to using a type of tool more. And if that tool isn't as interoperable with some of the other tools that you need to pass down the chain to actually ship it into production, at least at our scale.

I think for smaller startups, sure, PMs should just go ship it, but for us, we are still doing some handoffs between functions. I expect that to change over time and we are investing in some of design system components and MCPs and stuff to make it a little bit easier. But yeah, it's an investment and it takes time to smooth things out.

---

## How AI accelerates the growth experiment cycle

Lenny Rachitsky (00:51:19): Okay. Let's go back on track to where we were going. So this was how AI is impacting chess.com. How is AI changing just the work of a growth person?

Albert Cheng (00:51:30): I like to describe growth as the job is to connect users to the value of your product. And in order to do that, what I like to do is think about that user journey again, and essentially, staff teams that are oriented around each element of that user journey. And those teams have specific metric goals, they have roadmaps, et cetera. And then they go run against them.

So that's how it's structured. AI, I think can be applied to speed up some elements of that essentially experiment cycle that you get through. So one example is in product discovery. As opposed to core product, which tends to have longer timeframes, and you might do thorough user research or market research. It's more foundational, more for first principles, et cetera. Growth is a little bit less like that.

It's like you're running a lot of experiments and the output of any given experiment is the input to your next idea. And so historically, I don't even mean historically, but just a few months ago, we were operating in a, that's history, I suppose, but there would be a lot of manual writing of these analysis docs. You'd have to read them, you'd have to understand what insight you want to grab from them and then write another spec to translate that idea. That's still happening to some degree, but I think that's a spot where even tools like ChatGPT are super helpful.

You can just plug in like an analysis that another person wrote and just have it summarized for you and give you advice on ideas to go try. And so that ideation, that research cycle was much, much faster. I talked a little bit about prototyping also just becoming much, much faster than before. We have not yet gotten to the point where product managers themselves are actually shipping the code into production, but it's dramatically shortened the amount of time it takes to conceive of especially a bolder idea that you might have.

And so when I talked earlier about explore and exploit, a lot of the explore was harder to do, but now it's a little bit easier to do. You can take a broader concept and visualize it, and when you can visualize it, send it around the team, get people to click around it, that makes a world of difference.

---
