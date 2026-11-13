# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/thread/ContentBlocksPreview.tsx

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/thread/ContentBlocksPreview.tsx) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/thread/ContentBlocksPreview.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
import React from "react";
import { MultimodalPreview } from "./MultimodalPreview";
import { cn } from "@/lib/utils";
import { ContentBlock } from "@langchain/core/messages";

interface ContentBlocksPreviewProps {
  blocks: ContentBlock.Multimodal.Data[];
  onRemove: (idx: number) => void;
  size?: "sm" | "md" | "lg";
  className?: string;
}

/**
 * Renders a preview of content blocks with optional remove functionality.
 * Uses cn utility for robust class merging.
 */
export const ContentBlocksPreview: React.FC<ContentBlocksPreviewProps> = ({
  blocks,
  onRemove,
  size = "md",
  className,
}) => {
  if (!blocks.length) return null;
  return (
    <div className={cn("flex flex-wrap gap-2 p-3.5 pb-0", className)}>
      {blocks.map((block, idx) => (
        <MultimodalPreview
          key={idx}
          block={block}
          removable
          onRemove={() => onRemove(idx)}
          size={size}
        />
      ))}
    </div>
  );
};

```
