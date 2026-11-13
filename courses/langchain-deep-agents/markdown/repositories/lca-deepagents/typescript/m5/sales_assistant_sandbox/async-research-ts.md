# Official course repository: Python, TypeScript, lesson sources, and agent UI: typescript/m5/sales_assistant_sandbox/async-research.ts

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/typescript/m5/sales_assistant_sandbox/async-research.ts) · [Raw file](../../../../../../raw/repositories/lca-deepagents/typescript/m5/sales_assistant_sandbox/async-research.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
// typescript/m5/sales_assistant_sandbox/async-research.ts
/** createAsyncSubAgentMiddleware wiring for the newsletter-agent async subagent. */
import { createAsyncSubAgentMiddleware } from "deepagents";

/**
 * `createAsyncSubAgentMiddleware`, wired to the co-deployed newsletter-agent
 * graph, using the stock `start_async_task` tool unmodified — newsletter-agent
 * doesn't need any parent-thread context passed in, so there's nothing to add
 * to the launch call.
 */
export function buildAsyncResearchMiddleware() {
  return createAsyncSubAgentMiddleware({
    asyncSubAgents: [
      {
        name: "newsletter-agent",
        description:
          "Research this week's featured music genres and assemble the " +
          "styled HTML newsletter in the background. Launch it once per " +
          "newsletter request and keep working; check back on it later " +
          "with check_async_task/list_async_tasks to get the finished HTML.",
        graphId: "newsletter-agent",
      },
    ],
  });
}

```
