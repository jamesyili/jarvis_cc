# Adriel Frederick — Humanizing product development | Adriel Frederick (Reddit, Lyft, Facebook)
*Theme: decision-making | Extracted: 2026-04-04*

## Algorithms need human judgment for strategic constraints

Adriel Frederick: Let me refine that a little bit more. It's more about giving people the information that they can use for decisions that they alone are good at and giving machines the power to amplify a person's intent. So one of the ways I like to think about it is all software in any form including ML, is just a tool like a screwdriver and you could try to put a flat head into a Phillips and maybe it'll work a little bit but it's better to use a Phillips screwdriver. And we're tool designers generally and especially in part development function, you figure out how much do I put into the tool and how much do I leave it up to the person and I give the person the ability to choose what they want to do. I give them a screwdriver, a flathead, a Phillips, a torques and you let them decide how they want to use the tool for the application at hand.

And so going from that analogy to concretely with ML you say look, machine learning's going to be amazing at optimizing for a given objective, but it's not going to understand the constraints or strategic choices I need to make. The constraints and strategic choices that we need in the external world are always going to have to be decided by a person. You make that incredibly easy for people to do and intuitive for them to do and then you go that algorithm can then amplify their effect by making decisions on hundreds of thousands, potentially millions of individual decisions to take that person's intent and amplify it given all the information that they can learn in that single context. So I think about it as designing an interface and make it an extension of yourself rather than a black box on its own that you just need more information to.

Lenny: Is there an example that comes to mind where you did that or didn't do that well or someone on your team should have? Just something to make it a little more concrete even.

Adriel Frederick: Let's assume that you are a person working on pricing and you say like, great, I have an objective that is I would like to win market share in a region. And you left that to an algorithm to say I need you to optimize prices such that you maximize market share, but what would the algorithm do? Drop your prices to the floor. All the way to the floor, and then you don't make any money. Okay great. So then you say, okay, what's the next step of that? Let's give it a constraint. Let's set some target that we might want to have for how little profit that you might be willing to take. Okay, go do it now.

What if the guy on the other side is doing the exact same thing? Both of you will hit your constraints and then the game will stop. Okay great. So now it then flips to, oh we have to choose where we want to win. And so I think one of the things we did that I'm particularly proud of is building products that help people see and understand that game a little bit more and decide where they want to.

---

## North star metrics as organizational rallying cry, not precision

Lenny: Facebook is famous for this kind of activation milestone of getting 10 friends or seven friends, whatever it was, like there's some number friends you got to get and the good things will happen. Were you involved in that? Do you have any insight into how that came to be? Is that real?

Adriel Frederick: That decision came before me. I saw it. I understood the data and I worked on this problem. What I thought was brilliant about that was not the metric, it was the designing it to be understood and communicated. What I think is fabulous about it is that you are talking about it now because it's memorable and it got people to take the right actions to start chasing the goal. There was literally nothing magic about the number or the date, but basically it was a way of saying like get people as many friends as possible as fast as possible. And if you said that generically to someone, they'd be like, Yeah, I kind of get it, but yeah, I'll go do that.

When you create a discreet number and a discreet time and there is a concrete goal to chase and there's a number and a graph that everybody can look at and see, we are going to go make that thing go up, the organizational effect of that is galvanizing. So what I thought was brilliant about it is, and as I've heard the stories, this is all secondhand. There was a lot of debate about what the number should be, what timeframe should be, and at some point Zuck just said 10 friends, 14 days, go. And it just got people past the academic debate of like, All right, got it. As many friends as possible, the fast as possible, let's go.

Lenny: I love that. That's exactly how I've always thought about it, that it's not the number exactly, it's just a rallying cry that everyone can just get around and just go, doesn't need to be this perfect number that has incredibly correlated link to retention or anything like that. It's just like, this is good enough. It's directionally I'll just try to do this. Let's just go.

There are downsides of it. Some of them are really funny. I remember looking at a graph of retention versus number of friends and what actually dropped with 11 or 12 versus 10 because somewhere in code, somebody had done something with 10 friends is the limit to help improve retention. And it shut off at 11 or 12 and it came back up, but I was like, You know what, that's fine. That's completely fine. Because if we didn't get that organizational momentum, that graph would've just been lower. So I could take the kink where it drops, it's fine.

---
