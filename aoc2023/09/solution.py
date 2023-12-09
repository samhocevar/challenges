#!/usr/bin/env python

from itertools import pairwise

with open('input.txt') as f:
    data = [[int(n) for n in l.split()] for l in f]

def extrapolate(l):
    return l[-1] + (extrapolate([b - a for a, b in pairwise(l)]) if any(l) else 0)

print(sum(map(extrapolate, data)))
print(sum(map(extrapolate, (l[::-1] for l in data))))
