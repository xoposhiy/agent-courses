# Lecture 6: Agent Design Patterns & Scaffolds

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf) · [Raw file](../../raw/slides/lecture06.pdf)

Retrieved: 2026-11-13T16:21:01.293483+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Agent Design Patterns and Scaffolds

Diyi Yang, Michael Ryan, John Yang

CS329Z: Engineering AI Agents

## Page 2

CS329Z: Engineering AI Agents

Announcements

• Google credit submissions are due ASAP.  Do this today if you haven’t 
yet!  Details on Ed.

• Please be careful about ICLR submission format.  We will be mostly 
lenient about this proposal, but will enforce for midpoint/final reports.

• Homework 1 is due Friday October 30th.

• Midpoint demo due November 4th, report due November 6th.

## Page 3

CS329Z: Engineering AI Agents
Image Credit: https://refactoring.guru/design-patterns/singleton

## Page 4

CS329Z: Engineering AI Agents

Martin Fowler — author of “Patterns of Enterprise Application Architecture”

“Patterns are half-baked—meaning you

always have to finish them yourself and 
adapt them to your own environment.”

## Page 5

CS329Z: Engineering AI Agents

When building an agent system you

must make many design decisions.

Today we’ll introduce design patterns.

In practice you will customize your

solutions.

## Page 6

CS329Z: Engineering AI Agents

Learning Objectives

• Define common design patterns for workflows and agents.

• Compare and Contrast different design patterns for context 
management for agents.

• Analyze the design decisions present in a production agent harness 
(e.g. Pi)

## Page 7

CS329Z: Engineering AI Agents

Lecture Overview

• Review: Workflows vs Agents (5 minutes)

• Workflow Design Patterns (15 minutes)

• Agent Design Patterns: Reasoning/Acting (20 minutes)

• Agent Design Patterns: Context (20 minutes)

• Case Study: Pi (10 minutes)

## Page 8

CS329Z: Engineering AI Agents

Review: Workflows and Agents

Workflows vs Agents
Workflow Designs
Reasoning Designs
Context Designs
Case Study

## Page 9

CS329Z: Engineering AI Agents

Where does the control flow lie?

Model
Workflow or 
Compound AI System

Agent

Small part of

a larger

system

Logic and 
Orchestration

Lies in the

Program

Control flow 
is role of the

AI Model

GPT-6 Sol

Claude Fable 5.1

Ex)

Email Categorizer

News feed summarizer

Ex)

Customer Service 
Agent

Coding Agent

Ex)

## Page 10

CS329Z: Engineering AI Agents

Where does the control flow lie?

Image Credit: https://www.langchain.com/blog/how-to-

think-about-agent-frameworks

• Workflows are more predictable than 
agents because the control flow lies 
in the program logic.

• Agents are more adaptable/flexible 
than workflows because the control 
flow lies in the LLMs decisions.

## Page 11

CS329Z: Engineering AI Agents

Workflows vs Agents (Example)

## Page 12

CS329Z: Engineering AI Agents

Workflows vs Agents

Workflows
Agents

Control Flow
Code
LLM

Adaptation
Fixed (programmed) branches,

routes, and loops

Chooses next step based on

observations

Best Fit
Tasks with a clear, repeatable

structure

Tasks requiring exploration and

flexible decisions

Example
Classify support ticket -> retrieve

policy -> draft automatic reply

Resolve support ticket using tools

to investigate/solve the problem.

Real systems often combine workflows and agents.

## Page 13

CS329Z: Engineering AI Agents

Workflow Design Patterns

Workflows vs Agents
Workflow Designs
Reasoning Designs
Context Designs
Case Study

## Page 14

CS329Z: Engineering AI Agents

Anthropic Workflow Taxonomy
https://www.anthropic.com/engineering/building-effective-agents

## Page 15

CS329Z: Engineering AI Agents

Workflow Design Patterns

• Prompt Chaining: Decomposing the problem into smaller steps.

• Routing: Route the task to appropriate LLM.

• Parallelization: Divide the work amongst multiple threads.

• Orchestrator-Workers: Identify subtasks and dispatch workers to complete them.

• Evaluator-Optimizer: Generate an output, critique or respond, and iterate on the 
output.

## Page 16

CS329Z: Engineering AI Agents

Prompt Chaining

Image Credit: https://www.anthropic.com/engineering/building-effective-agents

• Decompose a larger task into a series of smaller steps

• Trades off latency for accuracy

• Useful when a task is complicated and can benefit from decomposition

## Page 17

CS329Z: Engineering AI Agents
Image Credit: https://www.anthropic.com/engineering/building-effective-agents

• Classify an input and route it to the appropriate LLM (could vary on 
model or prompt to handle different cases)

• Helps when a complex task has several categories that could help to 
process differently

• Can also be used to save money/time (weaker model for easier cases)

Routing

## Page 18

CS329Z: Engineering AI Agents
Image Credit: https://www.anthropic.com/engineering/building-effective-agents

• Sectioning: Splitting up parallel independent work (e.g. flagging a query 
as safe/unsafe while simultaneously processing that query)

• Voting: Inference-time scaling where you process the same input several 
times and the aggregator makes the final conclusion

• Enables focusing each call on an individual aspect

Parallelization

## Page 19

CS329Z: Engineering AI Agents
Image Credit: https://www.anthropic.com/engineering/building-effective-agents

• One LLM dynamically breaks down tasks and delegates to worker LLMs

• Useful when it is difficult to anticipate the nature and number of 
subtasks needed

• Similar to parallelization but in this case the subtasks are dynamically 
created.

Orchestrator-Workers

## Page 20

CS329Z: Engineering AI Agents
Image Credit: https://www.anthropic.com/engineering/building-effective-agents

• One LLM generates the response and another provides evaluation and 
feedback in a loop.

• Two necessary conditions: (1) Clear articulable feedback and (2) an LLM 
is capable of providing that feedback.

• Also important that the generator can improve based on the feedback.

Evaluator-Optimizer

## Page 21

CS329Z: Engineering AI Agents

Composition of Workflow Patterns
Real systems are compositions of these basic patterns.

## Page 22

CS329Z: Engineering AI Agents
Image Credit: https://github.com/stanford-oval/storm/tree/NAACL-2024-code-backup

Example: STORM

## Page 23

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.14207

Example: STORM

## Page 24

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.14207

Example: STORM

Approximately “Evaluator-Optimizer”

Prompt Chaining
Parallelization

Orchestrator-Workers*

*This is close to parallelization in this instance

## Page 25

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2402.14207

Example: STORM

## Page 26

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2409.15254

Archon: An Architecture Search Framework for 
Inference-Time Techniques

## Page 27

CS329Z: Engineering AI Agents
Table Credit: https://arxiv.org/pdf/2409.15254

Archon

output

## Page 28

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2409.15254

Archon

## Page 29

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2409.15254

Archon

## Page 30

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2409.15254

Recap

• Workflows are simpler to reproduce and 
debug than agents

• We covered five common workflow patterns: 
prompt chaining, routing, parallelization, 
orchestrator-workers, and evaluator-
optimizer

• In practice real workflows are often larger 
compositions of the individual components

## Page 31

CS329Z: Engineering AI Agents

Agent Design Patterns:

Reasoning/Acting

Workflows vs Agents
Workflow Designs
Reasoning Designs
Context Designs
Case Study

## Page 32

CS329Z: Engineering AI Agents

Agents

Image Credit: https://www.anthropic.com/engineering/building-effective-agents

In addition to the tools themselves we 
need to design *how* the LLM reasons 
and interacts with the environment.

## Page 33

CS329Z: Engineering AI Agents

ReAct (2023)
Key Insight: reason before taking actions

## Page 34

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2210.03629

ReAct: Reason + Act

## Page 35

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2210.03629

ReAct: Finetuning for Agents

Interestingly, the original paper found that you need to fine-tune for best performance.  
Now fine-tuning models to act as agents is common practice during post-training.

## Page 36

CS329Z: Engineering AI Agents
Table Credit: https://arxiv.org/pdf/2210.03629

ReAct: Importance of Reasoning

• Useful to reason before taking 
actions.

• Including thoughts before actions is 
still very common today.

## Page 37

CS329Z: Engineering AI Agents

Reflexion (2023)
Key Insight: self-reflection is useful

## Page 38

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2303.11366

Reflexion: Algorithm

Key Insight: Turn Evaluations/Reflections into “Memory” (context) for the actor LLM.

## Page 39

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2303.11366

Reflexion: Example Trajectories

## Page 40

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2303.11366

Reflexion

Reflexion improves accuracy over trials
It’s the LLM reflection that helps, not

just the past trajectories

## Page 41

CS329Z: Engineering AI Agents
Table Credit: https://arxiv.org/pdf/2310.01798

Limitations of Self-Reflection

• When asking an LLM to evaluate it’s 
own responses it leads to decreased 
performance.

• Reflexion gets around this by using 
external environment feedback.

• This finding pre-dates reasoning 
models, which show impressive 
ability to self-correct during 
reasoning.

• Today self-reflection is typically built 
into the LLM reasoning itself rather 
than explicitly enforced.

## Page 42

CS329Z: Engineering AI Agents
Table Credit: https://arxiv.org/pdf/2310.01798

CRITIC (2024)

Adding External Tools to the Verifier is useful! (Make an agentic verifier)

## Page 43

CS329Z: Engineering AI Agents

CodeAct (2024)
Key Insight: code is the right form factor for actions

## Page 44

CS329Z: Engineering AI Agents

Image Credit: https://arxiv.org/pdf/2402.01030

JSON Actions

Instruction:

Determine the most 
cost-effective country 
to purchase the 
smartphone model 
“CodeAct1”.  The 
countries to consider 
are the USA, Japan, 
Germany, and India.

## Page 45

CS329Z: Engineering AI Agents

Image Credit: https://arxiv.org/pdf/2402.01030

Code Actions

Instruction:

Determine the most 
cost-effective country 
to purchase the 
smartphone model 
“CodeAct 1”.  The 
countries to consider 
are the USA, Japan, 
Germany, and India.
Japan 904.0

“CodeAct 1”, country)

## Page 46

CS329Z: Engineering AI Agents

CodeAct: More Accurate and More Efficient

Image Credit: https://arxiv.org/pdf/2402.01030

Code as Action has a higher success rate and accomplishes tasks in fewer turns.

## Page 47

CS329Z: Engineering AI Agents

Planning then executing
Key Insight: planning enables turning agent action execution back into workflows

## Page 48

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2305.18323

ReWOO: Reasoning WithOut Observation (2023)

## Page 49

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2305.18323

ReWOO

Planning, then executing enables higher accuracy with fewer tokens

## Page 50

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2312.04511

LLMCompiler (2024)

Differences from ReWOO:

Parallel Execution and Dynamic Replanning

## Page 51

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2312.04511

LLMCompiler

## Page 52

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2312.04511

LLMCompiler

## Page 53

CS329Z: Engineering AI Agents

Recap

## Page 54

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2409.15254

Recap

• ReAct: Reasoning before acting is useful.

• Reflexion: Self-reflection is incorporated into 
the reasoning today.

• CodeAct: Code is a good form factor for 
actions.

• ReWOO/LLMCompiler: Compiling 
workflows is primarily done with parallel tool 
calls today.  Planning is still important.

• Sometimes workflows are still used for 
“sub-agent” orchestration.

## Page 55

CS329Z: Engineering AI Agents

Agent Design Patterns:

Context Management

Workflows vs Agents
Workflow Designs
Reasoning Designs
Context Designs
Case Study

## Page 56

CS329Z: Engineering AI Agents

Agents: Context

Image Credit: https://www.anthropic.com/engineering/building-effective-agents

Context 
Manager

## Page 57

CS329Z: Engineering AI Agents

Context Engineering

Image Credit: https://www.anthropic.com/engineering/

effective-context-engineering-for-ai-agents

## Page 58

CS329Z: Engineering AI Agents
Image Credit: https://github.com/gkamradt/needle-in-a-haystack

## Page 59

CS329Z: Engineering AI Agents
Image Credit: https://github.com/gkamradt/needle-in-a-haystack

Context Engineering: Principles

Focus the Context
Preserve Continuity

• Keep only what you need for the 
task at hand in the context 
window.

• The entire history does not need 
to be in the context.

• Excessive information is context-
bloat.

• Manipulate the context to 
preserve requirements, goals, 
constraints, progress, etc.

• Practically this also means 
preserving the KV Cache

## Page 60

CS329Z: Engineering AI Agents

Context Management Patterns

## Page 61

CS329Z: Engineering AI Agents

Context Patterns Overview

• Persistent Event Log: Rebuild the context from the system events

• Memory Offloading: Store knowledge to memory to enable pruning

• Compaction: Summarizing prior context into a compressed description

• Observation Masking: Hiding/truncating old outputs from tool calls

• Context Isolation: Use subagents for specific tasks, only include in the 
context what you actually need for the task at hand.

## Page 62

CS329Z: Engineering AI Agents

Persistent Event Log: OpenHands

Image Credit: https://arxiv.org/pdf/2407.16741v3

## Page 63

CS329Z: Engineering AI Agents
Image Credit: https://docs.openhands.dev/sdk/arch/events

• Everything gets preserved exactly as it happened even if the LLM input must 
be changed.  The event log history can be immutable (append only).

• For every call to the LLM the input is reconstructed from the event log.

• An event log also enables hooks for external observers to monitor the system 
state.

Persistent Event Log: OpenHands

## Page 64

CS329Z: Engineering AI Agents

Memory Offloading: MemGPT

Storing things to memory or files frees up parts of the context to prune

Image Credit: https://arxiv.org/pdf/2310.08560

## Page 65

CS329Z: Engineering AI Agents

Compaction

• Have the LLM summarize prior 
reasoning, action, observation 
instances.

• Compress the history into fewer 
tokens.

• Can be helpful for the 
compaction itself to be agentic.

## Page 66

CS329Z: Engineering AI Agents

Observation Masking

Image Credit: https://arxiv.org/pdf/2508.21433v3

## Page 67

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2508.21433v3

Observation Masking

• Instead of having an LLM 
compact the context into a 
summary you can take old 
observations and truncate them.

• Especially useful for coding 
agents where the observations 
can be quite long.

## Page 68

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2508.21433v3

Observation Masking

## Page 69

CS329Z: Engineering AI Agents

Context Isolation

Image Credit: https://www.langchain.com/blog/context-engineering-for-agents

## Page 70

CS329Z: Engineering AI Agents

Context Isolation: Progressive Disclosure

Image Credit: https://www.anthropic.com/engineering/

equipping-agents-for-the-real-world-with-agent-skills

You don’t need all tools 
and context in the initial 
prompt, you can disclose 
things later as needed 
(e.g. skill files)

## Page 71

CS329Z: Engineering AI Agents

Context Management

NOTE: These strategies are all compatible.  You can 
first offload knowledge to memory then compact the 
context.  You can both use an event log to build the 
context and truncate the observations.  Real systems 
are combinations of many or all of these strategies.

## Page 72

CS329Z: Engineering AI Agents

Recap

## Page 73

CS329Z: Engineering AI Agents

Context Management Taxonomy

Image Credit: https://www.langchain.com/blog/context-engineering-for-agents

## Page 74

CS329Z: Engineering AI Agents

Context Management Taxonomy

Image Credit: https://www.langchain.com/blog/context-engineering-for-agents

This Wednesday
Next Monday

## Page 75

CS329Z: Engineering AI Agents
Image Credit: https://www.anthropic.com/engineering/building-effective-agents

Recap

• Event Logs, Memory, Compaction, 
Observation Masking, and Context Isolation 
make up a few key design patterns for 
context management.

• Real systems combine these patterns 
together to manage the context.

• Context engineering is driven by two core 
principles: keep the context focused and 
preserve continuity.

## Page 76

CS329Z: Engineering AI Agents

Case Study: Pi

Workflows vs Agents
Workflow Designs
Reasoning Designs
Context Designs
Case Study

## Page 77

CS329Z: Engineering AI Agents

Pi Minimalist Agent Harness

## Page 78

CS329Z: Engineering AI Agents

Pi Design Philosophy

“Pi is a minimal agent harness. Adapt Pi to your workflows, not the other way around.”

Pi is an extremely basic harness and people build tons of extensions on top to add all 
the features of other mainstream harnesses.

Things Pi is lacking: 
• No Sub-Agents 
• No Permission Checks 
• No Plan Mode 
• No agent to-do lists 
• No bash in the background

## Page 79

CS329Z: Engineering AI Agents

Pi Tools

• Only read, bash, edit, 
and write are enabled 
by default.

• Minimal tool bloat.

• All other tools are 
subsets of bash.

Image Credit: https://pi.dev/docs/latest/cli#tools

## Page 80

CS329Z: Engineering AI Agents

Pi Agent Loop

Pi has a ReAct style loop of reasoning before acting on JSON tool calls.

Context is built as a tree, and you can return to a prior branch to continue a 
different thread of the conversation.

## Page 81

CS329Z: Engineering AI Agents

Pi Context Management

Image Credit: https://pi.dev/docs/latest/compaction

1. Event Log to LLM Input Conversion

2. Progressive Disclosure through Skill Files

3. Compaction

## Page 82

CS329Z: Engineering AI Agents

Pi Safety

Pi runs at the same permissions as the process, and 
has no popups to ask for permission, so consider it 
always on auto-mode with no protections.

## Page 83

CS329Z: Engineering AI Agents

Recap

• Pi is designed to be a minimalist harness.

• The community has built several extensions.

• The default tools are bash, read, write, and 
edit.

• Pi is a ReAct style agent.

• Context is managed through event logs, 
progressive disclosure, and compaction.

• Pi has no safeguards built in.

## Page 84

CS329Z: Engineering AI Agents

Summary

Workflows vs Agents
Workflow Designs
Reasoning Designs
Context Designs
Case Study

## Page 85

CS329Z: Engineering AI Agents

Summary

• Review: Workflows vs Agents

• Workflow Design Patterns

• Agent Design Patterns: Reasoning/Acting

• Agent Design Patterns: Context

• Case Study: Pi

## Page 86

CS329Z: Engineering AI Agents

Remember to come to class Wednesday

where we will talk about Memory!
