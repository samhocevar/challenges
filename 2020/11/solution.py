#!/usr/bin/env python

from collections import defaultdict
from itertools import product, count
import numpy as np

DIRS = [(i, j) for i, j in product(range(-1, 2), range(-1, 2)) if i or j]

with open('input.txt') as f:
    data = np.array([[".L".index(x) for x in l.strip()] for l in f])
grid = np.pad(data, 1)
h, w = grid.shape

# Compute neighbours to improve step 2
neighbours = defaultdict(list)
for y, x in product(range(1, h - 1), range(1, w - 1)):
    if grid[(y, x)] == 0:
        continue
    for dx, dy in DIRS:
        for n in count(1):
            x2, y2 = x + n * dx, y + n * dy
            if x2 < 0 or y2 < 0 or x2 >= w or y2 >= h:
                break
            if grid[(y2, x2)] > 0:
                neighbours[(y, x)].append((y2, x2))
                break

def solve(grid, mode):
    while True:
        on, off = [], []
        for y, x in product(range(1, h - 1), range(1, w - 1)):
            s = grid[(y, x)]
            if s == 0:
                continue
            if mode == 1:
                neigh = [grid[(y + dy, x + dx)] for dx, dy in DIRS]
            else:
                neigh = [grid[(y2, x2)] for y2, x2 in neighbours[(y, x)]]
            if s == 1 and max(neigh) == 1:
                on.append((y, x))
            elif s == 2 and sum(n & 2 for n in neigh) // 2 >= 3 + mode:
                off.append((y, x))
        if on:
            grid[tuple(zip(*on))] = 2
        if off:
            grid[(tuple(zip(*off)))] = 1
        if len(on) + len(off) == 0:
            return np.count_nonzero(grid == 2)

print(solve(grid.copy(), 1))
print(solve(grid.copy(), 2))
