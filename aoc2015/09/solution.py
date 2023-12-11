#!/usr/bin/env python

from itertools import permutations, pairwise

with open('input.txt') as f:
    data = {(a, b): int(c) for a, b, c in [(l.split()[::2]) for l in f]}

# Fill map with return journeys for convenience
for k, v in list(data.items()):
    data[k[::-1]] = v

# Compute all trip combinations and print min and max of their total distances
print(min(sum(data[(a, b)] for a, b in pairwise(p)) for p in permutations(set(next(zip(*data))))))
print(max(sum(data[(a, b)] for a, b in pairwise(p)) for p in permutations(set(next(zip(*data))))))
