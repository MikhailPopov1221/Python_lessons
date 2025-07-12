class Auto:
    def __init__(self, mark):
        self.mark = mark
        
    def __str__(self):
        return f"Автомобиль марки {self.mark}"
        
        
car = Auto("BMW")
print(car.mark)
print(car)

# str(car)
# repr(car)
