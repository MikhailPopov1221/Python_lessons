# s = input("Введите слово для проверки ")
# if s == s[::-1]:
#     print("Это полиндром")
# else:
#     print("Это не полиндром")
    
    
s = input("Введите слово для проверки ")
if s.lower() == s.lower()[::-1]:
    print("Это полиндром")
else:
    print("Это не полиндром")
    