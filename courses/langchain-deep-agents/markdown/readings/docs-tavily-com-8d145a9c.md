# Assigned reference: 

[Course index](../../README.md) · [Original source](https://docs.tavily.com/) · [Raw file](../../raw/readings/docs-tavily-com-8d145a9c.html)

Retrieved: 2026-11-13T17:01:37.390532+00:00

Get started

# Connect your AI agent to the web

Copy pageCopy page

Add Tavily’s web search, extraction, crawling, and research to Claude, Codex, Cursor, or any agent in one step, or call the API directly with a free API key.

Copy pageCopy page

Onboard your agent

Connect your agent to the web with Tavily. Get started for free.

[Get API key](https://app.tavily.com)

Tavily is the web layer for AI agents: real-time **search**, page **extraction**, site **crawling** and **mapping**, and cited **research**, returned as clean, LLM-ready content.

- ![](../../raw/assets/6dad309555bd8cc8.webp) Claude & Claude Code
- ![](../../raw/assets/3cc9924544b12ce8.webp) ChatGPT & Codex
- ![](../../raw/assets/1a5980c5643c5c0c.webp) Cursor
- ![](../../raw/assets/1be1e829778825df.png) OpenCode

Claude Code

```
claude mcp add tavily --transport http https://mcp.tavily.com/mcp/
```

**Claude** (claude.ai, Claude Desktop, and Cowork): click **Add to Claude**, then **Connect**, and sign in to Tavily. **Claude Code**: run the command above; Claude Code opens your browser to sign in to Tavily when you start a new session. See the [Claude guide](https://docs.tavily.com/documentation/integrations/claude) for the Tavily plugin and organization-wide access.

Codex

```
codex mcp add tavily --url https://mcp.tavily.com/mcp/
codex mcp login tavily
```

Click **Add to ChatGPT and Codex** to open the Tavily plugin, then connect it and sign in to Tavily. To use the MCP server in Codex instead, run the commands above. See the [MCP guide](https://docs.tavily.com/documentation/mcp) for other options.

mcp.json

```
{
  "mcpServers": {
    "tavily": {
      "url": "https://mcp.tavily.com/mcp/"
    }
  }
}
```

Click **Add to Cursor** and sign in to Tavily when Cursor prompts you, or add the server to `~/.cursor/mcp.json` yourself. For the recommended plugin setup, standalone options, and examples, see the [Cursor guide](https://docs.tavily.com/documentation/integrations/cursor).

Terminal

opencode.json

```
curl -fsSL https://cli.tavily.com/install.sh | bash
tvly login
```

```
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-tavily"]
}
```

Paste the setup prompt into OpenCode to let it set Tavily up, or install the Tavily CLI, sign in, and add the `opencode-tavily` plugin to your `opencode.json`. OpenCode installs the plugin on next launch. See the [OpenCode guide](https://docs.tavily.com/documentation/integrations/opencode) for details.

No account yet? [Keyless access](https://docs.tavily.com/documentation/keyless) lets you call Search and Extract with no API key.

## Make your first API call

Get a free [Tavily API key](https://app.tavily.com) (1,000 API credits every month, no credit card required), install an SDK, and replace `tvly-YOUR_API_KEY` with your key.

Python

JavaScript

cURL

```
# pip install tavily-python
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.search("Who is Leo Messi?")

print(response)
```

```
// npm i @tavily/core
const { tavily } = require("@tavily/core");

const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
const response = await tvly.search("Who is Leo Messi?");

console.log(response);
```

```
curl -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer tvly-YOUR_API_KEY" \
  -d '{"query": "Who is Leo Messi?"}'
```

Next, see the [Python](https://docs.tavily.com/sdk/python/quick-start) and [JavaScript](https://docs.tavily.com/sdk/javascript/quick-start) SDK guides, the [API reference](https://docs.tavily.com/documentation/api-reference/endpoint/search), or the [Getting Started notebook](https://colab.research.google.com/drive/1dWGtS3u4ocCLebuaa8Ivz7BkZ_40IgH1) for more advanced Python workflows.

## Coding agents

![](../../raw/assets/1a5980c5643c5c0c.webp)

## Cursor

![](../../raw/assets/1be1e829778825df.png)

## OpenCode

![](../../raw/assets/6dad309555bd8cc8.webp)

## Claude

![](../../raw/assets/2fb89a8378513521.svg)

## Hermes Agent

![](../../raw/assets/0e93eda5c0b41943.svg)

## Pi

![](../../raw/assets/3b1dfe8757e57539.png)

## NanoClaw

![](../../raw/assets/f662ad0a645afc18.svg)

## OpenClaw

![](../../raw/assets/b994fd144e9de378.png)

## Grok Build

## Any other agent

## Frameworks and platforms

![](../../raw/assets/c9a45aad534f145c.png)

## LangChain

![](../../raw/assets/c35d181e4a506aa9.png)

## OpenAI

![](../../raw/assets/e9f0ab03f47d9ad1.png)

## Vercel AI SDK

![](../../raw/assets/3944c6b538d8385c.png)

## n8n

![](../../raw/assets/695caba4957c8b5d.png)

## CrewAI

![](../../raw/assets/e279e6feb1f79b06.png)

## Mastra

Find more in the **Integrations** tab.

## Explore the API

## Search

Search the web for current, relevant sources.

## Extract

Pull clean content from one or more URLs.

## Research

Get a cited report from multi-source research.

## Crawl

Read many pages across a site.

## Map

Discover a site’s structure.

## Playground

Try the APIs in your browser.

## Need help?

Email [support@tavily.com](mailto:support@tavily.com), ask in the [community](https://community.tavily.com/), or check [Tavily status](https://status.tavily.com/).
