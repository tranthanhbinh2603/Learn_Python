# Example 1
# from abc import ABC, abstractmethod
# from typing import AsyncGenerator
# class People(ABC):
#     def Intro(self):
#         print('Đây là con người')
    
#     @abstractmethod
#     def Name():
#         pass
#     @abstractmethod
#     def Age():
#         pass
#     @abstractmethod
#     def Sex():
#         pass
#     @abstractmethod
#     def Job():
#         pass

# class Binh(People):
   
#     def Name(self):
#         print('My name is Binh')
    
#     def Age(self):
#         print('I am 13 years old')
    
#     def Sex(self):
#         print('Tôi là nam')
    
#     def Job(self):
#         print('I am student')

# obj1 = Binh()
# obj1.Intro()
# obj1.Name()
# obj1.Age()
# obj1.Sex()
# obj1.Job()

# Example 2:
from Modun import People
class Binh(People):
   
    def Name(self):
        print('My name is Binh')
    
    def Age(self):
        print('I am 13 years old')
    
    def Sex(self):
        print('Tôi là nam')
    
    def Job(self):
        print('I am student')

obj1 = Binh()
obj1.Intro()
obj1.Name()
obj1.Age()
obj1.Sex()
obj1.Job()
