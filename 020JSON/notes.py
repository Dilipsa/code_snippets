"""
JSON
========
JSON (JavaScript Object Notation) is a lightweight data interchange format that is used to transmit data 
between a server and a client, or to store data in a text format. JSON is easy for humans to read and write, 
and it's also easy for machines to parse and generate.

JSON Data Types
================
Following are the JSON data types and which is mapped with python datatypes.

| JSON Data Type | JSON Representation | Python Data Type | Python Representation  |
|----------------|---------------------|------------------|------------------------|
| String         | "string"            | str              | 'string'               |
| Number         | 42, 3.14            | int, float       | 42, 3.14               |
| Boolean        | true, false         | bool             | True, False            |
| Null           | null                | None             | None                   |
| Object         | {"key": "value"}    | dict             | {'key': 'value'}       |
| Array          | [1, 2, 3]           | list             | [1, 2, 3]              |

Examples:
====================================================================================
1] => JSON String:
=================
{"name": "Dilip Sapkota}

2] => JSON Number:
=================
{"age": 40}

3] => JSON Boolean:
================
{"result" : true}

4] => JSON Null:
================
{"result" : true,"grade" : null, "rollno" : 210}

5] => JSON Object:
=================
{"name":"Dilip","age":40, "mobile": 8989898989}

6] => JSON Array:
================
{"fruits":[ "Apple", "Vanana", "Cherry"]}



Convert from JSON to Python object
====================================
"""

import json 
  
# JSON string 
employee = '{"id":"09", "name": "Dilip", "department":"Development"}'
print("JSON data", type(employee))        # JSON data <class 'str'>
  
# Convert string to Python dict 
employee_dict = json.loads(employee) 
print("Python data", type(employee_dict)) # Python data <class 'dict'>
print(employee_dict)             # {'id': '09', 'name': 'Dilip', 'department': 'Development'}


"""
Convert from Python object to JSON
"""

import json 

# JSON string 
employee_dict = {'id': '09', 'name': 'Dilip', 'department': 'Development'} 
print("Python type ", type(employee_dict))  # Python type  <class 'dict'>

# Convert Python dict to JSON 
json_object = json.dumps(employee_dict, indent=4) 
print("Converted to JSON", type(json_object))   # Converted to JSON <class 'str'>
print(json_object)  
# prints 
# {
#   "id": "09",
#   "name": "Dilip",
#   "department": "Development"
# }
