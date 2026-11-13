# Agent behavior, human interaction, and interpretability

Human-agent interaction, social behavior, cognitive questions, and methods for inspecting internal model behavior.

Approval gates belong under architecture. Task success tests belong under evaluation. This category concerns interaction and the behavior or internal mechanisms being studied.

[All categories](README.md) · [CSV](behavior.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**16 concepts**: 7 confirmed in courses; 9 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Personalization and user modeling](#concept-personalization) | topic | 4 | 4 | 0 | S329, CMU, LC, S224 |  | yes |
| [Human-agent collaboration](#concept-human-collaboration) | topic | 4 | 3 | 1 | CMU, LC, S224, CU |  | yes |
| [Work automation and social impact](#concept-work-impact) | topic | 2 | 2 | 0 | CMU, S224 |  |  |
| [Emergent communication and social norms](#concept-emergent-norms) | concept | 1 | 1 | 0 | CMU |  | yes |
| [Proactive and mixed-initiative agents](#concept-proactive) | pattern | 1 | 1 | 0 | S224 | S329 |  |
| [Strategic and social agent behavior](#concept-social-behavior) | topic | 1 | 1 | 0 | CMU |  | yes |
| [Developer-agent alignment](#concept-developer-alignment) | topic | 1 | 0 | 1 | CU |  |  |
| [Activation patching and causal intervention](#concept-activation-patching) | method | 0 | 0 | 0 |  |  | yes |
| [Cognitive analysis of agents](#concept-cognitive-perspectives) | topic | 0 | 0 | 0 |  |  | yes |
| [Consciousness and agency theories](#concept-consciousness) | topic | 0 | 0 | 0 |  |  | yes |
| [Mechanistic interpretability](#concept-interpretability) | topic | 0 | 0 | 0 |  |  | yes |
| [Metacognition and self-knowledge](#concept-metacognition) | topic | 0 | 0 | 0 |  |  | yes |
| [Model circuit analysis](#concept-circuits) | method | 0 | 0 | 0 |  |  | yes |
| [Moral judgment and ethical behavior](#concept-moral-behavior) | topic | 0 | 0 | 0 |  |  | yes |
| [Sparse autoencoders for feature discovery](#concept-sparse-autoencoders) | method | 0 | 0 | 0 |  |  | yes |
| [Theory of mind](#concept-theory-of-mind) | concept | 0 | 0 | 0 |  |  | yes |

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

<a id="concept-personalization"></a>

### Personalization and user modeling

`personalization` · Human-agent interaction · original type: topic

Adapt agent behavior to a user's preferences, history, or needs.

**Aliases:** user modeling; personal agents.

**Evidence:** [S329, taught, p. 11](../../courses/stanford-cs329z/markdown/slides/lecture07.md); [CMU, taught, p. 49](../../courses/cmu-11768/markdown/slides/2026-10-27-zora-wang.md); [LC, taught, line 44](../../courses/langchain-deep-agents/markdown/lessons/m3.3-memory.md); [S224, taught, p. 39](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [BOOK, taught, line 436](../../courses/agentic-large-language-models/markdown/chapters/chapter-09-interaction-styles-for-agentic-llms.md).

<a id="concept-human-collaboration"></a>

### Human-agent collaboration

`human-collaboration` · Human-agent interaction · original type: topic

Design how people and agents share tasks, control, and interaction.

**Aliases:** human agent interaction; human-agent interaction.

**Evidence:** [CMU, taught, p. 48](../../courses/cmu-11768/markdown/slides/2026-10-27-zora-wang.md); [LC, taught, line 604](../../courses/langchain-deep-agents/markdown/lessons/m1.8-hitl.md); [S224, taught, p. 36](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2605-29442.md); [BOOK, taught, line 48](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).

<a id="concept-work-impact"></a>

### Work automation and social impact

`work-impact` · Human-agent interaction · original type: topic

Analyze how agent automation affects tasks, workers, and the design of work.

**Aliases:** future of work; labor impact.

**Evidence:** [CMU, taught, p. 47](../../courses/cmu-11768/markdown/slides/2026-10-27-zora-wang.md); [S224, taught, p. 68](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md).

<a id="concept-emergent-norms"></a>

### Emergent communication and social norms

`emergent-norms` · Social behavior · original type: concept

Study conventions and norms that arise from repeated agent interaction.

**Aliases:** emergent conventions; emergent communication.

**Evidence:** [CMU, taught, p. 33](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [BOOK, taught, line 82](../../courses/agentic-large-language-models/markdown/chapters/chapter-17-emergent-behavior-in-multi-llm-systems.md).

<a id="concept-proactive"></a>

### Proactive and mixed-initiative agents

`proactive` · Human-agent interaction · original type: pattern

Let an agent decide when to initiate useful actions or interaction.

**Aliases:** mixed initiative; proactive agents.

**Also relevant to:** [Architectural patterns](architecture.md).

**Evidence:** [S329, planned, line 87](../../courses/stanford-cs329z/markdown/pages/index.md); [S224, taught, p. 36](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md).

<a id="concept-social-behavior"></a>

### Strategic and social agent behavior

`social-behavior` · Social behavior · original type: topic

Study cooperation, coordination, persuasion, and social interaction among agents.

**Aliases:** strategic interaction.

**Related terms:** social dilemmas.

**Evidence:** [CMU, taught, p. 36](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [BOOK, taught, line 61](../../courses/agentic-large-language-models/markdown/chapters/chapter-15-studying-behavior-of-agentic-llms.md).

<a id="concept-developer-alignment"></a>

### Developer-agent alignment

`developer-alignment` · Human-agent interaction · original type: topic

Analyze whether an agent follows developer intent, constraints, and expected workflows.

**Aliases:** developer-agent misalignment.

**Evidence:** [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2605-29442.md).

<a id="concept-activation-patching"></a>

### Activation patching and causal intervention

`activation-patching` · Mechanistic interpretation · original type: method

Change internal activations to test their causal effect on model output.

**Aliases:** activation patching; causal tracing.

**Evidence:** [BOOK, taught, line 307](../../courses/agentic-large-language-models/markdown/chapters/chapter-21-mechanistic-interpretability-for-llm-agents.md).

<a id="concept-cognitive-perspectives"></a>

### Cognitive analysis of agents

`cognitive-perspectives` · Cognitive questions · original type: topic

Compare behavioral, representational, and mechanistic evidence about agent capabilities.

**Related terms:** cognitive perspectives.

**Evidence:** [BOOK, taught, line 43](../../courses/agentic-large-language-models/markdown/chapters/chapter-22-cognitive-perspectives-on-agentic-llms.md).

<a id="concept-consciousness"></a>

### Consciousness and agency theories

`consciousness` · Cognitive questions · original type: topic

Discuss theories and evidence about consciousness in model-based agents.

**Aliases:** machine consciousness.

**Evidence:** [BOOK, taught, line 23](../../courses/agentic-large-language-models/markdown/chapters/chapter-22-cognitive-perspectives-on-agentic-llms.md).

<a id="concept-interpretability"></a>

### Mechanistic interpretability

`interpretability` · Mechanistic interpretation · original type: topic

Study internal model features and computations that cause behavior.

**Aliases:** mechanistic analysis.

**Evidence:** [BOOK, taught, line 12](../../courses/agentic-large-language-models/markdown/chapters/chapter-21-mechanistic-interpretability-for-llm-agents.md).

<a id="concept-metacognition"></a>

### Metacognition and self-knowledge

`metacognition` · Cognitive questions · original type: topic

Study how agents estimate, monitor, or describe their own knowledge and limits.

**Aliases:** introspection; self-knowledge.

**Evidence:** [BOOK, taught, line 90](../../courses/agentic-large-language-models/markdown/chapters/chapter-22-cognitive-perspectives-on-agentic-llms.md).

<a id="concept-circuits"></a>

### Model circuit analysis

`circuits` · Mechanistic interpretation · original type: method

Identify groups of model components that implement specific computations.

**Aliases:** circuit discovery.

**Related terms:** induction heads.

**Evidence:** [BOOK, taught, line 27](../../courses/agentic-large-language-models/markdown/chapters/chapter-21-mechanistic-interpretability-for-llm-agents.md).

<a id="concept-moral-behavior"></a>

### Moral judgment and ethical behavior

`moral-behavior` · Social behavior · original type: topic

Study moral choices, value alignment, and differences between stated judgments and actions.

**Aliases:** moral judgment; ethical behavior.

**Evidence:** [BOOK, taught, line 467](../../courses/agentic-large-language-models/markdown/chapters/chapter-15-studying-behavior-of-agentic-llms.md).

<a id="concept-sparse-autoencoders"></a>

### Sparse autoencoders for feature discovery

`sparse-autoencoders` · Mechanistic interpretation · original type: method

Learn sparse features from model activations to inspect internal representations.

**Aliases:** SAEs; sparse autoencoders.

**Evidence:** [BOOK, taught, line 26](../../courses/agentic-large-language-models/markdown/chapters/chapter-21-mechanistic-interpretability-for-llm-agents.md).

<a id="concept-theory-of-mind"></a>

### Theory of mind

`theory-of-mind` · Social behavior · original type: concept

Represent or infer another actor's beliefs, goals, or knowledge.

**Aliases:** ToM; social cognition.

**Evidence:** [BOOK, taught, line 20](../../courses/agentic-large-language-models/markdown/chapters/chapter-15-studying-behavior-of-agentic-llms.md).
