def add(x, y):
    return x+y

def diff(x, y):
    return x-y

def prod(x, y):
    return x*y

def div(x, y):
    if y == 0:
        print("Enter number greater than zero")
    return x/y

print(add(5, 3))
print(diff(6, 3))
print(prod(4, 2))
print(div(9, 3))
