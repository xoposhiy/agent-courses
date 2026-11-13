# PLAN.md coverage

How each section of `PLAN.md` is implemented and how it is verified. Unit tests run with
`.venv/bin/python -m pytest -q` (127 tests, no network); live tests with `AOS_LIVE=1` (4 tests
against the Gemini proxy). The first use case was run end to end with `aos run`; the resulting
workspace is described under section 7. `tests/test_plan_coverage.py` checks that every PLAN.md
section has an entry here and that every file this document references exists.

## Goal

Requirement: a user gives AOS a goal; AOS decides which capability or coding agent performs the
next step, with which workspace files, producing which outputs; everything happens in a workspace
folder; keep it filesystem-first and simple.

Implementation: `aos/cli.py` (the `aos` command: init, run, step, status, describe, log, rollback,
workflow-save, workflow-run, workers) and `aos/orchestrator.py` (the decide-run-register-commit loop).

Verified by: `tests/test_orchestrator.py` (the full loop with a scripted planner and a fake worker),
the live test `test_live_end_to_end_with_coding_agent`, and the first use case (section 7).

## 1. Workspace as the Core Operating System

Requirement: every task runs inside a workspace directory with inputs/, sources/, generated/,
tasks/, code/ and workflows/; anything an agent inspects, produces or hands on lives inside it;
no important hidden state elsewhere; downloaded papers, databases, scripts and notes all land there.

Implementation:
- `aos/workspace.py`: `Workspace.create` makes the folders; `relpath` rejects any path outside the
  workspace, so every registration and every coding-agent tool call is confined.
- `aos/coding_agent.py`: list/read/write/replace/shell tools resolve paths through the workspace and
  refuse to touch AOS's own records.
- Capability runners write only under the step's output directory: `aos/capabilities/runners/run_storm.py`,
  `aos/capabilities/runners/run_sliders.py`, `aos/capabilities/runners/run_datastorm.py`,
  `aos/capabilities/runners/run_historygenie.py`, `aos/capabilities/runners/run_grill.py`.
- Fetched sources are files too: `patches/storm-fetch-archive.patch` and
  `patches/datastorm-fetch-archive.patch` add a `FetchArchive` hook to those systems so every search
  hit and downloaded page is saved under sources/webpages/ in the workspace; SLIDERS keeps its table
  store next to its outputs; GRILL's whole run directory is kept.

Verified by: `tests/test_workspace.py` (folder creation, path confinement), `tests/test_coding_agent.py`
(escape attempts and protected files are refused), `tests/test_capabilities.py` (the sources
directory is passed to the runner), and the live STORM smoke run, which archived 7 search hits,
5 raw pages and 3 extracted page texts.

## 2. Workspace Metadata

Requirement: for every meaningful file record path, type, source, reason, summary, task, agent,
input files, creation time and tags; one lightweight JSON file; easy for humans and agents to
inspect; given any file, AOS can say what it is, why it exists, where it came from.

Implementation: `aos/workspace.py` keeps the catalog in the SQLite file workspace.db: table
files(path, type, source, agent, task, step, reason, summary, tags, size, created, updated) and
link table file_inputs(path, input), with `register`, `describe`, `files`, `unregistered`,
`prune_metadata` and read-only `query`; `aos/orchestrator.py` (`register_inputs` registers
user-provided files, `run_step` discovers a step's outputs by diffing snapshots and registers each
with the worker, reason, task, step, inputs and an LLM one-sentence summary); `aos query`,
`aos describe`, `aos status` and `aos add` (catalog a new user file mid-task) in `aos/cli.py`; the
coding agent's `query_metadata` tool in `aos/coding_agent.py`. Files the user drops in during a
task are registered as source user before every planning decision. Workspaces from earlier
versions with a metadata.json are migrated on open.

Verified by: `tests/test_workspace.py` (`test_register_and_describe`, `test_prune_metadata_drops_deleted_files`,
`test_query_is_read_only_and_joins_inputs`, `test_legacy_metadata_json_is_migrated`),
`tests/test_orchestrator.py` (`test_full_loop_registers_inputs_outputs_and_checkpoints` asserts the
recorded source, reason, task, step, inputs and summary), `tests/test_cli.py` (describe,
`test_query_prints_the_catalog`, `test_add_copies_catalogs_and_commits`), `tests/test_coding_agent.py`
(`test_agent_can_query_the_catalog`), `tests/test_orchestrator.py`
(`test_files_dropped_into_inputs_mid_step_belong_to_the_user`,
`test_files_dropped_between_decisions_are_registered_before_the_next_one`),
and the first use case: 145 of 145 workspace files registered.

## 3. Git as the Workspace History Mechanism

Requirement: every workspace is a git repository; commits before and after meaningful steps;
inspect, diff and roll back; coding-agent changes and adapter fixes are covered; a bad fix can be
reverted.

Implementation: `aos/workspace.py` (`git`, `checkpoint`, `history`, `rollback`; rollback restores
files and metadata as a new commit and keeps the task records); `aos/orchestrator.py` checkpoints
before a step when the tree is dirty and after every step, and executes the planner's rollback
action; `aos log` and `aos rollback` in `aos/cli.py`; `aos init` copies the runner scripts into the
workspace as code/adapters/ (`install_adapters` in `aos/capabilities/base.py`) and the wrappers run
that copy, so an agent's fix to an adapter is versioned like everything else.

Verified by: `tests/test_workspace.py` (`test_checkpoint_commits_only_when_something_changed`,
`test_rollback_restores_files_and_metadata_but_keeps_task_records`), `tests/test_orchestrator.py`
(one commit per step, `test_rollback_action_restores_earlier_state`), `tests/test_cli.py` (rollback,
init installs adapters), `tests/test_capabilities.py` (`test_wrappers_prefer_the_workspace_adapter_copy`).

## 4. Agents and Capabilities

Requirement: thin wrappers for SatIR, SLIDERS, VERDICT, STORM, DataSTORM, GRILL and HistoryGenie
that take instructions and workspace paths, run the capability, know when it finishes and discover
the files it produced; capabilities never call each other; coding agents are first-class workers
that inspect, transform, connect, debug and fix inside the workspace.

Implementation:
- `aos/worker.py`: the `Worker` interface (`available`, `run`) and `run_command`, which runs a
  subprocess, tees its output into the step log and raises `StepFailed` on error.
- `aos/capabilities/base.py`: repo and virtualenv discovery under external/, environment for the
  runner, adapter installation.
- Wrappers: `aos/capabilities/grill.py`, `aos/capabilities/storm.py`, `aos/capabilities/sliders.py`,
  `aos/capabilities/datastorm.py`, `aos/capabilities/historygenie.py`; `aos/capabilities/forma.py`
  registers SatIR and VERDICT and reports why they cannot run (licensed ontologies, Elasticsearch and
  Snowstorm services, compiled build artifacts). `aos/capabilities/__init__.py` is the registry.
- `aos/coding_agent.py`: the coding agent; `scripts/setup_external.sh`: clone, virtualenv and patch
  per system.
- `aos/assistant.py`: the meta-assistant the plan lists among coding-agent uses, a read-only agent
  over the catalog, files, task records and commits (`aos ask`); `aos/ui.py` with
  `aos/static/index.html`: the web interface to view the workspace, run goals and chat with it
  (`aos ui`).

Verified by: `tests/test_capabilities.py` (availability reasons, command lines, output discovery,
failure when nothing is produced), `tests/test_runners.py` (runner helpers), `tests/test_coding_agent.py`
(tool loop, errors returned to the model, turn limit), `tests/test_assistant.py` (read-only tools,
conversation memory), `tests/test_ui.py` (page, state, query, file, upload, assistant and a
background run through the HTTP endpoints), the live test `test_live_coding_agent_writes_a_file`,
and live smoke runs of every runner: STORM (report plus archived sources), SLIDERS (4 tables with
evidence), DataSTORM (report over a SQLite cohort), HistoryGenie (exact transcription of a scanned
record), GRILL (4,000-word report with 106 evidence items).

## 5. Orchestration

Requirement: inspect the workspace, determine the next step, select files, choose a capability or
the coding agent, execute, inspect outputs, update metadata, checkpoint, repeat; modules communicate
only through files.

Implementation: `aos/orchestrator.py`: `decide` shows the planner the goal, the available workers
with what each expects and produces, the workspace listing with provenance, and the steps so far, and
asks for one JSON decision (run, done, rollback), re-asking with the validation error when it is
invalid; `run_step` runs the worker, diffs the workspace, summarizes and registers outputs and
commits; failures are recorded with the error so the next decision can retry or delegate a fix.

Verified by: `tests/test_orchestrator.py` (`test_full_loop_registers_inputs_outputs_and_checkpoints`,
`test_failed_step_is_recorded_and_planner_can_retry`, `test_invalid_decisions_are_rejected_and_reasked`,
`test_done_without_summary_is_reasked`, `test_planner_failure_marks_task_failed`,
`test_step_limit_stops_the_loop`, `test_unavailable_worker_fails_the_step_not_the_run`) and the live
end-to-end test.

## 6. Tasks and Reusable Workflows

Requirement: a lightweight record of what happened for each task (steps with inputs and outputs);
workflows as simple step sequences that can be saved and reused.

Implementation: `aos/tasks.py` (tasks/task-NNN/task.json with goal, status, steps, per-step log);
`aos workflow-save` writes a task's successful steps to workflows/<name>.json and `aos workflow-run`
replays them without the planner (`aos/cli.py`, `Orchestrator.run_workflow` in `aos/orchestrator.py`).

Verified by: `tests/test_tasks.py`, `tests/test_orchestrator.py` (`test_run_workflow_replays_steps_without_planner`),
`tests/test_cli.py` (`test_workflow_save`).

## 7. First Use Case

Requirement: a rare disease and patient records; research the disease, extract structured
characteristics, decide patient by patient; the workspace ends up holding the report, the feature
tables, the decisions with rationale and metadata, all under git.

Implementation: `examples/fabry/patients.csv` (twelve synthetic records, three describing Fabry
disease: P004, P009, P012) and `examples/fabry/README.md` (the commands).

Verified by: three live `aos run` executions, the last on the final code. The planner chose
coding_agent (inspect the records), storm (research), sliders (feature tables), coding_agent
(decisions with rationale), then declared done. Results of the final run:

| check | result |
|---|---|
| decisions | P004, P009, P012 flagged, all others not |
| files registered in metadata | 145 of 145 |
| archived web sources | 108 files under sources/webpages/ |
| commits | 11 (init, adapters, start, before/after each step, done) |

Deliverables in that workspace: the STORM report and sources under generated/research/, SLIDERS
tables and evidence under generated/research/, patient_results.json and rationale.md under
generated/decisions/, one log per step under tasks/task-001/.

## 8. Engineering Principles

- Filesystem first: every input, output, source, cache and log is a file in the workspace.
- Git first: history, checkpoints and rollback are plain git (`aos/workspace.py`).
- Metadata, not machinery: one SQLite table with a flat per-file record, queried with plain SQL.
- Loose coupling: AOS never imports the systems' code; each runs as a subprocess in its own
  virtualenv and communicates through files and arguments.
- Coding agents are first-class: the coding agent is a worker like any capability and covered the
  decision step that SatIR and VERDICT could not.
- AOS owns orchestration: capabilities do not know what ran before or after them.
- Keep it simple: seven modules, argparse, subprocesses, JSON files, git.
