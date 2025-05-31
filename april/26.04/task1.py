'''
-> '123'
<- один два три
'''
numbers = {
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    0: "ноль",
}

inp = input("Введите любое целое число: ")
# out = list(map(lambda x: numbers[int(x)], inp))
out = [numbers[int(i)] for i in inp]
print(*out)
