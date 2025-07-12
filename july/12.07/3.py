class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False
    
    def __str__(self):
        full_line = "* " * self.width
        middle = "* " + "  " * (self.width - 2) + "*" + "\n"
        middle = middle * (self.height - 2)
        return f"{full_line}\n{middle}{full_line}\n"
        
x1 = Rectangle(10, 5)
print(x1)
x2 = Rectangle(10, 5)
print(x2)
print(x1 == x2)
print(x1 == 10)