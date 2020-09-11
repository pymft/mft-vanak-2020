def my_gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


def my_gen_new(n):
    i = 0
    while n > i:
        yield i
        i += 1


lst = [1, 2, 3, 4, 5, 6]
gen1 = my_gen_new(10)

print(next(gen1))
print(next(gen1))
print("--------------")
for x in gen1:
    print(x)
