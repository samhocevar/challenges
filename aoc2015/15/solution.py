#!/usr/bin/env python

from math import prod
from re import findall

with open('input.txt') as f: data = [list(map(int, findall('-?[0-9]+', l))) for l in f]

# Iterate over all integer k-tuples that sum to n
def partition(n, k):
    if k == 1: yield (n,); return
    for i in range(n + 1)[::-1]: yield from ((i, *p) for p in partition(n - i, k - 1))

# Compute the score of all combinations of ingredients; if 'cal' is specified, only
# consider recipes that sum to that many calories.
def combine(cal):
    for p in partition(100, len(data)):
        if cal in [0, sum(p[i] * data[i][4] for i in range(len(data)))]:
            yield prod(max(0, sum((p[i] * data[i][n] for i in range(len(data))))) for n in range(4))

print(max(combine(0)))
print(max(combine(500)))
