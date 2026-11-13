# Using an LLM Judge

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/hl9qj2/using-an-llm-judge) · [Raw file](../../raw/lessons/hl9qj2.html)

Retrieved: 2026-11-13T17:26:05.867032+00:00

[00:00] In the last video, you explored how code evaluators check requirements
using explicit rules,

[00:06] but some requirements call for interpreting what a
response means in context.

[00:10] Was the response helpful? Did it answer the user's actual question?
Was the tone appropriate for somebody who was already frustrated?

[00:17] You need to read the response and consider the situation to
make those judgments.

[00:22] You can make those judgments yourself through a human review,
or use an LLM judge to automate them.

[00:27] An LLM judge uses a model to evaluate the agent's response against
written criteria, In this video,

[00:34] you'll look at how to put that evaluator together and use its
judgments to find responses that need a closer look.

[00:40] Let's start with the shelter's safe matching requirement.

[00:43] Suppose the agent recommends a dog that lunges at children for a
volunteer described as an experienced handler.

[00:49] The record can tell you about the dog's behavior,
and the profile can tell you about the volunteer's experience,

[00:54] but you still need to consider whether that experience prepares the
volunteer to manage this dog's particular behavior.

[01:00] Simply confirming that the volunteer is experienced doesn't settle
whether the match is safe.

[01:05] So, how would an LLM judge evaluate that recommendation? It needs
three things: a judge model, a rubric, and data from the agent's run.

[01:14] The judge model is the LLM that makes the evaluation. The rubric gives
the model the criteria and instructions for evaluating the response.

[01:22] For safe matching, those criteria might tell the judge to identify the
dog's behavior risks,

[01:27] compare them with the volunteer's relevant experience, and return SAFE
only when the volunteer appears to be able to manage those risks.

[01:35] The data gives the judge the evidence for that particular
recommendation, the volunteer's profile, the dog's record,

[01:41] and the agent's decision.

[01:43] The model applies the rubric to that evidence
and returns its judgment,

[01:47] So the rubric matters because it tells the model what to consider
when deciding whether the recommendation meets the requirement.

[01:54] Phoenix keeps the model, rubric, and data separate,
so you can change one without changing the others.

[01:59] You might try another model with the same rubric and examples,
or revise the rubric while keeping the model and examples the same.

[02:06] That lets you compare the evaluations and see how the judgments
differ. Let's look first at choosing the judge model.

[02:13] You don't have to use the same model for the judge that you
use in the application.

[02:17] For the application, you might choose a faster,
less expensive model to keep the response times and costs down.

[02:23] But the judge can often evaluate completed runs afterwards,

[02:27] so you may be able to use a more capable model even if it's
slower or more expensive.

[02:31] Mistakes by the judge affect your evaluation results,
so how reliably it applies the rubric matters.

[02:38] The judge's model can also come from a different provider than the
application's model.

[02:42] from the same provider may share biases in how they generate
and evaluate responses, so they may overlook similar problems.

[02:50] Choosing a different provider for the judge can help reduce that risk.

[02:54] Now, whichever model or provider you choose, what you really need to
know is whether the judge is applying your criteria correctly.

[03:01] You can check that by comparing its judgments with human judgments of
the same responses using the same criteria.

[03:07] In this course, we call the person making those judgments a Reviewer,
and the automated system an Evaluator.

[03:13] Later in the module, you'll look at how well the Evaluator agrees with
those Reviewers. Next, consider where the rubric will come from.

[03:21] Before writing one from scratch, check whether Phoenix already has an
evaluator for the requirement you want to measure.

[03:27] Built-in templates cover questions such as correctness,
tool selection and tool invocation, document relevance, and refusal.

[03:34] They give you prewritten criteria and an expected output,
and you provide the judge model and evidence to evaluate.

[03:41] A built-in evaluator is useful when those criteria
match your requirements,

[03:45] but a general Correctness evaluator doesn't know how the
shelter judges a match,

[03:49] including whether the volunteer's experience prepares them to manage
the dog's particular behavior.

[03:54] So you're going to need a custom rubric to tell the judge
which details matter

[03:57] and what makes a recommendation acceptable for the shelter.

[04:01] Once you've selected the model and rubric,
you can run the judge across a set of recorded runs.

[04:06] The workflow is to retrieve the data from Phoenix,
evaluate the responses, and save the judgments back to Phoenix.

[04:13] You'll work through the code for this workflow in the lab.
For now, let's look at what each part does.

[04:19] Start by retrieving the relevant spans from Phoenix as a dataframe,
and prepare the information the judge needs for each example.

[04:25] For a response check, that includes the input and output from the run,
along with any context needed to apply the rubric.

[04:32] For safe matching, you need the volunteer profile, the dog's record,
and the agent's recommendation.

[04:38] Then, set up the evaluator with your judge model and the rubric
that it will apply to that evidence.

[04:44] Before running the evaluator, remember that the judge also makes calls
to an LLM, and those calls can produce traces of their own.

[04:51] Use suppress_tracing around the evaluation code to pause
that recording while the judge runs.

[04:56] You'll still save the judge's scores and labels,

[04:59] but you won't add traces of the grading process alongside the
application runs you're evaluating.

[05:04] You can then run the judge across the recorded runs.

[05:07] For each safe matching example, the judge receives the volunteer's
profile, the dog's record, and the agent's recommendation.

[05:14] It applies the rubric and returns a structured result,
such as a safe or unsafe label, a score, and an explanation.

[05:22] Save those results back to Phoenix as annotations linked to the
runs they evaluated,

[05:26] so you can find the responses the judge flagged
and inspect what happened.

[05:30] Now you can sort by score or filter by label to find the responses
you want to inspect.

[05:35] For safe matching, you might start with
recommendations labeled UNSAFE.

[05:39] Those labels give you an explanation of what failed, so open one of
those traces and compare the volunteer's profile, the dog's record,

[05:46] and the agent's recommendation to see which risk the agent
may have overlooked.

[05:51] The automated evaluations help you choose where to focus your review,

[05:55] instead of having to read every response just to
find possible problems.

[05:58] The judge can help you find possible failures,
and the rubric tells it what to look for.

[06:04] In the next video, you'll look at how to turn the shelter's safe
matching requirement into a custom rubric the judge can apply.
