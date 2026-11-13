# Official course repository: Python, TypeScript, lesson sources, and agent UI: typescript/m1/m1.2_scratch_agent.ts

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/typescript/m1/m1.2_scratch_agent.ts) · [Raw file](../../../../../raw/repositories/lca-deepagents/typescript/m1/m1.2_scratch_agent.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { createDeepAgent } from "deepagents";

import { model } from "../models.js";

const agent = createDeepAgent({ model });

const result = await agent.invoke({
    messages: [{ role: "user", content: "What is an LLM?" }]
});

console.log(result.messages.at(-1)?.text);

```
