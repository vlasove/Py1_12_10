import json 

data = {
    "name" : "Bob",
    "is_valid": True,
    "chars" : ["Char1", "Char2", "Char3", {"one": 1, "two":2}],
    "location" : None,
    "age" : 29,
}

result = json.dumps(data, indent=4) # dump + string
print(result)

from_str = json.loads(result)
print(from_str , type(from_str))