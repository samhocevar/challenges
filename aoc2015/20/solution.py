#!/usr/bin/env python

from itertools import count
from math import prod

with open('input.txt') as f: house = int(next(f))

# Utility function to factorise an integer into prime factors; the internal
# list of prime numbers is expanded on-the-fly when needed.
def factor(n, primes=[2]):
    while primes[-1] ** 2 < n:
        primes.append(next(p for p in count(primes[-1] + 1) if next(factor(p))[0] == p))
    if n <= 1: return
    for p in primes:
        if p ** 2 > n: yield (n, 1); return
        if n % p == 0:
            for k in count(1):
                n //= p
                if n % p:
                    yield (p, k)
                    yield from factor(n)
                    return

# The σ1 function is the sum of divisors of a given integer, which happens to
# be the number of presents in the nth house divided by 10. We use the fact
# that σ1(ab) = σ1(a)σ1(b) for coprime numbers in order to speed up computations.
def sigma1(n): return prod((p ** (1 + k) - 1) // (p - 1) for p, k in factor(n))

# Part 1: find the first integer that satisfies σ1(n)·10 >= input
# This could be made faster by assuming the answer is most presumably a
# multiple of 2, 3, and 5, but that is not really known for a fact.
print(next(n for n in count() if sigma1(n) * 4 >= house))
