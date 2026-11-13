# Project code: stanford-oval/genie-worksheets: web/docs/api/from_spreadsheet/index.html

[Course index](../../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/docs/api/from_spreadsheet/index.html) · [Raw file](../../../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/api/from_spreadsheet/index.html)

Retrieved: 2026-11-13T17:06:24.900930+00:00

# From Spreadsheet

## src.worksheets.from\_spreadsheet

### Attributes

#### gsheet\_range\_default `module-attribute`

```
gsheet_range_default = 'A1:AD1007'
```

#### FORM\_PREDICATE `module-attribute`

```
FORM_PREDICATE = 0
```

#### FORM\_NAME `module-attribute`

```
FORM_NAME = 1
```

#### FIELD\_PREDICATE `module-attribute`

```
FIELD_PREDICATE = 2
```

#### KIND `module-attribute`

```
KIND = 3
```

#### FIELD\_TYPE `module-attribute`

```
FIELD_TYPE = 4
```

#### FIELD\_NAME `module-attribute`

```
FIELD_NAME = 5
```

#### VARIABLE\_ENUMS `module-attribute`

```
VARIABLE_ENUMS = 6
```

#### FIELD\_DESCRIPTION `module-attribute`

```
FIELD_DESCRIPTION = 7
```

#### DONT\_ASK `module-attribute`

```
DONT_ASK = 8
```

#### REQUIRED `module-attribute`

```
REQUIRED = 9
```

#### FIELD\_CONFIRMATION `module-attribute`

```
FIELD_CONFIRMATION = 10
```

#### FIELD\_ACTION `module-attribute`

```
FIELD_ACTION = 11
```

#### FORM\_ACTION `module-attribute`

```
FORM_ACTION = 12
```

#### FIELD\_VALIDATION `module-attribute`

```
FIELD_VALIDATION = 13
```

#### EMPTY\_COL `module-attribute`

```
EMPTY_COL = 14
```

#### str\_to\_type `module-attribute`

```
str_to_type = {'str': str, 'int': int, 'float': float, 'bool': bool, 'date': date, 'time': time}
```

### Functions

#### gsheet\_to\_classes

```
gsheet_to_classes(gsheet_id, gsheet_range=gsheet_range_default)
```

Convert Google Sheets data to Genie classes.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `gsheet_id` | `str` | The ID of the Google Sheet. | *required* |
| `gsheet_range` | `str` | The range of cells to retrieve. | `gsheet_range_default` |

Yields:

| Type | Description |
| --- | --- |
|  | Tuple[str, type]: The type of the class and the class itself. |

Source code in `src/worksheets/from_spreadsheet.py`

|  |  |
| --- | --- |
| ```  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 ``` | ``` def gsheet_to_classes(gsheet_id, gsheet_range=gsheet_range_default):     """Convert Google Sheets data to Genie classes.      Args:         gsheet_id (str): The ID of the Google Sheet.         gsheet_range (str): The range of cells to retrieve.      Yields:         Tuple[str, type]: The type of the class and the class itself."""     rows = retrieve_gsheet(gsheet_id, gsheet_range)     if not rows:         raise ValueError("No data found.")      rows = fill_all_empty(rows, EMPTY_COL + 1)      # removing headers from the CSV     rows = rows[1:]      # strip all the cells     rows = [[cell.strip() for cell in row] for row in rows]      # collecting all the rows     forms = []     i = 0     while i < len(rows):         enums = []         if len(rows[i][FORM_NAME]):             forms.append(                 {                     "form": rows[i],                     "fields": [],                     "outputs": [],                 }             )         else:             if rows[i][FIELD_TYPE] == "Enum":                 enum_idx = i + 1                 while (                     enum_idx < len(rows)                     and not len(rows[enum_idx][FIELD_TYPE].strip())                     and not len(rows[enum_idx][FIELD_NAME].strip())                 ):                     enums.append(rows[enum_idx][VARIABLE_ENUMS])                     enum_idx += 1              if rows[i][KIND] == "output":                 forms[-1]["outputs"].append({"slottype": rows[i][FIELD_TYPE]})             else:                 forms[-1]["fields"].append(                     {                         "slottype": (                             rows[i][FIELD_TYPE]                             if rows[i][FIELD_TYPE] != "Enum"                             else create_enum_class(rows[i][FIELD_NAME], enums)                         ),                         "name": rows[i][FIELD_NAME],                         "description": rows[i][FIELD_DESCRIPTION],                         "predicate": rows[i][FIELD_PREDICATE],                         "ask": not rows[i][DONT_ASK] == "TRUE",                         "optional": not rows[i][REQUIRED] == "TRUE",                         "actions": Action(rows[i][FIELD_ACTION]),                         "value": None,                         "requires_confirmation": rows[i][FIELD_CONFIRMATION] == "TRUE",                         "internal": False if rows[i][KIND].lower() == "input" else True,                         "primary_key": (                             True if "primary" in rows[i][KIND].lower() else False                         ),                         "validation": (                             None                             if len(rows[i][FIELD_VALIDATION].strip()) == 0                             else rows[i][FIELD_VALIDATION]                         ),                     }                 )         if len(enums):             i = enum_idx         else:             i += 1      # creating the genie worksheet     for form in forms:         class_name = form["form"][FORM_NAME].replace(" ", "")         form_predicate = form["form"][FORM_PREDICATE]         form_action = Action(form["form"][FORM_ACTION])         backend_api = form["form"][FIELD_NAME]         outputs = form["outputs"]         fields = form["fields"]         genie_type = form["form"][FIELD_TYPE].lower()         yield create_class(             class_name,             fields,             genie_type,             form_predicate,             form_action,             backend_api,             outputs,         ) ``` |

#### create\_class

```
create_class(class_name, fields, genie_type, form_predicate, form_action, backend_api, outputs)
```

Create a class dynamically based on the provided parameters.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `class_name` | `str` | The name of the class to create. | *required* |
| `fields` | `list` | A list of field dictionaries. | *required* |
| `genie_type` | `str` | The type of the Genie class (worksheet, db, type). | *required* |
| `form_predicate` | `str` | The predicate for the form. | *required* |
| `form_action` | `Action` | The action associated with the form. | *required* |
| `backend_api` | `str` | The backend API associated with the form. | *required* |
| `outputs` | `list` | A list of output dictionaries. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | Tuple[str, type]: The type of the class and the class itself. |

Source code in `src/worksheets/from_spreadsheet.py`

|  |  |
| --- | --- |
| ``` 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 ``` | ``` def create_class(     class_name,     fields,     genie_type,     form_predicate,     form_action,     backend_api,     outputs, ):     """Create a class dynamically based on the provided parameters.      Args:         class_name (str): The name of the class to create.         fields (list): A list of field dictionaries.         genie_type (str): The type of the Genie class (worksheet, db, type).         form_predicate (str): The predicate for the form.         form_action (Action): The action associated with the form.         backend_api (str): The backend API associated with the form.         outputs (list): A list of output dictionaries.      Returns:         Tuple[str, type]: The type of the class and the class itself."""      # Create a dictionary for class attributes     class_dict = {}     for field_dict in fields:         # Here, you would handle custom field types or validations         class_dict[field_dict["name"]] = GenieField(**field_dict)      if genie_type == "worksheet":         class_dict["predicate"] = form_predicate         class_dict["outputs"] = [output["slottype"] for output in outputs]         class_dict["actions"] = form_action         class_dict["backend_api"] = backend_api         return (genie_type, type(class_name, (GenieWorksheet,), class_dict))     elif genie_type == "db":         class_dict["outputs"] = [output["slottype"] for output in outputs]         class_dict["actions"] = form_action         return (genie_type, type(class_name, (GenieDB,), class_dict))     elif genie_type == "type":         class_dict["predicate"] = form_predicate         class_dict["actions"] = form_action         return (genie_type, type(class_name, (GenieType,), class_dict)) ``` |

#### create\_enum\_class

```
create_enum_class(class_name, enums)
```

Create an Enum class dynamically

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `class_name` | `str` | The name of the Enum class. | *required* |
| `enums` | `list` | A list of enum values. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `Enum` |  | The created Enum class. |

Source code in `src/worksheets/from_spreadsheet.py`

|  |  |
| --- | --- |
| ``` 181 182 183 184 185 186 187 188 189 190 191 192 ``` | ``` def create_enum_class(class_name, enums):     """Create an Enum class dynamically      Args:         class_name (str): The name of the Enum class.         enums (list): A list of enum values.      Returns:         Enum: The created Enum class."""      enums = [e.strip() for e in enums if len(e.strip())]     return Enum(convert_snake_to_camel_case(class_name), enums) ``` |

#### convert\_snake\_to\_camel\_case

```
convert_snake_to_camel_case(snake_str: str)
```

Convert a snake\_case string to camelCase.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `snake_str` | `str` | The snake\_case string to convert. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `str` |  | The converted camelCase string. |

Source code in `src/worksheets/from_spreadsheet.py`

|  |  |
| --- | --- |
| ``` 195 196 197 198 199 200 201 202 203 204 205 ``` | ``` def convert_snake_to_camel_case(snake_str: str):     """Convert a snake_case string to camelCase.      Args:         snake_str (str): The snake_case string to convert.      Returns:         str: The converted camelCase string.     """     components = snake_str.split("_")     return components[0] + "".join(x.title() for x in components[1:]) ``` |

#### gsheet\_to\_genie

```
gsheet_to_genie(gsheet_id, gsheet_range=gsheet_range_default)
```

Convert Google Sheets data to Genie componenets that are used to create the agent

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `gsheet_id` | `str` | The ID of the Google Sheet. | *required* |
| `gsheet_range` | `str` | The range of cells to retrieve. | `gsheet_range_default` |

Returns:

| Type | Description |
| --- | --- |
|  | Tuple[List[GenieWorksheet], List[GenieDB], List[GenieType]]: The lists of Genie components. |

Source code in `src/worksheets/from_spreadsheet.py`

|  |  |
| --- | --- |
| ``` 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 ``` | ``` def gsheet_to_genie(     gsheet_id,     gsheet_range=gsheet_range_default, ):     """Convert Google Sheets data to Genie componenets that are used to create the agent      Args:         gsheet_id (str): The ID of the Google Sheet.         gsheet_range (str): The range of cells to retrieve.      Returns:         Tuple[List[GenieWorksheet], List[GenieDB], List[GenieType]]: The lists of Genie components.     """     genie_worsheets = []     genie_worsheets_names = {}     genie_dbs = []     genie_dbs_names = {}     genie_types = []     genie_types_names = {}     for genie_type, cls in gsheet_to_classes(gsheet_id, gsheet_range):         if genie_type == "worksheet":             genie_worsheets.append(cls)             genie_worsheets_names[cls.__name__] = cls         elif genie_type == "db":             genie_dbs.append(cls)             genie_dbs_names[cls.__name__] = cls         elif genie_type == "type":             genie_types.append(cls)             genie_types_names[cls.__name__] = cls      for worksheet in genie_worsheets + genie_dbs + genie_types:         for field in get_genie_fields_from_ws(worksheet):             if isinstance(field.slottype, str):                 if field.slottype in str_to_type:                     field.slottype = str_to_type[field.slottype]                 elif field.slottype == "confirm":                     field.slottype = "confirm"                 elif field.slottype == "Enum":                     field.slottype = Enum(field.name, field.slottype[1])                 elif field.slottype.startswith("List"):                     if field.slottype[5:-1] in genie_types_names:                         field.slottype = List[genie_types_names[field.slottype[5:-1]]]                     elif field.slottype[5:-1] in genie_dbs_names:                         field.slottype = List[genie_dbs_names[field.slottype[5:-1]]]                     elif field.slottype[5:-1] in genie_worsheets_names:                         field.slottype = List[                             genie_worsheets_names[field.slottype[5:-1]]                         ]                     else:                         if field.slottype[5:-1] in str_to_type:                             field.slottype = List[str_to_type[field.slottype[5:-1]]]                         else:                             raise ValueError(f"Unknown type {field.slottype}")                 elif field.slottype in genie_types_names:                     field.slottype = genie_types_names[field.slottype]                 elif field.slottype in genie_dbs_names:                     field.slottype = genie_dbs_names[field.slottype]                 elif field.slottype in genie_worsheets_names:                     field.slottype = genie_worsheets_names[field.slottype]                 else:                     raise ValueError(f"Unknown type {field.slottype}")      for ws in genie_dbs + genie_worsheets:         for output in ws.outputs:             if output in genie_worsheets_names:                 ws.outputs[ws.outputs.index(output)] = genie_worsheets_names[output]             elif output in genie_types_names:                 ws.outputs[ws.outputs.index(output)] = genie_types_names[output]             else:                 raise ValueError(f"Unknown type {output}")      return genie_worsheets, genie_dbs, genie_types ``` |

Back to top
