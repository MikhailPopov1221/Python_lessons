class Car:
    count = 0
    def __init__(self, name, power):
        Car.count += 1
        self.name = name
        self.power = power
        self.serial_number = Car.count
        
    def __str__(self):
        return f"Имя - {self.name}\nМощность - {self.power}\nКоличество созданых машин - {self.count}\nСерийный номер - {self.serial_number}"
    

car1 = Car("Tesla", 500)
car2 = Car("Mersedes", 350)
print(car1)
print(car2)

