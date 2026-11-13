# Lecture 5: Frameworks & Orchestration

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture05.pdf) · [Raw file](../../raw/slides/lecture05.pdf)

Retrieved: 2026-11-13T16:20:05.943212+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Frameworks & Orchestration

Diyi Yang, Michael Ryan, John Yang

CS329Z: Engineering AI Agents

## Page 2

CS329Z: Engineering AI Agents

Announcements

• Project Proposal is due Friday 10/9 at 11:59pm on Gradescope!

• Submit as a group, please do not submit the same proposal individually!

• Apply for Google Credits by this Friday!  Enrolled students should have received 
an email from John.

• You should already have access to OpenRouter credits courtesy of Laude!

• Homework 1 was released, due on Friday October 30th at 11:59pm.

• Start early!  It’s a new homework and it’s pretty long!

## Page 3

CS329Z: Engineering AI Agents

Quick Poll

Who in this room has used

?

## Page 4

CS329Z: Engineering AI Agents

Abstractions in Frameworks

Writing Backprop by hand
Writing Backprop with PyTorch

## Page 5

CS329Z: Engineering AI Agents

Frameworks abstract away some of the

underlying system details.

In the rest of the course you must 
implement/understand the system details.

The goal for today is to learn the

abstractions.

## Page 6

CS329Z: Engineering AI Agents

Learning Objectives

• Identify common frameworks used in agentic system engineering.

• Relate the abstractions introduced by these frameworks back to the 
underlying system designs we have discussed in the course.

• Assess the usefulness of different tools for agent orchestration and 
reliability.

## Page 7

CS329Z: Engineering AI Agents

Lecture Overview

• What does it mean to “Engineer” Agents? (10 mins)

• Frameworks for Workflows and Programs (25 mins)

• Open Source Agent Harnesses (15 mins)

• Orchestration and Telemetry (15 mins)

• Best Practices and Challenges (15 mins)

## Page 8

CS329Z: Engineering AI Agents

Want to follow along with code today?

This lecture notebook will use about $1 or less of OpenRouter credits.

## Page 9

CS329Z: Engineering AI Agents

What does it mean to “Engineer”

Agents?

“Engineer” Agents?
Workflows
Agent Harnesses
Orchestration
Best Practices

## Page 10

CS329Z: Engineering AI Agents

Three Pillars of AI Systems

Data

• Training Data

• Rollouts

• Demonstrations

• Human Feedback

• …

System or

Model

• Language Model

• Compound AI 
System / 
Workflow

• Agentic System

• …

Evaluation +

Metric

• Pass Rate

• Exact Match

• LLM Judge

• Cost/Latency

• …

## Page 11

CS329Z: Engineering AI Agents

Three Pillars of AI Systems

Data

• Training Data

• Rollouts

• Demonstrations

• Human Feedback

• …

System or

Model

• Language Model

• Compound AI 
System / 
Workflow

• Agentic System

• …

Evaluation +

Metric

• Pass Rate

• Exact Match

• LLM Judge

• Cost/Latency

• …

AI System

## Page 12

CS329Z: Engineering AI Agents

Three Pillars of AI Systems

Data

• Training Data

• Rollouts

• Demonstrations

• Human Feedback

• …

System or

Model

• Language Model

• Compound AI 
System / 
Workflow

• Agentic System

• …

Evaluation +

Metric

• Pass Rate

• Exact Match

• LLM Judge

• Cost/Latency

• …

AI System Engineering

## Page 13

CS329Z: Engineering AI Agents

This Course

Introduction — What Are Agentic Systems? LLMs for Builders

Retrieval-Augmented Generation (RAG)
Tool Use & Function Calling

Frameworks & Orchestration
Agent Design Patterns & Scaffolds

Agent Memory Architectures
Multi-Agent Systems

Optimization
What Data Do Agents Need?

Data Selection & Quality
Evaluation Fundamentals & Benchmark Design

LLM-as-Judge & Evaluation Infrastructure
Agent Safety & Guardrails

Coding & Software Agents
Proactive Agents

Frontiers & Open Problems

System or 
Model

Data

Evaluation + 
Metric

Emerging 
Topics

## Page 14

CS329Z: Engineering AI Agents

Framework Landscape

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

…

Spectrum of Control Flow (Agency)

OpenAI API

Anthropic API

…
…

## Page 15

CS329Z: Engineering AI Agents

Framework Landscape

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

OpenAI API

Anthropic API

…
…
…

Reliability: 
…
Observability: 
…
,
,
,

## Page 16

CS329Z: Engineering AI Agents

Framework Landscape

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

OpenAI API

Anthropic API

…
…
…

Reliability: 
…
Observability: 
…
,
,
,

Part 1
Part 2

Part 3

## Page 17

CS329Z: Engineering AI Agents

Are these frameworks actually used?

## Page 18

CS329Z: Engineering AI Agents

Recap

• Engineering AI Systems requires three core components: Data, System, Evals.

• Agency spectrum for ai systems ranges from models ➡ workflows ➡ agents.

• There are frameworks for each level of the spectrum.

• Some frameworks are dedicated to improving the reliability and observability of 
agents.

## Page 19

CS329Z: Engineering AI Agents

Frameworks for Workflows and

Programs

“Engineer” Agents?
Workflows
Agent Harnesses
Orchestration
Best Practices

## Page 20

CS329Z: Engineering AI Agents

Framework Landscape

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

OpenAI API

Anthropic API

…
…
…

Reliability: 
…
Observability: 
…
,
,
,

## Page 21

CS329Z: Engineering AI Agents

## Page 22

CS329Z: Engineering AI Agents

Signatures

Modules

Optimizers

Strictly define Inputs/Outputs to the Language Model.

(What)

(How)

Compose signatures and program logic into callable functions.

Improve the prompts or weights of the program to maximize metrics.

## Page 23

CS329Z: Engineering AI Agents

Live Programming Demo

## Page 24

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Signatures

## Page 25

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Signatures

## Page 26

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Signatures

Not good that these are not following same format…

## Page 27

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Signatures

## Page 28

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Signatures

## Page 29

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Modules

## Page 30

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Modules

## Page 31

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Modules

## Page 32

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Modules

## Page 33

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Modules

## Page 34

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Modules

## Page 35

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers

## Page 36

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers

Data

• Training Data

• Rollouts

• Demonstrations

• Human Feedback

• …

System or

Model

• Language Model

• Compound AI 
System / 
Workflow

• Agentic System

• …

Evaluation +

Metric

• Pass Rate

• Exact Match

• LLM Judge

• Cost/Latency

• …

## Page 37

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers: The Data

## Page 38

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers: The Data

## Page 39

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers: The Metric

## Page 40

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers

## Page 41

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers

## Page 42

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers

## Page 43

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers

## Page 44

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Optimizers

## Page 45

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Agents

## Page 46

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Agents

## Page 47

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Agents

## Page 48

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Agents

## Page 49

CS329Z: Engineering AI Agents

React

Image Credit: https://arxiv.org/pdf/2210.03629

## Page 50

CS329Z: Engineering AI Agents

RLM

Image Credit: https://arxiv.org/pdf/2210.03629

## Page 51

CS329Z: Engineering AI Agents

DSPy Summary

• Signatures define input/output contracts

• Modules compose and specify how the signature contract should be fulfilled

• dspy.Predict, dspy.ChainOfThought, dspy.BestOfN, …

• Optimizers can improve the prompts/weights of a program given data and a 
metric.

• DSPy has built in modules to enable agents to fulfill the signature.

• dspy.ReAct, dspy.RLM

## Page 52

CS329Z: Engineering AI Agents

## Page 53

CS329Z: Engineering AI Agents

Outline of a LangGraph Workflow

The State is a shared workspace for the graph.  You 
can think of it as an object that the graph will modify.

## Page 54

CS329Z: Engineering AI Agents

Outline of a LangGraph Workflow

The State is a shared workspace for the graph.  You 
can think of it as an object that the graph will modify.

Start
End
Every Graph needs a Start and End Node

## Page 55

CS329Z: Engineering AI Agents

Outline of a LangGraph Workflow

The State is a shared workspace for the graph.  You 
can think of it as an object that the graph will modify.

Start
End

Nodes are functions that read and write to/from the shared state

## Page 56

CS329Z: Engineering AI Agents

Outline of a LangGraph Workflow

The State is a shared workspace for the graph.  You 
can think of it as an object that the graph will modify.

Start
End

Edges Define Control Flow

Some Edges are Conditional

## Page 57

CS329Z: Engineering AI Agents

Outline of a LangGraph Workflow

The State is a shared workspace for the graph.  You 
can think of it as an object that the graph will modify.

Start
End

## Page 58

CS329Z: Engineering AI Agents

Outline of a LangGraph Agent

The State (can be message history)

Start

Tools

LLM

End

## Page 59

CS329Z: Engineering AI Agents

Live Programming Demo

## Page 60

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Building the Graph

## Page 61

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Structured I/O

## Page 62

CS329Z: Engineering AI Agents

State

This is a backup slide in case we cannot do the live demo.

## Page 63

CS329Z: Engineering AI Agents

Node

This is a backup slide in case we cannot do the live demo.

## Page 64

CS329Z: Engineering AI Agents

Graph

This is a backup slide in case we cannot do the live demo.

## Page 65

CS329Z: Engineering AI Agents

Graph

This is a backup slide in case we cannot do the live demo.

## Page 66

CS329Z: Engineering AI Agents

Conditional Edges and Workflows

This is a backup slide in case we cannot do the live demo.

## Page 67

CS329Z: Engineering AI Agents

State

This is a backup slide in case we cannot do the live demo.

## Page 68

CS329Z: Engineering AI Agents

Nodes

This is a backup slide in case we cannot do the live demo.

## Page 69

CS329Z: Engineering AI Agents

Conditional Edge

This is a backup slide in case we cannot do the live demo.

## Page 70

CS329Z: Engineering AI Agents

Graph

This is a backup slide in case we cannot do the live demo.

## Page 71

CS329Z: Engineering AI Agents

Graph

This is a backup slide in case we cannot do the live demo.

## Page 72

CS329Z: Engineering AI Agents

Graph

This is a backup slide in case we cannot do the live demo.

## Page 73

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Agents

## Page 74

CS329Z: Engineering AI Agents

Agents

This is a backup slide in case we cannot do the live demo.

## Page 75

CS329Z: Engineering AI Agents

Agents

This is a backup slide in case we cannot do the live demo.

## Page 76

CS329Z: Engineering AI Agents

LangGraph Summary

• LangGraph operates on shared state over a Graph

• Nodes read and write to the state

• Edges define the control flow between the nodes

• Some edges can be conditional (to enable branching workflows)

• LangGraph has built-in tooling to create agents \`create_agent\`

## Page 77

CS329Z: Engineering AI Agents

Recap

…

• Workflows compose model calls, tools, and 
program logic into a larger AI system.

• Frameworks expose different abstractions: 
DSPy uses signatures and modules; 
LangGraph uses state, nodes, and edges.

• We design the control flow and choose 
where the model makes decisions.

• Improvement requires data and evaluation. 
DSPy makes this explicit through optimizers.

## Page 78

CS329Z: Engineering AI Agents

Open Source Agent Harnesses

“Engineer” Agents?
Workflows
Agent Harnesses
Orchestration
Best Practices

## Page 79

CS329Z: Engineering AI Agents

Framework Landscape

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

OpenAI API

Anthropic API

…
…
…

Reliability: 
…
Observability: 
…
,
,
,

## Page 80

CS329Z: Engineering AI Agents

What is an Agent Harness?

Image Credit: CS329Z Lecture 1 
Introduction — What Are Agentic Systems?

## Page 81

CS329Z: Engineering AI Agents

What differentiates Agent Harnesses?

• Building an agent involves design choices: tools, memory, context 
management, and execution.

• Different harnesses make different tradeoffs to suit their tasks and operating 
environments.

• A good harness balances task success, cost, latency, and user control. The right 
balance depends on the use case.

## Page 82

CS329Z: Engineering AI Agents

Mini SWE-Agent

• Does not have any tools other than bash

• Has a completely linear history — every step of the agent just appends to the 
messages and that's it.

• Executes actions with subprocess.run — every action is completely 
independent (as opposed to keeping a stateful shell session running)

## Page 83

CS329Z: Engineering AI Agents

Open Hands

• Stores every step as an event — one JSON file per event on disk, and the 
messages sent to the model are rebuilt from them each step.

• Keeps a persistent terminal — a tmux session, so cd, environment variables and 
virtualenvs carry over between commands

• Stops itself when it is stuck — a detector ends the run after 4 repeats of the 
same action and result.

## Page 84

CS329Z: Engineering AI Agents

Pi Agent

• Has only four tools — read, write, edit, and bash, with a system prompt under 
1,000 tokens.

• No permission system — it runs with whatever permissions you launched with.

• Stores history as a tree, not a list — you can go back to an earlier message and 
branch from there

• Deliberately Simple — there is no plan mode and no sub-agent tool

## Page 85

CS329Z: Engineering AI Agents

Open Claw

• Wakes itself up every 30 minutes — a heartbeat turn runs on a schedule, and 
the agent replies NO_REPLY to stay silent.

• Runs as one long-lived Gateway — a single process owns all the chat channels.

• Builds its identity from Markdown files — AGENTS.md, SOUL.md, 
IDENTITY.md, USER.md and MEMORY.md are injected into the system prompt

• Stores memories every night — at 3 AM a background job reads through the 
day's notes and moves the parts worth keeping into MEMORY.md

## Page 86

CS329Z: Engineering AI Agents

The Harness can make a big difference

Image Credit: https://arena.ai/blog/coding-agents-harness-tax

### Page links

- [Link 1](../readings/arena-ai-harnesstax-how-much-does-the-harness-matter-for-coding-agents-arena-blog-2026.md)

## Page 87

CS329Z: Engineering AI Agents

Meta-Harness

Image Credit: https://arxiv.org/pdf/2603.28052

## Page 88

CS329Z: Engineering AI Agents

Meta-Harness

Image Credit: https://arxiv.org/pdf/2603.28052

## Page 89

CS329Z: Engineering AI Agents

Bringing it together

• There is no one way to build an agent.

• In this course you will be experimenting with all of these design decisions.

• Perhaps you can build the next popular agent harness :D

## Page 90

CS329Z: Engineering AI Agents

Orchestration and Telemetry

“Engineer” Agents?
Workflows
Agent Harnesses
Orchestration
Best Practices

## Page 91

CS329Z: Engineering AI Agents

Framework Landscape

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

OpenAI API

Anthropic API

…
…
…

Reliability: 
…
Observability: 
…
,
,
,

## Page 92

CS329Z: Engineering AI Agents

Why is orchestration/telemetry needed?

Image Credit: https://metr.org/time-horizons/

### Page links

- [Link 1](https://metr.org/time-horizons/)

## Page 93

CS329Z: Engineering AI Agents

Why is orchestration/telemetry needed?

• Agents run for long periods of time (although previous slides was “human-
time”), and the infra supporting them must be reliable.

• It is useful to have logs and observability tools for debugging.

• These are hard taught lessons from good software engineering practices that 
transfer over to agents.

## Page 94

CS329Z: Engineering AI Agents

## Page 95

CS329Z: Engineering AI Agents

Temporal Execution Model

Your Code (Client)

Activities are functional units that can fail.

## Page 96

CS329Z: Engineering AI Agents

Temporal Execution Model

Your Code (Client)

Activities are functional units that can fail.

Workflows link activities together.

## Page 97

CS329Z: Engineering AI Agents

Temporal Execution Model

Your Code (Client)
Server

Activities are functional units that can fail.

Workflows link activities together.

Activity 
Workers

Workflow

Workers
Workers

## Page 98

CS329Z: Engineering AI Agents

Temporal Execution Model

Your Code (Client)
Server

Activities are functional units that can fail.

Workflows link activities together.

Execution

History &

State

Storage

Activity Queue

Workflow Queue

Task Queue

Activity 
Workers

Workflow

Workers
Workers

## Page 99

CS329Z: Engineering AI Agents

Live Programming Demo

## Page 100

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Durable Workflows

## Page 101

CS329Z: Engineering AI Agents

Making a Durable Workflow: Activities

This is a backup slide in case we cannot do the live demo.

## Page 102

CS329Z: Engineering AI Agents

Making a Durable Workflow: Workflow

This is a backup slide in case we cannot do the live demo.

## Page 103

CS329Z: Engineering AI Agents

Making a Durable Workflow: Worker

This is a backup slide in case we cannot do the live demo.

## Page 104

CS329Z: Engineering AI Agents

Making a Durable Workflow: Run it

This is a backup slide in case we cannot do the live demo.

## Page 105

CS329Z: Engineering AI Agents

Making a Durable Workflow

This is a backup slide in case we cannot do the live demo.

## Page 106

CS329Z: Engineering AI Agents

Making a Durable Workflow

This is a backup slide in case we cannot do the live demo.

## Page 107

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Retries

## Page 108

CS329Z: Engineering AI Agents

Retrying Flaky Activities

This is a backup slide in case we cannot do the live demo.

## Page 109

CS329Z: Engineering AI Agents

Retrying Flaky Activities

This is a backup slide in case we cannot do the live demo.

## Page 110

CS329Z: Engineering AI Agents

Retrying Flaky Activities

This is a backup slide in case we cannot do the live demo.

## Page 111

CS329Z: Engineering AI Agents

Retrying Flaky Activities

This is a backup slide in case we cannot do the live demo.

## Page 112

CS329Z: Engineering AI Agents
This is a backup slide in case we cannot do the live demo.

Server Based Orchestration

## Page 113

CS329Z: Engineering AI Agents

Server Based Timing

This is a backup slide in case we cannot do the live demo.

## Page 114

CS329Z: Engineering AI Agents

Server Based Timing

This is a backup slide in case we cannot do the live demo.

## Page 115

CS329Z: Engineering AI Agents

Server Based Timing

This is a backup slide in case we cannot do the live demo.

## Page 116

CS329Z: Engineering AI Agents

Server Based Timing

This is a backup slide in case we cannot do the live demo.

## Page 117

CS329Z: Engineering AI Agents

Server Based Timing

This is a backup slide in case we cannot do the live demo.

## Page 118

CS329Z: Engineering AI Agents

Additional Observability Frameworks

## Page 119

CS329Z: Engineering AI Agents

MLFlow

Image Credit: https://notebooks.databricks.com/devrel/mlflow/2024-11-27-dspy.html

## Page 120

CS329Z: Engineering AI Agents

LangSmith

Image Credit: https://www.langchain.com/blog/announcing-langsmith

### Page links

- [Link 1](https://www.langchain.com/blog/announcing-langsmith)

## Page 121

CS329Z: Engineering AI Agents

LangFuse

Image Credit: https://langfuse.com/

### Page links

- [Link 1](https://langfuse.com/)

## Page 122

CS329Z: Engineering AI Agents

Recap

• Orchestration keeps agents reliable

• Observability enables debugging and monitoring

• Pulling best practices and tools from software engineering will carry over into 
agent engineering as well.

• Setting up evals, monitoring, durable execution, etc. is what separates building 
agents from engineering agents.

## Page 123

CS329Z: Engineering AI Agents

Best Practices and Challenges

“Engineer” Agents?
Workflows
Agent Harnesses
Orchestration
Best Practices

## Page 124

CS329Z: Engineering AI Agents

Keep it Simple

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

• You might not always need to build an agent.  Sometimes a workflow is right for 
the task.

• When you do build an agent think carefully about what tools you should 
include.

• If you have a lot of data you may even be able to optimize a model end to end.

## Page 125

CS329Z: Engineering AI Agents

Make Failures Observable and Recoverable

…

• Trace model calls, tool calls, state changes, 
and errors.

• Set timeouts, retry limits, and execution 
budgets.

• Log outputs and diagnose failures.

• Monitor the state of your system.

You can raise the error to the agent to try again.

## Page 126

CS329Z: Engineering AI Agents

Example: Shepherd

Image Credit: https://arxiv.org/pdf/2605.10913

### Page links

- [Link 1](https://arxiv.org/pdf/2605.10913)

## Page 127

CS329Z: Engineering AI Agents

Run Evaluations

• The best way to make design decisions is to ground 
them in evals.

• Evaluations enable optimization

• Building a proper eval is one of the most important 
steps when making an AI system.

• Choose your metrics wisely (accuracy, cost, latency, 
etc.)

• Test representative tasks, edge cases, and failure 
scenarios.

## Page 128

CS329Z: Engineering AI Agents

Run Evaluations

Your Custom 
Domain Eval!

… Unless you are building a general coding agent harness or 
testing a general agent system improvement, the standard 
coding benchmarks are NOT what you should climb on.

## Page 129

CS329Z: Engineering AI Agents

Challenges / Limitations

Image Credit: https://hamel.dev/blog/posts/prompt/

• Abstractions lift you further from the 
underlying system details, so ensure you 
know what is going on under the hood.

• When building a complex AI system it can be 
challenging to identify where the failures 
come from.  Make sure to look at the traces!

• Building on top of frameworks adds 
dependencies and reliance on external 
libraries to be maintained.

## Page 130

CS329Z: Engineering AI Agents

Recap

• Engineer Agents by Building -> Running -> Evaluating -> Improving.  The 
engineering process is a cycle!

• Start simple and justify added complexity.

• Design for failure and recovery.

• Use evidence and evaluation to assess quality, cost, and latency.

• Fully understand how your system works.

## Page 131

CS329Z: Engineering AI Agents

Summary

“Engineer” Agents?
Workflows
Agent Harnesses
Orchestration
Best Practices

## Page 132

CS329Z: Engineering AI Agents

Summary

• What does it mean to “Engineer” Agents?

• Frameworks for Workflows and Programs (DSPy, LangGraph)

• Open Source Agent Harnesses

• Orchestration and Telemetry (Temporal)

• Best Practices and Challenges
