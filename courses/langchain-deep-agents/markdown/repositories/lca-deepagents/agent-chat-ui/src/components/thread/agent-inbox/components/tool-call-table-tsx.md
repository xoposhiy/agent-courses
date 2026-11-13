# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/thread/agent-inbox/components/tool-call-table.tsx

[Course index](../../../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/thread/agent-inbox/components/tool-call-table.tsx) · [Raw file](../../../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/thread/agent-inbox/components/tool-call-table.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
import { ToolCall } from "@langchain/core/messages/tool";
import { unknownToPrettyDate } from "../utils";

export function ToolCallTable({ toolCall }: { toolCall: ToolCall }) {
  return (
    <div className="max-w-full min-w-[300px] overflow-hidden rounded-lg border">
      <table className="w-full border-collapse">
        <thead>
          <tr>
            <th
              className="bg-gray-100 px-2 py-0 text-left text-sm"
              colSpan={2}
            >
              {toolCall.name}
            </th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(toolCall.args).map(([key, value]) => {
            let valueStr = "";
            if (["string", "number"].includes(typeof value)) {
              valueStr = value.toString();
            }

            const date = unknownToPrettyDate(value);
            if (date) {
              valueStr = date;
            }

            try {
              valueStr = valueStr || JSON.stringify(value, null);
            } catch (_) {
              // failed to stringify, just assign an empty string
              valueStr = "";
            }

            return (
              <tr
                key={key}
                className="border-t"
              >
                <td className="w-1/3 px-2 py-1 text-xs font-medium">{key}</td>
                <td className="px-2 py-1 font-mono text-xs">{valueStr}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

```
