# The workspace

A workspace is a folder that holds the entire state of one project: inputs, fetched sources,
generated results, scripts, task records, a SQLite catalog describing every file, and a git
repository recording every step. `aos init` creates one; every other command operates on one.

## Layout

```
workspace/
  workspace.db          SQLite catalog (tables workspace, files, file_inputs)
  inputs/               the user's files: patient records, documents, anything a task starts from
  sources/              material fetched by workers, e.g. sources/webpages/<run>/pages/*.html|txt
  generated/            worker outputs: reports, tables, databases, decisions, plots
  code/
    adapters/           run_<system>.py and web_search.py: editable copies of AOS's runner scripts
    scripts/            tools written by the coding agent
  workflows/            <name>.json saved by `aos workflow-save`
  tasks/
    task-001/
      task.json         the task record (goal, status, steps, usage)
      step-01.log       one log per step: worker output or the coding agent's tool trace
  .git/
```

Folders are created with a `.gitkeep` so they exist in git even when empty. The exact subfolders of
`generated/` and `sources/` are chosen by the planner (`output_dir` in each step) or by you
(`--output-dir` in `aos step`). Workers write only under their step's output directory, except
STORM and DataSTORM, which also archive fetched pages under `sources/webpages/<output dir name>/`.

### Ownership

- `inputs/` belongs to the user. Anything that appears there, at any time, is cataloged with source
  `user`, even if a worker was running at that moment.
- `workspace.db`, `tasks/` and `.git/` are AOS's. The coding agent's write tools and the UI editor
  refuse to touch them.
- Everything else is written by workers and may be edited by the user; see
  [Provenance](#provenance-user-mixed-and-worker-files).

### Hidden directories

Directories whose name starts with a dot (for example SLIDERS' `.sliders/` table store or
DataSTORM's `.domains/` description) are work products too: they are registered in the catalog and
committed to git. GRILL's `grill_run/` has no leading dot and is listed in full. Listings shown to the planner and in `aos status`
collapse each to one line with a file count, and the UI dims them in the explorer.

### What is not a work product

`Workspace.snapshot` skips `.git`, `__pycache__`, `node_modules`, `.pytest_cache`, `.gitkeep`
files, `workspace.db` (and its journal files), a legacy `metadata.json`, and the top-level
`tasks/` directory. Everything else counts as a file a step may have produced.

## The catalog (`workspace.db`)

A SQLite database with three tables, created by the schema in [aos/workspace.py](../aos/workspace.py):

```sql
CREATE TABLE workspace (key TEXT PRIMARY KEY, value TEXT);
-- keys: created, goal, setting.<name> (JSON), e.g. setting.budget_usd

CREATE TABLE files (
    path    TEXT PRIMARY KEY,   -- workspace-relative posix path
    type    TEXT NOT NULL,      -- markdown, csv, json, pdf, python, sqlite, image, ... (from the extension)
    source  TEXT NOT NULL,      -- who produced it: user, aos, coding_agent, storm, grill, sliders, datastorm, historygenie, mixed
    agent   TEXT,               -- the worker that created it (stays put when source becomes "mixed")
    task    TEXT,               -- task-NNN
    step    INTEGER,            -- step number within that task
    reason  TEXT,               -- why the file exists (the step's reason, or the user's --reason)
    summary TEXT,               -- one sentence about the content, written by the model
    tags    TEXT,               -- JSON list, e.g. ["edited-by-user"], ["adapter-sha:1a2b3c4d5e6f"]
    size    INTEGER,            -- bytes at registration
    created TEXT NOT NULL,      -- ISO 8601 UTC; kept across re-registrations
    updated TEXT NOT NULL
);

CREATE TABLE file_inputs (
    path  TEXT NOT NULL REFERENCES files(path) ON DELETE CASCADE,
    input TEXT NOT NULL,        -- a file this one was derived from (the step's inputs)
    PRIMARY KEY (path, input)
);
```

Query it from the shell with `aos query WORKSPACE "SELECT ..."` (SELECT, WITH and EXPLAIN only),
from the UI's database tab, from the coding agent's `query_metadata` tool, or with any SQLite
client. Useful queries:

```sql
-- every file with its provenance (the default of `aos query`)
SELECT path, source, task, step, summary FROM files ORDER BY task, step, path;

-- what the user provided
SELECT path, summary FROM files WHERE source = 'user';

-- everything derived from the patient records
SELECT f.path, f.source FROM files f JOIN file_inputs i ON i.path = f.path
WHERE i.input = 'inputs/patients.csv';

-- files a worker wrote that the user then edited
SELECT path, agent FROM files WHERE source = 'mixed';

-- files under one directory, largest first
SELECT path, size FROM files WHERE path LIKE 'generated/research/%' ORDER BY size DESC;
```

The `tags` column is JSON stored as text; filter it with `LIKE '%"edited-by-user"%'`.

### How rows get there

| event | source | reason | task / step |
|---|---|---|---|
| `aos init`, UI "New workspace" | `aos` | adapter script installed | – |
| file found unregistered before a planning decision, `aos add`, UI upload or `+` | `user` | `Provided by the user ...` or your `--reason` | the task being planned, if any |
| file appeared under `inputs/` while a step ran | `user` | `Provided by the user during task-NNN step N` | that task |
| file written or changed by a step | the worker's name | the step's reason | that task and step; inputs = the step's inputs that exist |
| `aos workflow-save` | `aos` | `Reusable workflow saved from task-NNN` | – |
| a worker's file edited by the user | `mixed` | unchanged | unchanged; tag `edited-by-user` added, summary refreshed |
| file deleted from disk | row removed at the next registration pass | | |

Every row carries a one-sentence `summary` written by the configured model from the first 1,500
characters of the file, in one batched call per step for up to 25 files. Summaries are best effort:
when the call fails, the row gets a generic sentence built from the context and the step continues.

### Provenance: user, mixed and worker files

The planner, the coding agent and the assistant are told the meaning of `source`:

- `user`: provided by the user; may appear at any time during a task, and should be used when
  relevant.
- `<worker>`: produced by that worker in the recorded task and step.
- `mixed`: produced by the worker in `agent`, then changed by the user. The user's version is
  authoritative; workers build on it and do not regenerate it unless asked.
- `aos`: AOS's own files (adapter scripts, saved workflows).

Edits are detected two ways. Saving in the UI editor marks the file immediately. An edit made on
disk with any other tool is noticed before the next planning decision: `git diff --name-only HEAD`
lists changed committed files, those whose source is not `user` are marked `mixed`, and the change
is committed as `User edits before task-NNN step N`.

### Legacy `metadata.json`

Workspaces created by early versions kept the catalog in `metadata.json`. Opening such a workspace
imports it into `workspace.db` and deletes the JSON file.

## Task records

`tasks/task-NNN/task.json`, written by [aos/tasks.py](../aos/tasks.py):

```json
{
  "id": "task-001",
  "goal": "Determine which of the patients in inputs/patients.csv have Fabry disease ...",
  "created": "2026-09-03T20:19:34+00:00",
  "status": "done",
  "pid": 41213,
  "steps": [
    {
      "n": 2,
      "worker": "storm",
      "instructions": "Research Fabry disease: clinical features, diagnostic criteria, genetics ...",
      "reason": "Research Fabry disease ... to establish a reference baseline.",
      "inputs": [],
      "output_dir": "generated/research/fabry_storm",
      "status": "ok",
      "started": "2026-09-03T20:20:01+00:00",
      "finished": "2026-09-03T20:31:48+00:00",
      "outputs": ["generated/research/fabry_storm/report.md", "sources/webpages/fabry_storm/pages/0701ab61177804fa.html", "..."],
      "summary": "STORM wrote generated/research/fabry_storm/report.md (3120 words); ...",
      "error": null,
      "commit": "e2b528d4af1f472ebc97ba538a812cfa02809094",
      "usage": {"calls": 3, "input_tokens": 41200, "output_tokens": 900, "reasoning_tokens": 0, "cost_usd": 0.0146,
                "unpriced_calls": 0, "internal": {"...": "AOS's own calls during the step"}, "external": {"...": "what the runner reported"}},
      "log": "tasks/task-001/step-02.log"
    }
  ],
  "result": "Patients P004, P009 and P012 ...",
  "finished": "2026-09-03T20:58:02+00:00",
  "usage": {"calls": 61, "input_tokens": 1520000, "output_tokens": 48000, "reasoning_tokens": 21000, "cost_usd": 0.58,
            "unpriced_calls": 0, "internal": {"...": "..."}, "external": {"...": "..."}}
}
```

Task status is one of `running`, `done`, `failed` (the planner could not decide, or a workflow step
failed), `stopped` (step limit or budget cap) or `interrupted` (the process died; set by the UI
server when it finds a `running` task whose pid is gone). Step status is `running`, `ok` or
`failed`. A rollback decision is recorded as a step whose worker is `rollback`.

Step logs (`step-NN.log`) start with a header (worker, reason, inputs, output_dir) followed by the
runner's command line and its live output, or, for the coding agent, every tool call with a
truncated result and the final summary.

`llm-calls.jsonl` in the same folder records every model request AOS made for the task (planner
decisions, catalog summaries, the coding agent's and other in-process workers' calls): one JSON line
per call with its step, purpose, messages, reply, tokens, cost and latency. Calls made outside a task
(the assistant, the UI's natural-language SQL, summaries for uploads) go to `tasks/llm-calls.jsonl`.
Read them with `aos trace`; format in [OBSERVABILITY.md](OBSERVABILITY.md).

## Workflows

`aos workflow-save WORKSPACE task-NNN NAME` writes the task's successful steps (rollbacks excluded)
to `workflows/NAME.json`:

```json
{
  "name": "fabry",
  "goal": "Determine which patients have Fabry disease ...",
  "steps": [
    {"worker": "storm", "instructions": "...", "reason": "...", "inputs": [], "output_dir": "generated/reports"},
    {"worker": "sliders", "instructions": "...", "reason": "...", "inputs": ["generated/reports/report.md"], "output_dir": "generated/databases"},
    {"worker": "coding_agent", "instructions": "...", "reason": "...", "inputs": ["inputs/patients.csv", "generated/databases/tables"], "output_dir": "generated/decisions"}
  ]
}
```

`aos workflow-run WORKSPACE path/to/NAME.json` replays the steps in order in any workspace, without
the planner, stopping at the first failure. The file may live inside or outside the workspace; edit
it by hand to change instructions or paths.

## Git history

Commit messages follow fixed patterns, so `aos log` reads as a timeline:

| message | when |
|---|---|
| `Initialize workspace` | `aos init` |
| `Install adapter scripts` | `aos init`, UI "New workspace" |
| `task-NNN: start` | a run or workflow begins |
| `task-NNN: checkpoint before step N` | the tree was dirty when a step was about to run |
| `User edits before task-NNN step N` | hand edits to worker files were detected |
| `task-NNN step N: <worker> (<ok/failed>) - <reason>` | after every step |
| `task-NNN: done` / `failed` / `stopped` | the run ends |
| `Add <paths>` | `aos add`, UI upload or add-path |
| `Edit <path>` | the UI editor saved a worker's file |
| `Save workflow <name>` | `aos workflow-save` |
| `Checkpoint before rollback` then `Rollback workspace to <sha>` | `aos rollback`, the planner's rollback action, UI history click |

The repository is a plain git repository with user `AOS <aos@localhost>`; `git -C WORKSPACE diff`,
`git log -p` and every other git command work as usual.
