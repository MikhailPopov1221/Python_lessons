num1 = 123 # {1,2,3}
num2 = 445

if set(str(num1)) & set(str(num2)):
    print("Есть пересечение")
else:
    print("Пересечений нет")