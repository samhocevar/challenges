#!/usr/bin/env python

from math import gcd

with open('input.txt') as f:
    n = int(next(f))
print(sum(i for i in range(n) if gcd(i, n) == 1))
