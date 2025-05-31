fl = open("task1.txt", "w", encoding="utf-8")
for i in range(1,11):
    fl.write(f"2 x {i} = {2*i}\n")
fl.close()