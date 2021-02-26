from abc import ABC, abstractmethod
class People(ABC):
    def Intro(self):
        print('Đây là con người')
    
    @abstractmethod
    def Name():
        pass
    @abstractmethod
    def Age():
        pass
    @abstractmethod
    def Sex():
        pass
    @abstractmethod
    def Job():
        pass