import json

file = '64KB.json'

with open(file, 'r', encoding="utf-8") as fl:
    data = json.load(fl)
    for d in data:
        if d["language"] == "Hindi":
            print(d["name"], d["id"])