# Context and memory techniques

Ways to select active context, store experience, maintain memory, and reuse skills.

Context isolation and tiered memory are information-management patterns. They stay here rather than under system topology. Memory evaluation belongs under evaluation.

[All categories](README.md) · [CSV](context-memory.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**17 concepts**: 17 confirmed in courses; 0 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Agent memory](#concept-memory) | topic | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| [Context engineering](#concept-context-engineering) | topic | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| [Context summarization and compaction](#concept-compaction) | pattern | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  | yes |
| [Context isolation](#concept-context-isolation) | pattern | 4 | 4 | 0 | S329, CMU, LC, S224 |  |  |
| [Context offloading](#concept-context-offload) | pattern | 4 | 4 | 0 | S329, CMU, LC, S224 |  |  |
| [Memory maintenance and consolidation](#concept-memory-maintenance) | pattern | 3 | 3 | 0 | S329, CMU, LC |  | yes |
| [Procedural memory and skills](#concept-procedural-memory) | concept | 3 | 3 | 0 | S329, CMU, LC | S224 |  |
| [Progressive disclosure](#concept-progressive-disclosure) | pattern | 3 | 3 | 0 | S329, CMU, LC |  |  |
| [Working memory](#concept-working-memory) | concept | 3 | 3 | 0 | S329, COL, LC |  | yes |
| [Semantic memory](#concept-semantic-memory) | concept | 2 | 2 | 0 | S329, COL |  |  |
| [Episodic memory](#concept-episodic-memory) | concept | 2 | 1 | 1 | S329, CU |  |  |
| [Dialogue state tracking and management](#concept-dialogue-state) | topic | 1 | 1 | 0 | S224 |  |  |
| [Memory scoping and user isolation](#concept-memory-scoping) | pattern | 1 | 1 | 0 | LC |  |  |
| [Observation masking](#concept-observation-masking) | pattern | 1 | 1 | 0 | S329 |  |  |
| [Skill induction from experience](#concept-skill-induction) | method | 1 | 1 | 0 | CMU |  |  |
| [Sliding-window conversation memory](#concept-sliding-memory) | pattern | 1 | 1 | 0 | COL |  |  |
| [Tiered memory](#concept-tiered-memory) | pattern | 1 | 1 | 0 | S329 |  |  |

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

<a id="concept-memory"></a>

### Agent memory

`memory` · Memory representations and maintenance · original type: topic

Store and reuse information across steps or interactions.

**Aliases:** agent memory architectures.

**Evidence:** [S329, taught, p. 10](../../courses/stanford-cs329z/markdown/slides/lecture07.md); [COL, taught, p. 3](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 17](../../courses/cmu-11768/markdown/slides/lecture-04-memory-and-skills.md); [LC, taught, line 39](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md); [S224, taught, p. 14](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [CU, assigned, p. 2](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-11432.md); [BOOK, taught, line 21](../../courses/agentic-large-language-models/markdown/chapters/chapter-09-interaction-styles-for-agentic-llms.md).

<a id="concept-context-engineering"></a>

### Context engineering

`context-engineering` · Context management · original type: topic

Select and organize the information supplied to a model for each step.

**Aliases:** context management.

**Evidence:** [S329, taught, p. 57](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 46](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 4](../../courses/cmu-11768/markdown/slides/lecture-03-long-context.md); [LC, taught, line 42](../../courses/langchain-deep-agents/markdown/lessons/m3.1-summarization-context-offloading.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md); [CU, assigned, p. 4](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-11432.md); [BOOK, taught, line 55](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-compaction"></a>

### Context summarization and compaction

`compaction` · Context management · original type: pattern

Replace long interaction history with a shorter useful representation.

**Aliases:** context summarization; compaction.

**Evidence:** [S329, taught, p. 61](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 52](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 48](../../courses/cmu-11768/markdown/slides/lecture-03-long-context.md); [LC, taught, line 66](../../courses/langchain-deep-agents/markdown/lessons/m3.1-summarization-context-offloading.md); [S224, taught, p. 21](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [BOOK, taught, line 489](../../courses/agentic-large-language-models/markdown/chapters/chapter-09-interaction-styles-for-agentic-llms.md).

<a id="concept-context-isolation"></a>

### Context isolation

`context-isolation` · Context management · original type: pattern

Give a task or subagent a separate context to limit interference.

**Also relevant to:** [Architectural patterns](architecture.md).

**Evidence:** [S329, taught, p. 61](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [CMU, taught, p. 13](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [LC, taught, line 146](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md); [S224, taught, p. 21](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md).

<a id="concept-context-offload"></a>

### Context offloading

`context-offload` · Context management · original type: pattern

Store information outside the active prompt and load it when needed.

**Aliases:** memory offloading; context offloading to files.

**Related terms:** memory offloading.

**Evidence:** [S329, taught, p. 61](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [CMU, taught, p. 48](../../courses/cmu-11768/markdown/slides/lecture-03-long-context.md); [LC, taught, line 42](../../courses/langchain-deep-agents/markdown/lessons/m3.1-summarization-context-offloading.md); [S224, taught, p. 21](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md).

<a id="concept-memory-maintenance"></a>

### Memory maintenance and consolidation

`memory-maintenance` · Memory representations and maintenance · original type: pattern

Update, combine, remove, or reorganize stored memories.

**Aliases:** memory consolidation; forgetting.

**Evidence:** [S329, taught, p. 57](../../courses/stanford-cs329z/markdown/slides/lecture07.md); [CMU, taught, p. 42](../../courses/cmu-11768/markdown/slides/lecture-04-memory-and-skills.md); [LC, taught, line 123](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md); [BOOK, taught, line 510](../../courses/agentic-large-language-models/markdown/chapters/chapter-09-interaction-styles-for-agentic-llms.md).

<a id="concept-procedural-memory"></a>

### Procedural memory and skills

`procedural-memory` · Memory representations and maintenance · original type: concept

Store reusable procedures or skills that guide actions.

**Aliases:** skill libraries; agent skills.

**Also relevant to:** [Runtime, deployment, and performance](runtime.md).

**Evidence:** [S329, taught, p. 20](../../courses/stanford-cs329z/markdown/slides/lecture07.md); [CMU, taught, p. 8](../../courses/cmu-11768/markdown/slides/lecture-04-memory-and-skills.md); [LC, taught, line 35](../../courses/langchain-deep-agents/markdown/lessons/m3.2-skills.md); [S224, planned, line 32](../../courses/stanford-cs224v/markdown/pages/schedule.md).

<a id="concept-progressive-disclosure"></a>

### Progressive disclosure

`progressive-disclosure` · Context management · original type: pattern

Load instructions or tool details only when the current task needs them.

**Evidence:** [S329, taught, p. 70](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [CMU, taught, p. 11](../../courses/cmu-11768/markdown/slides/lecture-04-memory-and-skills.md); [LC, taught, line 83](../../courses/langchain-deep-agents/markdown/lessons/m3.2-skills.md).

<a id="concept-working-memory"></a>

### Working memory

`working-memory` · Memory representations and maintenance · original type: concept

Keep information needed for the current task in active context.

**Aliases:** short-term memory.

**Evidence:** [S329, taught, p. 17](../../courses/stanford-cs329z/markdown/slides/lecture07.md); [COL, taught, p. 50](../../courses/columbia-coms4995/markdown/slides/week4.md); [LC, taught, line 43](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md); [BOOK, taught, line 489](../../courses/agentic-large-language-models/markdown/chapters/chapter-09-interaction-styles-for-agentic-llms.md).

<a id="concept-semantic-memory"></a>

### Semantic memory

`semantic-memory` · Memory representations and maintenance · original type: concept

Store facts and general knowledge for later use.

**Evidence:** [S329, taught, p. 19](../../courses/stanford-cs329z/markdown/slides/lecture07.md); [COL, taught, line 91](../../courses/columbia-coms4995/markdown/assignments/hw2.md).

<a id="concept-episodic-memory"></a>

### Episodic memory

`episodic-memory` · Memory representations and maintenance · original type: concept

Store events or past experiences that an agent can recall.

**Evidence:** [S329, taught, p. 18](../../courses/stanford-cs329z/markdown/slides/lecture07.md); [CU, assigned, p. 2](../../courses/colorado-csci7000/markdown/readings/arxiv-2303-11366.md).

<a id="concept-dialogue-state"></a>

### Dialogue state tracking and management

`dialogue-state` · Dialogue context · original type: topic

Represent conversation facts, task state, and valid next actions.

**Aliases:** dialog state tracking; conversational management.

**Evidence:** [S224, taught, p. 39](../../courses/stanford-cs224v/markdown/slides/l-newworksheet.md).

<a id="concept-memory-scoping"></a>

### Memory scoping and user isolation

`memory-scoping` · Memory representations and maintenance · original type: pattern

Keep persistent memories separate by user, thread, or workspace.

**Aliases:** memory isolation; memory namespaces.

**Also relevant to:** [Safety, security, and trust](safety-trust.md).

**Evidence:** [LC, taught, line 194](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md).

<a id="concept-observation-masking"></a>

### Observation masking

`observation-masking` · Context management · original type: pattern

Remove or hide older tool outputs while keeping useful interaction structure.

**Evidence:** [S329, taught, p. 61](../../courses/stanford-cs329z/markdown/slides/lecture06.md).

<a id="concept-skill-induction"></a>

### Skill induction from experience

`skill-induction` · Memory representations and maintenance · original type: method

Extract reusable procedures or code from prior task trajectories.

**Aliases:** skill learning; skill induction.

**Also relevant to:** [Model training and adaptation](training.md).

**Evidence:** [CMU, taught, p. 21](../../courses/cmu-11768/markdown/slides/lecture-04-memory-and-skills.md).

<a id="concept-sliding-memory"></a>

### Sliding-window conversation memory

`sliding-memory` · Context management · original type: pattern

Keep only a recent window of interaction history in the prompt.

**Aliases:** sliding window memory.

**Evidence:** [COL, taught, p. 50](../../courses/columbia-coms4995/markdown/slides/week4.md).

<a id="concept-tiered-memory"></a>

### Tiered memory

`tiered-memory` · Memory representations and maintenance · original type: pattern

Move information between memory levels with different capacity and access costs.

**Aliases:** memory hierarchy.

**Related terms:** MemGPT.

**Also relevant to:** [Architectural patterns](architecture.md).

**Evidence:** [S329, taught, p. 42](../../courses/stanford-cs329z/markdown/slides/lecture07.md).
