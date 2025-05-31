s = open("1.txt", "w", encoding="utf-8")

s.write("Добрый вечер Господа и Дамы")
try:
    print(s.read())
except Exception as e:
    pass
finally:
    s.close()
    print("файл закрыт")
