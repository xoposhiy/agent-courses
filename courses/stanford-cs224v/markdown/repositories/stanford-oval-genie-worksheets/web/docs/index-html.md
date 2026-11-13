# Project code: stanford-oval/genie-worksheets: web/docs/index.html

[Course index](../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/docs/index.html) · [Raw file](../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/index.html)

Retrieved: 2026-11-13T17:06:24.900930+00:00

# Home

## What is Genie Worksheets?

> TLDR: Framework for creating reliable conversational agents

Genie is a programmable framework for creating task-oriented conversational agents that are designed to handle complex user interactions and knowledge access.
Unlike LLMs, Genie provides reliable grounded responses, with controllable agent policies through its expressive specification, Genie Worksheet.
In contrast to dialog trees, it is resilient to diverse user queries, helpful with knowledge sources, and offers ease of programming policies through its declarative paradigm.

![Genie Worksheets Logo](../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/assets/genie_banner.jpg)

When to use Genie Worksheets?

GenieWorksheets excels at handling complex dialogues where the agent actively provides assistance to the user.

You should use GenieWorksheets if you need:

```
- Task-oriented agents integrated with knowledge - GenieWorksheets uniquely combines both capabilities.

- Mixed-initiative conversations where users can interrupt and switch between tasks seamlessly.

- Precise control over agent responses and behaviors through explicit programming controls.
```

## 🚀 Features

* **High-Level Declarative Specification:** Allows developers to easily define variables and actions for conversations through a spreadsheet-like format, without needing to manually code complex dialogue trees or manage LLM prompts.
* **Integrated Knowledge and Task Handling:** Uniquely combines the ability to handle both structured database queries and API calls in a single conversation flow, letting users seamlessly mix questions with task completion.
* **Reliable State Tracking:** Maintains conversation context through a formal dialogue state representation, reducing hallucinations and repetitive questioning common in pure LLM approaches.
* **Programmable Agent Policies:** Provides fine-grained control over agent behavior through explicit policy definitions, while still maintaining natural conversation flow and handling unexpected user inputs.

## ⚡ Getting Started

* Install the package ([see installation for detailed instructions](../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/installation))
* Define your agent in a python file
* Run your agent using the GenieWorksheets command-line interface or through a web interface

## 🆚 Comparative Analysis

| Feature | Pure LLMs | Dialog Trees | GenieWorksheets |
| --- | --- | --- | --- |
| Handles unexpected queries | ✅ | ❌ | ✅ |
| Reliable output | ❌ | ✅ | ✅ |
| Knowledge integration | ✅ | ❌ | ✅ |
| Natural conversations | ✅ | ❌ | ✅ |
| Control over responses | ❌ | ✅ | ✅ |
| Complex logic support | ❌ | ✅ | ✅ |
| Low hallucination risk | ❌ | ✅ | ✅ |
| Handles interruptions | ✅ | ❌ | ✅ |
| Programmable behaviors | ❌ | ✅ | ✅ |
| Dynamic field dependencies | ❌ | ✅ | ✅ |
| Development speed | ✅ | ❌ | ✅ |

## 📚 Research Paper

GenieWorksheets was introduced in our paper ["Coding Reliable LLM-based Integrated Task and Knowledge Agents with GenieWorksheets"](../../../../readings/arxiv-2407-05674.md). The paper details the design principles, implementation, and evaluation of the framework.

### Citation

If you use GenieWorksheets in your research, please cite our paper:

```
@article{genieworksheets,
  title={Coding Reliable LLM-based Integrated Task and Knowledge Agents with GenieWorksheets},
  author={Joshi, Harshit and Liu, Shicheng and Chen, James and Weigle, Robert and Lam, Monica S},
  journal={arXiv preprint arXiv:2407.05674},
  year={2024}
}
```

Back to top
