def my_gen(n):
    i = 0
    a, b = 1, 1
    while i < n:
        i = i + 1
        yield a
        a, b = b, a + b


obj = my_gen(5)



print(list(obj))