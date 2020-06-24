# positional argument
# keyword args or named arguements

def fun(x, y=2, z=1):
    res = z * x ** y
    return res


print(fun(10))
print(fun(10, y=3))
print(fun(10, z=5))
print(fun(10, z=5, y=3))
print(fun(10, 5, 3))
