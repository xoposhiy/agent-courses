# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/tsconfig.json

[Course index](../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/tsconfig.json) · [Raw file](../../../../raw/repositories/lca-deepagents/agent-chat-ui/tsconfig.json)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```json
{
  "compilerOptions": {
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    },
    "target": "ES2017"
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    "src/hooks/use-threads",
    "src/app/thread/[threadId]"
  ],
  "exclude": ["node_modules"]
}

```
