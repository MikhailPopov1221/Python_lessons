class Auto:
    def __init__(self, form, color, power):
        self.form = form
        self.color = color
        self.power = power
        self.producer = "Germany"
        
        if power <= 150:
            self.__tax = 5000
        elif power > 150 and power <= 200:
            self.__tax = 15000
        else:
            self.__tax = 50000
            
    def show_tax(self):
        return self.__tax
        
        
bmw = Auto("sedan", "black", 200)
print(bmw.color)
print(bmw.show_tax())

