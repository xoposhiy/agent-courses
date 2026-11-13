# Application areas

Types of tasks and domains where an agent is applied.

An application describes the work an agent does. Its reasoning, architecture, or evaluation is classified separately. Persona and style control is a prompting technique.

[All categories](README.md) · [CSV](applications.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**14 concepts**: 11 confirmed in courses; 3 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Coding and terminal agents](#concept-coding-agents) | application | 5 | 5 | 0 | S329, CMU, LC, S224, CU | COL | yes |
| [Deep research agents](#concept-deep-research) | application | 3 | 3 | 0 | CMU, LC, S224 |  |  |
| [Agentic debugging and refactoring](#concept-refactoring) | application | 2 | 2 | 0 | CMU, CU |  |  |
| [Natural-language database and graph queries](#concept-db-query) | application | 2 | 2 | 0 | LC, S224 |  | yes |
| [Clinical decision and literature agents](#concept-clinical-agents) | application | 1 | 1 | 0 | S224 |  | yes |
| [Computer-use and web agents](#concept-computer-use) | application | 1 | 1 | 0 | CMU |  | yes |
| [Data-driven research and analysis](#concept-structured-research) | application | 1 | 1 | 0 | S224 |  |  |
| [Historical document transcription](#concept-document-transcription) | application | 1 | 1 | 0 | S224 |  |  |
| [Sales and business assistants](#concept-sales-agents) | application | 1 | 1 | 0 | LC |  | yes |
| [Social simulation with agents](#concept-social-simulation) | application | 1 | 1 | 0 | CMU |  | yes |
| [Scientific workflow automation](#concept-scientific-workflows) | application | 1 | 0 | 1 | CU |  | yes |
| [Agents for games and puzzles](#concept-game-agents) | application | 0 | 0 | 0 |  |  | yes |
| [Trading and financial assistants](#concept-trading-agents) | application | 0 | 0 | 0 |  |  | yes |
| [Travel and flight assistants](#concept-travel-agents) | application | 0 | 0 | 0 |  |  | yes |

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

<a id="concept-coding-agents"></a>

### Coding and terminal agents

`coding-agents` · Software and interface work · original type: application

Use agents to write, edit, test, or run code and command-line tasks.

**Aliases:** software engineering agents; terminal agents.

**Evidence:** [S329, taught, p. 1](../../courses/stanford-cs329z/markdown/slides/lecture10.md); [COL, planned, line 49](../../courses/columbia-coms4995/markdown/pages/index.md); [CMU, taught, p. 33](../../courses/cmu-11768/markdown/slides/lecture-06-coding-agents.md); [LC, taught, line 76](../../courses/langchain-deep-agents/markdown/lessons/m2.3-sandboxes-and-localshell.md); [S224, taught, p. 40](../../courses/stanford-cs224v/markdown/slides/i-sliders.md); [CU, taught, p. 12](../../courses/colorado-csci7000/markdown/slides/w1l1.md); [BOOK, taught, line 348](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).

<a id="concept-deep-research"></a>

### Deep research agents

`deep-research` · Research and data work · original type: application

Run repeated searches, inspect evidence, and synthesize a research answer.

**Aliases:** deep research; research agents.

**Evidence:** [CMU, taught, p. 6](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [LC, taught, line 43](../../courses/langchain-deep-agents/markdown/lessons/m4.2-building-a-subagent-team.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw1.md).

<a id="concept-refactoring"></a>

### Agentic debugging and refactoring

`refactoring` · Software and interface work · original type: application

Use agents to locate bugs or change code structure while preserving required behavior.

**Aliases:** autonomous program improvement; refactoring agents.

**Evidence:** [CMU, taught, p. 33](../../courses/cmu-11768/markdown/slides/lecture-06-coding-agents.md); [CU, taught, p. 18](../../courses/colorado-csci7000/markdown/slides/w1l1.md).

<a id="concept-db-query"></a>

### Natural-language database and graph queries

`db-query` · Research and data work · original type: application

Use language models to query structured databases and knowledge graphs.

**Aliases:** knowledge graph querying; database agents.

**Evidence:** [LC, taught, line 152](../../courses/langchain-deep-agents/markdown/lessons/m2.4-interpreter.md); [S224, taught, p. 3](../../courses/stanford-cs224v/markdown/slides/l-agentic.md); [BOOK, taught, line 22](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-clinical-agents"></a>

### Clinical decision and literature agents

`clinical-agents` · Domain assistants and simulations · original type: application

Use agents to analyze clinical evidence, compare patient findings, or match trial criteria.

**Aliases:** clinical trial matching; rare-disease diagnosis.

**Evidence:** [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/slides/l-smt-match.md); [BOOK, taught, line 198](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).

<a id="concept-computer-use"></a>

### Computer-use and web agents

`computer-use` · Software and interface work · original type: application

Observe and operate browser or desktop interfaces to complete tasks.

**Aliases:** GUI agents; computer use agents; browser agents.

**Evidence:** [CMU, taught, p. 2](../../courses/cmu-11768/markdown/slides/lecture-07-computer-use-agents.md); [BOOK, taught, line 268](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-structured-research"></a>

### Data-driven research and analysis

`structured-research` · Research and data work · original type: application

Use queries and analysis to form, test, and explain findings from structured data.

**Aliases:** data-driven deep research.

**Related terms:** DataSTORM.

**Evidence:** [S224, taught, p. 10](../../courses/stanford-cs224v/markdown/slides/l-data-driven-deep-research.md).

<a id="concept-document-transcription"></a>

### Historical document transcription

`document-transcription` · Research and data work · original type: application

Extract structured text and layout from scans of printed or handwritten documents.

**Aliases:** document transcription.

**Related terms:** OCR; CHURRO.

**Evidence:** [S224, taught, p. 10](../../courses/stanford-cs224v/markdown/slides/l-churro.md).

<a id="concept-sales-agents"></a>

### Sales and business assistants

`sales-agents` · Domain assistants and simulations · original type: application

Use an agent to manage customer requests, business data, reports, or messages.

**Aliases:** sales assistants; business assistants.

**Evidence:** [LC, taught, line 21](../../courses/langchain-deep-agents/markdown/lessons/m5.1-putting-it-all-together.md); [BOOK, taught, line 89](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).

<a id="concept-social-simulation"></a>

### Social simulation with agents

`social-simulation` · Domain assistants and simulations · original type: application

Use interacting agents to model communities, groups, or societies.

**Aliases:** generative agent societies; agent-based social simulation.

**Evidence:** [CMU, taught, p. 37](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [BOOK, taught, line 54](../../courses/agentic-large-language-models/markdown/chapters/chapter-17-emergent-behavior-in-multi-llm-systems.md).

<a id="concept-scientific-workflows"></a>

### Scientific workflow automation

`scientific-workflows` · Research and data work · original type: application

Use agents to configure and run scientific tools or experiments.

**Related terms:** MDCrow; molecular dynamics agents.

**Evidence:** [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/ref-0cfd55675bb9.md); [BOOK, taught, line 322](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).

<a id="concept-game-agents"></a>

### Agents for games and puzzles

`game-agents` · Domain assistants and simulations · original type: application

Use agents to act in game environments or solve interactive puzzles.

**Aliases:** game-playing agents.

**Related terms:** BALROG.

**Evidence:** [BOOK, taught, line 19](../../courses/agentic-large-language-models/markdown/chapters/chapter-10-case-study-2-balrog-for-llm-reasoning-and-reflection.md).

<a id="concept-trading-agents"></a>

### Trading and financial assistants

`trading-agents` · Domain assistants and simulations · original type: application

Use agents to analyze financial information or support trading decisions.

**Aliases:** financial agents.

**Evidence:** [BOOK, taught, line 260](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).

<a id="concept-travel-agents"></a>

### Travel and flight assistants

`travel-agents` · Domain assistants and simulations · original type: application

Use agents to plan trips, book travel, or support flight operations.

**Aliases:** travel planning agents.

**Evidence:** [BOOK, taught, line 149](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).
