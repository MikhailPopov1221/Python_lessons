st1 = {0,1,2,3,4,5,6}
st2 = {5,6,7,8,9}
print(st1)
print(st2)

# объединение
# st3 = st1.union(st2)
# print(st3)
# st4 = st1 | st2
# print(st4)


# пересечение
# st3 = st1.intersection(st2)
# print(st3)

# st4 = st1 & st2
# print(st4)

# разность
# st3 = st1.difference(st2)
# print(st3)

# st4 = st1 - st2
# print(st4)

# st1 - st2 != st2 - st1


# Симметричная разность

st3 = st1.symmetric_difference(st2)
print(st3)

st4 = st1 ^ st2
print(st4)
# st1 ^ st2 == st2 ^ st1