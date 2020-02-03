n = 15
pattern_odd = "+"
pattern_even = "."
i = 1


while i <= n:
    i_new = 2 * i - 1
    if i % 2 == 0:
        line = pattern_even * i_new
    else:
        line = pattern_odd * i_new

    line_new = line.center(2*n-1)
    print(line_new)
    i = i + 1
