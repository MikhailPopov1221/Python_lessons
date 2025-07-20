class Parent1:
    def say(self):
        print("Hello from Parent1")

class Parent2:
    def sleep(self):
        print("Zzzz")
        
    def say(self):
        print("Hello from Parent2")

class Child(Parent2, Parent1):
    pass

c = Child()

c.say()
c.sleep()