class Animal:
    def __init__(self):
        pass
    def say(self):
        print("звук животного")
        
class Cat(Animal):
    def say(self):
        print("Мяу")
        
class Dog(Animal):
    def say(self):
        print("Гав")
        
class Cow(Animal):
    pass
        

_cat = Cat()
_dog = Dog()
_cow = Cow()

_cat.say()
_dog.say()
_cow.say()