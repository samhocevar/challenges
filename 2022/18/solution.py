#!/usr/bin/env python

from operator import add
import numpy as np

with open('input.txt') as f:
    droplets = [list(map(int, s.split(','))) for s in map(str.strip, f)]

size = 3 + max(*sum(droplets, []))
grid = np.zeros(size * size * size).astype(int).reshape(size, size, size)

for x, y, z in droplets:
    grid[(z + 1, y + 1, x + 1)] = 1

print(sum(np.count_nonzero(np.diff(grid, axis=n)) for n in range(3)))

todo = [(0,0,0)]
while todo:
    p = todo.pop()
    grid[p] = 3
    for d in [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]:
        p2 = tuple(map(add, p, d))
        if all(c >= 0 and c < size for c in p2) and grid[p2] == 0:
            todo.append(p2)
grid = (3 - grid) // 2

print(sum(np.count_nonzero(np.diff(grid, axis=n)) for n in range(3)))
