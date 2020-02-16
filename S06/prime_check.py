import math


def is_prime(n: int) -> bool:

    upper_limit = int(math.sqrt(n))
    for i in range(2, upper_limit):
        if n % i == 0:
            return False

    return True


def is_prime_old(n: int) -> bool:
    """
    checks if n is a prime number
    """
    upper_limit = n
    for i in range(2, upper_limit):
        if n % i == 0:
            return False

    return True

# print(is_prime(3))   # True
# print(is_prime(13))  # True
# print(is_prime(111))  # False
print(is_prime(73939133))  # False
print(is_prime_old(73939133))  # False