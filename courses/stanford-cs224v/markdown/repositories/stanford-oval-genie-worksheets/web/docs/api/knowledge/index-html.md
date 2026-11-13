# Project code: stanford-oval/genie-worksheets: web/docs/api/knowledge/index.html

[Course index](../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/docs/api/knowledge/index.html) · [Raw file](../../../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/api/knowledge/index.html)

Retrieved: 2026-11-13T17:06:24.900930+00:00

# Knowledge

## src.worksheets.knowledge

### Attributes

#### CURRENT\_DIR `module-attribute`

```
CURRENT_DIR = dirname(realpath(__file__))
```

### Classes

#### SUQLKnowledgeBase

Bases: `BaseModel`

Knowledge base for SUQL queries

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 ``` | ``` class SUQLKnowledgeBase(BaseModel):     """Knowledge base for SUQL queries"""      # Name of the LLM model to use for the queries     llm_model_name: str      # Tables with primary keys as values for the queries.     # TODO: This should be automatically generated from the database schema     tables_with_primary_keys: Optional[dict] = None      # Name of the database to run the queries on     database_name: Optional[str] = None      # Address of the embedding server to use for the queries on free-text data     embedding_server_address: Optional[str] = None      # Mapping of free-text files to their paths for free-text data     source_file_mapping: Optional[dict] = None      # Function to run on the generated SUQL query     postprocessing_fn: Callable      # Function to run on the result from execution of the SUQL query     result_postprocessing_fn: Optional[Callable] = None      # Maximum number of rows to return in the result     max_rows: int = 3      # Username for the database     db_username: Optional[str] = None      # Password for the database     db_password: Optional[str] = None      # db host     db_host: str = "127.0.0.1"      # db port     db_port: str = "5432"      # Additional parameters for Azure     api_base: Optional[str] = None      api_version: Optional[str] = None      def run(self, query, *args, **kwargs):         """Run the SUQL query and return the result."""          if self.postprocessing_fn:             query = self.postprocessing_fn(query)          query = query.strip().replace("\\'", "'")          results, column_names, _ = suql_execute(             query,             table_w_ids=self.tables_with_primary_keys,             database=self.database_name,             llm_model_name=self.llm_model_name,             embedding_server_address=self.embedding_server_address,             source_file_mapping=self.source_file_mapping,             select_username=self.db_username,             select_userpswd=self.db_password,             host=self.db_host,             port=self.db_port,             api_base=self.api_base,             api_version=self.api_version,         )          # Convert the results to a list of dictionaries for genie worksheets         results = [dict(zip(column_names, result)) for result in results]          if self.result_postprocessing_fn:             results = self.result_postprocessing_fn(results, column_names)          return results[: self.max_rows] ``` |

##### Attributes

###### llm\_model\_name `instance-attribute`

```
llm_model_name: str
```

###### tables\_with\_primary\_keys `class-attribute` `instance-attribute`

```
tables_with_primary_keys: Optional[dict] = None
```

###### database\_name `class-attribute` `instance-attribute`

```
database_name: Optional[str] = None
```

###### embedding\_server\_address `class-attribute` `instance-attribute`

```
embedding_server_address: Optional[str] = None
```

###### source\_file\_mapping `class-attribute` `instance-attribute`

```
source_file_mapping: Optional[dict] = None
```

###### postprocessing\_fn `instance-attribute`

```
postprocessing_fn: Callable
```

###### result\_postprocessing\_fn `class-attribute` `instance-attribute`

```
result_postprocessing_fn: Optional[Callable] = None
```

###### max\_rows `class-attribute` `instance-attribute`

```
max_rows: int = 3
```

###### db\_username `class-attribute` `instance-attribute`

```
db_username: Optional[str] = None
```

###### db\_password `class-attribute` `instance-attribute`

```
db_password: Optional[str] = None
```

###### db\_host `class-attribute` `instance-attribute`

```
db_host: str = '127.0.0.1'
```

###### db\_port `class-attribute` `instance-attribute`

```
db_port: str = '5432'
```

###### api\_base `class-attribute` `instance-attribute`

```
api_base: Optional[str] = None
```

###### api\_version `class-attribute` `instance-attribute`

```
api_version: Optional[str] = None
```

##### Functions

###### run

```
run(query, *args, **kwargs)
```

Run the SUQL query and return the result.

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 ``` | ``` def run(self, query, *args, **kwargs):     """Run the SUQL query and return the result."""      if self.postprocessing_fn:         query = self.postprocessing_fn(query)      query = query.strip().replace("\\'", "'")      results, column_names, _ = suql_execute(         query,         table_w_ids=self.tables_with_primary_keys,         database=self.database_name,         llm_model_name=self.llm_model_name,         embedding_server_address=self.embedding_server_address,         source_file_mapping=self.source_file_mapping,         select_username=self.db_username,         select_userpswd=self.db_password,         host=self.db_host,         port=self.db_port,         api_base=self.api_base,         api_version=self.api_version,     )      # Convert the results to a list of dictionaries for genie worksheets     results = [dict(zip(column_names, result)) for result in results]      if self.result_postprocessing_fn:         results = self.result_postprocessing_fn(results, column_names)      return results[: self.max_rows] ``` |

#### BaseSUQLParser

Bases: `BaseModel`

Base class for SUQL parsers

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ```  98  99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 ``` | ``` class BaseSUQLParser(BaseModel):     """Base class for SUQL parsers"""      # Name of the LLM model to use for the queries     llm_model_name: str      async def parse(self, dlg_history: List[CurrentDialogueTurn], query: str):         raise NotImplementedError      def convert_dlg_turn_to_suql_dlg_turn(self, dlg_history, turn, db_results):         # Convert the dialog history to the expected format for SUQL         suql_dlg_history = []         for i, turn in enumerate(dlg_history):             user_target = turn.user_target_suql             agent_utterance = turn.system_response             user_utterance = turn.user_utterance              if db_results is None:                 db_result = [                     obj.result                     for obj in turn.context.context.values()                     if isinstance(obj, Answer)                     and obj.query.value == turn.user_target_suql                 ]             else:                 db_result = db_results[i]              suql_dlg_history.append(                 SUQLDialogueTurn(                     user_utterance=user_utterance,                     db_results=db_result,                     user_target=user_target,                     agent_utterance=agent_utterance,                 )             )          return suql_dlg_history ``` |

##### Attributes

###### llm\_model\_name `instance-attribute`

```
llm_model_name: str
```

##### Functions

###### parse `async`

```
parse(dlg_history: List[CurrentDialogueTurn], query: str)
```

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 104 105 ``` | ``` async def parse(self, dlg_history: List[CurrentDialogueTurn], query: str):     raise NotImplementedError ``` |

###### convert\_dlg\_turn\_to\_suql\_dlg\_turn

```
convert_dlg_turn_to_suql_dlg_turn(dlg_history, turn, db_results)
```

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 ``` | ``` def convert_dlg_turn_to_suql_dlg_turn(self, dlg_history, turn, db_results):     # Convert the dialog history to the expected format for SUQL     suql_dlg_history = []     for i, turn in enumerate(dlg_history):         user_target = turn.user_target_suql         agent_utterance = turn.system_response         user_utterance = turn.user_utterance          if db_results is None:             db_result = [                 obj.result                 for obj in turn.context.context.values()                 if isinstance(obj, Answer)                 and obj.query.value == turn.user_target_suql             ]         else:             db_result = db_results[i]          suql_dlg_history.append(             SUQLDialogueTurn(                 user_utterance=user_utterance,                 db_results=db_result,                 user_target=user_target,                 agent_utterance=agent_utterance,             )         )      return suql_dlg_history ``` |

#### SUQLParser

Bases: `BaseSUQLParser`

Parser for SUQL queries

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 ``` | ``` class SUQLParser(BaseSUQLParser):     """Parser for SUQL queries"""      # Selector for the prompt to use for the queries     prompt_selector: Optional[Callable] = None      async def parse(         self,         dlg_history: List[CurrentDialogueTurn],         query: str,         bot: GenieRuntime,         db_results: List[str] | None = None,     ):         """         A SUQL conversational semantic parser, with a pre-set prompt file.         The function convets the List[CurrentDialogueTurn] to the expected format         in SUQL (suql.agent.DialogueTurn) and calls the prompt file.          # Parameters:          `dlg_history` (List[CurrentDialogueTurn]): a list of past dialog turns.          `query` (str): the current query to be parsed.          # Returns:          `parsed_output` (str): a parsed SUQL output         """          suql_dlg_history = self.convert_dlg_turn_to_suql_dlg_turn(             dlg_history, query, db_results         )          # Use the prompt selector if available         if self.prompt_selector:             prompt_file = await self.prompt_selector(bot, dlg_history, query)         else:             prompt_file = "suql_parser.prompt"          # Generate the SUQL output         parsed_output = await llm_generate(             prompt_file,             prompt_inputs={                 "dlg": suql_dlg_history,                 "query": query,                 "date": datetime.now().strftime("%Y-%m-%d"),                 "day": datetime.now().strftime("%A"),                 "day_tmr": (datetime.now() + timedelta(days=1)).strftime("%A"),             },             prompt_dir=bot.prompt_dir,             model_name=self.llm_model_name,             temperature=0.0,         )          return extract_code_block_from_output(parsed_output, lang="sql") ``` |

##### Attributes

###### llm\_model\_name `instance-attribute`

```
llm_model_name: str
```

###### prompt\_selector `class-attribute` `instance-attribute`

```
prompt_selector: Optional[Callable] = None
```

##### Functions

###### convert\_dlg\_turn\_to\_suql\_dlg\_turn

```
convert_dlg_turn_to_suql_dlg_turn(dlg_history, turn, db_results)
```

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 ``` | ``` def convert_dlg_turn_to_suql_dlg_turn(self, dlg_history, turn, db_results):     # Convert the dialog history to the expected format for SUQL     suql_dlg_history = []     for i, turn in enumerate(dlg_history):         user_target = turn.user_target_suql         agent_utterance = turn.system_response         user_utterance = turn.user_utterance          if db_results is None:             db_result = [                 obj.result                 for obj in turn.context.context.values()                 if isinstance(obj, Answer)                 and obj.query.value == turn.user_target_suql             ]         else:             db_result = db_results[i]          suql_dlg_history.append(             SUQLDialogueTurn(                 user_utterance=user_utterance,                 db_results=db_result,                 user_target=user_target,                 agent_utterance=agent_utterance,             )         )      return suql_dlg_history ``` |

###### parse `async`

```
parse(dlg_history: List[CurrentDialogueTurn], query: str, bot: GenieRuntime, db_results: List[str] | None = None)
```

A SUQL conversational semantic parser, with a pre-set prompt file.
The function convets the List[CurrentDialogueTurn] to the expected format
in SUQL (suql.agent.DialogueTurn) and calls the prompt file.

###### Parameters:

`dlg_history` (List[CurrentDialogueTurn]): a list of past dialog turns.

`query` (str): the current query to be parsed.

###### Returns:

`parsed_output` (str): a parsed SUQL output

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 ``` | ``` async def parse(     self,     dlg_history: List[CurrentDialogueTurn],     query: str,     bot: GenieRuntime,     db_results: List[str] | None = None, ):     """     A SUQL conversational semantic parser, with a pre-set prompt file.     The function convets the List[CurrentDialogueTurn] to the expected format     in SUQL (suql.agent.DialogueTurn) and calls the prompt file.      # Parameters:      `dlg_history` (List[CurrentDialogueTurn]): a list of past dialog turns.      `query` (str): the current query to be parsed.      # Returns:      `parsed_output` (str): a parsed SUQL output     """      suql_dlg_history = self.convert_dlg_turn_to_suql_dlg_turn(         dlg_history, query, db_results     )      # Use the prompt selector if available     if self.prompt_selector:         prompt_file = await self.prompt_selector(bot, dlg_history, query)     else:         prompt_file = "suql_parser.prompt"      # Generate the SUQL output     parsed_output = await llm_generate(         prompt_file,         prompt_inputs={             "dlg": suql_dlg_history,             "query": query,             "date": datetime.now().strftime("%Y-%m-%d"),             "day": datetime.now().strftime("%A"),             "day_tmr": (datetime.now() + timedelta(days=1)).strftime("%A"),         },         prompt_dir=bot.prompt_dir,         model_name=self.llm_model_name,         temperature=0.0,     )      return extract_code_block_from_output(parsed_output, lang="sql") ``` |

#### SUQLReActParser

Bases: `BaseSUQLParser`

ReAct Parser for SUQL queries

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 ``` | ``` class SUQLReActParser(BaseSUQLParser):     """ReAct Parser for SUQL queries"""      # Select examples for the queries     example_path: str      # Select instructions for the queries     instruction_path: str      # Select table schema for the queries     table_schema_path: str      # Knowledge base for the queries     knowledge: SUQLKnowledgeBase      # List of examples for the queries     examples: Optional[List[str]] = None      # List of instructions for the queries     instructions: Optional[List[str]] = None      # Table schema for the queries     table_schema: Optional[str] = None      # Conversation history for the queries     conversation_history: List = []      def __init__(self, **kwargs):         super().__init__(**kwargs)          if self.examples is None:             self.examples = []             with open(self.example_path, "r") as f:                 text = f.read()              for example in text.split("--"):                 if example.strip():                     self.examples.append(example.strip())          if self.instructions is None:             with open(self.instruction_path, "r") as f:                 self.instructions = f.readlines()          if self.table_schema is None:             with open(self.table_schema_path, "r") as f:                 self.table_schema = f.read()      async def parse(         self,         dlg_history: List[CurrentDialogueTurn],         query: str,         bot: GenieRuntime,         db_results: List[str] | None = None,     ):         suql_dlg_history = self.convert_dlg_turn_to_suql_dlg_turn(             dlg_history, query, db_results         )          self.conversation_history = suql_dlg_history          output = await self.anext_turn(             query,             update_conversation_history=False,             table_w_ids=self.knowledge.tables_with_primary_keys,             database_name=self.knowledge.database_name,             embedding_server_address=self.knowledge.embedding_server_address,             source_file_mapping=self.knowledge.source_file_mapping,         )          # TODO: KeyError: 'final_sql'         # happens when the action_counter limit is met without a final SQL being generated         logger.info(f"SUQL output: {output}")         try:             final_output = output["final_sql"].sql         except Exception as e:             logger.error(f"Error in parsing output: {e}")             final_output = None         return final_output      async def anext_turn(         self,         user_input: str,         update_conversation_history: bool = False,         table_w_ids: dict = None,         database_name: str = None,         embedding_server_address: str = None,         source_file_mapping: dict = None,     ):         try:             parser = PartToWholeParser()             parser.initialize(                 engine=self.llm_model_name,                 table_w_ids=table_w_ids,                 database_name=database_name,                 suql_model_name=self.knowledge.llm_model_name,                 suql_api_base=self.knowledge.api_base,                 suql_api_version=self.knowledge.api_version,                 embedding_server_address=embedding_server_address,                 source_file_mapping=source_file_mapping,                 domain_instructions=self.instructions,                 examples=self.examples,                 table_schema=self.table_schema,             )              output = await parser.arun(                 {                     "question": user_input,                     "conversation_history": self.conversation_history,                 }             )         finally:             write_prompt_logs_to_file(append=True, include_timestamp=True)          if update_conversation_history:             self.update_turn(self.conversation_history, output, response=None)          return output      def update_turn(self, conversation_history, output, response):         turn = DialogueTurn(             user_utterance=output["question"],             agent_utterance=response,             user_target=output["final_sql"].sql,             db_results=output["final_sql"].execution_result,         )          conversation_history.append(turn) ``` |

##### Attributes

###### llm\_model\_name `instance-attribute`

```
llm_model_name: str
```

###### example\_path `instance-attribute`

```
example_path: str
```

###### instruction\_path `instance-attribute`

```
instruction_path: str
```

###### table\_schema\_path `instance-attribute`

```
table_schema_path: str
```

###### knowledge `instance-attribute`

```
knowledge: SUQLKnowledgeBase
```

###### examples `class-attribute` `instance-attribute`

```
examples: Optional[List[str]] = None
```

###### conversation\_history `class-attribute` `instance-attribute`

```
conversation_history: List = []
```

###### instructions `class-attribute` `instance-attribute`

```
instructions: Optional[List[str]] = readlines()
```

###### table\_schema `class-attribute` `instance-attribute`

```
table_schema: Optional[str] = read()
```

##### Functions

###### convert\_dlg\_turn\_to\_suql\_dlg\_turn

```
convert_dlg_turn_to_suql_dlg_turn(dlg_history, turn, db_results)
```

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 ``` | ``` def convert_dlg_turn_to_suql_dlg_turn(self, dlg_history, turn, db_results):     # Convert the dialog history to the expected format for SUQL     suql_dlg_history = []     for i, turn in enumerate(dlg_history):         user_target = turn.user_target_suql         agent_utterance = turn.system_response         user_utterance = turn.user_utterance          if db_results is None:             db_result = [                 obj.result                 for obj in turn.context.context.values()                 if isinstance(obj, Answer)                 and obj.query.value == turn.user_target_suql             ]         else:             db_result = db_results[i]          suql_dlg_history.append(             SUQLDialogueTurn(                 user_utterance=user_utterance,                 db_results=db_result,                 user_target=user_target,                 agent_utterance=agent_utterance,             )         )      return suql_dlg_history ``` |

###### \_\_init\_\_

```
__init__(**kwargs)
```

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 ``` | ``` def __init__(self, **kwargs):     super().__init__(**kwargs)      if self.examples is None:         self.examples = []         with open(self.example_path, "r") as f:             text = f.read()          for example in text.split("--"):             if example.strip():                 self.examples.append(example.strip())      if self.instructions is None:         with open(self.instruction_path, "r") as f:             self.instructions = f.readlines()      if self.table_schema is None:         with open(self.table_schema_path, "r") as f:             self.table_schema = f.read() ``` |

###### parse `async`

```
parse(dlg_history: List[CurrentDialogueTurn], query: str, bot: GenieRuntime, db_results: List[str] | None = None)
```

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 ``` | ``` async def parse(     self,     dlg_history: List[CurrentDialogueTurn],     query: str,     bot: GenieRuntime,     db_results: List[str] | None = None, ):     suql_dlg_history = self.convert_dlg_turn_to_suql_dlg_turn(         dlg_history, query, db_results     )      self.conversation_history = suql_dlg_history      output = await self.anext_turn(         query,         update_conversation_history=False,         table_w_ids=self.knowledge.tables_with_primary_keys,         database_name=self.knowledge.database_name,         embedding_server_address=self.knowledge.embedding_server_address,         source_file_mapping=self.knowledge.source_file_mapping,     )      # TODO: KeyError: 'final_sql'     # happens when the action_counter limit is met without a final SQL being generated     logger.info(f"SUQL output: {output}")     try:         final_output = output["final_sql"].sql     except Exception as e:         logger.error(f"Error in parsing output: {e}")         final_output = None     return final_output ``` |

###### anext\_turn `async`

```
anext_turn(user_input: str, update_conversation_history: bool = False, table_w_ids: dict = None, database_name: str = None, embedding_server_address: str = None, source_file_mapping: dict = None)
```

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 ``` | ``` async def anext_turn(     self,     user_input: str,     update_conversation_history: bool = False,     table_w_ids: dict = None,     database_name: str = None,     embedding_server_address: str = None,     source_file_mapping: dict = None, ):     try:         parser = PartToWholeParser()         parser.initialize(             engine=self.llm_model_name,             table_w_ids=table_w_ids,             database_name=database_name,             suql_model_name=self.knowledge.llm_model_name,             suql_api_base=self.knowledge.api_base,             suql_api_version=self.knowledge.api_version,             embedding_server_address=embedding_server_address,             source_file_mapping=source_file_mapping,             domain_instructions=self.instructions,             examples=self.examples,             table_schema=self.table_schema,         )          output = await parser.arun(             {                 "question": user_input,                 "conversation_history": self.conversation_history,             }         )     finally:         write_prompt_logs_to_file(append=True, include_timestamp=True)      if update_conversation_history:         self.update_turn(self.conversation_history, output, response=None)      return output ``` |

###### update\_turn

```
update_turn(conversation_history, output, response)
```

Source code in `src/worksheets/knowledge.py`

|  |  |
| --- | --- |
| ``` 312 313 314 315 316 317 318 319 320 ``` | ``` def update_turn(self, conversation_history, output, response):     turn = DialogueTurn(         user_utterance=output["question"],         agent_utterance=response,         user_target=output["final_sql"].sql,         db_results=output["final_sql"].execution_result,     )      conversation_history.append(turn) ``` |

Back to top
