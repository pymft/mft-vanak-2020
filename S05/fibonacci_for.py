a = 1
b = 1

for i in range(100_000):
    a, b = b, a + b

print(a)
