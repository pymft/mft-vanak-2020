sz = 4
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 23, 2, 3, 99]

res = lst[:sz] + lst[-sz:]
print(res)
res2 = lst[2:7:2]
print(res2)
print(lst[-sz:-10:-1])