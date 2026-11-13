# Runtime, deployment, and performance

Execution infrastructure, persistence, recovery, service operation, and inference cost or speed.

These mechanisms support execution rather than define agent-team topology. Named products and protocols are separate. Training infrastructure stays under training.

[All categories](README.md) · [CSV](runtime.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**15 concepts**: 15 confirmed in courses; 0 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Tracing and observability](#concept-observability) | topic | 6 | 6 | 0 | S329, COL, CMU, LC, S224, EVAL |  | yes |
| [Cost, latency, and quality tradeoffs](#concept-cost-quality) | topic | 5 | 4 | 1 | S329, COL, CMU, EVAL, CU |  | yes |
| [Durable execution and recovery](#concept-durable-execution) | pattern | 3 | 3 | 0 | S329, CMU, LC |  |  |
| [Prompt prefix and KV caching](#concept-kv-cache) | method | 3 | 3 | 0 | S329, CMU, LC |  | yes |
| [Agent deployment and service APIs](#concept-deployment) | topic | 2 | 2 | 0 | CMU, LC |  | yes |
| [Agent filesystem and storage backends](#concept-filesystem) | topic | 2 | 2 | 0 | LC, S224 |  |  |
| [Checkpointing and resuming](#concept-checkpointing) | pattern | 2 | 2 | 0 | CMU, LC |  |  |
| [Error handling and retries](#concept-error-recovery) | pattern | 2 | 2 | 0 | COL, CMU |  | yes |
| [Inference serving and performance](#concept-serving) | topic | 2 | 2 | 0 | S329, CMU |  | yes |
| [Speculative decoding](#concept-speculative-decoding) | method | 2 | 2 | 0 | S329, CMU |  | yes |
| [Agent middleware](#concept-middleware) | concept | 1 | 1 | 0 | LC |  |  |
| [Model compression and quantization](#concept-compression) | method | 1 | 1 | 0 | COL |  | yes |
| [Model selection and provider integration](#concept-model-selection) | topic | 1 | 1 | 0 | LC |  | yes |
| [Response caching](#concept-caching) | method | 1 | 1 | 0 | COL |  |  |
| [State replay and branching](#concept-state-replay) | pattern | 1 | 1 | 0 | LC |  |  |

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

<a id="concept-observability"></a>

### Tracing and observability

`observability` · Serving and performance · original type: topic

Record agent steps and inspect behavior, failures, and runtime measurements.

**Aliases:** agent traces; telemetry; tracing.

**Also relevant to:** [Evaluation, research, and improvement](evaluation.md).

**Evidence:** [S329, taught, p. 118](../../courses/stanford-cs329z/markdown/slides/lecture05.md); [COL, taught, p. 40](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 18](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [LC, taught, line 81](../../courses/langchain-deep-agents/markdown/lessons/m5.2-local-deployment.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw1.md); [EVAL, taught, p. 47](../../courses/dlai-agentic-evals/markdown/slides/module-1.md); [BOOK, taught, line 121](../../courses/agentic-large-language-models/markdown/chapters/chapter-05-case-study-1-building-llms-from-scratch.md).

<a id="concept-cost-quality"></a>

### Cost, latency, and quality tradeoffs

`cost-quality` · Serving and performance · original type: topic

Compare performance gains with runtime cost, time, and failure consequences.

**Aliases:** cost-quality tradeoffs; latency tradeoffs.

**Evidence:** [S329, taught, p. 11](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [COL, taught, p. 33](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 76](../../courses/cmu-11768/markdown/slides/lecture-06-coding-agents.md); [EVAL, taught, p. 32](../../courses/dlai-agentic-evals/markdown/slides/module-5.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2603-22327.md); [BOOK, taught, line 383](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-durable-execution"></a>

### Durable execution and recovery

`durable-execution` · Persistence and recovery · original type: pattern

Persist execution state and recover work after failures or pauses.

**Aliases:** durable workflows; retries and recovery.

**Evidence:** [S329, taught, p. 101](../../courses/stanford-cs329z/markdown/slides/lecture05.md); [CMU, taught, p. 16](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [LC, taught, line 119](../../courses/langchain-deep-agents/markdown/lessons/m1.7-messages-threads-checkpointers.md).

<a id="concept-kv-cache"></a>

### Prompt prefix and KV caching

`kv-cache` · Serving and performance · original type: method

Reuse attention keys and values or shared prompt prefixes to reduce inference work.

**Aliases:** KV caching; prefix caching.

**Evidence:** [S329, taught, p. 168](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [CMU, taught, p. 37](../../courses/cmu-11768/markdown/slides/lecture-03-long-context.md); [LC, taught, line 74](../../courses/langchain-deep-agents/markdown/lessons/m1.4-system-prompt.md); [BOOK, taught, line 351](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-deployment"></a>

### Agent deployment and service APIs

`deployment` · Execution infrastructure · original type: topic

Run an agent as a persistent service with APIs and supporting infrastructure.

**Aliases:** agent deployment; agent server.

**Evidence:** [CMU, taught, p. 19](../../courses/cmu-11768/markdown/slides/lecture-14-openhands.md); [LC, taught, line 50](../../courses/langchain-deep-agents/markdown/lessons/m5.2-local-deployment.md); [BOOK, taught, line 271](../../courses/agentic-large-language-models/markdown/chapters/chapter-05-case-study-1-building-llms-from-scratch.md).

<a id="concept-filesystem"></a>

### Agent filesystem and storage backends

`filesystem` · Execution infrastructure · original type: topic

Expose file tools while controlling where files are stored and how they persist.

**Aliases:** filesystem backends; agent filesystem.

**Evidence:** [LC, taught, line 58](../../courses/langchain-deep-agents/markdown/lessons/m2.1-the-deep-agent-environment.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md).

<a id="concept-checkpointing"></a>

### Checkpointing and resuming

`checkpointing` · Persistence and recovery · original type: pattern

Save agent state so a thread or task can resume after interruption.

**Aliases:** checkpointers; execution checkpoints.

**Evidence:** [CMU, taught, p. 17](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [LC, taught, line 104](../../courses/langchain-deep-agents/markdown/lessons/m1.7-messages-threads-checkpointers.md).

<a id="concept-error-recovery"></a>

### Error handling and retries

`error-recovery` · Persistence and recovery · original type: pattern

Detect model or tool errors and retry, recover, or stop safely.

**Aliases:** exception handling; exponential backoff.

**Evidence:** [COL, taught, p. 19](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 56](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [BOOK, taught, line 576](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-serving"></a>

### Inference serving and performance

`serving` · Serving and performance · original type: topic

Manage inference engines, batching, latency, throughput, and memory use.

**Aliases:** model serving; inference optimization.

**Evidence:** [S329, taught, p. 120](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [CMU, taught, p. 9](../../courses/cmu-11768/markdown/slides/lecture-03-long-context.md); [BOOK, taught, line 383](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-speculative-decoding"></a>

### Speculative decoding

`speculative-decoding` · Serving and performance · original type: method

Use a draft model and verification to generate tokens with less inference time.

**Evidence:** [S329, taught, p. 136](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [CMU, taught, p. 12](../../courses/cmu-11768/markdown/slides/lecture-12-rl-systems.md); [BOOK, taught, line 425](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-middleware"></a>

### Agent middleware

`middleware` · Execution infrastructure · original type: concept

Add reusable behavior around model calls, tool calls, and agent execution.

**Aliases:** middleware hooks.

**Evidence:** [LC, taught, line 61](../../courses/langchain-deep-agents/markdown/lessons/m1.5-tools.md).

<a id="concept-compression"></a>

### Model compression and quantization

`compression` · Serving and performance · original type: method

Reduce model size or arithmetic precision to lower execution costs.

**Aliases:** model quantization; compression.

**Evidence:** [COL, taught, p. 45](../../courses/columbia-coms4995/markdown/slides/week5.md); [BOOK, taught, line 410](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-model-selection"></a>

### Model selection and provider integration

`model-selection` · Execution infrastructure · original type: topic

Choose a model for capability, cost, privacy, and tool support and connect its API.

**Aliases:** model selection.

**Related terms:** model providers.

**Also relevant to:** [Foundations and design concepts](foundations.md).

**Evidence:** [LC, taught, line 44](../../courses/langchain-deep-agents/markdown/lessons/m1.3-models.md); [BOOK, taught, line 196](../../courses/agentic-large-language-models/markdown/chapters/chapter-10-case-study-2-balrog-for-llm-reasoning-and-reflection.md).

<a id="concept-caching"></a>

### Response caching

`caching` · Serving and performance · original type: method

Reuse stored results for repeated model or tool requests.

**Aliases:** API caching; disk cache.

**Evidence:** [COL, taught, p. 20](../../courses/columbia-coms4995/markdown/slides/week4.md).

<a id="concept-state-replay"></a>

### State replay and branching

`state-replay` · Persistence and recovery · original type: pattern

Inspect earlier checkpoints and resume or fork from a previous state.

**Aliases:** time travel; state branching.

**Evidence:** [LC, taught, line 140](../../courses/langchain-deep-agents/markdown/lessons/m1.7-messages-threads-checkpointers.md).
