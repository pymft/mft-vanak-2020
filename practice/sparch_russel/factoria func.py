def factorial(n):
    out = 1
    for i in range(1, n + 1):
        out = out * i
    return out
print(factorial(5))

