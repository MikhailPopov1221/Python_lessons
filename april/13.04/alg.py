lst = [6, 465, 564, 32, 78, 123, 2, 464, 5, 66]
print(lst)

n = len(lst)
for i in range(n):
    is_changed = False
    for j in range(n - 1- i):
        if lst[j] > lst[j + 1]:
            is_changed =True
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp
    if is_changed == False:
        break 
    print(lst)