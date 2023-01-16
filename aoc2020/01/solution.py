#!/usr/bin/env python

from itertools import combinations

with open('input.txt') as f:
    data = list(map(int, f))

print(next(a * b for a, b in combinations(data, 2) if a + b == 2020))
print(next(a * b * c for a, b, c in combinations(data, 3) if a + b + c == 2020))
