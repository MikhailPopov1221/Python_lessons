from abc import ABC, abstractmethod

class MFU(ABC):
    @abstractmethod
    def i_print(self):
        pass
    
    @abstractmethod
    def i_scan(self):
        pass
    
    @abstractmethod
    def i_copy(self):
        pass
    

class Iprint(ABC):
    @abstractmethod
    def i_print(self):
        pass
    
class Icopy(ABC):
    @abstractmethod
    def i_copy(self):
        pass
    
class Iscan(ABC):
    @abstractmethod
    def i_scan(self):
        pass
    
    
class Printer1(Icopy, Iscan, Iprint):
    pass


class Printer2(Iprint):
    pass