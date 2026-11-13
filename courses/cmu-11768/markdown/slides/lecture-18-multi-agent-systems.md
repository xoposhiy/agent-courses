# Lecture 18 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-18-multi-agent-systems.pdf) · [Raw file](../../raw/slides/lecture-18-multi-agent-systems.pdf)

Retrieved: 2026-11-13T16:45:36.471290+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

A I  AG E N TS  |  L E CT U R E  1 8
Multi-agent Systems

Saujas Vaduguru

Carnegie Mellon University

Interaction 1 · October 29, 2026

1

## Page 2

What are multi-agent systems?

Agent

Agent

Agent

Environment
actions modify environment state

observation

& reward

observation

& reward

observation

& reward

action

action

joint
action

action

Figure adapted from Albrecht, Christianos & Schäfer, Multi-Agent Reinforcement Learning (MIT Press, 2024) ↗
2

### Page links

- [Link 1](../optional-readings/ref-77bc037fa503.md)

## Page 3

Why multi-agent systems?

Improved test-
time compute

Agents as abstractions that
allow for more effective use
of resources

Interacting with
other entities

Agents that work on
inherently multi-agent
problems

Training and
evaluation
environments for
agents

Using other agents to train
for and evaluate single
agent behavior

3

## Page 4

Multi-agent systems for test-time compute

Context management

The entire interaction builds up in context

Serial execution

All tasks have to be performed in a sequence,
even if they don't have any dependencies

Lack of specialization

The same LLM has to perform all parts of the
task

Limited exploration

Agents don't compare multiple approaches
and get locked in to one solution

A single agent typically works in a single stream

4

## Page 5

Role-based decomposition

Roles. An agent is created by an LLM prompted to play a specific role, typically
based on a role a person plays in a team of humans

Interaction. Agents in a system interact with other agents playing different roles

Orchestration. Agents are typically orchestrated with a fixed workflow

Communication. Agents may interact through messages passed to a subset of
agents on a board, sent only to an orchestrator, or through artifacts

In-Context Impersonation · Salewski et al., NeurIPS 2023 ↗
5

### Page links

- [Link 1](../optional-readings/arxiv-2305-14930.md)

## Page 6

Virtual software companies

ChatDev · Qian et al., ACL 2024 ↗
6

### Page links

- [Link 1](../optional-readings/arxiv-2307-07924.md)

## Page 7

Implementing a multi-agent workflow

calendar_agent = create_agent(
    model, tools=\[create_calendar_event, get_available_time_slots\],
    system_prompt="You are a calendar scheduling assistant. ..."
)

email_agent = create_agent(model, tools=\[send_email\], system_prompt="You are an email assistant. ...")

@tool
def schedule_event(request: str) -> str:
    return calendar_agent.invoke({"messages": \[{"role": "user", "content": request}\]})\["messages"\]\[-1\].text

@tool
def manage_email(request: str) -> str:
    return email_agent.invoke({"messages": \[{"role": "user", "content": request}\]})\["messages"\]\[-1\].text

supervisor_agent = create_agent(
    model, tools=\[schedule_event, manage_email\],
    system_prompt="You are a helpful personal assistant. You can schedule calendar events and send emails. ..."
)

LangChain docs · Subagents: personal assistant ↗
Lecture 15: Orchestration and Monitoring (slides) ↗
7

### Page links

- [Link 1](https://cmu-agents.com/slides/lecture-15-orchestration-and-monitoring.pdf)
- [Link 2](../optional-readings/ref-272d34aff8ce.md)

## Page 8

Open-ended delegation

Pre-defined roles and workflows are limiting

Sub-problems may not fall into neat categories that map to human roles

The number of agents needed for different tasks may be different

Open-ended delegation uses generic agents, but coordinates among multiple

instances

Depending on the specific method, the number may also be spawned as needed

8

## Page 9

Multi-agent debate

User Input: A treasure hunter found a buried treasure chest filled with gems. There were 175 diamonds, 35 fewer
rubies than diamonds, and twice the number of emeralds than the rubies. How many of the gems were there in the
chest?

Round 1

User Input: Using the solutions from other agents as additional information, can you give an updated response....

(Copy Agent 2’s reply)
(Copy Agent 1’s reply)

Round 2

User Input: Using the solutions from other agents as additional information, can you give an updated response....

(Copy Agent 2’s reply)
(Copy Agent 1’s reply)

Round 3

Agent 1: Let x be the number of rubies. Then the
number of diamonds is 175. And the number of…

Agent 2: If there were 175 diamonds, then the
number of rubies is 35 fewer, or 175 - 35 = 140…

Agent 1: Given the information provided in other
agents' solutions, we have two answers: One age…

Agent 2: After reviewing the solutions provided by
other agents, I agree with the second agent who…

Agent 1: After reviewing the solutions provided by
other agents, I agree with the second agent who…

Agent 2: After reviewing the solutions provided by
other agents, I also agree that the number of rubi…

Figure adapted from Du et al., Multiagent Debate, ICML 2024 ↗
9

### Page links

- [Link 1](../readings/arxiv-2305-14325.md)

## Page 10

Multi-agent debate results

Du et al., Multiagent Debate, ICML 2024 ↗
10

### Page links

- [Link 1](../readings/arxiv-2305-14325.md)

## Page 11

Launching subagents on demand

ROOT AGENT
depth=0

Task

Plan a 3-day Kyoto trip in early
April for a family. We want cherry
blossoms, one quiet temple, one…

1 Action

Find cherry-blossom…
less-crowded viewing…
early April…

Find Quiet temple + kid activity
+ … near Gion

Env

\["Philosopher’s path early…",
 "Shoren-In Temple; Kyoto…"\]

2 Action

finish("3-day Kyoto plan:…
Philosopher’s Path, …")

SUB-AGENT A
depth=1

Task

Find cherry blossom timing & less-
crowded viewing spots in Kyoto…

2 Action

finish("Philosopher’s path in
morning; Kyoto Botanical…")

SUB-AGENT B
depth=1

Task

Find Quiet temple + kid activity…

1 Action

One quiet Kyoto…

One kid-friendly…

2 Action

finish("Shōren-in, Kyoto…")

SUB-SUB-AGENT B.1
depth=2

Task

One quiet Kyoto temple, early April.
Best option.

1 Action

search_web("quiet temple…")

Env

\[{"title": "Shōren-in…"}, …\]

2 Action

finish("Shōren-in Temple")

SUB-SUB-AGENT B.2
depth=2

Task

One kid-friendly Kyoto activity…

1 Action

finish("Kyoto Railway Museum")

Figure adapted from Gandhi et al., Recursive Agent Optimization, arXiv 2026 ↗
11

### Page links

- [Link 1](../readings/arxiv-2605-06639.md)

## Page 12

Programmatic primitives for subagent
coordination

Tool that launches an clone of the agent with the argument as its goal

Run in parallel and gather  results

Use await  to sequence operations

Use Python’s built-in async context management tools to share state

async def launch_subagent(subgoal, ...) -> Any:
    ...

12

## Page 13

Delegating to subagents uses context effectively

Gandhi et al., Recursive Agent Optimization, arXiv 2026 ↗
13

### Page links

- [Link 1](../readings/arxiv-2605-06639.md)

## Page 14

Managed delegation to subagents

MACU · Koh, Salakhutdinov & Fried, Multi-Agent Computer Use, arXiv 2026 ↗
14

### Page links

- [Link 1](../readings/arxiv-2606-01533.md)

## Page 15

Delegation improves performance on longer,
more parallelizable tasks

MACU · Koh, Salakhutdinov & Fried, Multi-Agent Computer Use, arXiv 2026 ↗
15

### Page links

- [Link 1](../readings/arxiv-2606-01533.md)

## Page 16

Coordinating asynchronous agents

CAID · Geng & Neubig, Effective Strategies for Asynchronous Software Engineering Agents, arXiv 2026 ↗
16

### Page links

- [Link 1](../optional-readings/arxiv-2603-21489.md)

## Page 17

Coordinating asynchronous agents

Manager produces a DAG for planning

Manager communicates using structured JSON messages

Agents use Git to work in parallel with managed conflicts

Repurposing human coordination tools for agent coordination

CAID · Geng & Neubig, Effective Strategies for Asynchronous Software Engineering Agents, arXiv 2026 ↗
17

### Page links

- [Link 1](../optional-readings/arxiv-2603-21489.md)

## Page 18

Blackboard coordination

Salemi et al., LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science, arXiv 2025 ↗
18

### Page links

- [Link 1](../optional-readings/arxiv-2510-01285.md)

## Page 19

Waiting on subagents

DeLM · Mao et al., Decentralized Multi-Agent Systems with Shared Context, arXiv 2026 ↗
19

### Page links

- [Link 1](../optional-readings/arxiv-2606-10662.md)

## Page 20

Decentralized, asynchronous action

DeLM · Mao et al., Decentralized Multi-Agent Systems with Shared Context, arXiv 2026 ↗
20

### Page links

- [Link 1](../optional-readings/arxiv-2606-10662.md)

## Page 21

Decentralized, asynchronous action

Orchestration

Task queue is public

Each task is marked with the agent doing
that task

Communication

Public message board as shared context

Append-only

Typed entries that may carry attachments

DeLM · Mao et al., Decentralized Multi-Agent Systems with Shared Context, arXiv 2026 ↗
21

### Page links

- [Link 1](../optional-readings/arxiv-2606-10662.md)

## Page 22

Using Git to coordinate an agent swarm

GitSwarm · Shah et al., Decentralized Compounding Inference, arXiv 2026 ↗
22

### Page links

- [Link 1](../optional-readings/arxiv-2610-04862.md)

## Page 23

Communicating swarms do better than agents
acting alone

Park et al., Scaling Discovery through Test-Time Communication, arXiv 2026 ↗
23

### Page links

- [Link 1](../readings/arxiv-2609-21032.md)

## Page 24

…but not always

Communication does not outperform pass@k on Terminal-Bench 2.0.

Method
Mean Accuracy
Max Accuracy

Single agent pass@1
52.53%
–

Independent pass@2
62.36%
64.04%

Communicating team@2
60.67%
61.80%

Table 3 from Park et al., Scaling Discovery through Test-Time Communication, arXiv 2026 ↗
24

### Page links

- [Link 1](../readings/arxiv-2609-21032.md)

## Page 25

Verified progress sharing allows for effective
collaboration

Park et al., Scaling Discovery through Test-Time Communication, arXiv 2026 ↗
25

### Page links

- [Link 1](../readings/arxiv-2609-21032.md)

## Page 26

Interacting with other entities

26

## Page 27

Human-agent interaction as a multi-agent
system

SWEET-RL · Zhou et al., Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks, arXiv 2025 ↗
27

### Page links

- [Link 1](../readings/arxiv-2503-15478.md)

## Page 28

User simulators

Tomlin and Lin, What does it take to build a human-like user simulator?, blog 2025 ↗
28

### Page links

- [Link 1](../optional-readings/ref-f1c813ab9187.md)

## Page 29

Learning from simulated interactions

PPP · Sun et al., Training Proactive and Personalized LLM Agents, COLM 2026 ↗
29

### Page links

- [Link 1](../optional-readings/arxiv-2511-02208.md)

## Page 30

Learning from simulated interactions

R = R

​ +
Prod
R

​ +
Proact
R

​.
Pers

PPP · Sun et al., Training Proactive and Personalized LLM Agents, COLM 2026 ↗
30

### Page links

- [Link 1](../optional-readings/arxiv-2511-02208.md)

## Page 31

Overfitting and simulator collapse

Yu et al., One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL, arXiv 2026 ↗
31

### Page links

- [Link 1](../optional-readings/arxiv-2608-12253.md)

## Page 32

Communicating with a diverse group of agents
prevents collapse

Yu et al., One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL, arXiv 2026 ↗
32

### Page links

- [Link 1](../optional-readings/arxiv-2608-12253.md)

## Page 33

Conventions and emergent communication

GlossoGen · Stengel-Eskin et al., Emergent Language in Complex Multi-Agent LLM Interactions, arXiv 2026 ↗
33

### Page links

- [Link 1](../optional-readings/arxiv-2609-01491.md)

## Page 34

Conventions and emergent communication

GlossoGen · Stengel-Eskin et al., Emergent Language in Complex Multi-Agent LLM Interactions, arXiv 2026 ↗
34

### Page links

- [Link 1](../optional-readings/arxiv-2609-01491.md)

## Page 35

Communicating through directory names

METR, Independent investigation of the OpenAI / Hugging Face hacking incident, 2026 ↗
35

### Page links

- [Link 1](../optional-readings/ref-8e38112b54f3.md)

## Page 36

Simulating an agentic marketplace

Magentic Marketplace · Bansal et al., An Open-Source Environment for Studying Agentic Markets, arXiv 2025 ↗
36

### Page links

- [Link 1](../optional-readings/arxiv-2510-25779.md)

## Page 37

Simulating a town of generative agents

Generative Agents · Park et al., Interactive Simulacra of Human Behavior, UIST 2023 ↗
37

### Page links

- [Link 1](../optional-readings/arxiv-2304-03442.md)

## Page 38

Training and evaluation
environments for agents

38

## Page 39

Expressing uncertainty in responses

Zhou et al., Relying on the Unreliable, ACL 2024 ↗
39

### Page links

- [Link 1](../optional-readings/ref-3152627e51f7.md)

## Page 40

Multi-agent information seeking game

Eisenstein et al., Don't lie to your friends: Learning what you know from collaborative self-play, CoLM 2025 ↗
40

### Page links

- [Link 1](../readings/arxiv-2503-14481.md)

## Page 41

When is it optimal to hedge?

The game setup elicits calibration as the
equilibrium outcome

= chance that agent  guesses correctly

with search

= chance that the agent guesses

correctly from parametric knowledge

= cost of search

α
​i
i

β

δ

Eisenstein et al., Don't lie to your friends: Learning what you know from collaborative self-play, CoLM 2025 ↗
41

### Page links

- [Link 1](../readings/arxiv-2503-14481.md)

## Page 42

How can we trust a powerful agent?

Khan et al., Debating with More Persuasive LLMs Leads to More Truthful Answers, ICML 2024 ↗
42

### Page links

- [Link 1](../readings/arxiv-2402-06782.md)

## Page 43

Debate helps judges arrive at better conclusions

Khan et al., Debating with More Persuasive LLMs Leads to More Truthful Answers, ICML 2024 ↗
43

### Page links

- [Link 1](../readings/arxiv-2402-06782.md)

## Page 44

AI agents in multi-agent systems

Improved test-
time compute

Role-based
decompositions

Orchestrated delegation

Asynchronous action
and swarms

Interacting with
other entities

Human-agent
interaction as a multi-
agent system

Training collaborative
models

Emergent
communication

Training and
evaluation
environments for
agents

Learning calibration in
multi-agent games

Supervision through
debate

44
