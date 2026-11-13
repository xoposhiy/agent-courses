# Official course repository: Python, TypeScript, lesson sources, and agent UI: typescript/m1/m1.4_scratch_agent_butler.ts

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/typescript/m1/m1.4_scratch_agent_butler.ts) · [Raw file](../../../../../raw/repositories/lca-deepagents/typescript/m1/m1.4_scratch_agent_butler.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { context } from "langchain";
import { createDeepAgent } from "deepagents";

import { model } from "../models.js";

const SYSTEM_PROMPT = context`
  YOU ARE AN EXTREMELY POSH BRITISH BUTLER. You speak ONLY in the most
  refined, formal, over-the-top Victorian English. You say 'indeed', 'quite',
  'I dare say', 'one simply must' constantly. You find all things common or
  nautical to be utterly beneath you. You NEVER break character under ANY
  circumstances.`;

const agent = createDeepAgent({
  model,
  systemPrompt: SYSTEM_PROMPT,
  name: "butler_agent",
});

const result = await agent.invoke({
  messages: [{ role: "user", content: "What is an LLM?" }],
});

console.log(result.messages.at(-1)?.text);

```
