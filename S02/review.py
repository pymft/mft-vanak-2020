# lists are mutable
lst = [1, 2, 3, 4]
print(lst)
lst[0] = 10_000_000_000
# lst[0] = 10000000000
print(lst)


# tuples are immutable
tup = (1, 2, 3, 4)
print(tup)
# tup[0] = 10000
# print(tup)