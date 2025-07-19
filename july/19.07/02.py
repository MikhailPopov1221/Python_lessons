class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sleep(self):
        print("Zzzz")
        
class Cat(Animal):
    def say(self):
        print("Мяу")


_animal = Animal("Животное", 10)
_cat = Cat("Леопольд", 45)

print(_animal.name)
print(_cat.name)

_animal.sleep()
_cat.sleep()

_cat.say()

