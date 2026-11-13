# Prompting, reasoning, and planning techniques

Ways to guide a model, generate candidates, search reasoning paths, check answers, or improve instructions.

Local reasoning operations belong here. A planner-executor split belongs under architecture; factual grounding policy belongs under safety and trust.

[All categories](README.md) · [CSV](reasoning-techniques.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**19 concepts**: 19 confirmed in courses; 0 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Prompt design](#concept-prompting) | topic | 7 | 6 | 1 | S329, COL, CMU, LC, S224, EVAL, CU |  | yes |
| [Structured output and constrained decoding](#concept-structured-output) | method | 6 | 6 | 0 | S329, COL, CMU, LC, S224, EVAL |  |  |
| [Planning and task decomposition](#concept-planning) | topic | 6 | 5 | 1 | S329, COL, CMU, LC, S224, CU |  | yes |
| [Reflection and self-correction](#concept-reflection) | pattern | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| [Answer verification](#concept-verification) | pattern | 4 | 3 | 1 | COL, CMU, S224, CU |  | yes |
| [Chain of thought](#concept-cot) | pattern | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| [Multi-step reasoning](#concept-reasoning) | topic | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| [Reflexion](#concept-reflexion) | method | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| [Self-consistency](#concept-self-consistency) | pattern | 4 | 3 | 1 | S329, COL, CMU, CU |  | yes |
| [Decoding and sampling](#concept-decoding) | topic | 3 | 3 | 0 | S329, COL, EVAL |  |  |
| [Few-shot prompting](#concept-few-shot) | method | 3 | 3 | 0 | S329, COL, CMU |  | yes |
| [Beam search](#concept-beam-search) | method | 2 | 2 | 0 | S329, COL |  |  |
| [Inference-time scaling](#concept-inference-scaling) | method | 2 | 2 | 0 | S329, CMU |  | yes |
| [Persona and response style control](#concept-persona) | application | 2 | 2 | 0 | COL, LC |  | yes |
| [Automatic prompt optimization](#concept-prompt-optimization) | method | 1 | 1 | 0 | S329 |  | yes |
| [Best-of-N selection](#concept-best-of-n) | pattern | 1 | 1 | 0 | CMU |  |  |
| [Formal reasoning with SMT](#concept-smt) | method | 1 | 1 | 0 | S224 |  |  |
| [Soft prompt tuning](#concept-soft-prompts) | method | 1 | 1 | 0 | COL |  |  |
| [Tree of thoughts](#concept-tree-thoughts) | pattern | 1 | 1 | 0 | COL |  | yes |

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

<a id="concept-prompting"></a>

### Prompt design

`prompting` · Prompting and output control · original type: topic

Design instructions, examples, and role messages to guide a model.

**Aliases:** prompt engineering; prompting.

**Evidence:** [S329, taught, p. 160](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, p. 6](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 44](../../courses/cmu-11768/markdown/slides/lecture-03-long-context.md); [LC, taught, line 48](../../courses/langchain-deep-agents/markdown/lessons/m1.4-system-prompt.md); [S224, taught, p. 2](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md); [EVAL, taught, p. 27](../../courses/dlai-agentic-evals/markdown/slides/module-5.md); [CU, assigned, p. 4](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-11432.md); [BOOK, taught, line 104](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-structured-output"></a>

### Structured output and constrained decoding

`structured-output` · Prompting and output control · original type: method

Constrain model output to a schema or a set of valid tokens.

**Aliases:** structured I/O; constrained generation.

**Evidence:** [S329, taught, p. 153](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, line 68](../../courses/columbia-coms4995/markdown/assignments/hw2.md); [CMU, taught, p. 26](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [LC, taught, line 86](../../courses/langchain-deep-agents/markdown/lessons/m1.5-tools.md); [S224, taught, p. 2](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw2.md); [EVAL, taught, p. 27](../../courses/dlai-agentic-evals/markdown/slides/module-3.md).

<a id="concept-planning"></a>

### Planning and task decomposition

`planning` · Planning and candidate search · original type: topic

Choose and organize steps or subtasks before or during action.

**Aliases:** task planning; task decomposition.

**Evidence:** [S329, taught, p. 47](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 54](../../courses/columbia-coms4995/markdown/slides/week6.md); [CMU, taught, p. 5](../../courses/cmu-11768/markdown/slides/lecture-05-planning.md); [LC, taught, line 41](../../courses/langchain-deep-agents/markdown/lessons/m4.1-delegation.md); [S224, taught, p. 23](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [CU, assigned, p. 2](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-11432.md); [BOOK, taught, line 377](../../courses/agentic-large-language-models/markdown/chapters/chapter-07-vision-action-and-world-models.md).

<a id="concept-reflection"></a>

### Reflection and self-correction

`reflection` · Reasoning and verification · original type: pattern

Use feedback about an attempt to revise reasoning or future actions.

**Aliases:** self-reflection; self correction.

**Evidence:** [S329, taught, p. 40](../../courses/stanford-cs329z/markdown/slides/lecture01.md); [COL, taught, p. 33](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 38](../../courses/cmu-11768/markdown/slides/lecture-04-memory-and-skills.md); [S224, taught, p. 34](../../courses/stanford-cs224v/markdown/slides/l-freetext.md); [CU, assigned, p. 4](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-11432.md); [BOOK, taught, line 330](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-verification"></a>

### Answer verification

`verification` · Reasoning and verification · original type: pattern

Check claims or candidate answers before accepting a result.

**Aliases:** self-verification.

**Related terms:** chain of verification.

**Evidence:** [COL, taught, p. 34](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 10](../../courses/cmu-11768/markdown/slides/lecture-20-search-basics.md); [S224, taught, p. 32](../../courses/stanford-cs224v/markdown/slides/l-freetext.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2305-14325.md); [BOOK, taught, line 276](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-cot"></a>

### Chain of thought

`cot` · Reasoning and verification · original type: pattern

Generate intermediate reasoning steps before a final answer.

**Aliases:** CoT; chain-of-thought.

**Evidence:** [S329, taught, p. 37](../../courses/stanford-cs329z/markdown/slides/lecture01.md); [COL, taught, p. 27](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 8](../../courses/cmu-11768/markdown/slides/lecture-05-planning.md); [CU, assigned, p. 8](../../courses/colorado-csci7000/markdown/readings/arxiv-2409-02977.md); [BOOK, taught, line 169](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-reasoning"></a>

### Multi-step reasoning

`reasoning` · Reasoning and verification · original type: topic

Use intermediate reasoning steps to solve a task.

**Aliases:** LLM reasoning.

**Evidence:** [S329, taught, p. 33](../../courses/stanford-cs329z/markdown/slides/lecture01.md); [COL, taught, p. 24](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 24](../../courses/cmu-11768/markdown/slides/lecture-05-planning.md); [CU, assigned, p. 4](../../courses/colorado-csci7000/markdown/readings/arxiv-2308-11432.md); [BOOK, taught, line 29](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-reflexion"></a>

### Reflexion

`reflexion` · Reasoning and verification · original type: method

Store verbal feedback from earlier attempts to improve later attempts.

**Evidence:** [S329, taught, p. 37](../../courses/stanford-cs329z/markdown/slides/lecture06.md); [COL, taught, p. 33](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 19](../../courses/cmu-11768/markdown/slides/lecture-04-memory-and-skills.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2303-11366.md); [BOOK, taught, line 491](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-self-consistency"></a>

### Self-consistency

`self-consistency` · Reasoning and verification · original type: pattern

Sample several reasoning paths and combine their answers.

**Aliases:** self consistency.

**Evidence:** [S329, taught, p. 38](../../courses/stanford-cs329z/markdown/slides/lecture01.md); [COL, taught, p. 30](../../courses/columbia-coms4995/markdown/slides/week4.md); [CMU, taught, p. 13](../../courses/cmu-11768/markdown/slides/lecture-20-search-basics.md); [CU, assigned, p. 8](../../courses/colorado-csci7000/markdown/readings/arxiv-2409-02977.md); [BOOK, taught, line 254](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-decoding"></a>

### Decoding and sampling

`decoding` · Planning and candidate search · original type: topic

Choose output tokens from model probabilities.

**Aliases:** token sampling; generation strategies.

**Evidence:** [S329, taught, p. 20](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, p. 48](../../courses/columbia-coms4995/markdown/slides/week3.md); [EVAL, taught, p. 34](../../courses/dlai-agentic-evals/markdown/slides/module-5.md).

<a id="concept-few-shot"></a>

### Few-shot prompting

`few-shot` · Prompting and output control · original type: method

Include examples in a prompt to guide the response.

**Aliases:** fewshot prompting; in-context examples.

**Evidence:** [S329, taught, p. 14](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [COL, taught, line 65](../../courses/columbia-coms4995/markdown/assignments/hw2.md); [CMU, taught, p. 20](../../courses/cmu-11768/markdown/slides/lecture-04-memory-and-skills.md); [BOOK, taught, line 46](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-beam-search"></a>

### Beam search

`beam-search` · Planning and candidate search · original type: method

Keep several high-scoring partial outputs during decoding.

**Evidence:** [S329, taught, p. 21](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [COL, taught, p. 44](../../courses/columbia-coms4995/markdown/slides/week3.md).

<a id="concept-inference-scaling"></a>

### Inference-time scaling

`inference-scaling` · Planning and candidate search · original type: method

Spend more inference compute on reasoning, search, or repeated attempts.

**Aliases:** test-time scaling; test time compute.

**Evidence:** [S329, taught, p. 138](../../courses/stanford-cs329z/markdown/slides/lecture02.md); [CMU, taught, p. 1](../../courses/cmu-11768/markdown/slides/lecture-20-search-basics.md); [BOOK, taught, line 21](../../courses/agentic-large-language-models/markdown/chapters/chapter-04-scaling-laws-and-efficient-large-language-models.md).

<a id="concept-persona"></a>

### Persona and response style control

`persona` · Prompting and output control · original type: application

Make an agent follow a defined identity and style while preserving factual constraints.

**Aliases:** persona agents; style control.

**Also relevant to:** [Application areas](applications.md); [Agent behavior, human interaction, and interpretability](behavior.md).

**Evidence:** [COL, taught, line 56](../../courses/columbia-coms4995/markdown/assignments/hw3.md); [LC, taught, line 55](../../courses/langchain-deep-agents/markdown/lessons/m1.4-system-prompt.md); [BOOK, taught, line 177](../../courses/agentic-large-language-models/markdown/chapters/chapter-16-role-based-interaction-in-multi-llm-systems.md).

<a id="concept-prompt-optimization"></a>

### Automatic prompt optimization

`prompt-optimization` · Prompting and output control · original type: method

Use measured feedback to search for better instructions or examples.

**Aliases:** context optimization; instruction optimization.

**Evidence:** [S329, taught, p. 23](../../courses/stanford-cs329z/markdown/slides/lecture09.md); [BOOK, taught, line 432](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).

<a id="concept-best-of-n"></a>

### Best-of-N selection

`best-of-n` · Planning and candidate search · original type: pattern

Generate several candidates and select one with a verifier or reward score.

**Aliases:** best of n; candidate selection.

**Evidence:** [CMU, taught, p. 8](../../courses/cmu-11768/markdown/slides/lecture-20-search-basics.md).

<a id="concept-smt"></a>

### Formal reasoning with SMT

`smt` · Reasoning and verification · original type: method

Translate constraints to logic and use a satisfiability-modulo-theories solver.

**Aliases:** satisfiability modulo theories.

**Related terms:** MaxSMT.

**Also relevant to:** [Retrieval, data, and knowledge techniques](retrieval-knowledge.md).

**Evidence:** [S224, taught, p. 39](../../courses/stanford-cs224v/markdown/slides/l-smt-match.md).

<a id="concept-soft-prompts"></a>

### Soft prompt tuning

`soft-prompts` · Prompting and output control · original type: method

Learn prompt embeddings while keeping the main model weights fixed.

**Aliases:** soft prompting; prompt tuning.

**Evidence:** [COL, taught, p. 15](../../courses/columbia-coms4995/markdown/slides/week4.md).

<a id="concept-tree-thoughts"></a>

### Tree of thoughts

`tree-thoughts` · Reasoning and verification · original type: pattern

Search a branching set of intermediate reasoning states.

**Aliases:** ToT; tree-of-thoughts.

**Evidence:** [COL, taught, p. 31](../../courses/columbia-coms4995/markdown/slides/week4.md); [BOOK, taught, line 445](../../courses/agentic-large-language-models/markdown/chapters/chapter-06-multi-step-reasoning-in-llms.md).
