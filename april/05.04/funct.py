def hello(name):
    return f'Привет {name}!'

s1 = hello("Вася")
print(s1)

s2 = hello
print(s2)
print(s2("Петя"))
print(hello("Петя"))
