s = "Шел осенний дождь. \
Поздним вечером в июле Чупакабра прогуливалась под зонтом. \
И зашла она в чебуречную!\
решила купить 101 чебурек, съела и отравилась. \
и восстали Чупакабры!\
И тут я проснулся?!\
"
start_sentense = True
new_story = ''

for ch in s:
    if start_sentense == True and ch.isalpha():
       new_story += ch.upper()
       start_sentense = False
    else:
        new_story += ch
        
    if ch in (".!?"):
        start_sentense = True
        
        
print(new_story)

count_of_digits = 0
for sym in s:
    if sym in "0123456789":
        count_of_digits += 1
        # count_of_digits = count_of_digits + 1

print(f"Количество цифр в тексте = {count_of_digits}")
# print("Количество цифр в тексте =", count_of_digits)








