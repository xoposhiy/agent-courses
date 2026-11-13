# Course Topic Analysis

Analysis of seven downloaded courses. The downloaded book is a separate comparison source.

[Category dictionaries](categories/README.md) · [Method and limits](METHOD.md) · [Shared dictionary](DICTIONARY.md) · [Frequency CSV](frequency.csv) · [Course matrix](course-matrix.csv) · [Structured evidence](courses/)

The dictionary contains **205 concepts**. Frequency counts distinct courses with available teaching content or assigned readings. Planned topics and the book do not increase this count.

## Sources

| Code | Source | Confirmed concepts | Planned only | New dictionary entries |
| --- | --- | ---: | ---: | ---: |
| S329 | [Stanford: Engineering AI Agents](courses/stanford-cs329z.md) | 96 | 6 | 90 |
| COL | [Columbia: Designing LLM Agents](courses/columbia-coms4995.md) | 76 | 1 | 22 |
| CMU | [Carnegie Mellon: AI Agents](courses/cmu-11768.md) | 114 | 0 | 21 |
| LC | [LangChain Academy: Introduction to Deep Agents](courses/langchain-deep-agents.md) | 58 | 0 | 12 |
| S224 | [Stanford: Agentic AI](courses/stanford-cs224v.md) | 71 | 2 | 20 |
| EVAL | [DeepLearning.AI / Arize: Evaluating and Improving Agentic Applications](courses/dlai-agentic-evals.md) | 32 | 0 | 8 |
| CU | [CU Boulder: Building AI Agents](courses/colorado-csci7000.md) | 49 | 2 | 6 |
| BOOK | [Book: Agentic Large Language Models](courses/agentic-large-language-models.md) | 117 | 0 | 26 |

## Most frequent concepts

The first 30 rows use the same ranking as the full table. Ties use the number of courses with teaching evidence, then the concept name.

| Concept | Courses / 7 | Taught | Assigned | Courses | Planned only | Book |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Agent architecture | 7 | 7 | 0 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| Agent evaluation and benchmarks | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| Prompt design | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| Tool use and function calling | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| Human oversight and approval | 6 | 6 | 0 | COL, CMU, LC, S224, EVAL, CU | S329 | yes |
| Structured output and constrained decoding | 6 | 6 | 0 | S329, COL, CMU, LC, S224, EVAL |  |  |
| Tracing and observability | 6 | 6 | 0 | S329, COL, CMU, LC, S224, EVAL |  | yes |
| Agent frameworks and orchestration | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Agent harness design | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Agent memory | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Context engineering | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Planning and task decomposition | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Coding and terminal agents | 5 | 5 | 0 | S329, CMU, LC, S224, CU | COL | yes |
| Context summarization and compaction | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  | yes |
| Conversation and execution state | 5 | 5 | 0 | COL, CMU, LC, S224, CU |  | yes |
| Long-context modeling | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  | yes |
| Parallel execution | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  |  |
| Agent safety and guardrails | 5 | 4 | 1 | COL, CMU, LC, EVAL, CU | S329 | yes |
| Cost, latency, and quality tradeoffs | 5 | 4 | 1 | S329, COL, CMU, EVAL, CU |  | yes |
| Error analysis and failure taxonomy | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  |  |
| Evidence grounding and hallucination control | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  | yes |
| Human evaluation | 5 | 4 | 1 | S329, CMU, S224, EVAL, CU |  |  |
| Multi-agent systems | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| Orchestrator and workers | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| ReAct | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Reflection and self-correction | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Retrieval-augmented generation | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Shared memory and task coordination | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| Supervised fine-tuning | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Trajectory and process evaluation | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  |  |

## Most frequent patterns

| Concept | Courses / 7 | Taught | Assigned | Courses | Planned only | Book |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Human oversight and approval | 6 | 6 | 0 | COL, CMU, LC, S224, EVAL, CU | S329 | yes |
| Context summarization and compaction | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  | yes |
| Parallel execution | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  |  |
| Orchestrator and workers | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| ReAct | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Reflection and self-correction | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Shared memory and task coordination | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| Context isolation | 4 | 4 | 0 | S329, CMU, LC, S224 |  |  |
| Context offloading | 4 | 4 | 0 | S329, CMU, LC, S224 |  |  |
| Plan then execute | 4 | 4 | 0 | S329, COL, CMU, S224 |  | yes |
| Routing | 4 | 4 | 0 | S329, COL, CMU, EVAL |  |  |
| Agent as a tool | 4 | 3 | 1 | S329, CMU, LC, CU |  |  |
| Answer verification | 4 | 3 | 1 | COL, CMU, S224, CU |  | yes |
| Chain of thought | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| Self-consistency | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| Abstention and uncertainty handling | 3 | 3 | 0 | COL, CMU, EVAL |  | yes |
| CodeAct | 3 | 3 | 0 | S329, CMU, LC |  |  |
| Durable execution and recovery | 3 | 3 | 0 | S329, CMU, LC |  |  |
| Memory maintenance and consolidation | 3 | 3 | 0 | S329, CMU, LC |  | yes |
| Progressive disclosure | 3 | 3 | 0 | S329, CMU, LC |  |  |

## Full frequency table

| Concept | Courses / 7 | Taught | Assigned | Courses | Planned only | Book |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Agent architecture | 7 | 7 | 0 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| Agent evaluation and benchmarks | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| Prompt design | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| Tool use and function calling | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| Human oversight and approval | 6 | 6 | 0 | COL, CMU, LC, S224, EVAL, CU | S329 | yes |
| Structured output and constrained decoding | 6 | 6 | 0 | S329, COL, CMU, LC, S224, EVAL |  |  |
| Tracing and observability | 6 | 6 | 0 | S329, COL, CMU, LC, S224, EVAL |  | yes |
| Agent frameworks and orchestration | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Agent harness design | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Agent memory | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Context engineering | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Planning and task decomposition | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| Coding and terminal agents | 5 | 5 | 0 | S329, CMU, LC, S224, CU | COL | yes |
| Context summarization and compaction | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  | yes |
| Conversation and execution state | 5 | 5 | 0 | COL, CMU, LC, S224, CU |  | yes |
| Long-context modeling | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  | yes |
| Parallel execution | 5 | 5 | 0 | S329, COL, CMU, LC, S224 |  |  |
| Agent safety and guardrails | 5 | 4 | 1 | COL, CMU, LC, EVAL, CU | S329 | yes |
| Cost, latency, and quality tradeoffs | 5 | 4 | 1 | S329, COL, CMU, EVAL, CU |  | yes |
| Error analysis and failure taxonomy | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  |  |
| Evidence grounding and hallucination control | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  | yes |
| Human evaluation | 5 | 4 | 1 | S329, CMU, S224, EVAL, CU |  |  |
| Multi-agent systems | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| Orchestrator and workers | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| ReAct | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Reflection and self-correction | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Retrieval-augmented generation | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Shared memory and task coordination | 5 | 4 | 1 | S329, CMU, LC, S224, CU |  | yes |
| Supervised fine-tuning | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| Trajectory and process evaluation | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  |  |
| Code-based evaluators | 4 | 4 | 0 | S329, COL, CMU, EVAL |  | yes |
| Context isolation | 4 | 4 | 0 | S329, CMU, LC, S224 |  |  |
| Context offloading | 4 | 4 | 0 | S329, CMU, LC, S224 |  |  |
| Embedding-based retrieval | 4 | 4 | 0 | S329, COL, CMU, S224 |  | yes |
| Evaluation rubrics | 4 | 4 | 0 | S329, CMU, S224, EVAL |  |  |
| Judge validation and bias | 4 | 4 | 0 | S329, CMU, S224, EVAL |  | yes |
| LLM as a judge | 4 | 4 | 0 | S329, CMU, S224, EVAL |  | yes |
| Long-horizon agent tasks | 4 | 4 | 0 | COL, CMU, LC, S224 |  |  |
| Model Context Protocol | 4 | 4 | 0 | S329, COL, CMU, LC | CU | yes |
| Personalization and user modeling | 4 | 4 | 0 | S329, CMU, LC, S224 |  | yes |
| Plan then execute | 4 | 4 | 0 | S329, COL, CMU, S224 |  | yes |
| Reliability and repeated-run evaluation | 4 | 4 | 0 | S329, CMU, S224, EVAL |  |  |
| Routing | 4 | 4 | 0 | S329, COL, CMU, EVAL |  |  |
| Sparse retrieval | 4 | 4 | 0 | S329, COL, CMU, S224 |  | yes |
| Tool-call evaluation | 4 | 4 | 0 | S329, COL, CMU, EVAL |  |  |
| User and environment simulation | 4 | 4 | 0 | S329, CMU, S224, EVAL |  | yes |
| Workflows versus agents | 4 | 4 | 0 | S329, COL, CMU, CU |  |  |
| Agent as a tool | 4 | 3 | 1 | S329, CMU, LC, CU |  |  |
| Answer verification | 4 | 3 | 1 | COL, CMU, S224, CU |  | yes |
| Benchmark and test-set design | 4 | 3 | 1 | S329, CMU, EVAL, CU |  | yes |
| Chain of thought | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| Human-agent collaboration | 4 | 3 | 1 | CMU, LC, S224, CU |  | yes |
| Multi-step reasoning | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| Reflexion | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| Reinforcement learning | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| Sandboxed execution | 4 | 3 | 1 | COL, CMU, LC, CU | S329 |  |
| Self-consistency | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| Synthetic data and trajectory generation | 4 | 3 | 1 | S329, CMU, EVAL, CU |  | yes |
| Abstention and uncertainty handling | 3 | 3 | 0 | COL, CMU, EVAL |  | yes |
| CodeAct | 3 | 3 | 0 | S329, CMU, LC |  |  |
| Decoding and sampling | 3 | 3 | 0 | S329, COL, EVAL |  |  |
| Deep research agents | 3 | 3 | 0 | CMU, LC, S224 |  |  |
| Document chunking and indexing | 3 | 3 | 0 | S329, COL, S224 |  | yes |
| Durable execution and recovery | 3 | 3 | 0 | S329, CMU, LC |  |  |
| Few-shot prompting | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| Human demonstrations and feedback | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| LangGraph | 3 | 3 | 0 | S329, CMU, LC | CU |  |
| Memory maintenance and consolidation | 3 | 3 | 0 | S329, CMU, LC |  | yes |
| Model training and post-training | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| Multi-agent failure analysis | 3 | 3 | 0 | S329, CMU, S224 |  | yes |
| Privacy and user data protection | 3 | 3 | 0 | COL, CMU, LC | S329 | yes |
| Procedural memory and skills | 3 | 3 | 0 | S329, CMU, LC | S224 |  |
| Progressive disclosure | 3 | 3 | 0 | S329, CMU, LC |  |  |
| Prompt injection | 3 | 3 | 0 | COL, CMU, LC | S329 |  |
| Prompt prefix and KV caching | 3 | 3 | 0 | S329, CMU, LC |  | yes |
| Retrieval evaluation | 3 | 3 | 0 | S329, COL, S224 |  | yes |
| Reward hacking and evaluation gaming | 3 | 3 | 0 | S329, COL, CMU | S224 |  |
| Reward modeling | 3 | 3 | 0 | S329, COL, CMU |  |  |
| Task outcome and state-change verification | 3 | 3 | 0 | COL, CMU, EVAL |  | yes |
| Threat modeling and least privilege | 3 | 3 | 0 | COL, CMU, LC |  |  |
| Training data selection and quality | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| Transformer and attention | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| Working memory | 3 | 3 | 0 | S329, COL, LC |  | yes |
| Automatic harness improvement | 3 | 2 | 1 | S329, CMU, CU |  | yes |
| Knowledge curation and synthesis | 3 | 2 | 1 | CMU, S224, CU |  |  |
| Multi-agent debate | 3 | 2 | 1 | S329, CMU, CU |  | yes |
| Agent deployment and service APIs | 2 | 2 | 0 | CMU, LC |  | yes |
| Agent filesystem and storage backends | 2 | 2 | 0 | LC, S224 |  |  |
| Agentic debugging and refactoring | 2 | 2 | 0 | CMU, CU |  |  |
| Agentic retrieval | 2 | 2 | 0 | S329, CMU |  | yes |
| Asynchronous agent coordination | 2 | 2 | 0 | CMU, LC |  |  |
| Beam search | 2 | 2 | 0 | S329, COL |  |  |
| Checkpointing and resuming | 2 | 2 | 0 | CMU, LC |  |  |
| Citation and evidence evaluation | 2 | 2 | 0 | CMU, S224 |  | yes |
| Error handling and retries | 2 | 2 | 0 | COL, CMU |  | yes |
| Group relative policy optimization | 2 | 2 | 0 | S329, CMU |  |  |
| Hybrid retrieval | 2 | 2 | 0 | S329, COL |  | yes |
| Inference serving and performance | 2 | 2 | 0 | S329, CMU |  | yes |
| Inference-time scaling | 2 | 2 | 0 | S329, CMU |  | yes |
| Knowledge distillation | 2 | 2 | 0 | S329, CMU |  | yes |
| Language model foundations | 2 | 2 | 0 | S329, COL |  | yes |
| Natural-language database and graph queries | 2 | 2 | 0 | LC, S224 |  | yes |
| Persona and response style control | 2 | 2 | 0 | COL, LC |  | yes |
| Programmatic tool composition | 2 | 2 | 0 | CMU, LC |  |  |
| Prompt chaining | 2 | 2 | 0 | S329, COL |  |  |
| Proximal policy optimization | 2 | 2 | 0 | S329, CMU |  |  |
| Recursive and self-modifying agents | 2 | 2 | 0 | S329, LC |  | yes |
| Red teaming and adversarial evaluation | 2 | 2 | 0 | COL, CMU |  | yes |
| Regression and version comparison | 2 | 2 | 0 | CMU, EVAL |  |  |
| Reinforcement learning from human feedback | 2 | 2 | 0 | S329, COL |  | yes |
| Reranking and late interaction | 2 | 2 | 0 | S329, S224 |  | yes |
| Semantic memory | 2 | 2 | 0 | S329, COL |  |  |
| Speculative decoding | 2 | 2 | 0 | S329, CMU |  | yes |
| Tokenization | 2 | 2 | 0 | COL, CMU |  | yes |
| Tool authentication and credential handling | 2 | 2 | 0 | CMU, LC |  | yes |
| Vision-language models | 2 | 2 | 0 | CMU, S224 |  | yes |
| Work automation and social impact | 2 | 2 | 0 | CMU, S224 |  |  |
| Episodic memory | 2 | 1 | 1 | S329, CU |  |  |
| Multi-turn and session evaluation | 2 | 1 | 1 | EVAL, CU |  |  |
| Schema induction and information extraction | 2 | 1 | 1 | S224, CU |  |  |
| Tool discovery and selection | 2 | 1 | 1 | S329, CU |  |  |
| Agent handoffs | 1 | 1 | 0 | S329 |  |  |
| Agent middleware | 1 | 1 | 0 | LC |  |  |
| Agent2Agent protocol | 1 | 1 | 0 | S329 |  |  |
| Automatic prompt optimization | 1 | 1 | 0 | S329 |  | yes |
| Best-of-N selection | 1 | 1 | 0 | CMU |  |  |
| Clinical decision and literature agents | 1 | 1 | 0 | S224 |  | yes |
| Computer-use and web agents | 1 | 1 | 0 | CMU |  | yes |
| Concept canonicalization and ontologies | 1 | 1 | 0 | S224 |  |  |
| Constraint-satisfaction retrieval | 1 | 1 | 0 | S224 |  |  |
| Controlled improvement experiments | 1 | 1 | 0 | EVAL |  |  |
| Credit assignment and advantage estimation | 1 | 1 | 0 | CMU |  |  |
| Data-driven research and analysis | 1 | 1 | 0 | S224 |  |  |
| Database reconciliation and deduplication | 1 | 1 | 0 | S224 |  |  |
| Decision rationale and data provenance | 1 | 1 | 0 | S224 |  |  |
| Declarative task-oriented agent specifications | 1 | 1 | 0 | S224 |  |  |
| Dialogue state tracking and management | 1 | 1 | 0 | S224 |  |  |
| Direct preference optimization | 1 | 1 | 0 | COL |  | yes |
| Distributed and asynchronous RL systems | 1 | 1 | 0 | CMU |  |  |
| DSPy | 1 | 1 | 0 | S329 |  |  |
| Dynamic subagent creation and batch delegation | 1 | 1 | 0 | LC |  |  |
| Embedded code interpreter | 1 | 1 | 0 | LC |  |  |
| Emergent communication and social norms | 1 | 1 | 0 | CMU |  | yes |
| Evaluator and optimizer loop | 1 | 1 | 0 | S329 |  | yes |
| Evaluator precision, recall, and agreement | 1 | 1 | 0 | EVAL |  |  |
| Exploration and curriculum design | 1 | 1 | 0 | CMU |  |  |
| Formal reasoning with SMT | 1 | 1 | 0 | S224 |  |  |
| Gradient descent and backpropagation | 1 | 1 | 0 | COL |  | yes |
| Graph-based retrieval | 1 | 1 | 0 | S329 |  | yes |
| Historical document transcription | 1 | 1 | 0 | S224 |  |  |
| Hypothesis and evidence ledger | 1 | 1 | 0 | S224 |  |  |
| Low-rank adaptation | 1 | 1 | 0 | COL |  | yes |
| Managed agent hosting | 1 | 1 | 0 | LC |  |  |
| Memory evaluation | 1 | 1 | 0 | S329 |  |  |
| Memory poisoning | 1 | 1 | 0 | COL |  |  |
| Memory scoping and user isolation | 1 | 1 | 0 | LC |  |  |
| Missing-data imputation and assumptions | 1 | 1 | 0 | S224 |  |  |
| Model compression and quantization | 1 | 1 | 0 | COL |  | yes |
| Model selection and provider integration | 1 | 1 | 0 | LC |  | yes |
| Observation masking | 1 | 1 | 0 | S329 |  |  |
| Perspective-guided research | 1 | 1 | 0 | S224 |  |  |
| Policy gradient methods | 1 | 1 | 0 | CMU |  |  |
| Proactive and mixed-initiative agents | 1 | 1 | 0 | S224 | S329 |  |
| Production monitoring and evaluation feedback | 1 | 1 | 0 | EVAL |  |  |
| Queries over structured and unstructured data | 1 | 1 | 0 | S224 |  |  |
| Requirements and expected behavior | 1 | 1 | 0 | EVAL |  |  |
| Research design and paper critique | 1 | 1 | 0 | CU |  |  |
| Research result reproduction | 1 | 1 | 0 | S224 |  | yes |
| Response caching | 1 | 1 | 0 | COL |  |  |
| Sales and business assistants | 1 | 1 | 0 | LC |  | yes |
| Semantic parsing to formal queries | 1 | 1 | 0 | S224 |  |  |
| Skill induction from experience | 1 | 1 | 0 | CMU |  |  |
| Sliding-window conversation memory | 1 | 1 | 0 | COL |  |  |
| Social simulation with agents | 1 | 1 | 0 | CMU |  | yes |
| Soft prompt tuning | 1 | 1 | 0 | COL |  |  |
| State replay and branching | 1 | 1 | 0 | LC |  |  |
| Strategic and social agent behavior | 1 | 1 | 0 | CMU |  | yes |
| Tiered memory | 1 | 1 | 0 | S329 |  |  |
| Tree of thoughts | 1 | 1 | 0 | COL |  | yes |
| Visual interface grounding | 1 | 1 | 0 | CMU |  |  |
| Workspace isolation | 1 | 1 | 0 | S329 |  |  |
| World models | 1 | 1 | 0 | CMU |  | yes |
| Developer-agent alignment | 1 | 0 | 1 | CU |  |  |
| Scientific workflow automation | 1 | 0 | 1 | CU |  | yes |
| Self-play training | 1 | 0 | 1 | CU |  | yes |
| Activation patching and causal intervention | 0 | 0 | 0 |  |  | yes |
| Agents for games and puzzles | 0 | 0 | 0 |  |  | yes |
| Behavioral experiments on agents | 0 | 0 | 0 |  |  | yes |
| Belief-desire-intention agents | 0 | 0 | 0 |  |  | yes |
| Cognitive analysis of agents | 0 | 0 | 0 |  |  | yes |
| Consciousness and agency theories | 0 | 0 | 0 |  |  | yes |
| Language model scaling laws | 0 | 0 | 0 |  |  | yes |
| Mechanistic interpretability | 0 | 0 | 0 |  |  | yes |
| Meta-learning | 0 | 0 | 0 |  |  | yes |
| Metacognition and self-knowledge | 0 | 0 | 0 |  |  | yes |
| Model circuit analysis | 0 | 0 | 0 |  |  | yes |
| Model collapse and synthetic-data risks | 0 | 0 | 0 |  |  | yes |
| Model-based reinforcement learning | 0 | 0 | 0 |  |  | yes |
| Moral judgment and ethical behavior | 0 | 0 | 0 |  |  | yes |
| Query rewriting and expansion | 0 | 0 | 0 |  |  | yes |
| Sparse autoencoders for feature discovery | 0 | 0 | 0 |  |  | yes |
| Theory of mind | 0 | 0 | 0 |  |  | yes |
| Trading and financial assistants | 0 | 0 | 0 |  |  | yes |
| Travel and flight assistants | 0 | 0 | 0 |  |  | yes |
| Vision-language-action models | 0 | 0 | 0 |  |  | yes |

## Interpretation

Course frequency shows how widely a concept appears across these sources. It does not measure teaching time, depth, quality, or importance. A broad topic and a specific pattern can both appear in the table; their counts must not be added.

A blank course entry means no confirmed evidence was recorded in the selected available materials. It does not prove that the course omits the topic. Read the course reports and archive gap reports before treating a difference as a curriculum gap.
