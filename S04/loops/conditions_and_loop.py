n = 15
patterns = [".", "+"]
i = 1

while i <= n:
    i_new = 2 * i - 1

    line = patterns[i % 2] * i_new

    line_new = line.center(2 * n - 1)
    print(line_new)
    i = i + 1
