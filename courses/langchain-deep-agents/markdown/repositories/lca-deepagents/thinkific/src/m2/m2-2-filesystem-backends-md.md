# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m2/m2.2-filesystem-backends.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m2/m2.2-filesystem-backends.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m2/m2.2-filesystem-backends.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m2.2-filesystem-backends.md)

```javascript
mermaid.initialize({ startOnLoad: true, theme: 'base', themeVariables: { background: '#F2FAFF', primaryColor: '#E5F4FF', primaryBorderColor: '#006DDD', primaryTextColor: '#030710', lineColor: '#2F4B68' } });
```

Python TypeScript

<a id="filesystem-backends"></a>


# Filesystem Backends

```text
<button class="lt-tab active" data-p="fs" role="tab" aria-selected="true">Filesystem Backends</button>
```

```text
<button class="lt-tab" data-p="lab1" role="tab" aria-selected="false">Lab</button>
```

```text
<button class="lt-tab" data-p="quiz" role="tab" aria-selected="false">Quiz</button>
```

```text
<button class="lt-tab" data-p="homework" role="tab" aria-selected="false">Homework</button>
```

<a id="p-fs"></a>


Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/i6oUY8Y8h2H.md)

The agent always sees the same filesystem tools: `ls`, `read_file`, `write_file`, `edit_file`, `glob`, and `grep`. A filesystem backend decides where those files are actually stored.

This lesson covers the built-in filesystem backends and how to choose between them.

graph LR A[Agent filesystem tools] –> B[Backend] B –> S[StateBackendthread state] B –> F[FilesystemBackenddisk] B –> C[Custom backend, GitHub, other storage]

```text
classDef agent fill:#CCE9FF,stroke:#006DDD,stroke-width:2px,color:#030710
classDef backend fill:#7FC8FF,stroke:#006DDD,stroke-width:2px,color:#030710
classDef store fill:#E5F4FF,stroke:#40668D,stroke-width:1px,color:#030710

class A agent
class B backend
class S,F,C store
```

*All filesystem backends expose the same tools. The backend adapts each call to a specific storage implementation.*

---

<a id="the-filesystem-backends"></a>


## The filesystem backends

You can select different backends depending on where you want files to live. This lesson focuses on the built-in options that do not require a persistent store.

**StateBackend**: the default. Files live in the agent’s saved state for the current thread. This is fast and zero-config, and it is good for scratch work.

**FilesystemBackend / local disk**: reads and writes files on the local disk, scoped to a `root_dir` you specify. Use it when the agent should work with real files in a local directory.

**CompositeBackend**: routes different path prefixes to different backends. It lets one agent use StateBackend for normal scratch files while routing a specific directory, such as `/reference/`, to local disk.

**Custom backend**: implement the backend interface yourself to plug in another storage system, such as S3, GitHub, or a proprietary store.

**A naming note: “the agent’s filesystem” vs. `FilesystemBackend`**   
  
 “Filesystem” is used two ways here:

- The agent’s filesystem is the general capability: the `ls` / `read_file` / `write_file` / `edit_file` / `glob` / `grep` tools every Deep Agent has, no matter which backend is behind them.
- `FilesystemBackend` is just one of the four backends above: the one that stores those files on local disk. `StateBackend`, `CompositeBackend`, and a custom backend implement the exact same tools; they just store the data somewhere else.

Picking “a filesystem backend” doesn’t mean picking `FilesystemBackend` specifically.

---


Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/Fzcxn1OpG7D.md)

## Single Backend

vs

## Composite Backend

Single backend

graph TB A1[Agent] –> SB[StateBackend] SB –> D1[Thread state]

```text
classDef agent fill:#CCE9FF,stroke:#006DDD,stroke-width:2px,color:#030710
classDef backend fill:#7FC8FF,stroke:#006DDD,stroke-width:2px,color:#030710
classDef store fill:#E5F4FF,stroke:#40668D,stroke-width:1px,color:#030710

class A1 agent
class SB backend
class D1 store
```

Composite backend

graph TB A2[Agent] –> CB[CompositeBackend] CB –>|“/reference/”| D2[Local disk] CB –>|“everything else”| ST[Thread state]

```text
classDef agent fill:#CCE9FF,stroke:#006DDD,stroke-width:2px,color:#030710
classDef backend fill:#7FC8FF,stroke:#006DDD,stroke-width:2px,color:#030710
classDef disk fill:#E5F4FF,stroke:#006DDD,stroke-width:1px,color:#030710
classDef state fill:#E5F4FF,stroke:#40668D,stroke-width:1px,color:#030710

class A2 agent
class CB backend
class D2 disk
class ST state
```

<a id="single-backend"></a>


## Single backend

Pass any backend directly to `create_deep_agent`. If you do not pass one, Deep Agents uses `StateBackend()` by default.

```text
from deepagents import create_deep_agent
from deepagents.backends import StateBackend

agent = create_deep_agent(
    model=model,
    backend=StateBackend(),
)
```

Use `FilesystemBackend` when you want the agent’s filesystem tools to read and write real local files under a root directory:

```text
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend

agent = create_deep_agent(
    model=model,
    backend=FilesystemBackend(root_dir="/path/to/project", virtual_mode=True),
)
```

Pass any backend directly to `createDeepAgent`. If you do not pass one, Deep Agents uses `new StateBackend()` by default.

```text
import { createDeepAgent, StateBackend } from "deepagents";

const agent = createDeepAgent({
  model,
  backend: new StateBackend(),
});
```

Use `FilesystemBackend` when you want the agent’s filesystem tools to read and write real local files under a root directory:

```text
import { createDeepAgent, FilesystemBackend } from "deepagents";

const agent = createDeepAgent({
  model,
  backend: new FilesystemBackend({ rootDir: "/path/to/project", virtualMode: true }),
});
```

---

<a id="composite-backend"></a>


## Composite backend

Sometimes one backend is not enough. You may want ordinary scratch files to stay in thread state, but a specific directory to map to real local files.

`CompositeBackend` resolves this by routing path prefixes to different backends. Everything not matched by a route falls through to the default backend.

Pass the default backend with the `default` keyword and per-prefix backends with `routes`:

```text
from pathlib import Path

from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, FilesystemBackend, StateBackend

reference_dir = Path(__file__).parent / "reference"

agent = create_deep_agent(
    model=model,
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/reference/": FilesystemBackend(
                root_dir=str(reference_dir),
                virtual_mode=True,
            ),
        },
    ),
)
```

`CompositeBackend` takes the default backend and the routes as positional arguments:

```text
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import {
  CompositeBackend,
  FilesystemBackend,
  StateBackend,
  createDeepAgent,
} from "deepagents";

const __dirname = dirname(fileURLToPath(import.meta.url));
const referenceDir = join(__dirname, "reference");

const agent = createDeepAgent({
  model,
  backend: new CompositeBackend(new StateBackend(), {
    "/reference/": new FilesystemBackend({
      rootDir: referenceDir,
      virtualMode: true,
    }),
  }),
});
```

- `/reference/notes.md` → local file at `reference/notes.md`
- Everything else → `StateBackend`, scoped to the current thread’s saved state

---

<a id="permissions"></a>


## Permissions

Permissions are enforced in code, so the model cannot bypass them. Pass a list of `FilesystemPermission` rules to `create_deep_agent`. Rules are evaluated in order and the first match wins. If nothing matches, the operation is allowed.

Each rule has three fields:

| Field | Values | Default | Description |
| --- | --- | --- | --- |
| `operations` | `"read"`, `"write"` | - | `"read"` covers `ls`, `read_file`, `glob`, `grep`. `"write"` covers `write_file`, `edit_file`, `delete`. |
| `paths` | glob patterns | - | e.g. `["/reference/**"]`. Supports `**` and `{a,b}` alternation. |
| `mode` | `"allow"`, `"deny"`, `"interrupt"` | `"allow"` | `"interrupt"` pauses for human approval instead of blocking. |

```text
from pathlib import Path

from deepagents import FilesystemPermission, create_deep_agent
from deepagents.backends import CompositeBackend, FilesystemBackend, StateBackend

reference_dir = Path(__file__).parent / "reference"

agent = create_deep_agent(
    model=model,
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/reference/": FilesystemBackend(
                root_dir=str(reference_dir),
                virtual_mode=True,
            ),
        },
    ),
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/reference/**"],
            mode="deny",
        ),
    ],
)
```

Permissions are enforced in code, so the model cannot bypass them. Pass a `permissions` array of `FilesystemPermission` rules to `createDeepAgent`. Rules are evaluated in order and the first match wins. If nothing matches, the operation is allowed.

Each rule has three fields:

| Field | Values | Default | Description |
| --- | --- | --- | --- |
| `operations` | `"read"`, `"write"` | - | `"read"` covers `ls`, `read_file`, `glob`, `grep`. `"write"` covers `write_file`, `edit_file`. |
| `paths` | glob patterns | - | e.g. `["/reference/**"]`. Supports `**` and `{a,b}` alternation. |
| `mode` | `"allow"`, `"deny"` | `"allow"` | TypeScript does not yet support Python’s `"interrupt"` mode for pausing on human approval. |

```text
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import {
  CompositeBackend,
  FilesystemBackend,
  StateBackend,
  createDeepAgent,
  type FilesystemPermission,
} from "deepagents";

const __dirname = dirname(fileURLToPath(import.meta.url));
const referenceDir = join(__dirname, "reference");

const agent = createDeepAgent({
  model,
  backend: new CompositeBackend(new StateBackend(), {
    "/reference/": new FilesystemBackend({
      rootDir: referenceDir,
      virtualMode: true,
    }),
  }),
  permissions: [
    {
      operations: ["write"],
      paths: ["/reference/**"],
      mode: "deny",
    } satisfies FilesystemPermission,
  ],
});
```

The agent can read `/reference/`, but it cannot write to it. Other paths still use the default `StateBackend` route.

---

<a id="restricting-the-tool-list-itself"></a>


## Restricting the tool list itself

Permission rules control where an operation can happen. The `tools` option on the filesystem middleware controls which tools the model can see: pass it an allowlist of tool names, and anything left off is hidden. `read_file` must always be included.

```text
from deepagents import create_deep_agent, FilesystemMiddleware

agent = create_deep_agent(
    model=model,
    middleware=[FilesystemMiddleware(tools=["read_file", "grep", "ls"])],
)
```

The allowlist accepts `ls`, `read_file`, `write_file`, `edit_file`, `delete`, `glob`, `grep`, and `execute`.

```text
import { createDeepAgent, createFilesystemMiddleware } from "deepagents";

const agent = createDeepAgent({
  model,
  middleware: [createFilesystemMiddleware({ tools: ["read_file", "grep", "ls"] })],
});
```

The allowlist accepts `ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`, and `execute`.

---

<a id="recap"></a>


## Recap

- All filesystem backends expose the same tool surface
- **StateBackend** is the default and is good for scratch files in the current thread
- **FilesystemBackend / local disk** maps filesystem tools to real local files under a root directory
- **CompositeBackend** lets you route different path prefixes to different backends
- Permissions are enforced in code, not in the prompt

<a id="next"></a>


## Next

Complete the **Lab** and **Quiz** above, then continue to the next lesson on execution backends that add a shell `execute` tool on top of the filesystem surface.

---

<a id="references"></a>


## References

**Documentation:**

- [Filesystem Backends](../../../../../readings/docs-langchain-com-oss-python-deepagents-backends-9df47d8f.md)
- [Permissions](../../../../../readings/docs-langchain-com-oss-python-deepagents-permissions-7cf433c4.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`backends/state.py`](../../../../../readings/github-a4f325ab7ae3.md): `StateBackend`, files kept in agent state
- [`backends/filesystem.py`](../../../../../readings/github-2f33420a7caf.md): `FilesystemBackend`, files on local disk
- [`backends/store.py`](../../../../../readings/github-15889fe1c153.md): `StoreBackend`, files in a LangGraph store, shared across threads
- [`backends/composite.py`](../../../../../readings/github-075fb80c8832.md): `CompositeBackend`, routing paths to different backends

**Documentation:**

- [Filesystem Backends](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-backends-5e451258.md)
- [Permissions](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-permissions-22d268b5.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`backends/state.ts`](../../../../../readings/github-6081271cc455.md): `StateBackend`, files kept in agent state
- [`backends/filesystem.ts`](../../../../../readings/github-8447877c21b4.md): `FilesystemBackend`, files on local disk
- [`backends/store.ts`](../../../../../readings/github-c6b03dd9bd72.md): `StoreBackend`, files in a LangGraph store, shared across threads
- [`backends/composite.ts`](../../../../../readings/github-59cdd58eff4c.md): `CompositeBackend`, routing paths to different backends

<a id="p-quiz"></a>


## Check your understanding

<a id="p-lab1"></a>


<a id="lab-filesystem-permissions"></a>


## Lab: Filesystem Permissions

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/q4b8LOnnehl.md)

**Inspect your own run in LangSmith.** Notice the agent reading `/reference/chinook-sales.md` successfully, then getting blocked on the write.

LangSmith Video Walkthrough

[Public video walkthrough](../../../../../videos/CywMBDM59XU.md)

The lab agent uses a `CompositeBackend` with normal scratch files in `StateBackend` and `/reference/` routed to a local `FilesystemBackend`. A `FilesystemPermission` rule denies all writes to `/reference/**`.

The agent is given a reference file, asked to read it, then asked to add a note. You’ll see it read successfully and get blocked on the write.

Before running it, make sure your model API key from setup is available in the Python environment.

```text
# python/m2/m2.2_agent.py
from pathlib import Path

from deepagents import FilesystemPermission, create_deep_agent
from deepagents.backends import CompositeBackend, FilesystemBackend, StateBackend

from models import model

reference_dir = Path(__file__).parent / "reference"
reference_dir.mkdir(exist_ok=True)
(reference_dir / "chinook-sales.md").write_text("""\
# Chinook Sales Reference

You are a sales representative for Chinook Digital Music Store.

Responsibilities:
- Look up customer accounts and purchase history
- Recommend music based on genre and artist preferences
- Answer questions about artists, albums, tracks, and invoices
""", encoding="utf-8")

agent = create_deep_agent(
    model=model,
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/reference/": FilesystemBackend(
                root_dir=str(reference_dir),
                virtual_mode=True,
            ),
        },
    ),
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/reference/**"],
            mode="deny",
        ),
    ],
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Read /reference/chinook-sales.md, then add this note to it: "
                    "'Current promotion: 20% off all Jazz albums through end of month.'"
                ),
            }
        ]
    },
    config={"configurable": {"thread_id": "lab-m2.2"}},
)

print(result["messages"][-1].text)
```

From the repo root:

```text
cd python
uv run ./m2/m2.2_agent.py
```

Example output will vary by model, but it should show the same behavior:

```text
I read /reference/chinook-sales.md successfully, but I could not update it because writes to /reference/** are denied.

Current reference:
# Chinook Sales Reference
...

The note I would add is:
- Current promotion: 20% off all Jazz albums through end of month.
```

**What to look for:**

- The agent reads `/reference/chinook-sales.md` without issue
- When it tries to write, it reports that the file is read-only or write-protected
- Other paths still use the default state-backed filesystem route

Before running it, make sure your model API key from setup is available in the TypeScript environment.

```text
// typescript/m2/m2.2_agent.ts
import { dirname, join } from "node:path";
import { mkdirSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

import { context } from "langchain";
import {
  CompositeBackend,
  FilesystemBackend,
  StateBackend,
  createDeepAgent,
  type FilesystemPermission,
} from "deepagents";

import { model } from "../models.js";

const __dirname = dirname(fileURLToPath(import.meta.url));

// Set up a read-only reference directory the agent can consult but not modify.
const referenceDir = join(__dirname, "reference");
mkdirSync(referenceDir, { recursive: true });
writeFileSync(
  join(referenceDir, "chinook-sales.md"),
  `\
# Chinook Sales Reference

You are a sales representative for Chinook Digital Music Store.

Responsibilities:
- Look up customer accounts and purchase history
- Recommend music based on genre and artist preferences
- Answer questions about artists, albums, tracks, and invoices
`
);

const agent = createDeepAgent({
  model,
  backend: new CompositeBackend(new StateBackend(), {
    "/reference/": new FilesystemBackend({
      rootDir: referenceDir,
      virtualMode: true,
    }),
  }),
  permissions: [
    {
      operations: ["write"],
      paths: ["/reference/**"],
      mode: "deny",
    } satisfies FilesystemPermission,
  ],
});

const result = await agent.invoke(
  {
    messages: [
      {
        role: "user",
        content: context`
          Read /reference/chinook-sales.md, then add this note to it:
          'Current promotion: 20% off all Jazz albums through end of month.'`,
      },
    ],
  },
  { configurable: { thread_id: "lab-m2.2" } }
);
console.log(result.messages.at(-1)?.text);
```

From the repo root:

```text
cd typescript
pnpm tsx ./m2/m2.2_agent.ts
```

Example output will vary by model, but it should show the same behavior:

```text
Permission enforced: Error: permission denied for write on /reference/chinook-sales.md
```

**What to look for:**

- The agent reads `/reference/chinook-sales.md` without issue
- When it tries to write, it reports that the file is read-only or write-protected
- Other paths still use the default state-backed filesystem route

<a id="p-homework"></a>


<a id="configure-your-own-filesystem-backend"></a>


## Configure Your Own Filesystem Backend

The lab wired up one fixed setup: a `CompositeBackend` routing a single reference file to local disk, with a `FilesystemPermission` rule denying all writes to it. This homework asks you to do the same thing, but for a file-based task of your own choosing.

Open `python/m2/m2.2_homework.py`.

Your choice here changes what actually happens when you run your file, compared to the lab:

| Backend | What happens to your file | Compared to the lab |
| --- | --- | --- |
| `StateBackend` | Lives only in the thread’s saved state; disappears once the thread ends, nothing touches disk | The lab wrote a real file to disk; this skips that entirely |
| `FilesystemBackend` (`virtual_mode=True`) | A real file on disk under whatever `root_dir` you set; still there after the script exits | Same real-disk behavior as the lab’s `/reference/` route, but applied to your whole filesystem instead of one path |
| `CompositeBackend` | A real file on disk under `root_dir`, while everything else stays in thread state | Closest match to the lab’s exact setup: one real path on disk, everything else in state |

Whichever you pick, `FilesystemPermission` rules behave the same: they’re checked against the path before the backend is touched, so the same allow/deny/interrupt outcome happens no matter where the file actually lives.

1. **TODO 1**: pick a topic for a small text file (a packing list, a journal, a recipe box, meeting notes, etc.), seed it with some starting content, and configure any backend you like: `StateBackend`, `FilesystemBackend`, or a `CompositeBackend` routing between them.
2. **TODO 2**: write a task message that has the agent read your file, then write or edit it, and optionally add a `FilesystemPermission` rule that changes what the agent is allowed to do.

<a id="run-it"></a>


### Run it

```text
cd python
uv run ./m2/m2.2_homework.py
```

Stuck, or want to see the finished shape before you start? `m2.2_homework_filled.py` is a reference copy with every TODO filled in (using a recipe box with one heirloom recipe locked against writes); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** a filesystem tool allowlist that hides `write_file` from the model entirely, instead of letting it call the tool and blocking the call with a permission rule.

**Requirements:**

- Write your own `create_deep_agent(model=model, backend=..., middleware=[FilesystemMiddleware(backend=backend, tools=[...])])` call from scratch, in a new file under `python/m2/`.
- Configure a `CompositeBackend` routing one directory to a `FilesystemBackend(root_dir=..., virtual_mode=True)` (same shape as the lab), and seed it with a starting file.
- Add a `FilesystemMiddleware(backend=backend, tools=[...])` allowlist that leaves `write_file` (and/or `edit_file`) off the list, so the model never even sees that tool exists. `read_file` must stay on the list.
- Write a task that asks the agent to read the file, then also asks it to edit it. Check the trace/messages: no `write_file`/`edit_file` tool call shows up at all, since the model was never given that tool, unlike a `FilesystemPermission` deny rule, where the model calls the tool and only then gets blocked.

**⚠ Troubleshooting:** don’t forget `backend=backend` inside your own `FilesystemMiddleware(…)` call. `create_deep_agent` already builds its own backend-wired filesystem middleware internally and replaces it with yours by name, so a backend-less middleware silently falls back to state-only storage; your seeded file will look like it never existed.

<a id="configure-your-own-filesystem-backend-1"></a>


## Configure Your Own Filesystem Backend

The lab wired up one fixed setup: a `CompositeBackend` routing a single reference file to local disk, with a `FilesystemPermission` rule denying all writes to it. This homework asks you to do the same thing, but for a file-based task of your own choosing.

Open `typescript/m2/m2.2_homework.ts`.

Your choice here changes what actually happens when you run your file, compared to the lab:

| Backend | What happens to your file | Compared to the lab |
| --- | --- | --- |
| `StateBackend` | Lives only in the thread’s saved state; disappears once the thread ends, nothing touches disk | The lab wrote a real file to disk; this skips that entirely |
| `FilesystemBackend` (`virtual_mode=True`) | A real file on disk under whatever `root_dir` you set; still there after the script exits | Same real-disk behavior as the lab’s `/reference/` route, but applied to your whole filesystem instead of one path |
| `CompositeBackend` | A real file on disk under `root_dir`, while everything else stays in thread state | Closest match to the lab’s exact setup: one real path on disk, everything else in state |

Whichever you pick, `FilesystemPermission` rules behave the same: they’re checked against the path before the backend is touched, so the same allow/deny/interrupt outcome happens no matter where the file actually lives.

1. **TODO 1**: pick a topic for a small text file (a packing list, a journal, a recipe box, meeting notes, etc.), seed it with some starting content, and configure any backend you like: `StateBackend`, `FilesystemBackend`, or a `CompositeBackend` routing between them.
2. **TODO 2**: write a task message that has the agent read your file, then write or edit it, and optionally add a `FilesystemPermission` rule that changes what the agent is allowed to do.

<a id="run-it-1"></a>


### Run it

```text
cd typescript
pnpm tsx ./m2/m2.2_homework.ts
```

Stuck, or want to see the finished shape before you start? `m2.2_homework_filled.ts` is a reference copy with every TODO filled in (using a recipe box with one heirloom recipe locked against writes); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** a filesystem tool allowlist that hides `write_file` from the model entirely, instead of letting it call the tool and blocking the call with a permission rule.

**Requirements:**

- Write your own `createDeepAgent({ model, backend: ..., middleware: [createFilesystemMiddleware({ backend, tools: [...] })] })` call from scratch, in a new file under `typescript/m2/`.
- Configure a `CompositeBackend` routing one directory to a `new FilesystemBackend({ rootDir: ..., virtualMode: true })` (same shape as the lab), and seed it with a starting file.
- Add a `createFilesystemMiddleware({ backend, tools: [...] })` allowlist that leaves `write_file` (and/or `edit_file`) off the list, so the model never even sees that tool exists. `read_file` must stay on the list.
- Write a task that asks the agent to read the file, then also asks it to edit it. Check the trace/messages: no `write_file`/`edit_file` tool call shows up at all, since the model was never given that tool, unlike a `FilesystemPermission` deny rule, where the model calls the tool and only then gets blocked.

**⚠ Troubleshooting:** don’t forget `backend` inside your own `createFilesystemMiddleware(…)` call. `createDeepAgent` already builds its own backend-wired filesystem middleware internally and replaces it with yours by name, so a backend-less middleware silently falls back to state-only storage; your seeded file will look like it never existed.

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
