class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
    
    def __ne__(self, other):
        return True
    
        
    def __str__(self):
        return f"Point({self.x},{self.y})"
    
dot1 = Point(2,3)
dot2 = Point(3,4)
dot3 = Point(2,3)
print(dot1)
print(dot2)
print(dot1 == dot2)
print(dot1 == dot3)

print(dot1 != dot2)
print(dot1 != dot3)
