# Lecture 5 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-05-planning.pdf) · [Raw file](../../raw/slides/lecture-05-planning.pdf)

Retrieved: 2026-11-13T16:45:26.400523+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Planning and Task Decomposition

Daniel Fried

11-768: AI Agents

How agents decide what to do. Plus, a bit of multi-agent.

1

## Page 2

A reactive agent on a long task

TASK

Buy the lab's new GPU workstation: compare configurations and prices across vendor sites, check compatibility
against the cluster requirements on the internal wiki, and file the purchase requisition.

1 ACTION
goto vendor-a.com → Workstations → spec sheet → GPU
comparison ...

15 ACTION
configure: 2× RTX 6000, 128 GB RAM, 850 W PSU

31 OBSERVE
wiki: “racks accept 4U chassis; each slot with 1600 W”

context compacted · 128k → 14k tokens.
four vendors searched: only D fits, but has 20-week lead time

201 ACTION
pick D? look for a fifth vendor? relax a requirement?

202 ACTION
goto procurement portal → New requisition → Submit

1
Four independent searches run
as one thread in one context.

2
The four sites it chose all come
back and none is great.

3
It picks one anyway and files the
requisition.

2

## Page 3

Structure in a long task

Vendor A

Vendor B

Vendor C

Vendor D

Vendor E

Compatibility

check (wiki)
Requisition

arrives later

irreversible

replan

The task has parallel searches, dependencies, information that arrives later in the task, and a step that cannot be undone.

The graph itself also changes: when none of the four vendors fits, a fifth search has to be added.

TODAY'S QUESTIONS

Value

When is planning useful?
When can it hurt?

Representation

How is a plan
represented?

Commitment

When is a plan made, and
what may change it?

Oversight

How/when should a
person weigh in?

3

## Page 4

Plan Mode in coding agents

read-only
investigation →
clarifying
questions
→
written

plan
→
human

review
→
execution

Cursor, Claude Code, and Codex all introduced a
Plan Mode: write a persistent plan, have a
human verify it, carry it out (possibly with sub-
agents, in parallel).

Possibly helpful: more compute, better context,
an external artifact, decomposition, or the
human approval.

Cursor · “Introducing Plan Mode,” 2025 ↗
Claude Code permission modes ↗
OpenAI model guidance ↗
4

### Page links

- [Link 1](../optional-readings/ref-4e84b30d1d6b.md)
- [Link 2](../readings/ref-8478702a8e1e.md)
- [Link 3](../optional-readings/ref-5c4b950aaeff.md)

## Page 5

What is a plan (for LLM agents)?

WORKING DEFINITION

A plan is an explicit representation of intended future behavior: the actions or
subgoals an agent will attempt, with any ordering or dependencies among them.

A plan is for this task. (versus a skill, which provides reusable guidance across tasks). Plans can
be more specific than skills.

A plan organizes future work. It may specify actions or subgoals, along with their ordering and
dependencies.

A plan is a proposal, not a guarantee. It can be inspected and revised: by the user, another
model, or interactions with the environment.

“Everybody has a plan until they get punched in the mouth.” — Mike Tyson

5

## Page 6

Planning across the course

Topic
Lecture

Prompted plans and harness structure: decomposition,
replanning, plan artifacts
This lecture

A fixed workflow for coding (Agentless)
Coding agents

Multi-agent roles and communication
Interaction 1

Clarification and human approval
Interaction 2

Search over plans and predicted futures; MACU and RAO
revisited
Search 1–2

6

## Page 7

Decomposition before acting

“Weeks of programming can save you hours of planning.” — programmer proverb

7

## Page 8

Chain-of-thought is a plan

KOJIMA ET AL. 2022
WANG ET AL. 2023

Provides extra compute and a scratchpad for the model to refer back to

Plan and solution arrive in one model generation. Nothing explicitly inspects the plan.

The CoT can be trained to increase the probability of a correct answer (STaR, Zelikman et al.; DeepSeek
R1).

Q: \[problem\]
A: Let's think step by step.

Q: \[problem\]
A: Let's first understand the problem and
devise a plan to solve the problem. Then,
let's carry out the plan and solve the
problem step by step.

Kojima et al. · NeurIPS 2022 ↗
Wang et al. · ACL 2023 ↗
Zelikman et al. (STaR) · NeurIPS 2022 ↗
DeepSeek-AI (DeepSeek-R1), 2025 ↗
8

### Page links

- [Link 1](../optional-readings/arxiv-2203-14465.md)
- [Link 2](../optional-readings/arxiv-2205-11916.md)
- [Link 3](../optional-readings/arxiv-2305-04091.md)
- [Link 4](../optional-readings/arxiv-2501-12948.md)

## Page 9

Decomposing before solving

Separate out planning fom
solving:

Stage 1 writes subquestions.
Stage 2 answers them in order
and passes answers forward.

Models struggled at
answering complex questions
but were better at answering
sub-questions.

Answering sub-questions
requires less context.

Improvements grow with
problem length.

Least-to-Most · Zhou et al., ICLR 2023 · Figure 1 ↗
Recursive Language Models · Zhang et al., 2025 ↗
9

### Page links

- [Link 1](../readings/arxiv-2205-10625.md)
- [Link 2](../optional-readings/arxiv-2512-24601.md)

## Page 10

Decomposition allows modularity

A decomposer generates sub-tasks and routes each sub-task to a dedicated handler.

What awards have movies produced by people born in 1910 won? ->
Who were born in the year 1910? simple QA  + For which moves was #1 the producer? position QA  + ...

Modularity allows improving handler models independently: via in-context demonstrations or
training.

Programmatic/structured control: we'll see this later on with RAO, RLM, and MACU.

Decomposed Prompting · Khot et al., ICLR 2023 · Figure 1 ↗
10

### Page links

- [Link 1](../readings/arxiv-2210-02406.md)

## Page 11

Plans that act on the world

"We'll burn that bridge when we come to it."

11

## Page 12

Reasoning versus acting

A CoT reasoning step

changes only text

can be undone by writing more

every intermediate is visible

plans are useful if the model can
condition on them better

An action in the world

changes the state the agent meets next

can reveal information

can fail

can be irreversible: submit, send

Acting means plans must handle feasibility, consequences, information, and recovery.

12

## Page 13

Classical planning

A state is a set of predicates;
actions have preconditions
and effects.

A valid sequence of actions
satisfies every action's
preconditions.

Planning is a search problem:
find a sequence of valid
actions that reach the goal.

states

on-table(x) · on(x, y)
clear(x) · holding(x)
hand-empty

actions

pick-up(x) · unstack(x, y)
put-down(x) · stack(x, y)

preconditions + effects

pick-up(x): on-table(x) ∧ clear(x) ∧ hand-empty
→ holding(x) ∧ ¬on-table(x) ∧ ¬hand-empty

initial state + goal

on(blue, orange) · clear(red, blue, yellow)
goal: on(orange, blue)

plan

unstack(blue, orange)
put-down(blue)
pick-up(orange)
stack(orange, blue)

PlanBench · Valmeekam et al., NeurIPS 2023 Datasets & Benchmarks · p. 6 ↗
STRIPS · Fikes and Nilsson, Artificial Intelligence 1971 ↗
13

### Page links

- [Link 1](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf)
- [Link 2](../optional-readings/arxiv-2206-10498.md)

## Page 14

What is hard has changed

With LLMs everything is implicit!

For an LLM agent, writing a plausible plan is easier, and knowing whether its
model of the world is correct is harder.

So agent design uses less deep search, and more checking the world: observation,
verification, and recovery from errors.

But search, and action applicability, are still useful concepts

14

## Page 15

Plan representations

Formal plans are checkable; language plans are
general. Programs are in-between.

Line of work in ~2023: use a code LLM to write
code that calls perception and control APIs

The program runs and can be inspected, but is
limited by what its APIs and programmatic
structure allow.

... but, APIs could call an LLM or another neural
model

Code as Policies · Liang et al., ICRA 2023 ↗
ProgPrompt · Singh et al., ICRA 2023 ↗
Binder · Cheng et al., ICLR 2023 ↗
15

### Page links

- [Link 1](../readings/arxiv-2209-07753.md)
- [Link 2](../optional-readings/arxiv-2209-11302.md)
- [Link 3](../optional-readings/arxiv-2210-02875.md)

## Page 16

Why replan while acting?

DECISIONS MADE BEFORE EXECUTION
DECISIONS MADE DURING EXECUTION

Developer-defined workflow

The developer specifies the procedure:

check a fixed vendor list.

Agentless (next lecture)

→

Plan-then-execute agent

The model plans which vendors to check,

then commits before execution.

plan-then-execute

→

Adaptive agent

After four vendors fail, execution feedback

leads the model to search for another.

RAO · MACU

DEVELOPER-DEFINED PROCEDURE
Committing to a plan up front is faster,
cheaper, and more predictable.

Replanning lets the model adapt when
execution reveals new information.

Use replanning when that feedback is
worth the extra cost and complexity.

for v in VENDORS:               # fixed list

specs\[v\] = read_specs(v)    # model call

ok = \[v for v in specs if fits(v)\]

requisition(cheapest(ok))

Anthropic · “Building effective agents,” 2024 ↗
16

### Page links

- [Link 1](https://www.anthropic.com/research/building-effective-agents)

## Page 17

Reasons to add planning

structure

modularity · feedback · long horizons · control

“Plan to throw one away; you will, anyhow.” — Fred Brooks, The Mythical Man-Month

17

## Page 18

Planning pressures in the workstation task

GPU WORKSTATION PROCUREMENT

Search vendor A

Search vendor B

Search vendor C

Search vendor D

Check configurations

against the wiki

Submit purchase

requisition

MODULARITY
Searches carried out separately.

Search another vendor

FEEDBACK
None fits, so revise the plan.

LONG HORIZON
Requirements and progress persist across the whole task.

CONTROL
A person approves
before the agent submits.

18

## Page 19

Separating planner from executor

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Separate modules can use different models and training data.

Planner model (GPT-4o) is visually grounded but
bad at producing pixel-level actions: describe the
next action in language.

A separately trained 7B executor model maps that
description to screen coordinates.

UGround · Gou et al., ICLR 2025 · Figure 2 ↗
Agent S · Agashe et al., ICLR 2025 ↗
19

### Page links

- [Link 1](../optional-readings/arxiv-2410-05243.md)
- [Link 2](../optional-readings/arxiv-2410-08164.md)

## Page 20

Training the planner

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Have a teacher
model segment and
label successful
trajectories to
produce a plan.

Fine-tune a planner
model and an
executor model on
these annotated
trajectories.

Plan-and-Act · Erdogan et al., ICML 2025 · Figure 3 ↗
20

### Page links

- [Link 1](../readings/arxiv-2503-09572.md)

## Page 21

Beware of fixed roles and multi-agent systems

Role decompositions for coding have had limited success.

Roles are fixed before the task arrives: the
verifier cannot localize a fault to check its own
answer.

Handoffs are summary reports, which can drop
context the next agent needs.

Don’t Sleep on Single-agent Systems · Neubig, 2024 ↗
CodeR · Chen et al., 2024 · Figure 1 ↗
21

Graham

Neubig

### Page links

- [Link 1](../optional-readings/arxiv-2406-01304.md)
- [Link 2](../optional-readings/ref-b067890a8880.md)

## Page 22

Modeling affordances

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Recall classic planning:
actions have pre-conditions.

Learn a value function for
each robotic skill, which
predicts probability of
completing it.

Multiply this value with the
probability from the LLM
producing the plan.

SayCan rescores sub-tasks in the plan using a model of skill affordances.

SayCan · Ahn et al., CoRL 2022 · Figure 3 ↗
Zero-Shot Planners · Huang et al., ICML 2022 ↗
22

### Page links

- [Link 1](../optional-readings/arxiv-2201-07207.md)
- [Link 2](../readings/arxiv-2204-01691.md)

## Page 23

Replanning on environmental feedback

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

LLM-Planner · Song et al., ICCV 2023 · Figure 1 ↗
Inner Monologue · Huang et al., CoRL 2022 ↗
SwiftSage · Lin et al., NeurIPS 2023
23

### Page links

- [Link 1](../optional-readings/arxiv-2207-05608.md)
- [Link 2](../optional-readings/arxiv-2212-04088.md)
- [Link 3](../optional-readings/arxiv-2305-17390.md)

## Page 24

Thinking vs acting

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Match compute across three
different inference methods.

Produce longer CoTs, sample
multiple candidates, or interact
more with the environment.

"You just signaled task
completion. Let's pause and
think again."

Scaling interaction allows
obtaining more information
from the environment, like
Reflexion.

Test-Time Interaction · Shen et al., NeurIPS 2025 · Figure 3 ↗
24

### Page links

- [Link 1](../readings/arxiv-2506-07976.md)

## Page 25

Overthinking

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Patterns: analysis paralysis, rogue action
chains, premature disengagement.

More overthinking predicts less issue resolution
across model types.

Cuadron et al., 2025 · Figures 1 and 4 ↗
25

### Page links

- [Link 1](../optional-readings/arxiv-2502-08235.md)

## Page 26

Thinking vs looking

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

WHAT THE AGENT DOES NOT KNOW

Every file has a hidden format with
three parts:

delimiter
,  ;  \t

quote character
"  '

header rows to skip
0  1

Twelve combinations, and the file only parses if

all three are right. The filename is the only clue:

sales_fr.tsv  points to a tab.

Calibrate-then-Act · Ding, Tomlin, Durrett, 2026 · Figure 1 ↗
PPP-Agent · Sun et al., COLM 2026 ↗
26

### Page links

- [Link 1](../optional-readings/arxiv-2511-02208.md)
- [Link 2](../readings/arxiv-2602-16699.md)

## Page 27

Calibrating confidence before acting

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

WHAT CTA ADDS TO THE PROMPT

Additional context:
 • Estimated format likelihoods
   are provided below.

Format likelihoods:
{prior}

What the model then reads out of it:

The delimiter is most likely to be ';'  with a

probability of ~0.85 … But I'm not 100% sure,
so maybe I should run some unit tests to
confirm.

Calibrate-then-Act · Ding, Tomlin, Durrett, 2026 · Figure 2 ↗
27

### Page links

- [Link 1](../readings/arxiv-2602-16699.md)

## Page 28

Long-horizon failures

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Vending-Bench: run a simple business for a long time.

Task: price, order, and restock a vending machine.

Horizon: up to 2,000 messages—about 25M tokens and
up to 222 simulated days.

Later actions condition on the agent’s earlier mistake.

Was this just a bad plan?

One temporary error affects every later
decision.

PREMATURE RESTOCK
Due today ≠ already delivered
The environment correctly reports: items unavailable.

↓

WRONG INFERENCE
“Unavailable now” → “business failed”
The agent never waits for the fulfillment email or
checks again.

↓

ERROR PERSISTS
Daily fee becomes “fraud”

Subject: EMERGENCY: Unauthorized Fees After
Business Termination

Vending-Bench · Backlund and Petersson, 2025 · Tables 3–4 ↗
28

### Page links

- [Link 1](../optional-readings/arxiv-2502-15840.md)

## Page 29

Execution horizon

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Better step accuracy extends the horizon, while self-conditioning can make later steps less accurate.

Sinha et al., 2025 · Figure 1 ↗
29

### Page links

- [Link 1](../optional-readings/arxiv-2509-09677.md)

## Page 30

Model size and execution horizon

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Larger models execute longer tasks but self-condition more. Can reinforcement learning fix this?

Sinha et al., 2025 · Figure 1 ↗
30

### Page links

- [Link 1](../optional-readings/arxiv-2509-09677.md)

## Page 31

Decomposing adaptively and recursively

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

Delegation is an action, so it can be
trained.

The agent calls

launch_subagent(goal)  to run a
copy of itself on a subtask, and that
copy can do the same.

Each node is scored on its own task
plus how often its children
succeeded.

Trained on medium tasks only, it
delegates deeper on hard ones.

RAO · Gandhi et al., 2026 · Figures 1 and 7 ↗
Recursive Language Models · Zhang et al., 2025 ↗
ADaPT · Prasad et al., NAACL Findings 2024
31

Apurva Gandhi

### Page links

- [Link 1](../optional-readings/arxiv-2311-05772.md)
- [Link 2](../optional-readings/arxiv-2512-24601.md)
- [Link 3](../readings/arxiv-2605-06639.md)

## Page 32

Plans as security boundaries

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

ReAct lets every page influence the next action,
creating an injection path.

A program can accept values from pages
without accepting new actions.

Piet et al., 2026 · Figure 1 ↗
32

### Page links

- [Link 1](../optional-readings/arxiv-2605-14290.md)

## Page 33

Control: human editing and approval

Cursor
Introducing Plan Mode
Introducing Plan Mode

Watch on

Cursor · Introducing Plan Mode ↗
33

### Page links

- [Link 1](https://www.youtube-nocookie.com/channel/UC6YYHJzM6PhZ2Yey9BQiUaw)
- [Link 2](https://www.youtube.com/watch?v=WInPBmCK3l4)

## Page 34

Global constraints

Some constraints span every subtask.

Flights, hotels, food, and attractions
decompose cleanly.

Budget, transport, and diet remain global—and
are often violated across pieces.

TravelPlanner · Xie et al., ICML 2024 · Figure 1 ↗
34

### Page links

- [Link 1](../optional-readings/arxiv-2402-01622.md)

## Page 35

Multi-agent computer use

Putting it all together

35

## Page 36

Example task: finding ACL surgeons

Odysseys · Jang, Koh, Fried, Salakhutdinov, 2026 ↗
36

Lawrence Jang
Jing Yu Koh

### Page links

- [Link 1](../optional-readings/ref-4bec3d68e90a.md)

## Page 37

Example task: finding ACL surgeons

Odysseys · Jang, Koh, Fried, Salakhutdinov, 2026 ↗
37

Lawrence Jang
Jing Yu Koh

### Page links

- [Link 1](../optional-readings/ref-4bec3d68e90a.md)

## Page 38

Long-horizon computer use

Modularity
decompose and specialize

Feedback
replan when needed

Long horizon
limit context

Control
separate authority

MACU · Koh, Salakhutdinov, Fried, 2026 ↗
38

Jing Yu Koh

### Page links

- [Link 1](../readings/arxiv-2606-01533.md)

## Page 39

0:00 / 0:23

39

## Page 40

Where multiple agents help

MACU · Koh, Salakhutdinov, Fried, 2026 · Table 1 ↗
40

### Page links

- [Link 1](../readings/arxiv-2606-01533.md)

## Page 41

Stronger managers improve coordination

OSWORLD ABLATION · 36 TASKS · QWEN3.5-4B WORKER

MACU · Koh, Salakhutdinov, Fried, 2026 ↗
41

### Page links

- [Link 1](../readings/arxiv-2606-01533.md)

## Page 42

Weaker workers are lifted more

OSWORLD ABLATION · 36 TASKS · OPUS 4.6 MANAGER

MACU · Koh, Salakhutdinov, Fried, 2026 ↗
42

### Page links

- [Link 1](../readings/arxiv-2606-01533.md)

## Page 43

Worker parallelism on Odysseys

ODYSSEYS EASY SUBSET · 45 TASKS

MACU · Koh, Salakhutdinov, Fried, 2026 ↗
43

### Page links

- [Link 1](../readings/arxiv-2606-01533.md)

## Page 44

Revising the graph

MACU · Koh, Salakhutdinov, Fried, 2026 · Table 2 ↗
44

### Page links

- [Link 1](../readings/arxiv-2606-01533.md)

## Page 45

Closing

45

## Page 46

A design checklist

1
Are the subtasks separable? Would planner and executor benefit from different models or training?

2
Which failures or observations should change the plan?

3
How will the system stop errors and context from accumulating?

4
What information or authority stays separate—and who approves irreversible actions?

Before adding planning structure, ask:

46

## Page 47

Open problems

Checking

Language plans and subgoal graphs have no general
validator.

Calibration

Agents misjudge when to think, look, ask, or revise.

Global state

Cross-subtask constraints resist both decomposition and
longer context.

Scaffolding

Whether trained reasoning absorbs these structures
remains open.

47

## Page 48

Questions?

Next Class: Domains 1 · Coding Agents

48
