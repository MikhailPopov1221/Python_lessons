# import time 



# x = 1
# while True:
#     print(x)
#     if x == 100:
#         break
#     x = x + 1
#     time.sleep(1)
# print("Конец")


# inp = int(input("Введите свой возраст: "))
# while inp < 18:
#     print("Вход невозможен")
#     inp = int(input("Введите свой возраст: "))
    
# print("Вход разрешен")

x = 0
while x < 100:
    x = x + 1
    if x % 2 == 1:
        continue
    print(x)