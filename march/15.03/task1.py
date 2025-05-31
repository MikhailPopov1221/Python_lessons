h = int(input("Введите высоту прямоугольника: "))
w = int(input("Введите ширину прямоугольника: "))

# for i in range(h):
#     for j in range(w):
#         print('*', end=' ')
#     print()


# for i in range(h):
#     if i == 0 or i == h-1:
#         print("* " * w, end="")
#     else:
#         print("* ", end="")
#         for j in range(w - 2):
#             print("0 ", end="")
#         print("* ", end="")
#     print()


for i in range(h):
    for j in range(h):
        if h - 1 - i == j or i == j:
            print("0 ", end="")
        else:
            print("* ", end="")
    print()
