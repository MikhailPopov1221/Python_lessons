from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def say(self):
        pass
        
class Cat(Animal):
    def say(self):
        print("Мяу")
        
class Dog(Animal):
    def say(self):
        print("Гав")
        
class Cow(Animal):
    pass
        

# _animal = Animal()
_cat = Cat()
_dog = Dog()
# _cow = Cow()

_cat.say()
_dog.say()
# _cow.say()