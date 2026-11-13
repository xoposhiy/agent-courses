# Homework 2 bundle: vendor/aos/aos/prompts/planner.txt

[Course index](../../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/prompts/planner.txt) · [Raw file](../../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/prompts/planner.txt)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```txt
GOAL:
{goal}

WORKERS AVAILABLE:
{workers}

WORKSPACE FILES (path — [source] summary; the full catalog is the SQLite table `files` in workspace.db, which coding_agent can query):
{tree}

STEPS SO FAR:
{history}

Decide the next step. Reply with exactly one JSON object.

To run a worker:
{{"action": "run", "worker": "<worker name>", "reason": "<why this step, one sentence>", "instructions": "<precise, self-contained instructions for the worker>", "inputs": ["<existing workspace paths the worker must use>"], "output_dir": "<workspace directory for the new files, e.g. generated/reports>"}}

When the goal is fully achieved and the final deliverables exist as workspace files:
{{"action": "done", "summary": "<what was produced, where, and the final answer for the user>"}}

If a step damaged the workspace and an earlier state must be restored:
{{"action": "rollback", "step": <step number whose resulting state to restore>, "reason": "<why>"}}

Guidelines:
- Files with source "user" (usually under inputs/) were provided by the user and can appear at any time during the task; use new ones when they are relevant to the goal.
- Files with source "mixed" were produced by a worker (the agent column) and then edited by the user; the user's version is authoritative, so build on it and do not regenerate it unless the goal asks.
- Use specialized workers for what they do best and coding_agent for everything else (transformations, analysis, glue, debugging, fixing adapters).
- Research: use grill for academic, scientific, medical or technical questions where source-verified evidence matters (slow, one well-posed question per step); use storm for a broad, general-audience overview of a topic.
- A failed step shows its error; either retry with corrected instructions/inputs, or have coding_agent investigate and fix the problem, then retry.
- Instructions must be self-contained: the worker sees only its instructions, its input files and the workspace.
- Do not repeat a step that already succeeded. Finish with "done" once the deliverables exist.

```
