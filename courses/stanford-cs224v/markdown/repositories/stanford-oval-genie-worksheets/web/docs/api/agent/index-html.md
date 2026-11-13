# Project code: stanford-oval/genie-worksheets: web/docs/api/agent/index.html

[Course index](../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/docs/api/agent/index.html) · [Raw file](../../../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/api/agent/index.html)

Retrieved: 2026-11-13T17:06:24.900930+00:00

# Agent

## src.worksheets.agent

### Classes

#### Agent

Bases: `BaseModel`

Agent setting for GenieWorksheets

Source code in `src/worksheets/agent.py`

|  |  |
| --- | --- |
| ```  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 ``` | ``` class Agent(BaseModel):     """Agent setting for GenieWorksheets"""      # name of the agent     botname: str      # description of the agent. This is used for generating response     description: str      # directory where the prompts are stored     prompt_dir: str      # starting prompt for the agent to ask the user     starting_prompt: str      # arguments to pass to the agent for configuration     args: dict      # list of functions that are available to the agent for execution     api: list      # knowledge configuration for the agent to run queries and respond to the user     knowledge_base: SUQLKnowledgeBase      # semantic parser for knowledge queries     knowledge_parser: BaseSUQLParser      def load_from_gsheet(self, gsheet_id: str):         """Load the agent configuration from the google sheet.          Args:             gsheet_id (str): The ID of the Google Sheet.          Returns:             GenieRuntime: An instance of GenieRuntime configured with the loaded data.         """          # Load Genie worksheets, databases, and types from the Google Sheet         genie_worsheets, genie_dbs, genie_types = gsheet_to_genie(gsheet_id)          # Create a SUQL runner if knowledge_base is provided. Suql runner is used by the         # GenieRuntime to run queries against the knowledge base.         if self.knowledge_base:              def suql_runner(query, *args, **kwargs):                 return self.knowledge_base.run(query, *args, **kwargs)          else:             suql_runner = None          # Create an instance of GenieRuntime with the loaded configuration         bot = GenieRuntime(             name=self.botname,             prompt_dir=self.prompt_dir,             starting_prompt=self.starting_prompt,             description=self.description,             args=self.args,             api=self.api,             suql_runner=suql_runner,             suql_parser=self.knowledge_parser,         )          # Add worksheets, databases, and types to the GenieRuntime instance         for worksheet in genie_worsheets:             bot.add_worksheet(worksheet)          for db in genie_dbs:             bot.add_db_model(db)          for genie_type in genie_types:             bot.add_worksheet(genie_type)          return bot ``` |

##### Attributes

###### botname `instance-attribute`

```
botname: str
```

###### description `instance-attribute`

```
description: str
```

###### prompt\_dir `instance-attribute`

```
prompt_dir: str
```

###### starting\_prompt `instance-attribute`

```
starting_prompt: str
```

###### args `instance-attribute`

```
args: dict
```

###### api `instance-attribute`

```
api: list
```

###### knowledge\_base `instance-attribute`

```
knowledge_base: SUQLKnowledgeBase
```

###### knowledge\_parser `instance-attribute`

```
knowledge_parser: BaseSUQLParser
```

##### Functions

###### load\_from\_gsheet

```
load_from_gsheet(gsheet_id: str)
```

Load the agent configuration from the google sheet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `gsheet_id` | `str` | The ID of the Google Sheet. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `GenieRuntime` |  | An instance of GenieRuntime configured with the loaded data. |

Source code in `src/worksheets/agent.py`

|  |  |
| --- | --- |
| ``` 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 ``` | ``` def load_from_gsheet(self, gsheet_id: str):     """Load the agent configuration from the google sheet.      Args:         gsheet_id (str): The ID of the Google Sheet.      Returns:         GenieRuntime: An instance of GenieRuntime configured with the loaded data.     """      # Load Genie worksheets, databases, and types from the Google Sheet     genie_worsheets, genie_dbs, genie_types = gsheet_to_genie(gsheet_id)      # Create a SUQL runner if knowledge_base is provided. Suql runner is used by the     # GenieRuntime to run queries against the knowledge base.     if self.knowledge_base:          def suql_runner(query, *args, **kwargs):             return self.knowledge_base.run(query, *args, **kwargs)      else:         suql_runner = None      # Create an instance of GenieRuntime with the loaded configuration     bot = GenieRuntime(         name=self.botname,         prompt_dir=self.prompt_dir,         starting_prompt=self.starting_prompt,         description=self.description,         args=self.args,         api=self.api,         suql_runner=suql_runner,         suql_parser=self.knowledge_parser,     )      # Add worksheets, databases, and types to the GenieRuntime instance     for worksheet in genie_worsheets:         bot.add_worksheet(worksheet)      for db in genie_dbs:         bot.add_db_model(db)      for genie_type in genie_types:         bot.add_worksheet(genie_type)      return bot ``` |

Back to top
