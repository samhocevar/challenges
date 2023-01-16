#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    data = [[".#".index(c) for c in l] for l in map(str.strip, f)]

def step(grid):
    grid = np.pad(grid, 1)
    tmp = grid
    for axis in range(tmp.ndim):
        s1 = tuple(slice(0, -1) if axis == n else slice(None) for n in range(tmp.ndim))
        s2 = tuple(slice(1, None) if axis == n else slice(None) for n in range(tmp.ndim))
        p1 = tuple((int(axis == n), 0) for n in range(tmp.ndim))
        p2 = tuple((0, int(axis == n)) for n in range(tmp.ndim))
        tmp = tmp + np.pad(tmp[s1], p1) + np.pad(tmp[s2], p2)
    return np.logical_or(tmp == 3, np.logical_and(tmp == 4, grid == 1)).astype(int)

def count(grid, n):
    for _ in range(n):
        grid = step(grid)
    return np.count_nonzero(grid)

print(count(np.array([data]), 6))
print(count(np.array([[data]]), 6))
