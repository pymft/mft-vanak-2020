def shape(n, pat: str = "*", ws: str = " "):
    i = 1

    while i <= n:
        i_new = 2 * i - 1
        line = pat * i_new
        spaces = ws * (n - i)
        line_new = spaces + line + spaces
        print(line_new)
        i = i + 1


shape(10, pat=".", ws="@")
