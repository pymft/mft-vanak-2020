a = 1
b = 2

# binary
# * + / - pow(**) //

# unary
#  negation
d = -a

## COMPARE

a >= b

# > >= < <= == !=


## LOGICAL
# binary: and or
# unary:  not

#
#  a      b      c      d      e
#  10     20     30     40     50
# -+------+------+------+------+---------------- >
a, b, c, d, e = 10, 20, 30, 40, 50

num = 45
# -+###########################+---------------- >

cond = (num > a) and (num < e)
print(cond)
cond = a < num < e
print(cond)

# -+######+------+######+------+---------------- >

