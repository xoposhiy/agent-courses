# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/ui/skeleton.tsx

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/ui/skeleton.tsx) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/ui/skeleton.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
import { cn } from "@/lib/utils";

function Skeleton({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="skeleton"
      className={cn("bg-primary/10 animate-pulse rounded-md", className)}
      {...props}
    />
  );
}

export { Skeleton };

```
