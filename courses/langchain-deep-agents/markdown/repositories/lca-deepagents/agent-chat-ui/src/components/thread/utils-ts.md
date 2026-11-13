# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/thread/utils.ts

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/thread/utils.ts) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/thread/utils.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import type { Message } from "@langchain/langgraph-sdk";

/**
 * Extracts a string summary from a message's content, supporting multimodal (text, image, file, etc.).
 * - If text is present, returns the joined text.
 * - If not, returns a label for the first non-text modality (e.g., 'Image', 'Other').
 * - If unknown, returns 'Multimodal message'.
 */
export function getContentString(content: Message["content"]): string {
  if (typeof content === "string") return content;
  const texts = content
    .filter((c): c is { type: "text"; text: string } => c.type === "text")
    .map((c) => c.text);
  return texts.join(" ");
}

```
