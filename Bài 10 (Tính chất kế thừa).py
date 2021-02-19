## Example 1 - Căn bản
# class Father:
#     def FunA(self):
#         return 'Đây là hàm A trong lớp Father'

#     def FunB(self):
#         return 'Đây là hàm B trong lớp Father'

# class Son(Father):
#     def FunB(self):
#         return 'Đây là hàm B trong lớp Son'

# obj1 = Son()
# print(obj1.FunA())
# print(obj1.FunB())


## Example 2 - Tạo hàm mới trong hàm con
# class Father:
#     def FunA(self):
#         return 'Đây là hàm A trong lớp Father'

#     def FunB(self):
#         return 'Đây là hàm B trong lớp Father'

# class Son(Father):
#     def FunB(self):
#         return 'Đây là hàm B trong lớp Son'

#     def FunC(self):
#         return 'Đây là hàm C trong lớp Son'

# obj1 = Son()
# print(obj1.FunC())

## Example 3 - Mức độ ưu tiên kế thừa
class Father:
    def FunA(self):
        return 'Đây là hàm A trong lớp Father'

    def FunB(self):
        return 'Đây là hàm B trong lớp Father'

    def FunC(self):
        return 'Đây là hàm C trong lớp Father'

class Mother():
    def FunA(self):
        return 'Đây là hàm A trong lớp Mother'

    def FunB(self):
        return 'Đây là hàm B trong lớp Mother'

    def FunC(self):
        return 'Đây là hàm C trong lớp Mother'

class Son1(Father, Mother):
    pass

class Son2(Mother, Father):
    pass

obj1 = Son1()
obj2 = Son2()
print(obj1.FunA())
print(obj1.FunB())
print(obj1.FunC())
print(obj2.FunA())
print(obj2.FunB())
print(obj2.FunC())