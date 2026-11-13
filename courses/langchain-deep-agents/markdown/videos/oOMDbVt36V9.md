# Tool Decorator

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/oOMDbVt36V9) · [Raw file](../../raw/videos/oOMDbVt36V9.html)

Retrieved: 2026-11-13T16:57:39.175477+00:00

[00:00] **Speaker**: Now we're at a fun part, defining a tool  with a tool decorator.  The tool decorator from the LangChain library is super simple.  You write a regular Python function, and the decorator turns it into something the model can call. LangChain also ships some ready-made tools for common tasks,  such as Tavily search results for web search, so you don't have to write everything from scratch.

[00:20] **Speaker**: But let's take a look at what it actually looks like

[00:23] **Speaker**: So this is some code, and this is a diagram demonstrating the different parts of the code. First, we have the actual decorator itself

[00:30] **Speaker**: Just by adding @tool above your function,  LangChain registers it as a tool. Super easy. Then come the name and schema

[00:39] **Speaker**: These come directly from the function signature. The function name becomes the tool name and the arguments and their types become the schema.

[00:45] **Speaker**: So def get_stock_price gives the model a tool called get_stock_price

[00:50] **Speaker**: And expects a string called ticker. That's what gets sent to the LLM so it knows to call it. And finally, the most important part, the description. This is your docstring, and it's the only signal the model has for deciding when to reach for this tool versus any other.  You want to write this clearly and specifically and describe what the tool does and when to use it.
