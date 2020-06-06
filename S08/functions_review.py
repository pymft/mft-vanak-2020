def fun(a: int, b:int, c, x:int=1, y=2, z=3):
    m = a + b + c
    n = x + y + z

    return m * n

# GOOD :)
fun(10, 20, 30)
fun(10, 20, 30, x=100)
fun(10, 20, 30, y=100)
fun(10, 20, 30, z=100)
fun(10, 20, 30, z=200, x=100)

# BAD
fun(10, 20, 30, 100)

## fun(10, 20, 30, x=100, y=200, 1000)



