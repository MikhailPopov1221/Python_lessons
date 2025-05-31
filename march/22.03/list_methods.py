ls = [12, 22, 44, 54, 9]
ns = [0, 0, 7]

# print(len(ls))
# print(max(ls))
# print(min(ls))
# print(sum(ls))
# print(sorted(ls))
# print(sorted(ls,reverse=True))

# print(ls + ns)
# print(ls * 2)


# Методы списка
ls.append(55)
ls.append(ns)
print(ls[-1][2])


print(ls)
ls.insert(1, "привет")
ls.insert(5, "привет")
print(ls)


ls.remove("привет")
print(ls)

x = ls.pop()
print(x)
print(ls)
ls.pop(4)
print(ls)


ls.append(22)
print(ls)
print(ls.index(22))

print(ls.count(22))

# ls.sort()
# print(ls)

print(ls)
ls.reverse()
print(ls)

# ls.clear()
# print(ls)


print(ls)
print(55 in ls)
print(100 in ls)

ls = []
ls = [1, 3, 4]
ls = list()

s = "Мама мыла раму"
ls = list(s)
print(ls)
ls = s.split()
print(ls)
l = "Яблоко,персик,банан"
ls = l.split(",")
print(ls)
