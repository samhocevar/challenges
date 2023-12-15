#!/usr/bin/env python

from itertools import count

def factor(n, primes=[2]):
    while primes[-1] ** 2 < n:
        primes.append(next(p for p in count(primes[-1] + 1) if next(factor(p))[0] == p))
    if n <= 1: return
    for p in primes:
        if p ** 2 > n: yield (n, 1); return
        if n % p == 0:
            for k in count(1):
                n //= p
                if n % p: yield (p, k); yield from factor(n); return

print(list(factor(600851475143))[-1][0])
