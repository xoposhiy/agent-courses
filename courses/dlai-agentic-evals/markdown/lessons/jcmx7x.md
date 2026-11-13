# Building Code Evaluators

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/jcmx7x/building-code-evaluators) · [Raw file](../../raw/lessons/jcmx7x.html)

Retrieved: 2026-11-13T17:26:05.770122+00:00

[00:01] Welcome to module three.

[00:02] In the last module, you explored how to define requirements
and build test cases,

[00:07] and you saw how to review the results manually for errors
and group similar mistakes together.

[00:11] Reviewing results manually helps you develop a nuanced understanding
of where an application falls short of its requirements.

[00:18] When you personally see how it goes wrong and what details matter,

[00:21] you can use that understanding to make more informed decisions about
what needs to improve.

[00:27] But manual review takes time and focused attention, and the more test
cases you run, the more responses you have to review.

[00:34] That makes it hard to keep doing every review by hand.

[00:37] As you saw in module one, you can evaluate results yourself
through human review,

[00:41] but you can also automate those checks using code
evaluators and LLM judges.

[00:46] So in this module, you'll learn about those automated evaluators
so you can check more responses without reviewing each one yourself.

[00:53] You'll also learn how to test whether the evaluators are making the
right judgments. Let's start in this video with code evaluators.

[01:00] Once you run a test case, you have a response to check
against a requirement.

[01:05] A code evaluator makes that check programmatically with ordinary code,
using rules that specify exactly what counts as a pass or a failure.

[01:13] So, when should you use a code evaluator? The key is whether you can
program an explicit rule that determines the answer.

[01:21] For example, if a response must stay under 500 characters,
you can count the characters and compare the total with the limit.

[01:27] There's no judgment call about whether it's short enough.

[01:31] Contrast that with evaluating whether a response from the shelter app
clearly explains why a dog is a bad match for a volunteer.

[01:38] You need to consider what the response says and whether the
explanation is clear.

[01:42] So this kind of evaluation requires interpretation and is better
suited to a human or an LLM judge.

[01:48] So code evaluators fit questions where a specific rule or calculation
is enough to determine whether the requirement was met.

[01:55] So that might include checking whether a required step ran,
whether a claim matches the records,

[02:00] or whether a response includes all the required fields.

[02:03] So how do you turn one of those checks into a code evaluator?

[02:07] You can simply write a Python function that applies deterministic
logic to information from the trace.

[02:13] Every code evaluator follows the same pattern: it takes inputs,
runs your evaluation logic, and returns an output.

[02:20] For a response check, the inputs might be the request and response
from a span passed to the function as text.

[02:27] Other checks may need a database record or details of a tool call.

[02:31] The output is the evaluator's judgment, such as a score of 1 with a
pass label or 0 with a fail label.

[02:38] The particular check you want to make is the logic you
write in the middle.

[02:42] For example, in the shelter app, the agent should reject a volunteer
who is flagged in the do not adopt records.

[02:49] Your function needs the volunteer ID, the corresponding record,
and the agent's decision.

[02:54] If the record flags the volunteer, but the agent approved them,
evaluator returns a fail label and a score of 0.

[03:01] Because the rule determines the result, the evaluator does not need an
LLM to make the judgment.

[03:07] A code evaluator may be a simple Python function,
but that doesn't mean the work inside it has to be simple.

[03:12] You're not limited to string operations,
such as matching words in a response.

[03:17] You can call an API, query a database, or perform any deterministic
check you can write in code.

[03:23] For the shelter's volunteer check, the function first retrieves the
trace through an API call.

[03:28] The trace gives it the volunteer ID and the agent's decision.
The function then uses that ID to query the do not adopt records.

[03:35] Once the function has the record and the agent's decision,
it returns a fail if a flagged volunteer wasn't rejected.

[03:42] So this evaluator involves an API call, a database query,
and several lines of logic.

[03:47] What makes it a code evaluator isn't how simple the check is,
but that the check is deterministic.

[03:53] The logic can be as detailed as the requirement demands, and given the
same trace and the same record, it will return the same judgment.

[04:01] Code evaluators aren't limited to checking decisions.
You can also check whether the agent took the required steps.

[04:07] For example, the shelter agent might correctly approve a volunteer,
but the trace shows it never checked the do-not-adopt records.

[04:14] You can write an evaluator that looks for that required lookup in the
trace, and returns a fail if it's missing,

[04:20] even though the final decision was correct.

[04:22] Let's look at a few more examples from the shelter app.

[04:25] You can use code for format checks, such as whether the shelter agent
returns valid JSON and includes the volunteer ID, dog ID,

[04:33] and approval status.

[04:34] You can check whether the response stays within a length limit
or contains a prohibited phrase, such as "as an AI assistant."

[04:42] And you can check facts against the records and required steps against
the trace. Does the volunteer ID exist in the system?

[04:48] Does the dog's reported eligibility match its record? Did the agent
check the do-not-adopt records before approving the volunteer?

[04:55] These checks don't have to be brittle.

[04:57] When you're comparing text, you can normalize whitespace,
ignore capitalization where it doesn't matter,

[05:03] or write the check to accept valid alternative wording,
so a response doesn't fail just because it uses a different phrase.

[05:10] So when an explicit rule or calculation can determine whether a
requirement was met, you can automate that check with code.

[05:16] That makes code a useful first line of defense. You can catch a clear
violation without making or paying for an LLM call.

[05:23] Even a simple record check can catch a serious mistake,
such as approving a flagged volunteer.

[05:29] Code evaluators and LLM judges also fit into the same
evaluation workflow.

[05:34] You retrieve the recorded runs, pass each evaluator the information it
needs, and save its scores and labels with the run it evaluated.

[05:42] In Phoenix, you can log both kinds of judgment as annotations on the
same trace so you can see the evaluations together.

[05:49] But some requirements call for interpreting what a
response means in context.

[05:53] You might need to judge whether an explanation is clear,
whether a response is empathetic,

[05:58] or whether a recommendation addresses someone's needs.

[06:01] Those judgments depend on how the response fits the situation,

[06:05] so counting characters or checking that a field is
present won't be enough.

[06:09] You've already explored how to make judgments like these
through human review.

[06:12] In the next video, you'll learn how to use an LLM judge to evaluate
responses against requirements that call for interpretation.
