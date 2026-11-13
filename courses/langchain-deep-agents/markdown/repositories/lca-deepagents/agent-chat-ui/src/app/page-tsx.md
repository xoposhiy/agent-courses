# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/app/page.tsx

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/app/page.tsx) · [Raw file](../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/app/page.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
"use client";

import { Thread } from "@/components/thread";
import { StreamProvider } from "@/providers/Stream";
import { ThreadProvider } from "@/providers/Thread";
import { ArtifactProvider } from "@/components/thread/artifact";
import { Toaster } from "@/components/ui/sonner";
import React from "react";

export default function DemoPage(): React.ReactNode {
  return (
    <React.Suspense fallback={<div>Loading (layout)...</div>}>
      <Toaster />
      <ThreadProvider>
        <StreamProvider>
          <ArtifactProvider>
            <Thread />
          </ArtifactProvider>
        </StreamProvider>
      </ThreadProvider>
    </React.Suspense>
  );
}

```
