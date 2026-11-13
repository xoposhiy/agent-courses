# Assigned repository reference: /modelcontextprotocol/typescript-sdk

[Course index](../../README.md) · [Original source](https://github.com/modelcontextprotocol/typescript-sdk) · [Raw file](../../raw/readings/github-f7fb7d70e0ff.html)

Retrieved: 2026-11-13T17:02:09.458217+00:00

# MCP TypeScript SDK

Important

**This is the `main` branch: v2 of the SDK** (`@modelcontextprotocol/server`, `@modelcontextprotocol/client`), the stable release line, implementing the [2026-07-28 MCP spec](modelcontextprotocol-io-specification-latest-575ced6e.md). Start with the [v2 documentation](https://ts.sdk.modelcontextprotocol.io/v2/); coming from v1, see the [migration guide](https://ts.sdk.modelcontextprotocol.io/v2/migration/upgrade-to-v2).

**v1.x** (`@modelcontextprotocol/sdk`) lives on the [`v1.x` branch](https://github.com/modelcontextprotocol/typescript-sdk/tree/v1.x) and continues to receive bug fixes and security updates for at least six months after the v2 release (2026-07-27). Its documentation is at [ts.sdk.modelcontextprotocol.io](https://ts.sdk.modelcontextprotocol.io/).

Found a problem in v2? [Open an issue](https://github.com/modelcontextprotocol/typescript-sdk/issues/new?template=v2-feedback.yml).

Note

**Contributors without write access can have one open pull request at a time.** Draft pull requests don't count toward the limit. For a feature or a larger change, please [open an issue](https://github.com/modelcontextprotocol/typescript-sdk/issues/new/choose) first; see [CONTRIBUTING.md](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/CONTRIBUTING.md).

[![NPM Version - Server](../../raw/assets/2bc3d046efd54e5e.png)](https://www.npmjs.com/package/@modelcontextprotocol/server)
[![NPM Version - Client](../../raw/assets/78de2490ac769be4.png)](https://www.npmjs.com/package/@modelcontextprotocol/client) [![Apache-2.0 licensed](../../raw/assets/a5f2d6204a3ddd45.png)](https://camo.githubusercontent.com/07dc8c386e01cdb16650d1924c3b40eee6edb7a49206e6251ae22c512357035f/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f2534306d6f64656c636f6e7465787470726f746f636f6c253246736572766572)

Table of Contents

- [Overview](github-f7fb7d70e0ff.md)
- [Packages](github-f7fb7d70e0ff.md)
- [Installation](github-f7fb7d70e0ff.md)
- [Getting Started](github-f7fb7d70e0ff.md)
- [Documentation](github-f7fb7d70e0ff.md)
- [Contributing](github-f7fb7d70e0ff.md)
- [License](github-f7fb7d70e0ff.md)

## Overview

The Model Context Protocol (MCP) allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction.

This repository contains the TypeScript SDK implementation of the MCP specification. It runs on **Node.js**, **Bun**, and **Deno**, and ships:

- MCP **server** libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)
- MCP **client** libraries (transports, high-level helpers, OAuth helpers)
- Optional **middleware packages** for specific runtimes/frameworks (Express, Fastify, Hono, Node.js HTTP)
- Runnable **examples** (under [`examples/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples))

## Packages

This monorepo publishes split packages:

- **`@modelcontextprotocol/server`**: build MCP servers
- **`@modelcontextprotocol/client`**: build MCP clients

Tool and prompt schemas use [Standard Schema](https://standardschema.dev/) — bring Zod v4, Valibot, ArkType, or any compatible library.

### Middleware packages (optional)

The SDK also publishes small "middleware" packages under [`packages/middleware/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/packages/middleware) that help you **wire MCP into a specific runtime or web framework**.

They are intentionally thin adapters: they should not introduce new MCP functionality or business logic. See [`packages/middleware/README.md`](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md) for details.

- **`@modelcontextprotocol/node`**: Node.js Streamable HTTP transport wrapper for `IncomingMessage` / `ServerResponse`
- **`@modelcontextprotocol/express`**: Express helpers (app defaults + Host header validation)
- **`@modelcontextprotocol/fastify`**: Fastify helpers (app defaults + Host header validation)
- **`@modelcontextprotocol/hono`**: Hono helpers (app defaults + JSON body parsing hook + Host header validation)

## Installation

### Server

```
npm install @modelcontextprotocol/server
# or
bun add @modelcontextprotocol/server
# or
deno add npm:@modelcontextprotocol/server
```

### Client

```
npm install @modelcontextprotocol/client
# or
bun add @modelcontextprotocol/client
# or
deno add npm:@modelcontextprotocol/client
```

### Optional middleware packages

The SDK also publishes optional “middleware” packages that help you **wire MCP into a specific runtime or web framework** (for example Express, Fastify, Hono, or Node.js `http`).

These packages are intentionally thin adapters and should not introduce additional MCP features or business logic. See [`packages/middleware/README.md`](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/packages/middleware/README.md) for details.

```
# Node.js HTTP (IncomingMessage/ServerResponse) Streamable HTTP transport:
npm install @modelcontextprotocol/node

# Express integration:
npm install @modelcontextprotocol/express express

# Fastify integration:
npm install @modelcontextprotocol/fastify fastify

# Hono integration:
npm install @modelcontextprotocol/hono hono
```

## Getting Started

Here is what an MCP server looks like. This minimal example exposes a single `greet` tool over stdio:

```
import { McpServer } from '@modelcontextprotocol/server';
import { StdioServerTransport } from '@modelcontextprotocol/server/stdio';
import * as z from 'zod/v4';

const server = new McpServer({ name: 'greeting-server', version: '1.0.0' });

server.registerTool(
    'greet',
    {
        description: 'Greet someone by name',
        inputSchema: z.object({ name: z.string() })
    },
    async ({ name }) => ({
        content: [{ type: 'text', text: `Hello, ${name}!` }]
    })
);

async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
}

main();
```

Ready to build something real? Follow the step-by-step tutorials:

- [Build your first server](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) — a stdio weather-alert server, from `npm init` to a tool call
- [Build your first client](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) — connect to that server, list its tools, and call them

For runnable, end-to-end examples beyond the tutorials, see:

- [`examples/README.md`](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/README.md) — runnable, self-verifying client/server example pairs (one story per directory)

## Documentation

- [Build a server](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-server.md) — your first MCP server, step by step
- [Build a client](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/get-started/first-client.md) — your first MCP client, step by step
- [Documentation site](https://ts.sdk.modelcontextprotocol.io/v2/) — the full guides: tools, resources, prompts, serving over HTTP and stdio, clients, OAuth, and migration
- [Troubleshooting](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/troubleshooting.md) — common errors and their fixes
- [API reference](https://ts.sdk.modelcontextprotocol.io/v2/api/)
- [MCP documentation](https://modelcontextprotocol.io/docs)
- [MCP specification](modelcontextprotocol-io-specification-latest-575ced6e.md)

### Building docs locally

To work on the documentation site locally:

```
pnpm docs:api      # Generate the API reference markdown (output: docs/api/)
pnpm docs:dev      # Start the VitePress dev server for the V2 site
pnpm docs:build    # Build the V2 site (output: docs/.vitepress/dist/)
pnpm docs:multi    # Build the combined V1 + V2 site (output: tmp/docs-combined/)
```

The `docs:multi` script builds the V2 site from the current checkout, checks out the `v1.x` branch via a git worktree to build the V1 site, and produces a combined site with V1 docs at the root and V2 docs under `/v2/`.

## v1 (legacy) documentation and fixes

If you are using the **v1** generation of the SDK, the **v1 API documentation** is available at [`https://ts.sdk.modelcontextprotocol.io/`](https://ts.sdk.modelcontextprotocol.io/). The v1 source code and any v1-specific fixes live on the long-lived
[`v1.x` branch](https://github.com/modelcontextprotocol/typescript-sdk/tree/v1.x). V2 API docs are at [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/).

## Contributing

Issues and pull requests are welcome on GitHub at <https://github.com/modelcontextprotocol/typescript-sdk>.

## License

This project is licensed under the Apache License 2.0 for new contributions, with existing code under MIT. See the [LICENSE](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/LICENSE) file for details.
