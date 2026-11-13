# Official course repository: Python, TypeScript, lesson sources, and agent UI: typescript/m2/m2.4_eval_agent.ts

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/typescript/m2/m2.4_eval_agent.ts) · [Raw file](../../../../../raw/repositories/lca-deepagents/typescript/m2/m2.4_eval_agent.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
// typescript/m2/m2.4_eval_agent.ts
import { createCodeInterpreterMiddleware } from "@langchain/quickjs";
import { createDeepAgent } from "deepagents";

import { model } from "../models.js";

const agent = createDeepAgent({
  model,
  middleware: [createCodeInterpreterMiddleware()],
});

const result = await agent.invoke({
  messages: [
    {
      role: "user",
      content: "Use the eval tool to compute and return the first 15 Fibonacci numbers.",
    },
  ],
});

console.log(result.messages.at(-1)?.text);

```
