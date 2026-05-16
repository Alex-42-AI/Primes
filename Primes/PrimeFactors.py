from math import isqrt


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
        if p * p > n:
            break

        power = 0

        while not n % p:
            n //= p
            power += 1

        if power:
            factors[p] = power

        if n == 1:
            break

    if n > 1:
        factors[n] = 1

    return factors


def gcf(p1: int, p2: int) -> int:
    p1, p2 = abs(p1), abs(p2)

    while p1 != p2 and p1 and p2:
        if p1 > p2:
            p1 %= p2

        else:
            p2 %= p1

    return (p1, p2)[not p1]


def lcm(p1: int, p2: int) -> int:
    return abs(p1 * p2) // gcf(p1, p2)


def mutually_prime(n1: int, n2: int) -> bool:
    return gcf(n1, n2) == 1


def product(factor_function: dict[int, int]) -> int:
    p = 1

    for k, v in factor_function.items():
        if not prime(k):
            print(factor_function)

            raise ValueError

        p *= k ** v

    return p
