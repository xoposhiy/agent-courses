# Build the Northwind Benchmark

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/txe2f9/build-the-northwind-benchmark) · [Raw file](../../raw/lessons/txe2f9.html)

Retrieved: 2026-11-13T17:26:05.664358+00:00

[00:00] In this module, you've learned how to build a benchmark.

[00:03] You started by defining requirements: clear statements of what the
application should and should not do.

[00:09] Then you turned those requirements into test cases with the
information you gave the application and the outcome you expected.

[00:15] You ran those cases, reviewed the results,
and labeled the failures you found.

[00:20] And finally, you looked for gaps in coverage, added useful cases,
and curated the set so each case had a reason to stay.

[00:27] Now let's apply that full workflow to Northwind.

[00:30] The goal is to build the benchmark you'll use in the next module
when you start automating those judgments with evaluators.

[00:37] Start with a behavior you already found in a trace.
A customer asks, "How should I care for my merino wool sweater?"

[00:43] The agent looks at product information, which says machine washable on
wool cycle, but the agent answers,

[00:50] "You can machine wash it on wool cycle and then tumble dry."

[00:53] The first part is supported by the data, but the second part is not.

[00:57] The agent had information about washing,
but it didn't have any information about drying.

[01:01] And that unsupported detail matters, because care instructions can
affect what the customer actually does with the product.

[01:07] So, write down what actually went wrong.

[01:10] The agent recommended tumble-drying, even though Northwind didn't
provide drying instructions for this sweater.

[01:15] Next, turn that observation into a requirement. You could write,
"Do not recommend tumble-drying the merino wool sweater."

[01:22] But that's too narrow. It only covers this one product and this
one unsupported claim.

[01:27] The same kind of problem could happen with sizing, color,
availability, materials, or return policies.

[01:34] So make the requirement broader. Only make product claims that are
supported by Northwind data. Now you have a standard you can test.

[01:41] When the agent answers a product question, you can ask:
Does Northwind data support the claims in this response?

[01:47] Next, turn that requirement into test cases.
Just the sweater case is not enough.

[01:53] You want a small set of cases that checks the requirement under
different conditions. One case should have complete information.

[02:00] For example, a customer asks, "What colors does the
Classic Tee come in?"

[02:04] And the catalog data lists the available colors: white, black, navy,
and heather gray. Here, the expected outcome is straightforward.

[02:12] The agent should answer with the listed colors,
and avoid adding colors that are not in the catalog.

[02:17] But what if the agent only has partial information? A merino sweater
case fits here. The customer asks how to care for the sweater.

[02:24] Northwind data says it's machine washable on a wool cycle,
but gives no drying instructions.

[02:29] So the expected outcome is: use the supported washing instruction
and do not add drying advice.

[02:35] The agent can say the drying instructions are not available.

[02:38] A third case should have no relevant information Suppose a customer
asks, "What's your return policy?"

[02:44] but Northwind does not provide any return policy
information to this agent.

[02:48] The agent is expected to say that the information is not available or
that it cannot help with that request.

[02:54] Now you have three cases that test the same requirement from different
angles: complete information, partial information,

[03:00] and missing information.

[03:02] You can also vary the customer side. For example,
"What colors does the Classic Tee come in?"

[03:08] and "Do you have the Classic Tee in size medium and what colors are
available?" are two distinct requests.

[03:14] The second one asks about size and color, so it may require the agent
to handle multiple product details at once.

[03:20] But if two cases only change the wording without changing what the
agent needs to decide, you may not need both.

[03:26] The point is not to collect as many phrasings as possible,
but to keep cases that test meaningful differences.

[03:32] Once you have the cases, run the agent on them and review the results.
For each run, compare the actual versus the expected outcome.

[03:40] If the customer asked about colors, and the agent listed only colors
from the catalog, that run passes.

[03:46] If the agent adds forest green when the catalog only lists white,
black, navy, and heather gray, that run fails.

[03:52] Don't forget to write down why.

[03:55] In this case, the agent mentioned a product color that was not
supported by Northwind data, then label the failure.

[04:01] That could be a groundedness failure,
and more specifically, hallucination,

[04:05] because the agent made a claim with no supporting evidence.

[04:09] Now look at the return-policy case, where the customer asks,
"What's your return policy?"

[04:14] Northwind has no return-policy information, so if the agent says,
"I do not have return Policy information available",

[04:20] that meets the expected outcome.

[04:22] But if it says, "You can return items within 30 days," that fails.

[04:26] Here, the main problem is that the agent answered a question outside
the information Northwind can provide.

[04:32] So you might label that as a scope violation.

[04:35] The expected outcome tells you what should happen, while the failure
label tells you what went wrong when the agent did something else.

[04:42] Keep both with the case, As you review more cases, start looking
across the set. Do you have several unsupported product claims?

[04:50] Does the agent ever invent policies outside Northwind's scope?
Do you see cases where the agent should say information is missing?

[04:57] Are there cases where the agent should answer directly because the
data fully supports the answer?

[05:01] These questions help you find coverage gaps.
Suppose your first cases mostly test care instructions.

[05:08] That's useful, but the requirement is broader than care instructions.

[05:11] You may want cases about colors, materials, sizing, availability,
or product compatibility.

[05:17] Suppose you have several cases where the information is missing,

[05:20] but very few where the information is present and the agent
should answer directly.

[05:24] Then your benchmark may overrepresent refusals and underrepresent
ordinary successful answers. You need both.

[05:31] A useful benchmark should catch failures, but it should also confirm
that the agent still handles normal cases correctly.

[05:38] Next, add cases to fill the gaps.

[05:40] Start with real examples when you can, which you can find in traces,
reviewed runs, user questions, bug reports, or support examples.

[05:48] If you find a real customer question that tests an
important gap, use it.

[05:52] Real examples help the benchmark reflect situations the application
actually encounters.

[05:57] Just bear in mind that real examples may not cover
every case you need.

[06:01] If you need a specific kind of case and cannot find one,
you can create it yourself, or use an LLM to generate a candidate.

[06:09] For example, you might ask for a customer question where the catalog
contains some product information,

[06:14] but not enough to answer every part of the request.

[06:16] Then review the generated case carefully. Does it test the situation
you meant to test? Is the product data realistic?

[06:23] Is the expected outcome clear? Did the generated case quietly change
the requirement? only keep the case if it adds useful coverage.

[06:32] As the set grows, you should curate it. Some cases will be redundant.
For instance, "Is the Classic Tee available in medium?"

[06:40] and "Do you have the Classic Tee in size M?"
may test nearly the same thing.

[06:45] you probably don't need both unless the wording difference matters.

[06:48] But a case that asks, "Is the Classic Tee available in medium,
and what is your return policy?"

[06:53] does add a different challenge because the agent needs to answer the
product question using catalog data,

[06:58] while also avoiding an unsupported return policy answer.

[07:01] So that case may be worth keeping. A useful case should do at least
one of three things.

[07:06] It should either cover a meaningful situation, protect against an
important regression, or clarify a boundary in the requirement.

[07:13] If a case does none of those, remove it or revise it.

[07:17] Also pay attention to difficult cases If your benchmark has 98
straightforward product questions

[07:22] and only two difficult missing information cases, the overall score
can look strong even if the agent fails both difficult cases.

[07:30] That doesn't mean the benchmark is wrong.
It means you need to read the score in context.

[07:34] The overall score describes performance on the benchmark you built,
not the true frequency of success or failure in production.

[07:41] During development, it's often useful to include more difficult cases
than you expect to see in everyday use.

[07:46] That gives you enough examples to measure whether the agent improves
on the behaviors you care about.

[07:51] At the end of this process, each Northwind benchmark case should keep
together the pieces you need later: the customer query,

[07:58] the relevant product data, the expected outcome,
the source of the case, and when you've reviewed a failed run,

[08:04] the failure label that describes what went wrong.

[08:07] This is what a complete case might look like. customer query,
"What is your return policy?"

[08:13] Northwind data has no return policy information available. The
expected outcome would be, say that the information is not available.

[08:21] If the agent invents a return policy, label the failure
as a Scope violation.

[08:25] Another case might be: Customer query, "How should I care for the
Merino Wool Sweater?"

[08:30] Northwind data says, "Machine washable on wool cycle."

[08:34] The expected outcome is: Use only the supported machine washing
instruction, and do not add drying advice.

[08:40] If the agent adds unsupported drying instructions,
label the failure as Faithfulness drift.

[08:45] And the third case might be customer query,
"What colors does the Classic Tee come in?"

[08:51] Catalog data indicates "White, black, navy, and heather gray."
The expected outcome is "Answer with the listed colors."

[08:58] If the agent mentions another color,
label the failure as a Hallucination.

[09:03] Once the cases are reviewed and curated,
save them as a Northwind benchmark.

[09:07] That benchmark now contains requirements, test cases,
expected outcomes, reviewed judgments, and failure labels.

[09:14] You can run it again as the application changes, and because the cases
stay the same, you can compare versions against a stable standard.

[09:22] Keep that in mind for the next module, where you'll go into the
evaluate stage of the evals process.

[09:27] You'll build evaluators that check whether Northwind responses
meet these requirements,

[09:32] and you'll test whether those evaluators agree with the reviewed
labels you created here.

[09:36] See you in module three.
