def show_odd(start, end):
    for i in range(start + 1, end):
        if i % 2 != 0:
            print(i, end=" ")
            
start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
show_odd(start, end)