# Karina Nguyen — OpenAI researcher on why soft skills are the future of work | Karina Nguyen
*Theme: product-strategy-growth | Extracted: 2026-04-04*

## Canvas and Tasks: from prototype to product

Lenny Rachitsky (00:27:06): So talk about how that emerged and let's better understand just how you collaborate with product teams and how OpenAI works in that way, whatever you can share there.

Karina Nguyen (00:27:14): I think Canvas and tasks are going into the bucket of projects where it's more short or medium terms. And actually the way Canvas and tasks came about to be was it started with one person prototyping and creating a spec. It's kind of like PRD. It's like creating a spec of the behavior of the model. I don't think tasks is extremely groundbreaking feature necessarily. What makes it really cool is because the models are so general... Model can now search, they can write sci-fi stories, they can search for stocks, they can summarize the news every day. Because the models are so general giving something familiar to people that notifications is very familiar, having reminders is very familiar. So feeling like a form factor for the people who are very familiar, same as Canvas, Google Docs is very familiar, but then you add magical AI moment and it becomes very powerful.

But the way it comes usually operationally... Yeah, size is like a prototype, literally prompted prototype of how you would want the model to behave. For tasks, for example, you need to design... Literally design thinking is like okay, well, if the user says, 'Remind me to go to lunch at 8:00 AM tomorrow,' what information does the model need to extract from that prompt in order to create a reminder? And so this is how you design a spec for a new feature, like a tool. Canvas and tasks are all tools. So it's like how do you create the tool stack?

And then it's mostly like developing JSON schema. It was like, 'Okay, from this problem maybe the model should extract the time that the user requested.' And then you think about which format do you want the time to be? And then how do you want the model to notify you is basically the user should give instruction to the model. And then this instruction would fire off every day or something at that particular time.

---

## Prompting as product prototyping and iteration method

Lenny Rachitsky (00:26:29): Somebody needs to get on that. Main, it's wild how many features you built that I use every day and that many people use every day. This prototyping point you made is really important. It's something that comes up a ton on this podcast also of how that... is maybe the way that AI has most impacted the job of product builders recently is just prototyping instead of going from showing just like, 'Here's a PRD, here's a design.' PMs are more and more just, 'Here's the prototype with the idea that I have,' and it's working. You can play with it.

Karina Nguyen (00:24:35): I would say prompting is also a way to prototype new product ideas. Early days at Anthropic when I was working file uploads feature, I remember I was just prompting the model to just... I remember we were launching a hundred key contexts. I was just prototyping this in their local browser. I did the demo. People really, really loved it. And they just wanted API for file uploads or something. And then that's when it clicked to me, and also one of the blog posts a long time ago, it clicked on me prompting is a new way of product development or prototyping for designers and for product managers.

For example, one of the features that I want to do is have a personalized starter prompts. So whenever you come to Claude, it should recommend you starter prompts based on what your interests are. And so you can literally do it prompting for that.

Another feature was generating titles for the conversations. It's a very small micro experience but I'm really proud of. The way we did that was we took five latest conversation from the model, asked the model, 'What's the style of the user?' And then for the next new conversation, the generated title will be of the same style. It's just like really little micro experiences like this.

---
