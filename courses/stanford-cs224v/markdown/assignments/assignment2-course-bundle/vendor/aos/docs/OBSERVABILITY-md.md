# Homework 2 bundle: vendor/aos/docs/OBSERVABILITY.md

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/docs/OBSERVABILITY.md) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/docs/OBSERVABILITY.md)

Retrieved: 2026-11-13T17:00:50.402745+00:00

# Observability: what AOS records about every run

Everything AOS observes is written into the workspace, next to the work it describes, and committed
with it. There are three layers, from coarse to fine.

| layer | where | what |
|---|---|---|
| **usage and cost** | `tasks/task-NNN/task.json` (`usage` on each step and on the task); UI status bar and cards | calls, input/output/reasoning tokens, estimated USD, unpriced calls; split into AOS's own calls (`internal`) and what external runners reported (`external`) |
| **step logs** | `tasks/task-NNN/step-NN.log` | the runner's command line and its complete output as it ran, or the coding agent's every tool call with a truncated result and its final summary |
| **LLM call trace** | `tasks/task-NNN/llm-calls.jsonl`; `tasks/llm-calls.jsonl` for calls outside tasks | one record per model request: when, how long, which task/step/purpose, the model, the messages sent, the reply or error, tokens and cost |

The first two are described in [WORKSPACE.md](WORKSPACE-md.md) and
[ARCHITECTURE.md](ARCHITECTURE-md.md). This page is about the trace.

## The LLM call trace

[aos/llm.py](../aos/llm-py.md) records every `chat` call it makes through [aos/trace.py](../aos/trace-py.md).
The orchestrator opens a trace context per task, so calls made while a task runs land in that
task's folder, tagged with the step number and what the call was for; the assistant, the UI's
natural-language SQL and the summaries written for uploads record into the workspace-level file.
Contexts are per thread, so a run in the UI's background thread and a question answered at the same
time never mix.

One record (pretty-printed; the file has one JSON object per line):

```json
{
  "time": "2026-10-04T04:11:14+00:00",
  "duration_ms": 1840,
  "task": "task-001",
  "step": 1,
  "worker": "coding_agent",
  "purpose": "coding_agent",
  "model": "gemini-3.6-flash",
  "json_mode": false,
  "tools": ["query_metadata", "list_files", "read_file", "write_file", "replace_in_file", "run_shell"],
  "messages": 4,
  "continues": true,
  "new_messages": [
    {"role": "assistant", "content": null, "tool_calls": [{"id": "call_0", "type": "function", "function": {"name": "read_file", "arguments": "{\"path\": \"inputs/labs.csv\"}"}}]},
    {"role": "tool", "tool_call_id": "call_0", "content": "[inputs/labs.csv: lines 1-12 of 12]\nid,test,value\n..."}
  ],
  "response": {"content": null, "tool_calls": [{"name": "write_file", "arguments": "{\"path\": ...}"}], "finish_reason": "tool_calls"},
  "usage": {"input_tokens": 2310, "output_tokens": 96, "reasoning_tokens": 40, "cost_usd": 0.000933},
  "error": null
}
```

Fields:

- `task`, `step`, `worker`: where the call happened. Planning and output summaries between steps
  have no `step`.
- `purpose`: `planner` (a decision), `summary` (catalog summaries of new files), the worker's name
  (calls the worker made, e.g. `coding_agent`), `assistant`, `nl2sql`.
- `messages`: how many messages were sent. `continues` is true when the call extends the previous
  call's conversation in the same thread, in which case `new_messages` holds only the messages added
  since (the model's last reply and the tool results, typically). Reading a step's records in order
  therefore gives the whole conversation once, without repetition. The first call of a conversation
  carries all its messages, system prompt included.
- `response`: the reply text, the tool calls it requested, and `finish_reason`. `error` is set
  instead when the request failed (the exception type and message); the step then shows the same
  error.
- `usage`: this call's tokens and its estimated cost from the price table (`cost_usd` is null for a
  model without a price).
- Texts longer than 50,000 characters are cut with a marker; nothing else is abbreviated.

### Reading the trace

```bash
aos trace workspaces/review                     # every call in every task, plus calls outside tasks
aos trace workspaces/review task-003            # one task
aos trace workspaces/review task-003 --step 2 --full   # the prompts and replies of one step
aos trace workspaces/review --json | jq ...     # the raw records
```

The table view:

```
#  time      task      step  purpose       model             msgs  in    out  cost      ms    reply
1  04:11:14  task-001  -     summary       gemini-3.6-flash  1     2310  96   0.000933  1840  {"inputs/patients.csv": "Patient records."}
2  04:11:14  task-001  -     planner       gemini-3.6-flash  2     2310  96   0.000933  1840  {"action": "run", "worker": "coding_agent", ...
3  04:11:14  task-001  1     coding_agent  gemini-3.6-flash  2     2310  96   0.000933  1840  read_file
4  04:11:14  task-001  1     summary       gemini-3.6-flash  1     2310  96   0.000933  1840  {"generated/report.md": "The report."}
5  04:11:14  task-001  -     planner       gemini-3.6-flash  2     2310  96   0.000933  1840  {"action": "done", "summary": "Report written ..."}
```

`reply` shows the requested tool calls when there are any, else the start of the reply text, else
the error. `--full` prints each call's new messages and its reply in order, which reads as a
transcript of the step.

In the web interface the trace files appear under `tasks/` in the explorer and open as text; the
step cards and the status bar show the aggregated cost.

### Analysing it

The files are plain JSON lines, so the usual tools apply:

```bash
# cost per purpose in a task
jq -s 'group_by(.purpose) | map({purpose: .[0].purpose, calls: length, usd: (map(.usage.cost_usd // 0) | add)})' \
   workspaces/review/tasks/task-003/llm-calls.jsonl

# the slowest calls across the workspace
cat workspaces/review/tasks/*/llm-calls.jsonl | jq -c '{ms: .duration_ms, step, purpose}' | sort -t: -k2 -n -r | head

# every failed request
cat workspaces/review/tasks/*/llm-calls.jsonl workspaces/review/tasks/llm-calls.jsonl | jq -c 'select(.error) | {time, task, step, error}'
```

Or in Python with `aos.trace.read(path)`, or load the lines into pandas or SQLite. The coding agent
can do this inside the workspace too: ask it to "read tasks/task-003/llm-calls.jsonl and report
which calls cost most".

### What the external systems record themselves

Subprocess workers run outside AOS's process, so their model calls are not in the trace; AOS has
their totals through `usage.json` and their output through the step log. Several keep their own
call logs in their output directory: STORM writes `llm_call_history.jsonl` and `conversation_log.json`;
GRILL keeps every research task's prompt, transcript and answer under `grill_run/tasks/` and every
search under `grill_run/searches/`; DataSTORM writes `tree.json` and `.debug_rm.log`; SLIDERS writes
`trace.json`. See [WORKERS.md](WORKERS-md.md) for each.

## Sending it elsewhere

AOS has no exporter to a tracing service and no dependency on one, by design (standard library,
files first). The JSONL files are the integration point: a tracing backend that ingests
OpenTelemetry or its own JSON (Langfuse, Phoenix, LangSmith and the like) can be fed from them by a
small script run after a task, or by tailing the file during one. The record already carries what
such tools expect of a generation span: timestamps and duration, model, input messages, output,
token counts and cost, and the task/step hierarchy to group spans by.

## Privacy and size

Traces contain the prompts verbatim, and prompts contain the contents of workspace files (the
planner sees the file listing with summaries; the coding agent sees whatever it reads; summaries
see the first 1,500 characters of each new file). Treat the `tasks/` folder as you treat the inputs.
Everything is committed to the workspace's git repository with the step, so it travels with the
workspace and is restored by a rollback like any other record. A long coding-agent step produces a
few hundred kilobytes; a full research task a few megabytes.
