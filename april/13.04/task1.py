fruit = ("apple", "banana", "orange", "lemon", "apple", "apple", "lemon")

user_choice = input("Введите название фрукта:  ")
count = fruit.count(user_choice)

if count:
    print(f"{user_choice} встречается в кортеже {count} раз")
else:
    print("Такого у нас нет")
    
# print(bool([]))
# print(bool([0]))
# print(bool([""]))
# print(bool([1,2]))
# print(bool([[],[]]))
# print(bool([[]]))