class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sleep(self):
        print("Zzzz")
        
class Cat(Animal):
    def __init__(self, name, age, color):
        self.color = color
        super().__init__(name, age)
        # Animal.__init__(self, name, age)
          

    def say(self):
        print("Мяу")
        
class Dog(Animal):
    def say(self):
        print("Гав")


_animal = Animal("Животное", 10)
_cat = Cat("Леопольд", 45, "Grey")
_dog = Dog("Шарик", 12)

print(_animal.name)
print(_cat.name)

_animal.sleep()
_cat.sleep()

_cat.say()
_dog.say()

print(_cat.color)
