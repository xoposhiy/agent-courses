# Command line reference

The `aos` command is installed into `.venv/bin/` by `uv sync`. Run it as `.venv/bin/aos` or
activate the virtualenv. Every command except `ui` and `workers` takes a workspace path as its first
argument. Credentials come from `AOS/.env` (see [CONFIGURATION.md](CONFIGURATION.md)).

Every command is a thin wrapper over [aos/api.py](../aos/api.py)'s `AOS` class, which does the same
things from Python ([TUTORIAL.md](TUTORIAL.md#10-the-same-thing-from-python)).

Exit codes: `0` success; `1` a usage or workspace error (message on stderr, e.g. the path is not a
workspace); `2` the run, step or workflow ended in any state other than `done`/`ok`.

## Creating and running

### `aos init WORKSPACE [--goal TEXT]`

Create the folder if needed, the standard subfolders, `workspace.db` (with the goal), a git
repository, and copy the runner scripts into `code/adapters/`. Two commits: `Initialize workspace`
and `Install adapter scripts`. Safe to run on an existing workspace.

### `aos run WORKSPACE GOAL [--max-steps N] [--model NAME]`

Pursue a goal with the planner: decide a step, run it, register outputs, commit, repeat until the
planner says done. Progress lines print to stdout. Defaults: 12 steps, the model in `AOS_MODEL`.
Prints the task id, status and result at the end. See
[ARCHITECTURE.md](ARCHITECTURE.md#the-orchestration-loop) for what happens in the loop.

```bash
aos run workspaces/fabry "Determine which patients in inputs/patients.csv have Fabry disease. \
  Research the disease, extract its features as a table, then decide patient by patient into \
  generated/decisions/patient_results.json and rationale.md."
```

Steer the planner by naming workers or paths in the goal ("use grill for the research", "write the
table to generated/databases/features.csv").

### `aos step WORKSPACE WORKER INSTRUCTIONS [--inputs PATH ...] [--output-dir DIR] [--reason TEXT] [--model NAME]`

Run one step with a worker you choose, without the planner. AOS still does the bookkeeping: a new
task (`manual step: ...`), output discovery, catalog rows, a commit. Prints the step record as JSON.
`--output-dir` defaults to `generated`.

```bash
aos step workspaces/fabry storm "Fabry disease: genetics, clinical features, diagnosis, treatment" \
  --output-dir generated/reports
aos step workspaces/fabry sliders "List the clinical features and diagnostic criteria as tables" \
  --inputs generated/reports/report.md --output-dir generated/databases
aos step workspaces/fabry coding_agent "Decide for each patient in inputs/patients.csv ..." \
  --inputs inputs/patients.csv generated/databases/tables --output-dir generated/decisions
```

### `aos workflow-save WORKSPACE TASK_ID NAME`

Write the successful steps of a task to `workflows/NAME.json`, catalog it and commit. Format in
[WORKSPACE.md](WORKSPACE.md#workflows).

### `aos workflow-run WORKSPACE WORKFLOW.json [--model NAME]`

Replay a saved workflow's steps in order, no planner, stopping at the first failure. The JSON file
may be inside or outside the workspace.

### `aos add WORKSPACE FILE ... [--reason TEXT]`

Give the workspace new input files. A file outside the workspace is copied into `inputs/`; a file
already inside is cataloged in place. Each is registered with source `user`, your reason and a
model-written summary, then committed. Plain `cp` into `inputs/` works too: the files are registered
before the next planning decision.

## Inspecting

### `aos status WORKSPACE`

Goal, HEAD, every task with its steps (status, worker, reason), and the workspace listing with each
file's source and summary (large directories collapsed).

### `aos query WORKSPACE [SQL] [--json]`

Run a read-only query against `workspace.db` and print an aligned table (or JSON). Without SQL:
`SELECT path, source, task, step, summary FROM files ORDER BY task, step, path`. Only `SELECT`,
`WITH` and `EXPLAIN` statements are accepted. Schema and examples in
[WORKSPACE.md](WORKSPACE.md#the-catalog-workspacedb).

```bash
aos query workspaces/fabry "SELECT path, summary FROM files WHERE source='sliders'"
aos query workspaces/fabry "SELECT f.path FROM files f JOIN file_inputs i ON i.path=f.path WHERE i.input='inputs/patients.csv'" --json
```

### `aos describe WORKSPACE PATH`

Print the catalog row of one file as JSON (type, source, agent, task, step, reason, summary, tags,
size, timestamps, inputs). Exit 1 if the file has no row.

### `aos log WORKSPACE [-n N]`

The last N (default 20) commits: short sha, date, message. One commit per step; see the message
patterns in [WORKSPACE.md](WORKSPACE.md#git-history).

### `aos ask WORKSPACE QUESTION [--model NAME]`

Ask the read-only meta-assistant about the workspace: what files exist and why, what each task did,
what the history shows, what to run next. It queries the catalog, reads files and the task records,
and never modifies anything.

```bash
aos ask workspaces/fabry "Which files were derived from the patient records, and by which step?"
```

### `aos trace WORKSPACE [TASK] [--step N] [--full] [--json]`

Show the LLM calls recorded for the workspace: one line per call with time, task, step, purpose
(`planner`, `summary`, a worker's name, `assistant`, `nl2sql`), model, message count, input and
output tokens, estimated cost, latency and the start of the reply (or the tool calls it requested, or
the error). `TASK` (`task-NNN`) restricts it to one task, `--step N` to one step; without a task,
every task's calls plus the calls made outside tasks are listed in time order. `--full` also prints
each call's messages and reply, which reads as a transcript of the step. `--json` prints the raw
records. Record format and analysis examples in [OBSERVABILITY.md](OBSERVABILITY.md).

```bash
aos trace workspaces/fabry task-001
aos trace workspaces/fabry task-001 --step 3 --full
aos trace workspaces/fabry --json | jq 'select(.error)'
```

### `aos workers`

List every registered worker and whether it can run on this machine, with the reason when it
cannot (missing repo or virtualenv, missing environment variable, `codex` not on PATH, FORMA build
artifacts absent). Works without a configured LLM (prints a warning instead). Workers named in
`AOS_WORKERS` are included ([CUSTOM_WORKERS.md](CUSTOM_WORKERS.md)).

## Undoing

### `aos rollback WORKSPACE REF`

Restore files and the catalog to the state at commit `REF` as a new commit. The current state is
committed first, and the task records under `tasks/` are kept, so nothing is lost. `REF` is any git
revision: a sha from `aos log`, `HEAD~2`, and so on.

## The web interface

### `aos ui [PATH] [--host HOST] [--port PORT] [--max-steps N] [--model NAME]`

Serve the web interface at `http://127.0.0.1:8765` by default. `PATH` (default `./workspaces`,
created if missing) is a folder of workspaces, or a single workspace, in which case its parent
becomes the root and it is preselected. Ctrl-C stops the server. Details in [WEB_UI.md](WEB_UI.md).

Restart the server after updating AOS: the page is read from disk on each load, but the server keeps
the code it started with, and the page shows a banner when it is newer than the server.

## `--model`

`run`, `step`, `workflow-run`, `ask` and `ui` accept `--model NAME` to override `AOS_MODEL` for that
invocation. The name is passed to the external systems too (as `AOS_MODEL` in their environment).
