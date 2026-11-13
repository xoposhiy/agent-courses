# AOS — Agentic Operating System

AOS takes a goal and completes it by orchestrating research systems and a general-purpose coding
agent inside one **workspace folder**. The folder is the whole state: every input, fetched source,
intermediate result, report, table, script and decision is a file in it. A SQLite catalog
(`workspace.db`) records what each file is, why it exists and which step produced it from which
inputs, and git records every step as a commit that can be inspected or rolled back.

```
goal ─► planner picks a worker ─► worker reads/writes workspace files ─► outputs cataloged ─► commit ─► repeat
```

Workers available today: **STORM** (broad web research), **GRILL** (academic deep research with
source-verified claims), **SLIDERS** (documents to structured tables with evidence), **DataSTORM**
(insight generation over a database), **HistoryGenie** (OCR of scanned documents) and the built-in
**coding agent** (inspect, transform, join, decide, debug, fix adapters). **SatIR** and **VERDICT**
are registered but need licensed ontologies and services that are not set up here.

[PLAN.md](PLAN.md) is the design; [docs/PLAN_COVERAGE.md](docs/PLAN_COVERAGE.md) maps each of its
sections to code and tests.

## Documentation

| document | what it covers |
|---|---|
| [docs/TUTORIAL.md](docs/TUTORIAL.md) | start here: bringing your documents in, adding a database and sources, running the agents, how the planner chooses, making it repeatable, the same from Python |
| [docs/CUSTOM_WORKERS.md](docs/CUSTOM_WORKERS.md) | adding your own workers (in-process or subprocess), loading them with `AOS_WORKERS`, replacing built-in ones |
| [docs/OBSERVABILITY.md](docs/OBSERVABILITY.md) | what is recorded about every run: usage and cost, step logs, the per-call LLM trace and `aos trace` |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | modules, the orchestration loop, how workers and the workspace fit together, cost accounting |
| [docs/CLI.md](docs/CLI.md) | every `aos` command with arguments, examples and exit codes |
| [docs/WORKSPACE.md](docs/WORKSPACE.md) | workspace layout, the catalog schema and useful queries, provenance rules, task records, workflows, git history |
| [docs/WORKERS.md](docs/WORKERS.md) | each worker: inputs, outputs, runner arguments, model adaptations, tuning knobs, adapters in the workspace |
| [docs/WEB_UI.md](docs/WEB_UI.md) | the web interface and its HTTP API |
| [docs/CONFIGURATION.md](docs/CONFIGURATION.md) | `.env` variables, models and the proxy, prices, budget cap, timeouts |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | setup of the external systems, tests, adding a worker, patches, documentation conventions |
| [examples/fabry/README.md](examples/fabry/README.md) | the first use case: which patients have Fabry disease |

## Setup

```bash
uv sync --group dev                 # AOS itself: Python 3.12 virtualenv in .venv (add --group notebook for Jupyter)
cp -n .env.example .env             # then fill in API_KEY, BASE_URL (Gemini via the lab proxy), SERPER_API_KEY
scripts/setup_external.sh all       # clone the systems into external/ and build their virtualenvs
.venv/bin/aos workers               # which workers can run here, and why not
```

Use `cp -n`: it never overwrites an existing `.env`, whereas a plain `cp` replaces your keys with
the placeholders. AOS refuses placeholder keys. GRILL additionally needs the `codex` CLI on PATH
(`npm i -g @openai/codex`). Details and per-system notes in
[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md#setup); every variable in
[docs/CONFIGURATION.md](docs/CONFIGURATION.md).

## Quick start

From the shell:

```bash
aos init workspaces/fabry --goal "Determine which patients have Fabry disease"
cp examples/fabry/patients.csv workspaces/fabry/inputs/
aos run workspaces/fabry "Determine which patients in inputs/patients.csv have Fabry disease. \
  Research the disease, extract its characteristic features as a table, then decide patient by \
  patient with a rationale into generated/decisions/patient_results.json and rationale.md."
aos status workspaces/fabry          # tasks, steps, every file with its provenance
aos log workspaces/fabry             # one commit per step
```

That run chose coding_agent (inspect the records) → storm (research) → sliders (feature tables) →
coding_agent (decisions) on its own and flagged the three synthetic Fabry patients. Steer the planner
by naming workers or paths in the goal, or drive one step at a time with `aos step`.

From the browser:

```bash
aos ui                               # serves ./workspaces at http://127.0.0.1:8765
```

Create a workspace in the switcher, add inputs (upload, drag and drop, or a path on this machine),
and type the goal in the chat. Questions go to a read-only assistant that knows the catalog, the
files and the history; goals start runs whose steps, files and live logs appear as cards.

## Everyday commands

```bash
aos ask workspaces/fabry "Which files were derived from the patient records, and by which step?"
aos trace workspaces/fabry task-001 --step 2 --full   # every LLM call of a step: prompts, replies, tokens, cost
aos query workspaces/fabry "SELECT path, summary FROM files WHERE source='sliders'"
aos describe workspaces/fabry generated/reports/report.md
aos add workspaces/fabry ~/labs.csv --reason "lab results for the same patients"
aos step workspaces/fabry sliders "List the features of X as tables" --inputs generated/reports/report.md --output-dir generated/databases
aos rollback workspaces/fabry <commit>
aos workflow-save workspaces/fabry task-001 fabry && aos workflow-run workspaces/other workflows/fabry.json
```

Full reference in [docs/CLI.md](docs/CLI.md). The same operations from Python:

```python
from aos.api import AOS
aos = AOS.open("workspaces/fabry")
aos.add("~/labs.csv", reason="lab results for the same patients")
task = aos.run("Determine which patients in inputs/patients.csv have Fabry disease ...")
aos.ask("Which files were derived from the patient records?"); aos.query("SELECT path, source FROM files")
```

## How it works, in one paragraph

`aos run` loops: register any new user files, show the planner (Gemini through the proxy) the goal,
the available workers, the workspace listing with provenance and the steps so far, and ask for one
JSON decision. A `run` decision executes the chosen worker, which reads its inputs and writes files;
AOS diffs the workspace to find what was produced, writes a one-sentence summary for each new file
into the catalog with its source, task, step and inputs, and commits. Failed steps stay in the task
record with their error so the planner can retry, send the coding agent to fix the problem (adapter
scripts live in the workspace under `code/adapters/` for exactly this), or roll back. `done` ends
the task. Everything an external system fetches or builds stays in the workspace, including STORM's
archived web pages and GRILL's searches. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Layout

```
aos/
  workspace.py      the workspace: folders, the workspace.db catalog, git checkpoint/history/rollback
  tasks.py          tasks/task-NNN/task.json: goal + sequence of steps with inputs/outputs
  orchestrator.py   the loop: plan, run, register outputs, checkpoint; budget and usage
  coding_agent.py   tool-calling agent (catalog query, list/read/write/replace, shell) inside the workspace
  assistant.py      read-only meta-assistant for questions about a workspace
  ui.py, static/    the web interface: explorer, editor, chat, run log, tasks, history, database tab
  worker.py         Worker interface + run_command for subprocess-based workers
  llm.py            Gemini through the OpenAI-compatible proxy; token and cost accounting
  prompts/          every prompt sent to the model, one .txt file each (planner, summaries, coding agent, assistant, nl2sql)
  trace.py          the per-call LLM trace written into tasks/ (see docs/OBSERVABILITY.md)
  api.py            the Python interface: AOS.create/open, add, step, run, workflow, ask, query, trace, rollback
  cli.py            the `aos` command, a thin layer over api.py
  capabilities/     one thin wrapper per external system + runners/ executed in their virtualenvs; AOS_WORKERS loader
docs/               documentation (see the table above)
examples/fabry/     the first use case (synthetic patients.csv)
examples/workers/   a complete custom worker (glossary.py) to copy from
patches/            source changes applied to STORM and DataSTORM (the FetchArchive hook)
scripts/            setup_external.sh: clone + virtualenv + patch per system
tests/              unit tests (fake LLM) and live tests (AOS_LIVE=1)
external/           cloned systems (git-ignored)
workspaces/         default root for `aos ui` (git-ignored)
```

A workspace:

```
workspace/
  workspace.db                    SQLite catalog: files(path, type, source, agent, task, step, reason, summary, ...) + file_inputs(path, input)
  inputs/  sources/  generated/  workflows/
  code/adapters/run_<system>.py   editable copies of the runner scripts; code/scripts/ for agent-written tools
  tasks/task-001/task.json        + step-NN.log (worker output / coding-agent tool trace) + llm-calls.jsonl (every model call)
  .git
```

## Tests

```bash
.venv/bin/python -m pytest -q                      # 127 unit tests, no network
AOS_LIVE=1 .venv/bin/python -m pytest -q -m live   # 4 live tests against the proxy
```
