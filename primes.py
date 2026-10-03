from math import isqrt, gcd


def prime(n: int) -> bool:
    if n < 2 or n != 2 and not n % 2:
        return False

    for i in range(3, isqrt(n) + 1, 2):
        if not n % i:
            return False

    return True


def sieve(n: int) -> list[int]:
    if n < 2:
        return []

    result, composite, p = [2], bytearray(n + 3), 3

    while p <= n:
        result.append(p)

        for i in range(p * p, n + 1, 2 * p):
            composite[i] = True

        p += 2

        while composite[p]:
            p += 2

    return result


def factorize(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError

    factors = {}

    for p in sieve(isqrt(n)):
        power = 0

        while not n % p:
            n //= p
            power += 1

        if power:
            factors[p] = power

        if p * p > n:
            break

    if n > 1:
        factors[n] = 1

    return factors


def decompose(n: int) -> tuple[int, int]:
    if not n % 2:
        return 2, n // 2

    for p in range(3, isqrt(n) + 1, 2):
        if not n % p:
            return p, n // p

    return 1, n


def decompose_backwards(n: int) -> tuple[int, int]:
    if not n % 2:
        return 2, n // 2

    m = isqrt(n)

    for p in range(m + m % 2 - 1, 1, -2):
        if not n % p:
            return p, n // p

    return 1, n


def sieve_decompose(n: int) -> tuple[int, int]:
    if not n % 2:
        return 2, n // 2

    for p in reversed(sieve(isqrt(n))):
        if not n % p:
            return p, n // p

    return 1, n


def Fermat_algorithm(n: int) -> tuple[int, int]:
    a = isqrt(n)

    if a * a < n:
        a += 1

    while True:
        b2 = a * a - n
        b = isqrt(b2)

        if b * b == b2:
            return a - b, a + b

        a += 1


def lehmanish(n: int) -> tuple[int, int]:
    limit = int(n ** 0.25)

    for k in range(1, limit + 1):
        a = isqrt(kn := k * n)

        if a * a < kn:
            a += 1

        max_a = isqrt(2 * isqrt(kn) * n // k) + 1

        while a <= max_a:
            b2 = a * a - kn
            b = isqrt(b2)

            if b * b == b2:
                d = gcd(a - b, n)

                if 1 < d < n:
                    return d, n // d

            a += 1

    return 1, n


def mutually_prime(n1: int, n2: int) -> bool:
    return gcd(n1, n2) == 1


def product(factor_function: dict[int, int]) -> int:
    p = 1

    for k, v in factor_function.items():
        if not prime(k):
            print(factor_function)

            raise ValueError

        p *= k ** v

    return p
