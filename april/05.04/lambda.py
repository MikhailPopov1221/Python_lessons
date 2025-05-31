# def divide_by_2(number):
#     return number/2

# lst = [234, 352, 45, 66, 567]
# lst = list(map(divide_by_2, lst))
# print(lst)
        
        
# lambda number: number/2


lst = [234, 352, 45, 66, 567]
lst = list(map(lambda number: number/2, lst))
print(lst)

my_func = lambda x: x/2

print(my_func(1200))


        