class Auto:
    def __init__(self, form, color, power):
        self.form = form
        self.color = color
        self.power = power
        self.producer = "Germany"
        
        if power <= 150:
            self.tax = 5000
        elif power > 150 and power <= 200:
            self.tax = 15000
        else:
            self.tax = 50000
        
        

bmw = Auto("sedan", "black", 200)
print(bmw.color)
print(bmw.tax)
bmw.tax = 0
print(bmw.tax)


oka = Auto("sedan", "black", 300)
print(oka.color)
print(oka.tax)