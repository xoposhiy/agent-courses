# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/next.config.mjs

[Course index](../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/next.config.mjs) · [Raw file](../../../../raw/repositories/lca-deepagents/agent-chat-ui/next.config.mjs)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```mjs
/** @type {import('next').NextConfig} */
const nextConfig = {
  // ws (via langsmith/sandbox's exec/streaming path) relies on native
  // bufferutil/utf-8-validate bindings that webpack mis-bundles for server
  // routes — keep it external so Node's own require loads it instead.
  serverExternalPackages: ["ws"],
  experimental: {
    serverActions: {
      bodySizeLimit: "10mb",
    },
  },
};

export default nextConfig;

```
