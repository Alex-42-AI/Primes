from math import floor, sqrt
from Primes.PrimesList import Primes_173467
def prime(A: int):
    if A < 2 or A != 2 and not A % 2:
        return False
    for I in range(3, floor(sqrt(A)) + 1, 2):
        if not A % I:
            return False
    return True
def factorize(N: int):
    if N > 2358701:
        p = None
        for num in Primes_173467:
            if not N % num:
                p = num
                break
        if p is None:
            num = 2358721
            while p is None:
                if not N % num:
                    p = num
                    break
                num += 2
                if num >= floor(sqrt(N)):
                    return N
        for i in range(2358721, N // p + 1, 2):
            if prime(i):
                Primes_173467.append(i)
    else:
        if N < 2:
            raise ValueError('No...')
    Prime = True
    for i in Primes_173467:
        if N in Primes_173467:
            if not Prime:
                print(f'Found: {N} - once')
            break
        if not N % i:
            Prime, power = False, 0
            while not N % i:
                N //= i
                power += 1
            print(f'Found: {i} - {power} times' if power > 2 else (f'Found: {i} - twice' if power - 1 else f'Found: {i} - once'))
        if i > N or N == 1:
            break
def gcf(p1: int, p2: int):
    p1, p2 = abs(p1), abs(p2)
    while p1 != p2 and p1 and p2:
        if p1 > p2:
            p1 %= p2
        else:
            p2 %= p1
    return (p1, p2)[not p1]
def lcm(p1: int, p2: int):
    return abs(p1 * p2) // gcf(p1, p2)
def mutually_prime(n1: int, n2: int):
    return gcf(n1, n2) == 1
factorize(int(input()))
