import json

data = {
    "name" : "Sharik",
    "age": 3,
    "color": 'green'
    }

json_data = json.dumps(data)
print(json_data)