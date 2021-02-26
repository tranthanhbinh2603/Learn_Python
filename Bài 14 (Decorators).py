def decorator(func):
    def wrapper(*a):
        print('Dang chay!!!!')
        res = func(*a)
        return res
    return wrapper

@decorator
def Add(*a):
    tong=0
    for item in a:
        tong = tong + item
    return tong

@decorator
def Sub(*a):
    hieu=0
    for item in a:
        hieu = hieu - item
    return hieu

print(Add(1,2,3))
print(Sub(1,2,3))