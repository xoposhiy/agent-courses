# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m3/m3.3-memory.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m3/m3.3-memory.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m3/m3.3-memory.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m3.3-memory.md)

Python TypeScript

<a id="memory"></a>


# Memory

```text
<button class="lt-tab active" data-p="mem" role="tab" aria-selected="true">Memory</button>
```

```text
<button class="lt-tab" data-p="lab" role="tab" aria-selected="false">Lab</button>
```

```text
<button class="lt-tab" data-p="quiz" role="tab" aria-selected="false">Quiz</button>
```

```text
<button class="lt-tab" data-p="homework" role="tab" aria-selected="false">Homework</button>
```

<a id="p-mem"></a>


Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/JxDfJX9rj1l.md)

Agent memory splits into two scopes: short-term and long-term.

| Scope | Description |
| --- | --- |
| **Short-term memory** | The running message history for a single thread. It’s tracked automatically by the checkpointer and does not persist beyond that thread. |
| **Long-term memory** | What the agent has learned that should carry over across threads: user preferences, project conventions, recurring facts. It’s tracked in a persistent store or filesystem, separate from any one thread’s message history. |

What separates the two is **scope**:

- A checkpointer can be backed by a real database and outlive the process. Its history still counts as short-term, because it only exists inside the thread that created it.
- Long-term memory is visible to any thread that matches its scope, such as the same user or the same workspace, no matter which thread wrote it.

Both kinds can live in the filesystem. Deep Agents already offloads some short-term context to files by default, mostly large tool outputs that would otherwise crowd the message history. Memory files are the ones scoped to carry over from thread to thread.

This lesson focuses on long-term memory. In Deep Agents, long-term memory is represented as files in the backend, and any file the agent can read or write can be treated as memory once you configure it that way.

[Checkpointer vs. memory walkthrough; use arrow keys or Prev/Next to navigate](../../../../../lesson-assets/m3.3-memory-slides.md)

The checkpointer loads a thread’s history when a run starts and saves it again after each step, so the conversation picks up where it left off. The LLM never calls the checkpointer or the store itself. It just sees the messages and memory that land in front of it.

---

<a id="the-mental-model-memory-is-files"></a>


## The mental model: memory is files

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/MVBfa2AadOp.md)

In Deep Agents, memory is plain files on the agent filesystem. The common convention is a markdown file such as `/memories/AGENTS.md`.

AGENTS.md

```text
# Project Guidelines

## Code Style
- Use type annotations
- Prefer pathlib.Path for file operations

## Workflow
- Run tests with: uv run pytest
```

The agent reads and updates memory with the filesystem tools it already knows, especially `edit_file`, so there’s no separate memory API to learn.

The `memory` argument tells Deep Agents which files should be treated as memory:

`python {3} agent = create_deep_agent( model=model, memory=["/memories/AGENTS.md"], )`

Without `memory=[...]`, the file may still exist in a backend, but it is not loaded into the system prompt as agent memory.

---

<a id="how-memory-is-injected"></a>


## How memory is injected

Passing `memory=[...]` creates `MemoryMiddleware` behind the scenes.

For each run, the middleware:

1. Loads the configured memory files from the backend
2. Stores the loaded contents in agent state
3. Appends the combined memory to the system prompt inside an `<agent_memory>` block on each model call in that run

Compare that with how skills load:

|  | Memory | Skills |
| --- | --- | --- |
| What is always visible? | Loaded memory content | Skill names and descriptions |
| When is full content loaded? | Proactively for the run | On demand when the agent activates a skill |
| Typical use | Persistent facts and instructions | Reusable workflows and procedures |

Head to the **Lab** tab to see the `<agent_memory>` block in LangSmith.

---

<a id="how-memory-is-updated"></a>


## How memory is updated

The middleware also adds instructions telling the agent when to save new information. When a user says “remember this”, or shares context worth keeping, the agent calls `edit_file` on one of the paths passed to `memory=[...]`. It always writes to those same paths. Where each path is actually stored is up to the backend, which the next section covers.

That write updates the file in the backend. The `<agent_memory>` block won’t change right away, though. Memory is loaded the first time a thread runs and then kept in that thread’s state, so later turns in the same thread still see the old copy. Start a new thread, or run without a checkpointer, to see the update.

A typical memory write looks like:

```text
User: Remember: the team switched to ruff for linting.
Agent: edit_file('/memories/AGENTS.md', ...)
```

Only store information that is safe and useful in future conversations. Do not store secrets such as API keys, credentials, tokens, or passwords.

---

<a id="where-memory-lives"></a>


## Where memory lives

The backend controls where memory files are stored. A common production pattern is to use a `CompositeBackend`: keep normal working files in the default backend, and route a dedicated `/memories/` directory to persistent storage.

- `CompositeBackend`: the router. Sends some paths (e.g. `/memories/`) to a `StoreBackend`, and everything else to a different backend.
- `StoreBackend`: the adapter. Wraps a `store` and a namespace, exposing that namespaced slice of it as a virtual file path.
- `store`: the database. A `BaseStore` implementation (e.g. `InMemoryStore()`) that holds the actual key/value data.

```text
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()


def memory_namespace(runtime):
    user_id = runtime.context["user_id"]
    workspace_id = runtime.context["workspace_id"]
    return ("memory", workspace_id, user_id)


agent = create_deep_agent(
    model=model,
    backend=CompositeBackend(
        default=StateBackend(),
        routes={"/memories/": StoreBackend(namespace=memory_namespace)},
    ),
    store=store,
    memory=["/memories/AGENTS.md"],
)
```

In this setup, `/memories/AGENTS.md` is the logical path the agent sees. The `CompositeBackend` routes that path into `StoreBackend`, so memory persists beyond a single thread. Other working files can still use the default backend.

`StateBackend` is thread-scoped, so it is useful for temporary working files but not for persistent long-term memory.

| Component | Scope | Persists past the thread? | Use for |
| --- | --- | --- | --- |
| `StateBackend` | Single thread | No | Temporary working files |
| `StoreBackend` | Namespace you define (e.g. workspace/user) | Yes | Persistent, long-term memory |
| `CompositeBackend` | N/A, routes paths to the backend above | Depends on the route | Splitting working files from memory files |

`InMemoryStore()` is the `BaseStore` that `StoreBackend` writes to, and you pass it in separately via `store=`. It plays the same role for cross-thread memory that `InMemorySaver` plays for thread history. Both are in-process stand-ins for local development, and whatever they hold is gone when the process restarts.

In production, you pass a persistent `store` (and checkpointer) backed by real infrastructure instead.

---

<a id="scoping-memory"></a>


## Scoping memory

The `StoreBackend` namespace on the `/memories/` route determines which stored copy of that memory file the agent sees. In a real application, you usually derive that namespace from runtime context such as the authenticated user, workspace, tenant, or assistant ID.

Scope comes from which segments you include in the namespace tuple, and any combination is valid. Say your assistant is called `support-bot`. If the namespace factory returns `("memory", assistant_id)`, every user shares the memory stored under `("memory", "support-bot")`. If it returns `("memory", assistant_id, user_id)`, user `u_123` gets their own copy under `("memory", "support-bot", "u_123")`. The store matches namespaces exactly, so these are two unrelated keys, even though one looks like an extension of the other.

You pick the tuple shape once, when you write the namespace factory. Every invocation goes through that same shape, with different values filled in.

The `memory_namespace` function on the `/memories/` route in the previous section already defines a user-and-workspace scoped namespace. Invoke the agent with matching context, and the store resolves to that same namespace:

```text
agent.invoke(
    {"messages": [{"role": "user", "content": "Remember that I prefer concise answers."}]},
    context={"user_id": "u_123", "workspace_id": "acme"},
)
```

Common scoping patterns:

| Scope | Namespace shape | Use when… |
| --- | --- | --- |
| Shared assistant memory | `("memory", assistant_id)` | Everyone should share the same persistent instructions |
| User memory | `("memory", user_id)` | Preferences should follow one user across threads |
| Workspace memory | `("memory", workspace_id)` | A team/project should share conventions |
| User within workspace | `("memory", workspace_id, user_id)` | Users have private preferences inside a workspace |
| Assistant + user | `("memory", assistant_id, user_id)` | The same user may have different memories for different assistants |

Getting the scope wrong causes problems in both directions. Put private user memories in a shared namespace, and one user’s preferences can leak into another user’s run. Scope team memory too narrowly, say per user when it should be per workspace, and the agent can’t reuse conventions meant for the whole workspace.

---

<a id="recap"></a>


## Recap

- Checkpointers keep one thread’s history; memory carries across threads
- Memory is persistent knowledge stored as files
- `memory=[...]` activates `MemoryMiddleware` for those files
- Loaded memory is injected into the system prompt inside `<agent_memory>`
- Agents update memory by editing memory files
- The `/memories/` backend route determines persistence; the StoreBackend namespace determines scope

---

<a id="references"></a>


## References

**Documentation:**

- [Memory (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-memory-142f4f4b.md)
- [Filesystem Backends](../../../../../readings/docs-langchain-com-oss-python-deepagents-backends-9df47d8f.md)
- [agents.md specification](../../../../../readings/agents-md-e7c64f11.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/memory.py`](../../../../../readings/github-f8ba4efbbde6.md): loading `AGENTS.md` memory files into the prompt
- [`backends/store.py`](../../../../../readings/github-15889fe1c153.md): `StoreBackend`, for memory that persists across threads

Agent memory splits into two scopes: short-term and long-term.

| Scope | Description |
| --- | --- |
| **Short-term memory** | The running message history for a single thread. It’s tracked automatically by the checkpointer and does not persist beyond that thread. |
| **Long-term memory** | What the agent has learned that should carry over across threads: user preferences, project conventions, recurring facts. It’s tracked in a persistent store or filesystem, separate from any one thread’s message history. |

What separates the two is **scope**:

- A checkpointer can be backed by a real database and outlive the process. Its history still counts as short-term, because it only exists inside the thread that created it.
- Long-term memory is visible to any thread that matches its scope, such as the same user or the same workspace, no matter which thread wrote it.

Both kinds can live in the filesystem. Deep Agents already offloads some short-term context to files by default, mostly large tool outputs that would otherwise crowd the message history. Memory files are the ones scoped to carry over from thread to thread.

This lesson focuses on long-term memory. In Deep Agents, long-term memory is represented as files in the backend, and any file the agent can read or write can be treated as memory once you configure it that way.

[Checkpointer vs. memory walkthrough; use arrow keys or Prev/Next to navigate](../../../../../lesson-assets/m3.3-memory-slides.md)

The checkpointer loads a thread’s history when a run starts and saves it again after each step, so the conversation picks up where it left off. The LLM never calls the checkpointer or the store itself. It just sees the messages and memory that land in front of it.

---

<a id="the-mental-model-memory-is-files-1"></a>


## The mental model: memory is files

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/MVBfa2AadOp.md)

In Deep Agents, memory is plain files on the agent filesystem. The common convention is a markdown file such as `/memories/AGENTS.md`.

AGENTS.md

```text
# Project Guidelines

## Code Style
- Use camelCase for variables and functions
- Prefer path.join for file operations

## Workflow
- Run tests with: pnpm test
```

The agent reads and updates memory with the filesystem tools it already knows, especially `edit_file`, so there’s no separate memory API to learn.

The `memory` option tells Deep Agents which files should be treated as memory:

`typescript {3} const agent = createDeepAgent({ model, memory: ["/memories/AGENTS.md"], });`

Without `memory: [...]`, the file may still exist in a backend, but it is not loaded into the system prompt as agent memory.

---

<a id="how-memory-is-injected-1"></a>


## How memory is injected

Passing `memory: [...]` creates a memory middleware behind the scenes.

For each run, the middleware:

1. Loads the configured memory files from the backend
2. Stores the loaded contents in agent state
3. Appends the combined memory to the system prompt inside an `<agent_memory>` block on each model call in that run

Compare that with how skills load:

|  | Memory | Skills |
| --- | --- | --- |
| What is always visible? | Loaded memory content | Skill names and descriptions |
| When is full content loaded? | Proactively for the run | On demand when the agent activates a skill |
| Typical use | Persistent facts and instructions | Reusable workflows and procedures |

Head to the **Lab** tab to see the `<agent_memory>` block in LangSmith.

---

<a id="how-memory-is-updated-1"></a>


## How memory is updated

The middleware also adds instructions telling the agent when to save new information. When a user says “remember this”, or shares context worth keeping, the agent calls `edit_file` on one of the paths passed to `memory: [...]`. It always writes to those same paths. Where each path is actually stored is up to the backend, which the next section covers.

That write updates the file in the backend. The `<agent_memory>` block won’t change right away, though. Memory is loaded the first time a thread runs and then kept in that thread’s state, so later turns in the same thread still see the old copy. Start a new thread, or run without a checkpointer, to see the update.

A typical memory write looks like:

```text
User: Remember: the team switched to ruff for linting.
Agent: edit_file('/memories/AGENTS.md', ...)
```

Only store information that is safe and useful in future conversations. Do not store secrets such as API keys, credentials, tokens, or passwords.

---

<a id="where-memory-lives-1"></a>


## Where memory lives

The backend controls where memory files are stored. A common production pattern is to use a `CompositeBackend`: keep normal working files in the default backend, and route a dedicated `/memories/` directory to persistent storage.

- `CompositeBackend`: the router. Sends some paths (e.g. `/memories/`) to a `StoreBackend`, and everything else to a different backend.
- `StoreBackend`: the adapter. Wraps a `store` and a namespace, exposing that namespaced slice of it as a virtual file path.
- `store`: the database. A store implementation (e.g. `InMemoryStore()`) that holds the actual key/value data.

```text
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
  type StoreBackendContext,
} from "deepagents";
import { InMemoryStore } from "@langchain/langgraph";

const store = new InMemoryStore();

function memoryNamespace(context: StoreBackendContext): string[] {
  const configurable = (context.config?.configurable ?? {}) as {
    workspace_id: string;
    user_id: string;
  };
  return ["memory", configurable.workspace_id, configurable.user_id];
}

const agent = createDeepAgent({
  model,
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({ namespace: memoryNamespace }),
  }),
  store,
  memory: ["/memories/AGENTS.md"],
});
```

In this setup, `/memories/AGENTS.md` is the logical path the agent sees. The `CompositeBackend` routes that path into `StoreBackend`, so memory persists beyond a single thread. Other working files can still use the default backend.

`StateBackend` is thread-scoped, so it is useful for temporary working files but not for persistent long-term memory.

| Component | Scope | Persists past the thread? | Use for |
| --- | --- | --- | --- |
| `StateBackend` | Single thread | No | Temporary working files |
| `StoreBackend` | Namespace you define (e.g. workspace/user) | Yes | Persistent, long-term memory |
| `CompositeBackend` | N/A, routes paths to the backend above | Depends on the route | Splitting working files from memory files |

`new InMemoryStore()` is the store that `StoreBackend` writes to, and you pass it in separately via `store`. It plays the same role for cross-thread memory that an in-memory checkpointer plays for thread history. Both are in-process stand-ins for local development, and whatever they hold is gone when the process restarts.

In production, you pass a persistent `store` (and checkpointer) backed by real infrastructure instead.

---

<a id="scoping-memory-1"></a>


## Scoping memory

The `StoreBackend` namespace on the `/memories/` route determines which stored copy of that memory file the agent sees. In a real application, you usually derive that namespace from the run’s `RunnableConfig`, such as the authenticated user, workspace, tenant, or assistant ID threaded through `configurable`.

Scope comes from which segments you include in the namespace array, and any combination is valid. Say your assistant is called `support-bot`. If the namespace factory returns `["memory", assistantId]`, every user shares the memory stored under `["memory", "support-bot"]`. If it returns `["memory", assistantId, userId]`, user `u_123` gets their own copy under `["memory", "support-bot", "u_123"]`. The store matches namespaces exactly, so these are two unrelated keys, even though one looks like an extension of the other.

You pick the array shape once, when you write the namespace factory. Every invocation goes through that same shape, with different values filled in.

The `memoryNamespace` function on the `/memories/` route in the previous section already defines a user-and-workspace scoped namespace. Invoke the agent with matching context threaded through `configurable`, and the store resolves to that same namespace:

```text
await agent.invoke(
  { messages: [{ role: "user", content: "Remember that I prefer concise answers." }] },
  { configurable: { user_id: "u_123", workspace_id: "acme" } },
);
```

Common scoping patterns:

| Scope | Namespace shape | Use when… |
| --- | --- | --- |
| Shared assistant memory | `["memory", assistantId]` | Everyone should share the same persistent instructions |
| User memory | `["memory", userId]` | Preferences should follow one user across threads |
| Workspace memory | `["memory", workspaceId]` | A team/project should share conventions |
| User within workspace | `["memory", workspaceId, userId]` | Users have private preferences inside a workspace |
| Assistant + user | `["memory", assistantId, userId]` | The same user may have different memories for different assistants |

Getting the scope wrong causes problems in both directions. Put private user memories in a shared namespace, and one user’s preferences can leak into another user’s run. Scope team memory too narrowly, say per user when it should be per workspace, and the agent can’t reuse conventions meant for the whole workspace.

---

<a id="recap-1"></a>


## Recap

- Checkpointers keep one thread’s history; memory carries across threads
- Memory is persistent knowledge stored as files
- `memory: [...]` activates the memory middleware for those files
- Loaded memory is injected into the system prompt inside `<agent_memory>`
- Agents update memory by editing memory files
- The `/memories/` backend route determines persistence; the StoreBackend namespace determines scope

---

<a id="references-1"></a>


## References

**Documentation:**

- [Memory (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-memory-75ec9480.md)
- [Filesystem Backends](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-backends-5e451258.md)
- [agents.md specification](../../../../../readings/agents-md-e7c64f11.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/memory.ts`](../../../../../readings/github-87e12f714fb2.md): loading `AGENTS.md` memory files into the prompt
- [`backends/store.ts`](../../../../../readings/github-c6b03dd9bd72.md): `StoreBackend`, for memory that persists across threads

<a id="p-quiz"></a>


## Check your understanding

<a id="p-lab"></a>


<a id="lab-coding-assistant-with-memory"></a>


## Lab: Coding Assistant with Memory

Open `python/m3/m3.3_memory_agent.py` to see how memory is wired through `CompositeBackend`: normal working files use the default backend, while `/memories/` routes to `StoreBackend`. The script derives the memory namespace from runtime context, seeds `/memories/AGENTS.md` into an in-memory store, then runs the agent twice. The first invoke answers a question using the memory content; the second triggers a memory write.

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/0rmWKU64h0G.md)

**Inspect your own run in LangSmith.** Notice the `<agent_memory>` block in the system prompt holding the loaded `/memories/AGENTS.md` content, and the agent answering directly from it.

**Inspect your own run in LangSmith.** Notice the agent calling `edit_file` on `/memories/AGENTS.md` to add the note about switching to ruff for linting.

LangSmith Video Walkthrough

[Public video walkthrough](../../../../../videos/cJ0X5fXAUah.md)

---

<a id="run-it"></a>


### Run it

Before running it, make sure your model API key from setup is available in the Python environment.

From the repo root:

```text
cd python
uv run ./m3/m3.3_memory_agent.py
```

After both invokes complete, the script prints the stored `/memories/AGENTS.md` content from the store. Verify that the ruff note was written into that stored memory file.

<a id="lab-coding-assistant-with-memory-1"></a>


## Lab: Coding Assistant with Memory

Open `typescript/m3/m3.3_memory_agent.ts` to see how memory is wired through `CompositeBackend`: normal working files use the default backend, while `/memories/` routes to `StoreBackend`. The script derives the memory namespace from the invoke call’s `configurable`, seeds `/memories/AGENTS.md` into an in-memory store, then runs the agent twice. The first invoke answers a question using the memory content; the second triggers a memory write.

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/0rmWKU64h0G.md)

**Inspect your own run in LangSmith.** Notice the `<agent_memory>` block in the system prompt holding the loaded `/memories/AGENTS.md` content, and the agent answering directly from it.

**Inspect your own run in LangSmith.** Notice the agent calling `edit_file` on `/memories/AGENTS.md` to add the note about switching to ruff for linting.

LangSmith Video Walkthrough

[Public video walkthrough](../../../../../videos/cJ0X5fXAUah.md)

---

<a id="run-it-1"></a>


### Run it

Before running it, make sure your model API key from setup is available in the environment.

From the repo root:

```text
cd typescript
pnpm tsx ./m3/m3.3_memory_agent.ts
```

After both invokes complete, the script prints the stored `/memories/AGENTS.md` content from the store. Verify that the ruff note was written into that stored memory file.

<a id="p-homework"></a>


<a id="prove-memory-isolation-between-users"></a>


## Prove Memory Isolation Between Users

The lab only ever ran the agent under one fixed workspace/user context. So isolation between users (the risk that private memories leak into another user’s agent run when a namespace is scoped too broadly) was never actually demonstrated.

This homework closes that gap. Run the same agent under two different contexts that share a workspace but belong to different users, each resolving to its own `("memory", workspace_id, user_id)` namespace. Seed each context with different facts in a domain of your choosing. Then confirm a detail you tell the agent to remember under one context never leaks into what it says or stores under the other.

Open `python/m3/m3.3_homework.py`.

1. **TODO 1**: write two different seed memories, one for `CONTEXT_A` and one for `CONTEXT_B`, about the same general topic but with different specifics, so a leak would be obvious if it happened.
2. **TODO 2**: write three prompts: a question answerable from `CONTEXT_A`’s seed alone, a “remember this” message that adds a new, distinctive fact under `CONTEXT_A`, and the same question asked again under `CONTEXT_B` (it should get `CONTEXT_B`’s own answer, or no answer, never `CONTEXT_A`’s).

The script prints both contexts’ final stored memory and flags whether isolation held.

<a id="run-it-2"></a>


### Run it

```text
cd python
uv run ./m3/m3.3_homework.py
```

Stuck, or want to see the finished shape before you start? `m3.3_homework_filled.py` is a reference copy with every TODO filled in (using houseplant watering notes); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** a shared team workspace memory (the opposite of the homework’s per-user isolation): a namespace that’s designed to let every member of a workspace read and add to the same memory, like a shared team knowledge base.

**Requirements:**

- Write your own `create_deep_agent(model=model, backend=CompositeBackend(default=StateBackend(), routes={"/memories/": StoreBackend(namespace=workspace_namespace)}), store=store, memory=["/memories/AGENTS.md"])` call from scratch, in a new file under `python/m3/`.
- Write your own namespace function scoped to the workspace only, `("memory", workspace_id)`. Leave `user_id` out of the tuple on purpose, since a team workspace should behave the same for whichever member is running it.
- Run the agent under two contexts that share a `workspace_id` but have different `user_id`s, e.g. `{"workspace_id": "acme", "user_id": "alice"}` and `{"workspace_id": "acme", "user_id": "bob"}`.
- Have “alice” tell the agent to remember a fact, then ask the same question under bob’s context. Confirm bob’s run sees alice’s memory, proving the workspace-level namespace does what it’s meant to and shares memory across teammates.

**⚠ Troubleshooting:** don’t look for a tool call as proof this worked. Memory content gets auto-injected straight into the system prompt via `memory=[…]`, so bob’s run never calls `read_file` or `ls` to “see” alice’s memory; it’s just already there before the model generates anything. Check the store contents or bob’s final answer text instead of the trace’s tool calls.

<a id="prove-memory-isolation-between-users-1"></a>


## Prove Memory Isolation Between Users

The lab only ever ran the agent under one fixed workspace/user context. So isolation between users (the risk that private memories leak into another user’s agent run when a namespace is scoped too broadly) was never actually demonstrated.

This homework closes that gap. Run the same agent under two different contexts that share a workspace but belong to different users, each resolving to its own `("memory", workspace_id, user_id)` namespace. Seed each context with different facts in a domain of your choosing. Then confirm a detail you tell the agent to remember under one context never leaks into what it says or stores under the other.

Open `typescript/m3/m3.3_homework.ts`.

1. **TODO 1**: write two different seed memories, one for `CONTEXT_A` and one for `CONTEXT_B`, about the same general topic but with different specifics, so a leak would be obvious if it happened.
2. **TODO 2**: write three prompts: a question answerable from `CONTEXT_A`’s seed alone, a “remember this” message that adds a new, distinctive fact under `CONTEXT_A`, and the same question asked again under `CONTEXT_B` (it should get `CONTEXT_B`’s own answer, or no answer, never `CONTEXT_A`’s).

The script prints both contexts’ final stored memory and flags whether isolation held.

<a id="run-it-3"></a>


### Run it

```text
cd typescript
pnpm tsx ./m3/m3.3_homework.ts
```

Stuck, or want to see the finished shape before you start? `m3.3_homework_filled.ts` is a reference copy with every TODO filled in (using houseplant watering notes); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** a shared team workspace memory (the opposite of the homework’s per-user isolation): a namespace that’s designed to let every member of a workspace read and add to the same memory, like a shared team knowledge base.

**Requirements:**

- Write your own `createDeepAgent({ model, backend: new CompositeBackend(new StateBackend(), { "/memories/": new StoreBackend({ namespace: workspaceNamespace }) }), store, memory: [memoryPath] })` call from scratch, in a new file under `typescript/m3/`.
- Write your own namespace function scoped to the workspace only, `["memory", workspace_id]`. Leave `user_id` out of the tuple on purpose, since a team workspace should behave the same for whichever member is running it.
- Run the agent under two contexts that share a `workspace_id` but have different `user_id`s, e.g. `{ workspace_id: "acme", user_id: "alice" }` and `{ workspace_id: "acme", user_id: "bob" }`.
- Have “alice” tell the agent to remember a fact, then ask the same question under bob’s context. Confirm bob’s run sees alice’s memory, proving the workspace-level namespace does what it’s meant to and shares memory across teammates.

**⚠ Troubleshooting:** don’t look for a tool call as proof this worked. Memory content gets auto-injected straight into the system prompt via `memory: […]`, so bob’s run never calls a read/list tool to “see” alice’s memory; it’s just already there before the model generates anything. Check the store contents or bob’s final answer text instead of the trace’s tool calls.

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
