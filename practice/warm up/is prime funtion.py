def is_prime(n: int) -> bool:
    upper_limit = int(n ** 0.5)

    for i in range(2, upper_limit):
        if n % i == 0:
            # test
            return False

        return True



a = is_prime(13)
print(a)