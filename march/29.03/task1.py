height = int(input("Введите высоту треугольника "))
symbol = input("Введите символ заполнения ")

# =
# = =
# = = =
# = =
# =

def draw_triangle(h, chr):
    for i in range(h//2): 
        print(chr * (i+1))
    for i in range(h//2, -1, -1):
        print(chr * (i+1))

draw_triangle(height, symbol)