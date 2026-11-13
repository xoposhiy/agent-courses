# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/ui/sonner.tsx

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/ui/sonner.tsx) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/ui/sonner.tsx)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```tsx
import { useTheme } from "next-themes";
import { Toaster as Sonner, ToasterProps } from "sonner";

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme();

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      toastOptions={{
        classNames: {
          toast:
            "group toast group-[.toaster]:bg-background group-[.toaster]:text-foreground group-[.toaster]:border-border group-[.toaster]:shadow-lg",
          description: "group-[.toast]:text-muted-foreground",
          actionButton:
            "group-[.toast]:bg-primary group-[.toast]:text-primary-foreground font-medium",
          cancelButton:
            "group-[.toast]:bg-muted group-[.toast]:text-muted-foreground font-medium",
        },
      }}
      {...props}
    />
  );
};

export { Toaster };

```
