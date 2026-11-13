# Official course repository: Python, TypeScript, lesson sources, and agent UI: typescript/m1/m1.6_dice_server.ts

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/typescript/m1/m1.6_dice_server.ts) · [Raw file](../../../../../raw/repositories/lca-deepagents/typescript/m1/m1.6_dice_server.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "dice", version: "1.0.0" });

server.registerTool(
  "roll_dice",
  {
    description: "Roll a die with the given number of sides and return the result.",
    inputSchema: { sides: z.number().int().default(6) },
  },
  // the same tool as Lesson 1.5
  async ({ sides }) => ({
    content: [{ type: "text", text: String(Math.floor(Math.random() * sides) + 1) }],
  }),
);

await server.connect(new StdioServerTransport()); // start the server and wait for a client

```
