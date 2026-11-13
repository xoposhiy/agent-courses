# Homework 2 bundle: vendor/aos/docs/CUSTOM_WORKERS.md

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/docs/CUSTOM_WORKERS.md) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/docs/CUSTOM_WORKERS.md)

Retrieved: 2026-11-13T17:00:50.402745+00:00

# Adding your own workers

A worker is the unit of capability in AOS: something that reads workspace files and instructions and
writes workspace files. The planner chooses among the workers it is offered, so adding a worker is
how you teach AOS a new skill, and replacing one is how you swap a built-in system for your own.

Two kinds exist. An **in-process worker** is a Python class running inside AOS, like the built-in
`coding_agent`. A **subprocess worker** wraps a program with its own environment, like `storm` or
`sliders`. Start with the first; it is a few dozen lines.

## The contract

[aos/worker.py](../aos/worker-py.md):

```python
class Worker:
    name: str = ""           # what the planner writes in its decision and what `aos step` takes
    description: str = ""    # what the planner reads to decide when to use it and how to phrase
                             # instructions, inputs and output_dir: this is the whole contract
    last_usage: dict | None  # optional: tokens/cost of the last run, for subprocess workers

    def available(self) -> tuple[bool, str]:   # (True, "") or (False, "why not")
    def run(self, ws: Workspace, step: Step, log: Path) -> str:   # do the work, return a summary
```

Rules the orchestrator relies on:

- **Read from the workspace, write to the workspace.** `step.inputs` are workspace-relative paths
  that exist; `step.output_dir` is where new files should go. Resolve paths with `ws.abspath(...)`,
  which refuses anything outside the workspace.
- **Do not catalog, do not commit.** AOS diffs the workspace after `run` returns, registers every
  new or changed file with your worker as its source, summarises it and commits. Files that appear
  under `inputs/` during the step are treated as the user's.
- **Fail by raising `StepFailed("why")`.** The message lands in the step record and the planner
  sees it and can retry with different instructions. Any other exception is caught and recorded the
  same way, with its type.
- **Return a one- or two-line summary.** It goes into the step record, the planner's history and
  the UI card.
- **Append diagnostics to `log`.** The step log streams live into the UI.
- `run` may also accept `goal: str` as a keyword argument; the orchestrator passes the task's goal
  when the signature has it (the coding agent uses this).

Costs: a worker that calls the model through the client AOS hands it (`llm`) is costed
automatically, because the orchestrator diffs the client's counters around the step. A worker that
spends money elsewhere sets `self.last_usage = {"model", "calls", "input_tokens", "output_tokens",
"cost_usd"}` before returning (any value may be `None`) and AOS adds it to the step.

## An in-process worker, end to end

examples/workers/glossary.py (source archive omits `../examples/workers/glossary.py`) is a complete worker: it reads the
text files it is given, asks the model for the domain terms they rely on, and writes
`output_dir/glossary.csv`. The essential parts:

```python
from aos.tasks import Step
from aos.worker import StepFailed, Worker
from aos.workspace import Workspace

class Glossary(Worker):
    name = "glossary"
    description = (
        "Builds a glossary of the domain terms used in text documents: instructions = what to focus on "
        "(optional); inputs = the .md/.txt/.csv/.json files or folders to read (required); writes "
        "output_dir/glossary.csv with columns term, definition, source."
    )

    def __init__(self, llm):          # a constructor with an `llm` parameter receives AOS's client
        self.llm = llm

    def run(self, ws: Workspace, step: Step, log: Path) -> str:
        files = [p for i in step.inputs for p in _text_files(ws.abspath(i))]
        if not files:
            raise StepFailed("glossary needs at least one text file in inputs")
        reply = self.llm.complete_json(PROMPT.format(...))      # one JSON-mode call
        out = ws.abspath(step.output_dir) / "glossary.csv"
        ...write the CSV...
        return f"wrote {len(terms)} terms to {ws.relpath(out)}"
```

Run it without changing AOS:

```bash
export AOS_WORKERS=examples/workers/glossary.py:Glossary
aos workers                                   # glossary   available
aos step workspaces/review glossary "genetics terms" --inputs generated/research/fabry/report.md \
    --output-dir generated/glossary
aos run workspaces/review "Build a glossary of the terms in generated/research, then ..."   # the planner can pick it
```

From Python there is no variable to set: `aos.workers["glossary"] = Glossary(aos.llm)` on an
`aos.api.AOS` instance adds it to the planner's menu for that session
([TUTORIAL.md](TUTORIAL-md.md)).

`AOS_WORKERS` is a comma-separated list of `path/to/file.py:Class` or `importable.module:Class`
entries (put it in `.env` to make it permanent). Entries are added after the built-in workers, so an
entry whose `name` matches a built-in one **replaces** it: `AOS_WORKERS=mylab/research.py:MyStorm`
with `name = "storm"` makes the planner use yours. Built-in workers whose system is not installed are
never offered, so on a machine with only AOS and your workers the planner sees `coding_agent` plus
yours.

The `llm` the worker receives is [aos/llm.py](../aos/llm-py.md)'s client: `complete(prompt)`,
`complete_json(prompt)` and `chat(messages, tools=..., json_mode=...)`, all against the configured
model, all counted and traced ([OBSERVABILITY.md](OBSERVABILITY-md.md)). You may of course call any
other library instead; then report `last_usage` yourself if you want it costed.

## Writing the description

The description is documentation the planner reads under time pressure. State, in this order:

1. what the worker does and when to prefer it over `coding_agent` or another worker;
2. what `instructions` should contain;
3. what `inputs` must be (required or ignored; which file types);
4. what comes out and where (file names under `output_dir`);
5. how long it takes, if more than a minute, and any "use a fresh output_dir" rule.

Compare the built-in ones in [WORKERS.md](WORKERS-md.md). Vague descriptions produce vague
instructions; a description that says "inputs are ignored" stops the planner from waiting for files
that will not matter.

## Testing a worker

Unit tests do not need the real model. `tests/conftest.py` has `FakeLLM`, a scripted stand-in
whose replies are strings, dicts (JSON) or lists of tool calls, and a `ws` fixture with a fresh
workspace. Drive your worker through the orchestrator so the bookkeeping is exercised too:

```python
from aos.orchestrator import Orchestrator
from aos.tasks import Step
from conftest import FakeLLM

def test_glossary(ws):
    (ws.root / "inputs" / "notes.md").write_text("GLA variants cause Fabry disease.\n")
    llm = FakeLLM([
        {"inputs/notes.md": "notes"},                              # AOS summarises the input
        {"terms": [{"term": "GLA", "definition": "...", "source": "inputs/notes.md"}]},
        {"generated/glossary.csv": "one term"},                    # AOS summarises the output
    ])
    orch = Orchestrator(ws, llm, {"glossary": Glossary(llm)}, log=lambda _: None)
    task = orch.run_workflow("g", [Step(worker="glossary", instructions="", inputs=["inputs/notes.md"], output_dir="generated")])
    assert task.steps[0]["status"] == "ok" and task.steps[0]["outputs"] == ["generated/glossary.csv"]
    assert ws.describe("generated/glossary.csv")["source"] == "glossary"
```

`tests/test_capabilities.py::test_example_glossary_worker` is this test for the example.

## A subprocess worker

When the capability is a program with its own dependencies (another Python version, torch, a Node
tool), keep it out of AOS's process: a **runner** script executed in the program's environment and a
thin **wrapper** that builds the command line. [aos/capabilities/storm.py](../aos/capabilities/storm-py.md)
and [aos/capabilities/runners/run_storm.py](../aos/capabilities/runners/run_storm-py.md) are the model.

1. **Runner** `run_<system>.py`: takes `--output-dir` and whatever else as arguments, reads
   `API_KEY`, `BASE_URL`, `AOS_MODEL` from the environment, writes its files under the output
   directory, prints progress (it streams into the step log), and leaves a `usage.json`
   (`model`, `calls`, `input_tokens`, `output_tokens`, `cost_usd`) next to its outputs.
2. **Wrapper**: subclass `ExternalCapability` from
   [aos/capabilities/base.py](../aos/capabilities/base-py.md), set `name`, `repo` (the folder under
   `external/` holding the program and its `.venv`), `required_env` and `description`; in `run`,
   call `run_command([self.python, self.runner(ws, "run_<system>.py"), ...], cwd=self.repo_dir,
   log=log, env=self.env(), timeout=...)`, then `self.report_usage(out)`, check the expected
   artifact exists (raise `StepFailed` otherwise) and return a summary. `available()` already
   checks the repo, the virtualenv and the environment variables.
3. **Load it** with `AOS_WORKERS=mylab/wrapper.py:MySystem`, or register it permanently in
   [aos/capabilities/__init__.py](../aos/capabilities/__init__-py.md) and add its setup to
   scripts/setup_external.sh (source archive omits `../scripts/setup_external.sh`) (see
   [DEVELOPMENT.md](DEVELOPMENT-md.md)).

Runners under `aos/capabilities/runners/` are copied into every workspace as `code/adapters/`, and
the wrapper runs the workspace's copy when there is one. That is what lets the coding agent repair a
broken integration mid-task: the fix is a workspace file, committed and reversible. A runner you
keep outside AOS does not get this unless your wrapper's `runner()` points at a workspace copy.

If the program fetches material (web pages, papers), make it save them under the workspace too
(STORM and DataSTORM are patched to archive under `sources/webpages/`). The rule is that nothing an
agent used should exist only outside the workspace.

## Giving the coding agent a tool instead

Sometimes the right unit is not a worker but a tool the coding agent can call from its shell:
a script under `code/scripts/` in the workspace, or a package installed in AOS's virtualenv. The
agent's `run_shell` has `python` with `openai` and `pandas` and the credentials in its environment,
and its instructions can name the script. GRILL's `web_search.py` follows this pattern: a plain
script in the sandbox, never a tool server.
