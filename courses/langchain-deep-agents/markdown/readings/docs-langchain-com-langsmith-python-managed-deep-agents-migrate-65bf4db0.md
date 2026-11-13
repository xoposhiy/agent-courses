# Assigned reference: managed-deep-agents-migrate

[Course index](../../README.md) · [Original source](https://docs.langchain.com/langsmith/python/managed-deep-agents-migrate) · [Raw file](../../raw/readings/docs-langchain-com-langsmith-python-managed-deep-agents-migrate-65bf4db0.html)

Retrieved: 2026-11-13T17:00:54.029724+00:00

# Move from Deep Agents to Managed Deep Agents

Copy pageCopy page

Convert an agent built with create\_deep\_agent into a Managed Deep Agents project.

Copy pageCopy page

Managed Deep Agents runs the same [Deep Agents](docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md) harness you already build against, so moving an existing agent is a repackaging job rather than a rewrite. Your tools, middleware, and subagents carry over as they are. The agent entry changes, and the system prompt, skills, and memory move into project files.

Managed Deep Agents is in **public [beta](https://docs.langchain.com/langsmith/release-stages)** on [LangSmith Cloud](https://docs.langchain.com/langsmith/cloud) and [Bring Your Own Cloud (BYOC)](https://docs.langchain.com/langsmith/byoc). Use Managed Deep Agents CLI and SDK v0.10 or later for BYOC.

## Decide whether to move

Managed Deep Agents runs the same harness, so the agent itself behaves the same. Tools, middleware, and subagents work as they do today. Moving adds the layer around the agent: Slack and other chat surfaces, OAuth for end users, scheduled runs, a managed sandbox, and durable memory become declarations in a project file rather than services you build and operate.
Move an agent when you want that layer without running it. Stay on Deep Agents when you need to own it.


|  | Deep Agents | Managed Deep Agents |
| --- | --- | --- |
| **Hosting** | You run the agent in your own process or container, or deploy it on [LangSmith Agent Server](https://docs.langchain.com/langsmith/deployment). | LangSmith hosts the agent on [Agent Server](https://docs.langchain.com/langsmith/agent-server-overview). `mda deploy` is the whole deployment step. |
| **Filesystem and shell** | Any [backend](docs-langchain-com-oss-python-deepagents-backends-9df47d8f.md): agent state, local disk, a store, or a [sandbox](docs-langchain-com-oss-python-deepagents-sandboxes-a75e7a76.md) you provision with a provider. | One managed [sandbox](https://docs.langchain.com/langsmith/python/managed-deep-agents-sandboxes), declared in a file. LangSmith creates it, snapshots it, and stops it when idle. |
| **Memory across conversations** | You run the storage and wire it up yourself. | One shared [memory](https://docs.langchain.com/langsmith/python/managed-deep-agents-memory) tree, enabled by adding a file. |
| **Third-party access for end users** | You provision and store credentials for each user. | [Connections](https://docs.langchain.com/langsmith/python/managed-deep-agents-connections) hold workspace secrets and run OAuth, so end users authorize services themselves. |
| **Chat surfaces** | You write the integration. | [Channels](https://docs.langchain.com/langsmith/python/managed-deep-agents-channels) connect Slack and other messaging services. |
| **Scheduled runs** | You run the scheduler. | [Schedules](https://docs.langchain.com/langsmith/python/managed-deep-agents-schedules) run managed cron jobs. |
| **Code around the agent** | Yours to write, including custom routes and application code. | The agent only. For custom routes or application code, use [LangSmith Agent Server](https://docs.langchain.com/langsmith/deployment). |

The harness is the same either way. Start with [Managed Deep Agents](docs-langchain-com-langsmith-managed-deep-agents-75c0af16.md) for new agents when you want to run production agents without having to manage infrastructure. Use this guide when you already have a Deep Agents SDK agent and want the managed runtime. For using the same Deep Agents harness and hosting agents yourself or running a custom [Agent Server](https://docs.langchain.com/langsmith/deployment), see [Going to production](docs-langchain-com-oss-python-deepagents-going-to-production-bcebed58.md).

## Understand what changes

[create\_deep\_agent](https://reference.langchain.com/python/deepagents/graph/create_deep_agent) compiles an agent in your process, so it takes the backend, store, and checkpointer as parameters. `define_deep_agent` returns a definition instead, and the managed runtime compiles it. The definition is configuration rather than a runnable agent: the `mda` CLI consumes it on `mda dev` and `mda deploy`, and the runtime supplies the managed pieces at that point. For the full picture, see [Relationship to Deep Agents](docs-langchain-com-langsmith-managed-deep-agents-75c0af16.md).

## Check what does not carry over

Most agents move without changes beyond the entry file. Four cases need a decision first:

- **Custom backends**: Managed Deep Agents supplies the agent’s default backend. This is thread-scoped agent state, or a [managed sandbox](https://docs.langchain.com/langsmith/python/managed-deep-agents-sandboxes) when the project declares one. You cannot replace the default backend. To keep your own backend, mount it at a path prefix, such as `/documents/`, with [`routes`](https://docs.langchain.com/langsmith/python/managed-deep-agents-agent-definition#mount-your-own-backends). Routes require 0.10.3 or later.
- **Your own store or checkpointer**: Threads, runs, and persistence come from [Agent Server](https://docs.langchain.com/langsmith/agent-server-overview). An agent that depends on a specific store implementation needs that logic moved into a tool or middleware.
- **Custom application code and routes**: Managed Deep Agents hosts the agent, not an arbitrary web application. For custom routes, advanced authentication, or application code around the agent, use [LangSmith Agent Server](https://docs.langchain.com/langsmith/deployment) instead.
- **Custom state schemas in Python**: `define_deep_agent` does not accept `state_schema`, so an agent that extends `DeepAgentState` cannot move as is. The TypeScript `defineDeepAgent` does accept `stateSchema`.

If none of these apply, the agent logic transfers as written.

Convert a Deep Agents project into a Managed Deep Agents project.

CopiedCopy prompt

## Map the parameters

Most of the surface transfers to `define_deep_agent` unchanged, under the same names: `model`, `tools`, `middleware`, `subagents`, `interrupt_on`, `response_format`, `context_schema`, `cache`, and `debug`. Leave the tool and middleware modules where they already live and keep importing them from the agent entry.
`define_deep_agent` adds one required parameter. Pass `name` a static string that starts with a letter and contains only letters, numbers, underscores, or hyphens. Managed Deep Agents uses it as the agent’s graph ID and the default deployment name.
The rest move to a project file or become the runtime’s job:


| `create_deep_agent` | Where it goes | Notes |
| --- | --- | --- |
| `system_prompt` | `instructions.md` | Move the text into the file, then remove the parameter. See [Instructions](https://docs.langchain.com/langsmith/python/managed-deep-agents-instructions). |
| `skills` | `skills/` | One directory per skill, each with a `SKILL.md`. See [Skills](https://docs.langchain.com/langsmith/python/managed-deep-agents-skills). |
| `memory` | `memory.py` | Export `define_memory(scope="agent")`. Omit the file for no durable memory. See [Memory](https://docs.langchain.com/langsmith/python/managed-deep-agents-memory). |
| `backend` | `sandbox/` or `routes` | Declare a managed sandbox for the filesystem and shell. To keep other backends, mount them at path prefixes with `routes`. See [Sandboxes](https://docs.langchain.com/langsmith/python/managed-deep-agents-sandboxes) and [Mount your own backends](https://docs.langchain.com/langsmith/python/managed-deep-agents-agent-definition#mount-your-own-backends). |
| `permissions` | Stays a parameter | Accepted, and cleared when the project declares a sandbox. See [Permissions](docs-langchain-com-oss-python-deepagents-permissions-7cf433c4.md). |
| `store`, `checkpointer` | Managed runtime | Remove both. |
| `state_schema` | No equivalent | `define_deep_agent` does not accept it. |

Deep Agents backends are pluggable, and the managed runtime supplies its own. A project that declares `sandbox/` gets a managed sandbox for the agent filesystem and shell. A project without one gets thread-scoped agent state, alongside read-only [Context Hub](https://docs.langchain.com/langsmith/python/managed-deep-agents-context-hub) mounts for instructions, skills, and memory. You cannot replace this default backend. To keep a specific backend, mount it at a path prefix with [`routes`](https://docs.langchain.com/langsmith/python/managed-deep-agents-agent-definition#mount-your-own-backends). An agent that needs its own backend for every path stays on Deep Agents.

## Move an agent

Convert the project in place. The existing layout, module structure, and dependencies stay as they are: `mda build` merges the dependencies it needs into the project manifest rather than replacing it.
To install the `mda` CLI first, see the [quickstart](https://docs.langchain.com/langsmith/python/managed-deep-agents-quickstart).

1

Add the SDK to the project

```
uv add managed-deepagents
```

Pin the version to match the CLI, which `mda --version` reports.If the project builds with Hatchling, allow direct references in `pyproject.toml`:

pyproject.toml

```
[tool.hatch.metadata]
allow-direct-references = true
```

`mda build` rewrites the `managed-deepagents` requirement into a path reference to the runtime it stages, and Hatchling rejects that by default. Without the setting, `mda build` still succeeds and `mda dev` fails while installing the project, with `Dependency #N of field project.dependencies cannot be a direct reference`. Projects scaffolded by `mda init` declare no build backend, so the setting only comes up when converting an existing project.Leave every dependency the project already declares in place. Tools and middleware keep importing what they always did.

2

Rewrite the agent entry

Convert the call site using the table above, in a file named `agent.py` at the project root:

agent.py (before)

```
from deepagents import create_deep_agent

from tools.search import internet_search

agent = create_deep_agent(
    model="openai:gpt-5.5",
    tools=[internet_search],
    system_prompt=SYSTEM_PROMPT,
    skills=["/skills/research/"],
    checkpointer=checkpointer,  # yours to construct and wire
)
```

agent.py (after)

```
from managed_deepagents import define_deep_agent

from tools.search import internet_search

agent = define_deep_agent(
    name="research-assistant",
    model="openai:gpt-5.5",
    tools=[internet_search],
)
```

The entry must export a variable named `agent`, and the definition call itself has to live in this file. A root entry that re-exports the definition from another module fails, and the error names `name` rather than the real problem.A `src/` layout is otherwise fine. Keep the packages where they are and import them from the root entry.

3

Move the prompt, skills, and memory into files

Put the system prompt in `instructions.md` at the project root. Give each skill its own directory under `skills/` with a `SKILL.md`.If the agent needs memory that persists across threads, declare it in a root file exporting a variable named `memory`:

memory.py

```
from managed_deepagents import define_memory

memory = define_memory(scope="agent")
```

Durable memory is opt-in, and a project without the file mounts none. The scope is the only knob: `"agent"` mounts one tree that every caller of the deployment shares. To control what the agent keeps there, write a memory policy into `instructions.md`. See [Guide what to remember](https://docs.langchain.com/langsmith/python/managed-deep-agents-memory#guide-what-to-remember).

`define_memory` mounts an empty memory tree. Content from the files the old `memory` parameter pointed at does not transfer, so move anything the agent still needs into `instructions.md` or a skill before deleting those files.

4

Declare a sandbox

An agent that passed a sandbox `backend` needs a managed sandbox declaration instead. Create the directory and declare it:

sandbox/\_\_init\_\_.py

```
from managed_deepagents import define_sandbox

sandbox = define_sandbox(
    idle_ttl_seconds=600,
    default_timeout=600,
)
```

Declaring a sandbox clears `permissions`. A filesystem permission rule disables the sandbox `execute` tool, so the runtime drops the rules rather than the shell. Restrict a sandboxed agent through the tools you give it instead.

To provision a snapshot, add `sandbox/setup.sh`. Skip this step for an agent that had no sandbox backend. See [Sandboxes](https://docs.langchain.com/langsmith/python/managed-deep-agents-sandboxes).

5

Declare identity

(Optional) To give each caller private threads and downstream credentials, add a root identity declaration:

identity.py

```
from managed_deepagents import auth, define_identity

identity = define_identity(auth=auth.langsmith_api_key())
```

Without the file the deployment runs with no managed auth, which `mda dev` reports as `Identity none`. See [Identity](docs-langchain-com-langsmith-python-managed-deep-agents-identity-000af9d5.md).

6

Set credentials and ignore the build output

Put the model and tool API keys in a `.env` file at the project root. A value exported in your shell is not read. For shared workspace secrets and OAuth, use [connections](https://docs.langchain.com/langsmith/python/managed-deep-agents-connections) instead.Add the build directory to `.gitignore`:

.gitignore

```
.env
.env.*
.mda/
```

`mda build` copies the whole project root into `.mda/build`, and `mda deploy` uploads it. Anything sitting next to the agent entry ships with the agent, so move what the deployment does not need out of the project root.

7

Compile, then run

Compile without deploying:

```
mda build
```

Then start it locally:

```
mda dev
```

`mda build` does not inspect the definition call, so it exits 0 even when a managed parameter is still there. A leftover parameter surfaces when the graph loads under `mda dev`.

See [Local development](https://docs.langchain.com/langsmith/python/managed-deep-agents-local-development).

8

Deploy

Upload the project and let LangSmith build and host it:

```
mda deploy
```

See [Deploy](https://docs.langchain.com/langsmith/python/managed-deep-agents-deploy).

Starting a new agent rather than moving one? Scaffold the whole project, including the identity, sandbox, `.env`, and `.gitignore` files above:

```
mda init research-assistant
```

The install channel selects the authoring language: the npm package scaffolds TypeScript, and the PyPI package scaffolds Python. The command creates a new directory and does not run in place, so it suits a greenfield project rather than a migration. See the [quickstart](https://docs.langchain.com/langsmith/python/managed-deep-agents-quickstart).

## See also

- [Relationship to Deep Agents](docs-langchain-com-langsmith-managed-deep-agents-75c0af16.md): why the two entry points differ.
- [Agent definition](https://docs.langchain.com/langsmith/python/managed-deep-agents-agent-definition): the full parameter reference.
- [Project structure](https://docs.langchain.com/langsmith/python/managed-deep-agents-project-structure): where each file goes.
- [Going to production](docs-langchain-com-oss-python-deepagents-going-to-production-bcebed58.md): deployment options for Deep Agents.

---

[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-migrate.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo
