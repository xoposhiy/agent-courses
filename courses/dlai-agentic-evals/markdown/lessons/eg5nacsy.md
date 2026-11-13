# The Evals Process Part 2

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/eg5nacsy/the-evals-process-part-2) · [Raw file](../../raw/lessons/eg5nacsy.html)

Retrieved: 2026-11-13T17:26:05.024734+00:00

[00:00] In the previous video, you explored the first half of the evaluation
process, analyzing the agent's behavior, building test cases,

[00:08] and defining criteria for judging the results.

[00:10] Now in this video, you'll explore the second half of this overview.

[00:14] Here, your goal is to measure how well the agent performs
and use those findings to guide improvements.

[00:20] So, how do you turn those test cases and criteria into
evidence that you can use?

[00:25] You start with evaluators, which check the agent's responses
and actions against your criteria.

[00:30] To do that, you run the agent on your test cases and record its
responses and actions.

[00:35] Some checks also need supporting information, such as the records
that the agent used.

[00:40] You can review the results yourself or work with someone who
understands the task.

[00:44] But reviewing every result takes time, especially when you keep
testing after changes.

[00:49] Code evaluators and LLM judges let you automate some of that work.
Use code when you can write an explicit rule to make the check.

[00:57] For Northwind, a code evaluator could compare the recommended product
and requested size with the stock records, then return a pass or fail.

[01:04] Other checks require interpretation. For example,
do those clothes suit a winter camping trip?

[01:10] You can use an LLM to assess the recommendation using your rubric,
the customer's request, and relevant product information.

[01:17] When an LLM evaluates results this way, it's called an LLM judge.
You can implement both types of evaluator in your own Python code.

[01:25] An evaluation platform can help you run the checks
and organize the results,

[01:29] but you don't need a particular platform to use these methods.

[01:32] In these examples, we'll be using Phoenix,
an open-source solution from Arize.

[01:37] But before you rely on these evaluators, you need to check
that they're making the right judgments.

[01:41] They can miss failures or flag acceptable results,
which could mislead you about what needs improving.

[01:47] So compare their judgments with human judgments of the same results
using the same criteria and investigate disagreements.

[01:53] The reviewer or the criteria may need correcting too.

[01:56] You can then bring those individual judgments together to see how well
the agent performs across your evaluation set.

[02:02] Once you have evaluators that can judge the agent's work,
you need to find out how consistently it meets your requirements.

[02:08] An LLM can handle a request correctly on one run and fail on another,
even with the same input.

[02:14] And it may handle some kinds of requests while struggling with others.

[02:17] So a few successful responses aren't enough to establish
that it does the job reliably.

[02:22] That's why you measure performance across different
cases and repeated runs.

[02:26] Metrics, such as how often a requirement is met, help you understand
how consistently the agent performs in the situations you've tested,

[02:33] and where it needs attention.

[02:35] You can use those measurements to decide where to focus your efforts
and check whether your changes actually help.

[02:40] You'll explore the practical methods in the later modules,
starting with building and testing evaluators in Module 3.

[02:46] That brings you to the fourth and final part of the evaluation
process: using what you've learned to improve the agent.

[02:52] You're going to want to first decide what needs attention.

[02:56] Your results help you identify problems,
but how often something fails isn't the only consideration.

[03:01] A less common mistake might matter more because of the
harm it could cause.

[03:05] Improvement can also mean adding a capability or reducing cost
while keeping the quality you need.

[03:10] Then, investigate the problem before deciding what to change.

[03:14] Different problems call for different fixes,
so you want your changes to address what's actually going wrong.

[03:19] For example, if Northwind gives product advice that isn't
supported by its catalog,

[03:24] you might discover that its instructions never required it to stick
to that information.

[03:28] Adding that requirement would be one change to try.

[03:31] Other problems might call for better information,
changes to the tools or workflow, or a different model.

[03:37] You're using what you found to decide what to change,
rather than trying fixes without understanding the problem.

[03:43] But making that change doesn't establish that it worked.

[03:46] You still need to test whether it improved performance and whether
anything else got worse.

[03:50] To find out, you compare the original agent with the
version you changed.

[03:54] You run both on the same test cases, and judge them using the same
criteria and evaluators.

[04:00] That way, you're comparing their performance without also
changing how you measure it.

[04:05] You want to check whether the problem you targeted has improved, but
also whether the agent still does the work it was already doing well.

[04:12] A change can help in one situation and cause problems in another.
That loss of previously working behavior is called a regression.

[04:20] For Northwind, the new instruction might reduce
unsupported product advice,

[04:25] but also lead to unnecessary tool calls and make responses
slower or more expensive.

[04:30] So you need to look at what got better and what got worse
before deciding whether the change is worth keeping.

[04:35] That comparison helps you decide whether to keep the change,
revise it, or try something else.

[04:40] And you still need to consider whether the results meet your
requirements. Better than before doesn't necessarily mean good enough.

[04:47] If the evidence is unclear, you may need more testing before making
that decision. That concludes this overview of the evaluation process.

[04:54] As you test the agent and see how it handles real requests,

[04:58] you'll discover problems that lead to further improvements
and new things to evaluate.

[05:02] You'll explore the details of this process throughout the course,
starting in Module 2.

[05:07] But before you can put this process into practice,
you need evidence of what the agent actually did.

[05:12] The final output won't necessarily show you which information it used,
which tools it called, or whether it skipped something important.

[05:19] Traces record those steps so you can examine them and check whether
the agent did what it was supposed to do.

[05:25] So you'll wrap up this module with a look at traces and how they give
you the evidence you need for evaluation.
