
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# sub list
sub_list = lst[1:8]   # lst[1:-1]
print(sub_list)

# sub list w/ steps
sub_list = lst[1:8:2]   # lst[1:-1:2]
print(sub_list)


sub_list = lst[8:1:-1]
print(sub_list)


sub_list = lst[::]
print(sub_list)
