fib = [1, 1]

while len(fib) < 200_000:
    next_val = fib[-1] + fib[-2]
    fib.append(next_val)

print(fib[-1])

# 354224848179261915075