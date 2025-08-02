import json

data = {
    "name" : "Sharik",
    "age": 3,
    "color": 'green'
    }

with open("2.json", 'w', encoding="utf-8") as fl:
    json.dump(data, fl)