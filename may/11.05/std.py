import sys

sys.stdout.write("Hello world!")
sys.stdout.write("Hello world!")

fl = open("std.txt", "w", encoding="utf-8")

print("Hello from print!", file=fl)

fl.close()