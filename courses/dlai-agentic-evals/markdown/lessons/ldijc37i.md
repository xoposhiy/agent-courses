# Why Evals Matter

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/ldijc37i/why-evals-matter) · [Raw file](../../raw/lessons/ldijc37i.html)

Retrieved: 2026-11-13T17:26:04.799047+00:00

[00:00] Welcome to this course on AI evaluation.

[00:03] Knowing how to evaluate applications effectively has become a critical
skill in AI engineering,

[00:08] and I'm excited to share the ideas and methods that will help you put
that skill into practice.

[00:12] AI is giving software powerful new capabilities,

[00:15] but those capabilities also challenge some of the basic assumptions
behind how you build and test software.

[00:21] To see why, let's look at the app you'll be seeing
throughout this course.

[00:25] It's a support agent for Northwind Apparel,
a fictional clothing retailer.

[00:29] The agent helps customers find suitable products,
checks what's in stock, and adds items to their carts.

[00:35] As a responsible engineer, you need to know that the app does those
things correctly and reliably, so you need to test it.

[00:40] With traditional code, you write explicit rules
for what should happen,

[00:44] then test different inputs to see whether you get
the results you expect.

[00:48] And for deterministic code, the same inputs under the same conditions
give you the same results.

[00:53] But imagine you want the app to recommend clothes for a customer's
winter camping trip by reading their request

[00:58] and making a judgment about what they'll need.

[01:01] That's harder to write rules for and would typically
require human intervention.

[01:05] Of course, now an LLM can do that work and even explain why those
clothes are a good fit for the trip.

[01:11] And it can go beyond simple judgments.

[01:13] You can give an agent the goal of helping a customer put together a
new winter camping outfit,

[01:17] along with Northwind's instructions and tools for searching the
catalog, checking stock, and adding items to the cart.

[01:23] It can then decide how to use those tools as it works towards
that goal on the fly.

[01:28] With LLMs, a relatively small set of new abilities opens up a huge
range of possibilities for what you can build.

[01:34] But the same capabilities that let you build so much more also make it
much harder to know whether you can trust what you've built.

[01:41] Let's look at some of the reasons why.
For one, it's harder to predict how the model will behave.

[01:47] When you test traditional code, you expect the same test to give you
the same result if nothing has changed.

[01:52] But LLMs generate responses probabilistically,
so even with the same input, you can get a different result.

[01:58] For example, the Northwind agent might recommend suitable cold-weather
clothing for a winter camping trip.

[02:04] But run that same test again and it might recommend
cargo shorts instead.

[02:08] So, passing the test once doesn't tell you whether you can depend on
it to keep making suitable recommendations.

[02:14] And you can't guarantee consistent behavior just by writing better
prompts because you're relying on a model to follow instructions,

[02:20] but they're not enforced the way a hard rule in code can be.

[02:24] The second big reason is that mistakes can be harder to spot. With
conventional code, you've written the process the application follows.

[02:31] If the Northwind agent recommends some products and adds them to
the customer's cart,

[02:35] you might take that as a sign that your code is working.

[02:38] But with LLMs, your code can run to completion while the agent goes
about the job in a completely incorrect way.

[02:44] And you don't automatically see how it arrived at that result.
You just see that products were recommended and added to the cart.

[02:51] What if the agent skipped checking the product details
and hallucinated a convincing explanation for why cargo shorts

[02:56] would keep the customer warm on their winter trip?

[02:59] If you're only checking whether the recommendation
and cart update completed,

[03:02] you won't see that it ignored the customer's needs
and invented a product claim.

[03:07] The agent is choosing actions on the fly to reach its goal,

[03:10] and it won't necessarily take those actions in the order
or the way that you intended.

[03:14] As we saw, its behavior is probabilistic,
so it might not even do the same thing on the next run.

[03:20] And on top of that, rules written only in a prompt aren't enforced the
way rules in code can be. You're relying on the model to follow them.

[03:28] So if you want to know whether your application is behaving
as you expect, you need insight into what the agent actually did.

[03:34] You can't tell all of that by just seeing that it reached the end
and updated the cart.

[03:38] And the third big reason these applications are harder to test is
that there's a much wider range of situations that they can encounter.

[03:44] Once people can describe what they want in their own words,

[03:47] you can't articulate every way that they might ask or how
the agent will respond.

[03:52] For example, the Northwind agent might recognize that a customer needs
clothes for winter camping when they say it directly,

[03:58] then miss the winter part when it's buried in a longer
description of the trip.

[04:02] If your tests only used straightforward descriptions,
you wouldn't have caught that problem.

[04:07] And those different requests can lead the agent to
take different actions.

[04:11] It might ask a follow-up question, which gives the customer another
opportunity to respond in a way you didn't anticipate.

[04:17] That response affects what the agent does next,
so the possibilities keep expanding as the interaction continues.

[04:23] You're testing more than a single request followed by a single answer.
That makes choosing your test cases important.

[04:29] You need them to reflect the variety of situations the
app will actually face.

[04:33] You won't be able to anticipate every request or every interaction, so
you also need to keep checking what happens when real people use it.

[04:41] So overall, you're dealing with behavior that can change from run to
run, mistakes that can look like success,

[04:47] and a range of situations that you can't cover in a few examples.

[04:51] Tests that only confirm your code and tools work can
miss these problems.

[04:55] So, how do you build confidence that your application is ready for
real users? Through systematic evaluation.

[05:01] You check your application's responses and actions against what the
task requires, across realistic situations and repeated runs.

[05:09] That gives you evidence of where it performs well
and where it falls short,

[05:12] so you can work on those problems and check whether your
changes actually help.

[05:17] That makes evaluation useful throughout development. While you're
building, you're constantly deciding what to work on next.

[05:23] Should you change the instructions, try another model,
or give the agent a different tool?

[05:28] Understanding where the application struggles helps you decide
where to put that effort.

[05:33] Evaluating it again after a change helps you decide whether to keep
the change or try something else. And you can begin simply.

[05:40] Looking closely at a few examples can reveal problems worth working on
before you've built any formal evaluation system.

[05:46] As you develop the application,

[05:48] more systematic evaluations help you check whether those improvements
hold up across a wider range of situations.

[05:54] And that's what you'll learn in this course,
how to build and use evals in your own projects.

[05:59] We'll focus on why the methods work and give you practice with them in
the labs so you can keep applying what you learn

[06:04] as models and tools change.

[06:06] Over the next two videos, you'll get an overview of how evals work
and how to use them to understand and improve AI behavior.
