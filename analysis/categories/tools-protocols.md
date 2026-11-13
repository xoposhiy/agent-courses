# Named tools, frameworks, and protocols

Named implementation technologies and interoperability standards.

Products and standards belong here. Generic framework design, tool-use concepts, and implementation methods remain separate.

[All categories](README.md) · [CSV](tools-protocols.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**5 concepts**: 5 confirmed in courses; 0 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Model Context Protocol](#concept-mcp) | protocol | 4 | 4 | 0 | S329, COL, CMU, LC | CU | yes |
| [LangGraph](#concept-langgraph) | tool | 3 | 3 | 0 | S329, CMU, LC | CU |  |
| [Agent2Agent protocol](#concept-a2a) | protocol | 1 | 1 | 0 | S329 |  |  |
| [DSPy](#concept-dspy) | tool | 1 | 1 | 0 | S329 |  |  |
| [Managed agent hosting](#concept-managed-agents) | tool | 1 | 1 | 0 | LC |  |  |

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

<a id="concept-mcp"></a>

### Model Context Protocol

`mcp` · Protocols · original type: protocol

Connect agent hosts and tool servers through a shared tool interface.

**Aliases:** MCP.

**Evidence:** [S329, taught, p. 52](../../courses/stanford-cs329z/markdown/slides/lecture04.md); [COL, taught, p. 43](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 42](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [LC, taught, line 49](../../courses/langchain-deep-agents/markdown/lessons/m1.6-mcp.md); [CU, planned, line 100](../../courses/colorado-csci7000/markdown/pages/page-index.md); [BOOK, taught, line 21](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-langgraph"></a>

### LangGraph

`langgraph` · Frameworks and hosting · original type: tool

Build stateful model workflows with nodes, edges, and graph state.

**Evidence:** [S329, taught, p. 76](../../courses/stanford-cs329z/markdown/slides/lecture05.md); [CMU, taught, p. 7](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [LC, taught, line 52](../../courses/langchain-deep-agents/markdown/lessons/m5.2-local-deployment.md); [CU, planned, line 93](../../courses/colorado-csci7000/markdown/pages/page-index.md).

<a id="concept-a2a"></a>

### Agent2Agent protocol

`a2a` · Protocols · original type: protocol

Describe and exchange tasks between agents through a shared protocol.

**Aliases:** A2A.

**Evidence:** [S329, taught, p. 45](../../courses/stanford-cs329z/markdown/slides/lecture08.md).

<a id="concept-dspy"></a>

### DSPy

`dspy` · Frameworks and hosting · original type: tool

Build and optimize language model programs with signatures, modules, and optimizers.

**Evidence:** [S329, taught, p. 51](../../courses/stanford-cs329z/markdown/slides/lecture05.md).

<a id="concept-managed-agents"></a>

### Managed agent hosting

`managed-agents` · Frameworks and hosting · original type: tool

Use a hosted service to run agents and provide storage, tools, and interfaces.

**Related terms:** Managed Deep Agents; MDA.

**Evidence:** [LC, taught, line 12](../../courses/langchain-deep-agents/markdown/lessons/m6.1-what-is-managed-deep-agents.md).
