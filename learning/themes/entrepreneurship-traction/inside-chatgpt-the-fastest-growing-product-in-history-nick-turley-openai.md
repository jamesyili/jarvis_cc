# Nick Turley — Inside ChatGPT: The fastest growing product in history
*Theme: entrepreneurship-traction | Extracted: 2026-04-05*

## ChatGPT hackathon origin; shipping in 10 days; accidental product-market fit

Lenny Rachitsky (00:13:53):
Okay. So you mentioned the beginnings of ChatGPT. I was reading in a different interview. So you joined OpenAI. ChatGPT was just this internal experimental project that was basically a way to test GPT-3.5, and then Sam Altman is just like, "Hey, let me tweet about it, maybe see if people find this interesting," yada yada, yada. It's the most successful consumer product in history, I think both in growth rate in users and revenue, and just absurd. Can you give us a glimpse into that early period before it became something everyone is obsessed with?

Nick Turley (00:14:24):
Yeah. So we had decided that we wanted to do something consumer-facing, I think, right around the time that GPT-4 finished training, and it was actually mainly for a couple of reasons. We already had a product out there, which was our developer product. That's actually what I came in to help with initially, and that has been amazing for the mission. In fact, it's grown up. And now, it's the OpenAI platform with, I don't know, 4 million developers, I think. But at that time, it was early stage, and we were running into some constraints with it because there was two problems. One, you couldn't iterate very quickly because, every time you would change the model, you'd break everyone's app. So, it was really hard to try things.

And then the other thing was that it was really hard to learn because the feedback we would get was the feedback from the end user to the developer to us. So it was very disintermediated, and we were excited to make fast progress towards AGI and it just felt like we needed a more direct relationship with consumers. So we were trying to figure out where to start. And in classic OpenAI fashion, especially back then, we put together a hackathon of enthusiasts of just hacking on GPT-4 to see what awesome stuff we could create and maybe ship to users, and everyone's idea was some flavor of a super assistant. They were more specific ideas, like we had a meeting bot that would call into meetings, and the vision was maybe it would help you run the meeting over time. We had a coding tool, which full circle now, probably ahead of its time. And the challenge was that we tested those things, but every time we tested these more bespoke ideas, people wanted to use it for all this other stuff because it's just a very, very generically powerful technology.

So, after a couple of months of prototyping, we took that same crew of volunteers, and it was truly a volunteer group, right? We had someone from the supercomputing team who had built an iOS app before. We had someone on the research team who had written some backend code in their life. They were all part of this initial ChatGPT team, and we decided to ship something open-ended because we just wanted a real use case distribution. And this is a pattern with AI, I think, where you really have to ship to understand what is even possible and what people want, rather than being able to reason about that a priori. So, ChatGPT came together at the end because we just wanted the learnings as soon as we could, and we shipped it right before the holiday thinking we would come back and get the data and then wind it down. And obviously, that part turned out super differently because people really liked the product as is.

So I remember going through the motions of like, "Oh, man, dashboard is broken. Oh, wait, people are liking it. I'm sure it's just going viral and stuff is going to die down," to like, "Oh, wow, people are retaining, but I don't understand why." And then eventually, we fell into product development mode, but it was a little bit by accident.

---

## Making it free + no waitlist as distribution decisions that made history

Lenny Rachitsky (00:36:31):
So, you mentioned that you kind of got stuck with this name ChatGPT. Maybe this is part of the answer, but I'm curious just are there any accidental decisions you guys made early on that have stuck and have essentially become history changing?

Nick Turley (00:36:45):
There's so many and it is funny, because you have no time to think about them and then they end up being super consequential. The day was one, we went from chat with GPT-3.5 to ChatGPT the night before, slightly better but still really bad.

Lenny Rachitsky (00:36:58):
What was it called before?

Nick Turley (00:36:59):
It was going to be Chat with GPT-3.5 because we really didn't think it was going to be successful product. We were trying to actually be as nerdy as we could about it because that's really what it was. It was a research demo, not a product. So, we didn't think that was bad. But I think that in the original release, making it free was a big deal. I don't think we appreciate that because the GPT-3.5 model was in our API for at least six months prior to that. I think anyone could have built something like this. It might not have been quite as good on the modeling side, but I think it would've taken off. So, making it free and putting a nice UI on it, very consequential in the way that you take for granted now. And this is why I think that A, distribution and the interface are continuously important even in 2025.

The paid business, which now it's a giant business both in the consumer space and in the enterprise space. The birth of that was just to turn away demand originally. It was not like we brainstormed, "Oh, what is the best monetization model for AI?" It was really what monetization model or what mechanism would allow us to turn away people who are less serious than the people who are really trying to use it? And subscriptions just happened to have that property and it grew into a large business. I think shipping really funky capabilities before they were polished is another thing where that feels like a tactical decision, but it became a playbook because we would learn so much. Remember when we shipped Code Interpreter, we learned so much after we shipped it. Now it's known as I think data analysis in ChatGPT or something like that just because we actually got real world use cases back that we could then optimize. So, I think there's been a lot of decisions over time that proved pretty consequential, but we made them very, very quickly as we have to, so.

---
