num = int(input("Введите любое целое число: "))
new_num = 0
while num != 0:
    new_num = new_num * 10 + num % 10
    num = num // 10  
print(new_num)
