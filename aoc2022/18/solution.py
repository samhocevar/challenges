#!/usr/bin/env python

from operator import add
import numpy as np

with open('input.txt') as f:
    droplets = tuple(zip(*((1 + int(c) for c in l.split(',')) for l in f)))
size = 2 + max(*sum(droplets, ()))

grid = np.zeros(size * size * size).astype(int).reshape(size, size, size)
grid[droplets] = 1

print(s := sum(np.count_nonzero(np.diff(grid, axis=a)) for a in range(3)))

todo = [(0,0,0)]
while todo:
    p = todo.pop()
    grid[p] = 1
    for d in [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]:
        p2 = tuple(map(add, p, d))
        if all(c >= 0 and c < size for c in p2) and grid[p2] == 0:
            todo.append(p2)

print(s - sum(np.count_nonzero(np.diff(grid, axis=a)) for a in range(3)))
