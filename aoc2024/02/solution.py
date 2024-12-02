#!/usr/bin/env python

from itertools import pairwise

with open('input.txt') as f:
    levels = [list(map(int, l.split())) for l in f]

# A level is safe if all pairwise differences are 1, 2 or 3 (reverse list if nonincreasing)
safe = lambda l: set(b - a for a, b in pairwise(l if l[0] < l[-1] else l[::-1])).issubset({1, 2, 3})

# Part 1: print count of all safe levels
print(sum(1 for l in levels if safe(l)))

# Part 2: for each level, compute safety by testing removal of one element
print(sum(1 for l in levels if any(safe(l[:n] + l[n + 1:]) for n in range(len(l)))))
