class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__fullname = f"{self.__name} {self.__surname}"
        
    @property
    def name(self):
        return self.__name
    
    @name.setter    
    def name(self, new_name):
        self.__name = new_name
        self.__fullname = f"{self.__name} {self.__surname}"
      
    @property    
    def surname(self):
        return self.__name
    
    @surname.setter
    def surname(self, new_surname):
        self.__name = new_surname
        self.__fullname = f"{self.__name} {self.__surname}"
        
    @property    
    def fullname(self):
        return self.__fullname

        
        