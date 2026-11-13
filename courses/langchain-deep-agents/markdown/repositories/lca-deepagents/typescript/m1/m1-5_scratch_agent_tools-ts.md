# Official course repository: Python, TypeScript, lesson sources, and agent UI: typescript/m1/m1.5_scratch_agent_tools.ts

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/typescript/m1/m1.5_scratch_agent_tools.ts) · [Raw file](../../../../../raw/repositories/lca-deepagents/typescript/m1/m1.5_scratch_agent_tools.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { DatabaseSync } from "node:sqlite";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import { z } from "zod";
import { tool } from "langchain";
import { createDeepAgent } from "deepagents";

import { model } from "../models.js";

const __dirname = dirname(fileURLToPath(import.meta.url));
const DB_PATH = join(__dirname, "chinook.db");
const db = new DatabaseSync(DB_PATH);

const SYSTEM_PROMPT = `You are a SQL analyst with access to the Chinook music store database.

Rules:
- Use read_sql for SELECT queries.
- Do not modify the database.
- If a tool returns an error, revise the SQL and try again.
- Show your SQL in your final answer.
`;

const readSql = tool(
  ({ query }) => {
    try {
      const rows = db.prepare(query).all();
      return JSON.stringify(rows);
    } catch (e) {
      return `Error: ${e}`;
    }
  },
  {
    name: "read_sql",
    description: "Run a read-only SELECT query against the Chinook music store database.",
    schema: z.object({ query: z.string() }),
  }
);

const agent = createDeepAgent({
  model,
  name: "SQL_Agent",
  tools: [readSql],
  systemPrompt: SYSTEM_PROMPT,
});

const result = await agent.invoke({
  messages: [{ role: "user", content: "Which five genres have the most tracks?" }],
});

console.log(result.messages.at(-1)?.text);

```
