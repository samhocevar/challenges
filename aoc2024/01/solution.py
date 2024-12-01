#!/usr/bin/env python

from collections import Counter

with open('input.txt') as f:
    left, right = zip(*(map(int, l.split()) for l in f))

# Part 1: sort, compute distance, sum
print(sum(map(lambda x, y: abs(x - y), sorted(left), sorted(right))))

# Part 2: count occurrences, multiply, sum
f = Counter(right)
print(sum(map(lambda x: x * f[x], left)))
