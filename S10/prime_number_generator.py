
def is_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes_generator(upper_limit: int):
    lst = []
    for i in range(2, upper_limit):
        if is_prime(i):
            lst.append(i)
    return lst


primes = primes_generator(100)
print(primes)

# for prime in primes:
#     print(prime)
