# Architecture

AOS is a small Python package (about 3,500 lines) that turns a goal into a sequence of steps, each
performed by a *worker* inside a git-versioned *workspace* folder. There is no message bus, no
database server and no framework: files are the interface between workers, SQLite is the catalog,
git is the history, and subprocesses run the external research systems.

```
                    ┌──────────────────────────────────────────────┐
  aos run / aos ui  │  Orchestrator (aos/orchestrator.py)          │
  goal ──────────►  │  loop: inspect → decide → run → register →   │
                    │        checkpoint → repeat                   │
                    └───────┬──────────────────────┬───────────────┘
                            │ planner prompt        │ Step(worker, instructions, inputs, output_dir)
                            ▼                       ▼
                    ┌──────────────┐        ┌────────────────────────────────────────┐
                    │ LLM (llm.py) │        │ Workers (worker.py, capabilities/)      │
                    │ Gemini via   │        │  coding_agent   in-process tool loop    │
                    │ OpenAI proxy │        │  storm, grill, sliders, datastorm,      │
                    └──────────────┘        │  historygenie   subprocess runners     │
                                            │  satir, verdict  registered, unavailable│
                                            └───────────────┬────────────────────────┘
                                                            │ reads / writes files
                                                            ▼
                    ┌──────────────────────────────────────────────────────────────┐
                    │ Workspace (workspace.py)                                     │
                    │  inputs/ sources/ generated/ code/ workflows/  ← work files  │
                    │  workspace.db   SQLite catalog: files + file_inputs          │
                    │  tasks/task-NNN/task.json + step-NN.log + llm-calls.jsonl    │
                    │  .git           one commit per step                          │
                    └──────────────────────────────────────────────────────────────┘
```

## Modules

| module | responsibility |
|---|---|
| [aos/workspace.py](../aos/workspace.py) | The `Workspace` class: standard folders, path confinement (`relpath` rejects anything outside the root), the SQLite catalog (`register`, `describe`, `files`, `query`, `schema`, `prune_metadata`, `mark_edited`), file discovery (`snapshot`, `changed_since`, `unregistered`, `tree`), per-workspace settings, and git (`checkpoint`, `history`, `rollback`, `modified`). |
| [aos/tasks.py](../aos/tasks.py) | `Step` (one unit of work) and `Task` (goal + ordered step records persisted as `tasks/task-NNN/task.json`), plus `mark_interrupted` for runs whose process died. |
| [aos/orchestrator.py](../aos/orchestrator.py) | The loop. `run` (planner-driven), `run_workflow` (replay without the planner), `run_step`, `decide`, `register_inputs`, `summarize_files`, budget enforcement and cost accounting. |
| [aos/worker.py](../aos/worker.py) | The `Worker` interface, `StepFailed`, `run_command` (subprocess with live log tee, timeout and process-group kill) and `read_usage` (a runner's `usage.json`). |
| [aos/llm.py](../aos/llm.py) | `LLM`: chat, JSON mode and tool calling against the OpenAI-compatible proxy; token and cost accounting (per thread, so concurrent UI activity is costed separately); `parse_json` for tolerant JSON extraction; price table and `.env` loading. |
| [aos/prompts/](../aos/prompts/) | Every prompt AOS sends, one text file each (planner system and decision prompts, catalog summaries, coding agent, assistant, natural-language SQL), loaded with `prompts.load(name)`. Edit the files to change behaviour. |
| [aos/trace.py](../aos/trace.py) | The LLM call trace: a per-thread context (task, step, purpose, file) that `LLM.chat` records every request and reply into, as JSON lines under `tasks/`. See [OBSERVABILITY.md](OBSERVABILITY.md). |
| [aos/coding_agent.py](../aos/coding_agent.py) | The built-in general-purpose worker: a tool-calling loop with `query_metadata`, `list_files`, `read_file`, `write_file`, `replace_in_file` and `run_shell`, confined to the workspace. |
| [aos/assistant.py](../aos/assistant.py) | The read-only meta-assistant (`aos ask` and the UI chat): the coding agent's read tools plus a `history` tool over tasks and commits. |
| [aos/capabilities/](../aos/capabilities/) | One thin wrapper per external system, the shared `ExternalCapability` base, the worker registry (built-in workers plus those named in `AOS_WORKERS`), and `runners/` (the scripts executed inside each system's virtualenv). See [WORKERS.md](WORKERS.md) and [CUSTOM_WORKERS.md](CUSTOM_WORKERS.md). |
| [aos/ui.py](../aos/ui.py) + [aos/static/index.html](../aos/static/index.html) | A standard-library HTTP server and a single-page interface. See [WEB_UI.md](WEB_UI.md). |
| [aos/api.py](../aos/api.py) | `AOS`: the Python interface. Holds a workspace, the model client, the workers and the budget wiring; `create`/`open`, `add`, `step`, `run`, `workflow`, `save_workflow`, `ask`, `query`, `describe`, `trace`, `rollback`. See [TUTORIAL.md](TUTORIAL.md#10-the-same-thing-from-python). |
| [aos/cli.py](../aos/cli.py) | The `aos` command (argparse), a thin layer over `AOS`. See [CLI.md](CLI.md). |

Nothing in `aos/` imports the external systems' code. Each system runs as a subprocess with its own
virtualenv, and communicates only through command-line arguments, environment variables and files.

## The orchestration loop

`Orchestrator.run(goal)` in [aos/orchestrator.py](../aos/orchestrator.py):

1. **Create the task** (`tasks/task-NNN/task.json`, status `running`, with the pid of this process).
2. **Register inputs**: any file in the workspace without a catalog row is recorded with source
   `user`; rows for deleted files are dropped; worker-produced files whose content differs from the
   last commit are marked `mixed` (edited by the user) and committed.
3. **Checkpoint** (`task-NNN: start`).
4. **Loop** until `done`, failure, the step limit (`--max-steps`, default 12) or the budget cap:
   1. `register_inputs` again, so files dropped in since the last decision are visible.
   2. `decide`: build the planner prompt (goal, available workers with their descriptions, the
      workspace listing with provenance, the steps so far) and ask the model for one JSON decision
      in JSON mode. Decisions are validated (known worker, non-empty instructions, inputs exist,
      output_dir inside the workspace, rollback target is a completed step). An invalid reply is
      sent back with the error, up to three times; after that the task fails.
   3. `run`: `run_step` (below). `done`: record the summary and stop. `rollback`: restore the
      workspace to the commit after the named step, as a new commit, and record it as a step with
      worker `rollback`.
5. **Record usage** (AOS's own calls plus what the external systems reported) and checkpoint
   (`task-NNN: done|failed|stopped`).

`run_step(task, step)`:

1. If the worker is an external capability, make sure the workspace's adapter copies under
   `code/adapters/` exist and are current (see [WORKERS.md](WORKERS.md#adapters-in-the-workspace)).
2. If the tree is dirty, commit (`checkpoint before step N`), so the step's diff is clean.
3. Append the step record (status `running`) and open `tasks/task-NNN/step-NN.log`.
4. Take a snapshot of every work-product file (path → mtime and size).
5. Run the worker. Unknown or unavailable workers, `StepFailed` and any other exception become a
   failed step with the error text; the run continues and the planner sees the error.
6. Diff the workspace against the snapshot. Files that appeared under `inputs/` are the user's and
   are registered as such; everything else is the step's output.
7. Summarize the outputs (one LLM call for up to 25 visible files, best effort) and register each
   with `source=<worker>`, the step's reason, task, step number and the step's existing inputs as
   `file_inputs`.
8. Drop catalog rows for files the step deleted, attach usage, commit
   (`task-NNN step N: <worker> (<status>) - <reason>`), and store the commit sha in the step record.

Step logs are written line by line while the worker runs, which is what the UI tails.

## Workers

A worker is anything with a `name`, a `description` the planner can read, `available()` and
`run(ws, step, log)` (see [aos/worker.py](../aos/worker.py)). It reads its instructions and its input
files, writes files under `step.output_dir` (or wherever the instructions say), appends diagnostics to
the step log, and returns a one-paragraph summary. It does not register files or commit: the
orchestrator discovers outputs by diffing the workspace.

Two kinds exist:

- **The coding agent** runs in-process: a loop of model calls with tool results appended, up to 40
  turns, then a forced summary. Its tools resolve every path through the workspace and refuse to
  write `workspace.db`, `tasks/` or `.git/`. Shell commands run with the workspace root as working
  directory and the AOS virtualenv's `bin/` first on `PATH`.
- **External capabilities** subclass `ExternalCapability`: they know their repo folder under
  `external/`, the extra environment variables they need, and build one command line
  `external/<repo>/.venv/bin/python code/adapters/run_<system>.py --... ` executed with
  `run_command`. On success they check the expected artifact exists (for example `report.md`) and
  pick up `usage.json`.

## Files as the interface

The workspace is the only shared state. Three mechanisms keep it honest:

- **Path confinement**: `Workspace.relpath` resolves symlinks and rejects any path outside the
  root, and every registration, tool call and planner `output_dir` goes through it.
- **Snapshot diffing**: outputs are whatever changed on disk, so a worker cannot produce hidden
  state that AOS misses; caches and stores in dot-directories are registered too (as hidden files,
  collapsed to one line in listings).
- **Provenance in the catalog**: each row records `source`, `agent`, `task`, `step`, `reason`,
  `summary` and derived-from links. The planner sees this as its workspace listing; the coding agent
  and the assistant query it with SQL. See [WORKSPACE.md](WORKSPACE.md#the-catalog-workspacedb).

## Git as history

Every meaningful transition is a commit made by `Workspace.checkpoint`, which stages everything and
commits only when something changed. `rollback(ref)` first commits the current state
(`Checkpoint before rollback`), then resets the tree to `ref` with `git read-tree -u --reset`,
restores `tasks/` from the pre-rollback commit so the audit trail survives, and commits the result.
Nothing is ever rewritten: a rollback is a new commit and the abandoned state stays reachable.

## Cost accounting

`LLM` records prompt, completion and reasoning tokens of every call and prices them with the table
in `AOS_PRICES` (defaults in [aos/llm.py](../aos/llm.py)). Snapshots of that counter around a step
give the step's internal usage. Each runner writes a `usage.json` in its output directory
(`model`, `calls`, `input_tokens`, `output_tokens`, `cost_usd`), which the wrapper reads and the
orchestrator prices if the runner did not. Per-step and per-task totals are stored in the task
record; the UI adds the session's assistant and summary calls. A per-workspace budget cap (stored in
the catalog's `workspace` table) stops a run between steps once the estimate reaches it. Behind the
totals, every individual request and reply is recorded in the task's `llm-calls.jsonl`
([OBSERVABILITY.md](OBSERVABILITY.md)).

## Design constraints

From [PLAN.md](../PLAN.md), and kept deliberately:

- Filesystem first, git first, one flat SQLite table for metadata.
- Workers never call each other; only AOS sequences them.
- The coding agent is a peer of the specialized systems, not a fallback of last resort.
- No workflow language: a workflow is a JSON list of steps replayed in order.
- Standard library wherever possible: argparse, sqlite3, subprocess, http.server. The only runtime
  dependencies are `openai`, `pandas` and `python-dotenv`.
