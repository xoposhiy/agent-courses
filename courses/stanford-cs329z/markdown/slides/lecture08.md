# Lecture 8: Multi-Agent Systems

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture08.pdf) · [Raw file](../../raw/slides/lecture08.pdf)

Retrieved: 2026-11-13T16:28:50.012697+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Multi-Agent Systems

Diyi Yang, Michael Ryan, John Yang

CS329Z: Engineering AI Agents

## Page 2

CS329Z: Engineering AI Agents

Announcements

• Next Monday Guest Lecture!

• Homework 1 is due next Friday!

• We will release proposal feedback in the next few days.

Ryan Marten
Alex Shaw

## Page 3

CS329Z: Engineering AI Agents

## Page 4

CS329Z: Engineering AI Agents

Multi Agent Systems (MAS) are 
emergent work, making headlines.

Today we will break down what we

know about how to build MAS.

## Page 5

CS329Z: Engineering AI Agents

Learning Objectives

• Differentiate single and multi-agent systems.

• Identify multi-agent orchestration, communication, and coordination 
patterns

• Compare failure modes of multi-agent systems.

## Page 6

CS329Z: Engineering AI Agents

Lecture Overview

• Single vs Multi-Agent Systems (MAS) (10 minutes)

• MAS Orchestration Patterns (5 minutes)

• Communication (20 minutes)

• Coordination Infrastructure and Patterns (20 minutes)

• Failures and Challenges (15 minutes)

• \[Optional\] Case Study (10 minutes)

## Page 7

CS329Z: Engineering AI Agents

Single vs Multi-Agent Systems

SAS vs MAS
Orchestration
Communication
Failure Modes
Coordination

## Page 8

CS329Z: Engineering AI Agents

System Complexity

Model
Workflow or 
Compound AI System

Agent

## Page 9

CS329Z: Engineering AI Agents

System Complexity

Model
Workflow or 
Compound AI System

Multi Agent

System
Agent

Simple
Complex

GPT 6.1 Sol
Ex)

Triage Bug
Ex)

Implement Feature
Ex)

Maintain Repo

Ex)

## Page 10

CS329Z: Engineering AI Agents

What is a Multi-Agent System?

• A collection of multiple agents 
oriented to solve a shared task.

• When designing a MAS, one must 
consider:

• Orchestration

• Communication

• Coordination (Workspace/
tasks/shared context & 
memory)

## Page 11

CS329Z: Engineering AI Agents

Benefits of Multi Agent Systems

• Parallel execution: Work on separable 
subtasks concurrently.

• Specialization: Tailor instructions, models, 
and tools to particular responsibilities.

• Focused context: Give each agent the 
information relevant to its task.

• Broader exploration: Investigate different 
sources, hypotheses, or solution 
approaches.

Multiple agents provide more ways to distribute work, information, and responsibility.

## Page 12

CS329Z: Engineering AI Agents

Drawbacks of Multi Agent Systems

• Coordination overhead: Delegation, messaging, 
and integration consume time and tokens.

• Information loss: Handoffs can omit context 
that another agent needs.

• Conflicting actions: Agents can duplicate work, 
violate commitments, or overwrite changes.

• Error propagation: One agent’s mistake can 
mislead others.

• Engineering complexity: More roles, prompts, 
interfaces, and interactions to maintain/debug.

Collaboration helps when its benefits outweigh the coordination costs.

## Page 13

CS329Z: Engineering AI Agents

Sometimes Single Agent Systems Outperform

Towards a Science of Scaling Agent Systems \[Kim et al., 2026\]

Image Credit: https://arxiv.org/pdf/2512.08296

### Page links

- [Link 1](../readings/arxiv-2512-08296.md)

## Page 14

CS329Z: Engineering AI Agents

When to use SAS vs MAS

Prefer a Single Agent System when…
Try a Multi Agent System when…

• Steps are highly dependent on one 
another.

• Work is tightly coupled to a shared 
state (lots of overlap).

• One agent already meets the quality, 
cost, and latency goals.

• Subtasks can progress with limited 
synchronization.

• Information can be divided into focused 
contexts.

• Agents can own separate contributions 
and integrate them.

• Parallel work, specialization, or separate 
review addresses a measured bottleneck.

Recommendation: Start with a strong single-agent baseline. Add agents for a 
purpose and measure if contribution benefit outweighs coordination costs.

## Page 15

CS329Z: Engineering AI Agents

Comparison

## Page 16

CS329Z: Engineering AI Agents

MAS Orchestration Patterns

SAS vs MAS
Orchestration
Communication
Shared State
Failure Modes

## Page 17

CS329Z: Engineering AI Agents

Overview

• Independent: Only coordination between agents is an aggregator that reviews 
work from independent agents.

• Centralized (Orchestrator): One orchestrator communicates to all of the agents 
individually.

• Decentralized (Swarm): Each of the agents communicates with all other agents.

• Hybrid: Orchestrator and limited communication between peer agents.

## Page 18

CS329Z: Engineering AI Agents

Independent

• Agents work without exchanging intermediate messages.

• A final step combines or selects among their outputs.

• Tradeof: Enables parallel work, but agents cannot adjust their approach using 
one another’s intermediate findings.

Agent 2

Agent 3

Image Inspiration: https://www.anthropic.com/engineering/building-effective-agents

Agent 1

## Page 19

CS329Z: Engineering AI Agents

Centralized (Orchestrator)

• An orchestrator divides the task/assigns work to specialized agents.

• Workers return results, the orchestrator decides what happens next.

• Tradeof: Central oversight simplifies coordination, but the orchestrator can 
become a bottleneck.

Image Inspiration: https://www.anthropic.com/engineering/building-effective-agents

Orchestrator Agent

Worker Agent 1
Worker Agent 3

Worker Agent 2

## Page 20

CS329Z: Engineering AI Agents

Decentralized (Swarm)

• Agents can spawn subagents.

• All agents can communicate through a shared message board or communication 
channel (all-to-all communication).

• Good for large independent exploration and discovery at scale.

Image Inspiration: https://www.anthropic.com/engineering/building-effective-agents

Worker Agent 1
Worker Agent 3

Worker Agent 2

Shared State Tracking

## Page 21

CS329Z: Engineering AI Agents

Orchestrator Agent

Worker Agent 1
Worker Agent 3

Worker Agent 2

Hybrid

• An orchestrator manages the overall task and integrates results.

• Workers exchange information directly when their tasks require coordination.

• Combines global oversight with local flexibility, but requires clear rules for 
responsibilities and information sharing.

Image Inspiration: https://www.anthropic.com/engineering/building-effective-agents

Orchestrator Agent

Worker Agent 1
Worker Agent 3

Worker Agent 2

## Page 22

CS329Z: Engineering AI Agents

Comparison

Table Credit: https://arxiv.org/pdf/2512.08296

Towards a Science of Scaling Agent Systems \[Kim et al., 2026\]

### Page links

- [Link 1](../readings/arxiv-2512-08296.md)

## Page 23

CS329Z: Engineering AI Agents

The architecture to use depends on your task

Image Credit: https://arxiv.org/pdf/2512.08296

### Page links

- [Link 1](../readings/arxiv-2512-08296.md)

## Page 24

CS329Z: Engineering AI Agents

Multi-Agent architectures vary in cost

Image Credit: https://arxiv.org/pdf/2512.08296

Cost Structure: Single Agent < Orchestrated < Swarms

### Page links

- [Link 1](../readings/arxiv-2512-08296.md)

## Page 25

CS329Z: Engineering AI Agents

Dynamic Multi Agent Architecture

DyLAN \[Liu et al., 2023\]

Image Credit: https://arxiv.org/pdf/2310.02170

Run on several queries to determine “Agent Importance Scores” and assemble a task-
specific team.

### Page links

- [Link 1](https://arxiv.org/pdf/2310.02170)

## Page 26

CS329Z: Engineering AI Agents

Dynamic Multi Agent Architecture

DyLAN \[Liu et al., 2023\]

Image Credit: https://arxiv.org/pdf/2310.02170

• Run the agents in a forward pass

• Have them score each others 
responses for utility

• At the end back-propagate credit 
based on the agents that contributed 
to the agreed upon answer.

• Use this to select most influential/
important agents

### Page links

- [Link 1](https://arxiv.org/pdf/2310.02170)

## Page 27

CS329Z: Engineering AI Agents

Dynamic Multi Agent Architecture

DyLAN \[Liu et al., 2023\]

Image Credit: https://arxiv.org/pdf/2310.02170

• When running the team on new tasks 
use an LLM to score utility of each 
answer and dynamically drop agents 
from the team.

• Early stop when 2/3 of agents have a 
consistent answer.

### Page links

- [Link 1](https://arxiv.org/pdf/2310.02170)

## Page 28

CS329Z: Engineering AI Agents

Dynamic Multi Agent Architecture

DyLAN \[Liu et al., 2023\]

Image Credit: https://arxiv.org/pdf/2310.02170

Improved success rate in 
fewer API calls on Decision 
Making tasks.

### Page links

- [Link 1](https://arxiv.org/pdf/2310.02170)

## Page 29

CS329Z: Engineering AI Agents

Orchestration Pattern Summary

• Four core orchestration patterns:

• Independent: All agents work separately

• Centralized (Orchestrator): Orchestrator delegates

• Decentralized (Swarm): Agents pick up tasks and 
communicate directly to each other.

• Hybrid: Orchestrator delegates but worker agents 
can directly communicate.

• Also possible to build dynamic domain specific agent 
teams/architectures.

## Page 30

CS329Z: Engineering AI Agents

Communication

SAS vs MAS
Orchestration
Communication
Failure Modes
Coordination

## Page 31

CS329Z: Engineering AI Agents

Communication vs Coordination

• How the agents exchange 
information.

• Who receives which information, and 
through what channel?

• Message formats, protocols, and 
shared artifacts.

Communication
Coordination

• How the agents manage 
interdependent work.

• Who owns each task, and what must 
happen first?

• Assignments, dependencies, and 
conflict resolution.

## Page 32

CS329Z: Engineering AI Agents

Multi-Agent Communication as 
Conversations

AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations 
\[Wu et al., 2024\]

### Page links

- [Link 1](https://www.microsoft.com/en-us/research/wp-content/uploads/2023/08/LLM_agent.pdf)

## Page 33

CS329Z: Engineering AI Agents

AutoGen \[Wu et al., 2024\]

Image Credit: https://arxiv.org/pdf/2308.08155

Customize each agent and organize them into conversation patterns.

### Page links

- [Link 1](../readings/arxiv-2308-08155.md)

## Page 34

CS329Z: Engineering AI Agents

Example Conversation Patterns

Image Credit: https://arxiv.org/pdf/2308.08155

• Sequential: Agents communicate then handoff 
to the next team for the next step.

• Nested: Subagents communicate directly to 
managers.

• Group Chat: Shared context amongst agents in 
a group.

• Hierarchical Chat: All subagents communicate 
to orchestrator.

• Current patterns in AutoGen: 
RoundRobinGroupChat, SelectorGroupChat, 
Swarm, …

### Page links

- [Link 1](../readings/arxiv-2308-08155.md)

## Page 35

CS329Z: Engineering AI Agents

Image Credit: 
https://arxiv.org/
pdf/2308.08155

### Page links

- [Link 1](https://www.microsoft.com/en-us/research/wp-content/uploads/2023/08/LLM_agent.pdf)

## Page 36

CS329Z: Engineering AI Agents

Handoff vs Agent-as-tool

OpenAI Agents SDK

## Page 37

CS329Z: Engineering AI Agents

Handof

Image Credit: https://cellcog.ai/blog/agent-handoffs-vs-agents-as-tools/

• Control transfers: The receiving agent 
becomes active and continues the 
interaction.

• Context follows: Forward relevant 
conversation history and task details.

• Best fit: A specialist should interact directly 
with the user and own the next steps.

### Page links

- [Link 1](https://cellcog.ai/blog/agent-handoffs-vs-agents-as-tools/)

## Page 38

CS329Z: Engineering AI Agents

Agent-as-Tool

Image Credit: https://cellcog.ai/blog/agent-handoffs-vs-agents-as-tools/

• Caller retains control: It sends a specialist a bounded 
request and selected context.

• Result returns: The specialist contributes an answer or 
artifact, and the caller continues.

• Best fit: One agent should integrate specialist 
contributions and deliver the final response.

### Page links

- [Link 1](https://cellcog.ai/blog/agent-handoffs-vs-agents-as-tools/)

## Page 39

CS329Z: Engineering AI Agents

Handoff vs Agent-as-tool

Image Credit: Majid Sheikh | LinkedIn

### Page links

- [Link 1](https://www.linkedin.com/pulse/understanding-handoffs-vs-agents-as-tools-openais-agents-majid-sheikh-cvxgf/)

## Page 40

CS329Z: Engineering AI Agents

Message Board

MetaGPT \[Hong et al., 2024\] and Emergent Coordination

### Page links

- [Link 1](https://openreview.net/forum?id=VtmBAGCN7o)

## Page 41

CS329Z: Engineering AI Agents

MetaGPT \[Hong et al., 2024\]

Image Credit: https://openreview.net/pdf?id=VtmBAGCN7o

### Page links

- [Link 1](https://openreview.net/pdf?id=VtmBAGCN7o)

## Page 42

CS329Z: Engineering AI Agents

MetaGPT \[Hong et al., 2024\]

Image Credit: https://openreview.net/pdf?id=VtmBAGCN7o

### Page links

- [Link 1](https://openreview.net/pdf?id=VtmBAGCN7o)

## Page 43

CS329Z: Engineering AI Agents

HuggingFace Incident

Image Credit: https://metr.org/

### Page links

- [Link 1](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#core-takeaways-about-this-incident)

## Page 44

CS329Z: Engineering AI Agents

MoltBook

Image Credit: https://www.moltbook.com/post/e72d9de7-2bfd-4ce0-93b0-

f7af8ab7fb53

“Social Media” message board for agents.

### Page links

- [Link 1](https://www.moltbook.com/post/e72d9de7-2bfd-4ce0-93b0-f7af8ab7fb53)

## Page 45

CS329Z: Engineering AI Agents

Agent2Agent (A2A) Protocol

Google Agent2Agent Protocol

## Page 46

CS329Z: Engineering AI Agents

Agent2Agent Protocol

Image Credit: https://ai.plainenglish.io/
A2A is a protocol (like MCP) for communication between agents.

### Page links

- [Link 1](https://ai.plainenglish.io/a2a-protocol-complete-overview-95b792cc24d6?sk=ee6a54bff6a350e3b5c06cdab50880cf)

## Page 47

CS329Z: Engineering AI Agents

Agent Cards

Image Credit: https://codelabs.developers.google.com/

Agent Cards Describe 
the capabilities, skills, 
input/outputs, and 
other important 
details about a 
remote agent.

### Page links

- [Link 1](https://codelabs.developers.google.com/getting-started-mcp-a2a-adk?hl=en#0)

## Page 48

CS329Z: Engineering AI Agents

A2A Communication

Image Credit: https://codelabs.developers.google.com/

• The client requests the server agent card.

• The client dispatches requests to the 
server (which creates traceable tasks).

• The server pushes notifications about 
task progress to the client.

• The client and server can message back 
and forth as the server works.

• The server communicates back the 
completed task artifact to the client.

### Page links

- [Link 1](https://codelabs.developers.google.com/getting-started-mcp-a2a-adk?hl=en#0)

## Page 49

CS329Z: Engineering AI Agents

Communication Summary

• Possible Communication Channels:

• Main Conversation Thread (AutoGen)

• Handoff/Tool Call (OpenAI Agents SDK)

• Message Board (MetaGPT, OpenAI Swarm, 
MoltBook)

• Communication Protocol:

• Agent2Agent Protocol: Standardization for 
agent discovery, messaging, and artifact 
sharing.

## Page 50

CS329Z: Engineering AI Agents

Coordination Infrastructure and

Patterns

SAS vs MAS
Orchestration
Communication
Coordination
Failure Modes

## Page 51

CS329Z: Engineering AI Agents

Communication vs Coordination

• How the agents exchange 
information.

• Who receives which information, and 
through what channel?

• Message formats, protocols, and 
shared artifacts.

Communication
Coordination

• How the agents manage 
interdependent work.

• Who owns each task, and what must 
happen first?

• Assignments, dependencies, and 
conflict resolution.

## Page 52

CS329Z: Engineering AI Agents

Coordination

• Task Ledger: Tracking planning 
and execution progress.

• Shared Memory: Recall over 
prior experience.

• Worktree Isolation: Separation 
of workspace.

Infrastructure
Patterns

• Role Division: Assigning tasks

• Resource Division: Partitioning 
shared resources

• Negotiation: Discussing and 
agreeing on a plan.

## Page 53

CS329Z: Engineering AI Agents

Task Ledger

Magentic-One \[Fourney et al., 2024\] and Symphony

## Page 54

CS329Z: Engineering AI Agents

Task Ledger

• Track the task: Record the objective, 
current plan, and unresolved questions.

• Track execution: Record assignments, 
dependencies, progress, and blockers.

• Guide decisions: Use the current state to 
choose what runs next.

• Support recovery: Update the plan or 
retry work when execution stalls.

The task ledger maintains an explicit, updated account of the work to guide agent 
coordination.

## Page 55

CS329Z: Engineering AI Agents

Magentic-One  
\[Fourney et al., 2024\]

Orchestrator Agent 
maintains a Task Ledger 
keeping track of the plan and 
work to distribute to the 
worker agents.

Image Credit: https://arxiv.org/pdf/

2411.04468

### Page links

- [Link 1](https://arxiv.org/pdf/2411.04468)

## Page 56

CS329Z: Engineering AI Agents

Symphony

OpenAI: “Turning our 
issue tracker into an 
agent orchestrator”

Symphony monitors 
the issue tracker and 
dispatches eligible 
tasks to coding agents 
in separate 
workspaces.

## Page 57

CS329Z: Engineering AI Agents

Shared Memory Architecture

G-Memory \[Zhang et al., 2025\]

## Page 58

CS329Z: Engineering AI Agents

G-Memory \[Zhang et al., 2025\]

• Insight Graph: Abstracts Generalizable Insights from Experience 
• Query Graph: Encodes information about task queries and their relation 
• Interaction Graph: Exact logs amongst agents

Image Credit: https://arxiv.org/pdf/2506.07398

### Page links

- [Link 1](https://arxiv.org/pdf/2506.07398)

## Page 59

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2506.07398

• Insight Graph 
• Query Graph 
• Interaction Graph

G-Memory \[Zhang et al., 2025\]

Reflections

Episodic Task Index

Episodic Memory

### Page links

- [Link 1](https://arxiv.org/pdf/2506.07398)

## Page 60

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2506.07398 
Retrieve
Store
/

### Page links

- [Link 1](https://arxiv.org/pdf/2506.07398)

## Page 61

CS329Z: Engineering AI Agents
Image Credit: https://arxiv.org/pdf/2506.07398

G-Memory \[Zhang et al., 2025\]

Customized Multi-Agent Memory improves over single-agent-designed baselines.

### Page links

- [Link 1](https://arxiv.org/pdf/2506.07398)

## Page 62

CS329Z: Engineering AI Agents

Worktree Isolation

## Page 63

CS329Z: Engineering AI Agents

Worktree Isolation

• Problem: Agents editing the same 
working directory,

• Separate workspaces: Give each 
agent its own checkout and branch.

• Controlled integration: Merge 
completed contributions, resolve 
conflicts, and test the combined 
result.

• Tradeof: Isolation reduces 
interference during execution, but 
changes can diverge and create 
integration work.

Image Credit: https://medium.com/threadsafe/

### Page links

- [Link 1](https://medium.com/threadsafe/how-git-worktrees-improve-our-git-workflow-58f89171eb6b)

## Page 64

CS329Z: Engineering AI Agents

Emergent Coordination Patterns

CooperBench \[Khatua et al., 2026\]

## Page 65

CS329Z: Engineering AI Agents

Role Division \[Khatua et al., 2026\]
Agents agree on who handles which part of the task.

Image Credit: https://arxiv.org/pdf/2601.13295

Agent 1
Agent 2

### Page links

- [Link 1](https://arxiv.org/pdf/2601.13295)

## Page 66

CS329Z: Engineering AI Agents

Resource Division \[Khatua et al., 2026\]
Agents avoid collisions by partitioning shared resources.

Image Credit: https://arxiv.org/pdf/2601.13295

Agent 1
Agent 2

### Page links

- [Link 1](https://arxiv.org/pdf/2601.13295)

## Page 67

CS329Z: Engineering AI Agents

Negotiation \[Khatua et al., 2026\]
Agents resolve conflicting approaches by converging on a single plan.

Image Credit: https://arxiv.org/pdf/2601.13295

Agent 1
Agent 2

### Page links

- [Link 1](https://arxiv.org/pdf/2601.13295)

## Page 68

CS329Z: Engineering AI Agents

Coordination Summary

• Coordination Infrastructure

• Task Ledger: Space for tracking plan and execution.

• Shared Memory: Recalling prior experience of the 
full agent system.

• Worktree Isolation: Clean environment for each 
agent to work.

• Coordination Patterns:

• Role Division: Separation of tasks

• Resource Division: Separation of resources

• Negotiation: Planning to fulfill both parties interests.

## Page 69

CS329Z: Engineering AI Agents

Failures and Challenges

SAS vs MAS
Orchestration
Communication
Failure Modes
Coordination

## Page 70

CS329Z: Engineering AI Agents

Why Do Multi-Agent Systems Fail?

\[Cemri et al., 2025\]

## Page 71

CS329Z: Engineering AI Agents

Why Do Multi-Agent Systems Fail? \[Cemri et al., 2025\]

Image Credit: https://arxiv.org/pdf/2503.13657

Collect a lot of multi agent traces and organize their failures into a taxonomy.

### Page links

- [Link 1](../readings/arxiv-2503-13657.md)

## Page 72

CS329Z: Engineering AI Agents

Why Do Multi-Agent Systems Fail? \[Cemri et al., 2025\]

Image Credit: https://arxiv.org/pdf/2503.13657

### Page links

- [Link 1](../readings/arxiv-2503-13657.md)

## Page 73

CS329Z: Engineering AI Agents

The Curse of Coordination \[Khatua et al., 2026\]

## Page 74

CS329Z: Engineering AI Agents

CooperBench \[Khatua et al., 2026\]

600 collaborative coding tasks in 12 libraries across 4 programming languages.

Image Credit: https://arxiv.org/pdf/2601.13295

### Page links

- [Link 1](https://arxiv.org/pdf/2601.13295)

## Page 75

CS329Z: Engineering AI Agents

CooperBench \[Khatua et al., 2026\]

Image Credit: https://arxiv.org/pdf/2601.13295 
Single agent solving both tasks is better than coordinating two agents.

### Page links

- [Link 1](https://arxiv.org/pdf/2601.13295)

## Page 76

CS329Z: Engineering AI Agents

CooperBench \[Khatua et al., 2026\]

Image Credit: https://arxiv.org/pdf/2601.13295

### Page links

- [Link 1](https://arxiv.org/pdf/2601.13295)

## Page 77

CS329Z: Engineering AI Agents

Behavioral Problems

Patterns and Problems in Emerging Multi-Agent Systems \[Zou, 2026\]

### Page links

- [Link 1](https://www.anthropic.com/research/multiagent-systems)

## Page 78

CS329Z: Engineering AI Agents

Conformity \[Zou, 2026\]

“We asked a swarm of agents to work together and each individually create something 
impressive, over half of the agents decided to build either ray tracers or self-hosting compilers.”

Image Credit: https://arxiv.org/pdf/2510.01171

Image Credit: https://arxiv.org/pdf/2510.22954

### Page links

- [Link 1](https://arxiv.org/pdf/2510.01171)
- [Link 2](https://arxiv.org/pdf/2510.22954)

## Page 79

CS329Z: Engineering AI Agents

Incompatible Goals \[Zou, 2026\]

“Each model was tasked with 
migrating a Python backend 
on a fourth VM to another 
language. However, we gave 
each model a different target 
language for the migration.”

## Page 80

CS329Z: Engineering AI Agents

Incompatible Goals \[Zou, 2026\]

Image Credit: https://www.anthropic.com/research/multiagent-systems

When agents are 
given incompatible 
goals (e.g. deploy in 
python vs deploy in 
rust) they sometimes 
settle by force.

### Page links

- [Link 1](https://www.anthropic.com/research/multiagent-systems)

## Page 81

CS329Z: Engineering AI Agents

Incompatible Goals \[Zou, 2026\]

Image Credit: https://www.anthropic.com/research/multiagent-systems

When agents are 
given incompatible 
goals (e.g. deploy in 
python vs deploy in 
rust) they sometimes 
settle by force.

### Page links

- [Link 1](https://www.anthropic.com/research/multiagent-systems)

## Page 82

CS329Z: Engineering AI Agents

Failures Summary

• General Failures: System Design, Inter-
Agent, Verification.

• Coordination Failures: Expectation, 
Commitment, and Communication.

• Behavioral Failures: Lack of Diversity, 
Hostile conflict resolution.

## Page 83

CS329Z: Engineering AI Agents

Case Study

SAS vs MAS
Orchestration
Communication
Failure Modes
Coordination

If time permits

## Page 84

CS329Z: Engineering AI Agents

Engineering Swarm \[Carlini, 2026\]

Image Credit: https://www.anthropic.com/engineering/building-c-compiler

Companies are using Agent Swarms for Engineering and Science.  
Here is one look at how they may be operating these swarms.

### Page links

- [Link 1](https://www.anthropic.com/engineering/building-c-compiler)

## Page 85

CS329Z: Engineering AI Agents

Orchestration: Infinite Loop Decentralized Swarm

Image Credit: https://www.anthropic.com/engineering/building-c-compiler

### Page links

- [Link 1](https://www.anthropic.com/engineering/building-c-compiler)

## Page 86

CS329Z: Engineering AI Agents

Multiple Complementary Specialist Agents

Image Inspiration: https://www.anthropic.com/engineering/building-c-compiler

### Page links

- [Link 1](https://www.anthropic.com/engineering/building-c-compiler)

## Page 87

CS329Z: Engineering AI Agents

Coordination: Task folder synchronized on Git

Image Inspiration: https://www.anthropic.com/engineering/building-c-compiler

Inter-Agent Communication
Shared Memory

### Page links

- [Link 1](https://www.anthropic.com/engineering/building-c-compiler)

## Page 88

CS329Z: Engineering AI Agents

Coordination: Worktree Isolation

Image Inspiration: https://www.anthropic.com/engineering/building-c-compiler 
Git enables worktree isolation, and Agents select their own tasks.

Inter-Agent 
Communication
/Memory

### Page links

- [Link 1](https://www.anthropic.com/engineering/building-c-compiler)

## Page 89

CS329Z: Engineering AI Agents

Lessons Learned

• Strong tests guide autonomous work: Reliable correctness/
regression tests help agents recognize progress and catch 
breakages.

• Design for parallelism: Expose separable failures or subtasks.

• Make coordination explicit: Claim tasks, work in separate clones, 
and integrate contributions through Git.

• Preserve knowledge across sessions: Maintain shared 
documentation, progress notes, and records of failed approaches.

• Make feedback efficient: Provide concise error summaries, 
searchable logs, fast test subsets, and periodic progress updates.

• Assign complementary goals: Give agents distinct responsibilities.

## Page 90

CS329Z: Engineering AI Agents

Summary

SAS vs MAS
Orchestration
Communication
Failure Modes
Coordination

## Page 91

CS329Z: Engineering AI Agents

Summary

• Single vs Multi-Agent Systems (MAS)

• MAS Orchestration Patterns

• Communication

• Shared State

• Failures and Challenges

## Page 92

CS329Z: Engineering AI Agents

See you Wednesday for

Optimization!
