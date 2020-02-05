a = 1
b = 1

counter = 1

while counter < 500_000:
    a, b = b, a + b
    counter = counter + 1


print(a)

# 354224848179261915075

