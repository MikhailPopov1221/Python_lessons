rd = open("scores.txt", "r", encoding="utf-8")
wr = open("task3.txt", "w", encoding="utf-8")

line = rd.readline()
while line != "":
    # line - "Петров 3 5 5 4 5\n"
    new_line = line.strip().split()
    # new_line - ['Петров', '3', '5', '5', '4', '5']
    awg = [int(i) for i in new_line[1:]]
    # awg - [3, 5, 5, 4, 5]
    awg = sum(awg)/len(awg)
    wr.write(f"{new_line[0]} {awg}\n")
    
    line = rd.readline()
    
rd.close()
wr.close()