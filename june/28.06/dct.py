dct = {
    "a": 1,
    "b": 2,
    "c": 3
}

dct["d"] = 4

k = list(dct.keys())
v = list(dct.values())

print("Список ключей:", k)
print("Список значений:", *list(dct.values()))

new_dct = {}

for k,v in dct.items():
    new_dct[v] = k

print(new_dct)
