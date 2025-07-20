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
        

cat1 = Cat()
cat2 = Cat()
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

animals = [cat1, dog1, cat2, dog2, dog3]

for i in animals:
    i.say()