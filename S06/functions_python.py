
def multiply_by_two(n):
    out = n * 2
    return out


def concate(a: str, b: str) -> str:
    res = a.upper() + " " + b.lower()
    return res


def factorial(n: int):
    answer = 1
    for i in range(1, n+1):
        answer = answer * i

    return answer


print(concate("AaAaaAAA", "bBbBBbbB"))


