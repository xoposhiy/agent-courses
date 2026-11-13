# Tool-use and action techniques

Ways to define, discover, compose, and execute tools or map observations to actions.

Generic tool-use capabilities and methods belong here. MCP and named frameworks belong under tools and protocols. CodeAct as an agent-loop design belongs under architecture.

[All categories](README.md) · [CSV](tool-techniques.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**5 concepts**: 5 confirmed in courses; 0 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Tool use and function calling](#concept-tool-use) | topic | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| [Programmatic tool composition](#concept-programmatic-tools) | pattern | 2 | 2 | 0 | CMU, LC |  |  |
| [Tool discovery and selection](#concept-tool-discovery) | method | 2 | 1 | 1 | S329, CU |  |  |
| [Embedded code interpreter](#concept-code-interpreter) | method | 1 | 1 | 0 | LC |  |  |
| [Visual interface grounding](#concept-visual-grounding) | method | 1 | 1 | 0 | CMU |  |  |

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

<a id="concept-tool-use"></a>

### Tool use and function calling

`tool-use` · Tool interfaces and selection · original type: topic

Let a model choose and call external functions and consume their results.

**Aliases:** tool calling; function calling; tool invocation.

**Evidence:** [S329, taught, p. 1](../../courses/stanford-cs329z/markdown/slides/lecture04.md); [COL, taught, p. 7](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 3](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [LC, taught, line 44](../../courses/langchain-deep-agents/markdown/lessons/m1.5-tools.md); [S224, taught, p. 2](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md); [EVAL, taught, p. 14](../../courses/dlai-agentic-evals/markdown/slides/module-4.md); [CU, assigned, p. 2](../../courses/colorado-csci7000/markdown/readings/arxiv-2302-04761.md); [BOOK, taught, line 41](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-programmatic-tools"></a>

### Programmatic tool composition

`programmatic-tools` · Programmatic execution · original type: pattern

Write code that calls and combines several tools in one execution.

**Aliases:** programmatic tool calling; PTC.

**Also relevant to:** [Architectural patterns](architecture.md); [Runtime, deployment, and performance](runtime.md).

**Evidence:** [CMU, taught, p. 13](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [LC, taught, line 372](../../courses/langchain-deep-agents/markdown/lessons/m2.4-interpreter.md).

<a id="concept-tool-discovery"></a>

### Tool discovery and selection

`tool-discovery` · Tool interfaces and selection · original type: method

Find and select relevant tools from available tool descriptions.

**Aliases:** tool retrieval; API selection.

**Also relevant to:** [Retrieval, data, and knowledge techniques](retrieval-knowledge.md).

**Evidence:** [S329, taught, p. 53](../../courses/stanford-cs329z/markdown/slides/lecture04.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2305-15334.md).

<a id="concept-code-interpreter"></a>

### Embedded code interpreter

`code-interpreter` · Programmatic execution · original type: method

Run generated code in an interpreter within the agent loop.

**Aliases:** code interpreter; interpreter middleware.

**Also relevant to:** [Runtime, deployment, and performance](runtime.md).

**Evidence:** [LC, taught, line 46](../../courses/langchain-deep-agents/markdown/lessons/m2.4-interpreter.md).

<a id="concept-visual-grounding"></a>

### Visual interface grounding

`visual-grounding` · Tool interfaces and selection · original type: method

Map a visual instruction or screen element to an actionable UI target.

**Aliases:** UI grounding; screen grounding.

**Evidence:** [CMU, taught, p. 20](../../courses/cmu-11768/markdown/slides/lecture-07-computer-use-agents.md).
