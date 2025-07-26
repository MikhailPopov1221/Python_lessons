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
    
    
st = Stack()

st.push(1)
st.push(2)
st.push(3)


print(st.pop())
print(st.pop())
print(st.pop())


s = "Hello"
for i in s:
    st.push(i)
    
for elem in range(st.size()):
    print(st.pop(), end='')
