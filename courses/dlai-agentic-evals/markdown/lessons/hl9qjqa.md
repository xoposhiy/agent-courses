# Turning Production Failures into Regression Tests

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/hl9qjqa/turning-production-failures-into-regression-tests) · [Raw file](../../raw/lessons/hl9qjqa.html)

Retrieved: 2026-11-13T17:26:07.591547+00:00

[00:00] In the last video, you saw how production can reveal situations
that never made it into your offline benchmark.

[00:06] Now, let's follow one of those situations all the way through the
improvement loop with Northwind. First, look at the offline results.

[00:14] Suppose Northwind has a policy compliance score of 96%.
That sounds pretty good, and it may be.

[00:21] But before you conclude that the agent handles refunds reliably,
it's worth looking at the cases that produced that score.

[00:27] Most of the refund examples in the test set are very direct.

[00:31] A customer says, "Refund order 1842," or, "I want a refund for order
2271." Those are useful cases.

[00:39] They show that when the customer states the intent clearly,
the agent can recognize the request and follow the refund process.

[00:45] But then, a real customer writes, "I bought this last week
and it doesn't fit. Can I get my money back?"

[00:51] They never used the word "refund", but that's clearly
what they're asking for.

[00:55] So you search the offline dataset for similar examples
and you don't find one.

[01:00] The test set contains explicit refund requests,
but nothing phrased this way. That's an important distinction.

[01:06] It doesn't mean the 96% score was wrong.
The score told you how the agent performed on the cases you gave it.

[01:13] Production has now shown you a case the tests didn't cover.
So let's open the trace and see what happened.

[01:19] The customer says the item doesn't fit and asks for their money back.

[01:23] Instead of recognizing that as a refund request,
the agent responds more like this is a general product complaint:

[01:29] "I'm sorry it didn't work out.

[01:30] Would you like to fill out our feedback form?"
That's a sympathetic answer, but it never enters the refund process.

[01:37] And you can see that in the trajectory. There's no customer
verification, no order lookup, and no refund tool call.

[01:44] So the problem starts before any of those tools come into play.

[01:47] The agent never recognized that this message should trigger
the refund workflow.

[01:51] Now you have something much more useful than a failed production
conversation. You have a concrete behavior you can reproduce and test.

[01:58] Take the customer's original message and add it to your offline
dataset exactly as it appeared:

[02:04] "I bought this last week and it doesn't fit.

[02:06] Can I get my money back?"

[02:07] Keeping the original phrasing matters because that phrasing is part of
what your existing benchmark was missing.

[02:13] Then write down what the agent should do in this case.

[02:16] It should recognize that the customer wants a refund,
follow the refund policy,

[02:20] and perform whatever customer and order checks are required
before processing it.

[02:24] You can then use the evaluators you already have to check those
parts of the behavior.

[02:29] A policy evaluator can tell you whether the refund
rules were followed,

[02:33] and your tool evaluators can check whether the required lookups
and actions actually happened.

[02:38] At this point, something important has changed. This is no longer a
production failure that you happened to observe once.

[02:44] It's now a test case you can run every time you modify the agent.
The trace also gives you a clue about where to look next.

[02:52] The failure happens before the agent calls any refund tools, because
it never recognizes the request as a refund in the first place.

[02:59] So one place worth investigating is the instruction that tells the
agent when to enter the refund workflow.

[03:05] You might also look at the examples the agent has been given.

[03:09] If every refund example says something explicit like
"refund this order",

[03:13] the agent may not have enough guidance for requests such
as "can I get my money back?"

[03:17] That gives you a direction for your next change,
You could clarify the refund routing instruction,

[03:22] or maybe add a few examples that express refund
intent in different ways.

[03:27] The exact change depends on how the Northwind agent is implemented.

[03:31] So you wouldn't want to guess the final fix from this trace alone,
but now you have a concrete hypothesis to test.

[03:37] And when you test it, don't run only the new production case.
run the older refund examples, too.

[03:43] You still want refund order 1842 to work exactly as it did before.
Then run the rest of your known-good cases as well.

[03:51] If you make the agent more sensitive to indirect refund requests,

[03:55] you want to make sure it doesn't start interpreting ordinary product
questions as refunds.

[03:59] So your benchmark has gotten bigger.

[04:01] It still contains the refund cases you already knew about
and the other behaviors you've been protecting.

[04:07] And now it also contains this new production case.

[04:10] That means you should run the updated agent on that expanded benchmark
with the same evaluators.

[04:15] Then look first at the case that came from production.
When the customer says, "I bought this last week and it doesn't fit.

[04:21] Can I get my money back?", does the agent now recognize the refund
intent and enter the right workflow?

[04:26] If it does, check the other refund cases next. Do those still work?
And then look at the rest of the benchmark.

[04:33] Did anything else change that you didn't intend? This is the same
improvement process you've been using throughout the module.

[04:39] The only difference is where this particular test case came from.
It came from a real customer.

[04:44] And if you fix the behavior, you keep the case.
You don't remove it because the problem is gone.

[04:50] That customer has shown you one way that the agent can
fail, and from now on,

[04:54] future versions should have to prove that they don't
bring the failure back.

[04:57] That's how your benchmark gets stronger over time.
Some cases begin as failures you discover during development.

[05:03] Others begin as capabilities you want the agent to gain.
Others come from regressions introduced by your own changes.

[05:11] And yet others come from production, because real users will always
create situations you didn't think to write down in advance.

[05:18] Each time that happens, you can take what you learned and add it to
the next evaluation.

[05:23] By the time you've gone through several rounds of improvement, you're
no longer testing the agent against the benchmark you started with.

[05:29] You're testing it against a record of what you've
learned about the system.

[05:32] the failures that mattered, the behaviors you fixed,
and the cases you now know you need to protect.

[05:38] And that's the improvement stage of the process.
You started this module with the evaluation results already in hand.

[05:45] You had traces, datasets, and evaluators that could show you where the
agent was succeeding and where it was failing.

[05:50] Then, you use that evidence to choose what to improve, make a targeted
change, and compare the new version against the old one.

[05:58] And as you saw, improving your agent is rarely about one
change and one result.

[06:02] A fix can solve the problem you were aiming at and still introduce a
regression somewhere else.

[06:07] So, you inspect what changed, look at the traces,
refine the intervention, and run the comparison again.

[06:13] Once the agent is in production, real users give you new cases to
bring back into that same loop.

[06:19] And that brings us to the end of this course. So let's zoom back out
to the full evaluation framework you've been working through.

[06:27] The first stage in the process was to Observe.

[06:30] You looked closely at what the agent actually did,
found failures in its responses and actions,

[06:35] and gathered the evidence that showed where things went wrong.

[06:37] Then came Benchmark.

[06:39] You took those individual failures and turned them into criteria you
could apply consistently across many different cases.

[06:45] You worked out what should count as a pass, what should count
as a failure, and created examples with the judgments you expected.

[06:52] In Evaluate, you turn those criteria into automated checks
and tested how well those checks agreed with human judgment.

[06:59] Once you trusted the evaluation setup, you could use it to measure the
agent across a larger set of cases.

[07:05] And finally, in Improve, you use those measurements
to improve the system.

[07:10] You found the patterns that mattered, chose where to intervene,
tested changes against the stable benchmark,

[07:15] checked for regressions and trade-offs, and kept adding new evidence
as the agent encountered the real world.

[07:21] And then, the cycle continues. Improve gives you new traces to
investigate. New failures may lead you to refine your criteria.

[07:30] New behavior may require you to update your evaluations, and those
evaluations then give you the evidence for the next improvement.

[07:37] So the four stages connect into one ongoing process: Observe,
Benchmark, Evaluate, Improve.

[07:44] The goal isn't just to know whether an agent is good or bad.

[07:48] It's to build a process that helps you understand the behavior of your
agent, measure it in a way you can trust,

[07:53] and make better decisions about how to improve it.

[07:56] That's the core of the evaluation loop, and that brings us to the end
of this course. Congratulations!

[08:02] I hope you find the skills you've learned here useful as you build AI
applications going forward.
