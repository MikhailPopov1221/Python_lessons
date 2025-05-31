# Я купил 3 яблока и 5 груш
# Я купил три яблока и пять груш

s = "Я купил 3 яблока и 5 груш"

for i in range(10):
    if i == 0:
        s = s.replace(str(i),"ноль")
    if i == 1:
        s = s.replace(str(i),"один")
    if i == 2:
        s = s.replace(str(i),"два")
    if i == 3:
        s = s.replace(str(i),"три")
    if i == 4:
        s = s.replace(str(i),"четыре")
    if i == 5:
        s = s.replace(str(i),"пять")
    if i == 6:
        s = s.replace(str(i),"шесть")
    if i == 7:
        s = s.replace(str(i),"семь")
    if i == 8:
        s = s.replace(str(i),"восемь")
    if i == 9:
        s = s.replace(str(i),"девять")
    
    
print(s)
    