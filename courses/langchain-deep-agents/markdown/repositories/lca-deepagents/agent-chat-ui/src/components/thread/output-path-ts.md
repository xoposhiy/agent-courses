# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/thread/output-path.ts

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/thread/output-path.ts) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/thread/output-path.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
// Shared between messages/ai.tsx (inline download links) and
// async-task-status.tsx (the "report ready" check) so both recognize the
// same /outputs/<file> shape the sandbox filesystem actually produces.
export const OUTPUT_PATH_RE = /\/outputs\/[A-Za-z0-9._-]+\.[A-Za-z0-9]+/g;

export function findOutputPaths(text: string): string[] {
  return Array.from(new Set(text.match(OUTPUT_PATH_RE) ?? []));
}

```
