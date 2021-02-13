## Cú pháp: lambda <đối số>:<Kết quả trả về>

## Example 1:
# k = lambda a,b:a+b
# print(k(1,2))

## Dùng list(map(<lambda cần dùng>)) dể làm việc với list

## Example 2:
# my_list = [1,2,3]
# a = list(map(lambda a:a*3, my_list))
# print(a)

## Example 3:
# my_list = [1,2,3,4,5,6]
# a = list(map(lambda a: a%2 == 0, my_list))
# dem = -1
# for item in a:
#     dem = dem + 1
#     if item == True:
#         print(my_list[dem])