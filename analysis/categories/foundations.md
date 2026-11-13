# Foundations and design concepts

Core concepts that explain models, agent components, and system design.

General concepts and input representations belong here; concrete component arrangements belong under architecture.

[All categories](README.md) · [CSV](foundations.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**16 concepts**: 13 confirmed in courses; 3 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Agent architecture](#concept-agent-architecture) | topic | 7 | 7 | 0 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| [Agent frameworks and orchestration](#concept-frameworks) | topic | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| [Agent harness design](#concept-harness) | topic | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| [Conversation and execution state](#concept-state) | concept | 5 | 5 | 0 | COL, CMU, LC, S224, CU |  | yes |
| [Long-context modeling](#concept-long-context) | topic | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  | yes |
| [Multi-agent systems](#concept-multi-agent) | topic | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| [Long-horizon agent tasks](#concept-long-horizon) | topic | 4 | 4 | 0 | COL, CMU, LC, S224 |  |  |
| [Workflows versus agents](#concept-workflow-agent) | concept | 4 | 4 | 0 | S329, COL, CMU, CU |  |  |
| [Transformer and attention](#concept-transformer) | concept | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| [Language model foundations](#concept-llm-foundations) | topic | 2 | 2 | 0 | S329, COL |  | yes |
| [Tokenization](#concept-tokenization) | method | 2 | 2 | 0 | COL, CMU |  | yes |
| [Vision-language models](#concept-vlm) | topic | 2 | 2 | 0 | CMU, S224 |  | yes |
| [World models](#concept-world-models) | concept | 1 | 1 | 0 | CMU |  | yes |
| [Belief-desire-intention agents](#concept-bdi) | concept | 0 | 0 | 0 |  |  | yes |
| [Language model scaling laws](#concept-scaling-laws) | concept | 0 | 0 | 0 |  |  | yes |
| [Vision-language-action models](#concept-vla) | topic | 0 | 0 | 0 |  |  | yes |

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

<a id="concept-agent-architecture"></a>

### Agent architecture

`agent-architecture` · Agent design · original type: topic

Combine a model, tools, memory, control flow, and an environment into an agent.

**Aliases:** agent anatomy; agent components.

**Evidence:** [S329, taught, p. 29](../../courses/stanford-cs329z/markdown/slides/lecture01.md); [COL, taught, p. 53](../../courses/columbia-coms4995/markdown/slides/week1.md); [CMU, taught, p. 1](../../courses/cmu-11768/markdown/slides/lecture-01-agents.md); [LC, taught, line 34](../../courses/langchain-deep-agents/markdown/lessons/m1.1-overview.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md); [EVAL, taught, p. 6](../../courses/dlai-agentic-evals/markdown/slides/module-1.md); [CU, taught, p. 21](../../courses/colorado-csci7000/markdown/slides/w1l1.md); [BOOK, taught, line 36](../../courses/agentic-large-language-models/markdown/chapters/chapter-01-introduction.md).

<a id="concept-frameworks"></a>

### Agent frameworks and orchestration

`frameworks` · Agent design · original type: topic

Use reusable components and control flow to build agent systems.

**Aliases:** agent orchestration; agent frameworks.

**Evidence:** [S329, taught, p. 4](../../courses/stanford-cs329z/markdown/slides/lecture05.md); [COL, taught, p. 37](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 1](../../courses/cmu-11768/markdown/slides/lecture-14-openhands.md); [LC, taught, line 25](../../courses/langchain-deep-agents/markdown/lessons/m1.2-running-a-deep-agent.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2407-16741.md); [BOOK, taught, line 128](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-harness"></a>

### Agent harness design

`harness` · Agent design · original type: topic

Design the runtime around a model, including tools, state, limits, and execution.

**Aliases:** agent scaffolds; agent scaffolding.

**Evidence:** [S329, taught, p. 80](../../courses/stanford-cs329z/markdown/slides/lecture05.md); [COL, taught, p. 16](../../courses/columbia-coms4995/markdown/slides/week6.md); [CMU, taught, p. 14](../../courses/cmu-11768/markdown/slides/lecture-14-openhands.md); [LC, taught, line 18](../../courses/langchain-deep-agents/markdown/lessons/m1.1-overview.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2610-14224v1.md); [BOOK, taught, line 64](../../courses/agentic-large-language-models/markdown/chapters/chapter-01-introduction.md).

<a id="concept-state"></a>

### Conversation and execution state

`state` · Agent design · original type: concept

Track messages, task progress, and runtime data across agent steps.

**Aliases:** agent state; conversation state.

**Also relevant to:** [Context and memory techniques](context-memory.md); [Runtime, deployment, and performance](runtime.md).

**Evidence:** [COL, taught, p. 20](../../courses/columbia-coms4995/markdown/slides/week6.md); [CMU, taught, p. 17](../../courses/cmu-11768/markdown/slides/lecture-14-openhands.md); [LC, taught, line 77](../../courses/langchain-deep-agents/markdown/lessons/m1.7-messages-threads-checkpointers.md); [S224, taught, p. 31](../../courses/stanford-cs224v/markdown/slides/l-newworksheet.md); [CU, taught, p. 19](../../courses/colorado-csci7000/markdown/slides/w1l1.md); [BOOK, taught, line 383](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-long-context"></a>

### Long-context modeling

`long-context` · Model fundamentals · original type: topic

Extend or manage model behavior on long input sequences.

**Aliases:** long context; context length extension.

**Evidence:** [S329, taught, p. 87](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, p. 35](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 11](../../courses/cmu-11768/markdown/slides/lecture-03-long-context.md); [LC, taught, line 799](../../courses/langchain-deep-agents/markdown/lessons/m4.3-dynamic-subagents.md); [S224, taught, p. 7](../../courses/stanford-cs224v/markdown/slides/i-sliders.md); [BOOK, taught, line 336](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-multi-agent"></a>

### Multi-agent systems

`multi-agent` · Agent design · original type: topic

Use several agents that interact to solve tasks.

**Aliases:** MAS; multiagent systems.

**Evidence:** [S329, taught, p. 10](../../courses/stanford-cs329z/markdown/slides/lecture08.md); [CMU, taught, p. 2](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [LC, taught, line 42](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md); [S224, taught, p. 20](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-08155.md); [BOOK, taught, line 26](../../courses/agentic-large-language-models/markdown/chapters/chapter-16-role-based-interaction-in-multi-llm-systems.md).

<a id="concept-long-horizon"></a>

### Long-horizon agent tasks

`long-horizon` · Agent design · original type: topic

Maintain progress over long sequences of dependent actions.

**Aliases:** long horizon tasks.

**Evidence:** [COL, taught, p. 3](../../courses/columbia-coms4995/markdown/slides/week6.md); [CMU, taught, p. 28](../../courses/cmu-11768/markdown/slides/lecture-05-planning.md); [LC, taught, line 18](../../courses/langchain-deep-agents/markdown/lessons/m1.1-overview.md); [S224, taught, line 1](../../courses/stanford-cs224v/markdown/slides/i-sliders.md).

<a id="concept-workflow-agent"></a>

### Workflows versus agents

`workflow-agent` · Agent design · original type: concept

Distinguish fixed program control flow from model-directed control flow.

**Aliases:** workflows vs agents; workflow versus agent.

**Evidence:** [S329, taught, p. 56](../../courses/stanford-cs329z/markdown/slides/lecture01.md); [COL, taught, p. 22](../../courses/columbia-coms4995/markdown/slides/week6.md); [CMU, taught, p. 3](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [CU, taught, p. 19](../../courses/colorado-csci7000/markdown/slides/w1l1.md).

<a id="concept-transformer"></a>

### Transformer and attention

`transformer` · Model fundamentals · original type: concept

Use attention-based neural networks to model token sequences.

**Aliases:** transformers; self-attention.

**Evidence:** [S329, taught, p. 43](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, p. 40](../../courses/columbia-coms4995/markdown/slides/week2.md); [CMU, taught, p. 10](../../courses/cmu-11768/markdown/slides/lecture-03-long-context.md); [BOOK, taught, line 454](../../courses/agentic-large-language-models/markdown/chapters/chapter-02-foundations-of-language-modeling-with-llms.md).

<a id="concept-llm-foundations"></a>

### Language model foundations

`llm-foundations` · Model fundamentals · original type: topic

Explain next-token modeling and the main parts of a language model.

**Aliases:** LLM foundations; language modeling.

**Evidence:** [S329, taught, p. 5](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, p. 13](../../courses/columbia-coms4995/markdown/slides/week1.md); [BOOK, taught, line 196](../../courses/agentic-large-language-models/markdown/chapters/chapter-02-foundations-of-language-modeling-with-llms.md).

<a id="concept-tokenization"></a>

### Tokenization

`tokenization` · Model fundamentals · original type: method

Convert text to token IDs and back using a defined vocabulary and algorithm.

**Related terms:** BPE; byte pair encoding.

**Evidence:** [COL, taught, line 66](../../courses/columbia-coms4995/markdown/assignments/hw1.md); [CMU, taught, p. 9](../../courses/cmu-11768/markdown/slides/lecture-06-coding-agents.md); [BOOK, taught, line 19](../../courses/agentic-large-language-models/markdown/chapters/chapter-02-foundations-of-language-modeling-with-llms.md).

<a id="concept-vlm"></a>

### Vision-language models

`vlm` · Model fundamentals · original type: topic

Use models that combine visual inputs and language outputs.

**Aliases:** VLMs; multimodal language models.

**Evidence:** [CMU, taught, p. 47](../../courses/cmu-11768/markdown/slides/lecture-07-computer-use-agents.md); [S224, taught, p. 13](../../courses/stanford-cs224v/markdown/slides/l-churro.md); [BOOK, taught, line 26](../../courses/agentic-large-language-models/markdown/chapters/chapter-07-vision-action-and-world-models.md).

<a id="concept-world-models"></a>

### World models

`world-models` · Model fundamentals · original type: concept

Predict environment states or outcomes to support reasoning and action.

**Aliases:** agentic world models.

**Also relevant to:** [Prompting, reasoning, and planning techniques](reasoning-techniques.md); [Model training and adaptation](training.md).

**Evidence:** [CMU, taught, p. 78](../../courses/cmu-11768/markdown/slides/lecture-06-coding-agents.md); [BOOK, taught, line 377](../../courses/agentic-large-language-models/markdown/chapters/chapter-07-vision-action-and-world-models.md).

<a id="concept-bdi"></a>

### Belief-desire-intention agents

`bdi` · Agent design · original type: concept

Represent agent behavior through beliefs, goals, and intentions.

**Related terms:** BDI agents.

**Evidence:** [BOOK, taught, line 61](../../courses/agentic-large-language-models/markdown/chapters/chapter-09-interaction-styles-for-agentic-llms.md).

<a id="concept-scaling-laws"></a>

### Language model scaling laws

`scaling-laws` · Model fundamentals · original type: concept

Relate model performance to data size, parameter count, and compute budget.

**Aliases:** compute-optimal scaling.

**Related terms:** Chinchilla scaling.

**Evidence:** [BOOK, taught, line 27](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-vla"></a>

### Vision-language-action models

`vla` · Model fundamentals · original type: topic

Map visual and language inputs to actions, often for embodied tasks.

**Aliases:** VLA models; vision language action models.

**Evidence:** [BOOK, taught, line 203](../../courses/agentic-large-language-models/markdown/chapters/chapter-07-vision-action-and-world-models.md).
