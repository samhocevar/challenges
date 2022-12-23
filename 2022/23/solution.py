#!/usr/bin/env python

from itertools import count
from collections import defaultdict
import numpy as np

with open('input.txt') as f:
    grid = np.array(list([".#".index(c) for c in l] for l in map(str.strip, f)))

DIRS =  [(-1, 0), (1, 0), (0, -1), (0, 1)]
MASKS = [    0x7,  0x1c0,    0x49,  0x124]

for n in count(1):
    # Pad grid and compute neighbourhoods through convolution
    #  0x1   0x2   0x4
    #  0x8  0x10  0x20
    #  0x40 0x80 0x100
    grid = np.pad(grid, 1, constant_values=0)
    neig = np.pad(grid[:,:-1], ((0, 0), (1, 0))) + (grid << 1) + (np.pad(grid[:,1:], ((0, 0), (0, 1))) << 2)
    neig = np.pad(neig[:-1,:], ((1, 0), (0, 0))) + (neig << 3) + (np.pad(neig[1:,:], ((0, 1), (0, 0))) << 6)

    # Look where each elf wants to move; only keep destinations targeted by one elf
    moves = defaultdict(list)
    for p in np.argwhere(np.logical_and(grid, neig & ~0x10)):
        for d in [(k + n - 1) % 4 for k in range(4)]:
            if neig[tuple(p)] & MASKS[d] == 0:
                moves[(p[0] + DIRS[d][0], p[1] + DIRS[d][1])].append(p)
                break
    moves = {dst: tuple(src[0]) for dst, src in moves.items() if len(src) == 1}
    for dst, src in moves.items():
        grid[src], grid[dst] = 0, 1

    if not moves:
        print(n)
        break

    # Shrink grid to save some memory
    while not grid[-1,:].any(): grid = grid[:-1,:]
    while not grid[ 0,:].any(): grid = grid[1:, :]
    while not grid[:,-1].any(): grid = grid[:,:-1]
    while not grid[:, 0].any(): grid = grid[:, 1:]

    if n == 10:
        print(grid.size - grid.sum())
