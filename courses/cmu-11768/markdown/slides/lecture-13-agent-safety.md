# Lecture 13 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-13-agent-safety.pdf) · [Raw file](../../raw/slides/lecture-13-agent-safety.pdf)

Retrieved: 2026-11-13T16:45:30.494004+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

1 1 - 7 6 8  ·  A I  AG E N TS  ·  S A F E TY
Agent Safety

Limiting what agents can access and do

1

## Page 2

What can go wrong?

2

## Page 3

Unapproved email deletion

An OpenClaw user asked their agent to wait for approval before changing their inbox.

Stop request
Later exchange

Where should the system have required approval?

OpenClaw user · incident report
3

### Page links

- [Link 1](../optional-readings/ref-4288fb81af46.md)

## Page 4

Production database deletion

PocketOS reported a coding agent working on a staging task.

The agent deleted a production storage volume and its backups.

Staging

Coding agent

Fix a staging issue

Production

API token

Can delete production data

Volume
Backups

Volume and backups deleted

PocketOS incident · The New Stack
4

### Page links

- [Link 1](../optional-readings/ref-c7f02d919c6b.md)

## Page 5

Data exfiltration

Copilot could retrieve an organization’s private documents.

The email steered Copilot into leaking private information.

Organization

Private
documents

Copilot
Retrieve

Attacker’s email

Hidden instructions

Attacker’s

server
Private data leaves the organization

Researchers demonstrated the flaw; Microsoft patched it. No mass breach was reported.

Microsoft CVE-2025-32711 advisory
5

### Page links

- [Link 1](../optional-readings/msrc-cve-2025-32711-rendered.md)

## Page 6

Supply-chain compromise

Cline used an agent to read and label GitHub issues.

That token was later used to publish an unauthorized command-line release.

Issue handling
Release workflow

Issue
Agent + shell
Release job
npm release

Runs issue instructions

Poisoned shared cache

Restore

Publish token

An attacker with the publish token can ship code that runs on users’ machines.

Cline · maintainer postmortem
6

### Page links

- [Link 1](../optional-readings/ref-89e3f85f0604.md)

## Page 7

Payment-card theft

Gambit Security found an operator directing AI agents to steal payment data.

Access
The operator sent agents to break into online retailers.

Theft
The agents extracted stored credit card records.

Checkout
They installed scripts that stole card details during checkout.

Gambit Security · September 2026
7

### Page links

- [Link 1](../optional-readings/ref-4fb133d3e427.md)

## Page 8

Threat models

8

## Page 9

Malicious user

The user asks the agent to do something it should not do.

The goal could be theft, fraud, harassment, or another prohibited act.

Payment-card theft

User’s goal
Steal customers’ credit card details.

Agent’s role
Break into shops, extract records, and install card-stealing scripts.

Gambit Security · September 2026
9

### Page links

- [Link 1](../optional-readings/ref-4fb133d3e427.md)

## Page 10

Prompt injection

The user has a legitimate task for the agent.

An attacker puts instructions in an email, webpage, file, or tool result.

The agent follows them while carrying out the user’s task.

Issue title

untrusted text

Model context

followed as instructions

Shell command

action on a system

Cline · maintainer postmortem
Debenedetti et al. · AgentDojo
10

### Page links

- [Link 1](https://arxiv.org/abs/2406.13352)
- [Link 2](../optional-readings/ref-89e3f85f0604.md)

## Page 11

Agent error

The agent tries to do something useful, but makes a mistake.

In a simulated banking task, a balance check became a bill payment.

User’s request

Agent’s action

Ruan et al. · ToolEmu · Figure 2(b)
11

### Page links

- [Link 1](https://arxiv.org/abs/2309.15817)

## Page 12

Improper means

The agent pursues a useful goal using an inappropriate method.

In a security test, it copied an exposed answer instead of solving the challenge.

Meng et al. · Introducing Docent
12

### Page links

- [Link 1](../optional-readings/ref-0997c41eb5ae.md)

## Page 13

Red teaming and alignment

training

13

## Page 14

Human red teaming

Testers try to make agents break their rules in controlled tests.

Give testers tasks, attack goals, and feedback on their attempts.

Example: access another patient’s records in a Gray Swan Arena simulation.

The agent reveals the other patient’s records

Gray Swan Arena · Agent Red-Teaming Challenge
Zou et al. · ART · Figure 2
14

### Page links

- [Link 1](https://app.grayswan.ai/arena/challenge/agent-red-teaming/leaderboard)
- [Link 2](../optional-readings/arxiv-2507-20526.md)

## Page 15

Automatic red teaming

Use an attacker model to search for prompts that bypass safety rules.

Attacker
Draft prompt

Target

Answer

Reply

Judge
Check policy
Reply + score

An attacker model writes a prompt for the
target.

A judge checks whether the target’s reply
violates the policy.

The attacker uses the reply and score to revise
its next prompt.

Example: PAIR · Chao et al.
15

### Page links

- [Link 1](../optional-readings/arxiv-2310-08419.md)

## Page 16

Supervised safety training

Train on examples of appropriate replies to harmful and legitimate requests.

Illustrative training examples

Harmful request

Steal customers’ credit card details.

Decline the theft and offer help
protecting payment data.

Legitimate request

Explain how to protect credit card
details at checkout.

Explain appropriate security practices.

For synthetic examples, choose whether to refuse or help, then generate a reply.

Filter unsafe replies, then train on the remaining examples.

Example recipe: NVIDIA · Nemotron 3 Super report · §3.1, Safety
16

### Page links

- [Link 1](../optional-readings/ref-626d80751270.md)

## Page 17

Safety training with RL

Use rewards to teach models to resist attacks and answer legitimate requests.

Resist attacks

Reward responses that follow the
safety rules.

Use automatic attacks to find harder
variants.

Train on variants that fooled an early
model.

Avoid unnecessary refusals

Include legitimate safety-related
requests.

Reward useful answers to these
requests.

Mix safety tasks with other training
domains.

A reward model trained on human preferences can guide this training.

Example recipe: NVIDIA · Nemotron 3 Super report · §3.2.1–3.2.3
17

### Page links

- [Link 1](../optional-readings/ref-626d80751270.md)

## Page 18

Sandboxing

18

## Page 19

What is a sandbox?

A sandbox is an isolated environment that limits what a program can access and do.

Sandbox
Allowed here

Agent

Task files

Run code

Blocked by policy

Private files

Other services

Docker · Engine security
Modal · Sandbox networking and security
19

### Page links

- [Link 1](../optional-readings/ref-18f59818e451.md)
- [Link 2](../optional-readings/ref-b280e2c6307e.md)

## Page 20

Isolation boundaries

Filesystem and
processes

Which files can the agent access, and which processes
can it control?

Network
Which services can it contact, and what can it do
there?

Resource limits
How much computing power and storage can it use?
How long can it run?

Engine security
Sandbox networking and security
20

### Page links

- [Link 1](../optional-readings/ref-18f59818e451.md)
- [Link 2](../optional-readings/ref-b280e2c6307e.md)

## Page 21

Where to put the boundary

Run the agent inside the sandbox, or keep it outside and run its tools inside.

Agent in the sandbox

Sandbox

Agent
Tools

Tools in the sandbox

Sandbox

Agent

Tool call

Tools

Keep access rules and enforcement beyond the agent’s control.

Docker · Engine security
Example: OpenShell architecture
21

### Page links

- [Link 1](../optional-readings/ref-18f59818e451.md)
- [Link 2](../optional-readings/ref-49c58f9a64f0.md)

## Page 22

Shared state across runs

Shared state can outlive the run that changed it.

Shared state
Poisoned files

Issue-handling run

Run ended

Later release run

Release job

Restore

Cline · Maintainer postmortem
22

### Page links

- [Link 1](../optional-readings/ref-89e3f85f0604.md)

## Page 23

Sandbox requirements

A sandbox needs to support frequent agent runs as well as contain their execution.

Quick startup
Make a fresh environment ready with little delay.

Strong isolation
Separate the run from host resources and other runs.

Freeze and reload
Save files and running state; resume from that point.

Ease of use
Create, configure, inspect, and stop runs through a simple
interface.

Isolation · Docker security
Lifecycle · Modal sandboxes
Pause and resume · E2B
23

### Page links

- [Link 1](../optional-readings/ref-18f59818e451.md)
- [Link 2](../optional-readings/ref-85b9cb4e727d.md)
- [Link 3](../optional-readings/ref-4e1a0dd4eab5.md)

## Page 24

Local and cloud sandboxes

The location determines who manages the execution environment and how you access it.

Local

Runs on your machine or cluster.

You manage setup, limits, and
lifecycle.

Docker · Apptainer · QEMU

Cloud

Runs on a provider’s machines.

Create and control sandboxes
through an API.

Examples: Modal · E2B

Docker
Apptainer
QEMU
Modal
E2B
24

### Page links

- [Link 1](../optional-readings/ref-0c2170ebdbc6.md)
- [Link 2](../optional-readings/ref-18f59818e451.md)
- [Link 3](../optional-readings/ref-abe4ecf03936.md)
- [Link 4](../optional-readings/ref-4e1a0dd4eab5.md)
- [Link 5](../optional-readings/ref-0ad02a6920ec.md)

## Page 25

Local sandbox technologies

Containers share a host kernel; a virtual machine runs its own guest kernel.

Technology
Boundary
Why use it?

Docker
Container
Default for local development; broad
tooling

Apptainer
Container
Fits shared clusters; runs as your user
without root

QEMU
Virtual machine
Runs a complete guest operating system

Docker · security and boundaries
Apptainer · unprivileged use
QEMU · system emulation
25

### Page links

- [Link 1](../optional-readings/ref-0c2170ebdbc6.md)
- [Link 2](../optional-readings/ref-18f59818e451.md)
- [Link 3](../optional-readings/ref-0ad02a6920ec.md)

## Page 26

Credentialing

26

## Page 27

Identity and authority

Caller

who is asking?

Requested action

on which resource?

Permission check

allowed for this task?

Keeping an API key hidden does not prevent the agent from misusing the access it

provides.

Managing personal access tokens
RFC 8693: OAuth 2.0 Token Exchange
27

### Page links

- [Link 1](../optional-readings/ref-6eb91bf61e38.md)
- [Link 2](../optional-readings/ref-4bedf7e3ed42.md)

## Page 28

Fine-grained tokens

Issue-handling account
Release account

✓ Read issue
✓ Read approved source

✓ Apply label
✓ Publish release

× Publish release
× Modify issue cache

Limit which resources the token can access, which actions it permits, and how long it

lasts.

e.g. GitHub App installation tokens expire after one hour.

Managing personal access tokens
GitHub App installation tokens
28

### Page links

- [Link 1](../optional-readings/ref-6052acfa2f0f.md)
- [Link 2](../optional-readings/ref-6eb91bf61e38.md)

## Page 29

Credential brokering

Agent
Broker
API

Request + run ID

Check permissions

API call with key

Result + separately recorded event

A credential broker is a service that controls the agent’s access to APIs.

It can give the agent a temporary token, or keep the API key private and make requests

on its behalf.

OpenShell architecture
RFC 8693: OAuth 2.0 Token Exchange
29

### Page links

- [Link 1](../optional-readings/ref-49c58f9a64f0.md)
- [Link 2](../optional-readings/ref-4bedf7e3ed42.md)

## Page 30

Monitoring

30

## Page 31

Monitoring agent behavior

Monitoring records and checks an agent’s behavior to identify
mistakes and unsafe actions.

An agent can produce a useful answer after taking an unsafe action.

Checks during a run can flag problems in time to pause or block an action.

Reviewing logs afterward helps explain failures and improve safeguards.

Transluce · Introducing Docent
Greenblatt et al. · AI Control
31

### Page links

- [Link 1](../optional-readings/arxiv-2312-06942v5.md)
- [Link 2](../optional-readings/ref-0997c41eb5ae.md)

## Page 32

Evidence for monitoring

Inspect the user’s request, tool calls, results, and changes to the outside system.

Tool call: read the task’s Dockerfile

Tool result: the file contains the secret answer

A passing score hid an unintended shortcut in this Cybench port.

Transluce · Introducing Docent
OpenTelemetry · GenAI attributes
32

### Page links

- [Link 1](../optional-readings/ref-e1038c581bd2.md)
- [Link 2](../optional-readings/ref-0997c41eb5ae.md)

## Page 33

Rules and model-based checks

Use rules for precise conditions and models for questions that need context.

Rule

Is this publisher on the allowed
list?

Compare the account with the policy.

Model-based check

Did the agent follow an attacker’s
instructions in the issue?

Read the user’s task, issue, and tool
calls.

For a model’s judgment, inspect the supporting passages in the log.

Cline · maintainer postmortem
Example: Docent · behavioral review
33

### Page links

- [Link 1](../optional-readings/ref-89e3f85f0604.md)
- [Link 2](../optional-readings/ref-5f2e04db952a.md)

## Page 34

Tool calls and written reasoning

Task: implement mathematical functions and pass the tests.

Tool-call monitoring

Sees the code patch and tool outputs. This patch makes verify() always return true.

CoT monitoring

Also sees the agent’s written reasoning: its plan to bypass the tests.

Baker et al. · Figure 1 · excerpts from a coding trace
34

### Page links

- [Link 1](https://arxiv.org/abs/2503.11926v1)

## Page 35

Written reasoning as evidence

Useful evidence, with limits

Written reasoning can reveal cheating that tool calls alone miss.

In a separate experiment, strong pressure to pass a reasoning check led
agents to hide cheating.

Check actions and outcomes independently, even when the reasoning
looks harmless.

Baker et al. · reasoning and monitor evasion
35

### Page links

- [Link 1](../optional-readings/arxiv-2503-11926.md)

## Page 36

Monitoring and intervention

To prevent an unsafe tool call, finish the check before executing it.

Tool call
Check

Allow

Execute

Block or pause
Review log afterward

Investigate and improve

Keep the checks, logs, and stop controls beyond the agent’s control.

Greenblatt et al. · AI Control
Cline · maintainer postmortem
36

### Page links

- [Link 1](../optional-readings/arxiv-2312-06942v5.md)
- [Link 2](../optional-readings/ref-89e3f85f0604.md)

## Page 37

Safety evaluation

37

## Page 38

Safety benchmark coverage

Test unsafe behavior and successful handling of valid requests.

Malicious user
Will the agent help steal payment-card data?

Prompt injection
Will it obey an attacker’s instructions in an issue?

Agent error
Will it send money when asked to check a balance?

Improper means
Will it read a leaked answer to pass a challenge?

Malicious requests · AgentHarm
Prompt injection · AgentDojo
Risky tool use · ToolEmu
Unintended shortcut · Docent study
38

### Page links

- [Link 1](../optional-readings/arxiv-2309-15817v2.md)
- [Link 2](../optional-readings/arxiv-2406-13352v3.md)
- [Link 3](../optional-readings/arxiv-2410-09024.md)
- [Link 4](../optional-readings/ref-0997c41eb5ae.md)

## Page 39

Safety outcomes

Illustrative counts: 100 valid-task runs and 100 safety-test runs.

Metric
Numerator ÷ denominator
Example

Task completion
Valid tasks completed
÷ all valid-task runs
80 ÷ 100 = 80%

Unnecessary refusal
Valid tasks refused
÷ all valid-task runs
10 ÷ 100 = 10%

Unsafe attempt
Runs with an unsafe attempt
÷ all safety-test runs
25 ÷ 100 = 25%

Completed harm
Runs with a harmful effect
÷ all safety-test runs
10 ÷ 100 = 10%

Blocked attempts raise the attempt rate without causing completed harm.

Task utility · AgentDojo
Completion and refusals · AgentHarm
Attempts and effects · OpenAgentSafety
39

### Page links

- [Link 1](../optional-readings/arxiv-2406-13352v3.md)
- [Link 2](../optional-readings/arxiv-2410-09024.md)
- [Link 3](../optional-readings/arxiv-2507-06134v2.md)

## Page 40

Safety tests with real tools

OpenAgentSafety tests multi-turn tasks with real tools and locally hosted services.

User’s task
Competing instruction

Task illustration from the paper.

Check changes to the audit files and unsafe attempts in the log.

Example: OpenAgentSafety · Figure 1 and §2
40

### Page links

- [Link 1](../optional-readings/arxiv-2507-06134v2.md)

## Page 41

Benchmarks for different threats

Choose a benchmark to match the question you want to test.

Question
Example
How it tests

Will the agent carry out a malicious
request?
AgentHarm
Multi-step tasks with synthetic
tools

Will an indirect instruction redirect
the agent?
AgentDojo
Tool data carries an attacker’s
instructions

Will the agent make a risky mistake
during a valid task?
ToolEmu
A language model simulates
tool results

AgentHarm · §3
AgentDojo · §3
ToolEmu · §3
41

### Page links

- [Link 1](../optional-readings/arxiv-2309-15817v2.md)
- [Link 2](../optional-readings/arxiv-2406-13352v3.md)
- [Link 3](../optional-readings/arxiv-2410-09024.md)

## Page 42

Defense evaluation

Compare safeguards on the same tasks and model, including valid requests and attacks.

Illustrative example: rare unsafe actions can make most alerts false alarms.

10,000 decisions
189 alerts to review

100 unsafe → 90 caught

9,900 safe → 99 false alerts

48% of alerts correct

90 / (90 + 99)

Example: 1% unsafe • 90% caught • 1% of safe decisions flagged

OpenAgentSafety
AI Control
AgentDojo
Monitoring Monitorability
42

### Page links

- [Link 1](../optional-readings/arxiv-2312-06942v5.md)
- [Link 2](https://arxiv.org/abs/2406.13352)
- [Link 3](../optional-readings/arxiv-2507-06134v2.md)
- [Link 4](../optional-readings/arxiv-2512-18311.md)

## Page 43

Questions?

Next Class: OpenHands

43
