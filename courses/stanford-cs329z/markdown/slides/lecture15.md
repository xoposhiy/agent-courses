# Lecture 15: LLM-as-Judge & Evaluation Infrastructure

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture15.pdf) · [Raw file](../../raw/slides/lecture15.pdf)

Retrieved: 2026-11-13T16:31:57.427223+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

CS329Z: Engineering AI Agents

CS 329Z:Engineering AI Agents

LLM-as-Judge &
Evaluation Infrastructure

Diyi Yang, Michael Ryan, John Yang

## Page 2

CS329Z: Engineering AI Agents

Roadmap

LLM-as-Judge & Evaluation Infrastructure

tl;dr: Last lecture we discussed the high level concepts and best practices around 
agent benchmarks. This lecture we’ll zoom in on the nitty gritty of veriﬁcation: 
general approaches, their mechanics, and how to ensure reliability + objectivity.

●
Biases + Validate Judgment \[20 min\]
●
Handle Nondeterminism \[5 min\]
●
Motivation \[7 min\]
●
Grader Types \[13 min\]
●
LM-as-a-Judge \[35 min\]

## Page 3

CS329Z: Engineering AI Agents

Motivation

## Page 4

CS329Z: Engineering AI Agents

Motivation

Recall from last lecture, the 3 components of a benchmark’s task formulation

## Page 5

CS329Z: Engineering AI Agents

Motivation

Recall from last lecture, the 3 components of a benchmark’s task formulation

## Page 6

CS329Z: Engineering AI Agents

Motivation

What diﬀerent kinds of veriﬁcation techniques are there? One popular technique is 
to encode expected behavior as deterministic checks in the form of unit tests.

Find a Fact
BrowseComp

Fix a Bug
SWE-bench

Place an Order
Tau-bench

answer == gold
pytest all pass
order in orders.db?

Check w/ code
Check w/ code
Check w/ code

But is checking with code all we need?

## Page 7

CS329Z: Engineering AI Agents

Motivation

But many agent tasks don’t have deterministic, singular solutions.

Deterministic, Code
Abstract, Judgment

Find a Fact
BrowseComp

Fix a Bug
SWE-bench
Write a Paper
Better Code

Readability

Make a great

TV Show

Unit tests might not cover…

●
2+ valid answers, beyond reference
●
Process, beyond the outcome

●
Quality, beyond correctness
●
Partial credit, beyond pass/fail

## Page 8

CS329Z: Engineering AI Agents

Motivation

A miscalibrated grader may also artiﬁcially deﬂate or inﬂate benchmark scores.

True Positive

False Negative: On τ²-bench, 
Claude Opus 4.5 found a 
better solution that grader did 
not account for. \[A\ Blog\]

False Positive: In SWE-bench, 
some patches pass F2P tests, 
but fail unregistered P2P tests 
\[Wang 2025\]

True Negative

Correct

Incorrect

In reality, 
solution is

According to grader
Correct
Incorrect

### Page links

- [Link 1](https://arxiv.org/abs/2503.15223)
- [Link 2](../readings/grace-et-al-demystifying-evals-for-ai-agents-anthropic-2026.md)

## Page 9

CS329Z: Engineering AI Agents

Motivation

Agents are non-deterministic. Across multiple attempts on the same task, some 
attempts may fail while others will succeed, how do we account for this variance?

Let’s say you run 5 rollouts / trials of an agent on a task, and get: ❌ ✅ ❌ ❌ ✅

How do you report this outcome?

●
Average (40%): Communicates expected success rate per try.
●
At least once (Yes): Says whether agent is capable of solving task at all.
●
Solved every time (No): Says whether you can count on agent

## Page 10

CS329Z: Engineering AI Agents

Motivation

Let’s say you run a task 5 times, and get: ❌ ✅ ❌ ❌ ✅

How do you report this outcome?

●
Average (40%): Communicates expected success rate per try.
⇒ Hides: So is each attempt a coin ﬂip? Or tasks are always all pass/fail?

●
At least once (Yes): Says whether agent is capable of solving task at all.
⇒ Hides: Luck + cost of retrying. What if you scale arbitrarily to k retries?

●
Solved every time (No): Says whether you can count on agent
⇒ Hides: Near-misses and potential infra failings. Goes towards 0% w/ more k.

## Page 11

CS329Z: Engineering AI Agents

Motivation

Each section of today’s lecture addresses several key questions centered around 
how to set up reliable, fair veriﬁers for a benchmark / task:

●
Grader Types: What kinds of graders exist? When do I use each?

●
LM-as-a-Judge: When would I need LM-as-a-judge? How do I set it up?

●
Biases + Validating Judgment: How can I make sure the verdict is trustworthy?

●
Handling Non-determinism: There’s variance across multiple runs. How do we 
account for it?

## Page 12

CS329Z: Engineering AI Agents

Grader Types

## Page 13

CS329Z: Engineering AI Agents

Grader Types

Depending on the task, diﬀerent graders are more or less eﬀective at analyzing 
task artifacts meaningfully across a range of cost considerations.

Cost
Speed
Reliable
Flexibility
Scale
Nuance

Code
Cheap
Fast
Yes
Low
High
Low

Human
Expensive
Slow
Partly
High
Low
High

LM Judge
Moderate
Fast
Partly
High
High
High

Each of these graders can look at two things:

Final Environment State
Trajectory

## Page 14

CS329Z: Engineering AI Agents

Code Based Graders

Deterministic checks encoded as runnable scripts that operate on env. or transcript.

Common Checks

●
String / regex match
●
Unit tests (F2P, P2P)
●
Environment state checks
●
Static analysis
●
Tool-call checks (was X called?)

## Page 15

CS329Z: Engineering AI Agents

Code Based Graders

Diﬀerent tasks’ unit tests check diﬀerent components of a rollout on a task.

Checks Codebase
Checks Environment

SWE-bench
Checks repo’s 
own F2P + P2P 
tests

Terminal-Bench
Checks 
task-speciﬁc tests 
run in the 
container

OSWorld
Checks per-task 
scripts inspecting 
ﬁles, conﬁgs, app 
state

τ-bench
Checks ﬁnal 
database state vs. 
the expected 
state

## Page 16

CS329Z: Engineering AI Agents

Code Based Graders

But code-oriented grading is not perfect! They capture exactly what they capture, 
and nothing more.

Prescriptive
If a function or class is 
checked, the solution 
must have that function 
or class.

Static
Tests don’t evolve over 
time. Once they’re 
written, they are “set in 
stone”.

Reductive
Anything that the tests 
don’t cover will implicitly 
get registered as a 
“pass”.

## Page 17

CS329Z: Engineering AI Agents

Human Graders

People judge the work directly, can be eﬀective for more open-ended work.

Common Setups

●
Expert review (domain 
specialists)
●
Crowd votes (many 
non-experts)
●
Pairwise preference: A vs. B 
●
Live use: real users work with 
the agent, then rate it

## Page 18

CS329Z: Engineering AI Agents

Human Graders

Diﬀerent evaluations, depending on their topic, will consult diﬀerent demographics.

Chatbot Arena

Who: anonymous crowd

How: vote between two 
anonymous models’ replies

Score: votes aggregated 
into Elo ratings

GDPval

Who: occupational experts 
across 44 occupations

How: blind comparison of 
model vs. human-expert 
deliverables

Score: win rate vs. experts

Co-Gym (Real)

Who: real users with their 
own tasks

How: collaborate with the 
agent in a shared 
workspace, then rate it

Score: outcome + 
collaboration process

## Page 19

CS329Z: Engineering AI Agents

Human Graders

Human voting is a gold standard (high ﬁdelity to reality), but collection takes time.

Expensive

Every new model needs 
a new round of raters.

Days or weeks per 
evaluation

Disagreement

Two raters can reach 
diﬀerent verdicts.

Report inter-annotator 
agreement

Hard to Rerun

Rater pools and contexts 
change; results don’t 
reproduce exactly.

Sessions can’t replay

## Page 20

CS329Z: Engineering AI Agents

LM-as-a-Judge Graders

Use an LM as a stand in for a human grader! Prompt the LM with a rubric.

Common Checks

●
Reference-based: Does it 
match the gold answer?
●
Rubric scoring: Rate 1-10
●
Pairwise: Which is better? 
●
Assertions: is this statement 
about the output true?

## Page 21

CS329Z: Engineering AI Agents

LM-as-a-Judge Graders

Benchmarks diﬀer in how much judgment they ask of the model.

Speciﬁc: Does it match?
Open-ended Preferences

BrowseComp / HLE

Judge sees
Response + gold answer

Decides
Is the ﬁnal answer 
equivalent?

MT-bench

Judge sees
Multi-turn conversation

Decides
score 1-10, or pick the better 
of two

AlpacaEval

Judge sees
Model’s vs. reference’s reply

Decides
which is better 
(length-controlled win rate)

## Page 22

CS329Z: Engineering AI Agents

LM-as-a-Judge Graders

Scales like code, judges like human, but inherits problems of both.

Non-deterministic

The same input can get 
diﬀerent verdicts.

Run multiple judges or 
samples

Biased

Favors certain positions, 
longer answers, its own 
style.

How to deal with bias?

Needs Calibration

Only as good as its 
agreement with humans.

We’ll explore how to 
align judgment.

## Page 23

CS329Z: Engineering AI Agents

Summary

Evals sometimes use combinations of graders: deterministic, code-based unit tests 
where possible; LM where necessary; humans judiciously.

Multiple ways you can aggregate eval results 
together:

●
All must pass: tests pass and the LM 
rubric says the code is clean 
●
Weighted: scores add up to a threshold
●
Calibrate: humans spot-check LM 
judgment to maintain agreement

## Page 24

CS329Z: Engineering AI Agents

LM-as-a-Judge

## Page 25

CS329Z: Engineering AI Agents

LM-as-a-Judge

Let’s review the emergence and development of LM-as-a-judge grading.

●
\[Phase 1\] NLP Metrics: Can LMs supplant metrics for traditional NLP tasks (e.g., 
dialogue generation, text summarization)

●
\[Phase 2\] Human Preferences: Can LMs decide which completion is better in 
a manner that’s faithful to human inclinations?

●
\[Phase 3\] Human Actions: Can LMs interact with digital or real worlds the way 
we humans can, and make meaningful judgments based on such interactions?

## Page 26

CS329Z: Engineering AI Agents

\[Phase 1\] NLP Metrics

## Page 27

CS329Z: Engineering AI Agents

G-Eval

Motivation: Can an LLM evaluate open-ended text better than n-gram overlap?

Text Summarization

Dialogue Generation

Liu et al., “G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment,” EMNLP 2023

## Page 28

CS329Z: Engineering AI Agents

G-Eval

Method: Give GPT-4 the criteria (e.g., “coherence”), have it ﬁrst write out how it will 
judge, then ask for a 1–5 score. Score = average over likelihood of 1, 2, 3, 4, 5.

Given news article + AI 
summary, GPT-4 assigns 1 - 5 
score for factual consistency.

## Page 29

CS329Z: Engineering AI Agents

G-Eval

Findings: 0.514 Spearman with humans on summarization, beating prior metrics by 
a large margin. Early warning: it may favor LLM-written text.

## Page 30

CS329Z: Engineering AI Agents

GPTScore

Motivation: Can a generative LM score any aspect of text, given only an NL 
description of that aspect?

Fu et al., “GPTScore: Evaluate as You Desire,” NAACL 2024 (arXiv Feb 2023)

## Page 31

CS329Z: Engineering AI Agents

GPTScore

Method: Prompt LM with instruction describing the aspect (e.g., “write a summary 
of…”), then score candidate text by how probable the LM ﬁnds it as a continuation.

## Page 32

CS329Z: Engineering AI Agents

GPTScore

Findings: Tested 19 LMs (80M–175B) on 4 tasks, 22 aspects, 37 datasets: describing 
the task + aspect in the instruction makes scores more reliable.

## Page 33

CS329Z: Engineering AI Agents

Can LLMs Replace Human Evaluation?

Motivation: Human evaluation is hard to reproduce and unstable. Can an LLM ﬁll 
out the exact questionnaire human raters get?

Chiang & Lee, “Can Large Language Models Be an Alternative to Human Evaluations?” ACL 2023

## Page 34

CS329Z: Engineering AI Agents

Can LLMs Replace Human Evaluation?

Method: Give LLMs the identical instructions, samples, and questions used with 
expert raters (English teachers), on story generation and adversarial attacks.

## Page 35

CS329Z: Engineering AI Agents

Can LLMs Replace Human Evaluation?

Findings: LLMs rank texts the way experts do, and are stable across instruction 
wording and sampling. But they are more lenient than experts on unnatural text.

## Page 36

CS329Z: Engineering AI Agents

\[Phase 2\] Human Preferences

## Page 37

CS329Z: Engineering AI Agents

\[Phase 2\] Human Preferences

Phase 1 asked whether LMs can replace text metrics. Phase 2 asks: can an LM 
judge which output people would prefer?

1.
Can we learn a judge from human preferences?
2.
Can a prompted LM stand in for human raters?
3.
How do we make these judges better and trustworthy?

Tl;dr: the same preference judge can score a model (eval) or reward it (training). 
We’ll cover both in the upcoming papers!

## Page 38

CS329Z: Engineering AI Agents

A Brief Primer

There has been a long history of developing neural methods that mimic humans.

Christiano, Paul F., et al. "Deep reinforcement learning from human preferences." NeurIPS 2017.

## Page 39

CS329Z: Engineering AI Agents

Learning to summarize from human feedback

Motivation: ROUGE and reference summaries are rough proxies for quality. Can we 
train a model to predict what humans prefer, and optimize for that instead?

Stiennon et al., “Learning to summarize from human feedback,” NeurIPS 2020

## Page 40

CS329Z: Engineering AI Agents

Learning to summarize from human feedback

Method: Collect 
human comparisons 
between summaries, 
train a reward model 
to predict the 
preferred one, then 
use it as the reward 
to ﬁne-tune a 
summarizer with RL.

## Page 41

CS329Z: Engineering AI Agents

Learning to summarize from human feedback

Findings: Summaries beat human references + larger supervised models; reward 
model predicts human preferences better than ROUGE and transfers to news.

## Page 42

CS329Z: Engineering AI Agents

InstructGPT

Motivation: Generalizes the “Learning to Summarize…” strategy to beyond 
summarization.

Ouyang, Long, et al. "Training language models to follow instructions with human feedback." NeurIPS 2022

## Page 43

CS329Z: Engineering AI Agents

InstructGPT

Method: The 3 steps 
introduced in “Learning 
to Summarize” works in 
general!

## Page 44

CS329Z: Engineering AI Agents

InstructGPT

Findings: Labelers preferred outputs from the 1.3B InstructGPT over the 175B 
GPT-3, a model 100× larger. Also more truthful, less toxic, with minimal regressions.

## Page 45

CS329Z: Engineering AI Agents

MT-Bench + Chatbot Arena

Motivation: Can an LM stand in for human preference when grading chatbots?

Zheng et al., “Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena,” NeurIPS 2023

## Page 46

CS329Z: Engineering AI Agents

MT-Bench + Chatbot Arena

Method:

●
Collect human preferences (80 
multi-turn MT-Bench questions + 
Chatbot Arena votes)

●
Then test 3 judge formats:

## Page 47

CS329Z: Engineering AI Agents

MT-Bench + Chatbot Arena

Findings: GPT-4 agrees with humans over 80% of the time, the same rate humans 
agree with each other. But it shows position, verbosity, self-enhancement biases.

## Page 48

CS329Z: Engineering AI Agents

MT-Bench + Chatbot Arena

Findings: GPT-4 agrees with humans over 80% of the time, the same rate humans 
agree with each other. But it shows position, verbosity, self-enhancement biases.

## Page 49

CS329Z: Engineering AI Agents

Prometheus

Motivation: Can you train an OSS model to judge with rubrics? (instead of GPT-4)

Kim et al., “Prometheus: Inducing Fine-grained Evaluation Capability in Language Models,” ICLR 2024

## Page 50

CS329Z: Engineering AI Agents

Prometheus

Method: Fine-tune Llama-2-Chat-13B on the Feedback Collection (1K rubrics, 20K 
instructions, 100K GPT-4 feedback); input includes a rubric and a reference answer.

## Page 51

CS329Z: Engineering AI Agents

Prometheus

Findings: 0.897 Pearson with humans on 
45 custom rubrics, on par with GPT-4 
(0.882) and far above GPT-3.5 (0.392).

## Page 52

CS329Z: Engineering AI Agents

Brieﬂy, what do rubrics look like? \[Pointwise vs. Pairwise\]

Two ways to ask a judge: “how good is this?” or “which is better?”

Prompt: Explain why the sky is blue to a 10-year-old.

Response A: “Sunlight hits air molecules, 
and shorter wavelengths undergo stronger 
Rayleigh scattering, roughly ∝ 1/λ⁴.”

Response B: “Sunlight has every color mixed 
in. Air bounces blue light around the most, so 
blue reaches your eyes from all over the sky.”

Pointwise: Rate each answer on scale
Pairwise: Compare, which is better?

## Page 53

CS329Z: Engineering AI Agents

\[Phase 2\] Human Preferences

Can an LM judge which output people would prefer?

1.
Can we learn a judge from human preferences?

Learning from summarizing, InstructGPT

2.
Can a prompted LM stand in for human raters?

MT-bench & ChatbotArena

3.
How do we make these judges better and trustworthy?

Prometheus

## Page 54

CS329Z: Engineering AI Agents

\[Phase 3\] Human Actions

## Page 55

CS329Z: Engineering AI Agents

\[Phase 3\] Human Actions

Phase 2 is very single-turn / dialogue centric. Phase 3 asks: can an LM judge an 
agent’s actions and their eﬀects, not just its words?

●
Can an LM tell whether an agent’s trajectory succeeded?
●
Can the judge act like an agent, inspecting the environment itself?
●
How reliable are these judges compared with human experts?

Tl;dr: Let’s try judging actions, environments, and trajectories (beyond messages). 
Like Phas 2, the same judge can score an agent (eval) or reward it (training)

## Page 56

CS329Z: Engineering AI Agents

WebVoyager

Motivation: Live websites don’t have an answer key or database to check. Can a 
VLM look at what an agent did and judge whether it succeeded?

He et al., “WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models,” ACL 2024

## Page 57

CS329Z: Engineering AI Agents

WebVoyager

Method: Save screenshots of agent's navigation, then have GPT-4V judge the 
trajectory and ﬁnal answer; humans grade the same tasks to check the judge.

## Page 58

CS329Z: Engineering AI Agents

WebVoyager

Findings: WebVoyager reaches 59.1% success on live websites (vs. 40.1% text-only), 
and the GPT-4V judge’s scores track human labels closely overall (57.1%), though 
individual sites can diﬀer by 10+ points.

## Page 59

CS329Z: Engineering AI Agents

WebVoyager

Findings: The GPT-4V judge agrees with humans 85.3% of the time (κ = 0.70), 
making live-website evaluation scalable.

## Page 60

CS329Z: Engineering AI Agents

Autonomous Evaluation of Digital Agents

Motivation: Web and device agents only get graded by hand-written benchmark 
checks. Can a model judge a trajectory, and use that to improve the agent?

Pan et al., “Autonomous Evaluation and Refinement of Digital Agents,” COLM 2024

## Page 61

CS329Z: Engineering AI Agents

Autonomous Evaluation of Digital Agents

Method: Vision-language evaluators read the instruction plus screenshots of the 
agent’s trajectory and output success or failure.

## Page 62

CS329Z: Engineering AI Agents

Autonomous Evaluation

Method: Vision-language evaluators read the 
instruction plus screenshots of the agent’s 
trajectory and output success or failure.

## Page 63

CS329Z: Engineering AI Agents

Autonomous Evaluation of Digital Agents

Findings: 74.4 to 92.9% agreement with oracle metrics. Used as a reward, they 
improve a WebArena agent by 29% (relative) and an iOS agent by ~75%.

## Page 64

CS329Z: Engineering AI Agents

Agent-as-a-Judge

Motivation: Agents produce workspaces, not just answers. Can judge be an agent?

Zhuge et al., “Agent-as-a-Judge: Evaluate Agents with Agents,” ICML 2025

## Page 65

CS329Z: Engineering AI Agents

Agent-as-a-Judge

Method: DevAI: 55 AI-dev tasks with 365 hierarchical requirements. Judge agent 
explores workspace (locate, read, search, check the trajectory) to verify.

## Page 66

CS329Z: Engineering AI Agents

Agent-as-a-Judge

Findings: ~90% agreement with human experts vs. ~70% for LLM-as-a-Judge, at 
~97% less time and cost than a panel of three experts.

## Page 67

CS329Z: Engineering AI Agents

\[Phase 3\] Human Actions

Phase 3: can an LM judge an agent’s actions and their eﬀects, not just its words?

●
Can an LM tell whether an agent’s trajectory succeeded?

WebVoyager: VLMs reading screenshots agree with humans 85% of the time, 
and with oracle checks 74–93%.

●
Can the judge act like an agent, inspecting the environment itself?

Agent-as-a-Judge: letting the judge explore the workspace raises agreement 
with experts from ~70% to ~90%.

## Page 68

CS329Z: Engineering AI Agents

\[Phase 3\] Human Actions

Phase 3: can an LM judge an agent’s actions and their eﬀects, not just its words?

●
How reliable are these judges compared with human experts?

Good enough to train with (Pan: +29% on WebArena), but oﬀ by 10+ points on 
some slices (WebVoyager’s per-site gaps)

## Page 69

CS329Z: Engineering AI Agents

Biases + Validating Judgment

## Page 70

CS329Z: Engineering AI Agents

Biases + Validating Judgment

LM judges may have arbitrary biases. Let’s take a look at some of them + how 
we’ve dealt with them.

●
LM judges may be biased by the order of answers.
●
LM judges may be biased by the length of answers.
●
How do we build a judge that matches human judgment for my task?

## Page 71

CS329Z: Engineering AI Agents

LLMs Are Not Fair Evaluators

Motivation: When a judge compares 2 answers, does it matter which is shown ﬁrst?

Wang et al., “Large Language Models are not Fair Evaluators,” ACL 2024 (arXiv May 2023)

## Page 72

CS329Z: Engineering AI Agents

LLMs Are Not Fair Evaluators

Method: DevAI: 55 AI-dev tasks with 365 hierarchical requirements. Judge agent 
explores workspace (locate, read, search, check the trajectory) to verify.

## Page 73

CS329Z: Engineering AI Agents

LLMs Are Not Fair Evaluators

Method: DevAI: 55 AI-dev tasks with 365 hierarchical requirements. Judge agent 
explores workspace (locate, read, search, check the trajectory) to verify.

## Page 74

CS329Z: Engineering AI Agents

LLMs Are Not Fair Evaluators

Findings: ~90% agreement with human experts vs. ~70% for LLM-as-a-Judge, at 
~97% less time and cost than a panel of three experts.

## Page 75

CS329Z: Engineering AI Agents

Length-Controlled AlpacaEval

Motivation: LLM judges favor longer answers, and models learned to exploit it. Can 
we remove a known bias after the fact?

Dubois et al., “Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators,” COLM 2024

## Page 76

CS329Z: Engineering AI Agents

Length-Controlled AlpacaEval

Method: Fit regression that predicts judge’s preference from LM, the instruction, 
and the length diﬀerence; then ask what it would prefer if lengths were equal.

## Page 77

CS329Z: Engineering AI Agents

Length-Controlled AlpacaEval

Findings: Much harder to game with verbosity, and Spearman correlation with 
Chatbot Arena rises from 0.94 to 0.98.

## Page 78

CS329Z: Engineering AI Agents

Length-Controlled AlpacaEval

Findings: Much harder to game with verbosity, and Spearman correlation with 
Chatbot Arena rises from 0.94 to 0.98.

## Page 79

CS329Z: Engineering AI Agents

AutoMetrics

Motivation: Real user feedback is the gold standard, but it’s scarce for new tasks. 
Can a handful of human labels produce a judge that matches their judgment?

Ryan et al., “AutoMetrics: Approximate Human Judgments with Automatically Generated Evaluators,” ICLR 2026

## Page 80

CS329Z: Engineering AI Agents

AutoMetrics

Method: Get candidates from 48 existing metrics (MetricBank) plus auto-generated 
LLM-judge criteria. Fit a regression to the human labels to pick and weight them.

## Page 81

CS329Z: Engineering AI Agents

AutoMetrics

Findings: +33.4% Kendall correlation with human ratings than LLM-as-a-Judge, from 
fewer than 100 labels; also works as a proxy reward as well as a veriﬁable one.

## Page 82

CS329Z: Engineering AI Agents

Biases + Validating Judgment

●
LM judges may be biased by the order of answers.

Position, length, self-preference: errors that always lean the same way, so more 
examples don’t cancel them out.

●
LM judges may be biased by the length of answers.

Wang et al. 2023 (position), Length-Controlled AlpacaEval (length)

●
How do we build a judge that matches human judgment for my task?

AutoMetrics: build and check a judge against a small set of human labels.

## Page 83

CS329Z: Engineering AI Agents

Handling Nondeterminism

## Page 84

CS329Z: Engineering AI Agents

Handling Nondeterminism

Recall: Let’s say you run a task 5 times, and get: ❌ ✅ ❌ ❌ ✅

How do you report this outcome?

●
Average (40%): Communicates expected success rate per try.
⇒ Hides: So is each attempt a coin ﬂip? Or tasks are always all pass/fail?

●
At least once (Yes): Says whether agent is capable of solving task at all.
⇒ Hides: Luck + cost of retrying. What if you scale arbitrarily to k retries?

●
Solved every time (No): Says whether you can count on agent
⇒ Hides: Near-misses and potential infra failings. Goes towards 0% w/ more k.

## Page 85

CS329Z: Engineering AI Agents

pass@k

Introduced in HumanEval (Chen et al 2023), pass@k = “probability that at least one 
of k independent solution attempts will succeed”.

### Page links

- [Link 1](https://arxiv.org/abs/2107.03374)

## Page 86

CS329Z: Engineering AI Agents

pass^k

Introduced in tau-bench (Yao et al 2024), pass@k = “of all the ways to pick k of n 
trials, what fraction of these combinations are all passes?”.

### Page links

- [Link 1](https://arxiv.org/abs/2406.12045)

## Page 87

CS329Z: Engineering AI Agents

Why not just report the average?

Two agents can share the same average and behave completely diﬀerently.

Average
pass@2
pass^2

A
50%
83%
17%

B
50%
50%
50%

A: retrying helps a lot, but you 
can’t count on any single run.

B: retrying doesn’t help, but what 
it solves, it solves every time.

## Page 88

CS329Z: Engineering AI Agents

Which one should you use?

It really depends on how your agent is being used.

pass@k
You can retry, and a check picks 
the winner.

●
Coding with tests: sample k 
patches, keep one that passes
●
Research or Search: any 
correct ﬁnd is enough

pass^k
Every attempt reaches a user or 
changes the world.

●
Customer service: each 
customer gets 1 try
●
Generally, if agents take real 
actions (purchases, emails)

Either way: report k + number of trials n. Without k, the number is meaningless.
