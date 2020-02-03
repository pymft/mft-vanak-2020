n = 12
pattern = "*"
ws_pattern = " "
i = 1


while i <= n:
    i_new = 2 * i - 1
    line = pattern * i_new
    spaces = ws_pattern * (n - i)
    line_new = spaces + line + spaces
    print(line_new)
    i = i + 1


# line 5 * 2 - 1 = 9
# '*********'