def check_age(age):
    if age < 18:
        raise ValueError("Возраст должен быть >18 лет")
    elif age >100:
        raise ValueError("Может не надо?!")
    
    
age = int(input("Введите свой возраст:  "))
try:
    check_age(age)
except Exception as e:
    print(e)