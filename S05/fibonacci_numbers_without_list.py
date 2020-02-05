a = 1
b = 1

counter = 1

while counter < 10:
    # a_new = b
    # b_new = a + b
    #
    # a, b = a_new, b_new
    a, b = b, a + b

    counter = counter + 1


print(b/a)

# 1.618033988749895
# 1.618033988749895‬

