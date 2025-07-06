from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__diameter = 2 * radius
        self.__area = pi * radius ** 2
        
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, new_radius):
        self.__radius = new_radius
        self.__diameter = 2 * new_radius
        self.__area = pi * new_radius ** 2
    
    def get_diameter(self):
        return self.__diameter
    
    def get_area(self):
        return self.__area



    
c1 = Circle(2)
print(f"Радиус круга равен {c1.get_radius()}\nДиаметр равен {c1.get_diameter()}\nПлощадь круга равна {c1.get_area()}")
print()
print("Изменим радиус")
c1.set_radius(3)
print(f"Радиус круга равен {c1.get_radius()}\nДиаметр равен {c1.get_diameter()}\nПлощадь круга равна {c1.get_area()}")
