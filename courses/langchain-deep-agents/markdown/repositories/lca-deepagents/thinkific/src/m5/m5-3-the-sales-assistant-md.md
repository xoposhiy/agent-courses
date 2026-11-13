# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m5/m5.3-the-sales-assistant.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m5/m5.3-the-sales-assistant.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m5/m5.3-the-sales-assistant.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m5.3-the-sales-assistant.md)

Python TypeScript

<a id="the-sales-assistant"></a>


# The Sales Assistant

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/Nrg0yZ5FOeZ.md)

Lesson 1 covered what the Chinook Sales Assistant is and which Deep Agents features each part uses. Lesson 2 covered serving an agent with `langgraph dev`. This lesson presents the finished assistant, examines how little new code it requires, and runs it locally.

The assistant works for Jane Peacock, a Sales Support Agent at Chinook (an online music distributor). “Her book of business” means the customers whose support rep is Jane (`Customer.SupportRepId = 3` in the database). The assistant helps her answer quote requests, keep customer records current, research the market, and report on her territory.

---

<a id="how-it-fits-together"></a>


## How it fits together

Like any deployed agent, the assistant runs inside `langgraph dev` and is reached over HTTP by a chat UI. The distinguishing elements are what it draws on: the Chinook database, its sales playbooks, and mail.

The sales assistant, running locally

Chat UI Studio

HTTP

langgraph dev

Chinook Sales Assistant create\_deep\_agent(…)

Chinook DB SQL data

Sales playbooks skills / AGENTS.md

 mail MCP, mock

*The agent runs inside `langgraph dev` and draws on the database, its playbooks, and mail. A chat UI reaches it over HTTP.*

---

<a id="how-little-of-it-is-new-code"></a>


## How little of it is new code

The project structure shows how much of the agent’s behavior is defined by plain-text files rather than code:

```text
sales_assistant/
├── agent.py            # assembles the agent, the only "wiring" code
├── langgraph.json      # tells langgraph dev which graph to serve
├── start.sh            # starts mail server + langgraph dev
├── AGENTS.md           # operating manual: plain text, describes behavior
├── skills/             # one playbook per task: plain text, no code
│   ├── rfq-quote/
│   ├── weekly-newsletter/
│   └── territory-report/
├── subagents.py        # the four specialists
├── tools/              # tool code, each given to the agent that needs it
│   ├── sql.py          # → the chinook-analyst subagent
│   ├── html.py         # → the main agent (builds HTML deliverables)
│   ├── chart.py        # → the main agent (renders the territory chart)
│   └── search.py       # → the genre-researcher subagent
├── mcp/                # the mail MCP server; mail tools discovered here at startup
└── data/
    └── chinook.db      # the sales database (ships with the agent)
```

`AGENTS.md` and everything under `skills/` are natural language files, read directly by the model in any language it understands. The operating manual defines who the agent works for and how to behave; each skill is a playbook for one task. As covered in Lesson 1, most of the behavioral definition is natural language.

---

<a id="run-it"></a>


## Run it

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/dWsX1UbejTZ.md)

<a id="before-you-start"></a>


### Before you start

The assistant uses the shared `python/.env` from the course setup. Add `TAVILY_API_KEY` to enable newsletter web research, if you have not already done so. Remember to close the `langgraph dev` from the previous lesson.

<a id="running"></a>


### Running

The mock mail server must be running before the agent starts. `start.sh` launches the mail server, waits for it to accept connections, then starts `langgraph dev`.

```text
cd python/m5/sales_assistant
./start.sh
```

This starts the server on `http://localhost:2024` and opens LangGraph Studio. Studio is useful for stepping through the graph, but the human-approval steps (saving a draft or adding a customer) are more convenient with `agent-chat-ui`, which renders those pauses as inline approve / edit / reject cards.

<a id="chat-ui"></a>


### Chat UI

LangChain hosts a ready-made chat interface with no install required:

1. Open [agentchat.vercel.app](https://agentchat.vercel.app).
2. Set Deployment URL to `http://localhost:2024` and Assistant / Graph ID to `agent`.
3. Chat as normal. When the assistant saves an email draft or adds a customer, an approve / edit / reject card appears right in the conversation.

You can also self-host from the [agent-chat-ui repo](../../../../../readings/github-a0272d9ab735.md) with Node and `pnpm`, but the hosted version needs no setup.

<a id="what-it-can-do"></a>


### What it can do

The assistant supports three task sequences (these can take a couple of minutes to run):

1. Process an incoming RFQ: read a quote request from the inbox, look up the customer and prices, compute the quote exactly with the interpreter, have a reviewer subagent check it, draft the reply for approval, and log it. Try: `Check the inbox for any quote requests and process them.`
2. Write the weekly newsletter: fan out parallel research subagents (one per genre), then assemble an HTML newsletter on disk. *(requires `TAVILY_API_KEY`)* Try: `Write this week's "This Week in Music" newsletter.` Output is saved to `python/m5/sales_assistant/outputs/newsletter-<timestamp>.html`.
3. Report on the territory: pull metrics from the database and render a chart. Try: `How's my book of business looking? Give me a territory report.` Report is saved to `python/m5/sales_assistant/outputs/territory_report-<date>.md`; chart to `outputs/territory_chart.png`.

<a id="resetting-the-lab"></a>


### Resetting the lab

The mock inbox/drafts and the SQLite database can change as you run the assistant. To replay the RFQ flow, rerun the inbox seed helper from `python/m5/sales_assistant`:

```text
uv run python mcp/send_to_inbox.py --reset
```

If you approve an `add_customer` action, the local `data/chinook.db` file is modified. Restore it from git before rerunning the new-customer path if you want a clean starting point.

---

<a id="under-the-hood"></a>


### Under the hood

`start.sh` runs `agent.py`, a local FilesystemBackend agent with a QuickJS code interpreter and a dedicated chart tool.

`langgraph dev` points at a factory function in `agent.py` (`python/m5/sales_assistant/langgraph.json`):

```text
{
  "dependencies": ["../.."],
  "graphs": {
    "agent": "./agent.py:make_graph"
  },
  "env": "../../.env"
}
```

Unlike Lesson 2’s lab, this points at an async factory function. `langgraph dev` calls `make_graph()` on startup and serves the graph it returns, allowing `create_deep_agent` to run after the mail tools have been discovered from the MCP server.

<a id="the-code-that-wires-it-together"></a>


### The code that wires it together

`agent.py` wires together your agent and returns the assembled graph to the server.

Here is the complete `agent.py`:

<a id="agentpy-scroll"></a>


```python {23,44,49,50,52} # python/m5/sales\_assistant/agent.py “““Chinook Sales Assistant.

Uses a local FilesystemBackend, a QuickJS code interpreter for arithmetic and data prep, and a dedicated chart tool for rendering.

Start with: ./start.sh ““”

from **future** import annotations

import logging import os from pathlib import Path

from deepagents import create\_deep\_agent from deepagents.backends import FilesystemBackend from langchain\_mcp\_adapters.client import MultiServerMCPClient from langchain\_mcp\_adapters.sessions import StreamableHttpConnection from langchain\_quickjs import CodeInterpreterMiddleware from subagents import build\_subagents from tools.chart import render\_pie\_chart from tools.html import markdown\_to\_html

from models import strong\_model

logger = logging.getLogger(**name**)

HERE = Path(**file**).resolve().parent

SYSTEM\_PROMPT = ( “You are a sales assistant for Jane Peacock, a Sales Support Agent at” “Chinook, an online music distributor. Follow your operating manual (loaded” “from your memory) and use the matching playbook from /skills/ for each task.” )

MAIL\_SERVER: StreamableHttpConnection = {“transport”: “streamable\_http”, “url”: “http://127.0.0.1:5002/mcp”}

\_enable\_search = bool(os.environ.get(“TAVILY\_API\_KEY”)) if not \_enable\_search: logger.info(“TAVILY\_API\_KEY not set — newsletter research subagent disabled.”)

\_backend = FilesystemBackend(root\_dir=str(HERE), virtual\_mode=True)

async def make\_graph(): client = MultiServerMCPClient({“mock-mail”: MAIL\_SERVER}) mail\_tools = await client.get\_tools() return create\_deep\_agent( model=strong\_model, tools=[markdown\_to\_html, render\_pie\_chart], system\_prompt=SYSTEM\_PROMPT, subagents=build\_subagents(\_backend, enable\_search=\_enable\_search, mail\_tools=mail\_tools), skills=[“/skills”], memory=[“/AGENTS.md”], backend=\_backend, middleware=[CodeInterpreterMiddleware()], name=“chinook-sales-assistant”, ).with\_config({“recursion\_limit”: 50})

````text

</div>

<style>
#agentpy-scroll pre { max-height: 32em; overflow: auto; }
</style>

> **Note:** `make_graph` is an async factory. `langgraph.json` points at it; `langgraph dev` calls it. This is a factory function rather than a graph because the MCP tools are not known until run time, which prevents building the graph ahead of time.

And `subagents.py`, which defines the four specialists: `chinook-analyst`, `quote-reviewer`, `inbox-manager`, and `genre-researcher`.

```python {7,17,31,33,36}
# python/m5/sales_assistant/subagents.py

def build_subagents(
    backend: BackendProtocol,
    *,
    enable_search: bool,
    mail_tools: list,
) -> list[dict]:

    chinook_analyst = {
        "name": "chinook-analyst",
        "description": "Query the Chinook database ...",
        "system_prompt": ANALYST_PROMPT,
        "tools": [query_chinook, introspect_schema, add_customer],
        "model": model,
        "middleware": [MemoryMiddleware(backend=backend, sources=["/agents/chinook-analyst/AGENTS.md"])],
        "interrupt_on": {"add_customer": _APPROVE_EDIT_REJECT},
    }

    quote_reviewer = {
        "name": "quote-reviewer",
        "description": "Review a drafted quote ...",
        "system_prompt": REVIEWER_PROMPT,
        "model": strong_model,
    }

    inbox_manager = {
        "name": "inbox-manager",
        "description": "Read Jane's inbox ...",
        "system_prompt": INBOX_PROMPT,
        "tools": mail_tools,
        "model": model,
        "interrupt_on": {"mail_create_draft": _APPROVE_EDIT_REJECT},
    }

    subagents = [chinook_analyst, quote_reviewer, inbox_manager]

    if enable_search:
        genre_researcher = {
            "name": "genre-researcher",
            "description": "Research one music genre ...",
            "system_prompt": GENRE_PROMPT,
            "tools": [internet_search],
            "model": model,
            "permissions": [...],
        }
        subagents.append(genre_researcher)

    return subagents
````

The highlighted lines show the `mail_tools` parameter injected after MCP discovery, the `add_customer` gated write, `mail_tools` passed into inbox-manager, the `mail_create_draft` gated write, and the subagent list. The genre-researcher is conditional, present only when web search is configured.

Notice that the mail tools go only to inbox-manager. The approval gate on `mail_create_draft` is set on inbox-manager, so every draft it saves shows an approval card. If the main agent had the mail tools too, it could call `mail_create_draft` directly and skip that card, because the gate belongs to inbox-manager. The line in `AGENTS.md` saying “You have no email tools yourself” asks the model not to try, but leaving the tools out is what actually prevents it.

---

<a id="recap"></a>


## Recap

- The Chinook Sales Assistant runs inside `langgraph dev` and draws on the Chinook database, its sales playbooks, and mail.
- Most behavioral definition lives in natural language files (`AGENTS.md` and `skills/`). The code is focused on tools and subagents, assembled by a single `create_deep_agent(...)` call.

---

<a id="next"></a>


## Next

Continue to the next lesson on **async subagents**, for background work that shouldn’t block the main agent while it waits.

---

<a id="references"></a>


## References

**Documentation:**

- [Deep Agents overview](../../../../../readings/docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md)
- [Run a local server (`langgraph dev`)](../../../../../readings/docs-langchain-com-oss-python-langgraph-local-server-eea49b6a.md)
- [agent-chat-ui](../../../../../readings/github-a0272d9ab735.md)

Lesson 1 covered what the Chinook Sales Assistant is and which Deep Agents features each part uses. Lesson 2 covered serving an agent with `langgraphjs dev`. This lesson presents the finished assistant, examines how little new code it requires, and runs it locally.

The assistant works for Jane Peacock, a Sales Support Agent at Chinook (an online music distributor). “Her book of business” means the customers whose support rep is Jane (`Customer.SupportRepId = 3` in the database). The assistant helps her answer quote requests, keep customer records current, research the market, and report on her territory.

---

<a id="how-it-fits-together-1"></a>


## How it fits together

Like any deployed agent, the assistant runs inside `langgraphjs dev` and is reached over HTTP by a chat UI. The distinguishing elements are what it draws on: the Chinook database, its sales playbooks, and mail.

The sales assistant, running locally

Chat UI agent-chat-ui

HTTP

langgraphjs dev

Chinook Sales Assistant createDeepAgent(…)

Chinook DB SQL data

Sales playbooks skills / AGENTS.md

 mail MCP, mock

*The agent runs inside `langgraphjs dev` and draws on the database, its playbooks, and mail. A chat UI reaches it over HTTP.*

---

<a id="how-little-of-it-is-new-code-1"></a>


## How little of it is new code

The project structure shows how much of the agent’s behavior is defined by plain-text files rather than code:

```text
sales_assistant/
├── agent.ts            # assembles the agent, the only "wiring" code
├── langgraph.json      # tells langgraphjs dev which graph to serve
├── start.sh            # starts mail server + langgraphjs dev
├── AGENTS.md           # operating manual: plain text, describes behavior
├── skills/             # one playbook per task: plain text, no code
│   ├── rfq-quote/
│   ├── weekly-newsletter/
│   └── territory-report/
├── subagents.ts        # the four specialists
├── tools/              # tool code, each given to the agent that needs it
│   ├── sql.ts          # → the chinook-analyst subagent
│   ├── html.ts         # → the main agent (builds HTML deliverables)
│   ├── chart.ts        # → the main agent (renders the territory chart)
│   └── search.ts       # → the genre-researcher subagent
├── mcp/                # the mail MCP server; mail tools discovered here at startup
└── data/
    └── chinook.db      # the sales database (ships with the agent)
```

`AGENTS.md` and everything under `skills/` are natural language files, read directly by the model in any language it understands. The operating manual defines who the agent works for and how to behave; each skill is a playbook for one task. As covered in Lesson 1, most of the behavioral definition is natural language.

---

<a id="run-it-1"></a>


## Run it

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/dWsX1UbejTZ.md)

<a id="before-you-start-1"></a>


### Before you start

The assistant uses the shared `typescript/.env` from the course setup. Add `TAVILY_API_KEY` to enable newsletter web research, if you have not already done so. Remember to close the `langgraphjs dev` from the previous lesson.

<a id="running-1"></a>


### Running

`start.sh` launches the mock mail server, the local chat UI (`agent-chat-ui`), then starts `langgraphjs dev`.

```text
cd typescript/m5/sales_assistant
./start.sh
```

This starts the server on `http://localhost:2024` and opens LangGraph Studio. Studio is useful for stepping through the graph, but the human approval steps (saving a draft or adding a customer) are more convenient with `agent-chat-ui`, which renders those pauses as inline approve / edit / reject cards.

<a id="chat-ui-1"></a>


### Chat UI

`start.sh` already starts the chat UI for you:

1. Open [localhost:3000](http://localhost:3000).
2. Set Deployment URL to `http://localhost:2024` and Assistant / Graph ID to `agent`.
3. Chat as normal. When the assistant saves an email draft or adds a customer, an approve / edit / reject card appears right in the conversation.

<a id="what-it-can-do-1"></a>


### What it can do

The assistant supports three task sequences (these can take a couple of minutes to run):

1. Process an incoming RFQ: read a quote request from the inbox, look up the customer and prices, compute the quote exactly with the interpreter, have a reviewer subagent check it, draft the reply for approval, and log it. Try: `Check the inbox for any quote requests and process them.`
2. Write the weekly newsletter: fan out parallel research subagents (one per genre), then assemble an HTML newsletter on disk. *(requires `TAVILY_API_KEY`)* Try: `Write this week's "This Week in Music" newsletter.` Output is saved to `typescript/m5/sales_assistant/outputs/newsletter-<timestamp>.html`.
3. Report on the territory: pull metrics from the database and render a chart. Try: `How's my book of business looking? Give me a territory report.` Report is saved to `typescript/m5/sales_assistant/outputs/territory_report-<date>.md`; chart to `outputs/territory_chart.png`.

<a id="resetting-the-lab-1"></a>


### Resetting the lab

The mock inbox/drafts and the SQLite database can change as you run the assistant. To replay the RFQ flow, rerun the inbox seed helper:

```text
cd typescript/m5/sales_assistant
pnpm tsx ./mcp/send_to_inbox.ts --reset
```

If you approve an `add_customer` action, the local `data/chinook.db` file is modified. Restore it from git before rerunning the new-customer path if you want a clean starting point.

---

<a id="under-the-hood-1"></a>


### Under the hood

`start.sh` runs `agent.ts`, a local FilesystemBackend agent with a QuickJS code interpreter and a dedicated chart tool.

`langgraphjs dev` points at the exported graph in `agent.ts` (`typescript/m5/sales_assistant/langgraph.json`):

```text
{
  "dependencies": ["../.."],
  "graphs": {
    "agent": "./agent.ts:graph"
  },
  "env": "../../.env"
}
```

Unlike Lesson 2’s lab, this points directly at an exported `graph` rather than a factory function. `agent.ts` uses a top-level `await` to fetch the mail tools from the MCP client before that export exists, so `langgraphjs dev` still doesn’t serve the graph until the mail tools have been discovered — it just gets there by awaiting module evaluation instead of calling a factory function.

<a id="the-code-that-wires-it-together-1"></a>


### The code that wires it together

`agent.ts` wires together your agent and exports the assembled graph for the server.

Here is the complete `agent.ts`:

<a id="agentts-scroll"></a>


```typescript {21,36,41,43,45} // typescript/m5/sales\_assistant/agent.ts /\*\* \* Chinook Sales Assistant.  Uses a local FilesystemBackend, a QuickJS code interpreter for arithmetic \* and data prep, and a dedicated chart tool for rendering.  Start with: \* ./start.sh \*/ import { dirname } from “node:path”; import { fileURLToPath } from “node:url”;

import { MultiServerMCPClient } from “@langchain/mcp-adapters”; import { createCodeInterpreterMiddleware } from “@langchain/quickjs”; import { context } from “langchain”; import { FilesystemBackend, createDeepAgent } from “deepagents”;

import { strongModel } from “../../models.js”; import { buildSubagents } from “./subagents.js”; import { renderPieChart } from “./tools/chart.js”; import { markdownToHtml } from “./tools/html.js”;

const HERE = dirname(fileURLToPath(import.meta.url));

const SYSTEM\_PROMPT = context`You are a sales assistant for Jane Peacock, a Sales Support Agent at Chinook, an online music distributor. Follow your operating manual (loaded from your memory) and use the matching playbook from /skills/ for each task.`;

const enableSearch = Boolean(process.env.TAVILY\_API\_KEY); if (!enableSearch) { console.log(“TAVILY\_API\_KEY not set — newsletter research subagent disabled.”); }

const backend = new FilesystemBackend({ rootDir: HERE, virtualMode: true });

const client = new MultiServerMCPClient({ “mock-mail”: { transport: “http”, url: “http://127.0.0.1:5002/mcp” }, }); const mailTools = await client.getTools();

export const graph = createDeepAgent({ model: strongModel, tools: [markdownToHtml, renderPieChart], systemPrompt: SYSTEM\_PROMPT, subagents: buildSubagents(backend, { enableSearch, mailTools }), skills: [“/skills”], memory: [“/AGENTS.md”], backend, middleware: [createCodeInterpreterMiddleware({ executionTimeoutMs: 180\_000 })], name: “chinook-sales-assistant”, }).withConfig({ recursionLimit: 50 });

````text

</div>

<style>
#agentts-scroll pre { max-height: 32em; overflow: auto; }
</style>

> **Note:** There's no separate factory function here. `agent.ts` performs a top-level `await` to fetch `mailTools` from the MCP client, so the module doesn't finish evaluating (and `graph` isn't exported) until those tools are available. `langgraph.json` points `"agent": "./agent.ts:graph"` directly at that export; `langgraphjs dev` awaits the module's evaluation before serving it.

And `subagents.ts`, which defines the four specialists: `chinook-analyst`, `quote-reviewer`, `inbox-manager`, and `genre-researcher`.

```typescript {5,19,33,35,38}
// typescript/m5/sales_assistant/subagents.ts

export function buildSubagents(
  backend: AnyBackendProtocol,
  { enableSearch, mailTools }: BuildSubagentsOptions
): SubAgent[] {
  const chinookAnalyst: SubAgent = {
    name: "chinook-analyst",
    description: context`Query the Chinook database ...`,
    systemPrompt: ANALYST_PROMPT,
    tools: [queryChinook, introspectSchema, addCustomer],
    model,
    middleware: [
      createMemoryMiddleware({
        backend,
        sources: ["/agents/chinook-analyst/AGENTS.md"],
      }),
    ],
    interruptOn: { add_customer: APPROVE_EDIT_REJECT },
  };

  const quoteReviewer: SubAgent = {
    name: "quote-reviewer",
    description: context`Review a drafted quote ...`,
    systemPrompt: REVIEWER_PROMPT,
    model: strongModel,
  };

  const inboxManager: SubAgent = {
    name: "inbox-manager",
    description: context`Read Jane's inbox ...`,
    systemPrompt: INBOX_PROMPT,
    tools: mailTools,
    model,
    interruptOn: { mail_create_draft: APPROVE_EDIT_REJECT },
  };

  const subagents: SubAgent[] = [chinookAnalyst, quoteReviewer, inboxManager];

  if (enableSearch) {
    const genreResearcher: SubAgent = {
      name: "genre-researcher",
      description: context`Research one music genre ...`,
      systemPrompt: GENRE_PROMPT,
      tools: [internetSearch],
      model,
      permissions: [...],
    };
    subagents.push(genreResearcher);
  }

  return subagents;
}
````

The highlighted lines show the `mailTools` parameter injected after MCP discovery, the `add_customer` gated write, `mailTools` passed into inbox-manager, the `mail_create_draft` gated write, and the subagent list. The genre-researcher is conditional, present only when web search is configured.

Notice that the mail tools go only to inbox-manager. The approval gate on `mail_create_draft` is set on inbox-manager, so every draft it saves shows an approval card. If the main agent had the mail tools too, it could call `mail_create_draft` directly and skip that card, because the gate belongs to inbox-manager. The line in `AGENTS.md` saying “You have no email tools yourself” asks the model not to try, but leaving the tools out is what actually prevents it.

---

<a id="recap-1"></a>


## Recap

- The Chinook Sales Assistant runs inside `langgraphjs dev` and draws on the Chinook database, its sales playbooks, and mail.
- Most behavioral definition lives in natural language files (`AGENTS.md` and `skills/`). The code is focused on tools and subagents, assembled by a single `createDeepAgent(...)` call.

---

<a id="next-1"></a>


## Next

Continue to the next lesson on **async subagents**, for background work that shouldn’t block the main agent while it waits.

---

<a id="references-1"></a>


## References

**Documentation:**

- [Deep Agents overview](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-overview-9687b9be.md)
- [Run a local server (`langgraphjs dev`)](../../../../../readings/docs-langchain-com-oss-javascript-langgraph-local-server-9c862fd1.md)
- [agent-chat-ui](../../../../../readings/github-a0272d9ab735.md)
