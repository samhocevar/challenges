#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    data = [[int(x) for x in l.strip()] for l in f]
grid = np.array(data)

# Compute padded grid, as well as horizontal and vertical 1st order differences
high = np.amax(grid)
padded = np.pad(grid, (1, 1), mode='constant', constant_values=high)
dx = np.diff(padded, axis=0)
dy = np.diff(padded, axis=1)

# Find low points
lows = []
for a, v in np.ndenumerate(grid):
    y, x = a
    if max(dy[y+1, x], -dy[y+1, x+1], dx[y, x+1], -dx[y+1, x+1]) < 0:
        lows.append(a)

print(sum(1 + grid[a] for a in lows))

# Find basins
basins = []
for a in lows:
    todo = set([(a[0] + 1, a[1] + 1)])
    done = set()
    while todo:
        y, x = todo.pop()
        done.add((y, x))
        padded[y, x] = high
        for p in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if p not in done and padded[p] < high:
                todo.add(p)
    basins.append(len(done))

print(np.prod(sorted(basins)[-3:]))
