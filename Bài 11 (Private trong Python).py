class People:
    __Name = 'Trần Thanh Bình' # Đây là một biến private
    Name = __Name

    def __PrivateFunction(self):
        print('Hello, World!!!')
    
    def Function(self):
        self.__PrivateFunction()

object1 = People()
print(object1.Name)
object1.Function()
