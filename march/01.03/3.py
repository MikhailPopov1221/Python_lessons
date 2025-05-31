a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if (a > b and a > c):
    if (b > c):
        print(b)
    else:
        print(c) 
elif (b > c and b > a):
    if (a > c):
        print(a)
    else:
        print(c)
else:
    if (a > b):
        print(a)
    else:
        print(b)
        
        

    