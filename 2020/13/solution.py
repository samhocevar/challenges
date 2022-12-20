#!/usr/bin/env python

from math import prod, lcm

with open('input.txt') as f:
    t0 = int(next(f))
    data = [-1 if s == 'x' else int(s) for s in next(f).split(',')]

print(prod(min((n - t0 % n, n) for n in data if n > 0)))

t, period = 0, 1
for i, n in enumerate(data):
    if n > 0:
        # We want (t + i) % n == 0
        # We can only add multiples of period to t
        # So we compute the inverse of period modulo n
        t += pow(-period, -1, n) * (i + t) % n * period
        period = lcm(period, n)
print(t)
