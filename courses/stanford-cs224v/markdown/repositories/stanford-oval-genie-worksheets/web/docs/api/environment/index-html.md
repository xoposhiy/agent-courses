# Project code: stanford-oval/genie-worksheets: web/docs/api/environment/index.html

[Course index](../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/docs/api/environment/index.html) · [Raw file](../../../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/api/environment/index.html)

Retrieved: 2026-11-13T17:06:24.900930+00:00

# Environment

## src.worksheets.environment

Core environment module for Genie worksheets and runtime management.

This module provides the foundational classes and utilities for managing Genie worksheets,
including type handling, context management, and runtime execution. It implements the core
functionality for worksheet validation, action execution, and state management.

### Classes

#### GenieValue

A class to represent a value in Genie.

This class wraps primitive values (string, int, float, etc.) with additional
functionality like confirmation status tracking.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `value` |  | The wrapped primitive value. |
| `confirmed` | `bool` | Whether this value has been confirmed by the user. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 ``` | ``` class GenieValue:     """A class to represent a value in Genie.      This class wraps primitive values (string, int, float, etc.) with additional     functionality like confirmation status tracking.      Attributes:         value: The wrapped primitive value.         confirmed (bool): Whether this value has been confirmed by the user.     """      def __init__(self, value):         """Initialize a GenieValue.          Args:             value: The primitive value to wrap.         """         self.value = value         self.confirmed = False      def __repr__(self):         return f"{self.value}"      def __eq__(self, other):         if isinstance(other, GenieValue):             if self.value == other.value:                 return True          return self.value == other      def confirm(self, confirmed: bool = True):         """Mark the value as confirmed.          Args:             confirmed (bool, optional): Whether to mark as confirmed. Defaults to True.          Returns:             GenieValue: The confirmed value instance.         """         self.confirmed = confirmed         return self      def __str__(self):         return self.value      def __hash__(self):         return hash(self.value) ``` |

##### Attributes

###### value `instance-attribute`

```
value = value
```

###### confirmed `instance-attribute`

```
confirmed = False
```

##### Functions

###### \_\_init\_\_

```
__init__(value)
```

Initialize a GenieValue.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` |  | The primitive value to wrap. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 44 45 46 47 48 49 50 51 ``` | ``` def __init__(self, value):     """Initialize a GenieValue.      Args:         value: The primitive value to wrap.     """     self.value = value     self.confirmed = False ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 53 54 ``` | ``` def __repr__(self):     return f"{self.value}" ``` |

###### \_\_eq\_\_

```
__eq__(other)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 56 57 58 59 60 61 ``` | ``` def __eq__(self, other):     if isinstance(other, GenieValue):         if self.value == other.value:             return True      return self.value == other ``` |

###### confirm

```
confirm(confirmed: bool = True)
```

Mark the value as confirmed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `confirmed` | `bool` | Whether to mark as confirmed. Defaults to True. | `True` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `GenieValue` |  | The confirmed value instance. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 63 64 65 66 67 68 69 70 71 72 73 ``` | ``` def confirm(self, confirmed: bool = True):     """Mark the value as confirmed.      Args:         confirmed (bool, optional): Whether to mark as confirmed. Defaults to True.      Returns:         GenieValue: The confirmed value instance.     """     self.confirmed = confirmed     return self ``` |

###### \_\_str\_\_

```
__str__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 75 76 ``` | ``` def __str__(self):     return self.value ``` |

###### \_\_hash\_\_

```
__hash__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 78 79 ``` | ``` def __hash__(self):     return hash(self.value) ``` |

#### GenieResult

Bases: `GenieValue`

A class to represent results from executions.

This class extends GenieValue to store results from Answer executions or
other actions, maintaining references to parent objects.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `value` |  | The result value. |
| `parent` |  | The parent object that produced this result. |
| `parent_var_name` |  | The variable name of the parent in the context. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ```  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107 ``` | ``` class GenieResult(GenieValue):     """A class to represent results from executions.      This class extends GenieValue to store results from Answer executions or     other actions, maintaining references to parent objects.      Attributes:         value: The result value.         parent: The parent object that produced this result.         parent_var_name: The variable name of the parent in the context.     """      def __init__(self, value, parent, parent_var_name):         """Initialize a GenieResult.          Args:             value: The result value.             parent: The parent object that produced this result.             parent_var_name: The variable name of the parent in the context.         """         super().__init__(value)         self.parent = parent         self.parent_var_name = parent_var_name      def __getitem__(self, item):         return self.value[item] ``` |

##### Attributes

###### value `instance-attribute`

```
value = value
```

###### confirmed `instance-attribute`

```
confirmed = False
```

###### parent `instance-attribute`

```
parent = parent
```

###### parent\_var\_name `instance-attribute`

```
parent_var_name = parent_var_name
```

##### Functions

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 53 54 ``` | ``` def __repr__(self):     return f"{self.value}" ``` |

###### \_\_eq\_\_

```
__eq__(other)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 56 57 58 59 60 61 ``` | ``` def __eq__(self, other):     if isinstance(other, GenieValue):         if self.value == other.value:             return True      return self.value == other ``` |

###### confirm

```
confirm(confirmed: bool = True)
```

Mark the value as confirmed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `confirmed` | `bool` | Whether to mark as confirmed. Defaults to True. | `True` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `GenieValue` |  | The confirmed value instance. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 63 64 65 66 67 68 69 70 71 72 73 ``` | ``` def confirm(self, confirmed: bool = True):     """Mark the value as confirmed.      Args:         confirmed (bool, optional): Whether to mark as confirmed. Defaults to True.      Returns:         GenieValue: The confirmed value instance.     """     self.confirmed = confirmed     return self ``` |

###### \_\_str\_\_

```
__str__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 75 76 ``` | ``` def __str__(self):     return self.value ``` |

###### \_\_hash\_\_

```
__hash__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 78 79 ``` | ``` def __hash__(self):     return hash(self.value) ``` |

###### \_\_init\_\_

```
__init__(value, parent, parent_var_name)
```

Initialize a GenieResult.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` |  | The result value. | *required* |
| `parent` |  | The parent object that produced this result. | *required* |
| `parent_var_name` |  | The variable name of the parent in the context. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ```  94  95  96  97  98  99 100 101 102 103 104 ``` | ``` def __init__(self, value, parent, parent_var_name):     """Initialize a GenieResult.      Args:         value: The result value.         parent: The parent object that produced this result.         parent_var_name: The variable name of the parent in the context.     """     super().__init__(value)     self.parent = parent     self.parent_var_name = parent_var_name ``` |

###### \_\_getitem\_\_

```
__getitem__(item)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 106 107 ``` | ``` def __getitem__(self, item):     return self.value[item] ``` |

#### GenieREPR

Bases: `type`

A metaclass to customize string representation of Genie classes.

This metaclass provides custom string representation for classes that use it,
maintaining ordered attributes and generating schema representations.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `_ordered_attributes` |  | List of ordered attribute names for the class. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 ``` | ``` class GenieREPR(type):     """A metaclass to customize string representation of Genie classes.      This metaclass provides custom string representation for classes that use it,     maintaining ordered attributes and generating schema representations.      Attributes:         _ordered_attributes: List of ordered attribute names for the class.     """      def __new__(cls, name, bases, dct):         new_class = super().__new__(cls, name, bases, dct)         # Store the ordered attributes, these are used for asking questions in the order they are defined         new_class._ordered_attributes = [k for k in dct if not k.startswith("__")]         return new_class      def __repr__(cls):         parameters = []         for field in get_genie_fields_from_ws(cls):             parameters.append(field.schema(value=False))          return f"{cls.__name__}({', '.join([param for param in parameters])})"      def get_semantic_parser_schema(cls):         parameters = []         if hasattr(cls, "predicate") and (cls.predicate == "" or cls.predicate is True):             for field in get_genie_fields_from_ws(cls):                 if not field.internal:                     parameters.append(field.schema(value=False))          return f"{cls.__name__}({', '.join([repr(param) for param in parameters])})" ``` |

##### Functions

###### \_\_new\_\_

```
__new__(name, bases, dct)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 120 121 122 123 124 ``` | ``` def __new__(cls, name, bases, dct):     new_class = super().__new__(cls, name, bases, dct)     # Store the ordered attributes, these are used for asking questions in the order they are defined     new_class._ordered_attributes = [k for k in dct if not k.startswith("__")]     return new_class ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 126 127 128 129 130 131 ``` | ``` def __repr__(cls):     parameters = []     for field in get_genie_fields_from_ws(cls):         parameters.append(field.schema(value=False))      return f"{cls.__name__}({', '.join([param for param in parameters])})" ``` |

###### get\_semantic\_parser\_schema

```
get_semantic_parser_schema()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 133 134 135 136 137 138 139 140 ``` | ``` def get_semantic_parser_schema(cls):     parameters = []     if hasattr(cls, "predicate") and (cls.predicate == "" or cls.predicate is True):         for field in get_genie_fields_from_ws(cls):             if not field.internal:                 parameters.append(field.schema(value=False))      return f"{cls.__name__}({', '.join([repr(param) for param in parameters])})" ``` |

#### GenieField

A class representing a field in a Genie worksheet.

This class handles field definitions, validation, and value management for
worksheet fields. It supports various field types, validation rules, and
action triggers.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `slottype` | `str` | The type of the field. |
| `name` | `str` | The field name. |
| `question` | `str` | Question to ask when field needs filling. |
| `description` | `str` | Field description for LLM understanding. |
| `predicate` | `str` | Condition for field relevance. |
| `ask` | `bool` | Whether to ask user for this field. |
| `optional` | `bool` | Whether field is optional. |
| `actions` |  | Actions to perform when field is filled. |
| `requires_confirmation` | `bool` | Whether field needs confirmation. |
| `internal` | `bool` | Whether field is system-managed. |
| `primary_key` | `bool` | Whether field is a primary key. |
| `validation` | `str` | Validation criteria. |
| `parent` |  | Parent worksheet. |
| `bot` |  | Associated bot instance. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 ``` | ``` class GenieField:     """A class representing a field in a Genie worksheet.      This class handles field definitions, validation, and value management for     worksheet fields. It supports various field types, validation rules, and     action triggers.      Attributes:         slottype (str): The type of the field.         name (str): The field name.         question (str): Question to ask when field needs filling.         description (str): Field description for LLM understanding.         predicate (str): Condition for field relevance.         ask (bool): Whether to ask user for this field.         optional (bool): Whether field is optional.         actions: Actions to perform when field is filled.         requires_confirmation (bool): Whether field needs confirmation.         internal (bool): Whether field is system-managed.         primary_key (bool): Whether field is a primary key.         validation (str): Validation criteria.         parent: Parent worksheet.         bot: Associated bot instance.     """      def __init__(         self,         # The type of the slot, e.g., str, int, etc.         slottype: str,         # The name of the field (variable name)         name: str,         # The question to ask the user if the field is not filled         question: str = "",         # A description of the field. This is provided to the LLM for better understanding.         description: str = "",         # A predicate to determine if the field should be filled         predicate: str = "",         # Whether to ask the user for this field         ask: bool = True,         # Whether this field is optional         optional: bool = False,         # Any actions to perform when this field is filled         actions=None,         # The initial value of the field         value=None,         # Whether this field requires confirmation         requires_confirmation: bool = False,         # Whether this field is internal (not shown to the user and filled by the system)         internal: bool = False,         # Whether this field is a primary key. Used for database Worksheets.         primary_key: bool = False,         # Whether this field has been confirmed by the user         confirmed: bool = False,         # Any validation criteria for this field         validation: str | None = None,         # The parent worksheet         parent=None,         # The bot instance (GenieRuntime)         bot=None,         # Whether an action has been performed for this field         action_performed=False,         **kwargs,     ):         self.predicate = predicate         self.slottype = slottype         self.name = name         self.question = question         self.ask = ask         self.optional = optional         if self.ask is False:             self.optional = True         self.actions = actions         self.requires_confirmation = requires_confirmation         self.internal = internal         self.description = description         self.primary_key = primary_key         self.validation = validation         self.parent = parent         self.bot = bot          self.action_performed = action_performed         self._value = self.init_value(value)         self._confirmed = confirmed      def __deepcopy__(self, memo):         return GenieField(             slottype=deepcopy(self.slottype, memo),             name=deepcopy(self.name, memo),             question=deepcopy(self.question, memo),             description=deepcopy(self.description, memo),             predicate=deepcopy(self.predicate, memo),             ask=deepcopy(self.ask, memo),             optional=deepcopy(self.optional, memo),             actions=deepcopy(self.actions, memo),             value=deepcopy(self.value, memo),             requires_confirmation=deepcopy(self.requires_confirmation, memo),             internal=deepcopy(self.internal, memo),             primary_key=deepcopy(self.primary_key, memo),             confirmed=deepcopy(self.confirmed, memo),             validation=deepcopy(self.validation, memo),             action_performed=deepcopy(self.action_performed, memo),             parent=self.parent,             bot=self.bot,         )      def perform_action(self, bot: GenieRuntime, local_context: GenieContext):         """Perform the action associated with this field if it hasn't been performed yet.          Args:             bot (GenieRuntime): The bot instance.             local_context (GenieContext): The local context for the action.          Returns:             list: A list of actions performed.         """         if self.action_performed:             return []         logger.info(f"Peforming action for {self.name}: {self.actions.action}")         acts = []          # If there are no actions, return an empty list         if self.actions is None or len(self.actions) == 0:             return acts          # Perform the action         acts = self.actions.perform(self, bot, local_context)         self.action_performed = True          return acts      def __repr__(self) -> str:         return self.schema(value=True)      def schema(self, value=True):         """Generate a schema representation of the field.          Args:             value (bool, optional): Whether to include the value in the schema. Defaults to True.          Returns:             str: The schema representation.         """         # Getting the type of sources_type as a string         if isinstance(self.slottype, str) and self.slottype == "confirm":             slottype = "bool"         elif self.slottype.__name__ in ["List", "Dict"]:             slottype = self.slottype.__name__ + "["             if isinstance(self.slottype.__args__[0], str):                 slottype += self.slottype.__args__[0]             else:                 slottype += self.slottype.__args__[0].__name__             slottype += "]"         # Special case for enums         elif inspect.isclass(self.slottype) and issubclass(self.slottype, Enum):             options = ", ".join([repr(e.name) for e in self.slottype])             slottype = "Enum[" + options + "]"         else:             slottype = self.slottype.__name__          if value:             if self.value is None:                 val = "None"             elif self.value == "":                 val = '""'             else:                 val = self.value             return f"{self.name}: {slottype} = {repr(val)}"         else:             return f"{self.name}: {slottype}"      def schema_without_type(self, no_none=False):         """Generate a schema representation of the field without type information.          Args:             no_none (bool, optional): Whether to exclude None values. Defaults to False.          Returns:             str: The schema representation without type.         """         if self.value is None:             val = None         elif self.value == "":             val = '""'         else:             if isinstance(self.value, str):                 val = f"{repr(self.value)}"             else:                 val = self.value          if no_none and val == "None":             return          return f"{self.name} = {repr(val)}"      @property     def confirmed(self):         if hasattr(self, "_value") and isinstance(self._value, GenieValue):             return self._value.confirmed         return self._confirmed      @confirmed.setter     def confirmed(self, confirmed: bool):         self._confirmed = confirmed      @property     def value(self):         if isinstance(self._value, GenieValue):             return self._value.value         return self._value      @value.setter     def value(self, value):         self.action_performed = False         self._value = self.init_value(value)      def init_value(self, value: Any):         """Initialize a field value with proper validation and wrapping.          Args:             value (Any): The value to initialize.          Returns:             GenieValue: The initialized value, or None if validation fails.         """          def previous_action_contains_confirm():             """Only allow confirmation if the previous action was a confirmation action."""             if self.bot.dlg_history is not None and len(self.bot.dlg_history):                 if self.bot.dlg_history[-1].system_action is not None:                     for act in self.bot.dlg_history[-1].system_action.actions:                         if isinstance(act, AskAgentAct):                             if act.field.slottype == "confirm":                                 return True             return False          # TODO: If the value is set by the user for internal field, then do not assign.         # if done by the system, then assign.         if value == "" or value is None:             value = None         else:             if self.slottype == "confirm":                 prev_confirm = previous_action_contains_confirm()                 if not prev_confirm:                     return              valid = True             if self.validation:                 # Use LLM to check if the value is valid based on the validation rule                 matches_criteria, reason = validation_check(                     self.name, value, self.validation                 )                 if not matches_criteria:                     # If the validation fails, use the original value, log the error and set valid to False                     if isinstance(value, GenieValue):                         value = value.value                     self.parent.bot.context.agent_acts.add(                         ReportAgentAct(                             query=f"{self.name}={value}",                             message=f"Invalid value for {self.name}: {value} - {reason}",                         )                     )                     valid = False              if valid:                 # If the value is valid, create a GenieValue instance                 if isinstance(value, GenieValue):                     return value                 else:                     return GenieValue(value)      def __eq__(self, other):         # For equality check, we compare the name and value of the fields         if isinstance(other, GenieField):             if self.name == other.name and self.value == other.value:                 return True         return False ``` |

##### Attributes

###### predicate `instance-attribute`

```
predicate = predicate
```

###### slottype `instance-attribute`

```
slottype = slottype
```

###### name `instance-attribute`

```
name = name
```

###### question `instance-attribute`

```
question = question
```

###### ask `instance-attribute`

```
ask = ask
```

###### optional `instance-attribute`

```
optional = optional
```

###### actions `instance-attribute`

```
actions = actions
```

###### requires\_confirmation `instance-attribute`

```
requires_confirmation = requires_confirmation
```

###### internal `instance-attribute`

```
internal = internal
```

###### description `instance-attribute`

```
description = description
```

###### primary\_key `instance-attribute`

```
primary_key = primary_key
```

###### validation `instance-attribute`

```
validation = validation
```

###### parent `instance-attribute`

```
parent = parent
```

###### bot `instance-attribute`

```
bot = bot
```

###### action\_performed `instance-attribute`

```
action_performed = action_performed
```

###### \_value `instance-attribute`

```
_value = init_value(value)
```

###### \_confirmed `instance-attribute`

```
_confirmed = confirmed
```

###### confirmed `property` `writable`

```
confirmed
```

###### value `property` `writable`

```
value
```

##### Functions

###### \_\_init\_\_

```
__init__(slottype: str, name: str, question: str = '', description: str = '', predicate: str = '', ask: bool = True, optional: bool = False, actions=None, value=None, requires_confirmation: bool = False, internal: bool = False, primary_key: bool = False, confirmed: bool = False, validation: str | None = None, parent=None, bot=None, action_performed=False, **kwargs)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 ``` | ``` def __init__(     self,     # The type of the slot, e.g., str, int, etc.     slottype: str,     # The name of the field (variable name)     name: str,     # The question to ask the user if the field is not filled     question: str = "",     # A description of the field. This is provided to the LLM for better understanding.     description: str = "",     # A predicate to determine if the field should be filled     predicate: str = "",     # Whether to ask the user for this field     ask: bool = True,     # Whether this field is optional     optional: bool = False,     # Any actions to perform when this field is filled     actions=None,     # The initial value of the field     value=None,     # Whether this field requires confirmation     requires_confirmation: bool = False,     # Whether this field is internal (not shown to the user and filled by the system)     internal: bool = False,     # Whether this field is a primary key. Used for database Worksheets.     primary_key: bool = False,     # Whether this field has been confirmed by the user     confirmed: bool = False,     # Any validation criteria for this field     validation: str | None = None,     # The parent worksheet     parent=None,     # The bot instance (GenieRuntime)     bot=None,     # Whether an action has been performed for this field     action_performed=False,     **kwargs, ):     self.predicate = predicate     self.slottype = slottype     self.name = name     self.question = question     self.ask = ask     self.optional = optional     if self.ask is False:         self.optional = True     self.actions = actions     self.requires_confirmation = requires_confirmation     self.internal = internal     self.description = description     self.primary_key = primary_key     self.validation = validation     self.parent = parent     self.bot = bot      self.action_performed = action_performed     self._value = self.init_value(value)     self._confirmed = confirmed ``` |

###### \_\_deepcopy\_\_

```
__deepcopy__(memo)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 ``` | ``` def __deepcopy__(self, memo):     return GenieField(         slottype=deepcopy(self.slottype, memo),         name=deepcopy(self.name, memo),         question=deepcopy(self.question, memo),         description=deepcopy(self.description, memo),         predicate=deepcopy(self.predicate, memo),         ask=deepcopy(self.ask, memo),         optional=deepcopy(self.optional, memo),         actions=deepcopy(self.actions, memo),         value=deepcopy(self.value, memo),         requires_confirmation=deepcopy(self.requires_confirmation, memo),         internal=deepcopy(self.internal, memo),         primary_key=deepcopy(self.primary_key, memo),         confirmed=deepcopy(self.confirmed, memo),         validation=deepcopy(self.validation, memo),         action_performed=deepcopy(self.action_performed, memo),         parent=self.parent,         bot=self.bot,     ) ``` |

###### perform\_action

```
perform_action(bot: GenieRuntime, local_context: GenieContext)
```

Perform the action associated with this field if it hasn't been performed yet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for the action. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `list` |  | A list of actions performed. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 ``` | ``` def perform_action(self, bot: GenieRuntime, local_context: GenieContext):     """Perform the action associated with this field if it hasn't been performed yet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for the action.      Returns:         list: A list of actions performed.     """     if self.action_performed:         return []     logger.info(f"Peforming action for {self.name}: {self.actions.action}")     acts = []      # If there are no actions, return an empty list     if self.actions is None or len(self.actions) == 0:         return acts      # Perform the action     acts = self.actions.perform(self, bot, local_context)     self.action_performed = True      return acts ``` |

###### \_\_repr\_\_

```
__repr__() -> str
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 309 310 ``` | ``` def __repr__(self) -> str:     return self.schema(value=True) ``` |

###### schema

```
schema(value=True)
```

Generate a schema representation of the field.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `bool` | Whether to include the value in the schema. Defaults to True. | `True` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | The schema representation. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 ``` | ``` def schema(self, value=True):     """Generate a schema representation of the field.      Args:         value (bool, optional): Whether to include the value in the schema. Defaults to True.      Returns:         str: The schema representation.     """     # Getting the type of sources_type as a string     if isinstance(self.slottype, str) and self.slottype == "confirm":         slottype = "bool"     elif self.slottype.__name__ in ["List", "Dict"]:         slottype = self.slottype.__name__ + "["         if isinstance(self.slottype.__args__[0], str):             slottype += self.slottype.__args__[0]         else:             slottype += self.slottype.__args__[0].__name__         slottype += "]"     # Special case for enums     elif inspect.isclass(self.slottype) and issubclass(self.slottype, Enum):         options = ", ".join([repr(e.name) for e in self.slottype])         slottype = "Enum[" + options + "]"     else:         slottype = self.slottype.__name__      if value:         if self.value is None:             val = "None"         elif self.value == "":             val = '""'         else:             val = self.value         return f"{self.name}: {slottype} = {repr(val)}"     else:         return f"{self.name}: {slottype}" ``` |

###### schema\_without\_type

```
schema_without_type(no_none=False)
```

Generate a schema representation of the field without type information.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `no_none` | `bool` | Whether to exclude None values. Defaults to False. | `False` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | The schema representation without type. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 ``` | ``` def schema_without_type(self, no_none=False):     """Generate a schema representation of the field without type information.      Args:         no_none (bool, optional): Whether to exclude None values. Defaults to False.      Returns:         str: The schema representation without type.     """     if self.value is None:         val = None     elif self.value == "":         val = '""'     else:         if isinstance(self.value, str):             val = f"{repr(self.value)}"         else:             val = self.value      if no_none and val == "None":         return      return f"{self.name} = {repr(val)}" ``` |

###### init\_value

```
init_value(value: Any)
```

Initialize a field value with proper validation and wrapping.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `Any` | The value to initialize. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `GenieValue` |  | The initialized value, or None if validation fails. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 ``` | ``` def init_value(self, value: Any):     """Initialize a field value with proper validation and wrapping.      Args:         value (Any): The value to initialize.      Returns:         GenieValue: The initialized value, or None if validation fails.     """      def previous_action_contains_confirm():         """Only allow confirmation if the previous action was a confirmation action."""         if self.bot.dlg_history is not None and len(self.bot.dlg_history):             if self.bot.dlg_history[-1].system_action is not None:                 for act in self.bot.dlg_history[-1].system_action.actions:                     if isinstance(act, AskAgentAct):                         if act.field.slottype == "confirm":                             return True         return False      # TODO: If the value is set by the user for internal field, then do not assign.     # if done by the system, then assign.     if value == "" or value is None:         value = None     else:         if self.slottype == "confirm":             prev_confirm = previous_action_contains_confirm()             if not prev_confirm:                 return          valid = True         if self.validation:             # Use LLM to check if the value is valid based on the validation rule             matches_criteria, reason = validation_check(                 self.name, value, self.validation             )             if not matches_criteria:                 # If the validation fails, use the original value, log the error and set valid to False                 if isinstance(value, GenieValue):                     value = value.value                 self.parent.bot.context.agent_acts.add(                     ReportAgentAct(                         query=f"{self.name}={value}",                         message=f"Invalid value for {self.name}: {value} - {reason}",                     )                 )                 valid = False          if valid:             # If the value is valid, create a GenieValue instance             if isinstance(value, GenieValue):                 return value             else:                 return GenieValue(value) ``` |

###### \_\_eq\_\_

```
__eq__(other)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 449 450 451 452 453 454 ``` | ``` def __eq__(self, other):     # For equality check, we compare the name and value of the fields     if isinstance(other, GenieField):         if self.name == other.name and self.value == other.value:             return True     return False ``` |

#### GenieWorksheet

Base class for Genie worksheets.

This class provides the foundation for defining worksheets with fields,
actions, and state management. It handles initialization, field management,
and action execution.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `action_performed` | `bool` | Whether worksheet actions have been executed. |
| `result` |  | The result of worksheet execution. |
| `random_id` | `int` | Unique identifier for the worksheet instance. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 703 704 705 706 707 708 709 710 ``` | ``` class GenieWorksheet(metaclass=GenieREPR):     """Base class for Genie worksheets.      This class provides the foundation for defining worksheets with fields,     actions, and state management. It handles initialization, field management,     and action execution.      Attributes:         action_performed (bool): Whether worksheet actions have been executed.         result: The result of worksheet execution.         random_id (int): Unique identifier for the worksheet instance.     """      def __init__(self, **kwargs):         self.action_performed = False         self.result = None         self.random_id = 0          # Since the user doesn't initialize the fields, we need to do it for them         # first, we go over all the GenieFields in the class         # then, we create a params dict with all the fields in the GenieField         # finally, we check if the user has passed in a value for any GenieField         # if they have, we set the value of the GenieField to the value passed in         # and then we set the attribute of the class to the GenieField         for attr_name, attr_value in self.__class__.__dict__.items():             if isinstance(attr_value, GenieField):                 params = {                     field: getattr(attr_value, field)                     for field in dir(attr_value)                     if not field.startswith("__")                 }                 # if the user has passed in a value for the GenieField, set it                 # eg. Book(booking_id=125)                 # then the user has passed in a value for booking_id                 # attr_name is all the GenieFields in the class                 # kwargs is all the values the user has passed in (like booking_id=125)                 if attr_name in kwargs:                     params["value"] = kwargs[attr_name]                     if params["value"] == "":                         params["value"] = None                  if "optional" in params:                     if not params["optional"] and params["value"] == "NA":                         params["value"] = None                  setattr(self, attr_name, GenieField(**params))      def perform_action(self, bot: GenieRuntime, local_context: GenieContext):         """Perform the action associated with this worksheet if it hasn't been performed yet.          Args:             bot (GenieRuntime): The bot instance.             local_context (GenieContext): The local context for the action.          Returns:             list: A list of actions performed.         """          if self.action_performed:             return []         acts = []          if self.actions is None or len(self.actions) == 0:             return acts          acts = self.actions.perform(self, bot, local_context)         self.action_performed = True          return acts      def is_complete(self, bot: GenieRuntime, context: GenieContext) -> bool:         """Check if the worksheet is complete by evaluating all fields.          Args:             bot (GenieRuntime): The bot instance.             context (GenieContext): The context for evaluation.          Returns:             bool: True if the worksheet is complete, False otherwise.         """          for field in get_genie_fields_from_ws(self):             if eval_predicates(field.predicate, self, bot, context):                 if isinstance(field.value, GenieWorksheet):                     if not field.value.is_complete(bot, context):                         return False                 if (field.value is None or field.value == "") and not field.optional:                     return False                  if field.requires_confirmation and not field.confirmed:                     return False         return True      def __repr__(self):         parameters = []         for field in get_genie_fields_from_ws(self):             if isinstance(field, GenieField):                 parameters.append(field)          return f"{self.__class__.__name__}({', '.join([repr(param) for param in parameters])})"      def schema_without_type(self, context: GenieContext) -> str:         """Generate a schema representation of the worksheet without type information.          Args:             context (GenieContext): The context for the worksheet.          Returns:             str: The schema representation without type.         """         parameters = []         for field in get_genie_fields_from_ws(self):             if field.value is None:                 continue             if isinstance(field.value, str):                 if field.value == "":                     continue                 if field.confirmed:                     parameters.append(f"{field.name} = confirmed({repr(field.value)})")                 else:                     parameters.append(f"{field.name} = {repr(field.value)}")             elif isinstance(field._value, GenieResult):                 if isinstance(field.value, list):                     parent_var_name = None                     indices = []                      result_strings = []                     for val in field.value:                         if isinstance(val, GenieType):                             var_name, idx = find_list_variable(val, context)                             if var_name is None and idx is None:                                 result_strings.append(val)                             else:                                 if (                                     parent_var_name is not None                                     and parent_var_name != var_name                                 ):                                     logger.error(                                         "Cannot handle multiple list variables in the same answer"                                     )                                 parent_var_name = var_name  # Ignoring any potential multiple list variables                                  indices.append(idx)                         else:                             result_strings.append(val)                      if parent_var_name:                         indices_str = []                         for idx in indices:                             indices_str.append(f"{parent_var_name}[{idx}]")                          result_strings = "[" + ", ".join(indices_str) + "]"                 if len(result_strings):                     parameters.append(f"{field.name} = {str(result_strings)}")                 else:                     # TODO: Instead of getting the var_name from paren, we should search and find the same type of answer from the context                     parameters.append(f"{field.name} = {repr(field.value)}")             elif isinstance(field.value, GenieType):                 # This should be straight forward, same as the one above                 var_name, idx = find_list_variable(field.value, context)                 if var_name is None and idx is None:                     if field.confirmed:                         parameters.append(                             f"{field.name} = confirmed({repr(field.value)})"                         )                     else:                         parameters.append(f"{field.name} = {repr(field.value)}")                 else:                     if field.confirmed:                         parameters.append(                             f"{field.name} = confirmed({var_name}[{idx}])"                         )                     else:                         parameters.append(f"{field.name} = {var_name}[{idx}]")             else:                 var_name = get_variable_name(field.value, context)                  if isinstance(var_name, str):                     if field.confirmed:                         parameters.append(f"{field.name} = confirmed({repr(var_name)})")                     else:                         parameters.append(f"{field.name} = {var_name}")                 else:                     val = field.schema_without_type(no_none=True)                     if val:                         parameters.append(val)          return f"{self.__class__.__name__}({', '.join([str(param) for param in parameters])})"      def execute(self, bot: GenieRuntime, local_context: GenieContext):         """Execute the actions associated with this worksheet.          Args:             bot (GenieRuntime): The bot instance.             local_context (GenieContext): The local context for execution.         """         parameters = []         for f in get_genie_fields_from_ws(self):             parameters.append(f.name + "= " + "self." + f.name)          code = self.backend_api + "(" + ", ".join(parameters) + ")"         var_name = get_variable_name(self, local_context)         self.result = GenieResult(             execute_query(code, self, bot, local_context), self, var_name         )         self.bot.context.agent_acts.add(             ReportAgentAct(code, self.result, None, var_name + ".result")         )         self.action_performed = True         # local_context.context[         #     f"{generate_var_name(self.__class__.__name__)}_result"         # ] = self.result      # This might give me some troubles since we are already using .value at certain places.     # def __getattr__(self, name):     #     for field in get_genie_fields_from_ws(self):     #         if field.name == name:     #             return field.value      @classmethod     def new(cls, initialize_from_dict: dict):         return cls(**initialize_from_dict)      def __setattr__(self, name, value):         if hasattr(self, name):             attr = getattr(self, name)             if isinstance(attr, GenieField):                 self.action_performed = False                  # if the worksheet has a confirm type field which is set to true                 # upon update, we need to set it to false                 for field in get_genie_fields_from_ws(self):                     if field.slottype == "confirm" and field.value is True:                         field.value = False                  if isinstance(value, GenieField) and value.name == name:                     value.parent = self                     super().__setattr__(name, value)                     return                  if isinstance(value, GenieValue):                     attr.value = value                 else:                     attr.value = GenieValue(value)                 return         super().__setattr__(name, value)      def ask(self):         """This is a hack for when the user asks the system to ask a question from a different worksheet.          We increment the random_id to make sure that the ws is updated and the system with ask the question naturally         """         logger.info(f"Ask: {self}")         self.random_id += 1 ``` |

##### Attributes

###### action\_performed `instance-attribute`

```
action_performed = False
```

###### result `instance-attribute`

```
result = None
```

###### random\_id `instance-attribute`

```
random_id = 0
```

##### Functions

###### \_\_init\_\_

```
__init__(**kwargs)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 ``` | ``` def __init__(self, **kwargs):     self.action_performed = False     self.result = None     self.random_id = 0      # Since the user doesn't initialize the fields, we need to do it for them     # first, we go over all the GenieFields in the class     # then, we create a params dict with all the fields in the GenieField     # finally, we check if the user has passed in a value for any GenieField     # if they have, we set the value of the GenieField to the value passed in     # and then we set the attribute of the class to the GenieField     for attr_name, attr_value in self.__class__.__dict__.items():         if isinstance(attr_value, GenieField):             params = {                 field: getattr(attr_value, field)                 for field in dir(attr_value)                 if not field.startswith("__")             }             # if the user has passed in a value for the GenieField, set it             # eg. Book(booking_id=125)             # then the user has passed in a value for booking_id             # attr_name is all the GenieFields in the class             # kwargs is all the values the user has passed in (like booking_id=125)             if attr_name in kwargs:                 params["value"] = kwargs[attr_name]                 if params["value"] == "":                     params["value"] = None              if "optional" in params:                 if not params["optional"] and params["value"] == "NA":                     params["value"] = None              setattr(self, attr_name, GenieField(**params)) ``` |

###### perform\_action

```
perform_action(bot: GenieRuntime, local_context: GenieContext)
```

Perform the action associated with this worksheet if it hasn't been performed yet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for the action. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `list` |  | A list of actions performed. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 ``` | ``` def perform_action(self, bot: GenieRuntime, local_context: GenieContext):     """Perform the action associated with this worksheet if it hasn't been performed yet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for the action.      Returns:         list: A list of actions performed.     """      if self.action_performed:         return []     acts = []      if self.actions is None or len(self.actions) == 0:         return acts      acts = self.actions.perform(self, bot, local_context)     self.action_performed = True      return acts ``` |

###### is\_complete

```
is_complete(bot: GenieRuntime, context: GenieContext) -> bool
```

Check if the worksheet is complete by evaluating all fields.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `context` | `GenieContext` | The context for evaluation. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `bool` | `bool` | True if the worksheet is complete, False otherwise. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 ``` | ``` def is_complete(self, bot: GenieRuntime, context: GenieContext) -> bool:     """Check if the worksheet is complete by evaluating all fields.      Args:         bot (GenieRuntime): The bot instance.         context (GenieContext): The context for evaluation.      Returns:         bool: True if the worksheet is complete, False otherwise.     """      for field in get_genie_fields_from_ws(self):         if eval_predicates(field.predicate, self, bot, context):             if isinstance(field.value, GenieWorksheet):                 if not field.value.is_complete(bot, context):                     return False             if (field.value is None or field.value == "") and not field.optional:                 return False              if field.requires_confirmation and not field.confirmed:                 return False     return True ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 550 551 552 553 554 555 556 ``` | ``` def __repr__(self):     parameters = []     for field in get_genie_fields_from_ws(self):         if isinstance(field, GenieField):             parameters.append(field)      return f"{self.__class__.__name__}({', '.join([repr(param) for param in parameters])})" ``` |

###### schema\_without\_type

```
schema_without_type(context: GenieContext) -> str
```

Generate a schema representation of the worksheet without type information.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` | `GenieContext` | The context for the worksheet. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | The schema representation without type. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 ``` | ``` def schema_without_type(self, context: GenieContext) -> str:     """Generate a schema representation of the worksheet without type information.      Args:         context (GenieContext): The context for the worksheet.      Returns:         str: The schema representation without type.     """     parameters = []     for field in get_genie_fields_from_ws(self):         if field.value is None:             continue         if isinstance(field.value, str):             if field.value == "":                 continue             if field.confirmed:                 parameters.append(f"{field.name} = confirmed({repr(field.value)})")             else:                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field._value, GenieResult):             if isinstance(field.value, list):                 parent_var_name = None                 indices = []                  result_strings = []                 for val in field.value:                     if isinstance(val, GenieType):                         var_name, idx = find_list_variable(val, context)                         if var_name is None and idx is None:                             result_strings.append(val)                         else:                             if (                                 parent_var_name is not None                                 and parent_var_name != var_name                             ):                                 logger.error(                                     "Cannot handle multiple list variables in the same answer"                                 )                             parent_var_name = var_name  # Ignoring any potential multiple list variables                              indices.append(idx)                     else:                         result_strings.append(val)                  if parent_var_name:                     indices_str = []                     for idx in indices:                         indices_str.append(f"{parent_var_name}[{idx}]")                      result_strings = "[" + ", ".join(indices_str) + "]"             if len(result_strings):                 parameters.append(f"{field.name} = {str(result_strings)}")             else:                 # TODO: Instead of getting the var_name from paren, we should search and find the same type of answer from the context                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field.value, GenieType):             # This should be straight forward, same as the one above             var_name, idx = find_list_variable(field.value, context)             if var_name is None and idx is None:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({repr(field.value)})"                     )                 else:                     parameters.append(f"{field.name} = {repr(field.value)}")             else:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({var_name}[{idx}])"                     )                 else:                     parameters.append(f"{field.name} = {var_name}[{idx}]")         else:             var_name = get_variable_name(field.value, context)              if isinstance(var_name, str):                 if field.confirmed:                     parameters.append(f"{field.name} = confirmed({repr(var_name)})")                 else:                     parameters.append(f"{field.name} = {var_name}")             else:                 val = field.schema_without_type(no_none=True)                 if val:                     parameters.append(val)      return f"{self.__class__.__name__}({', '.join([str(param) for param in parameters])})" ``` |

###### execute

```
execute(bot: GenieRuntime, local_context: GenieContext)
```

Execute the actions associated with this worksheet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for execution. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 ``` | ``` def execute(self, bot: GenieRuntime, local_context: GenieContext):     """Execute the actions associated with this worksheet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for execution.     """     parameters = []     for f in get_genie_fields_from_ws(self):         parameters.append(f.name + "= " + "self." + f.name)      code = self.backend_api + "(" + ", ".join(parameters) + ")"     var_name = get_variable_name(self, local_context)     self.result = GenieResult(         execute_query(code, self, bot, local_context), self, var_name     )     self.bot.context.agent_acts.add(         ReportAgentAct(code, self.result, None, var_name + ".result")     )     self.action_performed = True ``` |

###### new `classmethod`

```
new(initialize_from_dict: dict)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 676 677 678 ``` | ``` @classmethod def new(cls, initialize_from_dict: dict):     return cls(**initialize_from_dict) ``` |

###### \_\_setattr\_\_

```
__setattr__(name, value)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 ``` | ``` def __setattr__(self, name, value):     if hasattr(self, name):         attr = getattr(self, name)         if isinstance(attr, GenieField):             self.action_performed = False              # if the worksheet has a confirm type field which is set to true             # upon update, we need to set it to false             for field in get_genie_fields_from_ws(self):                 if field.slottype == "confirm" and field.value is True:                     field.value = False              if isinstance(value, GenieField) and value.name == name:                 value.parent = self                 super().__setattr__(name, value)                 return              if isinstance(value, GenieValue):                 attr.value = value             else:                 attr.value = GenieValue(value)             return     super().__setattr__(name, value) ``` |

###### ask

```
ask()
```

This is a hack for when the user asks the system to ask a question from a different worksheet.

We increment the random\_id to make sure that the ws is updated and the system with ask the question naturally

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 704 705 706 707 708 709 710 ``` | ``` def ask(self):     """This is a hack for when the user asks the system to ask a question from a different worksheet.      We increment the random_id to make sure that the ws is updated and the system with ask the question naturally     """     logger.info(f"Ask: {self}")     self.random_id += 1 ``` |

#### GenieType

Bases: `GenieWorksheet`

Base class for Genie type definitions.

This class extends GenieWorksheet to provide type-specific functionality
and validation. It's used to define custom types in the Genie system.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `_parent` |  | Parent object reference. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 713 714 715 716 717 718 719 720 721 722 723 724 725 726 727 728 729 730 731 732 ``` | ``` class GenieType(GenieWorksheet):     """Base class for Genie type definitions.      This class extends GenieWorksheet to provide type-specific functionality     and validation. It's used to define custom types in the Genie system.      Attributes:         _parent: Parent object reference.     """      def __init__(self, **kwargs):         super().__init__(**kwargs)         self._parent = None      def is_complete(self, *args, **kwargs):         for field in get_genie_fields_from_ws(self):             if field.primary_key and field.value is not None:                 return True          return False ``` |

##### Attributes

###### action\_performed `instance-attribute`

```
action_performed = False
```

###### result `instance-attribute`

```
result = None
```

###### random\_id `instance-attribute`

```
random_id = 0
```

###### \_parent `instance-attribute`

```
_parent = None
```

##### Functions

###### perform\_action

```
perform_action(bot: GenieRuntime, local_context: GenieContext)
```

Perform the action associated with this worksheet if it hasn't been performed yet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for the action. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `list` |  | A list of actions performed. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 ``` | ``` def perform_action(self, bot: GenieRuntime, local_context: GenieContext):     """Perform the action associated with this worksheet if it hasn't been performed yet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for the action.      Returns:         list: A list of actions performed.     """      if self.action_performed:         return []     acts = []      if self.actions is None or len(self.actions) == 0:         return acts      acts = self.actions.perform(self, bot, local_context)     self.action_performed = True      return acts ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 550 551 552 553 554 555 556 ``` | ``` def __repr__(self):     parameters = []     for field in get_genie_fields_from_ws(self):         if isinstance(field, GenieField):             parameters.append(field)      return f"{self.__class__.__name__}({', '.join([repr(param) for param in parameters])})" ``` |

###### schema\_without\_type

```
schema_without_type(context: GenieContext) -> str
```

Generate a schema representation of the worksheet without type information.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` | `GenieContext` | The context for the worksheet. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | The schema representation without type. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 ``` | ``` def schema_without_type(self, context: GenieContext) -> str:     """Generate a schema representation of the worksheet without type information.      Args:         context (GenieContext): The context for the worksheet.      Returns:         str: The schema representation without type.     """     parameters = []     for field in get_genie_fields_from_ws(self):         if field.value is None:             continue         if isinstance(field.value, str):             if field.value == "":                 continue             if field.confirmed:                 parameters.append(f"{field.name} = confirmed({repr(field.value)})")             else:                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field._value, GenieResult):             if isinstance(field.value, list):                 parent_var_name = None                 indices = []                  result_strings = []                 for val in field.value:                     if isinstance(val, GenieType):                         var_name, idx = find_list_variable(val, context)                         if var_name is None and idx is None:                             result_strings.append(val)                         else:                             if (                                 parent_var_name is not None                                 and parent_var_name != var_name                             ):                                 logger.error(                                     "Cannot handle multiple list variables in the same answer"                                 )                             parent_var_name = var_name  # Ignoring any potential multiple list variables                              indices.append(idx)                     else:                         result_strings.append(val)                  if parent_var_name:                     indices_str = []                     for idx in indices:                         indices_str.append(f"{parent_var_name}[{idx}]")                      result_strings = "[" + ", ".join(indices_str) + "]"             if len(result_strings):                 parameters.append(f"{field.name} = {str(result_strings)}")             else:                 # TODO: Instead of getting the var_name from paren, we should search and find the same type of answer from the context                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field.value, GenieType):             # This should be straight forward, same as the one above             var_name, idx = find_list_variable(field.value, context)             if var_name is None and idx is None:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({repr(field.value)})"                     )                 else:                     parameters.append(f"{field.name} = {repr(field.value)}")             else:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({var_name}[{idx}])"                     )                 else:                     parameters.append(f"{field.name} = {var_name}[{idx}]")         else:             var_name = get_variable_name(field.value, context)              if isinstance(var_name, str):                 if field.confirmed:                     parameters.append(f"{field.name} = confirmed({repr(var_name)})")                 else:                     parameters.append(f"{field.name} = {var_name}")             else:                 val = field.schema_without_type(no_none=True)                 if val:                     parameters.append(val)      return f"{self.__class__.__name__}({', '.join([str(param) for param in parameters])})" ``` |

###### execute

```
execute(bot: GenieRuntime, local_context: GenieContext)
```

Execute the actions associated with this worksheet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for execution. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 ``` | ``` def execute(self, bot: GenieRuntime, local_context: GenieContext):     """Execute the actions associated with this worksheet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for execution.     """     parameters = []     for f in get_genie_fields_from_ws(self):         parameters.append(f.name + "= " + "self." + f.name)      code = self.backend_api + "(" + ", ".join(parameters) + ")"     var_name = get_variable_name(self, local_context)     self.result = GenieResult(         execute_query(code, self, bot, local_context), self, var_name     )     self.bot.context.agent_acts.add(         ReportAgentAct(code, self.result, None, var_name + ".result")     )     self.action_performed = True ``` |

###### new `classmethod`

```
new(initialize_from_dict: dict)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 676 677 678 ``` | ``` @classmethod def new(cls, initialize_from_dict: dict):     return cls(**initialize_from_dict) ``` |

###### \_\_setattr\_\_

```
__setattr__(name, value)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 ``` | ``` def __setattr__(self, name, value):     if hasattr(self, name):         attr = getattr(self, name)         if isinstance(attr, GenieField):             self.action_performed = False              # if the worksheet has a confirm type field which is set to true             # upon update, we need to set it to false             for field in get_genie_fields_from_ws(self):                 if field.slottype == "confirm" and field.value is True:                     field.value = False              if isinstance(value, GenieField) and value.name == name:                 value.parent = self                 super().__setattr__(name, value)                 return              if isinstance(value, GenieValue):                 attr.value = value             else:                 attr.value = GenieValue(value)             return     super().__setattr__(name, value) ``` |

###### ask

```
ask()
```

This is a hack for when the user asks the system to ask a question from a different worksheet.

We increment the random\_id to make sure that the ws is updated and the system with ask the question naturally

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 704 705 706 707 708 709 710 ``` | ``` def ask(self):     """This is a hack for when the user asks the system to ask a question from a different worksheet.      We increment the random_id to make sure that the ws is updated and the system with ask the question naturally     """     logger.info(f"Ask: {self}")     self.random_id += 1 ``` |

###### \_\_init\_\_

```
__init__(**kwargs)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 723 724 725 ``` | ``` def __init__(self, **kwargs):     super().__init__(**kwargs)     self._parent = None ``` |

###### is\_complete

```
is_complete(*args, **kwargs)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 727 728 729 730 731 732 ``` | ``` def is_complete(self, *args, **kwargs):     for field in get_genie_fields_from_ws(self):         if field.primary_key and field.value is not None:             return True      return False ``` |

#### GenieDB

Bases: `GenieWorksheet`

Base class for Genie database models.

This class extends GenieWorksheet to provide database-specific functionality
and schema management.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 735 736 737 738 739 740 ``` | ``` class GenieDB(GenieWorksheet):     """Base class for Genie database models.      This class extends GenieWorksheet to provide database-specific functionality     and schema management.     """ ``` |

##### Attributes

###### action\_performed `instance-attribute`

```
action_performed = False
```

###### result `instance-attribute`

```
result = None
```

###### random\_id `instance-attribute`

```
random_id = 0
```

##### Functions

###### \_\_init\_\_

```
__init__(**kwargs)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 ``` | ``` def __init__(self, **kwargs):     self.action_performed = False     self.result = None     self.random_id = 0      # Since the user doesn't initialize the fields, we need to do it for them     # first, we go over all the GenieFields in the class     # then, we create a params dict with all the fields in the GenieField     # finally, we check if the user has passed in a value for any GenieField     # if they have, we set the value of the GenieField to the value passed in     # and then we set the attribute of the class to the GenieField     for attr_name, attr_value in self.__class__.__dict__.items():         if isinstance(attr_value, GenieField):             params = {                 field: getattr(attr_value, field)                 for field in dir(attr_value)                 if not field.startswith("__")             }             # if the user has passed in a value for the GenieField, set it             # eg. Book(booking_id=125)             # then the user has passed in a value for booking_id             # attr_name is all the GenieFields in the class             # kwargs is all the values the user has passed in (like booking_id=125)             if attr_name in kwargs:                 params["value"] = kwargs[attr_name]                 if params["value"] == "":                     params["value"] = None              if "optional" in params:                 if not params["optional"] and params["value"] == "NA":                     params["value"] = None              setattr(self, attr_name, GenieField(**params)) ``` |

###### perform\_action

```
perform_action(bot: GenieRuntime, local_context: GenieContext)
```

Perform the action associated with this worksheet if it hasn't been performed yet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for the action. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `list` |  | A list of actions performed. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 ``` | ``` def perform_action(self, bot: GenieRuntime, local_context: GenieContext):     """Perform the action associated with this worksheet if it hasn't been performed yet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for the action.      Returns:         list: A list of actions performed.     """      if self.action_performed:         return []     acts = []      if self.actions is None or len(self.actions) == 0:         return acts      acts = self.actions.perform(self, bot, local_context)     self.action_performed = True      return acts ``` |

###### is\_complete

```
is_complete(bot: GenieRuntime, context: GenieContext) -> bool
```

Check if the worksheet is complete by evaluating all fields.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `context` | `GenieContext` | The context for evaluation. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `bool` | `bool` | True if the worksheet is complete, False otherwise. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 ``` | ``` def is_complete(self, bot: GenieRuntime, context: GenieContext) -> bool:     """Check if the worksheet is complete by evaluating all fields.      Args:         bot (GenieRuntime): The bot instance.         context (GenieContext): The context for evaluation.      Returns:         bool: True if the worksheet is complete, False otherwise.     """      for field in get_genie_fields_from_ws(self):         if eval_predicates(field.predicate, self, bot, context):             if isinstance(field.value, GenieWorksheet):                 if not field.value.is_complete(bot, context):                     return False             if (field.value is None or field.value == "") and not field.optional:                 return False              if field.requires_confirmation and not field.confirmed:                 return False     return True ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 550 551 552 553 554 555 556 ``` | ``` def __repr__(self):     parameters = []     for field in get_genie_fields_from_ws(self):         if isinstance(field, GenieField):             parameters.append(field)      return f"{self.__class__.__name__}({', '.join([repr(param) for param in parameters])})" ``` |

###### schema\_without\_type

```
schema_without_type(context: GenieContext) -> str
```

Generate a schema representation of the worksheet without type information.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` | `GenieContext` | The context for the worksheet. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | The schema representation without type. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 ``` | ``` def schema_without_type(self, context: GenieContext) -> str:     """Generate a schema representation of the worksheet without type information.      Args:         context (GenieContext): The context for the worksheet.      Returns:         str: The schema representation without type.     """     parameters = []     for field in get_genie_fields_from_ws(self):         if field.value is None:             continue         if isinstance(field.value, str):             if field.value == "":                 continue             if field.confirmed:                 parameters.append(f"{field.name} = confirmed({repr(field.value)})")             else:                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field._value, GenieResult):             if isinstance(field.value, list):                 parent_var_name = None                 indices = []                  result_strings = []                 for val in field.value:                     if isinstance(val, GenieType):                         var_name, idx = find_list_variable(val, context)                         if var_name is None and idx is None:                             result_strings.append(val)                         else:                             if (                                 parent_var_name is not None                                 and parent_var_name != var_name                             ):                                 logger.error(                                     "Cannot handle multiple list variables in the same answer"                                 )                             parent_var_name = var_name  # Ignoring any potential multiple list variables                              indices.append(idx)                     else:                         result_strings.append(val)                  if parent_var_name:                     indices_str = []                     for idx in indices:                         indices_str.append(f"{parent_var_name}[{idx}]")                      result_strings = "[" + ", ".join(indices_str) + "]"             if len(result_strings):                 parameters.append(f"{field.name} = {str(result_strings)}")             else:                 # TODO: Instead of getting the var_name from paren, we should search and find the same type of answer from the context                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field.value, GenieType):             # This should be straight forward, same as the one above             var_name, idx = find_list_variable(field.value, context)             if var_name is None and idx is None:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({repr(field.value)})"                     )                 else:                     parameters.append(f"{field.name} = {repr(field.value)}")             else:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({var_name}[{idx}])"                     )                 else:                     parameters.append(f"{field.name} = {var_name}[{idx}]")         else:             var_name = get_variable_name(field.value, context)              if isinstance(var_name, str):                 if field.confirmed:                     parameters.append(f"{field.name} = confirmed({repr(var_name)})")                 else:                     parameters.append(f"{field.name} = {var_name}")             else:                 val = field.schema_without_type(no_none=True)                 if val:                     parameters.append(val)      return f"{self.__class__.__name__}({', '.join([str(param) for param in parameters])})" ``` |

###### execute

```
execute(bot: GenieRuntime, local_context: GenieContext)
```

Execute the actions associated with this worksheet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for execution. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 ``` | ``` def execute(self, bot: GenieRuntime, local_context: GenieContext):     """Execute the actions associated with this worksheet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for execution.     """     parameters = []     for f in get_genie_fields_from_ws(self):         parameters.append(f.name + "= " + "self." + f.name)      code = self.backend_api + "(" + ", ".join(parameters) + ")"     var_name = get_variable_name(self, local_context)     self.result = GenieResult(         execute_query(code, self, bot, local_context), self, var_name     )     self.bot.context.agent_acts.add(         ReportAgentAct(code, self.result, None, var_name + ".result")     )     self.action_performed = True ``` |

###### new `classmethod`

```
new(initialize_from_dict: dict)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 676 677 678 ``` | ``` @classmethod def new(cls, initialize_from_dict: dict):     return cls(**initialize_from_dict) ``` |

###### \_\_setattr\_\_

```
__setattr__(name, value)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 ``` | ``` def __setattr__(self, name, value):     if hasattr(self, name):         attr = getattr(self, name)         if isinstance(attr, GenieField):             self.action_performed = False              # if the worksheet has a confirm type field which is set to true             # upon update, we need to set it to false             for field in get_genie_fields_from_ws(self):                 if field.slottype == "confirm" and field.value is True:                     field.value = False              if isinstance(value, GenieField) and value.name == name:                 value.parent = self                 super().__setattr__(name, value)                 return              if isinstance(value, GenieValue):                 attr.value = value             else:                 attr.value = GenieValue(value)             return     super().__setattr__(name, value) ``` |

###### ask

```
ask()
```

This is a hack for when the user asks the system to ask a question from a different worksheet.

We increment the random\_id to make sure that the ws is updated and the system with ask the question naturally

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 704 705 706 707 708 709 710 ``` | ``` def ask(self):     """This is a hack for when the user asks the system to ask a question from a different worksheet.      We increment the random_id to make sure that the ws is updated and the system with ask the question naturally     """     logger.info(f"Ask: {self}")     self.random_id += 1 ``` |

#### Answer

Bases: `GenieWorksheet`

Class representing an answer in the Genie system.

This class handles query execution, result management, and parameter tracking
for answers to user queries.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `query` | `GenieField` | The query to execute. |
| `actions` |  | Associated actions. |
| `result` |  | Query execution result. |
| `tables` |  | Related database tables. |
| `potential_outputs` |  | Possible output types. |
| `nl_query` |  | Natural language query. |
| `param_names` |  | Required parameter names. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 743 744 745 746 747 748 749 750 751 752 753 754 755 756 757 758 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773 774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791 792 793 794 795 796 797 798 799 800 801 802 803 804 805 806 807 808 809 810 811 812 813 814 815 816 817 818 819 820 821 822 823 824 825 826 827 828 829 830 831 832 833 834 835 836 837 838 839 840 841 842 843 844 845 846 847 848 849 850 851 852 853 854 855 856 857 858 859 860 861 862 863 864 865 866 867 868 869 870 871 872 873 874 875 876 877 878 879 880 881 882 883 884 885 886 887 888 889 890 891 892 893 894 895 896 897 898 899 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 ``` | ``` class Answer(GenieWorksheet):     """Class representing an answer in the Genie system.      This class handles query execution, result management, and parameter tracking     for answers to user queries.      Attributes:         query (GenieField): The query to execute.         actions: Associated actions.         result: Query execution result.         tables: Related database tables.         potential_outputs: Possible output types.         nl_query: Natural language query.         param_names: Required parameter names.     """      def __init__(self, query, required_params, tables, nl_query):         self.query = GenieField("str", "query", value=query)         self.actions = Action(">suql_runner(self.query.value, self.required_columns)")         self.result = None         self.tables = tables         self.potential_outputs = []         self.nl_query = nl_query         self.param_names = []         self.action_performed = False          for table in self.tables:             self.potential_outputs.extend(self.bot.context.context[table].outputs)          self.required_columns = [             field.name             for table in self.tables             for field in get_genie_fields_from_ws(self.bot.context.context[table])         ]          # Create required params and add them to ordered attributes         _ordered_attributes = ["query"]         if required_params is not None:             for db_name, params in required_params.items():                 for param in params:                     setattr(                         self,                         f"{db_name}_{param}",                         GenieField("str", f"{db_name}.{param}", value=None),                     )                     self.param_names.append(f"{db_name}_{param}")                     _ordered_attributes.append(f"{db_name}_{param}")          self._ordered_attributes = _ordered_attributes      def execute(self, bot: GenieRuntime, local_context: GenieContext):         """Execute the actions associated with this answer.          Args:             bot (GenieRuntime): The bot instance.             local_context (GenieContext): The local context for the execution.         """         if self.action_performed:             return         results = execute_query(self.actions.action, self, bot, local_context)         self.action_performed = True         if results is None:             results = []          # Get more information about the fields         ws, field_name, more_field_info_result = self.more_field_info_query(bot)         logger.info(f"More Field Info: {more_field_info_result}")         logger.info(f"Results: {results}")          # Earlier we had a mechanism to check if the user is asking to execute a query or asking for more information         # about the field. Hence we have output_idx.         # For now we are going to assume that the user is asking for the output of the query         output_idx = [1]          if len(output_idx):             output_idx = int(output_idx[0])             if output_idx == 1:                 # Check if the output type is in the results                 output = self.output_in_result(results)                 var_name = get_variable_name(self, local_context)                 self.result = GenieResult(output, self, var_name)                  # Report the agent act                 self.bot.context.agent_acts.add(                     ReportAgentAct(                         self.query, self.result, var_name, var_name + ".result"                     )                 )                 for i, _output in enumerate(output):                     if isinstance(_output, GenieWorksheet):                         # add the output to the local context                         local_context.set(                             f"{camel_to_snake(_output.__class__.__name__)}", _output                         )             elif output_idx == 2:                 # We don't use this for now but we can use it to ask for more information                 var_name = get_variable_name(self, local_context)                 self.result = GenieResult(more_field_info_result, self, var_name)                 self.bot.context.agent_acts.add(                     ReportAgentAct(                         f"AskClarificationQuestion({ws.__class__.__name__}, {field_name.name})",                         self.result,                         message_var_name=var_name + ".result",                     )                 )          # for i, _output in enumerate(output):         #     local_context.context[f"__{var_name}_result_{i}"] = _output      def more_field_info_query(self, bot: GenieRuntime):         if bot.dlg_history is None or len(bot.dlg_history) == 0:             return None, None, None         if bot.dlg_history[-1].system_action is None:             return None, None, None         acts = bot.dlg_history[-1].system_action.actions         for act in acts:             if isinstance(act, AskAgentAct):                 more_field_info = generate_clarification(act.ws, act.field.name)                 if more_field_info:                     return act.ws, act.field, more_field_info          return None, None, None      def output_in_result(self, results: list):         """Check if the output type is in the results."""         if len(self.potential_outputs):             output_results = []             for result in results:                 for output_type in self.potential_outputs:                     found_primary_key = False                     for field in get_genie_fields_from_ws(output_type):                         if field.primary_key and field.name in result:                             output_results.append(output_type(**result))                             found_primary_key = True                             break                     if not found_primary_key:                         output_results.append(result)              return output_results         return results      def update(self, query, unfilled_params, tables, query_str):         """Update the answer with new parameters and tables.          We are not using this method anymore, but we can keep it for reference."""         logger.error(f"Updating Answer: {query}, This has been deprecated")         self.query.value = query         for param in self.param_names:             del self.__dict__[param]             self._ordered_attributes.remove(param)         self.param_names = []         self.required_columns = [             field.name             for table in tables             for field in get_genie_fields_from_ws(self.bot.context.context[table])         ]         self.tables = tables         self.potential_outputs = []         for table in self.tables:             self.potential_outputs.extend(self.bot.context.context[table].outputs)          if unfilled_params is not None:             for db_name, params in unfilled_params.items():                 for param in params:                     setattr(                         self,                         f"{db_name}_{param}",                         GenieField("str", f"{db_name}.{param}", value=None),                     )                     self.param_names.append(f"{db_name}_{param}")                     self._ordered_attributes.append(f"{db_name}_{param}")          self.nl_query = query_str ``` |

##### Attributes

###### random\_id `instance-attribute`

```
random_id = 0
```

###### query `instance-attribute`

```
query = GenieField('str', 'query', value=query)
```

###### actions `instance-attribute`

```
actions = Action('>suql_runner(self.query.value, self.required_columns)')
```

###### result `instance-attribute`

```
result = None
```

###### tables `instance-attribute`

```
tables = tables
```

###### potential\_outputs `instance-attribute`

```
potential_outputs = []
```

###### nl\_query `instance-attribute`

```
nl_query = nl_query
```

###### param\_names `instance-attribute`

```
param_names = []
```

###### action\_performed `instance-attribute`

```
action_performed = False
```

###### required\_columns `instance-attribute`

```
required_columns = [name for table in tables for field in get_genie_fields_from_ws(context[table])]
```

###### \_ordered\_attributes `instance-attribute`

```
_ordered_attributes = _ordered_attributes
```

##### Functions

###### perform\_action

```
perform_action(bot: GenieRuntime, local_context: GenieContext)
```

Perform the action associated with this worksheet if it hasn't been performed yet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for the action. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `list` |  | A list of actions performed. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 ``` | ``` def perform_action(self, bot: GenieRuntime, local_context: GenieContext):     """Perform the action associated with this worksheet if it hasn't been performed yet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for the action.      Returns:         list: A list of actions performed.     """      if self.action_performed:         return []     acts = []      if self.actions is None or len(self.actions) == 0:         return acts      acts = self.actions.perform(self, bot, local_context)     self.action_performed = True      return acts ``` |

###### is\_complete

```
is_complete(bot: GenieRuntime, context: GenieContext) -> bool
```

Check if the worksheet is complete by evaluating all fields.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `context` | `GenieContext` | The context for evaluation. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `bool` | `bool` | True if the worksheet is complete, False otherwise. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 ``` | ``` def is_complete(self, bot: GenieRuntime, context: GenieContext) -> bool:     """Check if the worksheet is complete by evaluating all fields.      Args:         bot (GenieRuntime): The bot instance.         context (GenieContext): The context for evaluation.      Returns:         bool: True if the worksheet is complete, False otherwise.     """      for field in get_genie_fields_from_ws(self):         if eval_predicates(field.predicate, self, bot, context):             if isinstance(field.value, GenieWorksheet):                 if not field.value.is_complete(bot, context):                     return False             if (field.value is None or field.value == "") and not field.optional:                 return False              if field.requires_confirmation and not field.confirmed:                 return False     return True ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 550 551 552 553 554 555 556 ``` | ``` def __repr__(self):     parameters = []     for field in get_genie_fields_from_ws(self):         if isinstance(field, GenieField):             parameters.append(field)      return f"{self.__class__.__name__}({', '.join([repr(param) for param in parameters])})" ``` |

###### schema\_without\_type

```
schema_without_type(context: GenieContext) -> str
```

Generate a schema representation of the worksheet without type information.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` | `GenieContext` | The context for the worksheet. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | The schema representation without type. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 ``` | ``` def schema_without_type(self, context: GenieContext) -> str:     """Generate a schema representation of the worksheet without type information.      Args:         context (GenieContext): The context for the worksheet.      Returns:         str: The schema representation without type.     """     parameters = []     for field in get_genie_fields_from_ws(self):         if field.value is None:             continue         if isinstance(field.value, str):             if field.value == "":                 continue             if field.confirmed:                 parameters.append(f"{field.name} = confirmed({repr(field.value)})")             else:                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field._value, GenieResult):             if isinstance(field.value, list):                 parent_var_name = None                 indices = []                  result_strings = []                 for val in field.value:                     if isinstance(val, GenieType):                         var_name, idx = find_list_variable(val, context)                         if var_name is None and idx is None:                             result_strings.append(val)                         else:                             if (                                 parent_var_name is not None                                 and parent_var_name != var_name                             ):                                 logger.error(                                     "Cannot handle multiple list variables in the same answer"                                 )                             parent_var_name = var_name  # Ignoring any potential multiple list variables                              indices.append(idx)                     else:                         result_strings.append(val)                  if parent_var_name:                     indices_str = []                     for idx in indices:                         indices_str.append(f"{parent_var_name}[{idx}]")                      result_strings = "[" + ", ".join(indices_str) + "]"             if len(result_strings):                 parameters.append(f"{field.name} = {str(result_strings)}")             else:                 # TODO: Instead of getting the var_name from paren, we should search and find the same type of answer from the context                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field.value, GenieType):             # This should be straight forward, same as the one above             var_name, idx = find_list_variable(field.value, context)             if var_name is None and idx is None:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({repr(field.value)})"                     )                 else:                     parameters.append(f"{field.name} = {repr(field.value)}")             else:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({var_name}[{idx}])"                     )                 else:                     parameters.append(f"{field.name} = {var_name}[{idx}]")         else:             var_name = get_variable_name(field.value, context)              if isinstance(var_name, str):                 if field.confirmed:                     parameters.append(f"{field.name} = confirmed({repr(var_name)})")                 else:                     parameters.append(f"{field.name} = {var_name}")             else:                 val = field.schema_without_type(no_none=True)                 if val:                     parameters.append(val)      return f"{self.__class__.__name__}({', '.join([str(param) for param in parameters])})" ``` |

###### new `classmethod`

```
new(initialize_from_dict: dict)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 676 677 678 ``` | ``` @classmethod def new(cls, initialize_from_dict: dict):     return cls(**initialize_from_dict) ``` |

###### \_\_setattr\_\_

```
__setattr__(name, value)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 ``` | ``` def __setattr__(self, name, value):     if hasattr(self, name):         attr = getattr(self, name)         if isinstance(attr, GenieField):             self.action_performed = False              # if the worksheet has a confirm type field which is set to true             # upon update, we need to set it to false             for field in get_genie_fields_from_ws(self):                 if field.slottype == "confirm" and field.value is True:                     field.value = False              if isinstance(value, GenieField) and value.name == name:                 value.parent = self                 super().__setattr__(name, value)                 return              if isinstance(value, GenieValue):                 attr.value = value             else:                 attr.value = GenieValue(value)             return     super().__setattr__(name, value) ``` |

###### ask

```
ask()
```

This is a hack for when the user asks the system to ask a question from a different worksheet.

We increment the random\_id to make sure that the ws is updated and the system with ask the question naturally

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 704 705 706 707 708 709 710 ``` | ``` def ask(self):     """This is a hack for when the user asks the system to ask a question from a different worksheet.      We increment the random_id to make sure that the ws is updated and the system with ask the question naturally     """     logger.info(f"Ask: {self}")     self.random_id += 1 ``` |

###### \_\_init\_\_

```
__init__(query, required_params, tables, nl_query)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773 774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791 ``` | ``` def __init__(self, query, required_params, tables, nl_query):     self.query = GenieField("str", "query", value=query)     self.actions = Action(">suql_runner(self.query.value, self.required_columns)")     self.result = None     self.tables = tables     self.potential_outputs = []     self.nl_query = nl_query     self.param_names = []     self.action_performed = False      for table in self.tables:         self.potential_outputs.extend(self.bot.context.context[table].outputs)      self.required_columns = [         field.name         for table in self.tables         for field in get_genie_fields_from_ws(self.bot.context.context[table])     ]      # Create required params and add them to ordered attributes     _ordered_attributes = ["query"]     if required_params is not None:         for db_name, params in required_params.items():             for param in params:                 setattr(                     self,                     f"{db_name}_{param}",                     GenieField("str", f"{db_name}.{param}", value=None),                 )                 self.param_names.append(f"{db_name}_{param}")                 _ordered_attributes.append(f"{db_name}_{param}")      self._ordered_attributes = _ordered_attributes ``` |

###### execute

```
execute(bot: GenieRuntime, local_context: GenieContext)
```

Execute the actions associated with this answer.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for the execution. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 793 794 795 796 797 798 799 800 801 802 803 804 805 806 807 808 809 810 811 812 813 814 815 816 817 818 819 820 821 822 823 824 825 826 827 828 829 830 831 832 833 834 835 836 837 838 839 840 841 842 843 844 845 846 847 ``` | ``` def execute(self, bot: GenieRuntime, local_context: GenieContext):     """Execute the actions associated with this answer.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for the execution.     """     if self.action_performed:         return     results = execute_query(self.actions.action, self, bot, local_context)     self.action_performed = True     if results is None:         results = []      # Get more information about the fields     ws, field_name, more_field_info_result = self.more_field_info_query(bot)     logger.info(f"More Field Info: {more_field_info_result}")     logger.info(f"Results: {results}")      # Earlier we had a mechanism to check if the user is asking to execute a query or asking for more information     # about the field. Hence we have output_idx.     # For now we are going to assume that the user is asking for the output of the query     output_idx = [1]      if len(output_idx):         output_idx = int(output_idx[0])         if output_idx == 1:             # Check if the output type is in the results             output = self.output_in_result(results)             var_name = get_variable_name(self, local_context)             self.result = GenieResult(output, self, var_name)              # Report the agent act             self.bot.context.agent_acts.add(                 ReportAgentAct(                     self.query, self.result, var_name, var_name + ".result"                 )             )             for i, _output in enumerate(output):                 if isinstance(_output, GenieWorksheet):                     # add the output to the local context                     local_context.set(                         f"{camel_to_snake(_output.__class__.__name__)}", _output                     )         elif output_idx == 2:             # We don't use this for now but we can use it to ask for more information             var_name = get_variable_name(self, local_context)             self.result = GenieResult(more_field_info_result, self, var_name)             self.bot.context.agent_acts.add(                 ReportAgentAct(                     f"AskClarificationQuestion({ws.__class__.__name__}, {field_name.name})",                     self.result,                     message_var_name=var_name + ".result",                 )             ) ``` |

###### more\_field\_info\_query

```
more_field_info_query(bot: GenieRuntime)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 852 853 854 855 856 857 858 859 860 861 862 863 864 ``` | ``` def more_field_info_query(self, bot: GenieRuntime):     if bot.dlg_history is None or len(bot.dlg_history) == 0:         return None, None, None     if bot.dlg_history[-1].system_action is None:         return None, None, None     acts = bot.dlg_history[-1].system_action.actions     for act in acts:         if isinstance(act, AskAgentAct):             more_field_info = generate_clarification(act.ws, act.field.name)             if more_field_info:                 return act.ws, act.field, more_field_info      return None, None, None ``` |

###### output\_in\_result

```
output_in_result(results: list)
```

Check if the output type is in the results.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 866 867 868 869 870 871 872 873 874 875 876 877 878 879 880 881 882 ``` | ``` def output_in_result(self, results: list):     """Check if the output type is in the results."""     if len(self.potential_outputs):         output_results = []         for result in results:             for output_type in self.potential_outputs:                 found_primary_key = False                 for field in get_genie_fields_from_ws(output_type):                     if field.primary_key and field.name in result:                         output_results.append(output_type(**result))                         found_primary_key = True                         break                 if not found_primary_key:                     output_results.append(result)          return output_results     return results ``` |

###### update

```
update(query, unfilled_params, tables, query_str)
```

Update the answer with new parameters and tables.

We are not using this method anymore, but we can keep it for reference.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 884 885 886 887 888 889 890 891 892 893 894 895 896 897 898 899 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 ``` | ``` def update(self, query, unfilled_params, tables, query_str):     """Update the answer with new parameters and tables.      We are not using this method anymore, but we can keep it for reference."""     logger.error(f"Updating Answer: {query}, This has been deprecated")     self.query.value = query     for param in self.param_names:         del self.__dict__[param]         self._ordered_attributes.remove(param)     self.param_names = []     self.required_columns = [         field.name         for table in tables         for field in get_genie_fields_from_ws(self.bot.context.context[table])     ]     self.tables = tables     self.potential_outputs = []     for table in self.tables:         self.potential_outputs.extend(self.bot.context.context[table].outputs)      if unfilled_params is not None:         for db_name, params in unfilled_params.items():             for param in params:                 setattr(                     self,                     f"{db_name}_{param}",                     GenieField("str", f"{db_name}.{param}", value=None),                 )                 self.param_names.append(f"{db_name}_{param}")                 self._ordered_attributes.append(f"{db_name}_{param}")      self.nl_query = query_str ``` |

#### MoreFieldInfo

Bases: `GenieWorksheet`

Class for managing additional field information requests.

This class handles requests for clarification or additional information
about specific fields.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `api_name` | `GenieField` | Name of the API. |
| `parameter_name` | `GenieField` | Name of the parameter. |
| `actions` |  | Associated actions. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 918 919 920 921 922 923 924 925 926 927 928 929 930 931 932 933 934 935 936 ``` | ``` class MoreFieldInfo(GenieWorksheet):     """Class for managing additional field information requests.      This class handles requests for clarification or additional information     about specific fields.      Attributes:         api_name (GenieField): Name of the API.         parameter_name (GenieField): Name of the parameter.         actions: Associated actions.     """      def __init__(self, api_name, parameter_name):         self.api_name = GenieField("str", "api_name", value=api_name)         self.parameter_name = GenieField("str", "parameter_name", value=parameter_name)         self.actions = Action(             ">answer_clarification_question(self.api_name, self.parameter_name)"         )         self.action_performed = False ``` |

##### Attributes

###### result `instance-attribute`

```
result = None
```

###### random\_id `instance-attribute`

```
random_id = 0
```

###### api\_name `instance-attribute`

```
api_name = GenieField('str', 'api_name', value=api_name)
```

###### parameter\_name `instance-attribute`

```
parameter_name = GenieField('str', 'parameter_name', value=parameter_name)
```

###### actions `instance-attribute`

```
actions = Action('>answer_clarification_question(self.api_name, self.parameter_name)')
```

###### action\_performed `instance-attribute`

```
action_performed = False
```

##### Functions

###### perform\_action

```
perform_action(bot: GenieRuntime, local_context: GenieContext)
```

Perform the action associated with this worksheet if it hasn't been performed yet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for the action. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `list` |  | A list of actions performed. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 ``` | ``` def perform_action(self, bot: GenieRuntime, local_context: GenieContext):     """Perform the action associated with this worksheet if it hasn't been performed yet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for the action.      Returns:         list: A list of actions performed.     """      if self.action_performed:         return []     acts = []      if self.actions is None or len(self.actions) == 0:         return acts      acts = self.actions.perform(self, bot, local_context)     self.action_performed = True      return acts ``` |

###### is\_complete

```
is_complete(bot: GenieRuntime, context: GenieContext) -> bool
```

Check if the worksheet is complete by evaluating all fields.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `context` | `GenieContext` | The context for evaluation. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `bool` | `bool` | True if the worksheet is complete, False otherwise. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 ``` | ``` def is_complete(self, bot: GenieRuntime, context: GenieContext) -> bool:     """Check if the worksheet is complete by evaluating all fields.      Args:         bot (GenieRuntime): The bot instance.         context (GenieContext): The context for evaluation.      Returns:         bool: True if the worksheet is complete, False otherwise.     """      for field in get_genie_fields_from_ws(self):         if eval_predicates(field.predicate, self, bot, context):             if isinstance(field.value, GenieWorksheet):                 if not field.value.is_complete(bot, context):                     return False             if (field.value is None or field.value == "") and not field.optional:                 return False              if field.requires_confirmation and not field.confirmed:                 return False     return True ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 550 551 552 553 554 555 556 ``` | ``` def __repr__(self):     parameters = []     for field in get_genie_fields_from_ws(self):         if isinstance(field, GenieField):             parameters.append(field)      return f"{self.__class__.__name__}({', '.join([repr(param) for param in parameters])})" ``` |

###### schema\_without\_type

```
schema_without_type(context: GenieContext) -> str
```

Generate a schema representation of the worksheet without type information.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` | `GenieContext` | The context for the worksheet. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | The schema representation without type. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 ``` | ``` def schema_without_type(self, context: GenieContext) -> str:     """Generate a schema representation of the worksheet without type information.      Args:         context (GenieContext): The context for the worksheet.      Returns:         str: The schema representation without type.     """     parameters = []     for field in get_genie_fields_from_ws(self):         if field.value is None:             continue         if isinstance(field.value, str):             if field.value == "":                 continue             if field.confirmed:                 parameters.append(f"{field.name} = confirmed({repr(field.value)})")             else:                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field._value, GenieResult):             if isinstance(field.value, list):                 parent_var_name = None                 indices = []                  result_strings = []                 for val in field.value:                     if isinstance(val, GenieType):                         var_name, idx = find_list_variable(val, context)                         if var_name is None and idx is None:                             result_strings.append(val)                         else:                             if (                                 parent_var_name is not None                                 and parent_var_name != var_name                             ):                                 logger.error(                                     "Cannot handle multiple list variables in the same answer"                                 )                             parent_var_name = var_name  # Ignoring any potential multiple list variables                              indices.append(idx)                     else:                         result_strings.append(val)                  if parent_var_name:                     indices_str = []                     for idx in indices:                         indices_str.append(f"{parent_var_name}[{idx}]")                      result_strings = "[" + ", ".join(indices_str) + "]"             if len(result_strings):                 parameters.append(f"{field.name} = {str(result_strings)}")             else:                 # TODO: Instead of getting the var_name from paren, we should search and find the same type of answer from the context                 parameters.append(f"{field.name} = {repr(field.value)}")         elif isinstance(field.value, GenieType):             # This should be straight forward, same as the one above             var_name, idx = find_list_variable(field.value, context)             if var_name is None and idx is None:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({repr(field.value)})"                     )                 else:                     parameters.append(f"{field.name} = {repr(field.value)}")             else:                 if field.confirmed:                     parameters.append(                         f"{field.name} = confirmed({var_name}[{idx}])"                     )                 else:                     parameters.append(f"{field.name} = {var_name}[{idx}]")         else:             var_name = get_variable_name(field.value, context)              if isinstance(var_name, str):                 if field.confirmed:                     parameters.append(f"{field.name} = confirmed({repr(var_name)})")                 else:                     parameters.append(f"{field.name} = {var_name}")             else:                 val = field.schema_without_type(no_none=True)                 if val:                     parameters.append(val)      return f"{self.__class__.__name__}({', '.join([str(param) for param in parameters])})" ``` |

###### execute

```
execute(bot: GenieRuntime, local_context: GenieContext)
```

Execute the actions associated with this worksheet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context for execution. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 ``` | ``` def execute(self, bot: GenieRuntime, local_context: GenieContext):     """Execute the actions associated with this worksheet.      Args:         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context for execution.     """     parameters = []     for f in get_genie_fields_from_ws(self):         parameters.append(f.name + "= " + "self." + f.name)      code = self.backend_api + "(" + ", ".join(parameters) + ")"     var_name = get_variable_name(self, local_context)     self.result = GenieResult(         execute_query(code, self, bot, local_context), self, var_name     )     self.bot.context.agent_acts.add(         ReportAgentAct(code, self.result, None, var_name + ".result")     )     self.action_performed = True ``` |

###### new `classmethod`

```
new(initialize_from_dict: dict)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 676 677 678 ``` | ``` @classmethod def new(cls, initialize_from_dict: dict):     return cls(**initialize_from_dict) ``` |

###### \_\_setattr\_\_

```
__setattr__(name, value)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 ``` | ``` def __setattr__(self, name, value):     if hasattr(self, name):         attr = getattr(self, name)         if isinstance(attr, GenieField):             self.action_performed = False              # if the worksheet has a confirm type field which is set to true             # upon update, we need to set it to false             for field in get_genie_fields_from_ws(self):                 if field.slottype == "confirm" and field.value is True:                     field.value = False              if isinstance(value, GenieField) and value.name == name:                 value.parent = self                 super().__setattr__(name, value)                 return              if isinstance(value, GenieValue):                 attr.value = value             else:                 attr.value = GenieValue(value)             return     super().__setattr__(name, value) ``` |

###### ask

```
ask()
```

This is a hack for when the user asks the system to ask a question from a different worksheet.

We increment the random\_id to make sure that the ws is updated and the system with ask the question naturally

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 704 705 706 707 708 709 710 ``` | ``` def ask(self):     """This is a hack for when the user asks the system to ask a question from a different worksheet.      We increment the random_id to make sure that the ws is updated and the system with ask the question naturally     """     logger.info(f"Ask: {self}")     self.random_id += 1 ``` |

###### \_\_init\_\_

```
__init__(api_name, parameter_name)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 930 931 932 933 934 935 936 ``` | ``` def __init__(self, api_name, parameter_name):     self.api_name = GenieField("str", "api_name", value=api_name)     self.parameter_name = GenieField("str", "parameter_name", value=parameter_name)     self.actions = Action(         ">answer_clarification_question(self.api_name, self.parameter_name)"     )     self.action_performed = False ``` |

#### Action

Class for managing worksheet actions.

This class handles action definition, execution, and result management
for worksheet operations.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `action` |  | The action to perform. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 939 940 941 942 943 944 945 946 947 948 949 950 951 952 953 954 955 956 957 958 959 960 961 962 963 964 965 966 967 968 969 970 971 972 973 974 975 976 977 978 979 980 981 982 983 984 985 986 987 988 989 990 991 992 993 994 995 996 997 998 ``` | ``` class Action:     """Class for managing worksheet actions.      This class handles action definition, execution, and result management     for worksheet operations.      Attributes:         action: The action to perform.     """      def __init__(self, action):         self.action = action      def __len__(self):         return len(self.action)      def perform(         self, obj: GenieWorksheet, bot: GenieRuntime, local_context: GenieContext     ) -> list:         """Perform the action with the given context.          Args:             obj (GenieWorksheet): The worksheet object.             bot (GenieRuntime): The bot instance.             local_context (GenieContext): The local context.          Returns:             list: List of actions performed.         """         code = modify_action_code(self.action, obj, bot, local_context)         code = sanitize_dev_code(code, bot.get_all_variables())          # this is right now a hack. We are just going to assign all the statments to a variable         # and then return the variable         acts = []         # here what i need to do is:         # 1. rewrite the code such that and inbuilt function appends its result to __return         # 2. then return __return          # We append the results to the __return variable. This is done by the rewriter         transformed_code = rewrite_action_code(             code,             ["say", "propose", "answer_clarification_question"],  # predefined actions         )         code_ = f"__return = []\n{transformed_code}"          local_context.context["__return"] = None          # Execute the action code         bot.execute(code_, local_context)          # Context management         if local_context.context["__return"] is not None:             acts.extend(local_context.context["__return"])         del local_context.context["__return"]          if "_obj" in local_context.context:             del local_context.context["_obj"]          return acts ``` |

##### Attributes

###### action `instance-attribute`

```
action = action
```

##### Functions

###### \_\_init\_\_

```
__init__(action)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 949 950 ``` | ``` def __init__(self, action):     self.action = action ``` |

###### \_\_len\_\_

```
__len__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 952 953 ``` | ``` def __len__(self):     return len(self.action) ``` |

###### perform

```
perform(obj: GenieWorksheet, bot: GenieRuntime, local_context: GenieContext) -> list
```

Perform the action with the given context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `obj` | `GenieWorksheet` | The worksheet object. | *required* |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `list` | `list` | List of actions performed. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 955 956 957 958 959 960 961 962 963 964 965 966 967 968 969 970 971 972 973 974 975 976 977 978 979 980 981 982 983 984 985 986 987 988 989 990 991 992 993 994 995 996 997 998 ``` | ``` def perform(     self, obj: GenieWorksheet, bot: GenieRuntime, local_context: GenieContext ) -> list:     """Perform the action with the given context.      Args:         obj (GenieWorksheet): The worksheet object.         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context.      Returns:         list: List of actions performed.     """     code = modify_action_code(self.action, obj, bot, local_context)     code = sanitize_dev_code(code, bot.get_all_variables())      # this is right now a hack. We are just going to assign all the statments to a variable     # and then return the variable     acts = []     # here what i need to do is:     # 1. rewrite the code such that and inbuilt function appends its result to __return     # 2. then return __return      # We append the results to the __return variable. This is done by the rewriter     transformed_code = rewrite_action_code(         code,         ["say", "propose", "answer_clarification_question"],  # predefined actions     )     code_ = f"__return = []\n{transformed_code}"      local_context.context["__return"] = None      # Execute the action code     bot.execute(code_, local_context)      # Context management     if local_context.context["__return"] is not None:         acts.extend(local_context.context["__return"])     del local_context.context["__return"]      if "_obj" in local_context.context:         del local_context.context["_obj"]      return acts ``` |

#### GenieRuntime

Main runtime environment for Genie system.

This class manages the execution environment, including worksheet registration,
context management, and action execution.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `str` | Runtime instance name. |
| `prompt_dir` | `str` | Directory for prompts. |
| `args` |  | Additional arguments. |
| `genie_worksheets` | `list` | Registered worksheets. |
| `genie_db_models` | `list` | Registered database models. |
| `starting_prompt` | `str` | Initial system prompt. |
| `description` | `str` | Runtime description. |
| `suql_runner` |  | SQL query runner. |
| `suql_parser` |  | SQL query parser. |
| `context` | `GenieContext` | Global context. |
| `dlg_history` | `list` | Dialogue history. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1001 1002 1003 1004 1005 1006 1007 1008 1009 1010 1011 1012 1013 1014 1015 1016 1017 1018 1019 1020 1021 1022 1023 1024 1025 1026 1027 1028 1029 1030 1031 1032 1033 1034 1035 1036 1037 1038 1039 1040 1041 1042 1043 1044 1045 1046 1047 1048 1049 1050 1051 1052 1053 1054 1055 1056 1057 1058 1059 1060 1061 1062 1063 1064 1065 1066 1067 1068 1069 1070 1071 1072 1073 1074 1075 1076 1077 1078 1079 1080 1081 1082 1083 1084 1085 1086 1087 1088 1089 1090 1091 1092 1093 1094 1095 1096 1097 1098 1099 1100 1101 1102 1103 1104 1105 1106 1107 1108 1109 1110 1111 1112 1113 1114 1115 1116 1117 1118 1119 1120 1121 1122 1123 1124 1125 1126 1127 1128 1129 1130 1131 1132 1133 1134 1135 1136 1137 1138 1139 1140 1141 1142 1143 1144 1145 1146 1147 1148 1149 1150 1151 1152 1153 1154 1155 1156 1157 1158 1159 1160 1161 1162 1163 1164 1165 1166 1167 1168 1169 1170 1171 1172 1173 1174 1175 1176 1177 1178 1179 1180 1181 1182 1183 1184 1185 1186 1187 1188 1189 1190 1191 1192 1193 1194 1195 1196 1197 1198 1199 1200 1201 1202 1203 1204 1205 1206 1207 1208 1209 1210 1211 1212 1213 1214 1215 1216 1217 1218 1219 1220 1221 1222 1223 1224 1225 1226 1227 1228 1229 1230 1231 1232 1233 1234 1235 1236 1237 1238 1239 1240 1241 1242 1243 1244 1245 1246 1247 1248 1249 1250 1251 1252 1253 1254 1255 1256 ``` | ``` class GenieRuntime:     """Main runtime environment for Genie system.      This class manages the execution environment, including worksheet registration,     context management, and action execution.      Attributes:         name (str): Runtime instance name.         prompt_dir (str): Directory for prompts.         args: Additional arguments.         genie_worksheets (list): Registered worksheets.         genie_db_models (list): Registered database models.         starting_prompt (str): Initial system prompt.         description (str): Runtime description.         suql_runner: SQL query runner.         suql_parser: SQL query parser.         context (GenieContext): Global context.         dlg_history (list): Dialogue history.     """      def __init__(         self,         # The name of the bot         name,         # The directory where the prompts are stored         prompt_dir,         # The starting prompt of the bot         starting_prompt=None,         # A description of the bot         description=None,         # Any additional arguments         args=None,         # Define the API to be used         api=None,         # The SUQL runner (SUQLKnowledgeBase)         suql_runner=None,         # The SUQL parser (SUQLParser)         suql_parser=None,     ):         self.prompt_dir = prompt_dir         self.args = args         self.name = name         self.genie_worksheets = []         self.genie_db_models = []         if starting_prompt is None:             self.starting_prompt = f"Hello! I'm the {name}. What would you like to do?"         self.starting_prompt = starting_prompt         self.description = description         self.suql_runner = suql_runner         self.suql_parser = suql_parser          self._interpreter = GenieInterpreter()         self.context = GenieContext()         self.local_context_init = GenieContext()          # add the api to the context         if api:             if isinstance(api, list):                 apis = api             else:                 api_funcs = inspect.getmembers(api, inspect.isfunction)                 apis = [func for name, func in api_funcs if not name.startswith("_")]         else:             apis = []         self.dlg_history = []          self.order_of_actions = []          apis.extend([self.suql_runner])          Answer.bot = self          # Add the predefined apis and functions         apis.extend(             [                 propose,                 confirm,                 GenieValue,                 partial(answer_clarification_question, context=self.context),                 Answer,                 MoreFieldInfo,                 say,             ]         )         for api in apis:             self.add_api(api)      def reset(self):         """Reset the bot's context and state."""         self.context.reset_agent_acts()         to_delete = []         for key, value in self.context.context.items():             if isinstance(value, GenieWorksheet):                 to_delete.append(key)          for key in to_delete:             del self.context.context[key]         self.dlg_history = None         self.order_of_actions = []      def add_worksheet(self, ws: type):         """Add a worksheet to the bot's context.          Args:             ws (type): The worksheet class to add.         """         ws.bot = self         for field in get_genie_fields_from_ws(ws):             field.parent = ws             field.bot = self         self.genie_worksheets.append(ws)         self.context.set(ws.__name__, ws)         # self.context.update(self._grab_all_variables(ws))         # self.local_context_init.update(self._grab_all_variables(ws))      def add_db_model(self, db_model: type):         """Add a database model to the bot's context.          Args:             db_model (type): The database model class to add.         """         db_model.bot = self         for field in get_genie_fields_from_ws(db_model):             field.parent = db_model             field.bot = self         self.genie_db_models.append(db_model)         self.context.set(db_model.__name__, db_model)         # self.context.update(self._grab_all_variables(db_model))         # self.local_context_init.update(self._grab_all_variables(db_model))      def add_api(self, api: Any):         """Add an API function to the context.          Args:             api (Any): The API function or object to add.         """         self.context.set(callable_name(api), api)      def geniews(         self,         predicates=None,         outputs: GenieWorksheet | dict | None = None,         backend_api=None,         actions="",     ):         """Decorator to define a Genie worksheet."""          def decorator(cls):             cls.predicate = predicates             cls.outputs = outputs             cls.backend_api = backend_api             cls.actions = actions             self.add_worksheet(cls)             return cls          return decorator      def genie_sql(         self,         outputs: GenieWorksheet | dict | None = None,         actions="",     ):         """Decorator to define a Genie database model."""          def decorator(cls):             if outputs is None:                 outputs = {}             cls.outputs = outputs             cls.actions = actions             self.add_db_model(cls)             return cls          return decorator      def execute(         self, code: str, local_context: GenieContext | None = None, sp: bool = False     ):         """Execute the given code in the context of the bot.          Args:             code (str): The code to execute.             local_context (GenieContext | None, optional): Local context to use. Defaults to None.             sp (bool, optional): Whether this is a semantic parser execution. Defaults to False.         """         if local_context:             local_context.update(                 {k: v for k, v in self.local_context_init.context.items()}             )         else:             local_context = GenieContext(                 {k: v for k, v in self.local_context_init.context.items()}             )         self._interpreter.execute(             code,             self.context,             local_context,             sp=sp,         )          # Add the parents for all the objects in the local context         collect_all_parents(local_context)      def eval(self, code: str, local_context: GenieContext | None = None) -> Any:         """Evaluate the given code in the context of the bot.          Args:             code (str): The code to evaluate.             local_context (GenieContext | None, optional): Local context to use. Defaults to None.          Returns:             Any: The result of the evaluation.         """         if local_context:             local_context.update(                 {k: v for k, v in self.local_context_init.context.items()}             )         else:             local_context = GenieContext(                 {k: v for k, v in self.local_context_init.context.items()}             )         return self._interpreter.eval(             code,             self.context,             local_context,         )      def update_from_context(self, context):         """add new variables to the context"""         self.context.update(context.context)      def get_available_worksheets(self, context):         """Get all available worksheets based on their predicates."""         for ws in self.genie_worksheets:             if ws.predicate:                 if eval_predicates(ws.predicate, None, self, context):                     yield ws             else:                 yield ws      def get_available_dbs(self, context):         """Get all available database models based on their predicates."""         for db in self.genie_db_models:             if db.predicate:                 if eval_predicates(db.predicate, None, self, context):                     yield db             else:                 yield db      def get_all_variables(self):         """Get all fields (variables) from all worksheets."""         all_variables = []         for ws in self.genie_worksheets:             for field in get_genie_fields_from_ws(ws):                 all_variables.append(field.name)          return all_variables ``` |

##### Attributes

###### prompt\_dir `instance-attribute`

```
prompt_dir = prompt_dir
```

###### args `instance-attribute`

```
args = args
```

###### name `instance-attribute`

```
name = name
```

###### genie\_worksheets `instance-attribute`

```
genie_worksheets = []
```

###### genie\_db\_models `instance-attribute`

```
genie_db_models = []
```

###### starting\_prompt `instance-attribute`

```
starting_prompt = starting_prompt
```

###### description `instance-attribute`

```
description = description
```

###### suql\_runner `instance-attribute`

```
suql_runner = suql_runner
```

###### suql\_parser `instance-attribute`

```
suql_parser = suql_parser
```

###### \_interpreter `instance-attribute`

```
_interpreter = GenieInterpreter()
```

###### context `instance-attribute`

```
context = GenieContext()
```

###### local\_context\_init `instance-attribute`

```
local_context_init = GenieContext()
```

###### dlg\_history `instance-attribute`

```
dlg_history = []
```

###### order\_of\_actions `instance-attribute`

```
order_of_actions = []
```

##### Functions

###### \_\_init\_\_

```
__init__(name, prompt_dir, starting_prompt=None, description=None, args=None, api=None, suql_runner=None, suql_parser=None)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1021 1022 1023 1024 1025 1026 1027 1028 1029 1030 1031 1032 1033 1034 1035 1036 1037 1038 1039 1040 1041 1042 1043 1044 1045 1046 1047 1048 1049 1050 1051 1052 1053 1054 1055 1056 1057 1058 1059 1060 1061 1062 1063 1064 1065 1066 1067 1068 1069 1070 1071 1072 1073 1074 1075 1076 1077 1078 1079 1080 1081 1082 1083 1084 1085 1086 ``` | ``` def __init__(     self,     # The name of the bot     name,     # The directory where the prompts are stored     prompt_dir,     # The starting prompt of the bot     starting_prompt=None,     # A description of the bot     description=None,     # Any additional arguments     args=None,     # Define the API to be used     api=None,     # The SUQL runner (SUQLKnowledgeBase)     suql_runner=None,     # The SUQL parser (SUQLParser)     suql_parser=None, ):     self.prompt_dir = prompt_dir     self.args = args     self.name = name     self.genie_worksheets = []     self.genie_db_models = []     if starting_prompt is None:         self.starting_prompt = f"Hello! I'm the {name}. What would you like to do?"     self.starting_prompt = starting_prompt     self.description = description     self.suql_runner = suql_runner     self.suql_parser = suql_parser      self._interpreter = GenieInterpreter()     self.context = GenieContext()     self.local_context_init = GenieContext()      # add the api to the context     if api:         if isinstance(api, list):             apis = api         else:             api_funcs = inspect.getmembers(api, inspect.isfunction)             apis = [func for name, func in api_funcs if not name.startswith("_")]     else:         apis = []     self.dlg_history = []      self.order_of_actions = []      apis.extend([self.suql_runner])      Answer.bot = self      # Add the predefined apis and functions     apis.extend(         [             propose,             confirm,             GenieValue,             partial(answer_clarification_question, context=self.context),             Answer,             MoreFieldInfo,             say,         ]     )     for api in apis:         self.add_api(api) ``` |

###### reset

```
reset()
```

Reset the bot's context and state.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1088 1089 1090 1091 1092 1093 1094 1095 1096 1097 1098 1099 ``` | ``` def reset(self):     """Reset the bot's context and state."""     self.context.reset_agent_acts()     to_delete = []     for key, value in self.context.context.items():         if isinstance(value, GenieWorksheet):             to_delete.append(key)      for key in to_delete:         del self.context.context[key]     self.dlg_history = None     self.order_of_actions = [] ``` |

###### add\_worksheet

```
add_worksheet(ws: type)
```

Add a worksheet to the bot's context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ws` | `type` | The worksheet class to add. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1101 1102 1103 1104 1105 1106 1107 1108 1109 1110 1111 1112 ``` | ``` def add_worksheet(self, ws: type):     """Add a worksheet to the bot's context.      Args:         ws (type): The worksheet class to add.     """     ws.bot = self     for field in get_genie_fields_from_ws(ws):         field.parent = ws         field.bot = self     self.genie_worksheets.append(ws)     self.context.set(ws.__name__, ws) ``` |

###### add\_db\_model

```
add_db_model(db_model: type)
```

Add a database model to the bot's context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `db_model` | `type` | The database model class to add. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1116 1117 1118 1119 1120 1121 1122 1123 1124 1125 1126 1127 ``` | ``` def add_db_model(self, db_model: type):     """Add a database model to the bot's context.      Args:         db_model (type): The database model class to add.     """     db_model.bot = self     for field in get_genie_fields_from_ws(db_model):         field.parent = db_model         field.bot = self     self.genie_db_models.append(db_model)     self.context.set(db_model.__name__, db_model) ``` |

###### add\_api

```
add_api(api: Any)
```

Add an API function to the context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `api` | `Any` | The API function or object to add. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1131 1132 1133 1134 1135 1136 1137 ``` | ``` def add_api(self, api: Any):     """Add an API function to the context.      Args:         api (Any): The API function or object to add.     """     self.context.set(callable_name(api), api) ``` |

###### geniews

```
geniews(predicates=None, outputs: GenieWorksheet | dict | None = None, backend_api=None, actions='')
```

Decorator to define a Genie worksheet.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1139 1140 1141 1142 1143 1144 1145 1146 1147 1148 1149 1150 1151 1152 1153 1154 1155 1156 ``` | ``` def geniews(     self,     predicates=None,     outputs: GenieWorksheet | dict | None = None,     backend_api=None,     actions="", ):     """Decorator to define a Genie worksheet."""      def decorator(cls):         cls.predicate = predicates         cls.outputs = outputs         cls.backend_api = backend_api         cls.actions = actions         self.add_worksheet(cls)         return cls      return decorator ``` |

###### genie\_sql

```
genie_sql(outputs: GenieWorksheet | dict | None = None, actions='')
```

Decorator to define a Genie database model.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1158 1159 1160 1161 1162 1163 1164 1165 1166 1167 1168 1169 1170 1171 1172 1173 ``` | ``` def genie_sql(     self,     outputs: GenieWorksheet | dict | None = None,     actions="", ):     """Decorator to define a Genie database model."""      def decorator(cls):         if outputs is None:             outputs = {}         cls.outputs = outputs         cls.actions = actions         self.add_db_model(cls)         return cls      return decorator ``` |

###### execute

```
execute(code: str, local_context: GenieContext | None = None, sp: bool = False)
```

Execute the given code in the context of the bot.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `code` | `str` | The code to execute. | *required* |
| `local_context` | `GenieContext | None` | Local context to use. Defaults to None. | `None` |
| `sp` | `bool` | Whether this is a semantic parser execution. Defaults to False. | `False` |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1175 1176 1177 1178 1179 1180 1181 1182 1183 1184 1185 1186 1187 1188 1189 1190 1191 1192 1193 1194 1195 1196 1197 1198 1199 1200 1201 ``` | ``` def execute(     self, code: str, local_context: GenieContext | None = None, sp: bool = False ):     """Execute the given code in the context of the bot.      Args:         code (str): The code to execute.         local_context (GenieContext | None, optional): Local context to use. Defaults to None.         sp (bool, optional): Whether this is a semantic parser execution. Defaults to False.     """     if local_context:         local_context.update(             {k: v for k, v in self.local_context_init.context.items()}         )     else:         local_context = GenieContext(             {k: v for k, v in self.local_context_init.context.items()}         )     self._interpreter.execute(         code,         self.context,         local_context,         sp=sp,     )      # Add the parents for all the objects in the local context     collect_all_parents(local_context) ``` |

###### eval

```
eval(code: str, local_context: GenieContext | None = None) -> Any
```

Evaluate the given code in the context of the bot.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `code` | `str` | The code to evaluate. | *required* |
| `local_context` | `GenieContext | None` | Local context to use. Defaults to None. | `None` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `Any` | `Any` | The result of the evaluation. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1203 1204 1205 1206 1207 1208 1209 1210 1211 1212 1213 1214 1215 1216 1217 1218 1219 1220 1221 1222 1223 1224 1225 ``` | ``` def eval(self, code: str, local_context: GenieContext | None = None) -> Any:     """Evaluate the given code in the context of the bot.      Args:         code (str): The code to evaluate.         local_context (GenieContext | None, optional): Local context to use. Defaults to None.      Returns:         Any: The result of the evaluation.     """     if local_context:         local_context.update(             {k: v for k, v in self.local_context_init.context.items()}         )     else:         local_context = GenieContext(             {k: v for k, v in self.local_context_init.context.items()}         )     return self._interpreter.eval(         code,         self.context,         local_context,     ) ``` |

###### update\_from\_context

```
update_from_context(context)
```

add new variables to the context

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1227 1228 1229 ``` | ``` def update_from_context(self, context):     """add new variables to the context"""     self.context.update(context.context) ``` |

###### get\_available\_worksheets

```
get_available_worksheets(context)
```

Get all available worksheets based on their predicates.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1231 1232 1233 1234 1235 1236 1237 1238 ``` | ``` def get_available_worksheets(self, context):     """Get all available worksheets based on their predicates."""     for ws in self.genie_worksheets:         if ws.predicate:             if eval_predicates(ws.predicate, None, self, context):                 yield ws         else:             yield ws ``` |

###### get\_available\_dbs

```
get_available_dbs(context)
```

Get all available database models based on their predicates.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1240 1241 1242 1243 1244 1245 1246 1247 ``` | ``` def get_available_dbs(self, context):     """Get all available database models based on their predicates."""     for db in self.genie_db_models:         if db.predicate:             if eval_predicates(db.predicate, None, self, context):                 yield db         else:             yield db ``` |

###### get\_all\_variables

```
get_all_variables()
```

Get all fields (variables) from all worksheets.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1249 1250 1251 1252 1253 1254 1255 1256 ``` | ``` def get_all_variables(self):     """Get all fields (variables) from all worksheets."""     all_variables = []     for ws in self.genie_worksheets:         for field in get_genie_fields_from_ws(ws):             all_variables.append(field.name)      return all_variables ``` |

#### GenieInterpreter

Interpreter for executing Genie code.

This class provides code execution capabilities within the Genie environment,
handling variable resolution and context management.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1259 1260 1261 1262 1263 1264 1265 1266 1267 1268 1269 1270 1271 1272 1273 1274 1275 1276 1277 1278 1279 1280 1281 1282 1283 1284 1285 1286 1287 1288 1289 1290 1291 1292 1293 1294 1295 1296 1297 1298 1299 1300 1301 1302 1303 ``` | ``` class GenieInterpreter:     """Interpreter for executing Genie code.      This class provides code execution capabilities within the Genie environment,     handling variable resolution and context management.     """      def execute(self, code, global_context, local_context, sp=False):         # There are some issues here. since there are no numbers now,         # when we do courses_to_take = CoursesToTake(courses_0_details=course)         # since courses_to_take is a field in main worksheet, the code gets modified to:         # main.courses_to_take.value = CoursesToTake(courses_0_details=course)         # One easy fix could be if you are setting a GenieWorksheet to a field, then         # do not modify the code.          # Another way is to have an, argument which mentions if the execution is from semantic parser         # if it is, then do not modify the code.          if not sp:             # If the execution is for action then we replace the undefined variables             code = replace_undefined_variables(code, local_context, global_context)         try:             try:                 exec(code, global_context.context, local_context.context)             except NameError as e:                 local_context.set(e.name, None)                 # regex to catch the variable name. If the variable name is "user_task" then we want to find "user_task.value" as well until we hit a space.                 # This is just a hack ideally we should traverse the ast or at least use the tokenize module to find the variable name                 var_name = re.findall(rf"{e.name}\.\w+", code)                 if var_name:                     code = code.replace(var_name[0], f"{e.name}")                 exec(code, global_context.context, local_context.context)                 local_context.delete(e.name)         except Exception as e:             logger.error(f"Error: {e}")             logger.error(f"Code: {code}")      def eval(self, code, global_context, local_context):         # perform rewrite to update any variables that is not in the local context         # by using the variable resolver         code = replace_undefined_variables(code, local_context, global_context).strip()         try:             return eval(code, global_context.context, local_context.context)         except (NameError, AttributeError):             return False ``` |

##### Functions

###### execute

```
execute(code, global_context, local_context, sp=False)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1266 1267 1268 1269 1270 1271 1272 1273 1274 1275 1276 1277 1278 1279 1280 1281 1282 1283 1284 1285 1286 1287 1288 1289 1290 1291 1292 1293 1294 ``` | ``` def execute(self, code, global_context, local_context, sp=False):     # There are some issues here. since there are no numbers now,     # when we do courses_to_take = CoursesToTake(courses_0_details=course)     # since courses_to_take is a field in main worksheet, the code gets modified to:     # main.courses_to_take.value = CoursesToTake(courses_0_details=course)     # One easy fix could be if you are setting a GenieWorksheet to a field, then     # do not modify the code.      # Another way is to have an, argument which mentions if the execution is from semantic parser     # if it is, then do not modify the code.      if not sp:         # If the execution is for action then we replace the undefined variables         code = replace_undefined_variables(code, local_context, global_context)     try:         try:             exec(code, global_context.context, local_context.context)         except NameError as e:             local_context.set(e.name, None)             # regex to catch the variable name. If the variable name is "user_task" then we want to find "user_task.value" as well until we hit a space.             # This is just a hack ideally we should traverse the ast or at least use the tokenize module to find the variable name             var_name = re.findall(rf"{e.name}\.\w+", code)             if var_name:                 code = code.replace(var_name[0], f"{e.name}")             exec(code, global_context.context, local_context.context)             local_context.delete(e.name)     except Exception as e:         logger.error(f"Error: {e}")         logger.error(f"Code: {code}") ``` |

###### eval

```
eval(code, global_context, local_context)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1296 1297 1298 1299 1300 1301 1302 1303 ``` | ``` def eval(self, code, global_context, local_context):     # perform rewrite to update any variables that is not in the local context     # by using the variable resolver     code = replace_undefined_variables(code, local_context, global_context).strip()     try:         return eval(code, global_context.context, local_context.context)     except (NameError, AttributeError):         return False ``` |

#### GenieContext

Context manager for Genie runtime.

This class manages variable context and agent actions during runtime.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `context` | `dict` | The context dictionary. |
| `agent_acts` |  | Current agent actions. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1306 1307 1308 1309 1310 1311 1312 1313 1314 1315 1316 1317 1318 1319 1320 1321 1322 1323 1324 1325 1326 1327 1328 1329 1330 1331 1332 1333 1334 1335 1336 1337 1338 1339 1340 1341 1342 1343 1344 1345 1346 1347 1348 1349 1350 1351 1352 1353 1354 1355 1356 1357 1358 1359 1360 1361 1362 1363 1364 1365 1366 1367 1368 1369 1370 1371 1372 1373 1374 1375 1376 1377 1378 1379 1380 ``` | ``` class GenieContext:     """Context manager for Genie runtime.      This class manages variable context and agent actions during runtime.      Attributes:         context (dict): The context dictionary.         agent_acts: Current agent actions.     """      def __init__(self, context: dict = None):         if context is None:             context = {}         self.context = context         self.agent_acts = None         self.reset_agent_acts()      def reset_agent_acts(self):         self.agent_acts = AgentActs({})      def update(self, content: dict):         """Update the context with new content.          Args:             content (dict): Dictionary of content to update with.         """         for key, value in content.items():             if key != "answer" and key in self.context:                 if not isinstance(self.context[key], list):                     if self.context[key] != value:                         self.context[key] = [                             self.context[key]                         ]  # TODO: make the line below this else: if                 else:                     if isinstance(value, list):                         for v in value:                             if v not in self.context[key]:                                 self.context[key].append(v)                     else:                         self.context[key].append(value)             else:                 self.context[key] = value      def get(self, key: str) -> Any:         """Get a value from the context.          Args:             key (str): The key to get.          Returns:             Any: The value associated with the key.         """         return self.context[key]      def set(self, key: str, value: Any):         """Set a value in the context.          Args:             key (str): The key to set.             value (Any): The value to set.         """         if key != "answer" and key in self.context:             if not isinstance(self.context[key], list):                 self.context[key] = [self.context[key]]             self.context[key].append(value)         else:             self.context[key] = value      def delete(self, key: str):         """Delete a key from the context.          Args:             key (str): The key to delete.         """         del self.context[key] ``` |

##### Attributes

###### context `instance-attribute`

```
context = context
```

###### agent\_acts `instance-attribute`

```
agent_acts = None
```

##### Functions

###### \_\_init\_\_

```
__init__(context: dict = None)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1316 1317 1318 1319 1320 1321 ``` | ``` def __init__(self, context: dict = None):     if context is None:         context = {}     self.context = context     self.agent_acts = None     self.reset_agent_acts() ``` |

###### reset\_agent\_acts

```
reset_agent_acts()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1323 1324 ``` | ``` def reset_agent_acts(self):     self.agent_acts = AgentActs({}) ``` |

###### update

```
update(content: dict)
```

Update the context with new content.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `content` | `dict` | Dictionary of content to update with. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1326 1327 1328 1329 1330 1331 1332 1333 1334 1335 1336 1337 1338 1339 1340 1341 1342 1343 1344 1345 1346 1347 ``` | ``` def update(self, content: dict):     """Update the context with new content.      Args:         content (dict): Dictionary of content to update with.     """     for key, value in content.items():         if key != "answer" and key in self.context:             if not isinstance(self.context[key], list):                 if self.context[key] != value:                     self.context[key] = [                         self.context[key]                     ]  # TODO: make the line below this else: if             else:                 if isinstance(value, list):                     for v in value:                         if v not in self.context[key]:                             self.context[key].append(v)                 else:                     self.context[key].append(value)         else:             self.context[key] = value ``` |

###### get

```
get(key: str) -> Any
```

Get a value from the context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | The key to get. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `Any` | `Any` | The value associated with the key. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1349 1350 1351 1352 1353 1354 1355 1356 1357 1358 ``` | ``` def get(self, key: str) -> Any:     """Get a value from the context.      Args:         key (str): The key to get.      Returns:         Any: The value associated with the key.     """     return self.context[key] ``` |

###### set

```
set(key: str, value: Any)
```

Set a value in the context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | The key to set. | *required* |
| `value` | `Any` | The value to set. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1360 1361 1362 1363 1364 1365 1366 1367 1368 1369 1370 1371 1372 ``` | ``` def set(self, key: str, value: Any):     """Set a value in the context.      Args:         key (str): The key to set.         value (Any): The value to set.     """     if key != "answer" and key in self.context:         if not isinstance(self.context[key], list):             self.context[key] = [self.context[key]]         self.context[key].append(value)     else:         self.context[key] = value ``` |

###### delete

```
delete(key: str)
```

Delete a key from the context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | The key to delete. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1374 1375 1376 1377 1378 1379 1380 ``` | ``` def delete(self, key: str):     """Delete a key from the context.      Args:         key (str): The key to delete.     """     del self.context[key] ``` |

#### TurnContext

Context manager for dialogue turns.

This class manages context for individual dialogue turns.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `context` | `list[GenieContext]` | List of contexts for each turn. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1383 1384 1385 1386 1387 1388 1389 1390 1391 1392 1393 1394 1395 1396 1397 1398 1399 1400 1401 ``` | ``` class TurnContext:     """Context manager for dialogue turns.      This class manages context for individual dialogue turns.      Attributes:         context (list[GenieContext]): List of contexts for each turn.     """      def __init__(self):         self.context: list[GenieContext] = []      def add_turn_context(self, context: GenieContext):         """Add a new turn context.          Args:             context (GenieContext): The context to add for this turn.         """         self.context.append(deepcopy(context)) ``` |

##### Attributes

###### context `instance-attribute`

```
context: list[GenieContext] = []
```

##### Functions

###### \_\_init\_\_

```
__init__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1392 1393 ``` | ``` def __init__(self):     self.context: list[GenieContext] = [] ``` |

###### add\_turn\_context

```
add_turn_context(context: GenieContext)
```

Add a new turn context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` | `GenieContext` | The context to add for this turn. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1395 1396 1397 1398 1399 1400 1401 ``` | ``` def add_turn_context(self, context: GenieContext):     """Add a new turn context.      Args:         context (GenieContext): The context to add for this turn.     """     self.context.append(deepcopy(context)) ``` |

#### AgentAct

Base class for agent actions.

This class serves as the foundation for different types of agent actions
in the system.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1931 1932 1933 1934 1935 1936 ``` | ``` class AgentAct:     """Base class for agent actions.      This class serves as the foundation for different types of agent actions     in the system.     """ ``` |

#### ReportAgentAct

Bases: `AgentAct`

Action for reporting query results or messages.

This class handles reporting of query results and system messages.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `query` | `GenieField` | The query being reported. |
| `message` |  | The message or result to report. |
| `query_var_name` |  | Variable name for the query. |
| `message_var_name` |  | Variable name for the message. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1939 1940 1941 1942 1943 1944 1945 1946 1947 1948 1949 1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 1962 1963 1964 1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 ``` | ``` class ReportAgentAct(AgentAct):     """Action for reporting query results or messages.      This class handles reporting of query results and system messages.      Attributes:         query (GenieField): The query being reported.         message: The message or result to report.         query_var_name: Variable name for the query.         message_var_name: Variable name for the message.     """      def __init__(         self,         query: GenieField,         message: Any,         query_var_name=None,         message_var_name=None,     ):         self.query = query         self.message = message         self.query_var_name = query_var_name         self.message_var_name = message_var_name      def __repr__(self):         if self.query_var_name:             query_var_name = self.query_var_name         else:             query_var_name = self.query          if self.message_var_name:             message_var_name = self.message_var_name         else:             message_var_name = self.message         return f"Report({query_var_name}, {message_var_name})"      def __eq__(self, other):         if isinstance(other, ReportAgentAct):             if self.query == other.query and self.message == other.message:                 return True         return False ``` |

##### Attributes

###### query `instance-attribute`

```
query = query
```

###### message `instance-attribute`

```
message = message
```

###### query\_var\_name `instance-attribute`

```
query_var_name = query_var_name
```

###### message\_var\_name `instance-attribute`

```
message_var_name = message_var_name
```

##### Functions

###### \_\_init\_\_

```
__init__(query: GenieField, message: Any, query_var_name=None, message_var_name=None)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 ``` | ``` def __init__(     self,     query: GenieField,     message: Any,     query_var_name=None,     message_var_name=None, ):     self.query = query     self.message = message     self.query_var_name = query_var_name     self.message_var_name = message_var_name ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1963 1964 1965 1966 1967 1968 1969 1970 1971 1972 1973 ``` | ``` def __repr__(self):     if self.query_var_name:         query_var_name = self.query_var_name     else:         query_var_name = self.query      if self.message_var_name:         message_var_name = self.message_var_name     else:         message_var_name = self.message     return f"Report({query_var_name}, {message_var_name})" ``` |

###### \_\_eq\_\_

```
__eq__(other)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1975 1976 1977 1978 1979 ``` | ``` def __eq__(self, other):     if isinstance(other, ReportAgentAct):         if self.query == other.query and self.message == other.message:             return True     return False ``` |

#### AskAgentAct

Bases: `AgentAct`

Action for requesting information from users.

This class handles user information requests.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `ws` | `GenieWorksheet` | The worksheet context. |
| `field` | `GenieField` | The field to ask about. |
| `ws_name` |  | Worksheet name override. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 ``` | ``` class AskAgentAct(AgentAct):     """Action for requesting information from users.      This class handles user information requests.      Attributes:         ws (GenieWorksheet): The worksheet context.         field (GenieField): The field to ask about.         ws_name: Worksheet name override.     """      def __init__(self, ws: GenieWorksheet, field: GenieField, ws_name=None):         self.ws = ws         self.field = field         self.ws_name = ws_name      def __repr__(self):         description = None         if inspect.isclass(self.field.slottype):             if issubclass(self.field.slottype, Enum):                 options = [                     x.name for x in list(self.field.slottype.__members__.values())                 ]                 options = ", ".join(options)                 description = self.field.description + f" Options are: {options}"          if description is None and self.field.description is not None:             description = self.field.description          if self.ws_name:             return f"AskField({self.ws_name}, {self.field.name}, {description})"         return (             f"AskField({self.ws.__class__.__name__}, {self.field.name}, {description})"         ) ``` |

##### Attributes

###### ws `instance-attribute`

```
ws = ws
```

###### field `instance-attribute`

```
field = field
```

###### ws\_name `instance-attribute`

```
ws_name = ws_name
```

##### Functions

###### \_\_init\_\_

```
__init__(ws: GenieWorksheet, field: GenieField, ws_name=None)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1993 1994 1995 1996 ``` | ``` def __init__(self, ws: GenieWorksheet, field: GenieField, ws_name=None):     self.ws = ws     self.field = field     self.ws_name = ws_name ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 ``` | ``` def __repr__(self):     description = None     if inspect.isclass(self.field.slottype):         if issubclass(self.field.slottype, Enum):             options = [                 x.name for x in list(self.field.slottype.__members__.values())             ]             options = ", ".join(options)             description = self.field.description + f" Options are: {options}"      if description is None and self.field.description is not None:         description = self.field.description      if self.ws_name:         return f"AskField({self.ws_name}, {self.field.name}, {description})"     return (         f"AskField({self.ws.__class__.__name__}, {self.field.name}, {description})"     ) ``` |

#### ProposeAgentAct

Bases: `AgentAct`

Action for proposing worksheet values.

This class handles proposals for worksheet field values.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `ws` | `GenieWorksheet` | The worksheet context. |
| `params` | `dict` | Proposed parameters. |
| `ws_name` |  | Worksheet name override. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027 2028 2029 2030 2031 2032 2033 2034 2035 2036 2037 ``` | ``` class ProposeAgentAct(AgentAct):     """Action for proposing worksheet values.      This class handles proposals for worksheet field values.      Attributes:         ws (GenieWorksheet): The worksheet context.         params (dict): Proposed parameters.         ws_name: Worksheet name override.     """      def __init__(self, ws: GenieWorksheet, params: dict, ws_name=None):         self.ws = ws         self.params = params         self.ws_name = ws_name      def __repr__(self):         if self.ws_name:             return f"ProposeAgentAct({self.ws_name}, {self.params})"         return f"ProposeAgentAct({self.ws.__class__.__name__}, {self.params})" ``` |

##### Attributes

###### ws `instance-attribute`

```
ws = ws
```

###### params `instance-attribute`

```
params = params
```

###### ws\_name `instance-attribute`

```
ws_name = ws_name
```

##### Functions

###### \_\_init\_\_

```
__init__(ws: GenieWorksheet, params: dict, ws_name=None)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2029 2030 2031 2032 ``` | ``` def __init__(self, ws: GenieWorksheet, params: dict, ws_name=None):     self.ws = ws     self.params = params     self.ws_name = ws_name ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2034 2035 2036 2037 ``` | ``` def __repr__(self):     if self.ws_name:         return f"ProposeAgentAct({self.ws_name}, {self.params})"     return f"ProposeAgentAct({self.ws.__class__.__name__}, {self.params})" ``` |

#### AskForConfirmationAgentAct

Bases: `AgentAct`

Action for requesting user confirmation.

This class handles confirmation requests for field values.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `ws` | `GenieWorksheet` | The worksheet context. |
| `field` | `GenieField` | The field to confirm. |
| `ws_name` |  | Worksheet name override. |
| `field_name` |  | Field name override. |
| `value` |  | Value to confirm. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2040 2041 2042 2043 2044 2045 2046 2047 2048 2049 2050 2051 2052 2053 2054 2055 2056 2057 2058 2059 2060 2061 2062 2063 2064 2065 2066 2067 2068 2069 2070 2071 2072 2073 ``` | ``` class AskForConfirmationAgentAct(AgentAct):     """Action for requesting user confirmation.      This class handles confirmation requests for field values.      Attributes:         ws (GenieWorksheet): The worksheet context.         field (GenieField): The field to confirm.         ws_name: Worksheet name override.         field_name: Field name override.         value: Value to confirm.     """      def __init__(         self, ws: "GenieWorksheet", field: "GenieField", ws_name=None, field_name=None     ):         self.ws = ws         self.field = field         self.ws_name = ws_name         self.field_name = field_name         self.value = None      def __repr__(self):         if self.ws_name:             ws_name = self.ws_name         else:             ws_name = self.ws.__class__.__name__          if self.field_name:             field_name = self.field_name         else:             field_name = self.field.name          return f"AskForFieldConfirmation({ws_name}, {field_name})" ``` |

##### Attributes

###### ws `instance-attribute`

```
ws = ws
```

###### field `instance-attribute`

```
field = field
```

###### ws\_name `instance-attribute`

```
ws_name = ws_name
```

###### field\_name `instance-attribute`

```
field_name = field_name
```

###### value `instance-attribute`

```
value = None
```

##### Functions

###### \_\_init\_\_

```
__init__(ws: 'GenieWorksheet', field: 'GenieField', ws_name=None, field_name=None)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2053 2054 2055 2056 2057 2058 2059 2060 ``` | ``` def __init__(     self, ws: "GenieWorksheet", field: "GenieField", ws_name=None, field_name=None ):     self.ws = ws     self.field = field     self.ws_name = ws_name     self.field_name = field_name     self.value = None ``` |

###### \_\_repr\_\_

```
__repr__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2062 2063 2064 2065 2066 2067 2068 2069 2070 2071 2072 2073 ``` | ``` def __repr__(self):     if self.ws_name:         ws_name = self.ws_name     else:         ws_name = self.ws.__class__.__name__      if self.field_name:         field_name = self.field_name     else:         field_name = self.field.name      return f"AskForFieldConfirmation({ws_name}, {field_name})" ``` |

#### AgentActs

Container for managing multiple agent actions.

This class manages collections of agent actions, handling action ordering
and compatibility.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `args` |  | Arguments for action management. |
| `actions` | `list` | List of agent actions. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2076 2077 2078 2079 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 2100 2101 2102 2103 2104 2105 2106 2107 2108 2109 2110 2111 2112 2113 2114 2115 2116 2117 2118 2119 2120 2121 2122 2123 2124 2125 2126 2127 2128 2129 2130 2131 2132 2133 2134 2135 2136 2137 2138 2139 2140 2141 2142 2143 2144 2145 2146 2147 2148 2149 2150 2151 2152 2153 2154 2155 2156 2157 2158 2159 2160 2161 2162 2163 2164 2165 2166 2167 2168 2169 2170 2171 2172 2173 2174 2175 2176 2177 2178 2179 2180 2181 2182 ``` | ``` class AgentActs:     """Container for managing multiple agent actions.      This class manages collections of agent actions, handling action ordering     and compatibility.      Attributes:         args: Arguments for action management.         actions (list): List of agent actions.     """      def __init__(self, args):         self.args = args         self.actions = []      def add(self, action):         self._add(action)      def _add(self, action):         if self.should_add(action):             self.actions.append(action)      def should_add(self, incoming_action):         """There can be multiple ReportActs, and (multiple propose acts or one ask acts or one confirmation act) but only one of each type of act"""         acts_to_action = {}         for action in self.actions:             if action.__class__.__name__ in acts_to_action:                 acts_to_action[action.__class__.__name__].append(action)             else:                 acts_to_action[action.__class__.__name__] = [action]          # Check if the incoming action is a ReportAct, if it is then check if there is already a ReportAct with the same query         if incoming_action.__class__.__name__ == "ReportAgentAct":             for action in acts_to_action.get("ReportAgentAct", []):                 if (                     action.query == incoming_action.query                     and action.message == incoming_action.message                 ):                     return False             return True         # Check if the incoming action is a ProposeAct, if it is then check if there is already a ProposeAct with the same query         # or AskAgentAct or AskForConfirmationAct are present         elif incoming_action.__class__.__name__ == "ProposeAgentAct":             if (                 "AskAgentAct" in acts_to_action                 or "AskForConfirmationAgentAct" in acts_to_action             ):                 return False             for action in acts_to_action.get("ProposeAgentAct", []):                 if action.params == incoming_action.params and same_worksheet(                     action.ws, incoming_action.ws                 ):                     return False             return True         # Check if the incoming action is a AskAgentAct, if other AskAgentAct or ProposeAgentAct or AskForConfirmationAgentAct are present         elif incoming_action.__class__.__name__ == "AskAgentAct":             if (                 "ProposeAgentAct" in acts_to_action                 or "AskAgentAct" in acts_to_action                 or "AskForConfirmationAgentAct" in acts_to_action             ):                 return False             return True         # Check if the incoming action is a AskForConfirmationAct, if other AskAgentAct or ProposeAgentAct or AskForConfirmationAgentAct are present         elif incoming_action.__class__.__name__ == "AskForConfirmationAgentAct":             if (                 "ProposeAgentAct" in acts_to_action                 or "AskAgentAct" in acts_to_action                 or "AskForConfirmationAgentAct" in acts_to_action             ):                 return False             return True          # for action in self.actions:         #     if isinstance(action, ReportAgentAct) or isinstance(action, ReportAgentAct):         #         if action == incoming_action:         #             return True         #     else:         #         return True          # return False      def extend(self, actions):         for action in actions:             self._add(action)      def __iter__(self):         return iter(self.actions)      def __next__(self):         return next(self.actions)      def can_have_other_acts(self):         acts_to_action = {}         for action in self.actions:             if action.__class__.__name__ in acts_to_action:                 acts_to_action[action.__class__.__name__].append(action)             else:                 acts_to_action[action.__class__.__name__] = [action]          if (             "ProposeAgentAct" in acts_to_action             or "AskAgentAct" in acts_to_action             or "AskForConfirmationAgentAct" in acts_to_action         ):             return False         return True ``` |

##### Attributes

###### args `instance-attribute`

```
args = args
```

###### actions `instance-attribute`

```
actions = []
```

##### Functions

###### \_\_init\_\_

```
__init__(args)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2087 2088 2089 ``` | ``` def __init__(self, args):     self.args = args     self.actions = [] ``` |

###### add

```
add(action)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2091 2092 ``` | ``` def add(self, action):     self._add(action) ``` |

###### \_add

```
_add(action)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2094 2095 2096 ``` | ``` def _add(self, action):     if self.should_add(action):         self.actions.append(action) ``` |

###### should\_add

```
should_add(incoming_action)
```

There can be multiple ReportActs, and (multiple propose acts or one ask acts or one confirmation act) but only one of each type of act

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2098 2099 2100 2101 2102 2103 2104 2105 2106 2107 2108 2109 2110 2111 2112 2113 2114 2115 2116 2117 2118 2119 2120 2121 2122 2123 2124 2125 2126 2127 2128 2129 2130 2131 2132 2133 2134 2135 2136 2137 2138 2139 2140 2141 2142 2143 2144 2145 2146 2147 ``` | ``` def should_add(self, incoming_action):     """There can be multiple ReportActs, and (multiple propose acts or one ask acts or one confirmation act) but only one of each type of act"""     acts_to_action = {}     for action in self.actions:         if action.__class__.__name__ in acts_to_action:             acts_to_action[action.__class__.__name__].append(action)         else:             acts_to_action[action.__class__.__name__] = [action]      # Check if the incoming action is a ReportAct, if it is then check if there is already a ReportAct with the same query     if incoming_action.__class__.__name__ == "ReportAgentAct":         for action in acts_to_action.get("ReportAgentAct", []):             if (                 action.query == incoming_action.query                 and action.message == incoming_action.message             ):                 return False         return True     # Check if the incoming action is a ProposeAct, if it is then check if there is already a ProposeAct with the same query     # or AskAgentAct or AskForConfirmationAct are present     elif incoming_action.__class__.__name__ == "ProposeAgentAct":         if (             "AskAgentAct" in acts_to_action             or "AskForConfirmationAgentAct" in acts_to_action         ):             return False         for action in acts_to_action.get("ProposeAgentAct", []):             if action.params == incoming_action.params and same_worksheet(                 action.ws, incoming_action.ws             ):                 return False         return True     # Check if the incoming action is a AskAgentAct, if other AskAgentAct or ProposeAgentAct or AskForConfirmationAgentAct are present     elif incoming_action.__class__.__name__ == "AskAgentAct":         if (             "ProposeAgentAct" in acts_to_action             or "AskAgentAct" in acts_to_action             or "AskForConfirmationAgentAct" in acts_to_action         ):             return False         return True     # Check if the incoming action is a AskForConfirmationAct, if other AskAgentAct or ProposeAgentAct or AskForConfirmationAgentAct are present     elif incoming_action.__class__.__name__ == "AskForConfirmationAgentAct":         if (             "ProposeAgentAct" in acts_to_action             or "AskAgentAct" in acts_to_action             or "AskForConfirmationAgentAct" in acts_to_action         ):             return False         return True ``` |

###### extend

```
extend(actions)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2158 2159 2160 ``` | ``` def extend(self, actions):     for action in actions:         self._add(action) ``` |

###### \_\_iter\_\_

```
__iter__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2162 2163 ``` | ``` def __iter__(self):     return iter(self.actions) ``` |

###### \_\_next\_\_

```
__next__()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2165 2166 ``` | ``` def __next__(self):     return next(self.actions) ``` |

###### can\_have\_other\_acts

```
can_have_other_acts()
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2168 2169 2170 2171 2172 2173 2174 2175 2176 2177 2178 2179 2180 2181 2182 ``` | ``` def can_have_other_acts(self):     acts_to_action = {}     for action in self.actions:         if action.__class__.__name__ in acts_to_action:             acts_to_action[action.__class__.__name__].append(action)         else:             acts_to_action[action.__class__.__name__] = [action]      if (         "ProposeAgentAct" in acts_to_action         or "AskAgentAct" in acts_to_action         or "AskForConfirmationAgentAct" in acts_to_action     ):         return False     return True ``` |

### Functions

#### validation\_check

```
validation_check(name, value, validation)
```

Validate a value against specified criteria using LLM.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` | The name of the field being validated. | *required* |
| `value` | `Any` | The value to validate. | *required* |
| `validation` | `str` | The validation criteria. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `tuple` |  | A tuple containing: - bool: Whether the value is valid. - str or None: The reason for invalidity, if any. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 ``` | ``` def validation_check(name, value, validation):     """Validate a value against specified criteria using LLM.      Args:         name (str): The name of the field being validated.         value (Any): The value to validate.         validation (str): The validation criteria.      Returns:         tuple: A tuple containing:             - bool: Whether the value is valid.             - str or None: The reason for invalidity, if any.     """     prompt_path = "validation_check.prompt"     if isinstance(value, GenieValue):         val = str(value.value)     else:         val = str(value)     response = llm_generate(         prompt_path,         {             "value": val,             "criteria": validation,             "name": name,         },         model_name="gpt-4o-mini",     )      bs = BeautifulSoup(response, "html.parser")     reason = bs.find("reason")     valid = bs.find("valid")      if valid:         return valid.text.strip().lower() == "true", None     return False, reason.text if reason else None ``` |

#### get\_genie\_fields\_from\_ws

```
get_genie_fields_from_ws(obj: GenieWorksheet) -> list[GenieField]
```

Get all GenieField instances from a GenieWorksheet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `obj` | `GenieWorksheet` | The worksheet to get fields from. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `list[GenieField]` | list[GenieField]: List of GenieField instances. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1404 1405 1406 1407 1408 1409 1410 1411 1412 1413 1414 1415 1416 1417 1418 1419 ``` | ``` def get_genie_fields_from_ws(obj: GenieWorksheet) -> list[GenieField]:     """Get all GenieField instances from a GenieWorksheet.      Args:         obj (GenieWorksheet): The worksheet to get fields from.      Returns:         list[GenieField]: List of GenieField instances.     """     fields = []     for attr in obj._ordered_attributes:         if not attr.startswith("_"):             field = getattr(obj, attr)             if isinstance(field, GenieField):                 fields.append(field)     return fields ``` |

#### execute\_query

```
execute_query(code: str, obj: GenieWorksheet, bot: GenieRuntime, local_context: GenieContext) -> Any
```

Execute a query in the given context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `code` | `str` | The code to execute. | *required* |
| `obj` | `GenieWorksheet` | The worksheet object. | *required* |
| `bot` | `GenieRuntime` | The bot instance. | *required* |
| `local_context` | `GenieContext` | The local context. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `Any` | `Any` | The result of the query execution. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1422 1423 1424 1425 1426 1427 1428 1429 1430 1431 1432 1433 1434 1435 1436 1437 1438 1439 1440 1441 1442 1443 1444 1445 1446 1447 1448 1449 ``` | ``` def execute_query(     code: str, obj: GenieWorksheet, bot: GenieRuntime, local_context: GenieContext ) -> Any:     """Execute a query in the given context.      Args:         code (str): The code to execute.         obj (GenieWorksheet): The worksheet object.         bot (GenieRuntime): The bot instance.         local_context (GenieContext): The local context.      Returns:         Any: The result of the query execution.     """     # refactoring the developer written code     code = modify_action_code(code, obj, bot, local_context)     code_ = f"__return = {code}"     local_context.context["__return"] = None      bot.execute(code_, local_context)      if "_obj" in local_context.context:         del local_context.context["_obj"]      result = local_context.context["__return"]      del local_context.context["__return"]     return result ``` |

#### modify\_action\_code

```
modify_action_code(code, obj, bot, local_context)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1452 1453 1454 1455 1456 1457 1458 1459 1460 1461 1462 1463 1464 1465 1466 1467 1468 1469 1470 1471 1472 1473 1474 1475 1476 1477 1478 1479 1480 1481 1482 1483 1484 1485 1486 1487 1488 ``` | ``` def modify_action_code(code, obj, bot, local_context):     # Pattern to match decorators and their arguments     api_pattern = r"@(\w+)\((.*?)\)"     api_matches = re.findall(api_pattern, code)      inbuilt_pattern = r">(\w+)\((.*?)\)"     inbuilt_matches = re.findall(inbuilt_pattern, code)      def replace_sign(sign, matches, code):         for func_name, args in matches:             if (                 func_name not in bot.context.context                 and func_name not in local_context.context             ):                 continue              # Replace the decorator with the direct function call in the code             code = re.sub(f"{sign}{func_name}", func_name, code)         return code      def replace_self(code):         # Replace 'self.' with 'custom_obj.' to reference the custom object         if isinstance(obj, GenieWorksheet):             local_context.context["_obj"] = obj         elif isinstance(obj, GenieField):             local_context.context["_obj"] = obj.parent         modified_args = code.replace("self.", "_obj" + ".")         modified_args = re.sub(r"self$", "_obj", modified_args)         modified_args = re.sub(r"self}", "_obj" + "}", modified_args)          return modified_args      code = replace_self(code)      code = replace_sign("@", api_matches, code)     code = replace_sign(">", inbuilt_matches, code)     return code ``` |

#### eval\_predicates

```
eval_predicates(predicates: list | str, obj: GenieField | GenieWorksheet, bot: GenieRuntime, local_context: GenieContext) -> bool
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1491 1492 1493 1494 1495 1496 1497 1498 1499 1500 1501 1502 1503 1504 1505 1506 1507 1508 ``` | ``` def eval_predicates(     predicates: list | str,     obj: GenieField | GenieWorksheet,     bot: GenieRuntime,     local_context: GenieContext, ) -> bool:     if predicates is None:         return True     if len(predicates) == 0:         return True     if isinstance(predicates, list):         for predicate in predicates:             if not parse_single_predicate(predicate, obj, bot, local_context):                 return False     else:         if not parse_single_predicate(predicates, obj, bot, local_context):             return False     return True ``` |

#### parse\_single\_predicate

```
parse_single_predicate(predicate: str, obj, bot, context) -> bool
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1511 1512 1513 1514 1515 1516 1517 1518 1519 1520 1521 1522 1523 1524 1525 1526 1527 1528 ``` | ``` def parse_single_predicate(predicate: str, obj, bot, context) -> bool:     if isinstance(predicate, bool):         return predicate     if predicate.upper() == "TRUE":         return True     elif predicate.upper() == "FALSE":         return False     elif predicate == "":         return True      code = modify_action_code(predicate, obj, bot, context)     code = sanitize_dev_code(code, bot.get_all_variables()).strip()      res: bool = bot.eval(code, context)      if "_obj" in context.context:         del context.context["_obj"]     return res ``` |

#### rewrite\_action\_code

```
rewrite_action_code(code, builtin_funcs)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1531 1532 1533 1534 1535 1536 1537 1538 1539 1540 1541 1542 1543 1544 1545 1546 1547 1548 1549 1550 1551 1552 1553 1554 1555 1556 1557 1558 1559 1560 1561 1562 1563 1564 1565 1566 1567 1568 1569 ``` | ``` def rewrite_action_code(code, builtin_funcs):     class CallTransformer(ast.NodeTransformer):         def __init__(self, builtin_funcs) -> None:             super().__init__()             self.builtins = builtin_funcs          def visit_Call(self, node):             # Process the node further before possibly wrapping it             self.generic_visit(node)              # Wrap the function call in a result.append if it's not a built-in function             # Note: you'll need to determine if a function is built-in based on your criteria             if isinstance(node.func, ast.Name) and node.func.id in self.builtins:                 append_call = ast.Expr(                     value=ast.Call(                         func=ast.Attribute(                             value=ast.Name(id="__return", ctx=ast.Load()),                             attr="append",                             ctx=ast.Load(),                         ),                         args=[node],                         keywords=[],                     )                 )                 return append_call             return node      # Parse the code into an AST     tree = ast.parse(code)      # Initialize the transformer and apply it     transformer = CallTransformer(builtin_funcs=builtin_funcs)     transformer.result_added = False     transformed_tree = transformer.visit(tree)      # Fix missing locations in the AST     # Convert the AST back to code     new_code = ast.unparse(ast.fix_missing_locations(transformed_tree))     return new_code ``` |

#### same\_field

```
same_field(field1: GenieField, field2: GenieField)
```

Check if the values and confirmed status are the same for any two GenieField instances.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `field1` | `GenieField` | The first field to compare. | *required* |
| `field2` | `GenieField` | The second field to compare. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `bool` |  | True if the fields are the same, False otherwise. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1572 1573 1574 1575 1576 1577 1578 1579 1580 1581 1582 1583 ``` | ``` def same_field(field1: GenieField, field2: GenieField):     """Check if the values and confirmed status are the same for any two GenieField instances.      Args:         field1 (GenieField): The first field to compare.         field2 (GenieField): The second field to compare.      Returns:         bool: True if the fields are the same, False otherwise.     """      return field1.value == field2.value and field1.confirmed == field2.confirmed ``` |

#### same\_worksheet

```
same_worksheet(ws1: GenieWorksheet, ws2: GenieWorksheet)
```

Check if two GenieWorksheet instances are the same.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ws1` | `GenieWorksheet` | The first worksheet to compare. | *required* |
| `ws2` | `GenieWorksheet` | The second worksheet to compare. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `bool` |  | True if the worksheets are the same, False otherwise. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1586 1587 1588 1589 1590 1591 1592 1593 1594 1595 1596 1597 1598 1599 1600 1601 1602 1603 1604 1605 1606 1607 1608 1609 1610 1611 1612 1613 1614 1615 1616 1617 1618 1619 1620 1621 1622 1623 1624 1625 1626 1627 1628 1629 ``` | ``` def same_worksheet(ws1: GenieWorksheet, ws2: GenieWorksheet):     """Check if two GenieWorksheet instances are the same.      Args:         ws1 (GenieWorksheet): The first worksheet to compare.         ws2 (GenieWorksheet): The second worksheet to compare.      Returns:         bool: True if the worksheets are the same, False otherwise.     """     # If the randomly generated id is different, then the worksheets are different     if hasattr(ws1, "random_id") and hasattr(ws2, "random_id"):         if ws1.random_id != ws2.random_id:             return False      # Check if the fields in both worksheets are the same starting from WS1     for field in get_genie_fields_from_ws(ws1):         for field2 in get_genie_fields_from_ws(ws2):             if field.name == field2.name:                 if type(field.value) is not type(field2.value):                     return False                 if isinstance(field.value, GenieWorksheet) and isinstance(                     field2.value, GenieWorksheet                 ):                     # Recursively check if the worksheets are the same                     # if the value of the current field is a worksheet                     if not same_worksheet(field.value, field2.value):                         return False                 else:                     if not same_field(field, field2):                         return False      # Check if the fields in both worksheets are the same starting from WS2     for field in get_genie_fields_from_ws(ws2):         for field2 in get_genie_fields_from_ws(ws1):             if field.name == field2.name:                 if isinstance(field.value, GenieWorksheet):                     if not same_worksheet(field.value, field2.value):                         return False                 else:                     if not same_field(field, field2):                         return False      return True ``` |

#### count\_number\_of\_vars

```
count_number_of_vars(context: dict)
```

Count the number of variables of the same type in the context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` | `dict` | The context to count variables in. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `dict` |  | A dictionary with variable names as keys and their counts as values. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1632 1633 1634 1635 1636 1637 1638 1639 1640 1641 1642 1643 1644 1645 1646 1647 1648 1649 1650 ``` | ``` def count_number_of_vars(context: dict):     """Count the number of variables of the same type in the context.      Args:         context (dict): The context to count variables in.      Returns:         dict: A dictionary with variable names as keys and their counts as values."""     var_counters = {}     for key, value in context.items():         if isinstance(value, Answer):             continue         if isinstance(value, GenieWorksheet):             var_name = generate_var_name(value.__class__.__name__)             if var_name not in var_counters:                 var_counters[var_name] = -1             var_counters[var_name] += 1      return var_counters ``` |

#### genie\_deepcopy

```
genie_deepcopy(context)
```

Special deepcopy function for Genie context.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1653 1654 1655 1656 1657 1658 1659 1660 1661 1662 1663 1664 1665 ``` | ``` def genie_deepcopy(context):     """Special deepcopy function for Genie context."""     new_context = {}     for key, value in context.items():         if key == "__builtins__":             continue         if isinstance(value, GenieWorksheet):             new_context[key] = deepcopy(value)         elif isinstance(value, GenieField):             new_context[key] = deepcopy(value)         else:             new_context[key] = value     return new_context ``` |

#### get\_field\_variable\_name

```
get_field_variable_name(obj: GenieWorksheet, context: GenieContext)
```

Get the variable name of a field in a worksheet.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `obj` | `GenieWorksheet` | The worksheet object. | *required* |
| `context` | `GenieContext` | The context to search in. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | The variable name of the field. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1668 1669 1670 1671 1672 1673 1674 1675 1676 1677 1678 1679 1680 1681 1682 1683 1684 ``` | ``` def get_field_variable_name(obj: GenieWorksheet, context: GenieContext):     """Get the variable name of a field in a worksheet.      Args:         obj (GenieWorksheet): The worksheet object.         context (GenieContext): The context to search in.      Returns:         str: The variable name of the field.     """     for name, value in context.context.items():         if not inspect.isclass(value) and isinstance(value, GenieWorksheet):             for field in get_genie_fields_from_ws(value):                 if field == obj:                     return name + "." + field.name      return obj ``` |

#### collect\_all\_parents

```
collect_all_parents(context: GenieContext)
```

Collect all parent references for GenieField instances in the context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `context` | `GenieContext` | The context to collect parents from. | *required* |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1687 1688 1689 1690 1691 1692 1693 1694 1695 1696 1697 ``` | ``` def collect_all_parents(context: GenieContext):     """Collect all parent references for GenieField instances in the context.      Args:         context (GenieContext): The context to collect parents from.     """     for key, value in context.context.items():         if isinstance(value, GenieWorksheet):             for field in get_genie_fields_from_ws(value):                 if isinstance(field, GenieField):                     field.parent = value ``` |

#### find\_all\_variables\_matching\_name

```
find_all_variables_matching_name(field_name: str, context: GenieContext)
```

Go through all the variables in the context recursively and return the variables that match the field\_name

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1700 1701 1702 1703 1704 1705 1706 1707 1708 1709 1710 1711 1712 1713 1714 1715 ``` | ``` def find_all_variables_matching_name(field_name: str, context: GenieContext):     """Go through all the variables in the context recursively and return the variables that match the field_name"""     variables = []      def find_matching_variables(obj, field_name, key):         for field in get_genie_fields_from_ws(obj):             if field.name == field_name:                 variables.append(key + "." + field_name)             # if isinstance(field.value, GenieWorksheet):             # find_matching_variables(field.value, field_name, key + "." + field.name)      for key, value in context.context.items():         if isinstance(value, GenieWorksheet):             find_matching_variables(value, field_name, key)      return variables ``` |

#### replace\_undefined\_variables

```
replace_undefined_variables(code: str, local_context: GenieContext, global_context: GenieContext)
```

Replace undefined variables in the code with their corresponding values from the context.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1718 1719 1720 1721 1722 1723 1724 1725 1726 1727 1728 1729 1730 1731 1732 1733 1734 1735 1736 1737 1738 1739 1740 1741 1742 1743 1744 1745 1746 1747 1748 1749 1750 1751 1752 1753 1754 1755 1756 1757 1758 1759 1760 1761 1762 1763 1764 1765 1766 1767 1768 1769 1770 1771 1772 1773 1774 1775 1776 1777 1778 ``` | ``` def replace_undefined_variables(     code: str, local_context: GenieContext, global_context: GenieContext ):     """Replace undefined variables in the code with their corresponding values from the context."""      class ReplaceVariables(ast.NodeTransformer):         def visit_Name(self, node):             if node.id in local_context.context:                 if isinstance(local_context.context[node.id], GenieField):                     if node.id.endswith(".value"):                         name = node.id                     else:                         name = node.id + ".value"                     return ast.copy_location(                         ast.Name(                             id=name,                             ctx=node.ctx,                         ),                         node,                     )             elif node.id in global_context.context:                 if isinstance(global_context.context[node.id], GenieField):                     if node.id.endswith(".value"):                         name = node.id                     else:                         name = node.id + ".value"                     return ast.copy_location(                         ast.Name(                             id=name,                             ctx=node.ctx,                         ),                         node,                     )             else:                 replacement_var = variable_resolver(                     node.id, global_context, local_context                 )                 if replacement_var:                     if replacement_var.endswith(".value"):                         name = replacement_var                     else:                         name = replacement_var + ".value"                     return ast.copy_location(                         ast.Name(                             id=name,                             ctx=node.ctx,                         ),                         node,                     )             return node      # Parse the code into an AST     tree = ast.parse(code)      # Modify the AST     tree = ReplaceVariables().visit(tree)      # Convert back to source code     code = ast.unparse(tree)     code = code.replace(".value.value", ".value")     return code ``` |

#### variable\_resolver

```
variable_resolver(var_name, global_context, local_context)
```

We need to resolve the variable name since they are stored as . in the context
and the user only provides the field name. We also need to keep track of the latest object of a worksheet
so that we can resolve the variable name correctly.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1781 1782 1783 1784 1785 1786 1787 1788 1789 1790 1791 1792 1793 1794 1795 1796 1797 1798 1799 1800 1801 ``` | ``` def variable_resolver(var_name, global_context, local_context):     """We need to resolve the variable name since they are stored as <obj_name>.<field_name> in the context     and the user only provides the field name. We also need to keep track of the latest object of a worksheet     so that we can resolve the variable name correctly.     """     if var_name in local_context.context:         return var_name     elif var_name in global_context.context:         return var_name     else:         candidates = find_all_variables_matching_name(var_name, local_context)          if len(candidates) == 0:             candidates = find_all_variables_matching_name(var_name, global_context)          if len(candidates) == 1:             return candidates[0]         elif len(candidates) > 1:             logger.info(f"Could not resolve the variable name {var_name}.")             logger.info(f"Found multiple candidates: {candidates}")             return candidates[0] ``` |

#### select\_variable\_from\_list

```
select_variable_from_list(variables, value)
```

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1804 1805 1806 1807 1808 1809 ``` | ``` def select_variable_from_list(variables, value):     for var in variables:         if same_worksheet(var, value):             return generate_var_name(value.__class__.__name__)      return None ``` |

#### get\_variable\_name

```
get_variable_name(obj: GenieWorksheet, context: GenieContext)
```

Get the variable name of a worksheet in the context.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `obj` | `GenieWorksheet` | The worksheet object. | *required* |
| `context` | `GenieContext` | The context to search in. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | The variable name of the worksheet. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1812 1813 1814 1815 1816 1817 1818 1819 1820 1821 1822 1823 1824 1825 1826 1827 1828 1829 1830 1831 1832 1833 1834 1835 1836 1837 1838 1839 1840 1841 ``` | ``` def get_variable_name(obj: GenieWorksheet, context: GenieContext):     """Get the variable name of a worksheet in the context.      Args:         obj (GenieWorksheet): The worksheet object.         context (GenieContext): The context to search in.      Returns:         str: The variable name of the worksheet.     """     potential_objs = []     if isinstance(obj, GenieWorksheet):         for name, value in context.context.items():             if not inspect.isclass(value) and isinstance(value, GenieWorksheet):                 if value.__class__.__name__ == obj.__class__.__name__:                     potential_objs.append((name, value))      if len(potential_objs) == 1:         return potential_objs[0][0]     elif len(potential_objs) > 1:         for name, value in potential_objs:             fields_value = [(f.name, f.value) for f in get_genie_fields_from_ws(value)]             obj_fields_value = [                 (f.name, f.value) for f in get_genie_fields_from_ws(obj)             ]              if deep_compare_lists(fields_value, obj_fields_value):                 return name      return obj ``` |

#### propose

```
propose(worksheet: GenieWorksheet, params: dict) -> ProposeAgentAct
```

Create a proposal action.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `worksheet` | `GenieWorksheet` | The worksheet to propose values for. | *required* |
| `params` | `dict` | The parameters to propose. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `ProposeAgentAct` | `ProposeAgentAct` | The created proposal action. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1847 1848 1849 1850 1851 1852 1853 1854 1855 1856 1857 ``` | ``` def propose(worksheet: GenieWorksheet, params: dict) -> ProposeAgentAct:     """Create a proposal action.      Args:         worksheet (GenieWorksheet): The worksheet to propose values for.         params (dict): The parameters to propose.      Returns:         ProposeAgentAct: The created proposal action.     """     return ProposeAgentAct(worksheet(**params), params) ``` |

#### say

```
say(message: str) -> ReportAgentAct
```

Create a message report action.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `message` | `str` | The message to report. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `ReportAgentAct` | `ReportAgentAct` | The created report action. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1860 1861 1862 1863 1864 1865 1866 1867 1868 1869 ``` | ``` def say(message: str) -> ReportAgentAct:     """Create a message report action.      Args:         message (str): The message to report.      Returns:         ReportAgentAct: The created report action.     """     return ReportAgentAct(None, message) ``` |

#### generate\_clarification

```
generate_clarification(worksheet: GenieWorksheet, field: str) -> str
```

Generate clarification text for a field.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `worksheet` | `GenieWorksheet` | The worksheet containing the field. | *required* |
| `field` | `str` | The name of the field. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | The generated clarification text. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1872 1873 1874 1875 1876 1877 1878 1879 1880 1881 1882 1883 1884 1885 1886 1887 1888 1889 1890 1891 ``` | ``` def generate_clarification(worksheet: GenieWorksheet, field: str) -> str:     """Generate clarification text for a field.      Args:         worksheet (GenieWorksheet): The worksheet containing the field.         field (str): The name of the field.      Returns:         str: The generated clarification text.     """     for f in get_genie_fields_from_ws(worksheet):         if f.name == field:             if inspect.isclass(f.slottype) and issubclass(f.slottype, Enum):                 options = [x.name for x in list(f.slottype.__members__.values())]                 options = ", ".join(options)                 option_desc = f.description + f" Options are: {options}"                 return option_desc             return f.description      return "" ``` |

#### answer\_clarification\_question

```
answer_clarification_question(worksheet: GenieField, field: GenieField, context: GenieContext) -> ReportAgentAct
```

Create a clarification answer action.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `worksheet` | `GenieField` | The worksheet field. | *required* |
| `field` | `GenieField` | The field to clarify. | *required* |
| `context` | `GenieContext` | The context. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `ReportAgentAct` | `ReportAgentAct` | The created clarification report action. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1894 1895 1896 1897 1898 1899 1900 1901 1902 1903 1904 1905 1906 1907 1908 1909 1910 1911 ``` | ``` def answer_clarification_question(     worksheet: GenieField, field: GenieField, context: GenieContext ) -> ReportAgentAct:     """Create a clarification answer action.      Args:         worksheet (GenieField): The worksheet field.         field (GenieField): The field to clarify.         context (GenieContext): The context.      Returns:         ReportAgentAct: The created clarification report action.     """     ws = context.context[worksheet.value]     return ReportAgentAct(         f"AskClarification({worksheet.value}, {field.value})",         generate_clarification(ws, field.value),     ) ``` |

#### confirm

```
confirm(value: Any) -> GenieValue
```

Create a confirmed value.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `value` | `Any` | The value to confirm. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `GenieValue` | `GenieValue` | The confirmed value instance. |

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 1914 1915 1916 1917 1918 1919 1920 1921 1922 1923 1924 1925 ``` | ``` def confirm(value: Any) -> GenieValue:     """Create a confirmed value.      Args:         value (Any): The value to confirm.      Returns:         GenieValue: The confirmed value instance.     """     if isinstance(value, GenieValue):         return value.confirm()     return GenieValue(value).confirm() ``` |

#### sanitize\_dev\_code

```
sanitize_dev_code(code: str, all_variables: list[str])
```

Sanitize the developer's code to ensure it doesn't contain any undefined variables.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2185 2186 2187 2188 2189 2190 2191 2192 2193 2194 2195 2196 2197 ``` | ``` def sanitize_dev_code(code: str, all_variables: list[str]):     """Sanitize the developer's code to ensure it doesn't contain any undefined variables."""     lexer = PythonLexer()     tokens = lexer.get_tokens(code)     new_tokens_list = []     for token in tokens:         if token[0] == Token.Name and token[1] in all_variables:             new_tokens_list.append((Token.Name, token[1] + ".value"))         else:             new_tokens_list.append(token)      new_code = tokenize.untokenize(new_tokens_list)     return new_code ``` |

#### any\_open\_empty\_ws

```
any_open_empty_ws(turn_context: GenieContext, global_context: GenieContext)
```

Checks all the worksheets in the context. If there is any worksheet that is available but all the fields are None, then return True
else return False

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2200 2201 2202 2203 2204 2205 2206 2207 2208 2209 2210 2211 2212 2213 2214 2215 2216 2217 2218 2219 2220 2221 2222 2223 2224 2225 2226 ``` | ``` def any_open_empty_ws(turn_context: GenieContext, global_context: GenieContext):     """Checks all the worksheets in the context. If there is any worksheet that is available but all the fields are None, then return True     else return False     """     for key, value in turn_context.context.items():         if isinstance(value, GenieWorksheet):             all_none = True             for field in get_genie_fields_from_ws(value):                 if field.value is not None:                     all_none = False                     break              if all_none:                 return True      for key, value in global_context.context.items():         if isinstance(value, GenieWorksheet):             all_none = True             for field in get_genie_fields_from_ws(value):                 if field.value is not None:                     all_none = False                     break              if all_none:                 return True      return False ``` |

#### find\_list\_variable

```
find_list_variable(val, context)
```

Find the variable name which is a list and the index of the required value in the context.

Source code in `src/worksheets/environment.py`

|  |  |
| --- | --- |
| ``` 2229 2230 2231 2232 2233 2234 2235 2236 ``` | ``` def find_list_variable(val, context):     """Find the variable name which is a list and the index of the required value in the context."""     for key, value in context.context.items():         if isinstance(value, list):             for idx, v in enumerate(value):                 if v == val:                     return key, str(idx)     return None, None ``` |

Back to top
