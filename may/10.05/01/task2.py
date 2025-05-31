fl = open("task2.txt", "w", encoding="utf-8")
for j in range(1,10):
    for i in range(1,11):
        fl.write(f"{j} x {i} = {j*i}\n")
    fl.write("\n")
fl.close()