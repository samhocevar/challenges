#!/usr/bin/env python

from itertools import count
from collections import defaultdict
import numpy as np

with open('input.txt') as f:
    grid = np.array(list(["#.".index(c) for c in l] for l in map(str.strip, f)))

for n in count(1):
    # Pad grid
    grid = np.pad(grid, 1, constant_values=1)
    h, w = grid.shape

    moves = defaultdict(list)
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if grid[(y, x)]:
                continue
            neighbours = [[grid[(y + j, x + i)] for i in range(-1, 2)] for j in range(-1, 2)]
            if sum(map(sum, neighbours)) == 8:
                continue
            for d in range(4):
                match (d + n - 1) % 4:
                    case 0: # North
                        if sum(neighbours[0]) == 3: moves[(y - 1, x)].append((y, x)); break
                    case 1: # South
                        if sum(neighbours[2]) == 3: moves[(y + 1, x)].append((y, x)); break
                    case 2: # West
                        if all(neighbours[n][0] for n in range(3)): moves[(y, x - 1)].append((y, x)); break
                    case 3: # East
                        if all(neighbours[n][2] for n in range(3)): moves[(y, x + 1)].append((y, x)); break
    if not moves:
        print(n)
        break

    for dst, src in moves.items():
        if len(src) == 1:
            grid[src[0]] = 1
            grid[dst] = 0

    # Shrink grid
    while grid[-1,:].all(): grid = grid[:-1,:]
    while grid[ 0,:].all(): grid = grid[1:, :]
    while grid[:,-1].all(): grid = grid[:,:-1]
    while grid[:, 0].all(): grid = grid[:, 1:]

    if n == 10:
        print(grid.sum())
