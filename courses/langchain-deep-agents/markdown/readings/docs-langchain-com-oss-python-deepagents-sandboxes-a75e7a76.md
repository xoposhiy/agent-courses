# Assigned reference: sandboxes

[Course index](../../README.md) · [Original source](https://docs.langchain.com/oss/python/deepagents/sandboxes) · [Raw file](../../raw/readings/docs-langchain-com-oss-python-deepagents-sandboxes-a75e7a76.html)

Retrieved: 2026-11-13T17:01:26.166088+00:00

# Sandboxes

Copy pageCopy page

Execute code in isolated environments with sandbox backends

Copy pageCopy page

Agents generate code, interact with filesystems, and run shell commands. Because you can’t predict what an agent might do, it’s important that its environment is isolated so it can’t access credentials, files, or the network. Sandboxes provide this isolation by creating a boundary between the agent’s execution environment and your host system.
In Deep Agents, **sandboxes are [backends](docs-langchain-com-oss-python-deepagents-backends-9df47d8f.md)** that define the environment where the agent operates. Unlike other backends (State, Filesystem, Store) which only expose file operations, sandbox backends also give the agent an `execute` tool for running shell commands. When you configure a sandbox backend, the agent gets:

- All standard filesystem tools (`ls`, `read_file`, `write_file`, `edit_file`, `delete`, `glob`, `grep`)
- The `execute` tool for running arbitrary shell commands in the sandbox
- A secure boundary that protects your host system

## Why use sandboxes?

Sandboxes are used for security.
They let agents execute arbitrary code, access files, and use the network without compromising your credentials, local files, or host system.
This isolation is essential when agents run autonomously.
Sandboxes are especially useful for:

- Coding agents: Agents that run autonomously can use shell, git, clone repositories (many providers offer native git APIs, e.g., [Daytona’s git operations](https://www.daytona.io/docs/en/git-operations/)), and run Docker-in-Docker for build and test pipelines
- Data analysis agents: Load files, install data analysis libraries (pandas, numpy, etc.), run statistical calculations, and create outputs like PowerPoint presentations in a safe, isolated environment

**Using Deep Agents Code?** Deep Agents Code has built-in sandbox support via the `--sandbox` flag. See [Use remote sandboxes](https://docs.langchain.com/oss/deepagents/code/remote-sandboxes) for Deep Agents Code-specific setup, flags (`--sandbox-id`, `--sandbox-setup`), and examples.

**If you’re looking for LangSmith sandboxes:** LangSmith provides first-party managed sandboxes you can use directly from the LangSmith UI or SDK without a third-party account required. For managed sandbox resources, snapshots, service URLs, and the auth proxy, refer to [LangSmith Sandboxes](docs-langchain-com-langsmith-sandboxes-571b807e.md).

## Basic usage

These examples assume you have already created a sandbox/devbox using the provider’s SDK and have credentials set up. For signup, authentication, and provider-specific lifecycle details, see [Available providers](docs-langchain-com-oss-python-deepagents-sandboxes-a75e7a76.md).

- LangSmith
- Daytona
- E2B
- Modal
- Runloop
- Vercel

pip

uv

```
pip install langsmith
```

```
uv add langsmith
```

```
from deepagents import create_deep_agent
from deepagents.backends import LangSmithSandbox
from langchain_anthropic import ChatAnthropic
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model=ChatAnthropic(model="claude-sonnet-4-6"),
    system_prompt="You are a Python coding assistant with sandbox access.",
    backend=backend,
)
try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a small Python package and run pytest",
                }
            ]
        }
    )
finally:
    client.delete_sandbox(ls_sandbox.name)
```

## View example trace

Open a public LangSmith run for this example.

pip

uv

```
pip install langchain-daytona
```

```
uv add langchain-daytona
```

```
from daytona import Daytona
from deepagents import create_deep_agent
from langchain_anthropic import ChatAnthropic
from langchain_daytona import DaytonaSandbox

sandbox = Daytona().create()
backend = DaytonaSandbox(sandbox=sandbox)

agent = create_deep_agent(
    model=ChatAnthropic(model="claude-sonnet-4-6"),
    system_prompt="You are a Python coding assistant with sandbox access.",
    backend=backend,
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a small Python package and run pytest",
                }
            ]
        }
    )
finally:
    sandbox.stop()
```

## View example trace

Open a public LangSmith run for this example.

pip

uv

```
pip install langchain-e2b
```

```
uv add langchain-e2b
```

```
from e2b import Sandbox
from deepagents import create_deep_agent
from langchain_anthropic import ChatAnthropic
from langchain_e2b import E2BSandbox

e2b_sandbox = Sandbox.create()
backend = E2BSandbox(sandbox=e2b_sandbox)

agent = create_deep_agent(
    model=ChatAnthropic(model="claude-sonnet-4-6"),
    system_prompt="You are a Python coding assistant with sandbox access.",
    backend=backend,
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a small Python package and run pytest",
                }
            ]
        }
    )
finally:
    e2b_sandbox.kill()
```

pip

uv

```
pip install langchain-modal
```

```
uv add langchain-modal
```

```
import modal
from deepagents import create_deep_agent
from langchain_anthropic import ChatAnthropic
from langchain_modal import ModalSandbox

app = modal.App.lookup("your-app")
modal_sandbox = modal.Sandbox.create(app=app)
backend = ModalSandbox(sandbox=modal_sandbox)

agent = create_deep_agent(
    model=ChatAnthropic(model="claude-sonnet-4-6"),
    system_prompt="You are a Python coding assistant with sandbox access.",
    backend=backend,
)
try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a small Python package and run pytest",
                }
            ]
        }
    )
finally:
    modal_sandbox.terminate()
```

pip

uv

```
pip install langchain-runloop
```

```
uv add langchain-runloop
```

```
import os

from deepagents import create_deep_agent
from langchain_anthropic import ChatAnthropic
from langchain_runloop import RunloopSandbox
from runloop_api_client import RunloopSDK

client = RunloopSDK(bearer_token=os.environ["RUNLOOP_API_KEY"])

devbox = client.devbox.create()
backend = RunloopSandbox(devbox=devbox)

agent = create_deep_agent(
    model=ChatAnthropic(model="claude-sonnet-4-6"),
    system_prompt="You are a Python coding assistant with sandbox access.",
    backend=backend,
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a small Python package and run pytest",
                }
            ]
        }
    )
finally:
    devbox.shutdown()
```

pip

uv

```
pip install langchain-vercel-sandbox
```

```
uv add langchain-vercel-sandbox
```

```
from deepagents import create_deep_agent
from langchain_anthropic import ChatAnthropic
from langchain_vercel_sandbox import VercelSandbox
from vercel.sandbox import Sandbox

sandbox = Sandbox.create(runtime="python3.13")
backend = VercelSandbox(sandbox=sandbox)

agent = create_deep_agent(
    model=ChatAnthropic(model="claude-sonnet-4-6"),
    system_prompt="You are a Python coding assistant with sandbox access.",
    backend=backend,
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a small Python package and run pytest",
                }
            ]
        }
    )
finally:
    sandbox.stop()
```

[LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-deepagents-sandboxes) traces show which shell commands ran inside a sandbox and how the agent used filesystem tools. Follow the [observability quickstart](https://docs.langchain.com/langsmith/observability-quickstart) to get set up. For managed sandbox hosting, see [LangSmith Sandboxes](docs-langchain-com-langsmith-sandboxes-571b807e.md).We recommend you also set up [LangSmith Engine](https://docs.langchain.com/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.

## Available providers

For provider-specific setup, authentication, and lifecycle details, see [sandbox integrations](https://docs.langchain.com/oss/python/integrations/sandboxes).

## Lifecycle and scoping

Most applications choose either one sandbox per [thread](https://docs.langchain.com/langsmith/use-threads) (thread-scoped) or one shared sandbox for every thread on the same [assistant](https://docs.langchain.com/langsmith/assistants) (assistant-scoped).
Sandboxes consume resources and cost money until they are shut down. Make sure you shut sandboxes down once they are no longer in use.
For the full lifecycle table, async [graph factory](https://docs.langchain.com/langsmith/graph-rebuild) notes, TTL behavior, Agent Server wiring, and client-side examples, see [Sandbox lifecycle](docs-langchain-com-oss-python-deepagents-going-to-production-bcebed58.md) in Going to production.

### Thread-scoped (default)

Each conversation gets its own sandbox. The first run creates it; follow-up turns on the same thread reuse it. When the thread ends or the sandbox TTL expires, the environment goes away. Store the mapping with sandbox names or metadata as in the following example so each run resolves to the same sandbox.

When users can return after idle time, configure a TTL on the sandbox so the provider deletes or archives idle environments automatically.

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    sandbox_name = f"thread-{thread_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(
            name=sandbox_name,
            idle_ttl_seconds=3600,  # TTL: clean up when idle
        )
    return create_deep_agent(
        model="google_genai:gemini-4-hydrogen",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    sandbox_name = f"thread-{thread_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(
            name=sandbox_name,
            idle_ttl_seconds=3600,  # TTL: clean up when idle
        )
    return create_deep_agent(
        model="openai:gpt-6.1-sol",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    sandbox_name = f"thread-{thread_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(
            name=sandbox_name,
            idle_ttl_seconds=3600,  # TTL: clean up when idle
        )
    return create_deep_agent(
        model="anthropic:claude-sonnet-5",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    sandbox_name = f"thread-{thread_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(
            name=sandbox_name,
            idle_ttl_seconds=3600,  # TTL: clean up when idle
        )
    return create_deep_agent(
        model="openrouter:z-ai/glm-5.2",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    sandbox_name = f"thread-{thread_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(
            name=sandbox_name,
            idle_ttl_seconds=3600,  # TTL: clean up when idle
        )
    return create_deep_agent(
        model="fireworks:accounts/fireworks/models/glm-5p2",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    sandbox_name = f"thread-{thread_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(
            name=sandbox_name,
            idle_ttl_seconds=3600,  # TTL: clean up when idle
        )
    return create_deep_agent(
        model="baseten:zai-org/GLM-5.2",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    sandbox_name = f"thread-{thread_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(
            name=sandbox_name,
            idle_ttl_seconds=3600,  # TTL: clean up when idle
        )
    return create_deep_agent(
        model="ollama:north-mini-code-1.0",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

### Assistant-scoped

Every thread on the same assistant reuses one sandbox. Files, installed packages, and cloned repositories persist across conversations.

Assistant-scoped sandboxes accumulate in-sandbox state over time. Configure a TTL with your sandbox provider, use snapshots to reset periodically, or implement cleanup logic so disk and memory do not grow without bound.

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    assistant_id = config["configurable"]["assistant_id"]
    sandbox_name = f"assistant-{assistant_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(name=sandbox_name)
    return create_deep_agent(
        model="google_genai:gemini-4-hydrogen",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    assistant_id = config["configurable"]["assistant_id"]
    sandbox_name = f"assistant-{assistant_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(name=sandbox_name)
    return create_deep_agent(
        model="openai:gpt-6.1-sol",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    assistant_id = config["configurable"]["assistant_id"]
    sandbox_name = f"assistant-{assistant_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(name=sandbox_name)
    return create_deep_agent(
        model="anthropic:claude-sonnet-5",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    assistant_id = config["configurable"]["assistant_id"]
    sandbox_name = f"assistant-{assistant_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(name=sandbox_name)
    return create_deep_agent(
        model="openrouter:z-ai/glm-5.2",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    assistant_id = config["configurable"]["assistant_id"]
    sandbox_name = f"assistant-{assistant_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(name=sandbox_name)
    return create_deep_agent(
        model="fireworks:accounts/fireworks/models/glm-5p2",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    assistant_id = config["configurable"]["assistant_id"]
    sandbox_name = f"assistant-{assistant_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(name=sandbox_name)
    return create_deep_agent(
        model="baseten:zai-org/GLM-5.2",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()


async def agent(config: RunnableConfig):
    assistant_id = config["configurable"]["assistant_id"]
    sandbox_name = f"assistant-{assistant_id}"
    existing = [
        sb
        for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    if existing:
        ls_sandbox = existing[0]
    else:
        ls_sandbox = client.create_sandbox(name=sandbox_name)
    return create_deep_agent(
        model="ollama:north-mini-code-1.0",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
```

For manual create, execute, and teardown outside a graph factory, see [Basic usage](docs-langchain-com-oss-python-deepagents-sandboxes-a75e7a76.md) and [sandbox integrations](https://docs.langchain.com/oss/python/integrations/sandboxes) for provider-specific APIs.

## Integration patterns

There are two architecture patterns for integrating agents with sandboxes, based on where the agent runs.

### Agent in sandbox pattern

The agent runs inside the sandbox and you communicate with it over the network. You build a Docker or VM image with your agent framework pre-installed, run it inside the sandbox, and connect from outside to send messages.
Benefits:

- ✅ Mirrors local development closely.
- ✅ Tight coupling between agent and environment.

Trade-offs:

- 🔴 API keys must live inside the sandbox (security risk).
- 🔴 Updates require rebuilding images.
- 🔴 Requires infrastructure for communication (WebSocket or HTTP layer).

To run an agent in a sandbox, build an image and install deepagents on it.

```
FROM python:3.11
RUN pip install deepagents-code
```

Then run the agent inside the sandbox.
To use the agent inside the sandbox you have to add additional infrastructure to handle communication between your application and the agent inside the sandbox.

### Sandbox as tool pattern

The agent runs on your machine or server. When it needs to execute code, it calls sandbox tools (such as `execute`, `read_file`, or `write_file`) which invoke the provider’s APIs to run operations in a remote sandbox.
Benefits:

- ✅ Update agent code instantly without rebuilding images.
- ✅ Cleaner separation between agent state and execution.
  - API keys stay outside the sandbox.
  - Sandbox failures don’t lose agent state.
  - Option to run tasks in multiple sandboxes in parallel.
- ✅ Pay only for execution time.

Trade-offs:

- 🔴 Network latency on each execution call.

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model="google_genai:gemini-4-hydrogen",
    backend=backend,
    system_prompt="You are a coding assistant with sandbox access. You can create and run code in the sandbox.",
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a hello world Python script and run it",
                }
            ]
        }
    )
    print(result["messages"][-1].content)
finally:
    client.delete_sandbox(ls_sandbox.name)
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model="openai:gpt-6.1-sol",
    backend=backend,
    system_prompt="You are a coding assistant with sandbox access. You can create and run code in the sandbox.",
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a hello world Python script and run it",
                }
            ]
        }
    )
    print(result["messages"][-1].content)
finally:
    client.delete_sandbox(ls_sandbox.name)
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model="anthropic:claude-sonnet-5",
    backend=backend,
    system_prompt="You are a coding assistant with sandbox access. You can create and run code in the sandbox.",
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a hello world Python script and run it",
                }
            ]
        }
    )
    print(result["messages"][-1].content)
finally:
    client.delete_sandbox(ls_sandbox.name)
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model="openrouter:z-ai/glm-5.2",
    backend=backend,
    system_prompt="You are a coding assistant with sandbox access. You can create and run code in the sandbox.",
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a hello world Python script and run it",
                }
            ]
        }
    )
    print(result["messages"][-1].content)
finally:
    client.delete_sandbox(ls_sandbox.name)
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model="fireworks:accounts/fireworks/models/glm-5p2",
    backend=backend,
    system_prompt="You are a coding assistant with sandbox access. You can create and run code in the sandbox.",
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a hello world Python script and run it",
                }
            ]
        }
    )
    print(result["messages"][-1].content)
finally:
    client.delete_sandbox(ls_sandbox.name)
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model="baseten:zai-org/GLM-5.2",
    backend=backend,
    system_prompt="You are a coding assistant with sandbox access. You can create and run code in the sandbox.",
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a hello world Python script and run it",
                }
            ]
        }
    )
    print(result["messages"][-1].content)
finally:
    client.delete_sandbox(ls_sandbox.name)
```

```
from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model="ollama:north-mini-code-1.0",
    backend=backend,
    system_prompt="You are a coding assistant with sandbox access. You can create and run code in the sandbox.",
)

try:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Create a hello world Python script and run it",
                }
            ]
        }
    )
    print(result["messages"][-1].content)
finally:
    client.delete_sandbox(ls_sandbox.name)
```

## View example trace

Open a public LangSmith run for this example.

The examples in this doc use the sandbox as a tool pattern.
Choose the agent in sandbox pattern when your provider’s SDK handles the communication layer and you want production to mirror local development.
Choose the sandbox as tool pattern when you need to iterate quickly on agent logic, keep API keys outside the sandbox, or prefer cleaner separation of concerns.

## How sandboxes work

### Isolation boundaries

All sandbox providers protect your host system from the agent’s filesystem and shell operations. The agent cannot read your local files, access environment variables on your machine, or interfere with other processes. However, sandboxes alone do **not** protect against:

- **Context injection**: An attacker who controls part of the agent’s input can instruct it to run arbitrary commands inside the sandbox. The sandbox is isolated, but the agent has full control within it.
- **Network exfiltration**: Unless network access is blocked, a context-injected agent can send data out of the sandbox over HTTP or DNS. Some providers support blocking network access (e.g., `blockNetwork: true` on Modal).

See [security considerations](docs-langchain-com-oss-python-deepagents-sandboxes-a75e7a76.md) for how to handle secrets and mitigate these risks.

### The `execute` method

Sandbox backends have a simple architecture: the only method a provider must implement is `execute()`, which runs a shell command and returns its output.
Every other filesystem operation (`read`, `write`, `edit`, `delete`, `ls`, `glob`, `grep`) is built on top of `execute()` by the [`BaseSandbox`](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox) base class, which constructs scripts and runs them inside the sandbox via `execute()`.

This design means:

- **Adding a new provider is straightforward.** Implement `execute()`—the base class handles everything else.
- **The `execute` tool is conditionally available.** On every model call, the harness checks whether the backend implements [`SandboxBackendProtocol`](https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol). If not, the tool is filtered out and the agent never sees it.

When the agent calls the `execute` tool, it provides a `command` string and gets back the combined stdout/stderr, exit code, and a truncation notice if the output was too large.
You can also call the backend `execute()` method directly in your application code.

- LangSmith
- AgentCore
- Databricks
- Daytona
- E2B
- Modal
- NVIDIA OpenShell
- Runloop
- Vercel

```
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

result = backend.execute("python --version")
print(result.output)
```

pip

uv

```
pip install langchain-agentcore-codeinterpreter
```

```
uv add langchain-agentcore-codeinterpreter
```

```
from bedrock_agentcore.tools.code_interpreter_client import CodeInterpreter

from langchain_agentcore_codeinterpreter import AgentCoreSandbox

interpreter = CodeInterpreter(region="us-west-2")
interpreter.start()

backend = AgentCoreSandbox(interpreter=interpreter)

try:
    result = backend.execute("python3 --version")
    print(result.output)
finally:
    interpreter.stop()
```

pip

uv

```
pip install 'databricks-langchain[deepagents]>=0.22.0'
```

```
uv add 'databricks-langchain[deepagents]>=0.22.0'
```

```
from databricks.sdk import WorkspaceClient

from databricks_langchain import DatabricksSandbox

client = WorkspaceClient()
backend = DatabricksSandbox(client, "sandboxes/my-sandbox")

result = backend.execute("python --version")
print(result.output)
```

pip

uv

```
pip install langchain-daytona
```

```
uv add langchain-daytona
```

```
from daytona import Daytona

from langchain_daytona import DaytonaSandbox

sandbox = Daytona().create()
backend = DaytonaSandbox(sandbox=sandbox)

result = backend.execute("python --version")
print(result.output)
```

pip

uv

```
pip install langchain-e2b
```

```
uv add langchain-e2b
```

```
from e2b import Sandbox
from langchain_e2b import E2BSandbox

e2b_sandbox = Sandbox.create()
sandbox = E2BSandbox(sandbox=e2b_sandbox)

try:
    result = sandbox.execute("python --version")
    print(result.output)
finally:
    e2b_sandbox.kill()
```

```
import modal

from langchain_modal import ModalSandbox

app = modal.App.lookup("your-app")
modal_sandbox = modal.Sandbox.create(app=app)
backend = ModalSandbox(sandbox=modal_sandbox)

result = backend.execute("python --version")
print(result.output)
```

pip

uv

```
pip install langchain-nvidia-openshell
```

```
uv add langchain-nvidia-openshell
```

```
import openshell

from langchain_nvidia_openshell import OpenShellSandbox

with openshell.Sandbox(delete_on_exit=True) as sandbox:
    backend = OpenShellSandbox(sandbox=sandbox)

    result = backend.execute("python3 --version")
    print(result.output)
```

pip

uv

```
pip install langchain-runloop
```

```
uv add langchain-runloop
```

```
from runloop_api_client import RunloopSDK

from langchain_runloop import RunloopSandbox

api_key = "..."
client = RunloopSDK(bearer_token=api_key)

devbox = client.devbox.create()
backend = RunloopSandbox(devbox=devbox)

try:
    result = backend.execute("python --version")
    print(result.output)
finally:
    devbox.shutdown()
```

pip

uv

```
pip install langchain-vercel-sandbox
```

```
uv add langchain-vercel-sandbox
```

```
from vercel.sandbox import Sandbox

from langchain_vercel_sandbox import VercelSandbox

sandbox = Sandbox.create(runtime="python3.13")
backend = VercelSandbox(sandbox=sandbox)

try:
    result = backend.execute("python --version")
    print(result.output)
finally:
    sandbox.stop()
```

For example:

```
4
[Command succeeded with exit code 0]
```

```
bash: foobar: command not found
[Command failed with exit code 127]
```

If a command produces very large output, the result is automatically saved to a file and the agent is instructed to use `read_file` to access it incrementally. This prevents context window overflow.

### Two planes of file access

There are two distinct ways files move in and out of a sandbox, and it’s important to understand when to use each:
**Agent filesystem tools**: `read_file`, `write_file`, `edit_file`, `delete`, `ls`, `glob`, `grep`, `execute` are the tools the LLM calls during its execution. These go through `execute()` inside the sandbox. The agent uses them to read code, write files, and run commands as part of its task.
**File transfer APIs**: the `uploadFiles()` and `downloadFiles()` methods that your application code calls. These use the provider’s native file transfer APIs (not shell commands) and are designed for moving files between your host environment and the sandbox. Use these to:

- **Seed the sandbox** with source code, configuration, or data before the agent runs
- **Retrieve artifacts** (generated code, build outputs, reports) after the agent finishes
- **Pre-populate dependencies** that the agent will need

## Working with files

The deepagents sandbox backends support file transfer APIs for moving files between your application and the sandbox.

### Seeding the sandbox

Use `upload_files()` to populate the sandbox before the agent runs. Paths must be absolute and contents are `bytes`:

- LangSmith
- AgentCore
- Databricks
- Daytona
- E2B
- Modal
- Runloop
- Vercel

```
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

backend.upload_files(
    [
        ("/src/index.py", b"print('Hello')\n"),
        ("/pyproject.toml", b"[project]\nname = 'my-app'\n"),
    ]
)
```

pip

uv

```
pip install langchain-agentcore-codeinterpreter
```

```
uv add langchain-agentcore-codeinterpreter
```

```
from bedrock_agentcore.tools.code_interpreter_client import CodeInterpreter

from langchain_agentcore_codeinterpreter import AgentCoreSandbox

interpreter = CodeInterpreter(region="us-west-2")
interpreter.start()

backend = AgentCoreSandbox(interpreter=interpreter)

backend.upload_files(
    [
        ("hello.py", b"print('Hello')\n"),
        ("data.csv", b"name,value\na,1\nb,2\n"),
    ]
)
```

pip

uv

```
pip install 'databricks-langchain[deepagents]>=0.22.0'
```

```
uv add 'databricks-langchain[deepagents]>=0.22.0'
```

```
from databricks.sdk import WorkspaceClient

from databricks_langchain import DatabricksSandbox

client = WorkspaceClient()
backend = DatabricksSandbox(client, "sandboxes/my-sandbox")

backend.upload_files(
    [
        ("/src/index.py", b"print('Hello')\n"),
        ("/pyproject.toml", b"[project]\nname = 'my-app'\n"),
    ]
)
```

pip

uv

```
pip install langchain-daytona
```

```
uv add langchain-daytona
```

```
from daytona import Daytona

from langchain_daytona import DaytonaSandbox

sandbox = Daytona().create()
backend = DaytonaSandbox(sandbox=sandbox)

backend.upload_files(
    [
        ("/src/index.py", b"print('Hello')\n"),
        ("/pyproject.toml", b"[project]\nname = 'my-app'\n"),
    ]
)
```

pip

uv

```
pip install langchain-e2b
```

```
uv add langchain-e2b
```

```
from e2b import Sandbox
from langchain_e2b import E2BSandbox

e2b_sandbox = Sandbox.create()
sandbox = E2BSandbox(sandbox=e2b_sandbox)

try:
    sandbox.upload_files(
        [
            ("/src/index.py", b"print('Hello')\n"),
            ("/pyproject.toml", b"[project]\nname = 'my-app'\n"),
        ]
    )
finally:
    e2b_sandbox.kill()
```

```
import modal

from langchain_modal import ModalSandbox

app = modal.App.lookup("your-app")
modal_sandbox = modal.Sandbox.create(app=app)
backend = ModalSandbox(sandbox=modal_sandbox)

backend.upload_files(
    [
        ("/src/index.py", b"print('Hello')\n"),
        ("/pyproject.toml", b"[project]\nname = 'my-app'\n"),
    ]
)
```

pip

uv

```
pip install langchain-runloop
```

```
uv add langchain-runloop
```

```
from runloop_api_client import RunloopSDK

from langchain_runloop import RunloopSandbox

api_key = "..."
client = RunloopSDK(bearer_token=api_key)

devbox = client.devbox.create()
backend = RunloopSandbox(devbox=devbox)

backend.upload_files(
    [
        ("/src/index.py", b"print('Hello')\n"),
        ("/pyproject.toml", b"[project]\nname = 'my-app'\n"),
    ]
)
```

pip

uv

```
pip install langchain-vercel-sandbox
```

```
uv add langchain-vercel-sandbox
```

```
from vercel.sandbox import Sandbox

from langchain_vercel_sandbox import VercelSandbox

sandbox = Sandbox.create(runtime="python3.13")
backend = VercelSandbox(sandbox=sandbox)

backend.upload_files(
    [
        ("/src/index.py", b"print('Hello')\n"),
        ("/pyproject.toml", b"[project]\nname = 'my-app'\n"),
    ]
)
```

### Retrieving artifacts

Use `download_files()` to retrieve files from the sandbox after the agent finishes:

- LangSmith
- AgentCore
- Databricks
- Daytona
- E2B
- Modal
- Runloop
- Vercel

```
from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)


results = backend.download_files(["/src/index.py", "/output.txt"])
for result in results:
    if result.content is not None:
        print(f"{result.path}: {result.content.decode()}")
    else:
        print(f"Failed to download {result.path}: {result.error}")
```

pip

uv

```
pip install langchain-agentcore-codeinterpreter
```

```
uv add langchain-agentcore-codeinterpreter
```

```
from bedrock_agentcore.tools.code_interpreter_client import CodeInterpreter

from langchain_agentcore_codeinterpreter import AgentCoreSandbox

interpreter = CodeInterpreter(region="us-west-2")
interpreter.start()

backend = AgentCoreSandbox(interpreter=interpreter)

results = backend.download_files(["hello.py"])
for result in results:
    if result.content is not None:
        print(f"{result.path}: {result.content.decode()}")
    else:
        print(f"Failed to download {result.path}: {result.error}")

interpreter.stop()
```

pip

uv

```
pip install 'databricks-langchain[deepagents]>=0.22.0'
```

```
uv add 'databricks-langchain[deepagents]>=0.22.0'
```

```
from databricks.sdk import WorkspaceClient

from databricks_langchain import DatabricksSandbox

client = WorkspaceClient()
backend = DatabricksSandbox(client, "sandboxes/my-sandbox")

results = backend.download_files(["/src/index.py", "/output.txt"])
for result in results:
    if result.content is not None:
        print(f"{result.path}: {result.content.decode()}")
    else:
        print(f"Failed to download {result.path}: {result.error}")
```

pip

uv

```
pip install langchain-daytona
```

```
uv add langchain-daytona
```

```
from daytona import Daytona

from langchain_daytona import DaytonaSandbox

sandbox = Daytona().create()
backend = DaytonaSandbox(sandbox=sandbox)

results = backend.download_files(["/src/index.py", "/output.txt"])
for result in results:
    if result.content is not None:
        print(f"{result.path}: {result.content.decode()}")
    else:
        print(f"Failed to download {result.path}: {result.error}")
```

pip

uv

```
pip install langchain-e2b
```

```
uv add langchain-e2b
```

```
from e2b import Sandbox
from langchain_e2b import E2BSandbox

e2b_sandbox = Sandbox.create()
sandbox = E2BSandbox(sandbox=e2b_sandbox)

try:
    results = sandbox.download_files(["/src/index.py", "/output.txt"])
    for result in results:
        if result.content is not None:
            print(f"{result.path}: {result.content.decode()}")
        else:
            print(f"Failed to download {result.path}: {result.error}")
finally:
    e2b_sandbox.kill()
```

```
import modal

from langchain_modal import ModalSandbox

app = modal.App.lookup("your-app")
modal_sandbox = modal.Sandbox.create(app=app)
backend = ModalSandbox(sandbox=modal_sandbox)

results = backend.download_files(["/src/index.py", "/output.txt"])
for result in results:
    if result.content is not None:
        print(f"{result.path}: {result.content.decode()}")
    else:
        print(f"Failed to download {result.path}: {result.error}")
```

pip

uv

```
pip install langchain-runloop
```

```
uv add langchain-runloop
```

```
from runloop_api_client import RunloopSDK

from langchain_runloop import RunloopSandbox

api_key = "..."
client = RunloopSDK(bearer_token=api_key)

devbox = client.devbox.create()
backend = RunloopSandbox(devbox=devbox)

results = backend.download_files(["/src/index.py", "/output.txt"])
for result in results:
    if result.content is not None:
        print(f"{result.path}: {result.content.decode()}")
    else:
        print(f"Failed to download {result.path}: {result.error}")
```

pip

uv

```
pip install langchain-vercel-sandbox
```

```
uv add langchain-vercel-sandbox
```

```
from vercel.sandbox import Sandbox

from langchain_vercel_sandbox import VercelSandbox

sandbox = Sandbox.create(runtime="python3.13")
backend = VercelSandbox(sandbox=sandbox)

results = backend.download_files(["/src/index.py", "/output.txt"])
for result in results:
    if result.content is not None:
        print(f"{result.path}: {result.content.decode()}")
    else:
        print(f"Failed to download {result.path}: {result.error}")
```

Inside the sandbox, the agent uses filesystem tools (`read_file`, `write_file`). The `upload_files` and `download_files` methods are for your application code to move files across the boundary between your host and the sandbox.

## Security considerations

Sandboxes isolate code execution from your host system, but they don’t protect against **context injection**. An attacker who controls part of the agent’s input can instruct it to read files, run commands, or exfiltrate data from within the sandbox. This makes credentials inside the sandbox especially dangerous.

**Never put secrets inside a sandbox.** API keys, tokens, database credentials, and other secrets injected into a sandbox (via environment variables, mounted files, or the `secrets` option) can be read and exfiltrated by a context-injected agent. This applies even to short-lived or scoped credentials—if an agent can access them, so can an attacker.

### Handling secrets safely

If your agent needs to call authenticated APIs or access protected resources, you have two options:

1. **Keep secrets in tools outside the sandbox.** Define tools that run in your host environment (not inside the sandbox) and handle authentication there. The agent calls these tools by name, but never sees the credentials. This is the recommended approach.
2. **Use a network proxy that injects credentials.** Some sandbox providers support proxies that intercept outgoing HTTP requests from the sandbox and attach credentials (e.g., `Authorization` headers) before forwarding them. The agent never sees the secret—it just makes plain requests to a URL. This approach is not yet widely available across providers.

If you must inject secrets into a sandbox (not recommended), take these precautions:

- Enable [human-in-the-loop](docs-langchain-com-oss-python-deepagents-human-in-the-loop-65328403.md) approval for **all** tool calls, not just sensitive ones
- Block or restrict network access from the sandbox to limit exfiltration paths
- Use the narrowest possible credential scope and shortest possible lifetime
- Monitor sandbox network traffic for unexpected outbound requests

Even with these safeguards, this remains an unsafe workaround. A sufficiently creative enough context injection attack can bypass output filtering and HITL review.

### General best practices

- Review sandbox outputs before acting on them in your application
- Block sandbox network access when not needed
- Use [middleware](https://docs.langchain.com/oss/python/langchain/middleware) to filter or redact sensitive patterns in tool outputs
- Treat everything produced inside the sandbox as untrusted input

---

[Connect these docs](https://docs.langchain.com/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/sandboxes.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo
