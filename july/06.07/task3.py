class Color:
    def __init__(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.__r = r
            self.__g = g
            self.__b = b
        else:
            self.__r = 0
            self.__g = 0
            self.__b = 0
            
    @property
    def r(self):
        return self.__r
    
    @property
    def g(self):
        return self.__g
    
    @property
    def b(self):
        return self.__b
    
    @property
    def hex_color(self):
        r = hex(self.__r)[2:]
        g = hex(self.__g)[2:]
        b = hex(self.__b)[2:]
        return f"#{r}{g}{b}".upper()

    
header = Color(200, 215, 0) 
header.hex_color # "#F08080"
print(header.hex_color)
   