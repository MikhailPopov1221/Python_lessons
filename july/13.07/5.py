def sum_n(a,b):
    return a + b

print(sum_n(1,5))

class Sum_c:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __call__(self, *a, **k):
        return self.a + self.b
    
s = Sum_c(1,5)
print(s())
