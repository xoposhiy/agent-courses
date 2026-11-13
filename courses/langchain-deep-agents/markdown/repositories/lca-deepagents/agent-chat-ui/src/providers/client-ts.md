# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/providers/client.ts

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/providers/client.ts) · [Raw file](../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/providers/client.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { Client } from "@langchain/langgraph-sdk";

export function createClient(
  apiUrl: string,
  apiKey: string | undefined,
  authScheme: string | undefined,
) {
  return new Client({
    apiKey,
    apiUrl,
    ...(authScheme && {
      defaultHeaders: {
        "X-Auth-Scheme": authScheme,
      },
    }),
  });
}

```
