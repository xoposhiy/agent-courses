# Lecture 1 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-01-agents.pdf) · [Raw file](../../raw/slides/lecture-01-agents.pdf)

Retrieved: 2026-11-13T16:45:25.981928+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

What Are Agents?
And How Do They Work?

From language modeling to systems that act in the world

Daniel Fried · Graham Neubig

11-768: AI Agents

1

## Page 2

0 1  ·  I n t ro

How capable are current agents?

Sixteen agents built a 100,000-line C compiler in two weeks—able to compile the Linux kernel.

Building a C compiler with a team of parallel Claudes · Carlini, Anthropic 2026 ↗
2

### Page links

- [Link 1](https://github.com/anthropics/claudes-c-compiler)
- [Link 2](https://www.anthropic.com/engineering/building-c-compiler)

## Page 3

0 1  ·  I n t ro

How capable are current agents?

Summer Yue (@summeryue0) · X, February 2026 ↗
3

### Page links

- [Link 1](../optional-readings/ref-4288fb81af46.md)

## Page 4

0 1  ·  I n t ro

How capable are current agents?

What should an agent be allowed to do autonomously?
Autonomous
Ask first
Never

Diagnose why the online store’s
checkout started failing

UNCLASSIFIED

Draft and send a product-launch
email to 50,000 customers

UNCLASSIFIED

Collect your tax forms, and prepare
and file your 2025 tax return

UNCLASSIFIED

Migrate a payments API from Python
to Rust without breaking mobile
checkout

UNCLASSIFIED

Buy concert tickets to my favorite
band if they set up a show in my area

UNCLASSIFIED

Adjust an insulin dose after a week of
glucose readings

UNCLASSIFIED

4

## Page 5

Jing Yu Koh · multimodal GUI-agent demo · 2024
5

## Page 6

OpenHands
OpenHands Visual Debugging
OpenHands Visual Debugging

Watch on

Graham Neubig · OpenHands visual debugging
6

### Page links

- [Link 1](https://www.youtube-nocookie.com/channel/UCHWq8J_nvQqugBTH19ILCEA)
- [Link 2](https://www.youtube.com/watch?v=jMyTCXpEz10)

## Page 7

0 1  ·  I n t ro

Meet the teaching team

Instructors

Daniel Fried
Graham Neubig

TAs

Aditya Soni
Andy Liu
Apurva Gandhi
Demi Wang

Jiarui Liu
Saujas Vaduguru
Weiwei Sun
Yueqi Song

Course contact: 11-768-fall-2026@lists.andrew.cmu.edu
7

### Page links

- [Link 1](https://adityasoni9998.github.io/)
- [Link 2](https://andyjliu.github.io/)
- [Link 3](https://apga.github.io/)
- [Link 4](https://d3mi.wang/)
- [Link 5](https://dpfried.github.io/)
- [Link 6](https://jiarui-liu.github.io/)
- [Link 7](https://saujasv.github.io/)
- [Link 8](https://sunnweiwei.github.io/)
- [Link 9](https://www.phontron.com/)
- [Link 10](https://yueqis.github.io/)
- [Link 11](mailto:11-768-fall-2026@lists.andrew.cmu.edu)

## Page 8

0 1  ·  I n t ro

Compute sponsors

Thanks to these sponsors for providing compute for the assignments and project!

8

### Page links

- [Link 1](https://fireworks.ai/)
- [Link 2](https://modal.com/)
- [Link 3](https://sail.computer/)
- [Link 4](https://www.primeintellect.ai/)

## Page 9

0 2  ·  Fo u n d at i o n s

What is an agent?

An agent is anything that can be viewed
as perceiving its environment through
sensors and acting upon that
environment through actuators.

Russell & Norvig, Artificial Intelligence: A Modern
Approach

Environment: a repository, website, application, or workflow

State/Observations: messages, file contents, webpages, screenshots, and tool results

Actions: replies, file edits, shell commands, API calls, and mouse or keyboard events

Reward: passing test cases, satisfying LLM-as-a-judge rubrics, positive user feedback

9

## Page 10

0 2  ·  Fo u n d at i o n s

Recap: language models

Next-token prediction

At each step, predict a distribution over the
next token.

Append the generated token to the prefix
and predict again.

Chain of thought

Generate intermediate reasoning tokens
before the answer.

Those tokens become context for later
predictions.

2 × (3 + 4)

prompt tokens

Prompt
Model
Reasoning tokens

14

answer tokens

Answer

10

## Page 11

0 2  ·  Fo u n d at i o n s

Tool definition

A typed interface
exposed to the
model.

Name and description

JSON Schema for
arguments

The chat template
renders it as text

Example after apply_chat_template

{
  "name": "read_file",

"description": "Read a UTF-8 file.",
  "parameters": {

"type": "object",

"properties": { "path": { "type": "string" } },
    "required": \["path"\]

}
}

<tools>
{"name":"read_file","description":"Read a UTF-8 file.",

"parameters":{"type":"object","properties":{"path":{"type":"string"}},

"required":\["path"\]}}
</tools>

11

## Page 12

0 2  ·  Fo u n d at i o n s

Tool calls and results

Tool call

After apply_chat_template

Tool result

After apply_chat_template

{"role":"assistant","tool_calls":\[{
  "id":"call_7",

"name":"read_file",
  "arguments":{"path":"test.py"}

}\]}

<tool_call>

{"name":"read_file","arguments":{"path":"test.py"}}

</tool_call>

{"role":"tool",

"tool_call_id":"call_7",

"name":"read_file",
 "content":"def add(a, b): …"}

<tool_response>
def add(a, b): …

</tool_response>

12

## Page 13

0 2  ·  Fo u n d at i o n s

From LLMs to agents: actions as tokens

Language model

A tool call is another token sequence the
model can predict.

The sequence names a tool and supplies its
arguments.

Harness

Parses, validates, and executes the call.

Returns the result as observation tokens.

Model
Reasoning

read_file

path: "test.py"

Tool call
Execute

def add(a, b): …

Observation

Toolformer · Schick et al., NeurIPS 2023 ↗
13

### Page links

- [Link 1](../readings/arxiv-2302-04761.md)

## Page 14

0 2  ·  Fo u n d at i o n s

An agent is a model in a loop

Context

Task

What does test.py contain?

Tool
read_file(path)

History

Model
Reasoning

read_file("test.py")

Call

Execute
def add(a, b): …

Result

send_message

to: user

“test.py defines add(a, b).”

Call

ReAct · Yao et al., ICLR 2023 ↗
14

### Page links

- [Link 1](../readings/arxiv-2210-03629.md)

## Page 15

A minimal ReAct loop

mini-swe-agent
Browse the full source:
Loop →
Templates →

Assignment 1: implement and extend a similar controller; create and call your own tools; apply it to software tasks.

def run(self, task: str = "", **kwargs) -> dict:
    self.messages = \[\]
    self.add_messages(
        self.model.format_message(role="system", content=self._render_template(self.config.system_template)),
        self.model.format_message(role="user", content=self._render_template(self.config.instance_template)),

)

while True:
        self.step()

def step(self) -> list\[dict\]:
    return self.execute_actions(self.query())

def query(self) -> dict:
    message = self.model.query(self.messages)
    self.add_messages(message)
    return message

def execute_actions(self, message: dict) -> list\[dict\]:
    """Execute actions in message, add observation messages, return them."""

15

### Page links

- [Link 1](https://github.com/SWE-agent/mini-swe-agent/blob/main/src/minisweagent/agents/default.py#L80-L146)
- [Link 2](https://github.com/SWE-agent/mini-swe-agent/blob/main/src/minisweagent/config/default.yaml#L1-L40)
- [Link 3](../readings/ref-f1872c8c002e.md)

## Page 16

0 2  ·  Fo u n d at i o n s

Example agent trajectory
swebench.com ↗

16

### Page links

- [Link 1](https://www.swebench.com/)

## Page 17

0 3  ·  AG E N T  C A PA B I L I T I E S

Agent capabilities

1. Accurate tool calling
2. Coherence over long context

3. Customizability
4. Complex task management

5. Environment understanding
6. Safety

17

## Page 18

0 3  ·  AG E N T  C A PA B I L I T I E S

Two ways to build these capabilities

LLM training

Change the model’s behavior through
pretraining, SFT, or RL.

Teach reusable patterns for reasoning, tool
use, and recovery.

Capabilities become part of the learned
policy.

Harness engineering

Change the system around the model:
prompts, tools, memory, and control flow.

Provide context, validation, retries, and
safety boundaries.

Capabilities emerge from the model–
harness combination.

→
+

Training
Model
Harness

18

## Page 19

0 3  ·  T RA I N I N G  ·  P R E T RA I N I N G  → S F T  → R L

How agent behavior is trained

01

Pretraining

Text, code, multimodal data
Broad representations and
regularities

02

Mid-training / SFT

Instructions, traces, tool calls
Formats and demonstrations

03

RL

Rewards or preferences
Trajectory-level behavior

19

## Page 20

0 3  ·  C A PA B I L I TY  1  /  6

Accurate tool calling

Harness engineering

Grammar-constrained decoding.

LLM training

SFT: train on tool-calling traces.

read_file

path: "test.py"

Select tool
Arguments
Validate
Execute

20

## Page 21

0 3  ·  C A PA B I L I TY  2  /  6

Coherence over long context

Harness engineering

Context compression/compaction.

Dynamic memory lookup.

Sub-agent delegation.

LLM training

SFT: long-context training.

History
Summary
Memory
Retrieval

21

## Page 22

0 3  ·  C A PA B I L I TY  3  /  6

Customizability

Harness engineering

Agent memory.

Skills.

Custom tools.

LLM training

RL: learning from user feedback.

Memory
Skills
Tools

22

## Page 23

0 3  ·  C A PA B I L I TY  4  /  6

Complex task management

Harness engineering

Provide planning/decomposition tools.

Sub-agent delegation.

LLM training

RL: train on complex, long-horizon tasks.

Plan
Delegate
Verify
Goal

23

## Page 24

0 3  ·  C A PA B I L I TY  5  /  6

Environment understanding

Harness engineering

Learn skills corresponding to domain
knowledge.

LLM training

SFT: train on data w/ expected observation
shape.

RL: train in domain-specific environments.

Interface
Observe
Act

24

## Page 25

0 3  ·  C A PA B I L I TY  6  /  6

Safety

Harness engineering

Sandboxing tools.

Limit access to credentials.

Monitor trajectories.

LLM training

RL: safety-aware RL.

Credential
Guardrail
Sandbox
Monitor

25

## Page 26

0 4  ·  AG E N T  E N G I N E E R I N G

Agents are systems, not just models

Sandbox

Harness
Inference

Model

Monitoring
Training

26

## Page 27

0 4  ·  AG E N T  E N G I N E E R I N G

Harness engineering

Shared functionality

Manage state, tools, memory, and control
flow

Validate actions and handle errors

Enforce permissions and safety boundaries

Example software:

Coding agents: CC, Codex, OpenHands,
OpenCode, Pi

Orchestrators: LangChain, CrewAI

Harness

Permissions
Memory
Tools
Control flow

27

## Page 28

0 4  ·  AG E N T  E N G I N E E R I N G

Sandbox

Shared functionality

Isolate code and tool execution

Limit compute, network, and filesystem
access

Create reproducible environments

Example software:

Docker / Apptainer

Modal / Sail

Execution
Isolation
Resources
Access

28

## Page 29

0 4  ·  AG E N T  E N G I N E E R I N G

LM inference

Shared functionality

Serve model generations reliably

Batch requests and reuse the KV cache

Manage streaming, parallelism, and
throughput

Example software:

vLLM

SGLang

the
next
…

Requests
Route
Compute
KV cache
Tokens

29

## Page 30

0 4  ·  AG E N T  E N G I N E E R I N G

Training systems

Shared functionality

Prepare data and collect rollouts

Coordinate distributed workers

Checkpoint, evaluate, and reproduce runs

Example software:

SkyRL

Miles

Rollouts
Workers
Rewards
Update

30

## Page 31

0 4  ·  AG E N T  E N G I N E E R I N G

Observability and monitoring

Shared functionality

Capture traces and metrics

Track quality, cost, and failures

Compare trajectories and evaluations

Example software:

Laminar

MLFlow

Traces
Inspect
Quality
Latency
Cost

31

## Page 32

0 5  ·  L E A R N I N G  O BJ E CT I V E S

What you should be able to do

1. Implement an agent from scratch on

top of an open-source LLM.

2. Design evaluations for multi-step

tasks.

3. Train agents to improve their

capabilities.

4. Reason about safety and reliability

tradeoffs.

5. Pursue an open research question in

agents.

Build

Evaluate
Train

Safety

Research

32

## Page 33

0 6  ·  A SS I G N M E N TS

Learn by building and measuring

A1 · Harness

TENTATIVE DUE: THU, SEP 10

Build the basic infrastructure and establish a reproducible baseline.

A2 · Evaluation

TENTATIVE DUE: THU, SEP 24

Measure behavior, report failure cases, and distinguish demos from
evidence.

A3 · Training

TENTATIVE DUE: THU, OCT 22

Train or adapt a component; analyze behavior, cost, and robustness.

Project

Integrate the ideas around a scoped task, environment, and
evaluation.

33

## Page 34

0 6  ·  S E M E ST E R  S C H E D U L E

Semester schedule

Aug 25 – Sep 8

Agent capabilities
what is an agent · tools · context · memory · planning

Sep 10 – Sep 15

Domains
coding · GUI

Sep 17 – Oct 1

Training + domains
SFT · RL basics · deep research · advanced RL

Oct 6 – Oct 22

Frameworks + safety
sandboxes · OpenHands · LangGraph

Fall break: Oct 12–16

Oct 27 – Nov 5

Interaction + projects
people · multi-agent · project hours

Nov 10 – Dec 3

Advanced topics + presentations
future of work · search · posters

Thanksgiving: Nov 25–27

34

## Page 35

0 7  ·  CO U RS E  P R E R E Q U I S I T E S

Before we begin: prerequisites

This course requires prior serious
experience training a language model.

We’ll share a link to a Google form on
Piazza. Submit the form by Thursday,
Aug 27 so that we can finalize
enrollment.

In the form, tell us about a university
course with an LM-training
assignment: the course, assignment
link, term, and grade.

If you lack the formal prerequisite,
explain comparable experience—such
as pre/post-training work or
published research training 4–7B+
language models.

We will enforce the prerequisite
strictly; students who cannot meet it
will be asked to drop the course.

35

## Page 36

0 7  ·  A SS I G N M E N T  P O L I C I E S  ·  CO U RS E  W O R K

How course work adds up

Assignments 1–3: 40% total,
completed individually.

Lecture highlights: 10% total,
completed individually; due within 24
hours after each lecture, starting
Thursday.

Research project: 50% total, in teams
of 2–3.

Proposal 5% · check-in 5% ·
presentation 10% · final report 30%.

Assignment descriptions and Canvas
provide the authoritative
requirements and deadlines.

Build

Evaluate
Train

Safety

Research

36

## Page 37

0 7  ·  A SS I G N M E N T  P O L I C I E S  ·  US I N G  AG E N TS

Using Agents in This Class?

We acknowledge that you use agents day-to-day, but we also want you to learn how to

build, evaluate, and reason about them yourself.

AI tools are generally permitted unless a specific assignment or project writeup says

otherwise.

Lecture highlights must be written by you, not generated by AI.

You are responsible for every submitted claim, citation, result, and line of code—and will

be quizzed on it.

37

## Page 38

0 7  ·  A SS I G N M E N T  P O L I C I E S  ·  D E A D L I N E S

Deadlines, submission, and slack

Assignments 1–3 each include two 24-
hour slack days.

Slack days are attached to each
assignment: they cannot be
transferred or shared.

After slack days are used, the penalty
is 5% of the assignment score per
additional day or part-day.

Project proposal and report each have
two slack days; the presentation has
none.

× 2

Due date
2 slack days
−5% / day

38

## Page 39

Thank you, Questions?

Next Class: Agent Capabilities 1 — Tool Use

39
