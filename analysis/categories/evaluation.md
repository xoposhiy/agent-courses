# Evaluation, research, and improvement

Ways to define expected behavior, measure agents, validate judges, analyze failures, and test improvements.

A composed evaluator-optimizer loop belongs under architecture. Graders, experiments, and failure analyses belong here. Runtime tracing has a cross-reference from runtime.

[All categories](README.md) · [CSV](evaluation.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**28 concepts**: 27 confirmed in courses; 1 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Agent evaluation and benchmarks](#concept-evaluation) | topic | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| [Error analysis and failure taxonomy](#concept-error-analysis) | method | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  |  |
| [Human evaluation](#concept-human-eval) | method | 5 | 4 | 1 | S329, CMU, S224, EVAL, CU |  |  |
| [Trajectory and process evaluation](#concept-trajectory-eval) | topic | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  |  |
| [Code-based evaluators](#concept-code-grader) | method | 4 | 4 | 0 | S329, COL, CMU, EVAL |  | yes |
| [Evaluation rubrics](#concept-rubrics) | method | 4 | 4 | 0 | S329, CMU, S224, EVAL |  |  |
| [Judge validation and bias](#concept-judge-validation) | topic | 4 | 4 | 0 | S329, CMU, S224, EVAL |  | yes |
| [LLM as a judge](#concept-llm-judge) | method | 4 | 4 | 0 | S329, CMU, S224, EVAL |  | yes |
| [Reliability and repeated-run evaluation](#concept-reliability) | topic | 4 | 4 | 0 | S329, CMU, S224, EVAL |  |  |
| [Tool-call evaluation](#concept-tool-eval) | topic | 4 | 4 | 0 | S329, COL, CMU, EVAL |  |  |
| [User and environment simulation](#concept-user-simulation) | method | 4 | 4 | 0 | S329, CMU, S224, EVAL |  | yes |
| [Benchmark and test-set design](#concept-benchmark-design) | topic | 4 | 3 | 1 | S329, CMU, EVAL, CU |  | yes |
| [Multi-agent failure analysis](#concept-multi-agent-failures) | topic | 3 | 3 | 0 | S329, CMU, S224 |  | yes |
| [Retrieval evaluation](#concept-retrieval-eval) | topic | 3 | 3 | 0 | S329, COL, S224 |  | yes |
| [Reward hacking and evaluation gaming](#concept-reward-hacking) | concept | 3 | 3 | 0 | S329, COL, CMU | S224 |  |
| [Task outcome and state-change verification](#concept-outcome-eval) | topic | 3 | 3 | 0 | COL, CMU, EVAL |  | yes |
| [Automatic harness improvement](#concept-harness-optimization) | method | 3 | 2 | 1 | S329, CMU, CU |  | yes |
| [Citation and evidence evaluation](#concept-citation-eval) | topic | 2 | 2 | 0 | CMU, S224 |  | yes |
| [Regression and version comparison](#concept-regression-eval) | method | 2 | 2 | 0 | CMU, EVAL |  |  |
| [Multi-turn and session evaluation](#concept-session-eval) | topic | 2 | 1 | 1 | EVAL, CU |  |  |
| [Controlled improvement experiments](#concept-controlled-eval) | method | 1 | 1 | 0 | EVAL |  |  |
| [Evaluator precision, recall, and agreement](#concept-evaluator-metrics) | method | 1 | 1 | 0 | EVAL |  |  |
| [Memory evaluation](#concept-memory-eval) | topic | 1 | 1 | 0 | S329 |  |  |
| [Production monitoring and evaluation feedback](#concept-production-eval) | pattern | 1 | 1 | 0 | EVAL |  |  |
| [Requirements and expected behavior](#concept-requirements) | method | 1 | 1 | 0 | EVAL |  |  |
| [Research design and paper critique](#concept-research-methods) | topic | 1 | 1 | 0 | CU |  |  |
| [Research result reproduction](#concept-research-reproduction) | method | 1 | 1 | 0 | S224 |  | yes |
| [Behavioral experiments on agents](#concept-behavioral-experiments) | method | 0 | 0 | 0 |  |  | yes |

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

<a id="concept-evaluation"></a>

### Agent evaluation and benchmarks

`evaluation` · Requirements and measurement · original type: topic

Measure agent behavior and outcomes with defined tasks and scores.

**Aliases:** agent evals; agent benchmarking.

**Evidence:** [S329, taught, p. 2](../../courses/stanford-cs329z/markdown/slides/lecture13.md); [COL, taught, p. 34](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 16](../../courses/cmu-11768/markdown/slides/2026-10-27-zora-wang.md); [LC, taught, line 910](../../courses/langchain-deep-agents/markdown/lessons/m4.3-dynamic-subagents.md); [S224, taught, p. 51](../../courses/stanford-cs224v/markdown/slides/l-freetext.md); [EVAL, taught, p. 15](../../courses/dlai-agentic-evals/markdown/slides/module-1.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-11432.md); [BOOK, taught, line 160](../../courses/agentic-large-language-models/markdown/chapters/chapter-10-case-study-2-balrog-for-llm-reasoning-and-reflection.md).

<a id="concept-error-analysis"></a>

### Error analysis and failure taxonomy

`error-analysis` · Analysis and improvement · original type: method

Inspect failed cases, label failure types, and prioritize fixes by frequency and impact.

**Aliases:** failure analysis; failure categories.

**Evidence:** [COL, taught, p. 32](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 29](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [S224, taught, p. 68](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [EVAL, taught, p. 25](../../courses/dlai-agentic-evals/markdown/slides/module-2.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2605-30777.md).

<a id="concept-human-eval"></a>

### Human evaluation

`human-eval` · Graders and judge validation · original type: method

Use human judgments or labels to assess agent behavior or outputs.

**Aliases:** human graders.

**Evidence:** [S329, taught, p. 17](../../courses/stanford-cs329z/markdown/slides/lecture15.md); [CMU, taught, p. 38](../../courses/cmu-11768/markdown/slides/2026-10-27-zora-wang.md); [S224, taught, p. 35](../../courses/stanford-cs224v/markdown/slides/l-data-driven-deep-research.md); [EVAL, taught, p. 36](../../courses/dlai-agentic-evals/markdown/slides/module-1.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2603-22327.md).

<a id="concept-trajectory-eval"></a>

### Trajectory and process evaluation

`trajectory-eval` · Requirements and measurement · original type: topic

Evaluate the sequence of agent decisions and actions rather than only the final output.

**Aliases:** process evaluation; trajectory evaluation.

**Evidence:** [COL, taught, p. 34](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 28](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [S224, taught, p. 2](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw1.md); [EVAL, taught, p. 19](../../courses/dlai-agentic-evals/markdown/slides/module-4.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2604-12147.md).

<a id="concept-code-grader"></a>

### Code-based evaluators

`code-grader` · Graders and judge validation · original type: method

Use deterministic code or tests to score agent behavior or outputs.

**Aliases:** code based graders; programmatic evaluators.

**Evidence:** [S329, taught, p. 14](../../courses/stanford-cs329z/markdown/slides/lecture15.md); [COL, taught, line 68](../../courses/columbia-coms4995/markdown/assignments/hw2.md); [CMU, taught, p. 23](../../courses/cmu-11768/markdown/slides/lecture-06-coding-agents.md); [EVAL, taught, p. 4](../../courses/dlai-agentic-evals/markdown/slides/module-3.md); [BOOK, taught, line 276](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-rubrics"></a>

### Evaluation rubrics

`rubrics` · Graders and judge validation · original type: method

Define explicit criteria and rating rules for judgments.

**Aliases:** custom rubrics; grading rubrics.

**Evidence:** [S329, taught, p. 49](../../courses/stanford-cs329z/markdown/slides/lecture15.md); [CMU, taught, p. 90](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [S224, taught, p. 66](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [EVAL, taught, p. 23](../../courses/dlai-agentic-evals/markdown/slides/module-3.md).

<a id="concept-judge-validation"></a>

### Judge validation and bias

`judge-validation` · Graders and judge validation · original type: topic

Check evaluator agreement, accuracy, and bias against trusted labels.

**Aliases:** validating LLM judges; evaluator calibration.

**Evidence:** [S329, taught, p. 11](../../courses/stanford-cs329z/markdown/slides/lecture15.md); [CMU, taught, p. 42](../../courses/cmu-11768/markdown/slides/2026-10-27-zora-wang.md); [S224, taught, p. 66](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [EVAL, taught, p. 33](../../courses/dlai-agentic-evals/markdown/slides/module-3.md); [BOOK, taught, line 33](../../courses/agentic-large-language-models/markdown/chapters/chapter-19-synthetic-data-generation-for-training-agentic-llms.md).

<a id="concept-llm-judge"></a>

### LLM as a judge

`llm-judge` · Graders and judge validation · original type: method

Use a language model to score another system with stated criteria.

**Aliases:** LLM-as-judge; LM-as-a-judge; LLM judge.

**Evidence:** [S329, taught, p. 20](../../courses/stanford-cs329z/markdown/slides/lecture15.md); [CMU, taught, p. 87](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [S224, taught, p. 66](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [EVAL, taught, p. 15](../../courses/dlai-agentic-evals/markdown/slides/module-3.md); [BOOK, taught, line 271](../../courses/agentic-large-language-models/markdown/chapters/chapter-19-synthetic-data-generation-for-training-agentic-llms.md).

<a id="concept-reliability"></a>

### Reliability and repeated-run evaluation

`reliability` · Requirements and measurement · original type: topic

Measure variation and success across repeated agent runs.

**Aliases:** nondeterminism.

**Related terms:** pass@k; pass^k.

**Evidence:** [S329, taught, p. 83](../../courses/stanford-cs329z/markdown/slides/lecture15.md); [CMU, taught, p. 26](../../courses/cmu-11768/markdown/slides/lecture-06-coding-agents.md); [S224, taught, p. 2](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw1.md); [EVAL, taught, p. 37](../../courses/dlai-agentic-evals/markdown/slides/module-1.md).

<a id="concept-tool-eval"></a>

### Tool-call evaluation

`tool-eval` · Requirements and measurement · original type: topic

Check selected tools, arguments, execution, and tool-use outcomes.

**Aliases:** function-call evaluation; tool use evaluation.

**Evidence:** [S329, taught, p. 58](../../courses/stanford-cs329z/markdown/slides/lecture04.md); [COL, taught, p. 33](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 54](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [EVAL, taught, p. 15](../../courses/dlai-agentic-evals/markdown/slides/module-4.md).

<a id="concept-user-simulation"></a>

### User and environment simulation

`user-simulation` · Analysis and improvement · original type: method

Simulate interaction partners or environments for training and testing.

**Aliases:** user simulators; simulated users.

**Also relevant to:** [Agent behavior, human interaction, and interpretability](behavior.md); [Model training and adaptation](training.md).

**Evidence:** [S329, taught, p. 53](../../courses/stanford-cs329z/markdown/slides/lecture11.md); [CMU, taught, p. 28](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [S224, taught, p. 68](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [EVAL, taught, p. 36](../../courses/dlai-agentic-evals/markdown/slides/module-4.md); [BOOK, taught, line 155](../../courses/agentic-large-language-models/markdown/chapters/chapter-17-emergent-behavior-in-multi-llm-systems.md).

<a id="concept-benchmark-design"></a>

### Benchmark and test-set design

`benchmark-design` · Requirements and measurement · original type: topic

Define tasks, environments, stopping rules, and scoring for evaluation.

**Aliases:** benchmark design; test set design.

**Evidence:** [S329, taught, p. 32](../../courses/stanford-cs329z/markdown/slides/lecture13.md); [CMU, taught, p. 24](../../courses/cmu-11768/markdown/slides/2026-10-27-zora-wang.md); [EVAL, taught, p. 51](../../courses/dlai-agentic-evals/markdown/slides/module-2.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2606-17799.md); [BOOK, taught, line 416](../../courses/agentic-large-language-models/markdown/chapters/chapter-03-the-large-language-model-training-pipeline.md).

<a id="concept-multi-agent-failures"></a>

### Multi-agent failure analysis

`multi-agent-failures` · Analysis and improvement · original type: topic

Analyze coordination failures, conflicting goals, and harmful group behavior.

**Aliases:** coordination failures.

**Also relevant to:** [Architectural patterns](architecture.md); [Agent behavior, human interaction, and interpretability](behavior.md).

**Evidence:** [S329, taught, p. 70](../../courses/stanford-cs329z/markdown/slides/lecture08.md); [CMU, taught, p. 31](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [S224, taught, p. 68](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [BOOK, taught, line 82](../../courses/agentic-large-language-models/markdown/chapters/chapter-17-emergent-behavior-in-multi-llm-systems.md).

<a id="concept-retrieval-eval"></a>

### Retrieval evaluation

`retrieval-eval` · Requirements and measurement · original type: topic

Measure whether retrieval returns relevant evidence.

**Aliases:** retrieval metrics; recall at k; MRR; nDCG.

**Evidence:** [S329, taught, p. 45](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [COL, taught, line 55](../../courses/columbia-coms4995/markdown/assignments/hw2.md); [S224, taught, p. 11](../../courses/stanford-cs224v/markdown/slides/l-smt-match.md); [BOOK, taught, line 956](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-reward-hacking"></a>

### Reward hacking and evaluation gaming

`reward-hacking` · Analysis and improvement · original type: concept

Exploit a reward or scoring rule without meeting the intended task.

**Aliases:** reward hacking; benchmark gaming.

**Also relevant to:** [Safety, security, and trust](safety-trust.md); [Model training and adaptation](training.md).

**Evidence:** [S329, taught, p. 44](../../courses/stanford-cs329z/markdown/slides/lecture10.md); [COL, taught, p. 24](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 41](../../courses/cmu-11768/markdown/slides/lecture-11-rl-advanced.md); [S224, planned, line 33](../../courses/stanford-cs224v/markdown/pages/schedule.md).

<a id="concept-outcome-eval"></a>

### Task outcome and state-change verification

`outcome-eval` · Requirements and measurement · original type: topic

Check the actual system state and side effects after an agent acts.

**Aliases:** outcome verification; end-state verification.

**Evidence:** [COL, taught, p. 33](../../courses/columbia-coms4995/markdown/slides/week7.md); [CMU, taught, p. 35](../../courses/cmu-11768/markdown/slides/lecture-07-computer-use-agents.md); [EVAL, taught, p. 42](../../courses/dlai-agentic-evals/markdown/slides/module-4.md); [BOOK, taught, line 33](../../courses/agentic-large-language-models/markdown/chapters/chapter-14-case-study-3-building-a-multi-agent-diagnosis-framework.md).

<a id="concept-harness-optimization"></a>

### Automatic harness improvement

`harness-optimization` · Analysis and improvement · original type: method

Search or revise agent runtime instructions and structure using measured feedback.

**Aliases:** harness search.

**Related terms:** recursive agent harnessing.

**Also relevant to:** [Architectural patterns](architecture.md).

**Evidence:** [S329, taught, p. 110](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [CMU, taught, p. 28](../../courses/cmu-11768/markdown/slides/lecture-20-search-basics.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2610-14224v1.md); [BOOK, taught, line 198](../../courses/agentic-large-language-models/markdown/chapters/chapter-20-advanced-transformer-and-agentic-architectures.md).

<a id="concept-citation-eval"></a>

### Citation and evidence evaluation

`citation-eval` · Requirements and measurement · original type: topic

Check that references exist, support claims, and cover the answer.

**Aliases:** citation accuracy; citation support.

**Evidence:** [CMU, taught, p. 49](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [S224, taught, p. 45](../../courses/stanford-cs224v/markdown/slides/i-sliders.md); [BOOK, taught, line 1050](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-regression-eval"></a>

### Regression and version comparison

`regression-eval` · Analysis and improvement · original type: method

Compare agent versions on shared cases and detect behavior that became worse.

**Aliases:** regression testing; version comparison.

**Evidence:** [CMU, taught, p. 21](../../courses/cmu-11768/markdown/slides/lecture-15-orchestration-and-monitoring.md); [EVAL, taught, p. 42](../../courses/dlai-agentic-evals/markdown/slides/module-5.md).

<a id="concept-session-eval"></a>

### Multi-turn and session evaluation

`session-eval` · Requirements and measurement · original type: topic

Evaluate behavior across conversation turns and preserve relevant earlier constraints.

**Aliases:** session evaluation; multi-turn evaluation.

**Evidence:** [EVAL, taught, p. 29](../../courses/dlai-agentic-evals/markdown/slides/module-4.md); [CU, assigned, p. 2](../../courses/colorado-csci7000/markdown/readings/arxiv-2605-29442.md).

<a id="concept-controlled-eval"></a>

### Controlled improvement experiments

`controlled-eval` · Analysis and improvement · original type: method

Change a defined part of an agent and compare versions under the same test conditions.

**Aliases:** improvement tests; controlled version comparison.

**Evidence:** [EVAL, taught, p. 9](../../courses/dlai-agentic-evals/markdown/slides/module-5.md).

<a id="concept-evaluator-metrics"></a>

### Evaluator precision, recall, and agreement

`evaluator-metrics` · Graders and judge validation · original type: method

Measure evaluator errors and agreement against trusted labels.

**Aliases:** judge precision and recall.

**Related terms:** Cohen kappa.

**Evidence:** [EVAL, taught, p. 34](../../courses/dlai-agentic-evals/markdown/slides/module-3.md).

<a id="concept-memory-eval"></a>

### Memory evaluation

`memory-eval` · Requirements and measurement · original type: topic

Measure recall, updating, temporal reasoning, and useful memory use.

**Aliases:** memory benchmarks.

**Evidence:** [S329, taught, p. 7](../../courses/stanford-cs329z/markdown/slides/lecture07.md).

<a id="concept-production-eval"></a>

### Production monitoring and evaluation feedback

`production-eval` · Analysis and improvement · original type: pattern

Inspect real runs and feedback and turn production failures into test cases.

**Aliases:** production evals.

**Related terms:** data flywheel.

**Evidence:** [EVAL, taught, p. 56](../../courses/dlai-agentic-evals/markdown/slides/module-5.md).

<a id="concept-requirements"></a>

### Requirements and expected behavior

`requirements` · Requirements and measurement · original type: method

Define observable agent behavior and expected outcomes before evaluating a system.

**Aliases:** application requirements; behavior requirements.

**Evidence:** [EVAL, taught, p. 9](../../courses/dlai-agentic-evals/markdown/slides/module-2.md).

<a id="concept-research-methods"></a>

### Research design and paper critique

`research-methods` · Research methods · original type: topic

Form research questions, assess prior work, design experiments, and report evidence.

**Aliases:** paper critique; research project design.

**Evidence:** [CU, taught, line 12](../../courses/colorado-csci7000/markdown/pages/page-researchproject.md).

<a id="concept-research-reproduction"></a>

### Research result reproduction

`research-reproduction` · Research methods · original type: method

Reproduce published claims using source data and executable analysis.

**Aliases:** scientific reproducibility.

**Related terms:** SEER-Repro.

**Also relevant to:** [Application areas](applications.md).

**Evidence:** [S224, taught, p. 42](../../courses/stanford-cs224v/markdown/slides/l-data-driven-deep-research.md); [BOOK, taught, line 157](../../courses/agentic-large-language-models/markdown/chapters/chapter-10-case-study-2-balrog-for-llm-reasoning-and-reflection.md).

<a id="concept-behavioral-experiments"></a>

### Behavioral experiments on agents

`behavioral-experiments` · Research methods · original type: method

Use controlled tasks to measure observable agent behavior.

**Aliases:** experimental agent behavior analysis.

**Also relevant to:** [Agent behavior, human interaction, and interpretability](behavior.md).

**Evidence:** [BOOK, taught, line 49](../../courses/agentic-large-language-models/markdown/chapters/chapter-15-studying-behavior-of-agentic-llms.md).
