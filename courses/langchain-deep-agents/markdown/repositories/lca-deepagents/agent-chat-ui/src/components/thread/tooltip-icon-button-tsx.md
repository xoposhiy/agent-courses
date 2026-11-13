# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/thread/tooltip-icon-button.tsx

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/thread/tooltip-icon-button.tsx) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/thread/tooltip-icon-button.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
"use client";

import { forwardRef } from "react";

import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Button, ButtonProps } from "@/components/ui/button";
import { cn } from "@/lib/utils";

export type TooltipIconButtonProps = ButtonProps & {
  tooltip: string;
  side?: "top" | "bottom" | "left" | "right";
};

export const TooltipIconButton = forwardRef<
  HTMLButtonElement,
  TooltipIconButtonProps
>(({ children, tooltip, side = "bottom", className, ...rest }, ref) => {
  return (
    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger asChild>
          <Button
            variant="ghost"
            size="icon"
            {...rest}
            className={cn("size-6 p-1", className)}
            ref={ref}
          >
            {children}
            <span className="sr-only">{tooltip}</span>
          </Button>
        </TooltipTrigger>
        <TooltipContent side={side}>{tooltip}</TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
});

TooltipIconButton.displayName = "TooltipIconButton";

```
