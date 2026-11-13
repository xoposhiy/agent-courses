# Columbia: Designing LLM Agents

A practical introduction that builds from language modeling and decoding to memory, planning, tools, and agent safety. Homework covers data preparation, a small classifier, retrieval, conversation memory, and a grounded persona agent.

[Archived source](../../courses/columbia-coms4995/README.md) · [Shared dictionary](../DICTIONARY.md) · [Summary](../README.md)

## Scope and limits

- Eight lecture decks and three homework descriptions are available.
- The later vibe-coding session is schedule-only; it is excluded from confirmed frequency.
- Exercise data, solutions, and starter implementations are supporting material rather than separate course occurrences.

## Concepts and evidence

T = explained or implemented in available teaching content; A = assigned reading; P = schedule only. The evidence is a reviewed selection, not a complete list of occurrences.

| Concept | Type | Coverage | Evidence |
| --- | --- | --- | --- |
| Abstention and uncertainty handling | pattern | taught | [hw3, line 70](../../courses/columbia-coms4995/markdown/assignments/hw3.md) |
| Agent architecture | topic | taught | [week1, p. 53](../../courses/columbia-coms4995/markdown/slides/week1.md) |
| Agent evaluation and benchmarks | topic | taught | [week7, p. 34](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Agent frameworks and orchestration | topic | taught | [week7, p. 37](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Agent harness design | topic | taught | [week6, p. 16](../../courses/columbia-coms4995/markdown/slides/week6.md) |
| Agent memory | topic | taught | [week4, p. 3](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Agent safety and guardrails | topic | taught | [week9, p. 72](../../courses/columbia-coms4995/markdown/slides/week9.md) |
| Answer verification | pattern | taught | [week4, p. 34](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Beam search | method | taught | [week3, p. 44](../../courses/columbia-coms4995/markdown/slides/week3.md) |
| Chain of thought | pattern | taught | [week4, p. 27](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Code-based evaluators | method | taught | [hw2, line 68](../../courses/columbia-coms4995/markdown/assignments/hw2.md) |
| Coding and terminal agents | application | planned | [index, line 49](../../courses/columbia-coms4995/markdown/pages/index.md) |
| Context engineering | topic | taught | [week4, p. 46](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Context summarization and compaction | pattern | taught | [week4, p. 52](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Conversation and execution state | concept | taught | [week6, p. 20](../../courses/columbia-coms4995/markdown/slides/week6.md) |
| Cost, latency, and quality tradeoffs | topic | taught | [week7, p. 33](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Decoding and sampling | topic | taught | [week3, p. 48](../../courses/columbia-coms4995/markdown/slides/week3.md) |
| Direct preference optimization | method | taught | [week5, p. 7](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Document chunking and indexing | method | taught | [week5, p. 48](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Embedding-based retrieval | method | taught | [week5, p. 51](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Error analysis and failure taxonomy | method | taught | [week7, p. 32](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Error handling and retries | pattern | taught | [week4, p. 19](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Evidence grounding and hallucination control | topic | taught | [week5, p. 55](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Few-shot prompting | method | taught | [hw2, line 65](../../courses/columbia-coms4995/markdown/assignments/hw2.md) |
| Gradient descent and backpropagation | method | taught | [week2, p. 24](../../courses/columbia-coms4995/markdown/slides/week2.md) |
| Human demonstrations and feedback | method | taught | [week5, p. 23](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Human oversight and approval | pattern | taught | [week7, p. 36](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Hybrid retrieval | method | taught | [week5, p. 52](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Language model foundations | topic | taught | [week1, p. 13](../../courses/columbia-coms4995/markdown/slides/week1.md) |
| Long-context modeling | topic | taught | [week4, p. 35](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Long-horizon agent tasks | topic | taught | [week6, p. 3](../../courses/columbia-coms4995/markdown/slides/week6.md) |
| Low-rank adaptation | method | taught | [week5, p. 40](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Memory poisoning | concept | taught | [week9, p. 31](../../courses/columbia-coms4995/markdown/slides/week9.md) |
| Model compression and quantization | method | taught | [week5, p. 45](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Model Context Protocol | protocol | taught | [week7, p. 43](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Model training and post-training | topic | taught | [week3, p. 3](../../courses/columbia-coms4995/markdown/slides/week3.md) |
| Multi-step reasoning | topic | taught | [week4, p. 24](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Parallel execution | pattern | taught | [week7, p. 24](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Persona and response style control | application | taught | [hw3, line 56](../../courses/columbia-coms4995/markdown/assignments/hw3.md) |
| Plan then execute | pattern | taught | [week6, p. 58](../../courses/columbia-coms4995/markdown/slides/week6.md) |
| Planning and task decomposition | topic | taught | [week6, p. 54](../../courses/columbia-coms4995/markdown/slides/week6.md) |
| Privacy and user data protection | topic | taught | [hw1, line 54](../../courses/columbia-coms4995/markdown/assignments/hw1.md) |
| Prompt chaining | pattern | taught | [week6, p. 27](../../courses/columbia-coms4995/markdown/slides/week6.md) |
| Prompt design | topic | taught | [week4, p. 6](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Prompt injection | concept | taught | [week9, p. 27](../../courses/columbia-coms4995/markdown/slides/week9.md) |
| ReAct | pattern | taught | [week1, p. 58](../../courses/columbia-coms4995/markdown/slides/week1.md) |
| Red teaming and adversarial evaluation | method | taught | [week9, p. 94](../../courses/columbia-coms4995/markdown/slides/week9.md) |
| Reflection and self-correction | pattern | taught | [week4, p. 33](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Reflexion | method | taught | [week4, p. 33](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Reinforcement learning | topic | taught | [week5, p. 7](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Reinforcement learning from human feedback | method | taught | [week5, p. 23](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Response caching | method | taught | [week4, p. 20](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Retrieval evaluation | topic | taught | [hw2, line 55](../../courses/columbia-coms4995/markdown/assignments/hw2.md) |
| Retrieval-augmented generation | topic | taught | [week5, p. 47](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Reward hacking and evaluation gaming | concept | taught | [week5, p. 24](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Reward modeling | method | taught | [week5, p. 22](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Routing | pattern | taught | [week6, p. 47](../../courses/columbia-coms4995/markdown/slides/week6.md) |
| Sandboxed execution | method | taught | [week9, p. 91](../../courses/columbia-coms4995/markdown/slides/week9.md) |
| Self-consistency | pattern | taught | [week4, p. 30](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Semantic memory | concept | taught | [hw2, line 91](../../courses/columbia-coms4995/markdown/assignments/hw2.md) |
| Sliding-window conversation memory | pattern | taught | [week4, p. 50](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Soft prompt tuning | method | taught | [week4, p. 15](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Sparse retrieval | method | taught | [week5, p. 51](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Structured output and constrained decoding | method | taught | [hw2, line 68](../../courses/columbia-coms4995/markdown/assignments/hw2.md) |
| Supervised fine-tuning | method | taught | [week5, p. 16](../../courses/columbia-coms4995/markdown/slides/week5.md) |
| Task outcome and state-change verification | topic | taught | [week7, p. 33](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Threat modeling and least privilege | method | taught | [week9, p. 90](../../courses/columbia-coms4995/markdown/slides/week9.md) |
| Tokenization | method | taught | [hw1, line 66](../../courses/columbia-coms4995/markdown/assignments/hw1.md) |
| Tool use and function calling | topic | taught | [week7, p. 7](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Tool-call evaluation | topic | taught | [week7, p. 33](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Tracing and observability | topic | taught | [week7, p. 40](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Training data selection and quality | topic | taught | [hw1, line 55](../../courses/columbia-coms4995/markdown/assignments/hw1.md) |
| Trajectory and process evaluation | topic | taught | [week7, p. 34](../../courses/columbia-coms4995/markdown/slides/week7.md) |
| Transformer and attention | concept | taught | [week2, p. 40](../../courses/columbia-coms4995/markdown/slides/week2.md) |
| Tree of thoughts | pattern | taught | [week4, p. 31](../../courses/columbia-coms4995/markdown/slides/week4.md) |
| Workflows versus agents | concept | taught | [week6, p. 22](../../courses/columbia-coms4995/markdown/slides/week6.md) |
| Working memory | concept | taught | [week4, p. 50](../../courses/columbia-coms4995/markdown/slides/week4.md) |

## Dictionary update

Concepts first registered in this source: 22. Final source inventory after cross-course review: 77 concepts. Later evidence updates are listed in the reconciliation audit.
