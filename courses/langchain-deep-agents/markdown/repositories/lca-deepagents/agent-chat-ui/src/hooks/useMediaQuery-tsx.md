# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/hooks/useMediaQuery.tsx

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/hooks/useMediaQuery.tsx) · [Raw file](../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/hooks/useMediaQuery.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
import { useEffect, useState } from "react";

export function useMediaQuery(query: string) {
  const [matches, setMatches] = useState(false);

  useEffect(() => {
    const media = window.matchMedia(query);
    setMatches(media.matches);

    const listener = (e: MediaQueryListEvent) => setMatches(e.matches);
    media.addEventListener("change", listener);
    return () => media.removeEventListener("change", listener);
  }, [query]);

  return matches;
}

```
