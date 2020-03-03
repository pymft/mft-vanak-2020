from math import factorial as fact


def combination(n: int, r: int) -> int:
    result = fact(n) // (fact(r) * fact(n - r))
    return result


# lst = [combination(4, 0), combination(4, 1), combination(4, 2), combination(4, 3), combination(4, 4)]
# print(lst)


def pascal_row(n: int) -> list:
    lst = [combination(n, i) for i in range(n + 1)]
    return lst

for i in range(1, 20):
    print(pascal_row(i))
