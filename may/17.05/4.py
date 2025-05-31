print("Введите любое число: ")
try:
    number = int(input())
    print(2 * number)
    print(2 / number)
    print(2 + number)
    print(2 - number)
    dct = {
        [1,2,3]: "start",
    }
    
except ValueError:
    print("Введены некорректные данные")
   
except ZeroDivisionError:
    print("Ошибка деления на ноль")
    
except:
    print("Какая то ошибка")
    
# print(number)