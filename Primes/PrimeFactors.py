from math import floor, sqrt
from Personal.Primes.PrimesList import Primes_173467
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
    Prime, Res = True, ''
    for i in Primes_173467:
        if N in Primes_173467:
            Res += str(N)
            if not Prime:
                print(f'Found: {N} - once')
            break
        if not N % i:
            Res += str(i)
            Prime, power = False, 0
            while not N % i:
                N //= i
                power += 1
            print(f'Found: {i} - {power} times' if power > 2 else (f'Found: {i} - twice' if power - 1 else f'Found: {i} - once'))
            Res += str(power) * (power > 1)
        if i > N or N == 1:
            break
    return int(Res)
def gcf(p1: int, p2: int):
    p1, p2 = abs(p1), abs(p2)
    if 0 in [p1, p2]:
        return [p1, p2][not p1]
    while p1 - p2:
        if p1 > p2:
            p1 -= p2
        else:
            p2 -= p1
    return p1
def scd(p1: int, p2: int):
    p1_copy, p2_copy = abs(p1), abs(p2)
    while p1_copy - p2_copy:
        if p1_copy > p2_copy:
            p2_copy += abs(p2)
        else:
            p1_copy += abs(p1)
    return p1_copy
def mutually_prime(n1: int, n2: int):
    return gcf(n1, n2) == 1
n = factorize(int(input()))
while True:
    print(n)
    m, a = factorize(n), False
    if n in Primes_173467:
        a = True
    if not a:
        if prime(n):
            a = True
    if a:
        m, b = int(str(n)[::-1]), False
        if m in Primes_173467:
            b = True
        if not b:
            if prime(m):
                b = True
        if b:
            print(m)
            break
    n = m