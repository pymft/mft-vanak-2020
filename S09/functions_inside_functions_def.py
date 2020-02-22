def fun(f):
    def inner(x):
        return f(x)
    return inner


out = fun(len)
out([1, 2, 3])

