class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sleep(self):
        print("Zzzz")
        
class Cat(Animal):
    pass

class CatBreet(Cat):
    pass

_animal = Animal("Животное", 10)
_cat = Cat("Леопольд", 45)

print(_animal.name)
print(_cat.name)

_animal.sleep()
_cat.sleep()


_british_cat = CatBreet("Жорик", 1)
print(_british_cat.name)

