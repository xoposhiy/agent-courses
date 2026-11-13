# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/lib/utils.ts

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/lib/utils.ts) · [Raw file](../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/lib/utils.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

```
