# Official course repository: Python, TypeScript, lesson sources, and agent UI: agent-chat-ui/src/components/thread/agent-inbox/types.ts

[Course index](../../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/agent-chat-ui/src/components/thread/agent-inbox/types.ts) · [Raw file](../../../../../../../../raw/repositories/lca-deepagents/agent-chat-ui/src/components/thread/agent-inbox/types.ts)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```ts
import { BaseMessage } from "@langchain/core/messages";
import { Interrupt, Thread, ThreadStatus } from "@langchain/langgraph-sdk";

export type DecisionType = "approve" | "edit" | "reject";

export interface Action {
  name: string;
  args: Record<string, unknown>;
}

export interface ActionRequest {
  name: string;
  args: Record<string, unknown>;
  description?: string;
}

export interface ReviewConfig {
  action_name: string;
  allowed_decisions: DecisionType[];
  args_schema?: Record<string, unknown>;
}

export interface HITLRequest {
  action_requests: ActionRequest[];
  review_configs: ReviewConfig[];
}

export type Decision =
  | { type: "approve" }
  | { type: "reject"; message?: string }
  | { type: "edit"; edited_action: Action };

export type DecisionWithEdits =
  | { type: "approve" }
  | { type: "reject"; message?: string }
  | {
      type: "edit";
      edited_action: Action;
      acceptAllowed?: boolean;
      editsMade?: boolean;
    };

export type Email = {
  id: string;
  thread_id: string;
  from_email: string;
  to_email: string;
  subject: string;
  page_content: string;
  send_time: string | undefined;
  read?: boolean;
  status?: "in-queue" | "processing" | "hitl" | "done";
};

export interface ThreadValues {
  email: Email;
  messages: BaseMessage[];
  triage: {
    logic: string;
    response: string;
  };
}

export type ThreadData<
  ThreadValues extends Record<string, any> = Record<string, any>,
> = {
  thread: Thread<ThreadValues>;
} & (
  | {
      status: "interrupted";
      interrupts: Interrupt<HITLRequest>[] | undefined;
    }
  | {
      status: "idle" | "busy" | "error";
      interrupts?: never;
    }
);

export type ThreadStatusWithAll = ThreadStatus | "all";

export type SubmitType = DecisionType;

export interface AgentInbox {
  /**
   * A unique identifier for the inbox.
   */
  id: string;
  /**
   * The ID of the graph.
   */
  graphId: string;
  /**
   * The URL of the deployment. Either a localhost URL, or a deployment URL.
   */
  deploymentUrl: string;
  /**
   * Optional name for the inbox, used in the UI to label the inbox.
   */
  name?: string;
  /**
   * Whether or not the inbox is selected.
   */
  selected: boolean;
}

```
