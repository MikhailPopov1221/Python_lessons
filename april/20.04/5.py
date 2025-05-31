num1 = 123456789
num2 = 4560

set1 = set(str(num1))
set2 = set(str(num2))

if set2.issubset(set1):
    print(f"{num2} является подмножеством {num1}")
else:
    print(f"{num2} не является подмножеством {num1}")
    