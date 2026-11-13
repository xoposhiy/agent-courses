# Interpreting Evaluation Results Together

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/txe2fim/interpreting-evaluation-results-together) · [Raw file](../../raw/lessons/txe2fim.html)

Retrieved: 2026-11-13T17:26:06.972010+00:00

[00:01] Throughout this module, you've built evaluations that look at
different parts of an agent's work.

[00:05] You can check an individual tool call, the trajectory of a run,
requirements that carry across a conversation,

[00:12] and the state the agent ultimately changed.

[00:14] Now let's see what happens when you put those checks
together on the same task.

[00:19] Take a Northwind customer who says early in the conversation,
"Don't refund anything until I confirm the amount."

[00:25] The agent verifies the customer, looks up order 4521,
and finds that the refundable amount is $49.99. So far, so good.

[00:33] But then it calls process_refund immediately,
before the customer has confirmed anything,

[00:37] and tells them your $49.99 refund has been processed.

[00:41] When you check the database, the refund is there for the correct
amount and the correct order. So, several evaluations pass.

[00:48] The agent chose the right refund tool,
using the correct order and amount.

[00:52] Customer verification happened before the refund,
and the expected state change exists in the database.

[00:58] but the session-level check fails because the agent ignored an
instruction the customer gave earlier in the conversation.

[01:04] That combination of results tells you something very specific about
the failure. The problem isn't which tool the agent chose.

[01:11] It isn't the refund amount, the identity check,
or whether the refund actually happened.

[01:16] The problem is that a constraint established earlier in the session
was no longer being respected when the agent acted.

[01:23] This also helps explain why an overall score by itself can sometimes
hide the most useful information.

[01:29] Imagine two Northwind runs both received three passing evaluations out
of four. In the first run, the agent used the wrong order ID.

[01:37] In the second, the refund was correct,
but the customer wasn't verified first.

[01:42] The pass rate might be identical, but those are two
very different failures.

[01:46] one points you towards how information is being passed into a tool,
while the other shows you how the agent is sequencing required steps.

[01:53] When you evaluate a complex agent, the individual results help you
locate where the task broke down.

[01:59] That brings us back to the evaluation process you've been using
throughout the course. You still begin by investigating what happened.

[02:06] For a simple response, that might mean reading the answer.

[02:09] For the kinds of tasks you've seen in this module, it can mean opening
the trace, looking at the tool calls, reconstructing the trajectory,

[02:16] checking earlier turns in the session,
or looking at the state in the database.

[02:20] Then you define what correct behavior should have looked like.
Maybe the right Order ID should have been 4521.

[02:26] Perhaps verification had to happen before process_refund,
or the customer's instruction had to remain active.

[02:33] or maybe the task wasn't complete unless a refund
row actually appeared.

[02:37] Once that expectation is clear, you can evaluate it at the scope where
the relevant evidence exists.

[02:43] That's the deeper pass through the evaluate stage you've been
working on in this module.

[02:47] You're no longer asking only, "Was the final response good?"
You can ask, did the agent choose the right action?

[02:54] Did it use the right information? Did all the required steps happen?
Did they happen in the right order?

[03:00] Did the agent preserve important context across turns?
And did the task produce the state it was supposed to produce?

[03:07] Think back to the shelter example you started this module with.

[03:10] If the agent says, "You're booked with Pepper for Saturday at 2 PM",
you now know that evaluating that response is only the beginning.

[03:18] You can check whether it used the right volunteer record,
whether it checked eligibility before choosing the dog,

[03:24] whether the booking happened after those requirements were satisfied,
whether a constraint from an earlier turn was still respected,

[03:30] and finally, whether the booking actually exists.

[03:33] That's what it means to find and evaluate failures along the way
to completing a task.

[03:38] And once your evaluations can tell you where the agent succeeds
and where it breaks down,

[03:42] you have something more useful than a final score.

[03:45] You have evidence about what needs attention. In the next module,
you'll take that evidence into the improvement stage.

[03:52] You'll choose a behavior to improve, make a targeted change,
compare the new version with the old one,

[03:58] and check whether you fixed the problem without creating another
problem somewhere else.

[04:02] See you in module 5.
