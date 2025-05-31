fl = open("_readline.txt", "r", encoding="utf-8")

# print(fl.readline(), end='')
# print(fl.readline(), end='')

line = fl.readline()
while line != "":
    if line[0] == "7":
        print(line, end='')
    line = fl.readline()

fl.close()