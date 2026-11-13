# Lecture 13: Evaluation Fundamentals & Benchmark Design

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture13.pdf) · [Raw file](../../raw/slides/lecture13.pdf)

Retrieved: 2026-11-13T16:31:25.164136+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

CS329Z: Engineering AI Agents

CS 329Z:Engineering AI Agents
Evaluation Fundamentals &

Benchmark Design

Diyi Yang, Michael Ryan, John Yang

## Page 2

CS329Z: Engineering AI Agents

Roadmap

Evaluation Fundamentals & Benchmark Design

●
What’s a benchmark? \[25 min\]
●
Why benchmarks matter \[5 min\]
●
Agent Benchmarks \[25 min\]
●
What makes a benchmark good? \[15 min\]
●
What makes a score trustworthy? \[10 min\]

tl;dr: We’ll cover the core tenants of agent benchmark design, showcase these 
tenants through several examples, and discuss what makes for a good benchmark.

## Page 3

CS329Z: Engineering AI Agents

What is a benchmark?

## Page 4

CS329Z: Engineering AI Agents

What is a benchmark?

Recall everything we’ve discussed so far:

1. How to build an LM-based agent system

●
Frameworks & Agent Design
●
Memory & Multi-Agent Systems

2. How to train an LM-based agent system to have stronger agent capabilities

●
Optimization
●
Data for Agentic Systems

⚠ How do we know that any of these advancements are working?

## Page 5

CS329Z: Engineering AI Agents

What is a benchmark?

Let’s think back to the many ways we evaluate language models in general. 
Starting from the basics. Recall the LLMs for Builders lecture.

Modeling
Training Objective

## Page 6

CS329Z: Engineering AI Agents

What is a benchmark?

You can certainly just focus on training until your loss can’t get any lower. But why 
stop there? Can an LM actually do real world, natural language (NL) tasks?

Many of these tasks have long been studied by linguists. With the emergence of 
early LMs, several were repurposed into benchmarks to evaluate LM performance.

## Page 7

CS329Z: Engineering AI Agents

What is a benchmark?

For such tasks, we can formulate evaluation generally as response = LM(prompt).

## Page 8

CS329Z: Engineering AI Agents

What is a benchmark?

For such tasks, we can formulate evaluation generally as response = LM(prompt).

## Page 9

CS329Z: Engineering AI Agents

What is a benchmark?

For such tasks, we can formulate evaluation generally as response = LM(prompt).

T5 \[Raﬀel et al. 2019\]

## Page 10

CS329Z: Engineering AI Agents

What is a benchmark?

Large task collection bundles of many NL tasks emerged for comprehensive evals.

\[Srivastava et. al 2023\]

\[Wang et. al 2019\]

\[Hendrycks et. al 2021\]

\[Rajpurkar et al. 2016\]

\[Wang et al. 2019\]

\[Liang et al. 2023\]

## Page 11

CS329Z: Engineering AI Agents

What is a benchmark?

As LMs became more capable, subsequence evaluations pose more diﬃcult tasks.

●
Can LMs do well on tests that humans usually do? (e.g., SAT, AMC 12, AIME, 
GRE, APhO, Bar Examination) ⇒ Examination benchmarks

●
Can LMs respond well to open ended questions? Or hold a conversation well 
over multiple turns? ⇒ Chat benchmarks

●
Can LMs behave safely? Do they refuse queries of malicious intent, or respect 
user-speciﬁc constraints? ⇒ Safety benchmarks

●
Can LMs accomplish a task by interacting with a digital/real environment 
across many turns? ⇒ Agent benchmarks

## Page 12

CS329Z: Engineering AI Agents

Let’s brieﬂy review a bunch of popular, non-agentic LM 
benchmarks. But for this class, we’re generally focused on 
evaluations for LM agents.

## Page 13

CS329Z: Engineering AI Agents

Exam Benchmarks

## Page 14

CS329Z: Engineering AI Agents

Massive Multitask Language Understanding (MMLU)

\[Hendrycks 2020\] Multiple Choice, Knowledge questions covering 57 domains.

### Page links

- [Link 1](https://arxiv.org/abs/2009.03300)

## Page 15

CS329Z: Engineering AI Agents

MMLU-Pro

\[Wang 2024\] 4 ⇒ 10 options, noise questions ended up getting removed.

### Page links

- [Link 1](https://arxiv.org/abs/2406.01574)

## Page 16

CS329Z: Engineering AI Agents

Graduate-Level Google-Proof Q&A (GPQA)

\[Rein 2023\] An even harder exam written by PhD students.

### Page links

- [Link 1](https://arxiv.org/abs/2311.12022)

## Page 17

CS329Z: Engineering AI Agents

Humanity’s Last Exam

\[Phan 2025\] And then an even harder one, both multiple choice and short answer

### Page links

- [Link 1](https://arxiv.org/abs/2501.14249)

## Page 18

CS329Z: Engineering AI Agents

Chat Benchmarks

## Page 19

CS329Z: Engineering AI Agents

AlpacaEval

\[Leaderboard\] Chat based evaluations use win rate or Elo as the main metric

### Page links

- [Link 1](https://tatsu-lab.github.io/alpaca_eval/)

## Page 20

CS329Z: Engineering AI Agents

ChatbotArena

\[Chiang 2024\] Extends AlpacaEval setup to live, in-the-wild prompts.

### Page links

- [Link 1](https://arxiv.org/abs/2403.04132)

## Page 21

CS329Z: Engineering AI Agents

Safety Benchmarks

## Page 22

CS329Z: Engineering AI Agents

HarmBench

\[Mazeika 2024\] How often can red-teaming attacks elicit harmful responses?

### Page links

- [Link 1](https://arxiv.org/abs/2402.04249)

## Page 23

CS329Z: Engineering AI Agents

AIR-Bench

\[Zeng 2024\] 5694 prompts across 314 risk categories that LMs should refuse.

### Page links

- [Link 1](https://arxiv.org/abs/2407.17436)

## Page 24

CS329Z: Engineering AI Agents

What is a benchmark?

Summary

●
We use benchmarks to measure if we’ve improved the behavior and/or 
capabilities of an LM-based system.

●
Benchmarks generally consist of a set of prompts (e.g., questions, instructions, 
requests) along with a metric for reporting performance.

●
Otherwise, benchmarks come in all shapes and sizes! Diﬀerent types of tasks, 
expected model responses, and ways to grade them.

●
The remainder of this lecture + the next lecture will focus exclusively on details 
surrounding benchmarks for LM agents.

## Page 25

CS329Z: Engineering AI Agents

Why benchmarks matter

## Page 26

CS329Z: Engineering AI Agents

Why are benchmarks important?

The concept of a benchmark is not unique to Natural Language Processing or AI.

Computer Vision

Recommender Systems

Robotics

ML for Science

## Page 27

CS329Z: Engineering AI Agents

Why are benchmarks important?

Benchmarks are an important artifact for several reasons:

1.
Measurement: They enable practitioners to develop their models, prompts, 
scaﬀolds against empirical experiments.

2.
Direction: They unite a ﬁeld around shared problems and reﬂect what it has 
collectively decided to work on.

3.
Communication: They give researchers a common language, so “+5 on X” 
means the same thing to everyone and results are comparable across papers.

## Page 28

CS329Z: Engineering AI Agents

The Dark Side of Benchmarks

Goodhart’s Law: "Any observed statistical regularity will tend to collapse once 
pressure is placed upon it for control purposes."

When a measure becomes a target, it ceases to be a good measure.

“Grade essays by length 
and you’ll get long 
essays, not necessarily 
good ones.”

## Page 29

CS329Z: Engineering AI Agents

Agent Benchmarks:

Task Deﬁnition + Evaluation Protocol

## Page 30

CS329Z: Engineering AI Agents

How do we generally deﬁne an agent benchmark?

An agent benchmark asks a system to accomplish a task by acting in an 
environment over many steps, then grades what it accomplished.

Agent Benchmarks

How do they diﬀer from exam, chat, safety, other benchmarks?

●
Input: Not a prompt, but a task + environment to act in
●
Interaction: Not one response, but many turns of action ⇔ observation
●
Output: Not text, but a trajectory + changed environment

## Page 31

CS329Z: Engineering AI Agents

Agent Benchmarks

## Page 32

CS329Z: Engineering AI Agents

Agent benchmarks can be modeled as 2 major components:

1. Task formulation: Deﬁne the task you want to be solved

2. Evaluation protocol: Agent-speciﬁc parameters for how an

LM agent system should be run on the task.

## Page 33

CS329Z: Engineering AI Agents

Agent Benchmarks

Benchmarks can be thought of as a task formulation + evaluation protocol

## Page 34

CS329Z: Engineering AI Agents

Task Formulation

Problem Statement: What are you asking your agent to do? What is the deliverable 
the agent is expected to produce?

## Page 35

CS329Z: Engineering AI Agents

Task Formulation

Environment: Where is your agent going to carry out this task? What initial assets 
are available to the agent to complete this task?

## Page 36

CS329Z: Engineering AI Agents

Task Formulation

Veriﬁcation: How is the agent’s output scored?

## Page 37

CS329Z: Engineering AI Agents

Evaluation Protocol

Agent-speciﬁc parameters that aren’t tied to the benchmark.

●
How many attempts / rollouts / runs per task?

●
How does a rollout terminate? A maximum number of turns / wall clock time / 
compute budget? By the agent’s own accord?

●
What are the LM conﬁgurations (e.g., reasoning eﬀort, temperature)

●
Is the harness ﬁxed? Or is it bring-your-own? What tools are allowed? Is 
internet allowed?

●
How are runs aggregated? What dimensions (cost, turns, tokens) are reported?

## Page 38

CS329Z: Engineering AI Agents

Case Studies: Let’s apply this framework to agent benchmarks 
spanning across coding, web, and user interaction domains.

## Page 39

CS329Z: Engineering AI Agents

TextWorld

\[Côté 2018\] A sandbox that procedurally generates text-adventure games; agents 
read room descriptions and type commands to complete quests.

### Page links

- [Link 1](https://arxiv.org/abs/1806.11532)

## Page 40

CS329Z: Engineering AI Agents

ALFWorld

\[Shridhar 2020\] Household tasks (“put a clean mug in the coﬀee machine”) played 
as text games that mirror a 3D simulator.

### Page links

- [Link 1](https://arxiv.org/abs/2010.03768)

## Page 41

CS329Z: Engineering AI Agents

WebShop

\[Yao 2022\] Buy a product matching a user’s instruction on a simulated e-commerce 
site; graded by how well the purchased item matches.

### Page links

- [Link 1](https://arxiv.org/abs/2207.01206)

## Page 42

CS329Z: Engineering AI Agents

SWE-bench

\[Jimenez 2023\] Resolve real GitHub issues in popular Python repos; graded by 
running the repo’s own unit tests.

### Page links

- [Link 1](../readings/arxiv-2310-06770.md)

## Page 43

CS329Z: Engineering AI Agents

WebArena

\[Zhou 2023\] Complete everyday web tasks on self-hosted copies of real sites 
(shopping, forums, GitLab, maps); graded on the outcome.

### Page links

- [Link 1](https://arxiv.org/abs/2307.13854)

## Page 44

CS329Z: Engineering AI Agents

Tau-bench

\[Yao 2024\] Customer-service agents follow domain policies while talking to an 
LLM-simulated user; graded on the ﬁnal database state.

### Page links

- [Link 1](https://arxiv.org/abs/2406.12045)

## Page 45

CS329Z: Engineering AI Agents

Terminal-bench

\[Merrill 2026\] 89 hard tasks from real workﬂows, done entirely in a terminal, each 
with its own Docker environment and tests.

### Page links

- [Link 1](../readings/arxiv-2601-11868.md)

## Page 46

CS329Z: Engineering AI Agents

OSWorld

\[Xie 2024\] Complete real desktop tasks across apps in a full operating system, 
working from screenshots; graded by checking the ﬁnal system state.

### Page links

- [Link 1](https://arxiv.org/abs/2404.07972)

## Page 47

CS329Z: Engineering AI Agents

CodeClash

\[Yang 2025\] Agents improve their codebases across multi-round tournaments, then 
compete head-to-head in code arenas; given goals, not instructions.

### Page links

- [Link 1](https://arxiv.org/abs/2511.00839)

## Page 48

CS329Z: Engineering AI Agents

BrowseComp

\[Wei 2025\] Find obscure facts that take persistent, creative web browsing to track 
down but are easy to verify once found.

### Page links

- [Link 1](https://arxiv.org/abs/2504.12516)

## Page 49

CS329Z: Engineering AI Agents

VendingBench

\[Backlund 2025\] Run a simulated vending-machine business over many days 
(inventory, pricing, suppliers); scored by ﬁnal net worth.

### Page links

- [Link 1](https://arxiv.org/abs/2502.15840)

## Page 50

CS329Z: Engineering AI Agents

AIRS-bench

\[Lupidi 2026\] 20 ML research tasks drawn from state-of-the-art papers; agents go 
from idea to experiments w/o baseline code and are scored against human SOTA.

### Page links

- [Link 1](https://arxiv.org/abs/2602.06855)

## Page 51

CS329Z: Engineering AI Agents

What makes a benchmark “good”?

## Page 52

CS329Z: Engineering AI Agents

“Good” Benchmarks

A “good” benchmark encompasses a number of qualities. We put forth several, but 
there are certainly other properties worth consideration!

●
Challenging
●
Natural
●
Discriminative
●
Easy to Run
●
Easy to Verify
●
Interpretable
●
Durable

(a) There is a natural 
tension between 
these properties

(b) Benchmarks are 
“living” software. 
These properties 
evolve with the 
models.

## Page 53

CS329Z: Engineering AI Agents

“Good” Benchmarks

A “good” benchmark encompasses a number of qualities. We put forth several, but 
there are certainly other properties worth consideration!

●
Challenging
●
Natural
●
Discriminative
●
Easy to Run
●
Easy to Verify
●
Interpretable
●
Durable

(a) There is a natural 
tension between 
these properties

(b) Benchmarks are 
“living” software. 
These properties 
evolve with the 
models.

A general way to think about “good”: Benchmarks are a vehicle for

communicating to others what your model is \[not\] capable of.

You want your benchmarks to be as easy as possible for others to run.

## Page 54

CS329Z: Engineering AI Agents

Challenging

Tasks should be suﬃciently diﬃcult to point out behavioral or capability gaps.

## Page 55

CS329Z: Engineering AI Agents

Natural

Or, realistic. Tasks reﬂect what people want, not diﬃcult for the sake of diﬃculty.

## Page 56

CS329Z: Engineering AI Agents

Discriminative

A benchmark that distinguishes between LMs surfaces ﬁne-grained discrepancies

## Page 57

CS329Z: Engineering AI Agents

Easy to Run

Make your benchmark runnable with as few commands (1 ideally) as possible. Avoid 
a set up that requires too many steps for others to reproduce.

●
Have 1 script that sets up everything
●
Make system requirements explicit
●
Expose conﬁgurations easily (set via the 
CLI, not by having to change code)

## Page 58

CS329Z: Engineering AI Agents

Easy to Verify

A diﬃcult, natural task: “Write a really good TV show”. Easy-to-verify means a task’s 
veriﬁcation should be (a) smoothly runnable, and (b) is a useful metric.

LM-as-a-Judge
Live Evaluation
Heuristics

Have an LM score the script 
against a rubric.

Release it; measure ratings, 
viewership, retention.

Use a proxy: wins an award, 
critic scores.

●Favors length, own style
●Gameable
●Varies by prompt, judge

●Confound by marketing
●1 sample per release
●Months per data point

●Subjective, small juries
●Sparse winners
●Lagging results

## Page 59

CS329Z: Engineering AI Agents

Interpretable

Easy to understand how the model acted on the task. Trajectories can be analyzed.

## Page 60

CS329Z: Engineering AI Agents

Durable

Resists contamination and gaming. The score is meaningful with respect to the 
capability that it attempts to measure. Ensure task can’t be reward hacked.

## Page 61

CS329Z: Engineering AI Agents

Benchmarks Lifecycle

Propose ⇒ Adapt ⇒ Saturate ⇒ Replace

●
Exams: MMLU ⇒ MMLU-Pro ⇒ GPQA ⇒ HLE

●
Math: GSM8K ⇒ MATH ⇒ AIME ⇒ FrontierMath

●
Chat: MT-Bench ⇒ AlpacaEval (length-controlled) ⇒ Arena-Hard

●
Coding: SWE-bench Veriﬁed ⇒ Multilingual ⇒ Pro ⇒ DeepSWE

●
CUA / Web: WebShop ⇒ WebArena ⇒ OSWorld ⇒ BrowseComp

●
Terminal: Terminal-Bench 1.0 ⇒ 2.1 ⇒ 4.0

●
Tool Use / Customer Service: ToolEmu ⇒ τ-bench ⇒ τ²-bench

## Page 62

CS329Z: Engineering AI Agents

“Good” Benchmarks Checklist

❏
Challenging: Is there headroom for the model to improve?

❏
Natural: Are the tasks something that reﬂects real work?

❏
Discriminative: Does it separate the systems you care about?

❏
Easy to Run: Can a classmate run it in an afternoon?

❏
Easy to Verify: Can tasks be veriﬁed automatically and correctly?

❏
Interpretable: When an agent fails, can you tell why?

❏
Durable: Is it resistant to shortcuts and contaminations?

## Page 63

CS329Z: Engineering AI Agents

What makes a score trustworthy?

## Page 64

CS329Z: Engineering AI Agents

What makes a score trustworthy?

Good benchmarks provides guidelines for eﬀective task formulations.

Score trustworthiness is about best practices to respect the evaluation protocol.

## Page 65

CS329Z: Engineering AI Agents

Fair

Follow the protocol to ensure numbers across a leaderboard are comparable.

Match the benchmark’s

●
Scaﬀold + Tools
●
Turn / Time / Cost Budgets
●
Model settings
●
Attempts per task
●
Internet + Resource access

If you deviate, be clear how and why!

## Page 66

CS329Z: Engineering AI Agents

Reproducible

Make all model, system details explicit so that others can get the same number.

Match the benchmark’s

●
Scaﬀold + Tools
●
Turn / Time / Cost Budgets
●
Model settings
●
Attempts per task
●
Internet + Resource access

If you deviate, be clear how and why!

## Page 67

CS329Z: Engineering AI Agents

Transparent

Report more than the numbers: runs, error bars, costs, settings

Interpretation: At face value, 70% > 67%, but with more information: the 3% gap sits 
inside the error bars, and higher scores cost 3x more per task.

## Page 68

CS329Z: Engineering AI Agents

Honest

Use the test set to measure performance, never to tune or optimize for it.

Don’t tune on test
Don’t cherry-pick runs
Ship the system you 
report

In the 2015, ImageNet 
competition, a team was 
disqualiﬁed for submitting 
to the test set too many 
times.

Reporting pass@1, when 10 
passes were actually run 
selects the “luckiest” run as 
the results.

Report the numbers for the 
system you open source. 
Don’t optimize for the 
leaderboard with one 
variant and release another.

## Page 69

CS329Z: Engineering AI Agents

Trustworthy Score Checklist

❏
Fair: Did you use the benchmark’s harness, budget, and settings? If not, did 
you say how you deviated?

❏
Reproducible: Are the model snapshot, harness, dataset, and image versions 
pinned and recorded?

❏
Transparent: Did you report runs, error bars, cost, and any excluded tasks?

❏
Honest: Did you avoid tuning on the test set or picking your best run? Is the 
evaluated system the one you’re releasing?

## Page 70

CS329Z: Engineering AI Agents

Summary

## Page 71

CS329Z: Engineering AI Agents

Summary

●
To improve LM-based agent systems, we must know how to measure their 
behavior and performance. Benchmarks are the main vehicle for doing this.

●
Benchmarks can be conceptually decomposed into 3 key components: a 
problem statement, an environment, and a metric.

●
A protocol deﬁnes the hyperparameters for running an LM-based agent on a 
benchmark. They ensure fair comparison between all systems.

●
There is no one-evaluation-to-rule-them-all. Our ability to speak on how 
capable a model is in broad strokes relies on tracking many benchmarks.
