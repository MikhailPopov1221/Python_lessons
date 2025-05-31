import random as r

# for i in range(5):
#     print(r.random())

# for i in range(5):
#     print(r.randrange(90, 100,2))

# for i in range(5):
#     print(r.randint(90, 100))


lst = [i for i in range(10)]
print(r.choice(lst))


print(r.sample(lst,3))
