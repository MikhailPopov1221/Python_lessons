class Auto:
    def __init__(self, form, color, power):
        self.form = form
        self.color = color
        self.power = power
        

bmw = Auto("sedan", "black", 200)
print(bmw.color)