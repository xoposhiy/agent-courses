# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/app/api/[..._path]/route.ts

[Course index](../../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/app/api/[..._path]/route.ts) · [Raw file](../../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/app/api/[..._path]/route.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { initApiPassthrough } from "langgraph-nextjs-api-passthrough";

// This file acts as a proxy for requests to your LangGraph server.
// Read the [Going to Production](https://github.com/langchain-ai/agent-chat-ui?tab=readme-ov-file#going-to-production) section for more information.

export const { GET, POST, PUT, PATCH, DELETE, OPTIONS, runtime } =
  initApiPassthrough({
    apiUrl: process.env.LANGGRAPH_API_URL ?? "remove-me", // default, if not defined it will attempt to read process.env.LANGGRAPH_API_URL
    apiKey: process.env.LANGSMITH_API_KEY ?? "remove-me", // default, if not defined it will attempt to read process.env.LANGSMITH_API_KEY
    runtime: "edge", // default
  });

```
