# Ronny Kohavi — The ultimate guide to A/B testing | Ronny Kohavi (Airbnb, Microsoft, Amazon)
*Theme: org-strategy-leverage | Extracted: 2026-04-04*

## Institutional memory and quarterly experiment reviews

Lenny (00:19:23): What advice do you have for people to actually remember these surprises? You said that a lot of it is institutional. What do you recommend people do so that they can actually remember this when people leave, say three years later?

Ronny Kohavi (00:19:34): Document it. We had a large deck internally of these successes and failures, and we encourage people to look at them. The other thing that's very beneficial is just to have your whole history of experiments and do some ability to search by keywords.

So I have an idea. Type a few keywords and see if from the thousands of experiments that ran... And by the way, these are very reasonable numbers. At Microsoft, just to let you know, when I left in 2019, we were on a rate of about 20 to 25,000 experiments every year. So every working, day we were starting something like 100 new treatments. Big numbers. So when you're running in a group like Bing, which is running thousands and thousands of experiments, you want to be able to ask, "Has anybody did an experiment on this or this or this?" And so that searching capability is in the platform.

But more than that, I think just doing the quarterly meeting of the most successful... Most interesting, sorry, not just successful, most interesting experiments is very key. And that also helps the flywheel of experimentation.

Lenny (00:17:01): I feel like you feed that into ChatGPT, and you have basically a product manager creating a roadmap tool.

Ronny Kohavi (00:17:01): In general, by the way, a lot of that is institutional memory, which is can you document things well enough so that the organization remembers the successes and failures, and learns from them?

I think one of the mistakes that some company makes is they launch a lot of experiments and never go back and summarize the learnings. So I've actually put a lot of effort in this idea of institutional learning, of doing the quarterly meeting of the most surprising experiments.

By the way, surprising is another question that people often are not clear about. What is a surprising experiment? To me, a surprising experiment is one where the estimated result beforehand and the actual result differ by a lot. So that absolute value of the difference is large.

Now you can expect something to be great and it's flat. Well, you learn something. But if you expect something to be small and it turns out to be great, like that ad title promotion, then you've learned a lot. Or conversely, if you expect that something will be small and it's very negative, you can learn a lot by understanding why this was so negative. And that's interesting.

So we focused not just on the winners, but also surprising losers, things that people thought would be a no-brainer to run. And then for some reason, it was very negative. And sometimes, it's that negative that gives you insight.

---

## Building experimentation culture via beach head teams

Lenny (00:44:23): And I think the most important point there is if you're not running an experiment, 70% of stuff you're shipping is hurting your business.

Ronny Kohavi (00:44:23): Well, it's not hurting, it's flat too negative. Some of them are flat. And by the way, flat to me, if something is not Statsig, that's a no ship, because you've just introduced more code. There is a maintenance overhead to shipping your stuff. I've heard people say, "Look, we already spent all this time. The team will be demotivated if we don't ship it." And I'm, "No, that's wrong guys. Let's make sure that we understand that shipping this project has no value, is complicating the code base. Maintenance costs will go up." You don't ship on flat, unless it's a legal requirement.

Lenny (01:07:44): Say you're at a company where there's resistance to experimentation and A/B testing, whether it's a startup or a bigger company. What have you found works in helping shift that culture, and how long does that usually take, especially at a larger company?

Ronny Kohavi (01:07:57): My general experience is with Microsoft, where we went with this beach head of Bing. We were running a few experiments and then we were asked to focus on Bing, and we scaled experimentation and built a platform at scale at Bing.

Once Bing was successful and we were able to share all these surprising results, I think that many, many more people in the company were amenable. It was also the case that helped a lot that, there's a usual cross pollination. People from Bing move out to other groups, and that helped these other groups say, "Hey, there's a better way to build software."

So I think if you're starting out, find a place, find a team where experimentation is easy to run. And by that, I mean they're launching often, right? Don't go with the team that launches every six months, or Office used to launch every three years. Go with the team that launches frequently. They're running on sprints, they launch every week or two. Sometimes they launch daily. I mean, Bing used to launch multiple times a day.

And then make sure that you understand the question of the OEC. Is it clear what they're optimizing for? There are some groups where you can come up with a good OEC. Some groups are harder.

---
