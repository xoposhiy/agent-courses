# Category Method

[Category dictionaries](README.md) · [Original extraction method](../METHOD.md) · [Classification data](../taxonomy.json)

## Purpose

This is a classification of the existing 205 canonical concepts. It does not repeat source extraction, add new concepts, or change course frequencies. Each concept has exactly one primary category and one subgroup. Optional related-category links help navigation without duplicating category membership.

The categories describe a concept's role in agent development. They combine practical teaching areas with a distinction between system structure, local techniques, implementation technologies, and applications. This is a working curriculum taxonomy, not a claim that all concepts fit one universal classification.

The original `kind` field remains visible. It describes the concept's original type, such as topic, pattern, method, or application. A category provides an additional classification. For example, context compaction remains a pattern in the source dictionary and belongs to the context and memory category here.

## Categories

1. **Foundations and design concepts:** general model and agent concepts, components, representations, and design choices.
2. **Architectural patterns:** component arrangements, control flow, delegation, and coordination.
3. **Prompting, reasoning, and planning techniques:** instructions, reasoning paths, candidate search, and answer checks.
4. **Context and memory techniques:** active context, stored experience, reusable skills, and conversation state.
5. **Retrieval, data, and knowledge techniques:** indexing, evidence retrieval, queries, extraction, and reconciliation.
6. **Tool-use and action techniques:** tool selection, programmatic tool calls, interpreters, and interface grounding.
7. **Model training and adaptation:** weight updates, training signals, data, and learning systems.
8. **Evaluation, research, and improvement:** requirements, measurements, graders, experiments, and failure analysis.
9. **Safety, security, and trust:** threats, access protections, evidence requirements, and uncertainty policies.
10. **Runtime, deployment, and performance:** storage infrastructure, recovery, service operation, and inference efficiency.
11. **Named tools, frameworks, and protocols:** specific technologies and interoperability standards.
12. **Application areas:** the tasks and domains where agents are used.
13. **Agent behavior, human interaction, and interpretability:** interaction, social behavior, cognitive questions, and internal model mechanisms.

## Boundary decisions

| Concept or distinction | Primary category | Reason |
| --- | --- | --- |
| Orchestrator and workers; agent handoffs | Architectural patterns | These define roles, control, and interaction between components. |
| Plan then execute versus planning | Architecture versus reasoning techniques | A planner-executor split is system structure. Choosing task steps is a reasoning operation. |
| ReAct and CodeAct | Architectural patterns | These define how reasoning and action interact in an agent loop. |
| Multi-agent debate | Architectural patterns | The system uses a defined agent interaction pattern; reasoning and behavior are related categories. |
| Human oversight and approval | Architectural patterns | A human gate changes who authorizes the next action. Safety is a related category. |
| Context isolation and tiered memory | Context and memory techniques | These organize information, even when the source calls them patterns or architectures. |
| Workspace isolation | Architectural patterns | Separate workspaces support coordination between agents. Runtime is a related category. |
| Checkpointing, retries, and state replay | Runtime | These support persistence and recovery rather than define agent-team topology. |
| Generic tool use versus MCP | Tool-use techniques versus named tools and protocols | A capability is different from the standard used to expose it. |
| Generic agent frameworks versus LangGraph | Foundations versus named tools | The general design concept is different from a concrete implementation. |
| Code interpreter versus CodeAct | Tool-use techniques versus architecture | An interpreter is an execution mechanism. CodeAct describes the agent's action interface. |
| Persona and response style control | Prompting techniques | The concept controls identity and response style; it is not a task domain. The original type remains unchanged. |
| Prompt optimization versus model training | Reasoning techniques versus training | Prompt search changes instructions. Training changes weights or learning behavior. |
| Harness improvement versus recursive agents | Evaluation and improvement versus architecture | A measured improvement process differs from the recursive system structure it can produce. |
| Training data selection versus data reconciliation | Training versus knowledge techniques | The first prepares learning examples. The second resolves extracted knowledge records. |
| Tracing and observability | Runtime | Instrumentation produces evidence used by evaluation; evaluation is a related category. |
| Reward hacking | Evaluation and improvement | The concept explains a failure of a reward or scoring objective. Training and safety are related categories. |
| Agentic retrieval | Retrieval techniques | Its main purpose is deciding how to retrieve evidence. Architecture is a related category. |
| RL systems | Model training | These systems coordinate learning. Runtime is a related category. |

The classification does not move children automatically when a parent has a category. For example, a clinical application, its formal reasoning method, and its evaluation can belong to three different categories.

## Frequency rules

A frequency is the number of distinct courses with confirmed taught or assigned evidence, from 0 to 7. The two evidence levels remain separate. Schedule-only entries and the book do not increase course frequency. A zero-frequency entry can have confirmed book evidence.

Rows use the original ranking: course count descending, taught-course count descending, then the English name. A category's course coverage is the union of its concepts' courses. It is never the sum of their course frequencies.

The course-coverage matrix counts distinct confirmed concepts per category and course. It does not measure teaching time, depth, or quality. Broad topics and narrower methods can both appear, so their counts do not form independent measures of content volume.

## Files and rebuilding

`analysis/taxonomy.json` is the reviewed source of category assignments and boundaries. Category CSVs include the original frequency fields plus definitions, aliases, related terms, primary categories, subgroups, and related-category IDs. The structured export is `frequencies.json`. Input hashes are recorded in `inputs.json`.

Run from the project root after rebuilding the original topic analysis:

```powershell
python tools/categorize_topics.py build
python tools/categorize_topics.py validate
```

Validation checks complete and unique membership, valid category and subgroup IDs, unchanged definitions and frequencies, matching CSV exports, course totals, input hashes, local links, and concept anchors. Classification boundaries remain analyst judgments.
