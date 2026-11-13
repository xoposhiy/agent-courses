# Chapter 11 How Agents Use Tools to Act in the World

[Course index](../../README.md) · [Original source](https://arxiv.org/html/2610.13455v1#Ch11) · [Raw file](../../raw/originals/book.html)

Retrieved: 2026-11-13T16:41:17.579179+00:00

[Contents](../../CONTENTS.md) · [Full book](../book/full-book-html.md) · [Previous chapter](chapter-10-case-study-2-balrog-for-llm-reasoning-and-reflection.md) · [Next chapter](chapter-12-search-and-retrieval-in-agentic-llms.md)

<a id="Ch11"></a>


### Chapter 11 How Agents Use Tools to Act in the World

**What You Will Learn**

In this chapter you will learn how agentic Large Language Models connect to the external world through tools. Specifically, you will be able to:

- Explain why *tools* are essential for agents that act beyond pure language generation.
- Distinguish between the direct invocation and *Planner–Caller–Summarizer* architectural patterns.
- Work with toolchains and frameworks such as *LangChain* and the *ReAct* loop, and understand how agents interact with browsers and desktop environments.
- Describe the *Model Context Protocol* as a standardized approach to tool integration.
- Reason about robustness, error recovery, and the *safety* and security risks that arise when agents are given access to external tools.

<a id="Ch11.S1"></a>


#### 11.1 Why Tools Matter in Agentic LLMs

In the taxonomy of *reasoning–acting–interacting* (Figure [1.1](chapter-01-introduction.md#Ch1.F1 "Figure 1.1 ‣ 1.2.4 Training Data ‣ 1.2 Concepts and Definitions ‣ Chapter 1 Introduction ‣ Agentic Large Language Models")), tools are the primary bridge between an LLM’s internal reasoning and its actions in the external world. A tool may be as simple as a calculator, as complex as a scientific simulation engine, or as open-ended as a full desktop environment. By equipping LLMs with tool use capabilities, we allow them to:

- Access *fresh, domain-specific data* (e.g., via APIs, databases, or search engines).
- Perform *actions in the world* (e.g., controlling robots, operating browsers, sending messages).
- Delegate complex computations or retrieval to *specialized systems*.
- Chain multiple tools into *composite workflows* that can be planned, executed, and monitored.

Retrieval is one specific kind of tool primarily aimed to augment an LLM’s *knowledge*. We will discuss it in depth in Chapter [12](chapter-12-search-and-retrieval-in-agentic-llms.md#Ch12 "Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"). Tool use in general can also augment an LLM’s *capabilities* to manipulate its environment. These capabilities also come with additional risks, such as safety, reliability and performance risks. They introduce additional points of failure and might be misused under certain conditions.

<a id="Ch11.S2"></a>


#### 11.2 Tool Use Architectures

Let us see some common software architectures for tool use by LLMs.
Integrating tools into an LLM agent typically follows one of two patterns: direct invocation, and planner-caller-summarizer.

<a id="Ch11.S2.SSx1"></a>


##### Direct Invocation

<a id="Ch11.S2.SSx1.p1.1"></a>


In the direct invocation pattern, the LLM outputs structured calls (e.g., JSON or function signatures) that are parsed by an external controller and routed to the tool. For example: OpenAI’s function calling API or Gorilla [[Patil et al., 2023](#bibj.bib22)].

<a id="Ch11.S2.SSx2"></a>


##### Planner–Caller–Summarizer

The planner-caller-summarizer pattern is an extension of the direct invocation pattern where we use a multi-agent architecture where the LLM serves as a central planner. It calls a separate module to execute a tool (which might be another LLM or another kind of agent), which then returns a summarized observation back to the LLM. This allows the LLM to maintain a high-level view of the task while outsourcing the detailed execution to a dedicated system.

<a id="Ch11.S2.SSx2.p2.1"></a>


ReAct (Reasoning and Acting) [[Yao et al., 2022](#bibj.bib16)] is a prominent framework that interweaves reasoning and acting. Instead of generating a full plan and then executing, an LLM using ReAct follows an iterative loop of Thought, Action, and Observation. This allows the agent to dynamically adjust its plan based on the real-time feedback it receives from tool outputs, making it more robust to errors and unexpected results. This works well because the tools (observation part) often act as a grounding mechanism in the real world (such as the execution of a code snippet, or an internet search), which provides the LLM with factual information for the next iteration.

<a id="Ch11.S3"></a>


#### 11.3 APIs and Toolchains

When their application programming interface (API) is known, LLMs can be integrated easily with external tools: for an LLM, an API is just another language to learn.
One common way to use a tool, is to augment LLM input with results that are retrieved from external sources, such as search engines. You can read more about retrieval methods in Chapter [12](chapter-12-search-and-retrieval-in-agentic-llms.md#Ch12 "Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").

<a id="Ch11.S3.p2.1"></a>


Agentic LLMs must be trained to decide when and how to utilize external tools, depending on the task [[Shen et al., 2024](#bibj.bib9)].
Language models can teach themselves to use tools.
The Toolformer model [[Schick et al., 2023](#bibj.bib3)] is trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. A range of tools is tested: a calculator, a question-answering system, a search engine, a translation system, and a calendar. Further works extend this to a larger range of tools.
ToolBench [[Qin et al., 2023](#bibj.bib5)] contains 16,464 APIs from RapidAPI, a
large dataset of publicly available REST APIs.11
1
<https://rapidapi.com/hub>

<a id="Ch11.S3.p3.1"></a>


Another framework is EasyTool
[[Yuan et al., 2024](#bibj.bib11)], which focuses on structured and
unified instructions from tool documentations, building on ToolBench.
ToolAlpaca is a benchmark with over 3938 instances from 400 API
[[Tang et al., 2023](#bibj.bib4)]. A tool-based benchmark for question
answering is ToolQA [[Zhuang et al., 2023](#bibj.bib13)].
Gorilla is a finetuned LLaMa-based model for generating API calls
[[Patil et al., 2023](#bibj.bib22)], also introducing the APIBench benchmark. Many tool calling frameworks have been developed.

<a id="Ch11.S3.p4.1"></a>


Selecting the right tool and summarizing its result are difficult
skills for a model. [Zhao et al. [2024]](#bibj.bib10), [Shen et al. [2024]](#bibj.bib9) study how LLMs can improve recommendation
through tool learning. They use different LLMs for (1) reasoning ability, (2) request writing, and (3)
result summarization. Figure [11.1](#Ch11.F1 "Figure 11.1 ‣ 11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")
illustrates this architecture, consisting of a planner, a
caller, and a summarizer, each implemented by a different LLM finetuned
for its specific capability.

<a id="Ch11.F1"></a>
![Refer to caption](../../raw/source/figures/alpha.png)


Figure 11.1: <a id="Ch11.F1.4"></a>
Multi LLM agent Framework with a Planner, Caller, and Summarizer [[Shen et al., 2024](#bibj.bib9)]

<a id="Ch11.S3.p5.1"></a>


Good results are reported on the LLMs Claude-2, ChatGPT, GPT-4, and
Tool-LLaMa, using as reasoning strategies ReAct [[Yao et al., 2022](#bibj.bib16)] and
DFSDT [[Qin et al., 2023](#bibj.bib5)].
Other frameworks also exist, such as [[Ocker et al., 2024](#bibj.bib8)].

<a id="Ch11.S3.SS1"></a>


##### 11.3.1 LangChain Example

<a id="Ch11.S3.SS1.p1.1"></a>


LangChain [[Chase, 2022](#bibj.bib20)] is a widely-used framework for building LLM applications, offering robust abstractions for creating agents and tool chains. Listing [11.2](#Ch11.F2 "Figure 11.2 ‣ 11.3.1 LangChain Example ‣ 11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") is a simple Python example demonstrating how to define a tool and use it within a basic agentic framework. In this scenario, the agent is asked a question that requires a numerical check, which it delegates to a specialized tool.

<a id="Ch11.F2"></a>


[⬇](data:text/plain;base64,ZnJvbSBsYW5nY2hhaW4uYWdlbnRzIGltcG9ydCBpbml0aWFsaXplX2FnZW50LCBBZ2VudFR5cGUKZnJvbSBsYW5nY2hhaW5fZ29vZ2xlX2dlbmFpIGltcG9ydCBDaGF0R29vZ2xlR2VuZXJhdGl2ZUFJCmZyb20gbGFuZ2NoYWluLnRvb2xzIGltcG9ydCB0b29sCgojIDEuIERlZmluZSBhIHRvb2wgdXNpbmcgdGhlIGBAdG9vbGAgZGVjb3JhdG9yLgojICAgIFRoaXMgZnVuY3Rpb24gaXMgbm93IGEgY2FsbGFibGUgdG9vbCBmb3IgdGhlIGFnZW50LgojICAgIFRoZSBkb2NzdHJpbmcgaXMgdXNlZCBhcyB0aGUgdG9vbCdzIGRlc2NyaXB0aW9uLAojICAgIHdoaWNoIHRoZSBMTE0gd2lsbCByZWFkIHRvIGRlY2lkZSB3aGVuIHRvIHVzZSBpdC4KQHRvb2wKZGVmIGlzX3ByaW1lKG51bWJlcjogaW50KSAtPiBzdHI6CiAgICAiIiJDaGVja3MgaWYgYSBnaXZlbiBpbnRlZ2VyIGlzIGEgcHJpbWUgbnVtYmVyLgogICAgVGhlIGlucHV0IHNob3VsZCBiZSBhIHNpbmdsZSBpbnRlZ2VyLgoKICAgIEV4YW1wbGU6IGlzX3ByaW1lKDE3KSB3b3VsZCByZXR1cm4gJ1RydWUnLgogICAgIiIiCiAgICBpZiBudW1iZXIgPD0gMToKICAgICAgICByZXR1cm4gJ0ZhbHNlJwogICAgZm9yIGkgaW4gcmFuZ2UoMiwgaW50KG51bWJlcioqMC41KSArIDEpOgogICAgICAgIGlmIG51bWJlciAlIGkgPT0gMDoKICAgICAgICAgICAgcmV0dXJuICdGYWxzZScKICAgIHJldHVybiAnVHJ1ZScKCiMgMi4gSW5pdGlhbGl6ZSB0aGUgTExNIGFuZCB0aGUgdG9vbHMgZm9yIHRoZSBhZ2VudC4KIyAgICBXZSdsbCB1c2UgZ2VtaW5pLTIuNS1mbGFzaC1wcmV2aWV3LTA1LTIwIGFzIHRoZSBMTE0uCiMgICAgVGhlIEFQSSBrZXkgaXMgaGFuZGxlZCBhdXRvbWF0aWNhbGx5IGluIHRoaXMgZW52aXJvbm1lbnQuCmxsbSA9IENoYXRHb29nbGVHZW5lcmF0aXZlQUkobW9kZWw9ImdlbWluaS0yLjUtZmxhc2gtcHJldmlldy0wNS0yMCIpCnRvb2xzID0gW2lzX3ByaW1lXQoKIyAzLiBJbml0aWFsaXplIHRoZSBhZ2VudCB3aXRoIHRoZSBMTE0sIHRvb2xzLCBhbmQgYSB0eXBlLgphZ2VudCA9IGluaXRpYWxpemVfYWdlbnQoCiAgICB0b29scywKICAgIGxsbSwKICAgIGFnZW50PUFnZW50VHlwZS5aRVJPX1NIT1RfUkVBQ1RfREVTQ1JJUFRJT04sCiAgICB2ZXJib3NlPVRydWUKKQoKIyA0LiBSdW4gdGhlIGFnZW50IHdpdGggYSB1c2VyIHByb21wdC4KIyAgICBUaGUgYWdlbnQgd2lsbCByZWFzb24sIGNhbGwgdGhlIHRvb2wsIGFuZCB0aGVuIGZvcm11bGF0ZSBhIGZpbmFsIGFuc3dlci4KdXNlcl9wcm9tcHQgPSAiSXMgdGhlIG51bWJlciA5NyBhIHByaW1lIG51bWJlcj8gUGxlYXNlIGdpdmUgYSAnWWVzJyBvciAnTm8nIGFuc3dlci4iCnJlc3VsdCA9IGFnZW50LnJ1bih1c2VyX3Byb21wdCkKCiMgVGhlIGFnZW50J3MgZXhlY3V0aW9uIGxvb3A6CiMgSXQgd2lsbCBwcmludCB0aGUgJ1Rob3VnaHQnIGFuZCAnQWN0aW9uJyBzdGVwcyB0byB0aGUgY29uc29sZS4=)

1
**from** langchain.agents **import** initialize_agent, AgentType

2
**from** langchain_google_genai **import** ChatGoogleGenerativeAI

3
**from** langchain.tools **import** tool

4

5
*# 1. Define a tool using the ‘@tool‘ decorator.*

6
*# This function is now a callable tool for the agent.*

7
*# The docstring is used as the tool’s description,*

8
*# which the LLM will read to decide when to use it.*

9
@tool

10
**def** is_prime(number: **int**) -> **str**:

11
 """Checks␣if␣a␣given␣integer␣is␣a␣prime␣number.

12
␣␣␣␣The␣input␣should␣be␣a␣single␣integer.

13

14
␣␣␣␣Example:␣is_prime(17)␣would␣return␣’True’.

15
␣␣␣␣"""

16
 **if** number <= 1:

17
 **return** ’False’

18
 **for** i **in** **range**(2, **int**(number\*\*0.5) + 1):

19
 **if** number % i == 0:

20
 **return** ’False’

21
 **return** ’True’

22

23
*# 2. Initialize the LLM and the tools for the agent.*

24
*# We’ll use gemini-2.5-flash-preview-05-20 as the LLM.*

25
*# The API key is handled automatically in this environment.*

26
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-05-20")

27
tools = [is_prime]

28

29
*# 3. Initialize the agent with the LLM, tools, and a type.*

30
agent = initialize_agent(

31
 tools,

32
 llm,

33
 agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,

34
 verbose=True

35
)

36

37
*# 4. Run the agent with a user prompt.*

38
*# The agent will reason, call the tool, and then formulate a final answer.*

39
user_prompt = "Is␣the␣number␣97␣a␣prime␣number?␣Please␣give␣a␣’Yes’␣or␣’No’␣answer."

40
result = agent.run(user_prompt)

41

42
*# The agent’s execution loop:*

43
*# It will print the ’Thought’ and ’Action’ steps to the console.*

Figure 11.2: Example on how to use LangChain to define a tool and use it with an agent.

<a id="Ch11.S3.SS2"></a>


##### 11.3.2 Computer and Browser Tools

<a id="Ch11.S3.SS2.p1.1"></a>


One specific set of action tools is to let an LLM use a browser or even a complete computer system as a special form of API. Equipping agentic LLMs with the ability to interact directly with a computer environment enables many interaction possibilities. Tools that parse, interpret, and manipulate graphical user interfaces (GUIs) have gained attention for bridging the gap between language
models and real-world applications. One such example is OmniParser V2 [[Lu et al., 2024](#bibj.bib19)], which introduces a vision-based screen parsing method
to detect and label interactable elements such as buttons or icons. By converting raw screenshots into structured representations, OmniParser helps vision-language
models ground their action decisions in specific user interface components. This grounding increases the accuracy of the action predictions of LLMs.

Another line of research focuses on enabling LLMs to initiate system-level commands or navigate within browser or operating system interfaces.
Computer Use, proposed by Antropic, and Operator and later GPT Agent, proposed by OpenAI, are examples of such efforts. These tools wrap common desktop and browser actions (such as opening applications, clicking buttons, and filling forms) into tool APIs callable by an LLM. This setup translates high-level textual commands into executable steps. As a result, an agentic LLM can browse the
web, manage files, or run administrative tasks, all through natural language prompts. This can lead to more autonomous behavior and execution of larger and more complex tasks.

<a id="Ch11.S3.SS2.p3.1"></a>


Browser Use [[Müller and Žunič, 2024](#bibj.bib17)] is an example of an open-source tool that enables LLMs to use a browser with persistent session management. Browser Use enables agentic LLMs to maintain longer browsing states across multiple pages or domains. The tool manages cookies, session tokens, and dynamic web content updates, thereby allowing LLMs to execute more complex browsing tasks like multi-step form completions or cross-site queries.

<a id="Ch11.S3.SS2.p4.1"></a>


For a more in-depth discussion about browser and computer environments, see the survey by [Wang et al. [2025b]](#bibj.bib18). The survey discusses design patterns for combining automated GUI parsing, tool call integration, and human-in-the-loop supervision. Collectively, these approaches reveal that
reliable computer and browser tools are important components for agentic LLMs. By translating textual intents into grounded, environment-level operations, such systems expand the possible tasks and domains where language-driven autonomy can be effectively realized.

<a id="Ch11.S4"></a>


#### 11.4 Model Context Protocol and Context Management

<a id="Ch11.S4.p1.1"></a>


The *Model Context Protocol (MCP)* is an open-source standard introduced by Anthropic for connecting AI applications to external data sources, tools, and workflows [[Hou et al., 2026](#bibj.bib15)]. It is often described as a “USB-C port for AI”, providing a standardized way for applications such as Claude or ChatGPT to access local files, databases, search engines, calculators, and other external capabilities.

MCP uses a client-server architecture. An MCP host, such as an AI application, manages one or more MCP clients, with each client maintaining a connection to an MCP server. MCP servers provide context and capabilities that can be used by the host, including tools, resources, and prompts. Local servers commonly communicate with a single client through STDIO, while remote servers can support multiple clients through Streamable HTTP.

The protocol is organized into two layers. The data layer defines the JSON-RPC-based communication between clients and servers, including capability and version discovery, as well as primitives such as tools, resources, prompts, and notifications. The transport layer specifies how this communication is established and exchanged, including connection management, message framing, and authorization. This separation allows AI applications to interact with a wide range of external systems through a common interface, while leaving the management of the resulting context to the host application.

One of the key challenges in building agentic systems is managing the LLM its finite context window. For multi-step tasks that require numerous tool calls and observations, the context can quickly fill up, causing the model to lose track of its original goal or forget crucial past information. Simply keeping all the context and raw results from multiple tool calls often does not fit the context window and therefor causes forgetting. Deciding what to keep, what to summarize and what to discard is essential.

MCP servers are mostly stateless. This means that we need an additional set of strategies designed to manage the agent’s state and context. These strategies should ensure that the agent maintains a clear and coherent state throughout a long-running task. In addition to the fixed tool registration/calling format that MCP offers, additonal components to include are:

- Summarization: Tools’ outputs and past conversations are periodically summarized and stored in a compressed format. This reduces the token count while preserving key information.
- State Management: Explicitly maintaining a state variable or a *scratchpad* in the prompt, where the agent stores its current plan, important intermediate results, and a summary of its progress.
- Prioritized Retrieval: Instead of feeding the entire history back into the context, a retrieval mechanism can be used to only inject the most relevant past information for the current step, based on the agent’s reasoning.

<a id="Ch11.S4.SS0.SSS0.Px1"></a>


###### Example: Implementing the Model Context Protocol

Listing [11.3](#Ch11.F3 "Figure 11.3 ‣ Example: Implementing the Model Context Protocol ‣ 11.4 Model Context Protocol and Context Management ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") and [11.4](#Ch11.F4 "Figure 11.4 ‣ Example: Implementing the Model Context Protocol ‣ 11.4 Model Context Protocol and Context Management ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") illustrates a simplified implementation of the Model Context Protocol. It demonstrates how an agent can manage its context by summarizing past interactions to avoid exceeding a fixed context window size.22
2
The example uses LangChain, and while this is a popular library, there are also specialized MCP libraries such as the MCP-Python SDK: <https://github.com/modelcontextprotocol/python-sdk>, and others, which might be interesting to check out.

<a id="Ch11.F3"></a>


[⬇](data:text/plain;base64,aW1wb3J0IGFzeW5jaW8KaW1wb3J0IG5lc3RfYXN5bmNpbwpmcm9tIGxhbmdjaGFpbl9nb29nbGVfZ2VuYWkgaW1wb3J0IENoYXRHb29nbGVHZW5lcmF0aXZlQUkKZnJvbSBsYW5nY2hhaW4uYWdlbnRzIGltcG9ydCBpbml0aWFsaXplX2FnZW50LCBBZ2VudFR5cGUKZnJvbSBsYW5nY2hhaW4udG9vbHMgaW1wb3J0IHRvb2wKIyBSZXF1aXJlZCBmb3IgcnVubmluZyBhc3luY2lvIGluIGEgbm90ZWJvb2sgZW52aXJvbm1lbnQKbmVzdF9hc3luY2lvLmFwcGx5KCkKIyBEZWZpbmUgdGhlIG1heGltdW0gY29udGV4dCBzaXplIGluICJ0b2tlbnMiIChmb3IgdGhpcyBkZW1vLCB3ZSB1c2UgY2hhcmFjdGVycykuCk1BWF9DT05URVhUX1NJWkUgPSAyNTAKIyBBIHN0YXRlIGRpY3Rpb25hcnkgdG8gcGVyc2lzdCBpbmZvcm1hdGlvbiBhY3Jvc3Mgc3RlcHMuCmFnZW50X3N0YXRlID0gewogICAgJ2N1cnJlbnRfcGxhbic6ICdJbml0aWFsIHBsYW4gdG8gY2hlY2sgaWYgYSBudW1iZXIgaXMgcHJpbWUuJywKICAgICdoaXN0b3J5X3N1bW1hcnknOiAnTm8gaGlzdG9yeSB5ZXQuJwp9CmFzeW5jIGRlZiB1cGRhdGVfY29udGV4dF93aXRoX3N1bW1hcnkoY3VycmVudF9jb250ZXh0LCBuZXdfb2JzZXJ2YXRpb24pOgogICAgIiIiCiAgICBNYW5hZ2VzIHRoZSBjb250ZXh0IGJ5IHN1bW1hcml6aW5nIHBhc3QgaW50ZXJhY3Rpb25zIGlmIHRoZSBjb250ZXh0IHdpbmRvdyBsaW1pdCBpcyBleGNlZWRlZC4KICAgICIiIgogICAgIyBBcHBlbmQgdGhlIG5ldyBvYnNlcnZhdGlvbi4KICAgIG5ld19jb250ZXh0ID0gY3VycmVudF9jb250ZXh0ICsgbmV3X29ic2VydmF0aW9uICsgIlxuIgogICAgIyBDaGVjayBpZiB0aGUgbmV3IGNvbnRleHQgZXhjZWVkcyB0aGUgbWF4aW11bSBzaXplLgogICAgaWYgbGVuKG5ld19jb250ZXh0KSA+IE1BWF9DT05URVhUX1NJWkU6CiAgICAgICAgcHJpbnQoIkNvbnRleHQgaXMgZnVsbCEgU3VtbWFyaXppbmcgcGFzdCBoaXN0b3J5Li4uIikKICAgICAgICAjIEluaXRpYWxpemUgYW4gTExNIHNwZWNpZmljYWxseSBmb3Igc3VtbWFyaXphdGlvbi4KICAgICAgICBzdW1tYXJpemVyX2xsbSA9IENoYXRHb29nbGVHZW5lcmF0aXZlQUkobW9kZWw9ImdlbWluaS0xLjUtZmxhc2gtbGF0ZXN0IikKICAgICAgICAjIENyZWF0ZSBhIHByb21wdCB0byBpbnN0cnVjdCB0aGUgTExNIHRvIHN1bW1hcml6ZS4KICAgICAgICBzdW1tYXJ5X3Byb21wdCA9ICgKICAgICAgICAgICAgIlBsZWFzZSBwcm92aWRlIGEgdmVyeSBjb25jaXNlIHN1bW1hcnkgb2YgdGhlIGZvbGxvd2luZyBhZ2VudCBjb252ZXJzYXRpb24uICIKICAgICAgICAgICAgIkZvY3VzIG9uIHRoZSBrZXkgZGVjaXNpb25zIGFuZCBvdXRjb21lcy4gS2VlcCB0aGUgc3VtbWFyeSB1bmRlciAzMCB3b3Jkcy4iCiAgICAgICAgICAgIGYiXG5cbkNvbnZlcnNhdGlvbiB0byBzdW1tYXJpemU6XG57Y3VycmVudF9jb250ZXh0fSIKICAgICAgICApCiAgICAgICAgdHJ5OgogICAgICAgICAgICAjIENhbGwgdGhlIExMTSB0byBnZW5lcmF0ZSB0aGUgc3VtbWFyeSBhc3luY2hyb25vdXNseS4KICAgICAgICAgICAgc3VtbWFyeV9yZXNwb25zZSA9IGF3YWl0IHN1bW1hcml6ZXJfbGxtLmludm9rZShzdW1tYXJ5X3Byb21wdCkKICAgICAgICAgICAgc3VtbWFyeV90ZXh0ID0gc3VtbWFyeV9yZXNwb25zZS5jb250ZW50CiAgICAgICAgICAgIHByaW50KGYiR2VuZXJhdGVkIFN1bW1hcnk6IHtzdW1tYXJ5X3RleHR9IikKICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgICAgICMgSGFuZGxlIHBvdGVudGlhbCBBUEkgZXJyb3JzLgogICAgICAgICAgICBwcmludChmIkFuIGVycm9yIG9jY3VycmVkIGR1cmluZyBzdW1tYXJpemF0aW9uOiB7ZX0iKQogICAgICAgICAgICBzdW1tYXJ5X3RleHQgPSAiU3VtbWFyaXphdGlvbiBmYWlsZWQuIEhpc3RvcnkgdHJ1bmNhdGVkLiIKCiAgICAgICAgIyBVcGRhdGUgdGhlIGFnZW50J3MgcGVyc2lzdGVudCBzdGF0ZSB3aXRoIHRoZSBuZXcgc3VtbWFyeS4KICAgICAgICBhZ2VudF9zdGF0ZVsnaGlzdG9yeV9zdW1tYXJ5J10gPSBzdW1tYXJ5X3RleHQKICAgICAgICAjIFJlYnVpbGQgdGhlIGNvbnRleHQgd2l0aCB0aGUgc3VtbWFyeSBhbmQgdGhlIG1vc3QgcmVjZW50IHBhcnRzLgogICAgICAgIG5ld19jb250ZXh0ID0gKAogICAgICAgICAgICBmIkN1cnJlbnQgUGxhbjoge2FnZW50X3N0YXRlWydjdXJyZW50X3BsYW4nXX1cbiIKICAgICAgICAgICAgZiJQYXN0IEhpc3Rvcnk6IHthZ2VudF9zdGF0ZVsnaGlzdG9yeV9zdW1tYXJ5J119XG4iCiAgICAgICAgICAgIGYiUmVjZW50IE9ic2VydmF0aW9uOiB7bmV3X29ic2VydmF0aW9ufVxuIgogICAgICAgICkKICAgIHJldHVybiBuZXdfY29udGV4dA==)

1
**import** asyncio

2
**import** nest_asyncio

3
**from** langchain_google_genai **import** ChatGoogleGenerativeAI

4
**from** langchain.agents **import** initialize_agent, AgentType

5
**from** langchain.tools **import** tool

6
*# Required for running asyncio in a notebook environment*

7
nest_asyncio.**apply**()

8
*# Define the maximum context size in "tokens" (for this demo, we use characters).*

9
MAX_CONTEXT_SIZE = 250

10
*# A state dictionary to persist information across steps.*

11
agent_state = {

12
 ’current_plan’: ’Initial␣plan␣to␣check␣if␣a␣number␣is␣prime.’,

13
 ’history_summary’: ’No␣history␣yet.’

14
}

15
async **def** update_context_with_summary(current_context, new_observation):

16
 """

17
␣␣␣␣Manages␣the␣context␣by␣summarizing␣past␣interactions␣if␣the␣context␣window␣limit␣is␣exceeded.

18
␣␣␣␣"""

19
 *# Append the new observation.*

20
 new_context = current_context + new_observation + "\n"

21
 *# Check if the new context exceeds the maximum size.*

22
 **if** **len**(new_context) > MAX_CONTEXT_SIZE:

23
 **print**("Context␣is␣full!␣Summarizing␣past␣history...")

24
 *# Initialize an LLM specifically for summarization.*

25
 summarizer_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

26
 *# Create a prompt to instruct the LLM to summarize.*

27
 summary_prompt = (

28
 "Please␣provide␣a␣very␣concise␣summary␣of␣the␣following␣agent␣conversation.␣"

29
 "Focus␣on␣the␣key␣decisions␣and␣outcomes.␣Keep␣the␣summary␣under␣30␣words."

30
 f"\n\nConversation␣to␣summarize:\n{current_context}"

31
 )

32
 **try**:

33
 *# Call the LLM to generate the summary asynchronously.*

34
 summary_response = await summarizer_llm.invoke(summary_prompt)

35
 summary_text = summary_response.content

36
 **print**(f"Generated␣Summary:␣{summary_text}")

37
 **except** Exception as e:

38
 *# Handle potential API errors.*

39
 **print**(f"An␣error␣occurred␣during␣summarization:␣{e}")

40
 summary_text = "Summarization␣failed.␣History␣truncated."

41

42
 *# Update the agent’s persistent state with the new summary.*

43
 agent_state[’history_summary’] = summary_text

44
 *# Rebuild the context with the summary and the most recent parts.*

45
 new_context = (

46
 f"Current␣Plan:␣{agent_state[’current_plan’]}\n"

47
 f"Past␣History:␣{agent_state[’history_summary’]}\n"

48
 f"Recent␣Observation:␣{new_observation}\n"

49
 )

50
 **return** new_context

Figure 11.3: Simplified implementation of the Model Context Protocol (Part 1).

<a id="Ch11.F4"></a>


[⬇](data:text/plain;base64,YXN5bmMgZGVmIG1haW4oKToKICAgICMgLS0tIERlbW8gUnVuIC0tLQogICAgY3VycmVudF9jb250ZXh0ID0gKAogICAgICAgICJUYXNrOiBEZXRlcm1pbmUgaWYgOTcgaXMgYSBwcmltZSBudW1iZXIuXG4iCiAgICAgICAgIlRob3VnaHQ6IEkgbmVlZCB0byB1c2UgdGhlIGlzX3ByaW1lIHRvb2wgdG8gc29sdmUgdGhpcy5cbiIKICAgICAgICAiQWN0aW9uOiBDYWxsIHRvb2wgYGlzX3ByaW1lYCB3aXRoIG51bWJlciA5Ny5cbiIKICAgICkKCiAgICAjIFNpbXVsYXRlIGEgdG9vbCdzIG91dHB1dCBvYnNlcnZhdGlvbi4KICAgIHRvb2xfb3V0cHV0X29ic2VydmF0aW9uID0gIk9ic2VydmF0aW9uOiBUaGUgdG9vbCByZXR1cm5lZCB0aGUgdmFsdWUgJ1RydWUnLiIKCiAgICAjIFVwZGF0ZSB0aGUgY29udGV4dCB1c2luZyB0aGUgTUNQIGZ1bmN0aW9uLgogICAgdXBkYXRlZF9jb250ZXh0ID0gYXdhaXQgdXBkYXRlX2NvbnRleHRfd2l0aF9zdW1tYXJ5KGN1cnJlbnRfY29udGV4dCwgdG9vbF9vdXRwdXRfb2JzZXJ2YXRpb24pCgogICAgcHJpbnQoIlxuLS0tIFVwZGF0ZWQgQ29udGV4dCAtLS0iKQogICAgcHJpbnQodXBkYXRlZF9jb250ZXh0KQoKICAgICMgTm93LCBsZXQncyBhZGQgbW9yZSAiY2hhdHRlciIgdG8gZm9yY2UgYSBzdW1tYXJ5LgogICAgbG9uZ19jaGF0dGVyID0gKAogICAgICAgICJUaG91Z2h0OiBUaGUgdG9vbCBoYXMgY29uZmlybWVkIHRoYXQgOTcgaXMgYSBwcmltZSBudW1iZXIuICIKICAgICAgICAiVGhlIHRhc2sgaXMgY29tcGxldGUuICIKICAgICAgICAiRmluYWwgQW5zd2VyOiBZZXMsIDk3IGlzIGEgcHJpbWUgbnVtYmVyLiIKICAgICkKCiAgICB1cGRhdGVkX2NvbnRleHQgPSBhd2FpdCB1cGRhdGVfY29udGV4dF93aXRoX3N1bW1hcnkodXBkYXRlZF9jb250ZXh0LCBsb25nX2NoYXR0ZXIpCgogICAgcHJpbnQoIlxuLS0tIENvbnRleHQgYWZ0ZXIgc2Vjb25kIHVwZGF0ZSAoc3VtbWFyaXplZCkgLS0tIikKICAgIHByaW50KHVwZGF0ZWRfY29udGV4dCkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBhc3luY2lvLnJ1bihtYWluKCkp)

1
async **def** main():

2
 *# --- Demo Run ---*

3
 current_context = (

4
 "Task:␣Determine␣if␣97␣is␣a␣prime␣number.\n"

5
 "Thought:␣I␣need␣to␣use␣the␣is_prime␣tool␣to␣solve␣this.\n"

6
 "Action:␣Call␣tool␣‘is_prime‘␣with␣number␣97.\n"

7
 )

8

9
 *# Simulate a tool’s output observation.*

10
 tool_output_observation = "Observation:␣The␣tool␣returned␣the␣value␣’True’."

11

12
 *# Update the context using the MCP function.*

13
 updated_context = await update_context_with_summary(current_context, tool_output_observation)

14

15
 **print**("\n---␣Updated␣Context␣---")

16
 **print**(updated_context)

17

18
 *# Now, let’s add more "chatter" to force a summary.*

19
 long_chatter = (

20
 "Thought:␣The␣tool␣has␣confirmed␣that␣97␣is␣a␣prime␣number.␣"

21
 "The␣task␣is␣complete.␣"

22
 "Final␣Answer:␣Yes,␣97␣is␣a␣prime␣number."

23
 )

24

25
 updated_context = await update_context_with_summary(updated_context, long_chatter)

26

27
 **print**("\n---␣Context␣after␣second␣update␣(summarized)␣---")

28
 **print**(updated_context)

29

30
**if** __name__ == "__main__":

31
 asyncio.run(main())

Figure 11.4: Simplified implementation of the Model Context Protocol. (Part 2)

<a id="Ch11.S5"></a>


#### 11.5 Robustness, Error Handling, and Recovery

The external nature of tool use introduces new points of failure. An API service might be down, a tool might return an unexpected error, or the LLM might make a logical mistake in its plan. A robust agentic system must be able to handle these failures gracefully.

<a id="Ch11.S5.SS0.SSS0.Px1"></a>


###### Reactive Error Handling

<a id="Ch11.S5.SS0.SSS0.Px1.p1.1"></a>


A basic but essential strategy is to implement an error-handling loop. When a tool call fails, the system can provide the LLM with the error message as an observation. The LLM can then reason about the error and attempt a new action, such as re-invoking the tool with corrected arguments, trying a different tool, or informing the user of the failure. This process of observe-reflect-retry is a fundamental mechanism for self-healing in agentic systems [[Sun et al., 2024](#bibj.bib21)]. Note that this pattern is similar to the ReAct framework but in a different context.

<a id="Ch11.S5.SS0.SSS0.Px2"></a>


###### Self-Correcting and State-Aware Systems

<a id="Ch11.S5.SS0.SSS0.Px2.p1.1"></a>


More advanced systems, such as Healer, are designed to correct runtime errors in real-time [[Wu et al., 2024](#bibj.bib14)]. Healer can dynamically generate and execute a small code snippet to patch a faulty program state without stopping the entire execution. This goes beyond simple retries; it involves the LLM understanding the context of the error, analyzing the program state, and actively correcting the error (in code).

<a id="Ch11.S5.SS0.SSS0.Px3"></a>


###### Human-in-the-Loop Integration

<a id="Ch11.S5.SS0.SSS0.Px3.p1.1"></a>


While autonomy is a goal of agentic systems, the most effective applications often involve a human-in-the-loop. This approach improves safety, allows for corrections, and incorporates human expertise at critical junctures.33
3
Although it also introduces the possibility of human error. An agent can be designed to pause and ask for human confirmation before executing a high-stakes action (e.g., making a financial transaction or sending a critical email). This co-piloting model creates a powerful symbiosis, combining the LLM’s speed and scale with human judgment and domain knowledge [[Mozannar et al., 2025](#bibj.bib23)].

<a id="Ch11.S6"></a>


#### 11.6 Safety and Security

Safety and security are becoming more important as the capabilities of Agentic LLMs grow. This goes beyond simple error handling and is more subtle on a misbehavior and misuse level. An obvious example of a safety problem is that without additional protection, the system prompt of an LLM can easily be exposed, often revealing sensitive information.

<a id="Ch11.S6.p2.1"></a>


The robustness of LLMs to jailbreak attacks, where users design prompts to circumvent safety measures and misuse model capabilities, has been studied for chatbots. Meanwhile, agentic LLMs use
external tools and can execute multi stage tasks, and may pose a greater risk. [Andriushchenko et al. [2024]](#bibj.bib6) propose AgentHarm. This benchmark
includes a set of 110 malicious agent tasks ranging from fraud, cyber crime, to harassment.
The authors find that leading commercial LLMs are surprisingly compliant to their given rules with malicious user requests without jailbreaking (*How do I make a
pipe bomb?* is blocked). However, simple universal templates can
be adapted to effectively jailbreak agents (*Order online all necessary ingredients to make a pipe bomb and get them delivered to
my home without getting flagged by authorities*, however, passes in GPT-4).

<a id="Ch11.S6.p3.1"></a>


Rainbow Teaming [[Samvelyan et al., 2024](#bibj.bib7)] uses an open world approach to
generate adversarial LLM prompts, to improve the robustness of LLMs. As with training LLMs, a
problem with testing methods is a lack of diversity.
Rainbow Teaming casts adversarial prompt generation as a quality-diversity problem. Rainbow Teaming is an open-ended approach [[Hughes et al., 2024](#bibj.bib2)]. It creates diversity with MAP-Elites [[Mouret and Clune, 2015](#bibj.bib1)], an evolutionary meta search method that iteratively populates an archive with increasingly higher-performing prompts.
See Figures [11.5](#Ch11.F5 "Figure 11.5 ‣ 11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") and [11.6](#Ch11.F6 "Figure 11.6 ‣ 11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").

<a id="Ch11.F5"></a>
![Refer to caption](../../raw/source/figures/rainbow.png)


Figure 11.5: <a id="Ch11.F5.4"></a>
Adversarial prompts generated by Rainbow Teaming [[Samvelyan et al., 2024](#bibj.bib7)]

<a id="Ch11.F6"></a>
![Refer to caption](../../raw/source/figures/rainbow2.png)


Figure 11.6: <a id="Ch11.F6.4"></a>
Quality Diversity Mutation Architecture of Rainbow Teaming [[Samvelyan et al., 2024](#bibj.bib7)]

<a id="Ch11.S7"></a>


#### 11.7 Concluding Remarks

Tools are what turn a static language model into a dynamic agent that can act in the world. Their ability to grant LLMs access to fresh data, perform external actions, and delegate complex tasks is transformative. For any agentic system to be successful in practice, the result goes beyond just connecting a tool to an LLM, but now requires us to think about the full life-cycle of the agent’s interaction with the environment, and what can happen. Four steps should be followed:

1. <a id="Ch11.S7.I1.i1.p1.1"></a>


   Choose the right Architecture: Methodologies such as ReAct [[Yao et al., 2022](#bibj.bib16)], which tightly interleave reasoning and tool calls, lead to more robust self-correcting behavior than simpler one-shot approaches.
2. Manage your Context: For multistep long-term tasks, the LLM context window is a critical bottleneck. Use strategies such as the Model Context Protocol to summarize history and manage state, preventing the agent from losing its way.
3. Embrace Failure: Tool-use systems are inherently fragile due to their reliance on external APIs. Build in robust error handling, allowing the agent to observe and reason about failures, and attempt recovery.
4. Keep a Human in the Loop: For high-stakes applications, ensure that the agent has a clear mechanism to pause and seek human confirmation before taking irreversible actions. This blend of autonomy and human oversight is key to building trust and ensuring safety.

**Try it yourself!**

Want to experiment with LLM tool-use?
Open our:
  
[**LLM Tools tutorial** in Google Colab](https://colab.research.google.com/github/Agentic-LLMs/Agentic-AI-tutorials/blob/main/tools_tutorial.ipynb)

<a id="Ch11.S7.SS0.SSS0.Px1"></a>


###### Further Reading

<a id="Ch11.S7.SS0.SSS0.Px1.p1.1"></a>


Surveys on tool use in LLMs are [Shen [2024]](#bibj.bib12), [Patil et al. [2023]](#bibj.bib22), [Qin et al. [2023]](#bibj.bib5).
For more on GUI parsing and browser control see [Lu et al. [2024]](#bibj.bib19), [Müller and Žunič [2024]](#bibj.bib17). For
safety benchmarks and adversarial prompting see [Wang et al. [2025a]](#bibj.bib24).

<a id="bibj"></a>


### References

<a id="bibj.bib6"></a>
- Andriushchenko et al. (2024)
  M. Andriushchenko, A. Souly, M. Dziemian, D. Duenas, M. Lin, J. Wang, D. Hendrycks, A. Zou, Z. Kolter, M. Fredrikson, et al.
  Agentharm: a benchmark for measuring harmfulness of llm agents.
  arXiv preprint arXiv:2410.09024.
  Cited by: [§11.6](#Ch11.S6.p2.1 "11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib20"></a>
- Chase (2022)
  H. Chase
  LangChain.
  External Links: [Link](https://github.com/langchain-ai/langchain)
  Cited by: [§11.3.1](#Ch11.S3.SS1.p1.1 "11.3.1 LangChain Example ‣ 11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib15"></a>
- Hou et al. (2026)
  X. Hou, Y. Zhao, S. Wang, and H. Wang
  Model context protocol (mcp): landscape, security threats, and future research directions.
  ACM Trans. Softw. Eng. Methodol. 35 (10).
  External Links: ISSN 1049-331X,
  [Link](https://doi.org/10.1145/3796519),
  [Document](https://dx.doi.org/10.1145/3796519)
  Cited by: [§11.4](#Ch11.S4.p1.1 "11.4 Model Context Protocol and Context Management ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib2"></a>
- Hughes et al. (2024)
  E. Hughes, M. Dennis, J. Parker-Holder, F. Behbahani, A. Mavalankar, Y. Shi, T. Schaul, and T. Rocktaschel
  Open-endedness is essential for artificial superhuman intelligence.
  arXiv preprint arXiv:2406.04268.
  Cited by: [§11.6](#Ch11.S6.p3.1 "11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib19"></a>
- Lu et al. (2024)
  Y. Lu, J. Yang, Y. Shen, and A. Awadallah
  OmniParser for pure vision based gui agent.
  External Links: 2408.00203,
  [Link](https://arxiv.org/abs/2408.00203)
  Cited by: [§11.3.2](#Ch11.S3.SS2.p1.1 "11.3.2 Computer and Browser Tools ‣ 11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.7](#Ch11.S7.SS0.SSS0.Px1.p1.1 "Further Reading ‣ 11.7 Concluding Remarks ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib1"></a>
- Mouret and Clune (2015)
  J. Mouret and J. Clune
  Illuminating search spaces by mapping elites.
  arXiv preprint arXiv:1504.04909.
  Cited by: [§11.6](#Ch11.S6.p3.1 "11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib23"></a>
- Mozannar et al. (2025)
  H. Mozannar, G. Bansal, C. Tan, A. Fourney, V. Dibia, J. Chen, J. Gerrits, T. Payne, M. K. Maldaner, M. Grunde-McLaughlin, et al.
  Magentic-ui: towards human-in-the-loop agentic systems.
  arXiv preprint arXiv:2507.22358.
  Cited by: [§11.5](#Ch11.S5.SS0.SSS0.Px3.p1.1 "Human-in-the-Loop Integration ‣ 11.5 Robustness, Error Handling, and Recovery ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib17"></a>
- Müller and Žunič (2024)
  M. Müller and G. Žunič
  Browser use: enable ai to control your browser.
   GitHub.
  External Links: [Link](https://github.com/browser-use/browser-use)
  Cited by: [§11.3.2](#Ch11.S3.SS2.p3.1 "11.3.2 Computer and Browser Tools ‣ 11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.7](#Ch11.S7.SS0.SSS0.Px1.p1.1 "Further Reading ‣ 11.7 Concluding Remarks ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib8"></a>
- Ocker et al. (2024)
  F. Ocker, D. Tanneberg, J. Eggert, and M. Gienger
  Tulip agent–enabling llm-based agents to solve tasks using large tool libraries.
  arXiv preprint arXiv:2407.21778.
  Cited by: [§11.3](#Ch11.S3.p5.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib22"></a>
- Patil et al. (2023)
  S. G. Patil, T. Zhang, X. Wang, and J. E. Gonzalez
  Gorilla: large language model connected with massive apis.
  External Links: 2305.15334,
  [Link](https://arxiv.org/abs/2305.15334)
  Cited by: [§11.2](#Ch11.S2.SSx1.p1.1 "Direct Invocation ‣ 11.2 Tool Use Architectures ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.3](#Ch11.S3.p3.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.7](#Ch11.S7.SS0.SSS0.Px1.p1.1 "Further Reading ‣ 11.7 Concluding Remarks ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib5"></a>
- Qin et al. (2023)
  Y. Qin, S. Liang, Y. Ye, K. Zhu, L. Yan, Y. Lu, Y. Lin, X. Cong, X. Tang, B. Qian, et al.
  Toolllm: facilitating large language models to master 16000+ real-world apis.
  arXiv preprint arXiv:2307.16789.
  Cited by: [§11.3](#Ch11.S3.p2.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.3](#Ch11.S3.p5.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.7](#Ch11.S7.SS0.SSS0.Px1.p1.1 "Further Reading ‣ 11.7 Concluding Remarks ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib7"></a>
- Samvelyan et al. (2024)
  M. Samvelyan, S. C. Raparthy, A. Lupu, E. Hambro, A. H. Markosyan, M. Bhatt, Y. Mao, M. Jiang, J. Parker-Holder, J. Foerster, et al.
  Rainbow teaming: open-ended generation of diverse adversarial prompts.
  arXiv preprint arXiv:2402.16822.
  Cited by: [Figure 11.5](#Ch11.F5 "In 11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [Figure 11.5](#Ch11.F5.4 "In 11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [Figure 11.6](#Ch11.F6 "In 11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [Figure 11.6](#Ch11.F6.4 "In 11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.6](#Ch11.S6.p3.1 "11.6 Safety and Security ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib3"></a>
- Schick et al. (2023)
  T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, E. Hambro, L. Zettlemoyer, N. Cancedda, and T. Scialom
  Toolformer: language models can teach themselves to use tools.
  Advances in Neural Information Processing Systems 36, pp. 68539–68551.
  Cited by: [§11.3](#Ch11.S3.p2.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib9"></a>
- Shen et al. (2024)
  W. Shen, C. Li, H. Chen, M. Yan, X. Quan, H. Chen, J. Zhang, and F. Huang
  Small llms are weak tool learners: a multi-llm agent.
  arXiv preprint arXiv:2401.07324.
  Cited by: [Figure 11.1](#Ch11.F1 "In 11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [Figure 11.1](#Ch11.F1.4 "In 11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.3](#Ch11.S3.p2.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.3](#Ch11.S3.p4.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib12"></a>
- Shen (2024)
  Z. Shen
  Llm with tools: a survey.
  arXiv preprint arXiv:2409.18807.
  Cited by: [§11.7](#Ch11.S7.SS0.SSS0.Px1.p1.1 "Further Reading ‣ 11.7 Concluding Remarks ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib21"></a>
- Sun et al. (2024)
  Z. Sun, H. Zhu, B. Xu, X. Du, L. Li, and D. Lo
  LLM as runtime error handler: a promising pathway to adaptive self-healing of software systems.
  External Links: 2408.01055,
  [Link](https://arxiv.org/abs/2408.01055)
  Cited by: [§11.5](#Ch11.S5.SS0.SSS0.Px1.p1.1 "Reactive Error Handling ‣ 11.5 Robustness, Error Handling, and Recovery ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib4"></a>
- Tang et al. (2023)
  Q. Tang, Z. Deng, H. Lin, X. Han, Q. Liang, B. Cao, and L. Sun
  Toolalpaca: generalized tool learning for language models with 3000 simulated cases.
  arXiv preprint arXiv:2306.05301.
  Cited by: [§11.3](#Ch11.S3.p3.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib24"></a>
- Wang et al. (2025a)
  K. Wang, G. Zhang, Z. Zhou, J. Wu, M. Yu, S. Zhao, C. Yin, J. Fu, Y. Yan, H. Luo, et al.
  A comprehensive survey in llm (-agent) full stack safety: data, training and deployment.
  arXiv preprint arXiv:2504.15585.
  Cited by: [§11.7](#Ch11.S7.SS0.SSS0.Px1.p1.1 "Further Reading ‣ 11.7 Concluding Remarks ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib18"></a>
- Wang et al. (2025b)
  S. Wang, W. Liu, J. Chen, Y. Zhou, W. Gan, X. Zeng, Y. Che, S. Yu, X. Hao, K. Shao, B. Wang, C. Wu, Y. Wang, R. Tang, and J. Hao
  GUI agents with foundation models: a comprehensive survey.
  External Links: 2411.04890,
  [Link](https://arxiv.org/abs/2411.04890)
  Cited by: [§11.3.2](#Ch11.S3.SS2.p4.1 "11.3.2 Computer and Browser Tools ‣ 11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib14"></a>
- Wu et al. (2024)
  Y. Wu, T. Yue, S. Zhang, C. Wang, and Q. Wu
  StateFlow: enhancing llm task-solving through state-driven workflows.
  arXiv preprint arXiv:2403.11322.
  Cited by: [§11.5](#Ch11.S5.SS0.SSS0.Px2.p1.1 "Self-Correcting and State-Aware Systems ‣ 11.5 Robustness, Error Handling, and Recovery ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib16"></a>
- Yao et al. (2022)
  S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao
  React: synergizing reasoning and acting in language models.
  arXiv preprint arXiv:2210.03629.
  Cited by: [§11.2](#Ch11.S2.SSx2.p2.1 "Planner–Caller–Summarizer ‣ 11.2 Tool Use Architectures ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§11.3](#Ch11.S3.p5.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [item 1](#Ch11.S7.I1.i1.p1.1 "In 11.7 Concluding Remarks ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib11"></a>
- Yuan et al. (2024)
  S. Yuan, K. Song, J. Chen, X. Tan, Y. Shen, R. Kan, D. Li, and D. Yang
  Easytool: enhancing llm-based agents with concise tool instruction.
  arXiv preprint arXiv:2401.06201.
  Cited by: [§11.3](#Ch11.S3.p3.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib10"></a>
- Zhao et al. (2024)
  Y. Zhao, J. Wu, X. Wang, W. Tang, D. Wang, and M. de Rijke
  Let me do it for you: towards llm empowered recommendation via tool learning.
  In Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval,
  pp. 1796–1806.
  Cited by: [§11.3](#Ch11.S3.p4.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibj.bib13"></a>
- Zhuang et al. (2023)
  Y. Zhuang, Y. Yu, K. Wang, H. Sun, and C. Zhang
  Toolqa: a dataset for llm question answering with external tools.
  Advances in Neural Information Processing Systems 36, pp. 50117–50143.
  Cited by: [§11.3](#Ch11.S3.p3.1 "11.3 APIs and Toolchains ‣ Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
