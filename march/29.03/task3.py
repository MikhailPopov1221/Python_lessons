def draw_line(len_line, direction, symbol):
    if direction == 'vertical':
        # print(f"{symbol}\n" * len_line)
        print((symbol + "\n") * len_line)
    elif direction == 'horizontal':
        print(symbol * len_line)
    else:
        print("Wrong direction")
        
draw_line(10, "vertical", "%")
draw_line(10, "horizonal", "%")


a = 1
b = 3
c = 4
ls = [a, b, c]
        
