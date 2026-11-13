# Final project

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/project.html) · [Raw file](../../raw/assignments/project.html)

Retrieved: 2026-11-13T16:40:50.487488+00:00

COMS 4995-15

# Introduction to Designing LLM Agents

[← Back to Course Home](../pages/index.md)

# Final Project

## Part 1: Proposal [5 points]

**Due:** Monday, November 16 @ 11:59 PM ET (submit on Gradescope)

## Overview

For the final project, you will work in groups of 3-4 to design and build an LLM agent that solves a specific, well-scoped problem.
Your proposal should describe the problem you want to solve and how your agent will be structured at a high level.

**Submit a 2-page PDF proposal document that clearly explains the agent you plan to build.** It should include the following:

### 1. Problem, motivation, and scope

Explain the problem your agent will solve and why it matters. State the intended user or user group. Define exactly what the agent will do.
Your project should be narrow enough to complete in one month.

### 2. High-level agent design

Describe, at a high level, how your agent will work. You do not need full implementation details yet,
but you should identify the major components your final system is expected to have, including:

- Data collection and parsing
- A memory store + retrieval mechanism
- At least 3 tools the agent can call
- Decision logic or system flow
- A front end with a chat interface and ways to track the agent's progress
- Guardrails or safety considerations

### 3. Implementation and evaluation plan

Briefly explain how you will tell whether the project succeeds. What kinds of tasks, examples, or failure cases will you test? What challenges do you anticipate running into and how will you address them? What weekly milestones will you set to track progress?

### Examples of Well-Scoped Projects

- A travel planning agent that plans a trip for a given destination, date range, budget, and set of preferences.
  The agent compares flights, hotels, and activities across external tools and builds an itinerary that respects constraints like opening hours and travel time.
  It revises the plan when a booking fails or a price changes, and asks for confirmation before any purchase.
- An apartment-shortlisting agent for someone renting in a specific city.
  The agent keeps a ranked, continuously updated list of apartments based on constraints like safety, commute time, and budget, and learns from feedback on past listings (like a user liking bright light or higher floors).
  It contacts landlords to schedule viewings and tracks replies across multiple threads.
- A species conservation agent that helps individuals support a variety of endangered species, such as sea turtles.
  The agent tracks the species' status and threats, recommends evidence-backed everyday actions (e.g., cutting single-use plastics near nesting beaches), and explains why they matter.
  It also plans fundraisers by contacting charities and organizing events, checking with the user before sending messages or spending money.

## Part 2: Final Project

**Due:** Monday, December 14 @ 11:59 PM ET (submit on Gradescope)

## Your Agent [40 points]

### Deliverables:

1. Code: A zip file containing your code, along with a README.md file that explains how to run your agent.
2. Design Document: A PDF writeup that clearly explains your agent implementation and design choices.

### Required Agent Components:

- **Data incorporation:** Your agent must incorporate external data relevant to the task. You should collect, parse, clean, and organize this data into a form your system can reliably use.
- **Memory and retrieval:** Your agent must maintain a memory store and have a retrieval mechanism over that memory or knowledge base. The system should be able to retrieve relevant information when needed.
- **Three tools:** Your agent must be able to call at least 3 meaningful tools. These tools should play a real functional role in solving the task, not exist only to satisfy the requirement.
- **Robust system design:** Your system should have a clear agentic workflow with explicit logic for how it processes inputs, routes decisions, uses memory, calls tools, and terminates. The design should be modular and understandable.
- **Front end:** Your agent must have an aesthetic and functional front end that users can interact with directly. It must include a chat interface, along with other ways to keep track of the agent's progress and state (e.g., viewing the trip plan so far, the current apartment shortlist, or a log of the agent's actions). The interface should be clear and polished enough that a new user could use your agent without any instructions.
- **Guardrails and exception handling:** Your system must include guardrails and handle failure at all stages of execution. You should show how the agent checks user inputs, constrains or verifies tool calls, and validates outputs before returning them.
- **Evaluation framework:** You must build an evaluation framework that tests whether your agent succeeds on intended tasks and how it behaves on edge cases, failures, and adversarial inputs.

### Design Document Requirements:

Your design document should clearly explain your full system and justify your design choices. The document should begin by defining the problem, intended user, motivation, and project scope. You should then provide an end-to-end description of the system, explaining how the agent moves from user input to final output. It should include a detailed discussion of each required agent component: data incorporation, memory and retrieval, three tools, robust system design, front end, guardrails, and evaluation.
For each component, explain what you implemented, why you designed it that way, and any important alternatives, tradeoffs, or limitations.

The document must also include two diagrams.
First, include a system flow graph showing the complete agent pipeline, including possible user inputs, major decision points, memory reads and writes, tool calls, guardrail checks, branches, and termination conditions.
Second, include a threat model that identifies plausible risks such as unsafe user input, prompt injection, unsafe tool use, privacy leakage, or harmful outputs, and clearly indicates where validation and guardrails are applied in the system.
These diagrams can be implemented in any format you choose, as long as all needed information is shown.

Finally, describe your evaluation methodology, including the kinds of tasks, success criteria, failure cases, and adversarial cases you test.
You must also include three user transcripts that show meaningfully different system behaviors, such as a successful case, a difficult or ambiguous case, and a failure-handling or safety case.

## Demo [40 points]

**You are able to use late days only for the deliverables. Your demo must be done on December 7th or 14th, in class.**

You will give a final presentation and live demonstration of your agent.
The total presentation time must be 20 minutes.
It should include a clear explanation of the problem, an overview of the full agent design, and a ~10 minute live demo showcasing your agent's abilities through its front end.

Your demo should provide evidence that the agent actually contains the required components.
At minimum, you should show how user input is processed, how data is incorporated, how memory and retrieval are used, how the system selects or calls tools, how guardrails intervene when needed, how the front end lets the user interact with the agent and track its progress, and what the final output looks like.
The live demo should make clear that the architecture is real and functioning as designed.

## Participation [15 points]

Your participation grade is based on an end-of-project participation survey completed by all team members.
The survey asks about how work and responsibilities were shared across the team.

## FAQ

What day will we present on?

In the interest of fairness, all teams should come prepared to present on December 7th.
We will use a random selection process to determine which groups will present that day at the very beginning of class.


How do late days work for the final project?

If you use late days on the final project or proposal, all team members must each use a late day.
If one team member has no late days left, their team cannot submit anything late.


What if we run into rate limits?

You have one month to complete this project, so you should plan your development process accordingly.
We expect teams to work around rate limits through good engineering practice: start early, test incrementally,
cache intermediate outputs where appropriate, and avoid leaving all large-scale experimentation or evaluation to the end.
In emergency cases, you may make additional accounts to reset your credit usage, but do not rely on this.


What model should we use?

You may use Gemini Flash or any other model available through
[OpenRouter](../references/openrouter.md).
Part of the project is making reasonable design decisions, so you should be able to justify
your model choice based on the needs of your agent.

Free models are sufficient. You may choose to use a paid model and cover the costs yourself,
but your agent should still work effectively with a free model.

[Download example code](../activities/openrouter-example.md)
showing how to call a model through OpenRouter and have it use a tool.
