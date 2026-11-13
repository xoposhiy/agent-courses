# Project code: stanford-oval/genie-worksheets: web/docs/prompt/index.html

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/docs/prompt/index.html) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/prompt/index.html)

Retrieved: 2026-11-13T17:06:24.900930+00:00

# Creating Prompts

Genie uses two types of prompts for each agent:

1. **Semantic Parser Prompt**: Used to generate worksheet representation of the user's query
2. **Response Generator Prompt**: Used to generate the agent's response based on the worksheet representation and agent acts

## Prompt Structure

Each prompt file follows this general structure:

```
<|startofinstruction|>
[General Instructions and Guidelines]

Today's date is {{ date }} and the day is {{ day }}.

[Available APIs and Tools]

[Guidelines for Using APIs]

[Examples]
<|endofinstruction|>

<|startofinput|>
[Template for Input]
<|endofinput|>
```

`<|startofinstruction|>` and `<|endofinstruction|>` are used to mark the start and end of the system prompt.

`<|startofinput|>` and `<|endofinput|>` are used to mark the start and end of the user input.

## Common Elements

### Date and Day Variables

Both prompts include template variables for date and time:

```
Today's date is {{ date }} and the day is {{ day }}.
```

### API Definitions

APIs are defined using template variables:

```
These are the APIs available to you:
{{ apis }}
```

APIs are the tasks in your worksheet. Convert the tasks into python functions, with each field being a parameter.

## Semantic Parser Prompt

The semantic parser prompt is responsible for converting user utterances into API calls and worksheet updates.

### Key Components

1. **Purpose Statement**

   ```
   You are a semantic parser. Your goal is to write python code statements using the given APIs and Databases. Plan your response first, then write the code.
   ```
2. **Available Tools**

   * Define the APIs and databases the parser can use
   * Specify what the `answer(query: str)` function that can be used to query the knowledge base.
3. **Guidelines**
   Guidelines should include:

   * Field handling instructions
   * Special cases (like chit-chat handling)
   * Domain specific guidelines or instructions on how to use the APIs

General guidelines for all semantic parser prompts:

```
Follow these guidelines:
- To update any field of the APIs, use: `api_name.field_name = value`
- When asking questions, use: `answer(query:str)`
- Fill API fields with user-provided information only
- Don't assume values; leave empty if not provided
- For chit-chat/greetings, write: # Chit-chat, greeting or thanking
```

### Examples Section

Examples are crucial for the semantic parser, it helps the parser understand the user's query and generate the right worksheet representation.

Example structure (for semantic parser)

Each example should follow this structure:

```
Example: [Short description of the scenario]
State:
```
[Current state of the conversation]
```
Agent Action:
```
[List of actions the agent is taking]
```

Last-turn Conversation:
Agent: [Previous agent message]
User: [User message]

User Target:
```
[Expected code output]
```
```

Key aspects of examples:

1. **State**: Shows the current conversation state including:

   * Active worksheets
   * Field values
   * Previous query results
2. **Agent Action**: Shows what actions the agent is taking, such as:

   * Asking for field values
   * Requesting confirmation
   * Reporting query results
3. **Last-turn Conversation**: Shows the context of the interaction
4. **User Target**: Shows the expected code output

## Response Generator Prompt

The response generator prompt converts agent actions and state into natural language responses.

### Key Components

1. **Purpose Statement**

   ```
   You are talking to a [user type] about [domain]. You will be given a list of agent actions and you have to use them to respond to the user.
   ```
2. **Available Actions**
   Define all possible actions the agent can take:

   ```
   These are the actions that you can perform:
   - AskField(worksheet, field, field_description)
   - AskForConfirmation(worksheet)
   - Report(query, answer)
   - ProposeWorksheet(worksheet, parameters)
   - AskForFieldConfirmation(worksheet, field, value)
   ```
3. **Guidelines**
   Include rules for:
4. How to perform each action type
5. Response formatting
6. Error handling
7. Special cases

### Examples Section

Response generator examples should demonstrate:

1. How to handle different action types
2. How to format responses
3. How to combine multiple actions
4. How to handle edge cases

Example structure (for response generator)

`` `
Example: [Description of the scenario]
State: ``
[Current conversation state]
`Agent Action:`
[Actions to perform]
```

Previous Turns:
Agent: [Previous agent message]
User: [User message]

Latest Agent Response: [Example of correct agent response]
```

## Best Practices for Creating Examples

1. **Coverage**
2. Include examples for all common scenarios
3. Cover edge cases and error conditions
4. Show both simple and complex interactions
5. **Progression**
6. Start with basic examples
7. Build up to more complex scenarios
8. Include examples without state for initial interactions
9. **Clarity**
10. Use descriptive names for example scenarios
11. Include comments explaining key aspects
12. Show both input and expected output
13. **Variety**
14. Include examples for different API calls
15. Show different field types and values
16. Demonstrate error handling
17. **Completeness**
18. Show complete conversation context
19. Include all relevant state information
20. Demonstrate proper handling of all action types

## Template Variables

Your prompt files can use these template variables:

* `{{ date }}`: Current date
* `{{ day }}`: Current day
* `{{ apis }}`: Available APIs
* `{{ state }}`: Current conversation state
* `{{ agent_acts }}`: Current agent actions
* `{{ agent_utterance }}`: Previous agent message
* `{{ user_utterance }}`: Current user message
* `{{ parsing }}`: Parsing results (if applicable)

Back to top
