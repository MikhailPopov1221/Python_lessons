class HappyMan:
    def __init__(self):
        self.__name = ''
        self.__sname = ''
        self.__bday = ''
        self.__phone = ''
        self.__city = ''
        self.__country = ''
        self.__adress = ''
        self.__fio = f"{self.__name} {self.__sname}"
        
    
    def input_fio(self,name: str, sname: str):
        if type(name) == str and name.isalpha():
            self.__name = name.capitalize()
        
        if type(sname) == str and sname.isalpha():
            self.__sname = sname.capitalize()
            
        self.__fio = f"{self.__name} {self.__sname}"
        
    def get_fio(self):
        return self.__fio 
    
    def get_name(self):
        return self.__name 
    
    def get_sname(self):
        return self.__sname 
    
    def input_phone(self, phone):
        if type(phone) == int and len(str(phone)) == 11:
            self.__phone = "+7" + str(phone)[1:]
            
        elif type(phone) == str:
            temp_lst = [i for i in phone if i.isdigit()]
            if len(temp_lst) == 11:
                self.__phone = "+7" + "".join(temp_lst)[1:]
                
    def get_phone(self):
        return self.__phone
    
    
adam = HappyMan()
adam.input_fio("adam", "adamov")
adam.input_phone(89995554433)

print(adam.get_fio())
print(adam.get_phone())

adam.input_phone("8 000 445-44-22")
print(adam.get_phone())

        
        
        