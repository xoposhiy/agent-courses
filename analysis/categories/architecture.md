# Architectural patterns

Reusable ways to arrange components, assign control, coordinate agents, and compose execution stages.

System structure and control flow belong here. Local prompting, context operations, and runtime recovery mechanisms have separate categories.

[All categories](README.md) · [CSV](architecture.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**18 concepts**: 18 confirmed in courses; 0 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Human oversight and approval](#concept-hitl) | pattern | 6 | 6 | 0 | COL, CMU, LC, S224, EVAL, CU | S329 | yes |
| [Parallel execution](#concept-parallelization) | pattern | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  |  |
| [Orchestrator and workers](#concept-orchestrator-workers) | pattern | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| [ReAct](#concept-react) | pattern | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| [Shared memory and task coordination](#concept-shared-memory) | pattern | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| [Plan then execute](#concept-plan-execute) | pattern | 4 | 4 | 0 | S329, COL, CMU, S224 |  | yes |
| [Routing](#concept-routing) | pattern | 4 | 4 | 0 | S329, COL, CMU, EVAL |  |  |
| [Agent as a tool](#concept-agent-as-tool) | pattern | 4 | 3 | 1 | S329, CMU, LC, CU |  |  |
| [CodeAct](#concept-codeact) | pattern | 3 | 3 | 0 | S329, CMU, LC |  |  |
| [Multi-agent debate](#concept-multi-agent-debate) | pattern | 3 | 2 | 1 | S329, CMU, CU |  | yes |
| [Asynchronous agent coordination](#concept-async-agents) | pattern | 2 | 2 | 0 | CMU, LC |  |  |
| [Prompt chaining](#concept-prompt-chain) | pattern | 2 | 2 | 0 | S329, COL |  |  |
| [Recursive and self-modifying agents](#concept-recursive-agents) | pattern | 2 | 2 | 0 | S329, LC |  | yes |
| [Agent handoffs](#concept-agent-handoff) | pattern | 1 | 1 | 0 | S329 |  |  |
| [Declarative task-oriented agent specifications](#concept-declarative-agents) | pattern | 1 | 1 | 0 | S224 |  |  |
| [Dynamic subagent creation and batch delegation](#concept-dynamic-delegation) | pattern | 1 | 1 | 0 | LC |  |  |
| [Evaluator and optimizer loop](#concept-critic-loop) | pattern | 1 | 1 | 0 | S329 |  | yes |
| [Workspace isolation](#concept-worktree-isolation) | pattern | 1 | 1 | 0 | S329 |  |  |

## Course codes

- **S329**: [Engineering AI Agents](../courses/stanford-cs329z.md)
- **COL**: [Designing LLM Agents](../courses/columbia-coms4995.md)
- **CMU**: [AI Agents](../courses/cmu-11768.md)
- **LC**: [Introduction to Deep Agents](../courses/langchain-deep-agents.md)
- **S224**: [Agentic AI](../courses/stanford-cs224v.md)
- **EVAL**: [Evaluating and Improving Agentic Applications](../courses/dlai-agentic-evals.md)
- **CU**: [Building AI Agents](../courses/colorado-csci7000.md)
- **BOOK**: [Agentic Large Language Models](../courses/agentic-large-language-models.md)

## Definitions and evidence

Entries follow frequency order. Related categories are navigation links; they do not create additional category membership or frequency.

<a id="concept-hitl"></a>

### Human oversight and approval

`hitl` · Human control · original type: pattern

Pause or route an agent decision to a person for review or approval.

**Aliases:** human-in-the-loop; HITL; human oversight.

**Also relevant to:** [Safety, security, and trust](safety-trust.md); [Agent behavior, human interaction, and interpretability](behavior.md).

**Evidence:** [S329, planned, line 83](../../courses/stanford-cs329z/markdown/pages/index.md); [COL, taught, p. 36](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 33](../../courses/cmu-11768/markdown/slides/lecture-05-planning.md); [LC, taught, line 40](../../courses/langchain-deep-agents/markdown/lessons/m1.8-hitl.md); [S224, taught, p. 5](../../courses/stanford-cs224v/markdown/slides/l-smt-match.md); [EVAL, taught, p. 33](../../courses/dlai-agentic-evals/markdown/slides/module-4.md); [CU, taught, p. 18](../../courses/colorado-csci7000/markdown/slides/w1l1.md); [BOOK, taught, line 603](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-parallelization"></a>

### Parallel execution

`parallelization` · Control flow and composition · original type: pattern

Run independent tasks at the same time and combine results.

**Aliases:** parallelization; parallelisation.

**Evidence:** [S329, taught, p. 15](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 24](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 50](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [LC, taught, line 43](../../courses/langchain-deep-agents/markdown/lessons/m4.2-building-a-subagent-team.md); [S224, taught, p. 20](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md).

<a id="concept-orchestrator-workers"></a>

### Orchestrator and workers

`orchestrator-workers` · Delegation and coordination · original type: pattern

Let a coordinator split work and assign subtasks to worker agents.

**Aliases:** orchestrator-workers; supervisor-worker.

**Evidence:** [S329, taught, p. 15](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [CMU, taught, p. 5](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [LC, taught, line 81](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md); [S224, taught, p. 19](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-00352.md); [BOOK, taught, line 132](../../courses/agentic-large-language-models/markdown/chapters/chapter-14-case-study-3-building-a-multi-agent-diagnosis-framework.md).

<a id="concept-react"></a>

### ReAct

`react` · Control flow and composition · original type: pattern

Alternate reasoning, tool actions, and observations.

**Aliases:** reasoning and acting.

**Also relevant to:** [Prompting, reasoning, and planning techniques](reasoning-techniques.md); [Tool-use and action techniques](tool-techniques.md).

**Evidence:** [S329, taught, p. 33](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 58](../../courses/columbia-coms4995/markdown/slides/week1.md); [CMU, taught, p. 15](../../courses/cmu-11768/markdown/slides/lecture-01-agents.md); [S224, taught, p. 33](../../courses/stanford-cs224v/markdown/slides/l-agentic.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2210-03629.md); [BOOK, taught, line 491](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-shared-memory"></a>

### Shared memory and task coordination

`shared-memory` · Delegation and coordination · original type: pattern

Coordinate agents through shared state, task records, or message stores.

**Related terms:** task ledger; message board.

**Also relevant to:** [Context and memory techniques](context-memory.md).

**Evidence:** [S329, taught, p. 52](../../courses/stanford-cs329z/markdown/slides/lecture08.md); [CMU, taught, p. 11](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [LC, taught, line 67](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md); [CU, assigned, p. 4](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-00352.md); [BOOK, taught, line 116](../../courses/agentic-large-language-models/markdown/chapters/chapter-14-case-study-3-building-a-multi-agent-diagnosis-framework.md).

<a id="concept-plan-execute"></a>

### Plan then execute

`plan-execute` · Control flow and composition · original type: pattern

Separate a planning stage from the execution of the planned steps.

**Aliases:** plan-and-execute; plan then execution.

**Also relevant to:** [Prompting, reasoning, and planning techniques](reasoning-techniques.md).

**Evidence:** [S329, taught, p. 47](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 58](../../courses/columbia-coms4995/markdown/slides/week6.md); [CMU, taught, p. 19](../../courses/cmu-11768/markdown/slides/lecture-05-planning.md); [S224, taught, p. 15](../../courses/stanford-cs224v/markdown/slides/l-data-driven-deep-research.md); [BOOK, taught, line 19](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-routing"></a>

### Routing

`routing` · Control flow and composition · original type: pattern

Choose a specialized path or component for an input.

**Aliases:** router pattern.

**Evidence:** [S329, taught, p. 15](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 47](../../courses/columbia-coms4995/markdown/slides/week6.md); [CMU, taught, p. 8](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [EVAL, taught, p. 62](../../courses/dlai-agentic-evals/markdown/slides/module-5.md).

<a id="concept-agent-as-tool"></a>

### Agent as a tool

`agent-as-tool` · Delegation and coordination · original type: pattern

Call a specialist agent as a tool while the caller keeps control.

**Aliases:** subagent as tool.

**Evidence:** [S329, taught, p. 36](../../courses/stanford-cs329z/markdown/slides/lecture08.md); [CMU, taught, p. 14](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [LC, taught, line 35](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md); [CU, assigned, p. 5](../../courses/colorado-csci7000/markdown/readings/arxiv-2407-16741.md).

<a id="concept-codeact"></a>

### CodeAct

`codeact` · Control flow and composition · original type: pattern

Use executable code as the agent action interface.

**Aliases:** code actions.

**Also relevant to:** [Tool-use and action techniques](tool-techniques.md).

**Evidence:** [S329, taught, p. 43](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [CMU, taught, p. 16](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [LC, taught, line 50](../../courses/langchain-deep-agents/markdown/lessons/m2.4-interpreter.md).

<a id="concept-multi-agent-debate"></a>

### Multi-agent debate

`multi-agent-debate` · Delegation and coordination · original type: pattern

Let several agents exchange arguments or critique candidate answers.

**Aliases:** agent debate.

**Also relevant to:** [Prompting, reasoning, and planning techniques](reasoning-techniques.md); [Agent behavior, human interaction, and interpretability](behavior.md).

**Evidence:** [S329, taught, p. 41](../../courses/stanford-cs329z/markdown/slides/lecture01.md); [CMU, taught, p. 9](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2305-14325.md); [BOOK, taught, line 210](../../courses/agentic-large-language-models/markdown/chapters/chapter-16-role-based-interaction-in-multi-llm-systems.md).

<a id="concept-async-agents"></a>

### Asynchronous agent coordination

`async-agents` · Delegation and coordination · original type: pattern

Run agents concurrently and coordinate completion, progress, and results.

**Aliases:** async subagents; asynchronous subagents.

**Evidence:** [CMU, taught, p. 16](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [LC, taught, line 44](../../courses/langchain-deep-agents/markdown/lessons/m5.4-async-subagents.md).

<a id="concept-prompt-chain"></a>

### Prompt chaining

`prompt-chain` · Control flow and composition · original type: pattern

Pass the output of one model step into the next step.

**Aliases:** prompt chain.

**Evidence:** [S329, taught, p. 15](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 27](../../courses/columbia-coms4995/markdown/slides/week6.md).

<a id="concept-recursive-agents"></a>

### Recursive and self-modifying agents

`recursive-agents` · Control flow and composition · original type: pattern

Use recursive agent calls or agent-directed changes to system behavior.

**Aliases:** recursive agents.

**Related terms:** hyperagents.

**Also relevant to:** [Prompting, reasoning, and planning techniques](reasoning-techniques.md).

**Evidence:** [S329, taught, p. 109](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [LC, taught, line 904](../../courses/langchain-deep-agents/markdown/lessons/m4.3-dynamic-subagents.md); [BOOK, taught, line 90](../../courses/agentic-large-language-models/markdown/chapters/chapter-20-advanced-transformer-and-agentic-architectures.md).

<a id="concept-agent-handoff"></a>

### Agent handoffs

`agent-handoff` · Delegation and coordination · original type: pattern

Transfer control and relevant information from one agent to another.

**Aliases:** handoff.

**Evidence:** [S329, taught, p. 36](../../courses/stanford-cs329z/markdown/slides/lecture08.md).

<a id="concept-declarative-agents"></a>

### Declarative task-oriented agent specifications

`declarative-agents` · Control flow and composition · original type: pattern

Define task fields, constraints, and policies and let a runtime manage the dialogue.

**Aliases:** task-oriented dialogue.

**Related terms:** Genie Worksheets.

**Evidence:** [S224, taught, p. 31](../../courses/stanford-cs224v/markdown/slides/l-newworksheet.md).

<a id="concept-dynamic-delegation"></a>

### Dynamic subagent creation and batch delegation

`dynamic-delegation` · Delegation and coordination · original type: pattern

Create or schedule subagents for a changing list of work items.

**Aliases:** dynamic subagents; batch subagents.

**Evidence:** [LC, taught, line 50](../../courses/langchain-deep-agents/markdown/lessons/m4.3-dynamic-subagents.md).

<a id="concept-critic-loop"></a>

### Evaluator and optimizer loop

`critic-loop` · Control flow and composition · original type: pattern

Use a separate evaluator to guide repeated improvement of an output.

**Aliases:** evaluator-optimizer; generator-critic.

**Also relevant to:** [Evaluation, research, and improvement](evaluation.md); [Prompting, reasoning, and planning techniques](reasoning-techniques.md).

**Evidence:** [S329, taught, p. 15](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [BOOK, taught, line 177](../../courses/agentic-large-language-models/markdown/chapters/chapter-16-role-based-interaction-in-multi-llm-systems.md).

<a id="concept-worktree-isolation"></a>

### Workspace isolation

`worktree-isolation` · Delegation and coordination · original type: pattern

Give agents separate working directories to prevent conflicting file changes.

**Aliases:** worktree isolation.

**Also relevant to:** [Runtime, deployment, and performance](runtime.md).

**Evidence:** [S329, taught, p. 52](../../courses/stanford-cs329z/markdown/slides/lecture08.md).
