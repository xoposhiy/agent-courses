# Official course repository: Python, TypeScript, lesson sources, and agent UI: typescript/m1/m1.7_messages_threads_checkpointers.ts

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/typescript/m1/m1.7_messages_threads_checkpointers.ts) · [Raw file](../../../../../raw/repositories/lca-deepagents/typescript/m1/m1.7_messages_threads_checkpointers.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { MemorySaver } from "@langchain/langgraph";
import { createDeepAgent } from "deepagents";

import { model } from "../models.js";

const agent = createDeepAgent({
  model,
  checkpointer: new MemorySaver(),
});

const threadA = { configurable: { thread_id: "m1-7-thread-a" } };
const threadB = { configurable: { thread_id: "m1-7-thread-b" } };

let result = await agent.invoke(
  { messages: [{ role: "user", content: "Remember that my favorite colour is blue." }] },
  threadA
);
console.log("Thread A, turn 1:");
console.log(result.messages.at(-1)?.text);

result = await agent.invoke(
  { messages: [{ role: "user", content: "What is my favorite colour?" }] },
  threadA
);
console.log("\nThread A, turn 2:");
console.log(result.messages.at(-1)?.text);

result = await agent.invoke(
  { messages: [{ role: "user", content: "What is my favorite colour?" }] },
  threadB
);
console.log("\nThread B, turn 1:");
console.log(result.messages.at(-1)?.text);

```
