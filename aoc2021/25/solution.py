#!/usr/bin/env python

import numpy as np
from itertools import count

g2ch = '.> v    '
ch2g = {'.': 0, '>': 1, 'v': 3}

with open('input.txt') as f:
    grid = np.array([[ch2g[ch] for ch in l] for l in map(str.strip, f)])
h, w = np.shape(grid)

def step(grid):
    # Move left
    tmp = np.append(grid[:,-1:], grid, axis=1).reshape(h, w + 1)
    tmp = np.diff(tmp, axis=1)
    tmp = (tmp == -1).astype(int)
    moved = np.count_nonzero(tmp)
    tmp = np.append(tmp, tmp[:,:1], axis=1).reshape(h, w + 1)
    tmp = np.diff(tmp, axis=1)
    grid -= tmp

    # Move bottom
    tmp = np.append(grid[-1:,:], grid, axis=0).reshape(h + 1, w)
    tmp = np.diff(tmp, axis=0)
    tmp = (tmp == -3).astype(int) * 3
    moved += np.count_nonzero(tmp)
    tmp = np.append(tmp, tmp[:1,:], axis=0).reshape(h + 1, w)
    tmp = np.diff(tmp, axis=0)
    grid -= tmp

    return moved

for n in count(1):
    if step(grid) == 0:
        print(n)
        break
