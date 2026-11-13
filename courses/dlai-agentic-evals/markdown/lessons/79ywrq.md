#  Validating LLM Judges

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/79ywrq/-validating-llm-judges) · [Raw file](../../raw/lessons/79ywrq.html)

Retrieved: 2026-11-13T17:26:06.076301+00:00

[00:00] You just saw how you can turn a requirement into a rubric.

[00:04] You gave the judge a role, criteria, inputs, examples,
and output instructions,

[00:09] but a clear-looking rubric does not guarantee that a judge
will apply it correctly.

[00:14] Before you use its labels to decide what needs improving,
you need to test whether those labels can be trusted.

[00:20] Let's go back to the shelter's safe matching evaluator.

[00:23] The judge reads a volunteer profile, a dog record, and the agent's
recommendation, and it returns a label like SAFE or UNSAFE.

[00:31] That label may look definitive, but it is still the judge's
interpretation of the rubric.

[00:36] So you should treat the judge like a classifier.

[00:39] It's assigning labels to cases, and you can test those labels by
comparing them with the reviewed labels from your benchmark.

[00:46] When you do that, start with cases that weren't used to
write or tune the rubric.

[00:51] If you test only on the examples you used while building the rubric,
the results can look better than they really are.

[00:57] Those examples already shaped the evaluator.
So instead, keep a separate held-out set.

[01:03] These are reviewed cases that the judge has not seen as prompt
examples, and that haven't been used to refine the rubric.

[01:10] Run the judge on those held-out cases, and, for each case,
compare the judge's label with the reviewed label.

[01:16] Suppose the shelter agent recommends a dog that requires an
experienced handler to a first-time volunteer.

[01:22] A human reviewer labels that recommendation UNSAFE,
but the judge labels it SAFE. Now you have a disagreement.

[01:29] the judge missed a failure that the reviewer caught.

[01:32] Across the validation set, these matches and disagreements tell you
how reliably the judge is applying the rubric.

[01:38] There are two useful metrics when measuring a judge's reliability:
precision and recall.

[01:44] For this evaluator, focus on the UNSAFE label because unsafe
recommendations are the failures you most need the judge to catch.

[01:52] Precision tells you of the recommendations that the
judge labeled UNSAFE,

[01:56] how many were actually UNSAFE according to the reviewed labels?

[02:00] If the judge labels a SAFE match as UNSAFE, that's a false alarm
that will cause precision to go down.

[02:06] So precision tells you how often the judge's warnings are right.

[02:10] Recall measures: of all the recommendations reviewers labeled unsafe,
how many did the judge catch?

[02:16] If the judge labels an unsafe match as safe, that's a missed failure,
and it will bring recall down.

[02:22] So recall tells you whether unsafe recommendations are slipping
through. Which mistake matters more depends on the requirement.

[02:30] At the shelter, a false alarm means someone may review a safe
recommendation unnecessarily. That costs time.

[02:37] But a missed failure means an unsafe match may move forward,
which could put a volunteer or a dog at risk.

[02:44] So for the safe matching evaluator, recall matters a lot.

[02:47] You may be willing to accept some extra false alarms if that helps
catch more unsafe matches.

[02:53] One thing to note, recall and precision metrics are at
odds with each other.

[02:57] If one goes up, the other goes down, so you can't prioritize both at
the same time. Another evaluator might need a different balance.

[03:04] For example, if a judge flags too many acceptable responses for manual
review, it may become too noisy to use.

[03:11] So don't treat precision and recall as abstract scores.
Read them in terms of what errors would actually cost.

[03:17] You can also measure agreement across all labels with Cohen's kappa.

[03:21] Imagine you've just reviewed 10 shelter cases,
nine of which you manually labeled as SAFE and one as UNSAFE.

[03:28] Let's say the judge labels every case safe.
It agrees with the reviewer 9 out of 10 times.

[03:34] That sounds like 90% agreement, but the judge missed the only unsafe
case. It didn't show that it can distinguish safe from unsafe matches.

[03:42] It basically just benefited from choosing the most common label.

[03:46] Cohen's kappa adjusts for the agreement you would expect by chance,
given how often the labels appear.

[03:52] A kappa of 1 means the judge and reviewers matched on every label.

[03:56] A kappa of 0 means their agreement was no better than chance, and a
negative kappa means they disagreed more than chance would predict.

[04:04] Kappa is useful because it gives you a broader view of agreement,
but it's not enough by itself.

[04:10] On a small validation set, one disagreement can move the score a lot.
And kappa only compares two sets of labels.

[04:18] It doesn't prove that either label is correct.
The judge and reviewer can agree and still both be wrong.

[04:24] Perhaps the reviewer missed an important detail,
or the rubric itself is unclear,

[04:29] or maybe everyone is applying the wrong standard consistently.

[04:32] So use the metrics as signals, not as the final answer.
When the labels disagree, inspect the case.

[04:39] Read the volunteer profile, the dog record, and the agent's
recommendation, and go through the judge's explanation.

[04:45] Then apply the safe matching requirement yourself.

[04:48] If the judge's decision follows the requirement,
the reviewed label may need to be corrected.

[04:53] If the reviewed label is right, the judge may have
misapplied the rubric.

[04:58] And if the case could reasonably go either way,
the rubric might not be making the boundary clear enough.

[05:03] A disagreement does not automatically mean fix the judge.
It tells you where the evaluation needs investigation.

[05:09] As you inspect disagreements, look for patterns because some judge
errors are not random.

[05:16] For example, suppose the agent recommends a calm senior dog to an
experienced volunteer. The response sounds careful.

[05:23] It says the dog is gentle and explains that the volunteer has
handled many dogs before.

[05:28] At first glance, the recommendation may seem safe, but the volunteer's
profile says they can safely handle dogs up to 50 lb.

[05:35] This dog weighs 80 lb. So the problem is that the recommendation
ignores a physical handling limit.

[05:41] An LLM judge might miss that if it focuses on the positive language
in the recommendation,

[05:45] instead of comparing the dog's weight with the
volunteer's stated limit.

[05:49] To see whether that mistake is part of a pattern,
compare similar cases.

[05:54] Does the judge catch unsafe matches when the behavior risk is obvious,
but miss cases where the risk is a numeric constraint?

[06:00] Or maybe recall drops when the recommendation sounds thoughtful
and the dog seems calm.

[06:06] If so, the judge may be giving too much weight to the agent's
explanation and not enough weight to the underlying evidence.

[06:12] One thing you can do is to try a targeted rubric change.

[06:16] For example, before assigning a label, require the judge to identify
the volunteer's handling limit and the dog's weight,

[06:22] then compare them directly.

[06:24] That pushes the judge towards the evidence that should determine
the safety decision.

[06:29] But don't assume the change helps just because it fixes one case.

[06:32] Change one thing at a time, then test the revised rubric on
fresh reviewed cases.

[06:38] If you use a disagreement to revise the rubric,
that case has now influenced the evaluator,

[06:43] It's no longer a clean validation case for the revised version.

[06:46] So when possible, test the revision on other reviewed cases that were
not used to make the change. Compare the old and new versions.

[06:54] Did recall improve on unsafe matches?
Did precision fall too far? Did kappa improve?

[07:00] Do the explanations show that the judge is using the relevant
volunteer and dog information?

[07:05] Keep the change only if the evaluator improved overall.

[07:09] If the change fixes one case but creates new errors elsewhere,
revise again or return to the previous version.

[07:15] This is the same discipline you'd use when changing application code.
A local fix is not enough.

[07:21] You need to know whether the change improves behavior across
the cases that matter.

[07:26] So before you trust an LLM judge, bring several checks together.
Use recall to see whether it catches the failures you care about.

[07:33] Check precision to see whether its warnings are usually right, and get
Cohen's kappa to measure agreement with reviewed labels beyond chance.

[07:41] Inspect any disagreements to understand what actually went wrong.

[07:45] and read explanations to confirm that the judge is applying the
requirement using the right evidence.

[07:51] Only then should you rely on the judge's labels to guide
improvement or block a change.

[07:56] So far in this module, you've gone through the evaluation process
using the dog shelter agent as an example.

[08:01] You built a code evaluator when the requirement could
be checked strictly.

[08:05] You chose an LLM judge when the requirement needed interpretation, and
you built a rubric to tell the judge how to apply that requirement.

[08:12] And now you've seen how to test whether the judge's
labels are reliable.

[08:17] Next, you'll bring those pieces together with the Northwind agent.

[08:20] You'll choose different evaluators for different requirements,
keep their results separate,

[08:25] and validate the custom judge before relying on its labels.
