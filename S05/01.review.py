
s = 0
for i in range(1, 1000_000):
    s = s + 1/(i*i)

pi_approx = (s*6) ** 0.5
print(pi_approx)
