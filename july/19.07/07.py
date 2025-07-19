class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    @property    
    def perimetr(self):
        return (self.height + self.width) * 2
    
class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)
        
        
fig1 = Rectangle(2,4)
fig2 = Square(6)

print(fig1.perimetr)
print(fig2.perimetr)