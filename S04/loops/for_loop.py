lst = [1, 2, True, "hello", (1, 2, 3)]
#
# i = 0
# while i < len(lst):
#     temp = lst[i]
#     print(temp)
#
#     i = i + 1
#
# lst = [1, 2, 3, 4, 5, 6, 7]
# for temp in range(5, 101, 5):
#     print(temp)


factorial = 1
n = 1000
for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)