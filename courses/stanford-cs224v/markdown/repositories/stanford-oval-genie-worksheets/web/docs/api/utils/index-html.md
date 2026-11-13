# Project code: stanford-oval/genie-worksheets: web/docs/api/utils/index.html

[Course index](../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/docs/api/utils/index.html) · [Raw file](../../../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/api/utils/index.html)

Retrieved: 2026-11-13T17:06:24.900930+00:00

# Utility Modules

## Annotation Utils

## src.worksheets.annotation\_utils

Utility functions for handling Genie worksheet annotations and context management.

This module provides utilities for managing and formatting Genie worksheet annotations,
handling different types of answers, and preparing context for semantic parsing and
dialogue interactions.

### Functions

#### handle\_genie\_type

```
handle_genie_type(key, value, context, response_generator)
```

Processes a Genie type value and generates its schema representation.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | The key/name of the Genie type value. | *required* |
| `value` | `Union[GenieType, Answer, GenieWorksheet]` | The value to process. | *required* |
| `context` |  | The context object containing variable information. | *required* |
| `response_generator` | `bool` | Flag indicating whether to include response generation info. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | The schema representation of the Genie type value, or None if not applicable. |

Source code in `src/worksheets/annotation_utils.py`

|  |  |
| --- | --- |
| ``` 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 ``` | ``` def handle_genie_type(key, value, context, response_generator):     """Processes a Genie type value and generates its schema representation.      Args:         key (str): The key/name of the Genie type value.         value (Union[GenieType, Answer, GenieWorksheet]): The value to process.         context: The context object containing variable information.         response_generator (bool): Flag indicating whether to include response generation info.      Returns:         str: The schema representation of the Genie type value, or None if not applicable.     """     schema = ""     if isinstance(value, GenieType):         return     if key.startswith("__"):  # To prevent __answer_result from shown in the schema         return     if isinstance(value, Answer):         if value.query.value is not None and response_generator:             schema += (                 key                 + " = answer("                 + repr(value.nl_query)                 + ", sql="                 + repr(value.query.value)                 + ")\n"             )         else:             schema += key + " = answer(" + repr(value.nl_query) + ")\n"          if value.result:             if hasattr(value.result, "value"):                 res = value.result.value             else:                 res = value.result             if isinstance(res, list):                 parent_var_name = None                 indices = []                  result_strings = []                 for val in res:                     if isinstance(val, GenieType):                         var_name, idx = find_list_variable(val, context)                         if var_name is None and idx is None:                             result_strings.append(val)                         else:                             if (                                 parent_var_name is not None                                 and parent_var_name != var_name                             ):                                 logger.error(                                     "Cannot handle multiple list variables in the same answer"                                 )                             parent_var_name = var_name  # Ignoring any potential multiple list variables                              indices.append(idx)                     else:                         result_strings.append(val)                  if parent_var_name:                     indices_str = []                     for idx in indices:                         indices_str.append(f"{parent_var_name}[{idx}]")                      result_strings = "[" + ", ".join(indices_str) + "]"              else:                 result_strings = (                     res.schema_without_type(context)                     if isinstance(res, GenieWorksheet)                     else res                 )             schema += key + ".result = " + str(result_strings) + "\n"         else:             schema += key + ".result = None\n"     elif isinstance(value, GenieWorksheet):         if value.__class__.__name__ == "MoreFieldInfo":             return         schema += key + " = " + str(value.schema_without_type(context)) + "\n"         if hasattr(value, "result"):             if value.result:                 schema += key + ".result = " + str(value.result.value) + "\n"      return schema ``` |

#### get\_context\_schema

```
get_context_schema(context, response_generator=False)
```

Generates a schema representation of the given context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` |  | The context object containing variables and their values. | *required* |
| `response_generator` | `bool` | Flag to include response generation info. Defaults to False. | `False` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | A string representation of the context schema with escaped backslashes removed. |

Source code in `src/worksheets/annotation_utils.py`

|  |  |
| --- | --- |
| ``` 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 ``` | ``` def get_context_schema(context, response_generator=False):     """Generates a schema representation of the given context.      Args:         context: The context object containing variables and their values.         response_generator (bool, optional): Flag to include response generation info. Defaults to False.      Returns:         str: A string representation of the context schema with escaped backslashes removed.     """     schema = ""      for key, value in context.context.items():         if isinstance(value, list):             bad_list = False             for val in value:                 if not isinstance(val, GenieType):                     bad_list = True                     break              if not bad_list:                 schema += key + " = " + str(value) + "\n"         else:             new_schema = handle_genie_type(key, value, context, response_generator)             if new_schema:                 schema += new_schema      return schema.replace("\\", "") ``` |

#### get\_agent\_action\_schemas

```
get_agent_action_schemas(agent_acts, *args, **kwargs)
```

Converts agent actions into their schema representations.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `agent_acts` |  | List of agent actions to convert. | *required* |
| `*args` |  | Variable length argument list. | `()` |
| `**kwargs` |  | Arbitrary keyword arguments. | `{}` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `list` |  | List of string representations of agent actions. |

Source code in `src/worksheets/annotation_utils.py`

|  |  |
| --- | --- |
| ``` 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 ``` | ``` def get_agent_action_schemas(agent_acts, *args, **kwargs):     """Converts agent actions into their schema representations.      Args:         agent_acts: List of agent actions to convert.         *args: Variable length argument list.         **kwargs: Arbitrary keyword arguments.      Returns:         list: List of string representations of agent actions.     """     agent_acts_schema = []     if agent_acts:         for act in agent_acts:             agent_acts_schema.append(str(act))      return agent_acts_schema ``` |

#### prepare\_context\_input

```
prepare_context_input(bot, dlg_history, current_dlg_turn)
```

Prepares context input for dialogue processing.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` |  | The bot instance containing context and configuration. | *required* |
| `dlg_history` |  | List of previous dialogue turns. | *required* |
| `current_dlg_turn` |  | The current dialogue turn being processed. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `tuple` |  | A tuple containing (state\_schema, agent\_acts, agent\_utterance). |

Source code in `src/worksheets/annotation_utils.py`

|  |  |
| --- | --- |
| ``` 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 ``` | ``` def prepare_context_input(bot, dlg_history, current_dlg_turn):     """Prepares context input for dialogue processing.      Args:         bot: The bot instance containing context and configuration.         dlg_history: List of previous dialogue turns.         current_dlg_turn: The current dialogue turn being processed.      Returns:         tuple: A tuple containing (state_schema, agent_acts, agent_utterance).     """     if len(dlg_history):         state_schema = get_context_schema(bot.context)         agent_acts = json.dumps(             get_agent_action_schemas(dlg_history[-1].system_action, bot.context),             indent=2,         )         agent_utterance = dlg_history[-1].system_response     else:         state_schema = "None"         agent_acts = "None"         agent_utterance = bot.starting_prompt      return state_schema, agent_acts, agent_utterance ``` |

#### prepare\_semantic\_parser\_input

```
prepare_semantic_parser_input(bot, dlg_history, current_dlg_turn)
```

Prepares input for semantic parsing by gathering necessary context and schemas.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` |  | The bot instance containing worksheets and database models. | *required* |
| `dlg_history` |  | List of previous dialogue turns. | *required* |
| `current_dlg_turn` |  | The current dialogue turn being processed. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `tuple` |  | A tuple containing (state\_schema, agent\_acts, agent\_utterance, available\_worksheets\_text, available\_dbs\_text). |

Source code in `src/worksheets/annotation_utils.py`

|  |  |
| --- | --- |
| ``` 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 ``` | ``` def prepare_semantic_parser_input(bot, dlg_history, current_dlg_turn):     """Prepares input for semantic parsing by gathering necessary context and schemas.      Args:         bot: The bot instance containing worksheets and database models.         dlg_history: List of previous dialogue turns.         current_dlg_turn: The current dialogue turn being processed.      Returns:         tuple: A tuple containing (state_schema, agent_acts, agent_utterance,                available_worksheets_text, available_dbs_text).     """     state_schema, agent_acts, agent_utterance = prepare_context_input(         bot, dlg_history, current_dlg_turn     )      available_worksheets = [         ws.get_semantic_parser_schema() for ws in bot.genie_worksheets     ]     available_worksheets_text = "\n".join(available_worksheets)      available_dbs = [db.get_semantic_parser_schema() for db in bot.genie_db_models]     available_dbs_text = "\n".join(available_dbs)     return (         state_schema,         agent_acts,         agent_utterance,         available_worksheets_text,         available_dbs_text,     ) ``` |

## Utils

## src.worksheets.utils

### Functions

#### callable\_name

```
callable_name(any_callable)
```

Source code in `src/worksheets/utils.py`

|  |  |
| --- | --- |
| ```  7  8  9 10 11 12 13 14 ``` | ``` def callable_name(any_callable):     if isinstance(any_callable, partial):         return any_callable.func.__name__      try:         return any_callable.__name__     except AttributeError:         return str(any_callable) ``` |

#### deep\_compare\_lists

```
deep_compare_lists(list1, list2)
```

Source code in `src/worksheets/utils.py`

|  |  |
| --- | --- |
| ``` 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` | ``` def deep_compare_lists(list1, list2):     try:         # First, try the simple Counter method for hashable elements.         from collections import Counter          return Counter(list1) == Counter(list2)     except TypeError:         # If elements are unhashable, fall back to a method that sorts them.         # This requires all elements to be comparable.         try:             return sorted(list1) == sorted(list2)         except TypeError:             # Final fallback: Convert inner structures to tuples if they are lists             def to_tuple(x):                 if isinstance(x, list):                     return tuple(to_tuple(e) for e in x)                 return x              return sorted(map(to_tuple, list1)) == sorted(map(to_tuple, list2)) ``` |

#### generate\_var\_name

```
generate_var_name(name)
```

Source code in `src/worksheets/utils.py`

|  |  |
| --- | --- |
| ``` 38 39 40 41 42 ``` | ``` def generate_var_name(name):     name = camel_to_snake(name)     name = name.lower()      return name ``` |

#### camel\_to\_snake

```
camel_to_snake(name)
```

Source code in `src/worksheets/utils.py`

|  |  |
| --- | --- |
| ``` 45 46 47 ``` | ``` def camel_to_snake(name):     name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)     return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower() ``` |

#### extract\_code\_block\_from\_output

```
extract_code_block_from_output(output: str, lang='python')
```

Source code in `src/worksheets/utils.py`

|  |  |
| --- | --- |
| ``` 50 51 52 53 54 55 56 57 58 ``` | ``` def extract_code_block_from_output(output: str, lang="python"):     code = output.split("```")     if len(code) > 1:         res = code[1]         if res.startswith(lang):             res = res[len(lang) :]         return res     else:         return output ``` |

#### num\_tokens\_from\_string

```
num_tokens_from_string(string: str, model: str = 'gpt-3.5-turbo') -> int
```

Returns the number of tokens in a text string.

Source code in `src/worksheets/utils.py`

|  |  |
| --- | --- |
| ``` 61 62 63 64 65 ``` | ``` def num_tokens_from_string(string: str, model: str = "gpt-3.5-turbo") -> int:     """Returns the number of tokens in a text string."""     encoding = tiktoken.encoding_for_model(model)     num_tokens = len(encoding.encode(string))     return num_tokens ``` |

## Interface Utils

## src.worksheets.interface\_utils

### Classes

#### bcolors

Source code in `src/worksheets/interface_utils.py`

|  |  |
| --- | --- |
| ``` 33 34 35 36 37 38 39 40 41 42 ``` | ``` class bcolors:     HEADER = "\033[95m"     OKBLUE = "\033[94m"     OKCYAN = "\033[96m"     OKGREEN = "\033[92m"     WARNING = "\033[93m"     FAIL = "\033[91m"     ENDC = "\033[0m"     BOLD = "\033[1m"     UNDERLINE = "\033[4m" ``` |

##### Attributes

###### HEADER `class-attribute` `instance-attribute`

```
HEADER = '\x1b[95m'
```

###### OKBLUE `class-attribute` `instance-attribute`

```
OKBLUE = '\x1b[94m'
```

###### OKCYAN `class-attribute` `instance-attribute`

```
OKCYAN = '\x1b[96m'
```

###### OKGREEN `class-attribute` `instance-attribute`

```
OKGREEN = '\x1b[92m'
```

###### WARNING `class-attribute` `instance-attribute`

```
WARNING = '\x1b[93m'
```

###### FAIL `class-attribute` `instance-attribute`

```
FAIL = '\x1b[91m'
```

###### ENDC `class-attribute` `instance-attribute`

```
ENDC = '\x1b[0m'
```

###### BOLD `class-attribute` `instance-attribute`

```
BOLD = '\x1b[1m'
```

###### UNDERLINE `class-attribute` `instance-attribute`

```
UNDERLINE = '\x1b[4m'
```

### Functions

#### convert\_to\_json

```
convert_to_json(dialogue: list[CurrentDialogueTurn])
```

Convert the dialogue history to a JSON-compatible format.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `dialogue` | `list[CurrentDialogueTurn]` | The dialogue history. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | list[dict]: The dialogue history in JSON format. |

Source code in `src/worksheets/interface_utils.py`

|  |  |
| --- | --- |
| ```  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` | ``` def convert_to_json(dialogue: list[CurrentDialogueTurn]):     """Convert the dialogue history to a JSON-compatible format.      Args:         dialogue (list[CurrentDialogueTurn]): The dialogue history.      Returns:         list[dict]: The dialogue history in JSON format.     """     json_dialogue = []     for turn in dialogue:         json_turn = {             "user": turn.user_utterance,             "bot": turn.system_response,             "turn_context": get_context_schema(turn.context),             "global_context": get_context_schema(turn.global_context),             "system_action": get_agent_action_schemas(turn.system_action),             "user_target_sp": turn.user_target_sp,             "user_target": turn.user_target,             "user_target_suql": turn.user_target_suql,         }         json_dialogue.append(json_turn)     return json_dialogue ``` |

#### input\_user

```
input_user() -> str
```

Prompt the user for input and return the input string.

Source code in `src/worksheets/interface_utils.py`

|  |  |
| --- | --- |
| ``` 45 46 47 48 49 50 51 52 53 54 ``` | ``` def input_user() -> str:     """Prompt the user for input and return the input string."""     try:         user_utterance = input(bcolors.OKCYAN + bcolors.BOLD + "User: ")         # ignore empty inputs         while not user_utterance.strip():             user_utterance = input(bcolors.OKCYAN + bcolors.BOLD + "User: ")     finally:         print(bcolors.ENDC)     return user_utterance ``` |

#### print\_chatbot

```
print_chatbot(s: str)
```

Print the chatbot's response in a formatted way.

Source code in `src/worksheets/interface_utils.py`

|  |  |
| --- | --- |
| ``` 57 58 59 ``` | ``` def print_chatbot(s: str):     """Print the chatbot's response in a formatted way."""     print(bcolors.OKGREEN + bcolors.BOLD + "Agent: " + s + bcolors.ENDC) ``` |

#### print\_user

```
print_user(s: str)
```

Print the user's utterance in a formatted way.

Source code in `src/worksheets/interface_utils.py`

|  |  |
| --- | --- |
| ``` 62 63 64 ``` | ``` def print_user(s: str):     """Print the user's utterance in a formatted way."""     print(bcolors.OKCYAN + bcolors.BOLD + "User: " + s + bcolors.ENDC) ``` |

#### print\_complete\_history

```
print_complete_history(dialogue_history)
```

Print the complete dialogue history.

Source code in `src/worksheets/interface_utils.py`

|  |  |
| --- | --- |
| ``` 67 68 69 70 71 ``` | ``` def print_complete_history(dialogue_history):     """Print the complete dialogue history."""     for turn in dialogue_history:         print_user(turn.user_utterance)         print_chatbot(turn.system_response) ``` |

#### conversation\_loop `async`

```
conversation_loop(bot, output_state_path, quit_commands=None)
```

Run the conversation loop with the chatbot. Dumps the dialogue history to a JSON file upon exit.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` |  | The chatbot instance. | *required* |
| `output_state_path` | `str` | The path to save the dialogue history. | *required* |
| `quit_commands` | `list[str]` | List of commands to quit the conversation. Defaults to None. | `None` |

Source code in `src/worksheets/interface_utils.py`

|  |  |
| --- | --- |
| ```  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 ``` | ``` async def conversation_loop(bot, output_state_path, quit_commands=None):     """Run the conversation loop with the chatbot. Dumps the dialogue history to a JSON file upon exit.      Args:         bot: The chatbot instance.         output_state_path (str): The path to save the dialogue history.         quit_commands (list[str], optional): List of commands to quit the conversation. Defaults to None.     """     if quit_commands is None:         quit_commands = ["exit", "exit()"]      try:         while True:             if len(bot.dlg_history) == 0:                 print_chatbot(bot.starting_prompt)             user_utterance = None             if user_utterance is None:                 user_utterance = input_user()             if user_utterance == quit_commands:                 break              await generate_next_turn(user_utterance, bot)             print_complete_history(bot.dlg_history)     except Exception as e:         print(e)          import traceback          traceback.print_exc()     finally:         with open(output_state_path, "w") as f:             json.dump(convert_to_json(bot.dlg_history), f, indent=4) ``` |

## GSheet Utils

## src.worksheets.gsheet\_utils

### Attributes

#### CURR\_DIR `module-attribute`

```
CURR_DIR = dirname(realpath(__file__))
```

#### SCOPES `module-attribute`

```
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
```

### Functions

#### retrieve\_gsheet

```
retrieve_gsheet(id, range)
```

Retrieve values from a Google Sheet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `id` | `str` | The ID of the Google Sheet. | *required* |
| `range` | `str` | The range of cells to retrieve. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `List` |  | A list of values from the specified range in the Google Sheet. |

Source code in `src/worksheets/gsheet_utils.py`

|  |  |
| --- | --- |
| ``` 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` | ``` def retrieve_gsheet(id, range):     """Retrieve values from a Google Sheet.      Args:         id (str): The ID of the Google Sheet.         range (str): The range of cells to retrieve.      Returns:         List: A list of values from the specified range in the Google Sheet."""     creds = using_service_account()      try:         service = build("sheets", "v4", credentials=creds)          # Call the Sheets API         sheet = service.spreadsheets()         result = sheet.values().get(spreadsheetId=id, range=range).execute()         values: List = result.get("values", [])          return values      except HttpError as err:         print(err) ``` |

#### fill\_all\_empty

```
fill_all_empty(rows, desired_columns)
```

Source code in `src/worksheets/gsheet_utils.py`

|  |  |
| --- | --- |
| ``` 43 44 45 46 47 ``` | ``` def fill_all_empty(rows, desired_columns):     for row in rows:         for i in range(desired_columns - len(row)):             row.append("")     return rows ``` |

#### using\_service\_account

```
using_service_account()
```

Source code in `src/worksheets/gsheet_utils.py`

|  |  |
| --- | --- |
| ``` 50 51 52 53 54 55 56 57 58 59 60 61 62 ``` | ``` def using_service_account():     # Path to your service account key file     SERVICE_ACCOUNT_FILE = os.path.join(CURR_DIR, "service_account.json")      # Scopes required by the Sheets API     SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]      # Create credentials using the service account key file     credentials = service_account.Credentials.from_service_account_file(         SERVICE_ACCOUNT_FILE, scopes=SCOPES     )      return credentials ``` |

## Chat

## src.worksheets.chat

### Functions

#### generate\_next\_turn `async`

```
generate_next_turn(user_utterance: str, bot)
```

Generate the next turn in the dialogue based on the user's utterance.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `user_utterance` | `str` | The user's input. | *required* |
| `bot` | `Agent` | The bot instance handling the dialogue. | *required* |

Source code in `src/worksheets/chat.py`

|  |  |
| --- | --- |
| ```  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` | ``` async def generate_next_turn(user_utterance: str, bot):     """Generate the next turn in the dialogue based on the user's utterance.      Args:         user_utterance (str): The user's input.         bot (Agent): The bot instance handling the dialogue.     """     # instantiate a new dialogue turn     current_dlg_turn = CurrentDialogueTurn()     current_dlg_turn.user_utterance = user_utterance      # initialize contexts     current_dlg_turn.context = GenieContext()     current_dlg_turn.global_context = GenieContext()      # process the dialogue turn to GenieWorksheets     await semantic_parsing(current_dlg_turn, bot.dlg_history, bot)      # run the agent policy if user_target is not None     if current_dlg_turn.user_target is not None:         run_agent_policy(current_dlg_turn, bot)      # generate a response based on the agent policy     await generate_response(current_dlg_turn, bot.dlg_history, bot)     bot.dlg_history.append(current_dlg_turn) ``` |

Back to top
