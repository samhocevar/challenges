#!/usr/bin/env python

from itertools import permutations, pairwise
from re import findall

with open('input.txt') as f:
    data = {(l[0], l[2]): int(l[1]) for l in [findall('[A-Z][a-z]+|-?[0-9]+', s.replace('lose ', '-')) for s in f]}

names = list(set(next(zip(*data))))

print(max(sum(data[(a, b)] + data[(b, a)] for a, b in pairwise((names[0], *p, names[0]))) for p in permutations(names[1:])))
print(max(sum(data[(a, b)] + data[(b, a)] for a, b in pairwise(p)) for p in permutations(names)))
