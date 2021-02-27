import numpy as np

# Nếu không chạy được thì dùng thư viện anaconda.
# Đổi trình chạy ở góc bên dưới
# Có nút Python 3.8.5 64/32 bit (conda) là ok

# Example 1:
# my_list = [1,2,3,4,'Binh']
# my_arr = np.array(my_list)
# print(my_arr[4])

# Example 2:
# list = np.arange(0,10,2)
# for i in list:
#     print(i)

# Example 3:
# Chú ý: Muốn chia số phần là n thì tổng số là n+1
# list = np.linspace(0,100,11)
# for i in list:
#     print(i)

# Example 4:
# array = np.array(([1,2,3],['one','two','three']))
# for i in range(0,2):
#     for z in range(0,3):
#         print(array[i][z])

# Example 5:
# array = np.zeros((3,3))
# for i in array:
#     print(i)

# Example 6:
# array = np.eye((3))
# for i in array:
#     print(i)

# # Example 7: 
# a = np.random.randint(1,100,(2,8))
# print(a[1][2])

# Example 8:
# a = np.random.choice(['Binh','Bo Binh', 'Me Binh'])
# print(a)

# Example 9:
# a = np.random.choice(['Binh','Bo Binh', 'Me Binh'],size=10)
# print(a)

# Example 10:
# a = np.array([1,2,3,4])
# b = a.reshape(4,1)
# print(b)

# Example 11:
# a = np.array(([1,2,3],[4,5,6]))
# print(a[1][1:])

# Example 12:
# a = np.array([1,2,3,4,5])
# print(a*2)

# Example 12:
# a = np.array([1,2,3,4,5])
# b = np.array([100,200,300,400,500])
# print(a+b)

# Example 13:
# b = np.array([100,200,300,400,500])
# print(b.max())
# print(b.min())
# print(np.sqrt(b))

# Example 14:
# a = np.array([1,2,3,4,5,10])
# print(np.sort(a))

# Example 14:
# a = np.array([1,2,3,4,5,10])
# print(np.array_split(a,3))