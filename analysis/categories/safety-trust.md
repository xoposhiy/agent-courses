# Safety, security, and trust

Risks, protections, evidence requirements, and uncertainty policies that limit harmful or unsupported behavior.

Approval gates belong under architecture because they change control flow. Memory namespaces remain under memory. Direct security and trust requirements belong here.

[All categories](README.md) · [CSV](safety-trust.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**11 concepts**: 11 confirmed in courses; 0 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Agent safety and guardrails](#concept-safety) | topic | 5 | 4 | 1 | COL, CMU, LC, EVAL, CU | S329 | yes |
| [Evidence grounding and hallucination control](#concept-grounding) | topic | 5 | 4 | 1 | COL, CMU, S224, EVAL, CU |  | yes |
| [Sandboxed execution](#concept-sandboxing) | method | 4 | 3 | 1 | COL, CMU, LC, CU | S329 |  |
| [Abstention and uncertainty handling](#concept-abstention) | pattern | 3 | 3 | 0 | COL, CMU, EVAL |  | yes |
| [Privacy and user data protection](#concept-privacy) | topic | 3 | 3 | 0 | COL, CMU, LC | S329 | yes |
| [Prompt injection](#concept-prompt-injection) | concept | 3 | 3 | 0 | COL, CMU, LC | S329 |  |
| [Threat modeling and least privilege](#concept-threat-modeling) | method | 3 | 3 | 0 | COL, CMU, LC |  |  |
| [Red teaming and adversarial evaluation](#concept-red-teaming) | method | 2 | 2 | 0 | COL, CMU |  | yes |
| [Tool authentication and credential handling](#concept-auth) | topic | 2 | 2 | 0 | CMU, LC |  | yes |
| [Decision rationale and data provenance](#concept-provenance) | concept | 1 | 1 | 0 | S224 |  |  |
| [Memory poisoning](#concept-memory-poisoning) | concept | 1 | 1 | 0 | COL |  |  |

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

<a id="concept-safety"></a>

### Agent safety and guardrails

`safety` · Threats and protections · original type: topic

Limit harmful agent actions and enforce task or use constraints.

**Aliases:** agent guardrails; safety guardrails.

**Evidence:** [S329, planned, line 83](../../courses/stanford-cs329z/markdown/pages/index.md); [COL, taught, p. 72](../../courses/columbia-coms4995/markdown/slides/week9.md); [CMU, taught, p. 39](../../courses/cmu-11768/markdown/slides/lecture-13-agent-safety.md); [LC, taught, line 57](../../courses/langchain-deep-agents/markdown/lessons/m1.4-system-prompt.md); [EVAL, taught, p. 13](../../courses/dlai-agentic-evals/markdown/slides/module-4.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2605-30777.md); [BOOK, taught, line 615](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-grounding"></a>

### Evidence grounding and hallucination control

`grounding` · Evidence and uncertainty · original type: topic

Tie claims to trusted evidence and reduce unsupported statements.

**Aliases:** grounded generation; hallucination mitigation.

**Evidence:** [COL, taught, p. 55](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 6](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [S224, taught, p. 32](../../courses/stanford-cs224v/markdown/slides/l-freetext.md); [EVAL, taught, p. 8](../../courses/dlai-agentic-evals/markdown/slides/module-5.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2305-15334.md); [BOOK, taught, line 186](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-sandboxing"></a>

### Sandboxed execution

`sandboxing` · Threats and protections · original type: method

Run code or tools inside a restricted environment.

**Aliases:** sandboxing; execution sandbox.

**Also relevant to:** [Runtime, deployment, and performance](runtime.md).

**Evidence:** [S329, planned, line 83](../../courses/stanford-cs329z/markdown/pages/index.md); [COL, taught, p. 91](../../courses/columbia-coms4995/markdown/slides/week9.md); [CMU, taught, p. 20](../../courses/cmu-11768/markdown/slides/lecture-13-agent-safety.md); [LC, taught, line 100](../../courses/langchain-deep-agents/markdown/lessons/m2.3-sandboxes-and-localshell.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2407-16741.md).

<a id="concept-abstention"></a>

### Abstention and uncertainty handling

`abstention` · Evidence and uncertainty · original type: pattern

Decline to answer or ask for help when evidence or confidence is insufficient.

**Aliases:** I don't know; selective answering.

**Evidence:** [COL, taught, line 70](../../courses/columbia-coms4995/markdown/assignments/hw3.md); [CMU, taught, p. 39](../../courses/cmu-11768/markdown/slides/lecture-18-multi-agent-systems.md); [EVAL, taught, p. 16](../../courses/dlai-agentic-evals/markdown/slides/module-4.md); [BOOK, taught, line 403](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).

<a id="concept-privacy"></a>

### Privacy and user data protection

`privacy` · Threats and protections · original type: topic

Control disclosure and use of private user information.

**Aliases:** privacy risks.

**Evidence:** [S329, planned, line 83](../../courses/stanford-cs329z/markdown/pages/index.md); [COL, taught, line 54](../../courses/columbia-coms4995/markdown/assignments/hw1.md); [CMU, taught, p. 5](../../courses/cmu-11768/markdown/slides/lecture-13-agent-safety.md); [LC, taught, line 115](../../courses/langchain-deep-agents/markdown/lessons/m2.3-sandboxes-and-localshell.md); [BOOK, taught, line 137](../../courses/agentic-large-language-models/markdown/chapters/chapter-13-from-tools-to-assistants-real-world-applications.md).

<a id="concept-prompt-injection"></a>

### Prompt injection

`prompt-injection` · Threats and protections · original type: concept

Untrusted content attempts to redirect an agent or override instructions.

**Aliases:** indirect prompt injection.

**Evidence:** [S329, planned, line 83](../../courses/stanford-cs329z/markdown/pages/index.md); [COL, taught, p. 27](../../courses/columbia-coms4995/markdown/slides/week9.md); [CMU, taught, p. 10](../../courses/cmu-11768/markdown/slides/lecture-13-agent-safety.md); [LC, taught, line 62](../../courses/langchain-deep-agents/markdown/lessons/m5.5-sandbox-async-agent.md).

<a id="concept-threat-modeling"></a>

### Threat modeling and least privilege

`threat-modeling` · Threats and protections · original type: method

Identify threats and limit access to the permissions a task requires.

**Related terms:** threat modeling; least privilege.

**Evidence:** [COL, taught, p. 90](../../courses/columbia-coms4995/markdown/slides/week9.md); [CMU, taught, p. 8](../../courses/cmu-11768/markdown/slides/lecture-13-agent-safety.md); [LC, taught, line 248](../../courses/langchain-deep-agents/markdown/lessons/m2.2-filesystem-backends.md).

<a id="concept-red-teaming"></a>

### Red teaming and adversarial evaluation

`red-teaming` · Threats and protections · original type: method

Test an agent with attacks and difficult misuse cases.

**Aliases:** red teaming; adversarial testing.

**Evidence:** [COL, taught, p. 94](../../courses/columbia-coms4995/markdown/slides/week9.md); [CMU, taught, p. 14](../../courses/cmu-11768/markdown/slides/lecture-13-agent-safety.md); [BOOK, taught, line 281](../../courses/agentic-large-language-models/markdown/chapters/chapter-19-synthetic-data-generation-for-training-agentic-llms.md).

<a id="concept-auth"></a>

### Tool authentication and credential handling

`auth` · Threats and protections · original type: topic

Authenticate tool connections and control how credentials reach tools.

**Related terms:** OAuth; credential brokering.

**Also relevant to:** [Runtime, deployment, and performance](runtime.md); [Named tools, frameworks, and protocols](tools-protocols.md).

**Evidence:** [CMU, taught, p. 44](../../courses/cmu-11768/markdown/slides/lecture-02-tool-use.md); [LC, taught, line 26](../../courses/langchain-deep-agents/markdown/lessons/m1.6-mcp.md); [BOOK, taught, line 305](../../courses/agentic-large-language-models/markdown/chapters/chapter-11-how-agents-use-tools-to-act-in-the-world.md).

<a id="concept-provenance"></a>

### Decision rationale and data provenance

`provenance` · Evidence and uncertainty · original type: concept

Record where facts came from and how evidence and assumptions support a decision.

**Aliases:** data provenance; decision rationale.

**Related terms:** accountability; faithful rationale.

**Also relevant to:** [Retrieval, data, and knowledge techniques](retrieval-knowledge.md).

**Evidence:** [S224, taught, p. 38](../../courses/stanford-cs224v/markdown/slides/l-smt-match.md).

<a id="concept-memory-poisoning"></a>

### Memory poisoning

`memory-poisoning` · Threats and protections · original type: concept

An attacker changes stored memory to affect later agent behavior.

**Evidence:** [COL, taught, p. 31](../../courses/columbia-coms4995/markdown/slides/week9.md).
