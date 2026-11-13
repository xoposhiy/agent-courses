# Lecture 1: Introduction — What Are Agentic Systems?

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture01.pdf) · [Raw file](../../raw/slides/lecture01.pdf)

Retrieved: 2026-11-13T16:17:26.829778+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

CS 329Z:Engineering AI Agents
Intro to Agentic Systems

Diyi Yang, Michael Ryan, John Yang

## Page 2

Welcome to CS329Z: Engineering AI Agents

2

## Page 3

Welcome to CS329Z: Engineering AI Agents

●
Contact:

○
Post on Ed

○
Other issues email cs329z-staff@lists.stanford.edu

●
Website: http://web.stanford.edu/class/cs329z

●
Ed Discussion: https://edstem.org/us/courses/106723/discussion

3

### Page links

- [Link 1](http://web.stanford.edu/class/cs329z)
- [Link 2](https://edstem.org/us/courses/106723/discussion)
- [Link 3](mailto:cs329z-staff@lists.stanford.edu)

## Page 4

Lecture Overview

●Course logistics (10 mins)

●History of agents (15 mins)

●Agent architectures (20 mins)

●Compound AI systems: RAG, tool use, MCP (10 mins)

●Key challenges: training, eval, safety (15 mins)

## Page 5

Why CS329Z: Engineering AI Agents

Both modeling and systems perspectives in the age of LLM agents

●
LLM people know how models are trained, prompted, aligned, and 
evaluated

●
Systems people know how to build reliable software: tools, APIs, 
environments, infrastructure…

Expectation:

●
Lectures on foundations + hands-on building/evaluating of agents

5

## Page 6

A Quick Glance of CS329Z: Foundational Basics

●
LLMs for builders

●
Retrieval-augmented generation

●
Tool use and function calling

●
Agent design and scaffolds

●
Agent memory

●
Multi-agent systems

6

●
Optimization and harness

●
Data for agentic systems

●
Evaluation and benchmark

●
Agent safety and guardrails

●
Coding agents

●
Proactive agents

Week 1- Week 5
After Week 5

## Page 7

A Quick Glance of CS329Z: Special Guests

7

## Page 8

Class Activities

●
Project (40%)

○
Proposal  (5%)

○
Midway report (5%)

○
Midpoint demo (5%)

○
Final submission (15%)

○
Final system demo (10%)

●
Homeworks (15%)

●
Homework-based quizzes (15%)

●
Paper video (10%)

●
Peer review (20%)

8

## Page 9

Clarification on Class Activities \[details to come\]

●
Homework-based quiz

○
15-min oral check-in on any part of your submission

●
Paper video

○
Pick an agent paper not covered in class

○
Record a 10-min video presenting it

●
Peer review

○
Paper videos, midpoint demos, agent evaluations, final system demos

○
Give constructive, specific feedback

○
Graded on usefulness and on whether authors adopt it

9

## Page 10

Instructor Office Hours 
https://cs329z.stanford.edu/logistics.html#office-hours

10

## Page 11

Course Policy

●
Please familiarize yourself with Stanford's honor code.

●
You should use AI to learn.

●
Laptop use is strongly discouraged during the lecture.

●
Each student will have a total of 3 free late (calendar) days.

○
Peer review and final project papers cannot be turned in late under any 
circumstances.

11

## Page 12

Prerequisites and Compute

●
Strongly recommended: CS 224N, 224V, CS 336, or equivalent

●
You are expected to know basic LLMs: to the extent that you 
understand concepts like train/dev/test set, pretraining, fine-tuning, 
alignment, prompting, etc. (We will not cover these in this course!)

●
Compute: 200$ support from Laude Institute and 250$ from 
Thinking Machine

12

## Page 13

Enrollment and Waitlist

●
The course is unfortunately at capacity

●
Spots often open up in the first two weeks

●
Lecture slides and videos will be posted online

13

## Page 14

14

## Page 15

The Hidden Cost: Skills Erode

RCT, 52 engineers learning a new Python library, with vs. without AI assistance

AI users scored 17% lower on follow-up quiz (~ two letter grades)

Gap was most pronounced on debugging, the skill seniors 
are made of

Shen & Tamkin (Anthropic, 2026)

https://www.anthropic.com/research/AI-assistance-coding-skills

“We found that using AI

assistance led to a 
statistically significant

decrease in mastery”

## Page 16

Use AI to learn how to learn : )

It’s about you and your CS329Z

16

## Page 17

Lecture Overview

●Course logistics (10 mins)

●History of agents (15 mins)

●Agent architectures (20 mins)

●Compound AI systems: RAG, tool use, MCP (10 mins)

●Key challenges: training, eval, safety (15 mins)

Learning Objective: get familiar with an agent loop on top of LLMs, key 
components of agents, and open problems about agent training and eval

## Page 18

Agents

18

## Page 19

History of Agents (before 1990)

●
The word “agent” from Latin agens, late 15th c; “one who acts”

●
First indexed “AI use” is from Hewitt, Bishop and Steiger in 1973

"A Universal Modular ACTOR Formalism," IJCAI 1973

## Page 20

History of Agents (before 1990)

●
The word “agent” from Latin agens, late 15th c; “one who acts”

●
First indexed “AI use” is from Hewitt, Bishop and Steiger in 1973

●
Contract Net Protocol on agents negotiating tasks in 1980

●
Marvin Minsky on the Society of Mind in 1986

## Page 21

History of Agents (the 1990s)

21

(Pattie Maes, Designing 
Autonomous Agents, 1994)

Wooldridge and Jennings define an

agent by autonomy, social ability,

reactivity and proactivity (1995)

Russell and Norvig's textbook (1995)

defines an agent as anything that 
perceives through sensors and acts

through actuators

## Page 22

History of Agents: the RL Era

22

Agent-environment  loop

(Sutton and Barto, 1998)

DQN on Atari (Mnih et al., 2015)

## Page 23

History of Agents: the LLM Era

23
GPT3 and in context learning

## Page 24

What LLMs Made Possible: Reasoning and Tool Use

24

Modular Reasoning, 
Knowledge and 
Language (MRKL, 2022)

### Page links

- [Link 1](https://arxiv.org/pdf/2205.00445)

## Page 25

The Emergence of “Agents”

Oct 2022

ReAct

Nov 30, 2022

ChatGPT

Mar 14, 2023

GPT-4

Mar 28, 2023

BabyAGI

Mar 30, 2023

AutoGPT

(Yao et al., 2022)
https://github.com/yoheinakajima/babyagi_archive

### Page links

- [Link 1](../readings/arxiv-2210-03629.md)

## Page 26

LLMs Getting Better: Model Capability

https://epoch.ai/data-insights/gpt-capabilities-progress

## Page 27

Agents Getting Better: Agentic Capability

## Page 28

Lecture Overview

●Course logistics (10 mins)

●History of agents (15 mins)

●Agent architectures (20 mins)

●Compound AI systems: RAG, tool use, MCP (10 mins)

●Key challenges: training, eval, safety (15 mins)

## Page 29

Anatomy of an Agent

(ReAct: Yao et al., 2022)

the model →LLM Core

Think\[…\] →Planning & Reasoning

traces so far →Memory

Act: →Tools

Obs: →Environment

## Page 30

30

LLM Core

Planning & Reasoning
Memory

Tools
Retrieval, Calculator, Code, Search, File Operations…

Agent actions: tool call, interaction, response to users

Environment 
(external world)

Desktop OS,
Web browser,

Mobile apps,

Games,
Databases,

etc
act

observe

Agents: Key Components

## Page 31

Similar Definitions of Agents

https://lilianweng.github.io/posts/2023-06-23-agent/

Cognitive Language Agents 
(Sumers and Yao, 2024)

### Page links

- [Link 1](../readings/arxiv-2309-02427.md)

## Page 32

Agents: Key Components

32

LLM Core

Planning & Reasoning
Memory

Tools
Retrieval, Calculator, Code, Search, Read/Write Memory…

Agent actions: tool call, interaction, response to users

Environment 
(external world)

Desktop OS,
Web browser,

Mobile apps,

Games,
Databases,

etc
act

observe

## Page 33

Reasoning and Planning

• For humans: mental 
processes such as 
deduction, analogy and 
planning

• For LLMs: intermediate 
generations that imitate 
various (but not all) 
human mental processes

• For agents: internal 
actions that update the 
agent’s own state

33

Action

Observation

## Page 34

Why is reasoning helpful for agents?

34

Obs

Act

Observation to Action mapping could be hard

“The dish should be savory, and since salt is 
out, I should find the soy sauce instead. It is in 
the cabinet to my right…”
Reasoning

Reason to act

1.
Generalization

2.
Alignment

You see a cabinet and a table…

You are cooking a dish and seeing salt is out…
Obs t

Turn right
Act t

Obs t+1

Open cabinet
Act t+1

## Page 35

Reasoning without acting

35

Answer: iPod

Standard

Thought: Let's think step by step. Apple Remote was originally designed to 
interact with Apple TV. Apple TV can be controlled by iPhone, iPad, and iPod 
Touch. So the answer is iPhone, iPad, and iPod Touch.

Answer: iPhone, iPad, iPod Touch

Reason Only

Question: Aside from the Apple Remote, what other device can control the 
program Apple Remote was originally designed to interact with?

## Page 36

Reasoning with acting

36

Question: Aside from the Apple Remote, what other device can control the 
program Apple Remote was originally designed to interact with?

ReAct (Reason + Act)

✓

Thought 1: I need to search Apple Remote and find the program it was originally designed to interact with.
Act 1: Search\[Apple Remote\]
Obs 1: The Apple Remote is a remote control introduced in October 2005 by Apple … originally designed to control 
the Front Row media center program ……(long text omitted)

Thought 2: Apple Remote was originally designed to control the Front Row media center program. I need to search 
Front Row next and find what other device can control it.
Act 2: Search\[Front Row\]
Obs 2: Could not find \[Front Row\]. Similar: \['Front Row Seat to Earth', 'Front Row Motorsports','Front Row 
(software)', …\]

Thought 3: Front Row is not found. I need to search Front Row (software) .
Act 3: Search\[Front Row (software)\]
Obs 3: Front Row is a discontinued media center software …(long text omitted)

Thought 4: Front Row (software) is controlled by an Apple Remote or the keyboard function keys. So the answer is 
keyboard function keys.
Act 4: Finish\[keyboard function keys\]

## Page 37

Comparing ReAct with COT, SC

• ReAct outperforms Act consistently
• Hallucination is a serious problem 
for CoT, and ReAct can help mitigate

37

## Page 38

Self-Consistency \[Wang et al., 2023\]

• Prompt a language model using chain-of-thought (CoT) prompting

• Generate a diverse set of reasoning paths

• Aggregate by choosing the most consistent answer in the final answer set

## Page 39

Reflexion: agents reflect via natural language feedback
(Shinn et al., 2023)

Reflexion agents verbally reflect on task feedback signals, then maintain 
their own reflective text to induce better decision-making.

39

## Page 40

Reduce error cases by using self-reflection to distill long, failed trajectories 
into relevant experiences that can be used as "self-hints" in the future

40

Reflexion: agents reflect via natural language feedback

## Page 41

Multi-agent debate to improve reasoning \[Du et al., 
2023\]

41

### Page links

- [Link 1](https://arxiv.org/pdf/2305.14325)

## Page 42

Multi-agent debate to improve reasoning \[Du et al., 2023\]

42

### Page links

- [Link 1](https://arxiv.org/pdf/2305.14325)

## Page 43

Coordinate with Orchestrator

https://www.microsoft.com/en-us/research/publication/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/

## Page 44

Agents: Key Components

44

LLM Core

Planning & Reasoning
Memory

Tools
Retrieval, Calculator, Code, Search, Read/Write Memory…

Agent actions: tool call, interaction, response to users

Environment 
(external world)

Desktop OS,
Web browser,

Mobile apps,

Games,
Databases,

etc
act

observe

## Page 45

The Need for Memory

Context window cannot possibly hold all the event streams
Even if possible, might be hard to attend to relevant events, or digest over them

45

Generative agents 
(Park et al., 2025)

## Page 46

Different Types of Memory

Note: we only categorize based on memory content, which is inspired by human long-term memory systems

Type by content
Definition
Examples

Episodic memory
Stores experience
Generative agents 
\[Park et al., 2023\]

Semantic memory
Stores knowledge

Procedural 
memory

Stores skills
Voyager 
\[Wang et al., 2023\]

### Page links

- [Link 1](../readings/arxiv-2304-03442.md)
- [Link 2](https://arxiv.org/abs/2305.16291)
- [Link 3](https://en.wikipedia.org/wiki/Long-term_memory)

## Page 47

Episodic Memory

•
Write: append-only event streams
•
Read: retrieval based on heuristic scores

47

## Page 48

Semantic Memory

•
Write: LLM reasoning over events
•
Read: retrieval

48

## Page 49

Procedural Memory \[Wang et al., 2023\]

•
Write: Code-based skills
•
Read: Embedding retrieval

49

## Page 50

Agents: Key Components

50

LLM Core

Planning & Reasoning
Memory

Tools
Retrieval, Calculator, Code, Search, Read/Write Memory…

Agent actions: tool call, interaction, response to users

Environment 
(external world)

Desktop OS,
Web browser,

Mobile apps,

Games,
Databases,

etc
act

observe

## Page 51

Toolformer: LLMs can teach themselves to use tools

• Toolformer trains LMs to 
decide which APIs to call, 
when to call them, what 
arguments to pass, and how to 
best incorporate the results.

• Tools: calculator, Q&A system, 
search engine, translation 
system, calendar.

51

### Page links

- [Link 1](../readings/arxiv-2302-04761.md)

## Page 52

Gorilla: LLMs connected with massive APIs (Patil et al., 2023)

52

### Page links

- [Link 1](../readings/arxiv-2305-15334.md)

## Page 53

Putting It All Together: Skeleton of an Agent

53

LLM Core

Planning & Reasoning
Memory

Tools
Retrieval, Calculator, Code, Search, Read/Write Memory…

Agent actions: tool call, interaction, response to users

Environment 
(external world)

Desktop OS,
Web browser,

Mobile apps,

Games,
Databases,

etc
act

observe

## Page 54

Lecture Overview

●Course logistics (10 mins)

●History of agents (15 mins)

●Agent architectures (20 mins)

●Compound AI systems: RAG, tool use, MCP (10 mins)

●Key challenges: training, eval, safety (15 mins)

## Page 55

Agents: Three Layers

Despite many components, agent engineering can be divided into:

The system (architecture design etc.)

The data (training examples, demonstrations, context)

The evals ( + the metric)

## Page 56

Workflows vs. Agents: Who Decides the Steps?

Both are compound AI systems: an LLM plus other components

•
Workflow: code fixes the steps (e.g., Agentless, AlphaCode 2)
•
Agent: the LLM decides the steps (e.g., SWE-agent)

Zaharia et al., The Shift from Models to Compound AI Systems, BAIR, 2024 (https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/)

AlphaCode2: fine-tuned 
LLMs for sampling and 
scoring programs; code 
execution module. It 
generates up to 1 million 
solutions for a coding problem 
then filters and scores them.

## Page 57

Retrieval Augmented Generation (RAG)

57

1. RETRIEVE

Search your 
documents for

relevant info

2. AUGMENT

Add context to the

user's question

3. GENERATE

LLM answers using

retrieved facts

RAG connects LLMs to external knowledge sources in real-time

## Page 58

Tool Use: Anatomy of a Call

58

Select

which tool, from

the schemas in

context

→

Arguments

typed fields, 
filled from the

task

→

Validate

schema check,

constrained

decoding

→

Execute

sandboxed; 
result returns to

context

Example: “What does test.py contain?”

read_file

Chosen from the 
tools in context

{“path”: “test.py”}

filled from the

task

path: string

checked before

the call

def add(a, b): …

returned to

context

## Page 59

Model Context Protocol (MCP)

59

https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture

## Page 60

Lecture Overview

●Course logistics (10 mins)

●History of agents (15 mins)

●Agent architectures (20 mins)

●Compound AI systems: RAG, tool use, MCP (10 mins)

●Key challenges: training, eval, safety (15 mins)

## Page 61

Key Challenges in Building Agents

Reliability
Errors compound in agent setup

Training
Sparse reward, long horizon, expensive rollouts

Long-horizon
Context grows and drifts

Safety
Task success ≠ safe behavior

Evaluation
What and how to evaluate

## Page 62

Reliability vs Evaluation

01

Consistency

across runs

Do agents produce the

same outcome when given

the same task twice?

02

Robustness

to perturbations

How do agents respond to

small, realistic shifts in

prompts, tools, etc?

03

Predictable

failure modes

When agents fail, do they

fail in legible, recoverable

ways or unpredictably

https://hal.cs.princeton.edu/

## Page 63

The Capability-Reliability Gap

HAL Reliability Dashboard (https://hal.cs.princeton.edu/reliability/)

## Page 64

Task Completion ≠ Safety Compliance

64
HarnessAudit Bench (https://harnessaudit.github.io/)

## Page 65

Lack of Collaboration Awareness and Agency

65

https://www.platformer.news/openai-operator-ai-agent-hands-on/

### Page links

- [Link 1](https://www.platformer.news/openai-operator-ai-agent-hands-on/)

## Page 66

Pop-ups for agents lead to 87% attack success rate

(i.e., AI agents get distracted and can’t finish the original task)

66

Adversarial Attacks

Zhang, Yanzhe, Tao Yu, and Diyi Yang. "Attacking Vision-Language Computer Agents via Pop-ups." arXiv preprint arXiv:2411.02391 (2024).

## Page 67

Privacy and Security Concerns

67

Shao, Yijia, Tianshi Li, Weiyan Shi, Yanchen Liu, and Diyi Yang. "PrivacyLens: Evaluating Privacy Norm Awareness of Language Models in Action.” NeurIPS D&B 2024

## Page 68

Misalignment and Sycophancy

68
https://www.anthropic.com/research/reward-tampering

Misalignment and Sycophancy

## Page 69

Multi-agent Collusion

69
https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#core-takeaways-about-this-incident

## Page 70

Multi-agent Collusion

70

## Page 71

Lecture Summary

✅Course logistics

✅History of agents

✅Agent architectures

LLM core, planning & reasoning, memory, tools, environment

✅Compound AI systems: RAG, tool use, MCP

✅Key challenges

Reliability, training, long-horizon, safety, evaluation
