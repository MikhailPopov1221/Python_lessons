from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__diameter = 2 * radius
        self.__area = pi * radius ** 2
    
    @property    
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius
        self.__diameter = 2 * new_radius
        self.__area = pi * new_radius ** 2
    
    
    @property
    def diameter(self):
        return self.__diameter
    
    
    @property 
    def area(self):
        return self.__area


c1 = Circle(2)

print(f"Радиус круга равен {c1.radius}\nДиаметр равен {c1.diameter}\nПлощадь круга равна {c1.area}")

c1.radius = 5

print()
print(f"Радиус круга равен {c1.radius}\nДиаметр равен {c1.diameter}\nПлощадь круга равна {c1.area}")
