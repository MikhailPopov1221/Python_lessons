def is_simple_number(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

lst = [23, 7, 13, 4, 55, 7567, 345, 435, 2345, 435]
lst_2 = list(filter(is_simple_number, lst))
print(lst_2)
