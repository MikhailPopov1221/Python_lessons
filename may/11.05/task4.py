
with open("task4.txt", "r", encoding="utf-8") as fl, open("task4_1.txt", "w", encoding="utf-8") as fl1:
    text = fl.read().strip().split()
    text = [i.strip(" .,!?;:\"'_") for i in text]
    new_text = [f"{i}\n" for i in text if len(i)>=7]
    print(new_text)
    fl1.writelines(new_text)