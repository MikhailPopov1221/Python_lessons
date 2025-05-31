count = 10
real_pass = 25
user_input = 0

while count > 0:
    user_input = int(input("Введите пароль: "))
    count -= 1     # count = count - 1
    if user_input == real_pass:
        print("Пароль верный. Доступ получен!")
        break
    else:
        print("Пароль неверный. Доступ запрещен!")
        print("Осталось попыток: ", count)
 
if (user_input == real_pass):   
    print("Осуществляем вход в систему")
else:
    print("Вы израсходовали все попытки, доступ к аккаунту заблокирован")


    











