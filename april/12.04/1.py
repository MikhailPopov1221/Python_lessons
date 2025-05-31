lst = [10, 12, 13, "apple", 15, True, 34]

for elem in lst:
    print(elem)
    
print(lst)

# for i in range(len(lst)):
#     print(i)
    
for i in range(len(lst)):
    lst = i + 10

print(lst)  