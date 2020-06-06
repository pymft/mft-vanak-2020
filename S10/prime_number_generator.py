
def is_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes_generator(upper_limit: int):
    for i in range(2, upper_limit):
        if is_prime(i):
            yield i


def infinite_primes_generator():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


primes = infinite_primes_generator()

print(primes)

# next(primes)

for prime in primes:
    print(prime)
