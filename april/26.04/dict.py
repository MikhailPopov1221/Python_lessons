capitals = {"Russia":"Moscow", "Great Britan": "London", "Spain": "Madrid"}
print(capitals)
print(f"Столицей России является {capitals['Russia']}")

capitals = dict(Russia="Moscow", Great_Britan="London", Spain="Madrid")
print(capitals)

capitals = dict([("Russia","Moscow"), ("Great Britan","London"), ("Spain","Madrid")])
# print(capitals)

# for i in capitals:
#     print(i)
    
# for key in capitals:
#     print(capitals[key])
    
# for key in capitals:
#     print(key, capitals[key])
    
for key in capitals.keys():
    print(key)
    
for value in capitals.values():
    print(value)
    
for item in capitals.items():
    print(item)

for key, value in capitals.items():
    print(key, value)
    
    
capitals = {0:"Moscow", 0: "London", 2: "Madrid"}
print(capitals[0])

# capitals = {(1,2,3):"Moscow", (1,22,33): "London", (11,22,22): "Madrid"}
# print(capitals[(1,2,3)])


# capitals = {[1,2,3]:"Moscow", (1,22,33): "London", (11,22,22): "Madrid"}
# print(capitals[(1,2,3)])