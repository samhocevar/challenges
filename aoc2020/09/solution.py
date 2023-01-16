#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations, accumulate

with open('input.txt') as f:
    data = list(map(int, f))
sums = list(accumulate(data))

WINDOW = 25

# Pre-seed set of valid sums
valid = defaultdict(int)
for i, j in combinations(data[:WINDOW], 2):
    valid[i + j] += 1

# Check numbers one by one
for n in range(WINDOW, len(data)):
    if valid[data[n]] == 0:
        print(data[n])
        i, j = next((i, j) for i, j in combinations(range(len(sums)), 2) if sums[j] - sums[i] == data[n])
        print(min(data[i+1:j+1]) + max(data[i+1:j+1]))
        break
    for i in range(1, WINDOW):
        valid[data[n - WINDOW] + data[n - i]] -= 1
        valid[data[n] + data[n - i]] += 1
