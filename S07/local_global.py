def fun(n: int) -> int:
    print(locals())
    a = n * 2
    b = n ** 2

    return b

print(locals())
fun(10)

