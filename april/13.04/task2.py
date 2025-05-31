fruit = ("apple", "banana", "orange", "lemon", "apple", "apple", "lemon", "bananamango")

user_choice = input("Введите название фрукта:  ")
count = len(tuple(filter(lambda x: user_choice in x,fruit)))



if count:
    print(f"{user_choice} встречается в кортеже {count} раз")
else:
    print("Такого у нас нет")
