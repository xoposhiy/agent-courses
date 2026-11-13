# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m5/m5.4-async-subagents.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m5/m5.4-async-subagents.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m5/m5.4-async-subagents.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m5.4-async-subagents.md)

Python TypeScript

<a id="async-subagents"></a>


# Async Subagents

```text
<button class="lt-tab active" data-p="async" role="tab" aria-selected="true">Async Subagents</button>
```

```text
<button class="lt-tab" data-p="lab" role="tab" aria-selected="false">Lab</button>
```

```text
<button class="lt-tab" data-p="quiz" role="tab" aria-selected="false">Quiz</button>
```

<a id="p-async"></a>


Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/hrK9spfpxOn.md)

Lesson Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/hrK9spfpxOn.md)

<a id="the-two-invocation-paths"></a>


## The two invocation paths

Async subagents let a supervisor agent launch background tasks that return immediately, so the supervisor can continue interacting with the user while subagents work concurrently. The supervisor can check progress, send follow-up instructions, or cancel tasks at any point.

<a id="dg-fanout-steps"></a>

```javascript

buildDiagram({
  id: 'dg-fanout-steps',
  vw: 720, vh: 530,
  staticSVG:
    '<text x="360" y="38" text-anchor="middle" font-size="17" font-weight="300" fill="#F2FAFF">One supervisor, several async subagents at once</text>' +
    '<ellipse cx="360" cy="82" rx="64" ry="24" fill="#0D1322" stroke="#7FC8FF" stroke-width="1.5"/>' +
    '<text x="360" y="87" text-anchor="middle" font-size="13" fill="#F2FAFF">User</text>' +
    '<line x1="360" y1="106" x2="360" y2="150" stroke="#40668D" stroke-width="1.5" marker-end="url(#arr-dg-fanout-steps)"/>' +
    '<rect x="230" y="152" width="260" height="64" rx="8" fill="#161F34" stroke="#7FC8FF" stroke-width="1.5"/>' +
    '<text x="360" y="182" text-anchor="middle" font-size="15" font-weight="600" fill="#7FC8FF">Supervisor Agent</text>' +
    '<text x="360" y="202" text-anchor="middle" font-size="11" fill="#99D3FF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">stays responsive to the user</text>' +
    '<rect x="50" y="350" width="240" height="82" rx="8" fill="#0D1322" stroke="#40668D" stroke-width="1.2"/>' +
    '<text x="170" y="368" text-anchor="middle" font-size="9.5" letter-spacing="0.5" fill="#5BADDF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">ASYNC SUBAGENT</text>' +
    '<text x="170" y="390" text-anchor="middle" font-size="14" font-weight="600" fill="#CCE9FF">Researcher</text>' +
    '<text x="170" y="409" text-anchor="middle" font-size="10.5" fill="#99D3FF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">runs independently</text>' +
    '<rect x="430" y="350" width="240" height="82" rx="8" fill="#0D1322" stroke="#40668D" stroke-width="1.2"/>' +
    '<text x="550" y="368" text-anchor="middle" font-size="9.5" letter-spacing="0.5" fill="#5BADDF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">ASYNC SUBAGENT</text>' +
    '<text x="550" y="390" text-anchor="middle" font-size="14" font-weight="600" fill="#CCE9FF">Coder</text>' +
    '<text x="550" y="409" text-anchor="middle" font-size="10.5" fill="#99D3FF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">runs independently</text>',
  steps: [
    { tag: '1 · Launch → Researcher', caption: 'The supervisor launches the researcher subagent and gets a task ID back immediately, without waiting for it to finish.' },
    { tag: '2 · Launch → Coder', caption: "It launches the coder subagent right away too, without waiting on the researcher at all." },
    { tag: '3 · Meanwhile', caption: 'Both subagents now run independently, at the same time. The supervisor can check on either one, whenever it wants, in any order.' },
    { tag: '4 · Check ← Researcher', caption: "Later, on its own schedule, the supervisor checks on the researcher's task." },
    { tag: '5 · Check ← Coder', caption: 'And checks on the coder whenever it wants, on its own schedule, same as with the researcher.' }
  ],
  buildSteps: function (a) {
    return [
      '<line x1="245" y1="216" x2="155" y2="350" stroke="#B2DEFF" stroke-width="1.5" marker-end="url(#' + a + ')"/>' +
        '<text x="185" y="284" text-anchor="end" font-size="10.5" fill="#B2DEFF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">launch</text>' +
        '<rect x="50" y="350" width="240" height="82" rx="8" fill="none" stroke="#7FC8FF" stroke-width="2.5"/>',
      '<line x1="475" y1="216" x2="565" y2="350" stroke="#B2DEFF" stroke-width="1.5" marker-end="url(#' + a + ')"/>' +
        '<text x="535" y="284" text-anchor="start" font-size="10.5" fill="#B2DEFF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">launch</text>' +
        '<rect x="430" y="350" width="240" height="82" rx="8" fill="none" stroke="#7FC8FF" stroke-width="2.5"/>',
      '<rect x="50" y="350" width="240" height="82" rx="8" fill="none" stroke="#7FC8FF" stroke-width="2.5"/>' +
        '<rect x="430" y="350" width="240" height="82" rx="8" fill="none" stroke="#7FC8FF" stroke-width="2.5"/>' +
        '<text x="360" y="500" text-anchor="middle" font-size="11.5" fill="#CCE9FF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">both run independently, at the same time</text>',
      '<line x1="185" y1="350" x2="275" y2="216" stroke="#5BADDF" stroke-width="1.5" marker-end="url(#' + a + ')"/>' +
        '<text x="243" y="284" text-anchor="start" font-size="10.5" fill="#5BADDF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">check</text>' +
        '<rect x="230" y="152" width="260" height="64" rx="8" fill="none" stroke="#7FC8FF" stroke-width="2.5"/>',
      '<line x1="535" y1="350" x2="445" y2="216" stroke="#5BADDF" stroke-width="1.5" marker-end="url(#' + a + ')"/>' +
        '<text x="477" y="284" text-anchor="end" font-size="10.5" fill="#5BADDF" font-family="\'IBM Plex Mono\', ui-monospace, monospace">check</text>' +
        '<rect x="230" y="152" width="260" height="64" rx="8" fill="none" stroke="#7FC8FF" stroke-width="2.5"/>'
    ];
  }
});

```

```javascript

(function () {
  var stage = document.getElementById('dg-fanout-steps-stage');
  if (!stage) return;
  var svg = stage.querySelector('svg');
  if (!svg) return;
  var ns = 'http://www.w3.org/2000/svg';
  var g = document.createElementNS(ns, 'g');
  g.id = 'dg-fanout-steps-hint';
  g.setAttribute('style', 'pointer-events:none');
  var r = document.createElementNS(ns, 'rect');
  r.setAttribute('x','0'); r.setAttribute('y','0');
  r.setAttribute('width','720'); r.setAttribute('height','530');
  r.setAttribute('fill','rgba(3,7,16,0.85)');
  g.appendChild(r);
  var t1 = document.createElementNS(ns, 'text');
  t1.setAttribute('x','360'); t1.setAttribute('y','258');
  t1.setAttribute('text-anchor','middle'); t1.setAttribute('fill','#E5F4FF');
  t1.setAttribute('font-size','18'); t1.setAttribute('font-weight','500');
  t1.setAttribute('font-family','IBM Plex Mono, monospace');
  t1.textContent = 'Click to step through the flow';
  g.appendChild(t1);
  var t2 = document.createElementNS(ns, 'text');
  t2.setAttribute('x','360'); t2.setAttribute('y','282');
  t2.setAttribute('text-anchor','middle'); t2.setAttribute('fill','#7FC8FF');
  t2.setAttribute('font-size','13'); t2.setAttribute('font-family','IBM Plex Mono, monospace');
  t2.textContent = 'or use the ← → buttons below';
  g.appendChild(t2);
  svg.appendChild(g);
  function unfade() {
    var hint = document.getElementById('dg-fanout-steps-hint');
    if (hint) hint.style.display = 'none';
    stage.removeEventListener('click', unfade);
    var nb = document.getElementById('dg-fanout-steps-next');
    if (nb) nb.removeEventListener('click', unfade);
  }
  stage.addEventListener('click', unfade);
  var nb = document.getElementById('dg-fanout-steps-next');
  if (nb) nb.addEventListener('click', unfade);
})();

```

An async subagent runs differently from a synchronous one in two ways:

<a id="dg-invoke-table"></a>


| Synchronous subagent (module 4.1, 4.2) | Async subagent |
| --- | --- |
|  |  |

| Synchronous subagent (module 4.1, 4.2) | Async subagent |
| --- | --- |
|  |  |

That remote server is the same kind of deployment you set up earlier in this module, when you ran `langgraph dev` to serve an agent over HTTP. An async subagent target is just another deployed graph, reachable the same way.

---

<a id="setup"></a>


## Setup

You already have both pieces this needs from 5.2’s homework (`python/m5/homework/call_agent_api.py`):

- **The key**: `langgraph.json`’s `"graphs"` mapping (e.g. `"agent": "./agent.py:graph"`) is what `langgraph dev` uses to decide which graph to serve. You used that same key as `ASSISTANT_ID = "agent"`.
- **The address**: the LangGraph SDK reached that server at `API_URL = "http://127.0.0.1:2024"`.

Below, `graph_id` is that same key, and `url` is that same kind of address, just pointing at a different deployment.

You already have both pieces this needs from 5.2’s homework (`typescript/m5/homework/call_agent_api.ts`):

- **The key**: `langgraph.json`’s `"graphs"` mapping (e.g. `"agent": "./agent.ts:graph"`) is what `langgraphjs dev` uses to decide which graph to serve. You used that same key as `ASSISTANT_ID = "agent"`.
- **The address**: the LangGraph SDK reached that server at `API_URL = "http://localhost:2024"`.

Below, `graphId` is that same key, and `url` is that same kind of address, just pointing at a different deployment.

Configuring an async subagent looks like configuring a sync one, but instead of a system prompt and tools, you point at a deployed graph:

<a id="dg-async-setup-code"></a>


```python {3,11,23} import os

from deepagents import AsyncSubAgent, create\_deep\_agent from langchain\_openai import ChatOpenAI

subagents = [ AsyncSubAgent( name=“researcher”, description=“Long-running research agent for deep, multi-source analysis.”, graph\_id=“research\_agent”, url=“https://my-deployment.langsmith.dev”, ),]

model = ChatOpenAI( model=“nvidia/nemotron-3-ultra-550b-a55b:free”, base\_url=“https://openrouter.ai/api/v1”, api\_key=os.environ[“OPENROUTER\_API\_KEY”], )

agent = create\_deep\_agent( model=model, subagents=subagents, )

````text

</div>

<div data-lang="typescript" markdown="1">

```typescript {2,8-9,20}
import { initChatModel } from "langchain";
import { createDeepAgent, type AsyncSubAgent } from "deepagents";

const subagents: AsyncSubAgent[] = [
  {
    name: "researcher",
    description: "Long-running research agent for deep, multi-source analysis.",
    graphId: "research_agent",
    url: "https://my-deployment.langsmith.dev",
  },
];

// Reads OPENROUTER_API_KEY from the environment.
const model = await initChatModel(
  "openrouter:nvidia/nemotron-3-ultra-550b-a55b:free"
);

const agent = createDeepAgent({
  model,
  subagents,
});
````

The highlighted lines are what actually make this an async setup:

- Importing `AsyncSubAgent` instead of a plain dict, and building a list of them
- Pointing at a remote deployment with `graph_id` and `url`
- Passing that list straight to `subagents=` on `create_deep_agent`, same param a sync subagent’s dict config goes in. No middleware to wire in yourself; it’s added to the stack automatically once async subagents are configured

- Typing the entries as `AsyncSubAgent` instead of `SubAgent`, and building an array of them. `AsyncSubAgent` is an interface here, not a class, so each entry is a plain object literal; the annotation is what documents the intent
- Pointing at a remote deployment with `graphId` and `url`
- Passing that array straight to `subagents` on `createDeepAgent`, the same option a sync subagent’s config object goes in. No middleware to wire in yourself; it’s added to the stack automatically once async subagents are configured

This example is shown with NVIDIA’s Nemotron model, an open model.

- **`name`**: what the main agent calls this subagent type when it calls `start_async_task`.
- **`description`**: how the main agent decides when to delegate to it, same role as a sync subagent’s description.
- **`graph_id`**: the graph or assistant ID on the remote server.
- **`url`**: where that server lives. Omit it to connect to a local graph over ASGI transport instead of HTTP; for Agent Server, authentication is handled automatically from your environment (`LANGGRAPH_API_KEY`, `LANGSMITH_API_KEY`, or `LANGCHAIN_API_KEY`).

- **`name`**: what the main agent calls this subagent type when it calls `start_async_task`.
- **`description`**: how the main agent decides when to delegate to it, same role as a sync subagent’s description.
- **`graphId`**: the graph or assistant ID on the remote server.
- **`url`**: where that server lives. Omit it to fall back to the LangGraph SDK’s default endpoint; for Agent Server, authentication is handled automatically from your environment (`LANGGRAPH_API_KEY`, `LANGSMITH_API_KEY`, or `LANGCHAIN_API_KEY`). You can also pass `headers` for custom auth.

You can register more than one async subagent type, each with its own `graph_id` and optionally its own `url`. And since `AsyncSubAgent` entries and plain sync subagent dicts both just go in `subagents=`, you don’t need to keep them in separate lists: `create_deep_agent` sorts out which is which when it compiles the agent.

You can register more than one async subagent type, each with its own `graphId` and optionally its own `url`. And since `AsyncSubAgent` entries and plain sync subagent config objects both just go in `subagents`, you don’t need to keep them in separate arrays: `createDeepAgent` sorts out which is which when it compiles the agent.

---

<a id="the-five-tools"></a>


## The five tools

That middleware exposes five tools to the main agent, alongside the single `task` tool synchronous subagents use, not instead of it:

| Tool | What it does |
| --- | --- |
| `start_async_task` | Launches a background run on the named async subagent. Returns a `task_id` immediately. |
| `check_async_task` | Looks up the current status of a task by `task_id`. If it’s finished, the result comes back too. |
| `update_async_task` | Sends new instructions to a still-running task, on the same thread. |
| `cancel_async_task` | Stops a running task. |
| `list_async_tasks` | Reports the live status of every tracked task at once, optionally filtered by status. |

`start_async_task` doesn’t block. It creates a thread on the remote server, kicks off a run on it, and hands the model a `task_id` right away, its own model call continues without waiting on the subagent at all.

One agent can use sync and async subagents together. By default, deepagents adds a general-purpose sync subagent, so the `task` tool is already there. Add async subagents and the main agent has all six tools: `task` plus the five above. In a single conversation, it can hand a quick job to an in-process subagent, then send a long job to a remote one.

Step through a typical exchange to see how the pieces connect. Notice that “check” is a separate, later round trip; nothing happens automatically in between.

<a id="dg-async-lifecycle"></a>

```javascript

buildDiagram({
  id: 'dg-async-lifecycle',
  participants: ['User', 'Supervisor', 'Agent Protocol Server'],
  cx: [100, 360, 620],
  bw: 170, bh: 36,
  tby: 20, bby: 670,
  vw: 720, vh: 720,
  partFontSize: 11,
  steps: [
    { tag: '1 · Ask', caption: 'The user asks the supervisor to do something.' },
    { tag: '2 · Launch', caption: "The supervisor calls start_async_task, naming the subagent type and describing the job." },
    { tag: '3 · New thread, new run', caption: 'Behind that one call: the server creates a new thread, then starts a run on it targeting the subagent\'s graph_id, the same "graphs" key from langgraph.json.' },
    { tag: '4 · Task ID back', caption: "It gets a task_id back immediately (it's actually the thread_id) and reports it, without waiting for the subagent to finish." },
    { tag: '5 · Tracked in state', caption: 'The supervisor records this task as an AsyncTask in its own state, under the async_tasks key: the task_id, thread_id, run_id, and a status of "running".' },
    { tag: '6 · Meanwhile', caption: 'Time passes. The user keeps talking to the supervisor; the researcher keeps working, unattended, on the remote server.' },
    { tag: '7 · Ask again', caption: 'Later, on their own initiative, the user checks in.' },
    { tag: '8 · Check', caption: 'Only now does the supervisor check the task. Checking happens on request, never automatically, and it can happen as many times as the user asks.' },
    { tag: '9 · Still running', caption: "This check comes back too early: the run hasn't finished, so check_async_task just reports the status, with no result to return yet." },
    { tag: '10 · Ask again', caption: 'The user checks back in again, later.' },
    { tag: '11 · Check again', caption: 'The supervisor checks the same task_id a second time. Nothing stops it from checking as many times as it needs to.' },
    { tag: '12 · Look up the run', caption: "check_async_task looks up the tracked task by task_id, then asks the server for that run's current status. Only if it's finished does it also fetch the thread's latest values to read out the result." },
    { tag: '13 · Result back', caption: 'This time the run has finished, so the result comes back and the supervisor reports it.' }
  ],
  buildSteps: function (a) {
    var hw = 85;
    return [
      solidArrow(100+hw, 360-hw, 110, '"Research topic X"', 230, a),
      solidArrow(360+hw, 620-hw, 160, 'launch(researcher, "topic X")', 490, a),
      '',
      dashedArrow(620-hw, 360+hw, 200, 'task_id: abc123', 490, a) +
        dashedArrow(360-hw, 100+hw, 240, '"Started task abc123"', 230, a),
      '',
      labelBox(360, 270, 560, ['user keeps chatting, researcher keeps working, unattended'], 11),
      solidArrow(100+hw, 360-hw, 345, "\"How's the research going?\"", 230, a),
      solidArrow(360+hw, 620-hw, 390, 'check(abc123)', 490, a),
      dashedArrow(620-hw, 360+hw, 430, 'status: running', 490, a) +
        dashedArrow(360-hw, 100+hw, 470, '"Still working on it..."', 230, a),
      solidArrow(100+hw, 360-hw, 515, '"Any update?"', 230, a),
      solidArrow(360+hw, 620-hw, 560, 'check(abc123)', 490, a),
      '',
      dashedArrow(620-hw, 360+hw, 600, 'status: success, result: "findings..."', 490, a, 10.5) +
        dashedArrow(360-hw, 100+hw, 640, '"Here are the results"', 230, a)
    ];
  }
});

```

```javascript

(function () {
  var stage = document.getElementById('dg-async-lifecycle-stage');
  if (!stage) return;
  var svg = stage.querySelector('svg');
  if (!svg) return;
  var ns = 'http://www.w3.org/2000/svg';
  var g = document.createElementNS(ns, 'g');
  g.id = 'dg-async-lifecycle-hint';
  g.setAttribute('style', 'pointer-events:none');
  var r = document.createElementNS(ns, 'rect');
  r.setAttribute('x','0'); r.setAttribute('y','0');
  r.setAttribute('width','720'); r.setAttribute('height','720');
  r.setAttribute('fill','rgba(3,7,16,0.85)');
  g.appendChild(r);
  var t1 = document.createElementNS(ns, 'text');
  t1.setAttribute('x','360'); t1.setAttribute('y','353');
  t1.setAttribute('text-anchor','middle'); t1.setAttribute('fill','#E5F4FF');
  t1.setAttribute('font-size','18'); t1.setAttribute('font-weight','500');
  t1.setAttribute('font-family','IBM Plex Mono, monospace');
  t1.textContent = 'Click to step through the flow';
  g.appendChild(t1);
  var t2 = document.createElementNS(ns, 'text');
  t2.setAttribute('x','360'); t2.setAttribute('y','377');
  t2.setAttribute('text-anchor','middle'); t2.setAttribute('fill','#7FC8FF');
  t2.setAttribute('font-size','13'); t2.setAttribute('font-family','IBM Plex Mono, monospace');
  t2.textContent = 'or use the ← → buttons below';
  g.appendChild(t2);
  svg.appendChild(g);
  function unfade() {
    var hint = document.getElementById('dg-async-lifecycle-hint');
    if (hint) hint.style.display = 'none';
    stage.removeEventListener('click', unfade);
    var nb = document.getElementById('dg-async-lifecycle-next');
    if (nb) nb.removeEventListener('click', unfade);
  }
  stage.addEventListener('click', unfade);
  var nb = document.getElementById('dg-async-lifecycle-next');
  if (nb) nb.addEventListener('click', unfade);
})();

```

---

<a id="tracking-a-task"></a>


## Tracking a task

Every launched task is tracked as an `AsyncTask` and persisted in the main agent’s state, under an `async_tasks` key: a `task_id` (the thread ID), which agent type launched it, its `run_id`, its `status`, and when it was created, last checked, and last updated.

Every launched task is tracked as an `AsyncTask` and persisted in the main agent’s state, under an `asyncTasks` key: a `taskId` (the thread ID), which agent type launched it (`agentName`), its `runId`, its `status`, and when it was created, last checked, and last updated.

Because of that, **it survives context compaction.** If the conversation gets long enough that older messages are summarized away, the task record stays put, since it lives in state.

---

<a id="how-the-main-agent-is-expected-to-behave"></a>


## How the main agent is expected to behave

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/L2KbPSOEeGs.md)

Lesson Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/L2KbPSOEeGs.md)

Checking on a task right after launching it defeats the purpose, so the model should report the task ID and move on. In Python, the async tools’ own descriptions teach this. The model reads them as part of each tool’s schema. `AsyncSubAgentMiddleware` accepts an optional `system_prompt`, but it defaults to `None` as of deepagents 0.7, and `create_deep_agent` doesn’t set one when you pass it async subagents. So this lab relies on the tool descriptions, which ask for:

- **Launch, then stop.** After `start_async_task`, report the task ID and return control. Don’t immediately call `check_async_task` on it.
- **Check only on request, by default.** The `check_async_task` description tells the model to check only when the user asks for a status update. Auto-notifying the supervisor when a subagent finishes is possible, but needs extra middleware on the subagent side that isn’t part of this default setup.
- **Never trust a status already in the transcript.** A task that shows `"running"` earlier in the conversation may be done by now. Always call a tool to get the current status rather than repeating a stale one.
- **`update_async_task` restarts the run.** It interrupts the current run and starts a fresh one on the same thread, so the subagent sees the full history plus the new instructions. The `task_id` doesn’t change.

Launching a task and immediately checking on it defeats the point, so the model needs to report the task ID and move on. In TypeScript that discipline is carried by the async tools’ own descriptions, which the model reads as part of each tool’s schema. `createAsyncSubAgentMiddleware` takes an optional `systemPrompt`, but it defaults to `null`: this lab’s `main_agent/agent.ts` passes nothing and relies on those tool descriptions, which ask for:

- **Launch, then stop.** After `start_async_task`, report the task ID and return control. Don’t immediately call `check_async_task` on it.
- **Check only on request, by default.** The `check_async_task` description tells the model to check only when the user asks for a status update. Auto-notifying the supervisor when a subagent finishes is possible, but needs extra middleware on the subagent side that isn’t part of this default setup.
- **Never trust a status already in the transcript.** A task that shows `"running"` earlier in the conversation may be done by now. Always call a tool to get the current status rather than repeating a stale one.
- **`update_async_task` restarts the run.** It interrupts the current run and starts a fresh one on the same thread, so the subagent sees the full history plus the new instructions. The `taskId` doesn’t change.

---

<a id="sync-vs.-async-side-by-side"></a>


## Sync vs. async, side by side

<a id="dg-sync-async-table"></a>


|  | Synchronous subagent | Async subagent |
| --- | --- | --- |
| Invoked via | built-in `task` tool | `start_async_task` + friends |
| Runs where | in-process, via `create_agent` | remote server, via the LangGraph SDK |
| Main agent | blocks until it returns | continues immediately |
| Identified by | nothing, it’s just a tool call | `task_id` (persisted in state) |
| Good fit for | focused work the main agent needs before it can continue | long-running or concurrent work the main agent shouldn’t wait on |

**Reach for an async subagent when:**

- The work takes a while, longer than you want the main agent sitting idle
- You want several long jobs running concurrently while the user keeps interacting with the main agent
- The work is better run on a separate, specialized deployment than in-process

**Stick with a synchronous subagent when:**

- The main agent needs the result before it can take its next step
- The task is quick, and the SDK round-trip and remote deployment aren’t worth it
<a id="dg-dynamic-note"></a>


**This is a different topic from Dynamic Subagents (module 4):**

- Sync vs. async is about **how** a subagent call runs
- Dynamic subagents is about **who decides how many** to launch: code writing a loop instead of the model calling `task()` by hand
- The two combine: a dynamically-dispatched subagent can itself be sync or async

The **Lab** tab puts that last point into practice: two real local deployments, one of them carrying a dependency the other doesn’t need.

The **Lab** tab puts that last point into practice: two real local deployments, one of them running a job slow enough that you’d never want it inline.

---

<a id="recap"></a>


## Recap

- An async subagent is a separate agent running on a **remote Agent Protocol server**, reached through the **LangGraph SDK**.
- Async subagents add five tools, which sit alongside the `task` tool that sync subagents use: `start_async_task`, `check_async_task`, `update_async_task`, `cancel_async_task`, and `list_async_tasks`. You can mix sync and async subagents on the same agent; in that case `task` and all five async tools get added.
- `start_async_task` returns a `task_id` immediately; the main agent is expected to report it and move on, not poll.
- Tasks are tracked as `AsyncTask` records in state under `async_tasks`, which is why they survive context compaction.
- Any status already in the conversation may be stale, so checking always means calling a tool.
- Configuring an async subagent means pointing at a deployed graph (`graph_id`, `url`), the same kind of deployment you built earlier in this module.

- An async subagent is a separate agent running on a **remote Agent Protocol server**, reached through the **LangGraph SDK**.
- Async subagents add five tools, which sit alongside the `task` tool that sync subagents use: `start_async_task`, `check_async_task`, `update_async_task`, `cancel_async_task`, and `list_async_tasks`. You can mix sync and async subagents on the same agent; in that case `task` and all five async tools get added.
- `start_async_task` returns a `taskId` immediately; the main agent is expected to report it and move on, not poll.
- Tasks are tracked as `AsyncTask` records in state under `asyncTasks`, which is why they survive context compaction.
- Any status already in the conversation may be stale, so checking always means calling a tool.
- Configuring an async subagent means pointing at a deployed graph (`graphId`, `url`), the same kind of deployment you built earlier in this module.

---

<a id="next"></a>


## Next

Complete the **Lab** and **Quiz** above to see this running end to end, with two real local deployments talking to each other. That wraps up the course. To go further, try wiring an async subagent into the Sales Assistant from the previous lesson, or revisit **Dynamic Subagents** for dispatching subagents programmatically from a loop instead of one call at a time.

---

<a id="references"></a>


## References

**Documentation:**

- [Async subagents (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-async-subagents-6674cbf2.md)
- [Subagents (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-subagents-528266b9.md)
- [Deep Agents overview](../../../../../readings/docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/async_subagents.py`](../../../../../readings/github-510b430b15c6.md): the async task tools and how they talk to remote deployments

- [Async subagents (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-async-subagents-4835e470.md)
- [Subagents (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-subagents-2a904d1e.md)
- [Deep Agents overview](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-overview-9687b9be.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/async_subagents.ts`](../../../../../readings/github-f212fc11a76b.md): the async task tools and how they talk to remote deployments

**Blog:**

- [Running subagents in the background](../../../../../readings/www-langchain-com-blog-running-subagents-in-the-background-76f7f127.md)

<a id="p-lab"></a>


<a id="lab-two-deployments-one-supervisor"></a>


## Lab: Two Deployments, One Supervisor

Lab + Studio Video Walkthrough

[Public video walkthrough](../../../../../videos/QDCRMohPVfN.md)

Every lab so far has run a single `langgraph dev` server. This one runs two, because `specialized_agent` needs `pandas` and `main_agent` doesn’t:

- Installing `pandas` into the shared course environment would mean every other lab picks it up too. Splitting the two into separate deployments keeps that dependency isolated to the one agent that actually needs it.
- You’d hit the same choice building a real app: say one subagent needs a heavyweight ML library that takes a minute to install and load. Bundle it into your main agent’s deployment and every deployment pays that cost, even requests that never touch it. Put it on its own deployment instead, and only the subagent that needs it pays for it.

In this lab:

- **`main_agent`** is light. It depends on the shared course environment, exactly like every other lab in this course, and never installs `pandas`.
- **`specialized_agent`** is heavier. It has its own standalone `pyproject.toml`, isolated from the shared course environment, and it’s the only place `pandas` gets installed. `main_agent` reaches it as an async subagent, over HTTP, without ever needing that dependency itself.

That isolation comes from `specialized_agent/langgraph.json` declaring `"dependencies": ["."]` instead of the `["../.."]` every other lab in this course uses to reach the shared environment:

`json {3} // python/m5/async_lab/specialized_agent/langgraph.json { "dependencies": ["."], "graphs": { "agent": "./agent.py:graph" }, "env": "../../../.env" }`

Its `pyproject.toml` lists `pandas` alongside a minimal set of its own dependencies, separate from the course’s shared list:

`toml {8} # python/m5/async_lab/specialized_agent/pyproject.toml dependencies = [ "deepagents==0.7.0", "langgraph>=1.0.0,<2.0", "langchain-anthropic", "langchain-openai", "langgraph-cli[inmem]>=0.4.0", "pandas>=2.2.0", ]`

And its agent uses that `pandas` dependency in a single tool, `analyze_sales`, which sleeps for 20 seconds (`time.sleep(20)`) to stand in for a heavyweight job. It takes a `group_by` argument, “region” or “product”, so the main agent can launch more than one independent analysis at once:

```python {3,5} # python/m5/async\_lab/specialized\_agent/agent.py @tool def analyze\_sales(group\_by: str = “region”) -> str: “““Run a full sales breakdown, grouped by”region” or by “product”, ranked highest revenue first.”“” time.sleep(20) # stands in for a genuinely slow job grouped = SALES.groupby(group\_by)[[“units\_sold”, “revenue”]].sum().sort\_values(“revenue”, ascending=False) …

<a id="langgraph.json-points-at-this-variable-.agent.pygraph"></a>


# langgraph.json points at this variable: “./agent.py:graph”

graph = create\_deep\_agent(model=model, tools=[analyze\_sales])

````text

<div class="callout" markdown="1">

**Using a provider other than Anthropic?** This deployment can't import the shared `models.py`, so it sets its own model in `agent.py`: `model = init_chat_model("anthropic:claude-haiku-4-5")`. Change that string to your provider's model. Its `pyproject.toml` only includes `langchain-anthropic` and `langchain-openai`, so for any other provider, run `uv add` with that provider's package from inside `specialized_agent/`. API keys still come from the shared `.env`, through `"env": "../../../.env"` in its `langgraph.json`.
</div>

`main_agent` never sees that tool directly. It only knows about an `AsyncSubAgent` named `"analyst"`, pointed at the second server's address:

<Image src="images/m5.4-lab-code-overview.svg" width="800px" alt="Code overview of main_agent/agent.py: an AsyncSubAgent named analyst with a description, graph_id and url pointing at a second langgraph dev server on port 2025, passed to create_deep_agent so the main agent gets async task tools." />

```python {7}
# python/m5/async_lab/main_agent/agent.py
subagents = [
    AsyncSubAgent(
        name="analyst",
        description="Runs sales analysis grouped by region or by product, returning total revenue and units sold per group only. Slow, so it lives on its own deployment.",
        graph_id="agent",
        url="http://127.0.0.1:2025",
    ),
]

graph = create_deep_agent(model=model, subagents=subagents)
````

The description also limits what the main agent asks for. The analyst’s only tool returns total revenue and units sold per group. Without the part of the description that says so, the main agent may ask for something `analyze_sales` never computes, like average transaction value. The analyst can’t compute that, but it may answer anyway with a plausible-looking number instead of saying it doesn’t have the data. Spelling out what the analyst can return in its description helps prevent this kind of hallucination.

<a id="run-it"></a>


### Run it

In the walkthrough video above, `time.sleep(20)` in `analyze_sales` was temporarily changed to `time.sleep(300)` (5 minutes) purely to leave enough time on camera to narrate each step before a task finished on its own. The lab code itself still uses `20`; you don’t need to change anything to follow along.

Two terminals, two servers. Start the specialized deployment first, on port `2025`:

```text
cd python/m5/async_lab/specialized_agent
uv run langgraph dev --port 2025
```

Then, in a second terminal, start the main agent on the default port, `2024`:

```text
cd python/m5/async_lab/main_agent
uv run langgraph dev
```

The second command opens Studio for `main_agent`. Chat with it there, working through the tools from the table above:

1. Ask it to **analyze sales by region, and separately by product, at the same time**. It should call `start_async_task` twice and report two `task_id`s right away, both jobs now running concurrently on the same `specialized_agent` server, without blocking the main agent on either one.
2. Keep chatting, ask it something unrelated, ask what time it is, anything, while both analyses run in the background.
3. Change your mind about the regional one: **tell it to narrow that task to just the West region.** It should call `update_async_task` on that `task_id`. This interrupts the run that’s still in `time.sleep(20)` and starts a new one on the same thread. The subagent sees your new instruction, and the `task_id` stays the same.
4. Decide you don’t need the product breakdown after all: **ask it to cancel that task.** It should call `cancel_async_task` on the product `task_id`.
5. **Ask for an update on what’s left.** It should report back the West-region-only breakdown, reflecting the instruction you sent in step 3.

For step 5, it may call `list_async_tasks`, which reports the status of every tracked task at once instead of one `task_id` at a time.

If you stop the `specialized_agent` server partway through, `main_agent` still reports a `task_id` immediately and stays responsive, it just can’t successfully check the task until that server is back.

---

<a id="lab-two-deployments-one-supervisor-1"></a>


## Lab: Two Deployments, One Supervisor

**The TypeScript version of this lab was made available on September 10, 2026.** Pull the latest changes from the repo root to access it:

```text
git pull
```

Lab + Studio Video Walkthrough (Python)

[Public video walkthrough](../../../../../videos/QDCRMohPVfN.md)

Every lab so far has run a single `langgraphjs dev` server. This one runs two, so the slow analysis job lives somewhere other than the main agent’s own process:

- The analyst’s one tool sleeps for 20 seconds, standing in for a heavyweight job. Run that in-process and it blocks the main agent for the duration; it can’t answer anything else while it waits.
- You’d hit the same choice building a real app. Put the slow work on its own deployment and it can be restarted, scaled, or taken down on its own, and the main agent reaches it the same way it would reach any remote Agent Protocol server: over HTTP, by `graphId` and `url`.

In this lab:

- **`main_agent`** is light. It pulls the shared model from the course’s `models.ts`, exactly like every other lab in this course, and knows nothing about how the analysis actually runs.
- **`specialized_agent`** owns the slow work. It serves the `analyze_sales` tool on port `2025`, and `main_agent` reaches it as an async subagent, over HTTP.

Its agent does that work in a single tool, `analyze_sales`, which waits 20 seconds (`setTimeout(..., 20_000)`) to stand in for a heavyweight job. It takes a `groupBy` argument, “region” or “product”, so the main agent can launch more than one independent analysis at once:

```typescript {5,17} // typescript/m5/async\_lab/specialized\_agent/agent.ts const analyzeSales = tool( async ({ groupBy }: { groupBy: “region” | “product” }) => { // Stands in for a genuinely slow job (a big data pipeline, a model call, etc.). await new Promise((resolve) => setTimeout(resolve, 20\_000)); const totals = new Map<string, { unitsSold: number; revenue: number }>(); // … sum unitsSold and revenue per group, then rank by revenue }, { name: “analyze\_sales”, description: ‘Run a full sales breakdown, grouped by “region” or by “product”, ranked highest revenue first.’, schema: z.object({ groupBy: z.enum([“region”, “product”]).default(“region”) }), } );

// langgraph.json points at this export: “./agent.ts:graph” export const graph = createDeepAgent({ model, tools: [analyzeSales] });

````text

`main_agent` never sees that tool directly. It only knows about an `AsyncSubAgent` named `"analyst"`, pointed at the second server's address:

<Image src="images/m5.4-lab-code-overview-typescript.svg" width="800px" alt="Code overview of main_agent/agent: an async subagent named analyst with a description, graph id and url pointing at a second dev server on port 2025." />

```typescript {8-9,13}
// typescript/m5/async_lab/main_agent/agent.ts
const subagents: AsyncSubAgent[] = [
  {
    name: "analyst",
    description:
      "Runs sales analysis grouped by region or by product, returning total " +
      "revenue and units sold per group only. Slow, so it lives on its own deployment.",
    graphId: "agent",
    url: "http://localhost:2025",
  },
];

export const graph = createDeepAgent({ model, subagents });
````

The description also limits what the main agent asks for. The analyst’s only tool returns total revenue and units sold per group. Without the part of the description that says so, the main agent may ask for something `analyze_sales` never computes, like average transaction value. The analyst can’t compute that, but it may answer anyway with a plausible-looking number instead of saying it doesn’t have the data. Spelling out what the analyst can return in its description helps prevent this kind of hallucination.

<a id="run-it-1"></a>


### Run it

In the walkthrough video above, `time.sleep(20)` in `analyze_sales` was temporarily changed to `time.sleep(300)` (5 minutes) purely to leave enough time on camera to narrate each step before a task finished on its own. The TypeScript lab’s equivalent 20-second `setTimeout` is unchanged; you don’t need to change anything to follow along.

Two terminals, two servers. Start the specialized deployment first, on port `2025`:

```text
cd typescript/m5/async_lab/specialized_agent
pnpm exec langgraphjs dev --port 2025
```

Then, in a second terminal, start the main agent on the default port, `2024`:

```text
cd typescript/m5/async_lab/main_agent
pnpm exec langgraphjs dev
```

The second command opens Studio for `main_agent`. Chat with it there, working through the tools from the table above:

1. Ask it to **analyze sales by region, and separately by product, at the same time**. It should call `start_async_task` twice and report two `taskId`s right away, both jobs now running concurrently on the same `specialized_agent` server, without blocking the main agent on either one.
2. Keep chatting, ask it something unrelated, ask what time it is, anything, while both analyses run in the background.
3. Change your mind about the regional one: **tell it to narrow that task to just the West region.** It should call `update_async_task` on that `taskId`. This interrupts the run that’s still in `setTimeout(..., 20_000)` and starts a new one on the same thread. The subagent sees your new instruction, and the `taskId` stays the same.
4. Decide you don’t need the product breakdown after all: **ask it to cancel that task.** It should call `cancel_async_task` on the product `taskId`.
5. **Ask for an update on what’s left.** It should report back the West-region-only breakdown, reflecting the instruction you sent in step 3.

For step 5, it may call `list_async_tasks`, which reports the status of every tracked task at once instead of one `taskId` at a time.

Step 1 should come back in a few seconds, not the 20 the analysis itself takes, and step 5’s result looks like this:

```text
West region: $78,500 revenue, 2,050 units

Regional ranking by revenue:
1. East    - $99,400 revenue, 2,380 units
2. West    - $78,500 revenue, 2,050 units
3. Central - $54,900 revenue, 1,350 units
```

If you stop the `specialized_agent` server partway through, `main_agent` still reports a `taskId` immediately and stays responsive, it just can’t successfully check the task until that server is back.

---

<a id="p-quiz"></a>


## Check your understanding

## Check your understanding

```javascript

(function () {
  var tabs = document.querySelectorAll('.lt-tab');
  function show(p) {
    tabs.forEach(function (t) {
      var on = t.getAttribute('data-p') === p;
      t.classList.toggle('active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    document.querySelectorAll('.lt-panel').forEach(function (panel) {
      panel.classList.toggle('active', panel.id === 'p-' + p);
    });
  }
  tabs.forEach(function (t) {
    t.addEventListener('click', function () { show(t.getAttribute('data-p')); });
  });
})();

```
