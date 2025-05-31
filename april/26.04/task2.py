abc = {
    1: ".,!?",
    2: "АБВГ",
    3: "ДЕЖЗ",
    4: "ИЙКЛ",
    5: "МНОП",
    6: "РСТУ",
    7: "ФХЦЧ",
    8: "ШЩЪЫ",
    9: "ЬЭЮЯ",
    0: " "
}

s = input("Введите строку для кодировки: ")
for ch in s:
    for k, v in abc.items():
        if ch.upper() in v:
            print(str(k) * (v.index(ch.upper()) + 1), end="")
       
