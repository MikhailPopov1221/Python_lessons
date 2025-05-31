import sys

fl = open("_input.txt", "r", encoding="utf-8")
sys.stdin = fl

try:
    name = input()
    while name != '':
        print(f"Привет, {name}!")
        name = input()
except:
    pass

fl.close()