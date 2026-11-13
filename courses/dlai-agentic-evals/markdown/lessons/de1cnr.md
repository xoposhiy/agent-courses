# Comparing Versions and Assessing Tradeoffs

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/de1cnr/comparing-versions-and-assessing-tradeoffs) · [Raw file](../../raw/lessons/de1cnr.html)

Retrieved: 2026-11-13T17:26:07.183480+00:00

[00:00] In the last video, you planned an improvement test for Northwind.

[00:04] The agent was adding product advice that the catalog didn't support,
so you changed one thing: adding a grounding rule that says,

[00:12] "Never state a product detail unless a tool result supports it."

[00:16] And you decided to test that change on two kinds of cases, where the
agent was already failing, and cases it was already handling well.

[00:24] Like we said, those are capability evals and
regression evals respectively.

[00:28] Now you're going to run that comparison and see what actually happens.
Start by saving the cases you want to reuse.

[00:35] First, take the traces where the faithfulness evaluator found
unsupported product details.

[00:40] The question about the merino wool sweater belongs here,

[00:43] along with other cases where the agent added information
that didn't come from the product tool.

[00:47] Save those as a data set. For this experiment,
we'll call it Northwind faithfulness failures.

[00:53] Then save a second set with cases the original agent
already handled correctly.

[00:58] For example, some basic sizing questions and straightforward product
information requests. Those are your known-good cases.

[01:06] With that, you have one set that can show whether the problem you care
about gets better and another

[01:10] that can show whether you broke behavior that was already working.

[01:14] Next, you need the two versions of the agent you want to compare.
Keep the original version as your baseline.

[01:20] Then, create a second version with the new
grounding rule in the prompt.

[01:24] Everything else stays the same: model,
same instructions, same evaluators.

[01:29] The thing you're testing here is that additional grounding rule.
Now you need a way to run each dataset through the agent.

[01:36] In Phoenix, you do that with a task, which is just a function
that handles one example.

[01:41] For the wool care case, the task receives the customer's question,
runs the Northwind agent, and returns the response.

[01:48] Phoenix can then apply that same function to every
example in the dataset.

[01:52] You write the logic for one example, and Phoenix takes care of
repeating it across the rest.

[01:57] Once you have that task, you can run an experiment.

[02:01] You give Phoenix the dataset, the task that runs the agent,
and the evaluators you want to apply.

[02:06] Phoenix runs the examples, scores the results,
and keeps the traces with them.

[02:11] That last part is useful because when a score changes,
you can go back and see what the agent actually did.

[02:17] Run the baseline and the updated agent on the same cases with the same
evaluators. That gives you something you can compare directly.

[02:24] Let's start with the cases you wanted to improve.
Here's the wool care example again.

[02:29] Before the change, the product tool returned one instruction:
"Machine washable on wool cycle".

[02:34] but the agent added several more recommendations.
After you add the grounding rule, the response is much shorter.

[02:41] It says that the sweater can be machine washed on the wool
cycle, and it stops there.

[02:45] So in this case, you got the behavior you were aiming for.
The unsupported recommendations are gone.

[02:51] That's encouraging, but this is why you also saved the known-good
cases. Go look at those next.

[02:58] Most of them still behave as expected, but a few sizing questions have
changed. The final answer is still correct, which at first looks fine.

[03:06] Then you open the trace. Take a merino sweater sizing question.

[03:10] In both versions, the customer asks the same thing, and in both
versions, the agent already has the sizing information it needs.

[03:18] In the baseline, it uses that information and answers directly.
In the updated version, something different happens.

[03:25] The agent calls the product tool again.
The lookup doesn't give it any new sizing information.

[03:30] Then the agent gives essentially the same final answer as before.

[03:33] So from the customer's point of view, the answer may look just
as good, but the trajectory has changed.

[03:39] The new version did an extra lookup that didn't help.

[03:42] If you only checked whether the final answer was correct,
you'd probably miss that.

[03:47] Now you have something more specific to investigate,

[03:50] The grounding rule may be making the agent think it needs fresh tool
evidence before it can make a product claim,

[03:55] even when the supporting information is already available.

[03:58] That doesn't prove exactly why the model made the extra call,
but it gives you a useful hypothesis for the next iteration.

[04:05] This kind of trade-off can show up in other ways, too.
Suppose you make the shelter agent stricter about eligibility.

[04:12] After the change, unsafe matches go down. Great. But then you notice
that some volunteers who should qualify are now being rejected.

[04:20] If you only looked at one overall score, those two movements could
partially cancel each other out.

[04:25] So when you compare versions, look at the failure categories
separately. What got better? What got worse?

[04:32] And which specific cases changed? Now, come back to Northwind.
You have a real decision to make.

[04:38] A grounding rule improves the behavior you were targeting.

[04:41] The care answer is now supported by the catalog, but the same rule is
also causing extra tool calls in some cases that were already working.

[04:49] Is that a worthwhile tradeoff? There isn't one answer
that applies to every product.

[04:54] If unsupported product claims could seriously mislead a customer,

[04:57] you may decide that stronger grounding is worth an
occasional extra lookup.

[05:01] If the tool calls are expensive or latency matters a lot for your
application, then you may want to make the rule more precise.

[05:08] Maybe the next version should make it clear that the agent can use
supporting information it already

[05:12] has and only needs another look up when that information is missing.

[05:16] That would be another candidate change.
You would test it the same way.

[05:20] Keep the cases and evaluators fixed, run the new version,

[05:24] and see whether the care behavior stays improved while the
unnecessary lookups go away.

[05:29] And again, don't assume the new wording will work just because the
explanation sounds plausible.

[05:34] Run the comparison, and let the results tell you. There's also a
bigger question here: How long should you keep iterating?

[05:41] You can almost always find one more thing to improve,
but each additional change takes engineering time,

[05:47] and that time has to be worth what you expect to gain from it.

[05:50] Maybe the first iteration removes a large cluster of failures,
then the next one fixes a smaller group.

[05:56] Eventually, what remains may be a handful of rare cases
that each require a lot of specialized work.

[06:02] That doesn't mean those cases never matter. A rare safety failure can
be much more important than a common cosmetic one.

[06:08] So look at the value of the improvement, the severity of the remaining
failures, and the effort required for the next change,

[06:15] and go back to the bar you set before you started.

[06:18] Did the new version reach the level of performance you said you
needed? Are the remaining regressions acceptable for this application?

[06:25] If so, you may decide that this version is good enough for now,

[06:29] or you may decide that the extra lookup is important enough to
justify another round.

[06:34] Those are two different decisions.

[06:36] You can keep the improvement you already made and still decide
to keep working on it,

[06:40] or you can keep the change and move on to something more valuable.

[06:43] The important thing is that the decision comes from
the comparison you ran.

[06:47] You can see which cases improve, what changes elsewhere,
and when you need more detail,

[06:52] you can open the traces and see where the behavior started to diverge.

[06:56] That gives you the evidence for what to try next.

[06:59] So far, the change we tested was in the prompt,
but a prompt isn't always the right place to intervene.

[07:05] Sometimes the agent is missing information,
or maybe the tool behavior is the problem.

[07:09] Other times, the workflow itself needs to change, and sometimes,
you may actually need a different model altogether.

[07:16] In the next video, you'll look at different places you can intervene
and how the failure you found helps you decide where to start.
