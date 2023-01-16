#!/usr/bin/env python

from itertools import count

with open('input.txt') as f:
    k1, k2 = tuple(map(int, f))

n, s, end = 1, 7, 0
for loop in count(1):
    n = n * s % 20201227
    if n == k1 and not end:
        n, s, end = 1, k2, loop * 2
    elif loop == end:
        break

print(n)
