# Подсчет символов в строке

s = input("Введите любой текст: ")
dct = {}

# Hello
for ch in s.split():
    dct[ch] = dct.get(ch,0) + 1
    
print(dct)