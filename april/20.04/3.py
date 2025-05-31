number1 = 124110
number2 = 123456

stroka = str(number1)
if len(stroka) == len(set(stroka)):
    print("Повторов нет")
else:
    print("Повторы есть")