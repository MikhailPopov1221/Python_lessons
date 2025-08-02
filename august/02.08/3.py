import json


json_data = '{"name": "Sharik", "age": 3, "color": "green"}'

data = json.loads(json_data)

print(data["name"])
print(type(data))