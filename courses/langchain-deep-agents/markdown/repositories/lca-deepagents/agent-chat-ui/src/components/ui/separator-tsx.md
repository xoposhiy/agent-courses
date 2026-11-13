# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/ui/separator.tsx

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/ui/separator.tsx) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/ui/separator.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
import * as React from "react";
import * as SeparatorPrimitive from "@radix-ui/react-separator";

import { cn } from "@/lib/utils";

function Separator({
  className,
  orientation = "horizontal",
  decorative = true,
  ...props
}: React.ComponentProps<typeof SeparatorPrimitive.Root>) {
  return (
    <SeparatorPrimitive.Root
      data-slot="separator-root"
      decorative={decorative}
      orientation={orientation}
      className={cn(
        "bg-border shrink-0 data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px",
        className,
      )}
      {...props}
    />
  );
}

export { Separator };

```
