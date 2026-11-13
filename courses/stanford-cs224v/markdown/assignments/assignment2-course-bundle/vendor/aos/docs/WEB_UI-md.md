# Homework 2 bundle: vendor/aos/docs/WEB_UI.md

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/docs/WEB_UI.md) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/docs/WEB_UI.md)

Retrieved: 2026-11-13T17:00:50.402745+00:00

# Web interface

`aos ui [PATH]` serves a single-page interface for a folder of workspaces. It is standard library
only ([aos/ui.py](../aos/ui-py.md): `ThreadingHTTPServer` and JSON endpoints;
[aos/static/index.html](../aos/static/index-html.md): one HTML file, no build step). Default address
`http://127.0.0.1:8765`.

```bash
aos ui                      # ./workspaces (created if missing)
aos ui ~/projects           # another folder of workspaces
aos ui workspaces/fabry     # one workspace; its parent becomes the root and it is preselected
aos ui --host 0.0.0.0 --port 9000
```

There is no authentication. Keep the default loopback host unless the network is trusted.

## The page

Laid out like an editor:

- **Workspace switcher** (title bar): every workspace under the root, plus "New workspace" (name,
  optional goal). Each workspace has its own chat, run state and log; one run at a time per
  workspace.
- **Explorer** (left): the workspace folder as a tree. The dot on each file is its source (user,
  storm, sliders, grill, coding_agent, aos, mixed); hovering shows the catalog summary; hidden
  (dot-directory) folders are dimmed. Buttons: `+` creates a file (a name field appears in the tree
  and an empty editable tab opens), upload puts files into `inputs/`, the folder button copies a
  file or folder from a path on the server's machine, and files dropped onto the explorer are
  uploaded to `inputs/`.
- **Editor** (center): clicking a file opens it with a provenance strip (source, task and step,
  derived-from files). Text files are editable with line numbers and highlighting; Markdown opens
  as a rendered preview with Source and Edit modes; CSV opens as a table with an Edit mode. Save or
  Ctrl+S writes the file, catalogs it and commits. Files above `AOS_MAX_FILE_CHARS` load partially
  with a "load the whole file" link. Editing a worker's file keeps its provenance and marks it
  `mixed` with the tag `edited-by-user`.
- **Database tab**: opening `workspace.db` shows each table with columns, row count and first rows,
  a SQL box for read-only SELECT queries (Ctrl+Enter), and a plain-English box: the model turns the
  question into SQLite, the SQL appears in the box for editing and the result below.
- **Chat** (front page): one box for both kinds of input. A goal starts a run; its card shows each
  step with worker, duration, produced files (click to open), usage and result, and the live tail of
  the running step's log. A question goes to the read-only assistant. Auto mode treats text that
  ends with `?` or starts with a question word (what, why, how, which, list, show, ...) as a
  question and everything else as a goal; the Run and Ask buttons force either. Runs from before the
  server started appear as earlier cards.
- **Run log** panel at the bottom while a goal runs (toggle with "log" in the status bar).
- **Tasks tab** (activity bar): every task with its steps (click a step to open its log; the latest
  log line shows under a running step) and the git history (click a commit to roll the workspace
  back to it, as a new commit; refused while a run is in progress).
- **Search tab**: filter files by path or catalog summary.
- **Settings** (gear): workers available, the model dropdown, and the budget cap.
- **Status bar**: HEAD, file count, estimated spend (spent / cap when a cap is set, amber at 80%)
  and the model dropdown. The light/dark toggle sits on the activity bar; the choice is remembered
  per browser.

The page compares its `API_VERSION` with the server's on every state poll and shows a banner asking
for a restart when the page is newer than the running server.

## HTTP API

All endpoints return JSON. Workspace-scoped endpoints take `?ws=NAME`; without it the server uses the
preselected workspace, or the first one alphabetically. Errors: `400` with `{"error": ...}` for bad
input or workspace errors, `409` when a run is already in progress, the budget cap is reached, or a
rollback is attempted during a run, `404` for unknown routes.

### Server-wide

| method | path | body / params | returns |
|---|---|---|---|
| GET | `/` | | the page |
| GET | `/api/workspaces` | | `{root, default, workspaces: [{name, path, goal, tasks, files, last_task, running, updated}]}` |
| POST | `/api/workspaces` | `{name, goal?}` | creates a workspace (folders, catalog, git, adapters) and returns its info |
| GET | `/api/models` | | `{models, current}` as the proxy lists them |
| POST | `/api/models` | `{model}` | switches the model for every later call in this server |

### Per workspace (`?ws=NAME`)

| method | path | body / params | returns |
|---|---|---|---|
| GET | `/api/state` | | goal, head, model, file count, prices, cost summary, budget, workers, every task with steps and usage, recent history, current run |
| GET | `/api/tree` | | the folder as a nested tree; each file with `source`, `summary`, `task`, `step`, `size` |
| GET | `/api/file` | `path`, `full=1` | `{path, entry, size, binary, text, truncated, limit}` |
| GET | `/api/tail` | `path`, `lines` (≤200) | the last lines of a text file (for running step logs) |
| GET | `/api/query` | `sql` | `{rows}` of a read-only catalog query |
| GET | `/api/db` | | catalog overview: tables, columns, counts, first rows, the db's own catalog row |
| POST | `/api/sql` | `{sql}` | `{sql, columns, rows (≤500), total, truncated}` |
| POST | `/api/nl2sql` | `{question}` | the generated `sql`, its result or `error`, and `usage` |
| GET | `/api/run` | | `{run}`: the current or last run (goal, status, log lines, task id, result) |
| POST | `/api/run` | `{goal, max_steps?}` | starts a run in a background thread; `409` if one is running or the cap is reached |
| POST | `/api/message` | `{message, mode: auto\|run\|ask}` | `{kind: "run", run}` or `{kind: "ask", reply}` |
| POST | `/api/assistant` | `{message}` | `{reply}` from the assistant |
| GET | `/api/assistant` | | the assistant's conversation so far (this server session) |
| GET | `/api/thread` | | the chat as this server saw it: goals with their runs, questions with replies, rollbacks |
| POST | `/api/add` | `?name=FILE&reason=...`, raw bytes body | saves `inputs/FILE`, catalogs, commits; returns the catalog row |
| POST | `/api/add-path` | `{path, reason?}` | copies a file or folder from the server's machine into `inputs/`; `{added, count}` |
| POST | `/api/write` | `{path, content, reason?}` | writes a text file (not `workspace.db`, `tasks/`, `.git/`), catalogs, commits; returns the row |
| POST | `/api/rollback` | `{ref}` | `{head}` after restoring the workspace to `ref` as a new commit |
| GET | `/api/settings` | | `{budget_usd, spent_usd}` |
| POST | `/api/settings` | `{budget_usd}` (number, or empty to clear) | `{budget_usd, spent_usd}` |

Example:

```bash
curl -s 'http://127.0.0.1:8765/api/state?ws=fabry' | python3 -m json.tool | head -30
curl -s -X POST 'http://127.0.0.1:8765/api/message?ws=fabry' \
  -d '{"message": "Which files were derived from inputs/patients.csv?", "mode": "ask"}'
curl -s -X POST 'http://127.0.0.1:8765/api/add?ws=fabry&name=labs.csv&reason=lab%20results' --data-binary @labs.csv
```

## Behaviour worth knowing

- **One run per workspace.** Runs execute in a daemon thread of the server process; the page polls
  `/api/state` and `/api/tail`. Closing the browser does not stop a run; stopping the server does.
- **Interrupted runs.** When a workspace is first opened by the server, tasks still marked `running`
  whose recorded pid no longer exists are marked `interrupted` (their running step `failed`). A run
  in progress from another process, such as the CLI, is left alone.
- **Session usage.** Assistant answers, natural-language SQL and the summaries written for uploads
  and edits are AOS calls outside any task; the server counts them as session usage and adds them to
  the workspace's estimated spend for the budget check.
- **Model switching** changes `AOS_MODEL` in the server's environment, so external runners started
  afterwards use the new model as well.
- **Restart after updating AOS.** The HTML is re-read on every load but the Python code is not.
