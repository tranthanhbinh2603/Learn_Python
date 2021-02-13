#module.py

def Example_module_1(*a):
    sum= 0
    for item in a:
        sum = sum + int(item)
    return sum

def Example_module_2(*a):
    max = a[0]
    for item in a:
        if max<item:
            max=item
    return max
