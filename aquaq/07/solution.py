#!/usr/bin/env python

from operator import gt
from collections import defaultdict

ratings = defaultdict(lambda: 1200)

with open('input.txt') as f:
    next(f)
    for a, b, s in map(lambda s: s.split(','), f):
        ra, rb = ratings[a], ratings[b]
        d = 20 / (1 + pow(10, (ra - rb) / 400))
        if gt(*map(int, s.split('-'))):
            d -= 20
        ratings[a], ratings[b] = ra + d, rb - d

print(int(max(ratings.values())) - int(min(ratings.values())))
