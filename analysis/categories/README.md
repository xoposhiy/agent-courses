# Frequency Dictionaries by Category

The shared dictionary contains **205 concepts** in **13 primary categories**. **185** have confirmed course evidence; **20** have confirmed evidence only in the book.

[Category method and boundaries](METHOD.md) · [All concepts CSV](all-concepts.csv) · [Category summary CSV](summary.csv) · [Course coverage CSV](category-course-counts.csv) · [Original analysis](../README.md)

Each concept belongs to one primary category. Related categories are cross-references. This keeps architectural patterns separate from local techniques and named products without repeating concepts in category totals.

## Category dictionaries

| Category | All concepts | Confirmed in courses | Book only | Most frequent concepts | CSV |
| --- | ---: | ---: | ---: | --- | --- |
| [Foundations and design concepts](foundations.md) | 16 | 13 | 3 | Agent architecture (7/7); Agent frameworks and orchestration (6/7); Agent harness design (6/7) | [CSV](foundations.csv) |
| [Architectural patterns](architecture.md) | 18 | 18 | 0 | Human oversight and approval (6/7); Parallel execution (5/7); Orchestrator and workers (5/7) | [CSV](architecture.csv) |
| [Prompting, reasoning, and planning techniques](reasoning-techniques.md) | 19 | 19 | 0 | Prompt design (7/7); Structured output and constrained decoding (6/7); Planning and task decomposition (6/7) | [CSV](reasoning-techniques.csv) |
| [Context and memory techniques](context-memory.md) | 17 | 17 | 0 | Agent memory (6/7); Context engineering (6/7); Context summarization and compaction (5/7) | [CSV](context-memory.csv) |
| [Retrieval, data, and knowledge techniques](retrieval-knowledge.md) | 19 | 18 | 1 | Retrieval-augmented generation (5/7); Embedding-based retrieval (4/7); Sparse retrieval (4/7) | [CSV](retrieval-knowledge.csv) |
| [Tool-use and action techniques](tool-techniques.md) | 5 | 5 | 0 | Tool use and function calling (7/7); Programmatic tool composition (2/7); Tool discovery and selection (2/7) | [CSV](tool-techniques.csv) |
| [Model training and adaptation](training.md) | 22 | 19 | 3 | Supervised fine-tuning (5/7); Reinforcement learning (4/7); Synthetic data and trajectory generation (4/7) | [CSV](training.csv) |
| [Evaluation, research, and improvement](evaluation.md) | 28 | 27 | 1 | Agent evaluation and benchmarks (7/7); Error analysis and failure taxonomy (5/7); Human evaluation (5/7) | [CSV](evaluation.csv) |
| [Safety, security, and trust](safety-trust.md) | 11 | 11 | 0 | Agent safety and guardrails (5/7); Evidence grounding and hallucination control (5/7); Sandboxed execution (4/7) | [CSV](safety-trust.csv) |
| [Runtime, deployment, and performance](runtime.md) | 15 | 15 | 0 | Tracing and observability (6/7); Cost, latency, and quality tradeoffs (5/7); Durable execution and recovery (3/7) | [CSV](runtime.csv) |
| [Named tools, frameworks, and protocols](tools-protocols.md) | 5 | 5 | 0 | Model Context Protocol (4/7); LangGraph (3/7); Agent2Agent protocol (1/7) | [CSV](tools-protocols.csv) |
| [Application areas](applications.md) | 14 | 11 | 3 | Coding and terminal agents (5/7); Deep research agents (3/7); Agentic debugging and refactoring (2/7) | [CSV](applications.csv) |
| [Agent behavior, human interaction, and interpretability](behavior.md) | 16 | 7 | 9 | Personalization and user modeling (4/7); Human-agent collaboration (4/7); Work automation and social impact (2/7) | [CSV](behavior.csv) |

## How to read the categories

Architecture describes how a system is arranged and who controls the next step. A technique describes an operation, such as sampling reasoning paths, summarizing context, or reranking search results. A product or protocol describes an implementation choice. An application describes the work the agent performs.

For example, orchestrator and workers is an architectural pattern; self-consistency is a reasoning technique; context compaction is a context technique; MCP is a protocol; and a coding agent is an application area. Human approval is classified as a control-flow pattern and linked to safety. The category method explains other boundary cases.

## Course coverage by category

Cells count distinct confirmed concepts in the category and course. They do not measure lessons, teaching hours, depth, or course quality. The book is excluded. Category size depends on the dictionary's granularity.

| Category | S329 | COL | CMU | LC | S224 | EVAL | CU |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Foundations and design concepts](foundations.md) | 8 | 10 | 12 | 7 | 8 | 1 | 6 |
| [Architectural patterns](architecture.md) | 14 | 6 | 11 | 9 | 7 | 2 | 6 |
| [Prompting, reasoning, and planning techniques](reasoning-techniques.md) | 13 | 15 | 12 | 4 | 6 | 3 | 8 |
| [Context and memory techniques](context-memory.md) | 13 | 6 | 9 | 10 | 6 | 0 | 3 |
| [Retrieval, data, and knowledge techniques](retrieval-knowledge.md) | 8 | 5 | 5 | 0 | 15 | 0 | 3 |
| [Tool-use and action techniques](tool-techniques.md) | 2 | 1 | 3 | 3 | 1 | 1 | 2 |
| [Model training and adaptation](training.md) | 11 | 10 | 14 | 0 | 1 | 1 | 4 |
| [Evaluation, research, and improvement](evaluation.md) | 15 | 8 | 18 | 1 | 13 | 19 | 8 |
| [Safety, security, and trust](safety-trust.md) | 0 | 9 | 9 | 6 | 2 | 3 | 3 |
| [Runtime, deployment, and performance](runtime.md) | 6 | 5 | 9 | 9 | 2 | 2 | 1 |
| [Named tools, frameworks, and protocols](tools-protocols.md) | 4 | 1 | 2 | 3 | 0 | 0 | 0 |
| [Application areas](applications.md) | 1 | 0 | 5 | 4 | 6 | 0 | 3 |
| [Agent behavior, human interaction, and interpretability](behavior.md) | 1 | 0 | 5 | 2 | 4 | 0 | 2 |

## Course codes

- **S329**: [Stanford: Engineering AI Agents](../courses/stanford-cs329z.md)
- **COL**: [Columbia: Designing LLM Agents](../courses/columbia-coms4995.md)
- **CMU**: [Carnegie Mellon: AI Agents](../courses/cmu-11768.md)
- **LC**: [LangChain Academy: Introduction to Deep Agents](../courses/langchain-deep-agents.md)
- **S224**: [Stanford: Agentic AI](../courses/stanford-cs224v.md)
- **EVAL**: [DeepLearning.AI / Arize: Evaluating and Improving Agentic Applications](../courses/dlai-agentic-evals.md)
- **CU**: [CU Boulder: Building AI Agents](../courses/colorado-csci7000.md)
- **BOOK**: [Book: Agentic Large Language Models](../courses/agentic-large-language-models.md)

## Count rules

A concept's frequency is unchanged from the original analysis: one count per course with taught or assigned evidence. Schedule-only topics and the book do not raise that frequency. Counts are not inherited from parent concepts. Book-only concepts remain visible at frequency zero.

Each category file includes the full frequency ranking, definitions, aliases, related terms, and source evidence. Its CSV preserves the original frequency fields and adds the primary category, subgroup, and related categories.
