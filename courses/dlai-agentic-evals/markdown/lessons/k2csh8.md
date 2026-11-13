# Planning an Improvement Test

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/k2csh8/planning-an-improvement-test) · [Raw file](../../raw/lessons/k2csh8.html)

Retrieved: 2026-11-13T17:26:07.075090+00:00

[00:00] Welcome to Module 5.

[00:02] So far, you've learned how to collect traces, build datasets,

[00:06] and create evaluators that help you see where your agent
succeeds and where it fails.

[00:11] Now, you're going to use all of that to improve the agent itself.
This is the improvement stage of the evaluation process.

[00:18] And there's a little more to that than finding a bad response
and changing the prompt.

[00:22] A change can fix the failure you noticed and cause a new
problem somewhere else.

[00:26] Or you can make several changes at once, see the score go up,
and have no idea which change actually helped.

[00:31] So before you start changing things, it helps to have a plan.

[00:35] You need to decide what behavior you want to improve,
choose a change that might help,

[00:40] and set up a comparison that will tell you what happened.

[00:43] Let's start with what you want to improve. Suppose you run the shelter
agent on your eval set and find several failed matches.

[00:50] Here's one of them: a volunteer has experience handling large dogs.
The dog is a very large Cane Corso that pulls strongly on walks.

[00:58] The agent sees the volunteer's experience and approves the match.
But the evaluator rejects it. Why?

[01:05] Because experience with large dogs is useful information,

[01:08] but the agent never checked whether the volunteer can physically
handle this particular dog now.

[01:13] So that gives you one failure. Now look at a few more. One evaluator
explanation says the volunteer's physical capacity wasn't assessed.

[01:22] Another says experience with large dogs was treated as sufficient.
Another says the dog's pulling strength wasn't considered.

[01:28] Those explanations sound a little different,
but they're pointing to the same underlying problem.

[01:33] The agent is treating past experience as enough evidence
that the volunteer can physically handle the dog.

[01:39] Now you have something much more useful than a collection of failed
scores. You have a behavior you can try to improve.

[01:46] You want the agent to consider current physical handling ability,
rather than approving a match based on previous experience alone.

[01:53] That's one way an improvement target can emerge.

[01:56] You start with failures you've already observed, read the examples
and the evaluator explanations, and look for a pattern worth fixing.

[02:04] Sometimes though, you already know about a capability you
want the agent to gain.

[02:08] Maybe you want the shelter agent to remember that a volunteer said,
"Don't schedule me for walks after six,"

[02:13] and respect that constraint throughout the rest of the conversation.

[02:17] You can write an evaluation for that behavior before the agent can
reliably do it. At first, you may expect it to fail.

[02:24] Then you have a target to work towards as you improve the agent.
You'll sometimes hear this called eval-driven development.

[02:31] An eval that tracks that a previous ability stays around is
called a regression eval.

[02:35] An eval that is looking for a new ability is called a capability eval.

[02:40] So whether the target comes from a failure you've already seen,
or a capability you want to add, the next question is the same.

[02:46] what changes are worth trying. For that, let's switch to Northwind.
We'll use this example for the experiment in the next video.

[02:55] A customer has bought a merino wool sweater
and asks how to care for it.

[02:59] The product tool returns one instruction, Machine washable on wool
cycle, but the agent gives a much longer answer.

[03:06] It recommends cool water, wool-specific detergent,
cedar blocks for moths, and several other things.

[03:12] Those suggestions may sound reasonable,
but the catalog didn't provide them.

[03:16] So the faithfulness evaluator flags the response because some of the
product claims aren't supported by the information

[03:21] the agent retrieved.

[03:23] Now look at the agent's instructions. The current prompt doesn't say
that product details have to be supported by tool results.

[03:30] That gives you a reasonable change to test. You could add,
never state a product detail unless a tool result supports it.

[03:37] For the sweater question, that should push the agent to stick to the
care instruction it actually retrieved.

[03:42] But be careful not to jump to any conclusions at this point.

[03:45] The missing instruction doesn't prove that it caused the agent to add
those extra recommendations.

[03:50] And adding the new rule doesn't prove the problem will go away.
What you have is a hypothesis and a specific change you can test.

[03:57] Now you need to decide how you'll test it. Suppose you update the
prompt, run your evals again, and the score goes up by eight points.

[04:05] That sounds good, but imagine that you also changed the test cases,
or rewrote the evaluator, or switched models at the same time.

[04:12] Now, it's much harder to tell what produced the improvement.
So for this experiment, keep the comparison stable.

[04:18] Run the original agent and the updated agent on the same cases,
using the same evaluators.

[04:23] And because you're testing a prompt change, keep the model
and the rest of the agent configuration the same, too.

[04:29] You want the new grounding rule to be the meaningful difference
between the two versions.

[04:34] There's another piece to planning the comparison.
Think about which cases you're going to include.

[04:39] You definitely want failures you're trying to improve.

[04:41] For Northwind, that includes the wool care question,

[04:44] and other cases where the agent added product details that weren't
supported by the tool results.

[04:49] Those cases answer one question: does the updated agent handle
something the original agent got wrong?

[04:54] But if those are the only cases you test,
you're missing half of the picture.

[04:58] A prompt change can improve those failures and still damage behavior
that was already working. So you also want some known-good cases.

[05:06] Maybe the original agent already handles basic sizing questions
and straightforward product-information requests correctly.

[05:13] Keep those too. Now you can ask a second question:
does the updated agent still handle the things it was already good at?

[05:20] You can think of the first group as your capability cases. You want to
see those improve. The second group protects you against regressions.

[05:28] You want to keep those working. And before you start iterating,
decide what kind of result would actually be good enough.

[05:34] That depends on your application. For one agent,
a small improvement might be enough to justify a change.

[05:41] For another, a particular safety or policy requirement may need to be
almost perfectly reliable before you're comfortable shipping it.

[05:48] The important thing is to decide what matters before you
look at the new results.

[05:53] Otherwise, it's very easy to keep changing the system simply
because you can still find something to improve.

[05:58] So now you have the pieces you need for the experiment.

[06:01] You know the behavior you want to improve, You have a candidate change
based on the evidence you saw,

[06:06] and you have a comparison that can tell you whether the target
behavior gets better and whether something else gets worse.

[06:13] In the next video, you'll run that comparison on Northwind.

[06:16] You'll save the cases, test the new grounding rule,
and then look closely at what changed.

[06:21] As you'll see, the answer is a little more interesting than
just the score went up.
