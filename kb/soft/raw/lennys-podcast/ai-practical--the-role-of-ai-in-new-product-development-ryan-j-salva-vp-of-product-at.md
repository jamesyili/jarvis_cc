# Ryan J. Salva — The role of AI in new product development | Ryan J. Salva (VP of Product at GitHub)
*Theme: ai-practical | Extracted: 2026-04-04*

## What Copilot is and how it keeps developers in flow

Lenny (00:11:15): What I'm most curious about, and we're going to spend time on this, is just how a product like this comes to be at a larger company. But before we get into that, what's the craziest story of someone using Copilot to write code? And I'll share one real quick... I'm curious, what have you seen?

Ryan J. Salva (00:12:15): Developers for the last 20 years or more have had essentially simple, intelligent autocomplete. You hit the period and you get the next variable that might come up. It's helpful for moving a little bit faster through your code, helpful sometimes for remembering what the particular syntax might look like for a method or a function. Copilot is essentially that magnified by many lines of code. It is multi-line autocomplete that is fundamentally powered by an AI model called CodeX, which is a derivative of another one that you might be familiar with, GPT-3.

When you are in the editor, it could be VS Code, it could be IntelliJ, it could be them, essentially, as you are typing, Copilot will provide suggestions usually in kind of this italicized gray text that is really, to your point, kind of magical what it's able to infer. Based upon the variables around it, the class names, the method names around it, your comments, Copilot infers what you intend to create, and then hopefully does a pretty good job at nailing it by providing scaffolding code template that you can then riff on. Now, what we tend to find is that developers love it. They really enjoy it. They kind of find themselves getting a little addicted to it because it helps them stay in the flow.

As developers, we love to be in that place. I love to be in that place where I'm creating things, where I'm focusing on some product, some piece of software that I'm going to give to my customers, my users. The labor of remembering what's the order of parameters that need to come into a particular API, or hey, what's the particular syntax of this thing I'm supposed to do, or oh, I've got to create a bunch of dummy data that is days of the week or months in the year. That's just labor. It's not creating. It's just typing.

Copilot helps developers stay in the flow by bringing all of that information into the editor, preventing them from having to go check out documentation or watch tutorial or go to Stack Overflow and either find an answer or worse, have to ask a question and wait for an answer. It just brings all of that into the editor and gives the developer often multiple suggestions that they can choose from and just pick and choose what is the right solution to solve the problem for the thing they're trying to create.

---

## Future of AI in the dev stack: augmenting not replacing developers

Lenny (00:44:40): Wow. What this makes me think about is your team is at the forefront of AI in this applied way. I'm curious what your thinking is on just where this goes for developers especially. I saw a stat that maybe 40% of people's code is now written by Copilot. I don't know if that's right. But is the vision in the future becomes something like 90? Where do you see this all going?

Ryan J. Salva (00:45:02): Just to put a fine point on that stat, it is 40% is specifically for Python developers. Candidly, it varies depending upon the language. Because as you might imagine, some languages have better representation in the public domain than others. And usually both the volume and the diversity of training data correlates with the quality of suggestions, which is then represented by either the number of lines written or the acceptance rate or any one of a number of other metrics.

Ryan J. Salva (00:45:58): It does. It enables even mediocre developers like myself to be able to do some pretty amazing things. But where's it going? First, I think, I hope it's obvious to most developers that AI is going to infuse pretty much our entire development stack in the not so distant future. Copilot is really just the very tip of the sphere for a lot of innovations and better managing maybe our build queues or helping to... Here's a great one. I don't know about you, but often the comments that I get with commit messages and PRs aren't super great. It puts a lot of effort onto the code reviewer to go figure out what the developer was actually trying to do. What if AI could summarize all of your changes with your full request and you just have to, as the contributing developer, just review it to make sure it's accurate, send it on its way, and you don't have to put in extra effort for that.

There are lots and lots of different opportunities for AI to essentially be able to take some of the drudgery out of our work so that we can focus on creative acts. What I hear from developers and what I experience myself is that Copilot kind of forces me to think a little bit more about what are the design patterns I'm trying to create? What is the end user experience or the outcomes that I'm trying to drive with my code, and that I can rely on Copilot to scaffold out a lot of that so that I can focus on more creative work? That is really what I hope for our industry five, 10 years from now, is that not only will we be inviting more developers or more people to become developers by essentially providing a layer of abstraction a little bit, or at least a little bit of a hand in development, but that also the really experienced developers are focusing on much larger problems and focusing on outcomes and creativity rather than really low level difficult rote memorization of things like syntax or ordering of parameters and the like.

Ryan J. Salva (00:52:17): We do not want Copilot auto generating code where a thinking, reasoning, breathing human being is not on the other side of that keyboard making recent decisions. We do not want Copilot to replace any other part of the stack, whether it is static analysis tools or your unit tests or whatever kind of measures you're putting in today to make sure that your humans produce good quality code. We want you to keep all of those same systems in place to make sure that humans who are leveraging tools like Copilot continue to produce that good quality code.

---

## Prompt crafting and latency optimization as core AI product work

Ryan J. Salva (00:25:27): Creating the model is one thing, but then figuring out how to use the model in terms of what parameters do you want to adjust for, what do you want to optimize for in terms of... A great example of this is performance, right? When you're in a code editor, you don't necessarily want to type, type, type and then have to wait one second, two seconds, three seconds to get a suggestion back when your entire goal is to stay in the flow. We would run experiments to see how many milliseconds are the right amount such that a developer doesn't feel like they're being interrupted by Copilot and a suggestion.

Lenny (00:26:06): What's the answer to that?

Ryan J. Salva (00:26:09): It seems like right now it's around 200 milliseconds. Depending upon where you're in the world, your latency can go up or down a little bit from there. But it seems like the sweet spot is somewhere around 200 milliseconds.

Lenny (00:26:20): Good to know.

Ryan J. Salva (00:26:22): We also experimented quite a bit. It's not just about the model, but it's also about what you feed the model. How do you prompt the model to return back a useful response? This kind of began a journey of experimentation for what we call prompt crafting.

---
