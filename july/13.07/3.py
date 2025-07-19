class Wallet:
    def __init__(self, count):
        self.money = count
    
    def __add__(self, value):
        if isinstance(value, Wallet):
            return Wallet(self.money + value.money)
        elif isinstance(value, int):
            return Wallet(self.money + value)
        return NotImplemented
    
    def __radd__(self, value):
        if isinstance(value, int):
            return Wallet(self.money + value)
        return NotImplemented
        
    def __str__(self):
        return f"Баланс кошелька = {self.money}"
        

w1 = Wallet(100)
w2 = Wallet(500)
w3 = w1 + w2

print(w1)
print(w2)
print(w3)

w1 = 5 + w1 ## 5.__add__(w1)
# w1 = w1 + 5 ## w1.__add__(5)
print(w1)
