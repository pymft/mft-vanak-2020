upper_limit = 7_000
lower_limit = 1_000
step = 1

i = lower_limit
out = 0

while i <= upper_limit:
    out = out + i
    i = i + step

print("sum = ", out)

