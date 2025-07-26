class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        else:
            return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        else:
            return self.items[-1]
    
    def clear(self):
        self.items.clear()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    


def check_brackets(s: str) -> bool:
    stack = Stack()
    for elem in s:
        if elem in "({[":
            stack.push(elem)
        elif elem in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top == "(" and elem != ")":
                return False
            elif top == "[" and elem != "]":
                return False
            elif top == "{" and elem != "}":
                return False
    return stack.is_empty()


s = "{[()]}"
print(check_brackets(s))

s = "{[)]}"
print(check_brackets(s))  

s = "{[(777)]}"
print(check_brackets(s))

s = "{[(])}"
print(check_brackets(s))           