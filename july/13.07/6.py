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
        return self.__add__(value)
    
    def __int__(self):
        return self.money
    
    def __bool__(self):
        if self.money > 0:
            return True
        return False
    
    def __str__(self):
        return f"Баланс кошелька = {self.money}"
        

w1 = Wallet(100)

print(w1)

x = int(w1)
print(x)


w1 = Wallet(0)
if w1:
    print(w1)
else:
    print("Сработал False")
