# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/lib/api-key.tsx

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/lib/api-key.tsx) · [Raw file](../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/lib/api-key.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
export function getApiKey(): string | null {
  try {
    if (typeof window === "undefined") return null;
    return window.localStorage.getItem("lg:chat:apiKey") ?? null;
  } catch {
    // no-op
  }

  return null;
}

```
