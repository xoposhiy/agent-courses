# Lecture 14 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-14-openhands.pdf) · [Raw file](../../raw/slides/lecture-14-openhands.pdf)

Retrieved: 2026-11-13T16:45:31.827906+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

AG E N T I C  A I  |  L E CT U R E  1 4
OpenHands

Frameworks 1 · October 8, 2026

1

## Page 2

Simple Frontend Demo

2

## Page 3

Agent Canvas

OpenHands Agent Canvas · Live demo ↗
3

### Page links

- [Link 1](https://app.all-hands.dev/canvas)

## Page 4

History

4

## Page 5

Code completion

Through 2023

Copilot and early Cursor: code
suggestions

HumanEval: single functions,
unit tests

Human-led editing, execution,
and checking

A HumanEval-style task

Input: a function specification

Output: a function implementation

def has_close_elements(

numbers, threshold

):

"""Nearby number pairs"""

# Function completion

Chen et al. · HumanEval
GitHub Copilot · 2021
5

### Page links

- [Link 1](../optional-readings/arxiv-2107-03374.md)
- [Link 2](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)

## Page 6

Repository-level evaluation

October 2023 · SWE-bench

Real issue + repository snapshot

Patch + repository tests; difficult early results

Jimenez et al. · SWE-bench · Figure 1
6

### Page links

- [Link 1](../optional-readings/arxiv-2310-06770v1.md)

## Page 7

Devin

Cognition
Introducing Devin, the first AI software engineer
Introducing Devin, the first AI software engineer

Watch on

Cognition · Devin launch demo · March 12, 2024 ↗
7

### Page links

- [Link 1](https://www.youtube-nocookie.com/channel/UCk_Il3HoK3qTz1tvzyphozg)
- [Link 2](../videos/video-fjHtjT7GO1c.md)

## Page 8

OpenDevin

Frontend + agent + Docker sandbox · March 26, 2024

Junyang Lin · Original callout ↗
Graham Neubig · Early frontend ↗
8

### Page links

- [Link 1](../optional-readings/ref-6e55f120e19a.md)
- [Link 2](../optional-readings/ref-e2274cfcd6df.md)

## Page 9

Early coding agents

April 2024

SWE-agent

File search, code edits, fix
verification

May 2024

OpenDevin CodeAct 1.0

Code execution, terminal
commands, feedback

Agent–computer interfaces as a research topic

SWE-agent · April 2 release
CodeAct 1.0 · May 7 announcement
9

### Page links

- [Link 1](https://github.com/SWE-agent/SWE-agent)
- [Link 2](../optional-readings/ref-6f62ba16682a.md)

## Page 10

Benchmark progress

2025

Better models

Reasoning, code editing, tool use

Better agent systems

Tools, test environments, context,
recovery

Benchmark performance: model + agent system

Wang et al. · OpenHands Software Agent SDK · §5
10

### Page links

- [Link 1](../optional-readings/arxiv-2511-03690v1.md)

## Page 11

Deployment

2026

Longer runs, interruptions, parallel tasks

Progress visibility and result inspection

Repeatable workflows, scoped access, verification

OpenHands SDK
Neubig · Fujitsu talk · September 2026
11

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk)
- [Link 2](https://github.com/neubig/slides/tree/main/slides/2026-09-25-fujitsu-openhands-en)

## Page 12

The OpenHands
Software Agent SDK

12

## Page 13

Batteries included, but flexible

Ready-to-use agent

Models, tools, state, workspaces

Customizable components

Model choice, new tools,

instructions, deployment

Shared foundation for GUI, CLI, and integrations

OpenHands Software Agent SDK · Browse the examples ↗
13

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk)

## Page 14

Model and tools

Model choice

Terminal, editor, task
tracker

Reusable agent
configuration

llm = LLM(
    model=os.getenv("LLM_MODEL", "gpt-5.5"),
    api_key=os.getenv("LLM_API_KEY"),
)

agent = Agent(
    llm=llm,
    tools=\[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
        Tool(name=TaskTrackerTool.name),
    \],
)

Hello-world example · Browse the full source ↗
14

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/01_hello_world.py)

## Page 15

Conversation

Workspace: files and execution

Conversation: task, actions, observations

Run: action–observation loop

cwd = os.getcwd()
conversation = Conversation(agent=agent, workspace=cwd)

conversation.send_message(
    "3 project facts in FACTS.txt"
)
conversation.run()

Hello-world example · Browse the full source ↗
15

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/01_hello_world.py)

## Page 16

Custom tools

Action: typed input

Executor: search
implementation

Observation: model-
readable result

class GrepAction(Action):
    pattern: str = Field(
        description="Regex to search for"
    )
    path: str = Field(default=".")

class GrepObservation(Observation):
    matches: list\[str\] = Field(
        default_factory=list
    )

Custom grep tool · Browse the full source ↗
16

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/02_custom_tools.py)

## Page 17

Conversation persistence

Saved events and conversation state

Restoration: same ID and storage

Workspace persistence: a separate concern

conversation = Conversation(
    agent=agent,
    workspace=cwd,
    persistence_dir="./.conversations",
    conversation_id=conversation_id,
)

Persistence example · Browse the full source ↗
17

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/10_persistence.py)

## Page 18

Context management

Older events → summary

Original instructions + recent work

Potential detail loss; files and tests as evidence

condenser = LLMSummarizingCondenser(
    llm=llm.model_copy(update={"usage_id": "condenser"}),
    max_size=10,
    keep_first=2,
)
agent = Agent(llm=llm, tools=tools, condenser=condenser)

Context condenser · Browse the full source ↗
18

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/14_context_condenser.py)

## Page 19

Remote execution

Agent Server inside Docker

Same conversation API; remote task and events

with DockerWorkspace(
    server_image=server_image,
    platform=detect_platform(),
) as workspace:
    agent = get_default_agent(llm=llm, cli_mode=True)
    conversation = Conversation(agent=agent, workspace=workspace)
    conversation.send_message(
        "3 project facts in FACTS.txt"
    )
    conversation.run()

Docker workspace · Browse the full source ↗
19

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/02_remote_agent_server/02_convo_with_docker_sandboxed_server.py)

## Page 20

Action confirmation

Pause before action execution

Pending action → human decision

Rejection → revised plan

conversation.set_confirmation_policy(AlwaysConfirm())
conversation.send_message("Directory listing with ls -la")
conversation.run()

Confirmation example · Browse the full source ↗
20

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/04_confirmation_mode_example.py)

## Page 21

Single Agent vs.

Multi-agent

21

## Page 22

Specialized roles

Early multi-agent workflows: specialized roles

Manager
Issue plan

Reproducer
Bug reproduction

Fault localizer
Bug location

Editor
Code changes

Verifier
Fix verification

Chen et al. · CodeR · §2
Related: MetaGPT
22

### Page links

- [Link 1](../optional-readings/arxiv-2308-00352.md)
- [Link 2](../optional-readings/arxiv-2406-01304.md)

## Page 23

A single-agent baseline

One agent: reproduce, locate, edit, test

Shared context across activities

Separate roles: handoffs and maintenance

Additional agents for a clear purpose

Neubig · Don't Sleep on Single-agent Systems · 2024
23

### Page links

- [Link 1](../optional-readings/ref-42f1d27e513b.md)

## Page 24

General-purpose tools

A small tool set, many combinations

Edit files

Source, configuration,
documentation

Run commands

Search, dependencies,
tests

Browse

Documentation and
visual inspection

Neubig · Single-agent design · General action space
24

### Page links

- [Link 1](../optional-readings/ref-42f1d27e513b.md)

## Page 25

Skills

Additional instructions for the same agent

Project conventions and
recurring procedures

Relevant instructions on
demand

Earlier name: microagents

agent_context = AgentContext(
    skills=\[Skill(
        name="repo.md",
        content=repo_instructions,
        trigger=None,
    )\],
)
agent = Agent(
    llm=llm, tools=tools,
    agent_context=agent_context,
)

Skill activation example · Browse the full source ↗
25

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/03_activate_skill.py)

## Page 26

MCP tools

Model Context Protocol: external tool connections

Server-provided tool descriptions and execution

Built-in and external tools together

Server access and trust requirements

mcp_config = {
    "repomix": MCPServer(
        command="npx", args=\["-y", "repomix@1.4.2", "--mcp"\]
    ),
}
agent = Agent(llm=llm, tools=tools, mcp_config=mcp_config)

MCP integration example · Browse the full source ↗
26

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/07_mcp_integration.py)

## Page 27

Generalist problem solving

OpenHands-Versa: coding + visual browsing + search + file access

Shared tools across coding, research, and office work

Soni et al. · OpenHands-Versa · Figure 1
27

### Page links

- [Link 1](../optional-readings/arxiv-2506-03011v1.md)

## Page 28

Division of labor

Parallel work
Independent issues or repositories

Independent
review
Patch checking; separate task and permissions

Cost control
Cheaper models for suitable tasks

Task boundaries, shared context, coordination cost

SDK · Delegation example
Fujitsu talk · Pages 11, 13, 16
28

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/blob/69e26889401fe69157fff536e6a69049e6644cb3/examples/01_standalone_sdk/25_agent_delegation.py)
- [Link 2](https://github.com/neubig/slides/tree/main/slides/2026-09-25-fujitsu-openhands-en)

## Page 29

Agent Hosting

and Interface

29

## Page 30

Local and cloud execution

Local computer

Existing files, services, and context

Machine availability during

execution

Cloud workspace

Continued work with the laptop
off

Remote repository, dependencies,
credentials

SDK · Remote workspace examples
30

### Page links

- [Link 1](https://github.com/OpenHands/software-agent-sdk/tree/69e26889401fe69157fff536e6a69049e6644cb3/examples/02_remote_agent_server)

## Page 31

Interface choices

Execution location × interaction interface

Local execution
Cloud execution

IDE
Editor workspace
Remote workspace

GUI
Desktop application
Browser application

CLI
Local terminal
Remote session

Integration
Local service
Hosted worker

31

## Page 32

IDE

Familiar coding
workspace

Files, diffs, and tests
Task management and
review

Microsoft · VS Code with GitHub Copilot · Change review ↗
32

### Page links

- [Link 1](../optional-readings/ref-3f891021aedc.md)

## Page 33

Custom GUI

A workspace organized
around agent tasks

Progress and parallel
runs

Previews, diffs, and
approvals

Setup and workspace
management

OpenHands Agent Canvas · Revisit the opening demo ↗
33

### Page links

- [Link 1](https://app.all-hands.dev/canvas)

## Page 34

Human effort and oversight

20 regular copilot users · Python tasks · Copilot vs. OpenHands

Lower active effort; continued need for understanding and oversight

Chen et al. · Code with Me or for Me? · Figure 4
34

### Page links

- [Link 1](../optional-readings/arxiv-2507-08149v1.md)

## Page 35

CLI

A familiar interface
across environments

Local and remote
terminals

Shell commands and
scripts

Separate visual
previews

Anthropic · Claude Code · Terminal demo ↗
35

### Page links

- [Link 1](../optional-readings/ref-56b6b6b51040.md)

## Page 36

Integrations

Agents in existing work
channels

Issues: task context

PRs: diffs, tests,
review

Chat: requests and
results

GitHub · Copilot coding agent · PR review ↗
36

### Page links

- [Link 1](../optional-readings/ref-68c75debbb7b.md)

## Page 37

Automations for
Software Development

37

## Page 38

Automation dashboard

OpenHands OSS automation demo ↗
38

### Page links

- [Link 1](https://oss-agent-canvas.ngrok.dev/)

## Page 39

An automation run

Event → bounded task → inspectable result

Trigger

Issue, PR,

or schedule

→

Context

Repository,

instructions,

permissions

→

Run

Isolated

workspace

→

Artifact

Patch,

report,

or comment

→

Check

Person

or policy

Adapted from Neubig · Fujitsu talk · Page 8
39

### Page links

- [Link 1](https://github.com/neubig/slides/tree/main/slides/2026-09-25-fujitsu-openhands-en)

## Page 40

Automation demo

Existing issue-triage or PR-review run

Trigger and instructions

Repository and permissions

Input event → run → output

Output quality against the original task

OpenHands OSS automation demo ↗
40

### Page links

- [Link 1](https://oss-agent-canvas.ngrok.dev/)

## Page 41

Software factory

Recurring tasks, explicit handoffs, checks

Issue triage
Request and acceptance criteria

Implementation
Patch, tests, pull request

Code review
Independent verification

Merge check
Passing checks and approval on the current commit

Adapted from Fujitsu talk · Page 13
OpenHands · Software-factory example
41

### Page links

- [Link 1](../optional-readings/ref-c002ca076243.md)
- [Link 2](https://github.com/neubig/slides/tree/main/slides/2026-09-25-fujitsu-openhands-en)

## Page 42

Learning from past runs

Khatry et al. · SkillRefiner · Figure 1
42

### Page links

- [Link 1](../optional-readings/ref-eb2d1e8cfb37-pdf.md)

## Page 43

Skill refinement results

Held-out tasks · Accuracy (%) and PR-review F1

Higher scores than initial skills across both agent models

Khatry et al. · SkillRefiner · Table 1
43

### Page links

- [Link 1](../optional-readings/ref-eb2d1e8cfb37-pdf.md)

## Page 44

Questions?

Next Class: LangGraph

44
