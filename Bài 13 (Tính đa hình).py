# Nếu không có thư viện chạy câu lệnh: pip install multipledispatch
from multipledispatch import dispatch
from collections import namedtuple
class Example():
    @dispatch(Iterable)
    def Class1(self, arg):
        print('Phần tử là: ',arg)
    
    @dispatch(object, object)
    def Class1(self, arg1, arg2): # Hai hàm có tên giống nhau
        print('Phần tử thứ nhất:', arg1,',phần tử thứ hai:', arg2)
    
obj1 = Example()
obj1.Class1(1)
obj1.Class1(1,2)

