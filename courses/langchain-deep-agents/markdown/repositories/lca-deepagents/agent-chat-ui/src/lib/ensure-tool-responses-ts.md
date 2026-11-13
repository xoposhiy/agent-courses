# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/lib/ensure-tool-responses.ts

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/lib/ensure-tool-responses.ts) · [Raw file](../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/lib/ensure-tool-responses.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { v4 as uuidv4 } from "uuid";
import { Message, ToolMessage } from "@langchain/langgraph-sdk";

export const DO_NOT_RENDER_ID_PREFIX = "do-not-render-";

export function ensureToolCallsHaveResponses(messages: Message[]): Message[] {
  const newMessages: ToolMessage[] = [];

  messages.forEach((message, index) => {
    if (message.type !== "ai" || message.tool_calls?.length === 0) {
      // If it's not an AI message, or it doesn't have tool calls, we can ignore.
      return;
    }
    // If it has tool calls, ensure the message which follows this is a tool message
    const followingMessage = messages[index + 1];
    if (followingMessage && followingMessage.type === "tool") {
      // Following message is a tool message, so we can ignore.
      return;
    }

    // Since the following message is not a tool message, we must create a new tool message
    newMessages.push(
      ...(message.tool_calls?.map((tc) => ({
        type: "tool" as const,
        tool_call_id: tc.id ?? "",
        id: `${DO_NOT_RENDER_ID_PREFIX}${uuidv4()}`,
        name: tc.name,
        content: "Successfully handled tool call.",
      })) ?? []),
    );
  });

  return newMessages;
}

```
