def fun(f):
    inner = lambda x: f(x)
    return inner


out = fun(len)
out([1, 2, 3])