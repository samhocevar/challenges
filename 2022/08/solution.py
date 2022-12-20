#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    data = [list(map(int, l.strip())) for l in f]

grid = np.array(data)
top = 1 + np.amax(grid)
visibility = np.full(grid.shape, False)
score = np.ones(grid.shape).astype(int)

for _ in range(4):
    for y in range(grid.shape[0]):
        hmax = -1
        last = [0] * top
        for x in range(grid.shape[1]):
            h = grid[(y,x)]
            # Visibility: true if the tree is higher than the highest encountered tree so far.
            if h > hmax:
                visibility[(y,x)] = True
                hmax = h
            # Scenic score: distance to the last tree that was as high as the current one.
            score[(y,x)] *= x - last[h]
            last = [x] * (h + 1) + last[h+1:]
    # Rotate everything 90° and start again
    grid, visibility, score = map(np.rot90, (grid, visibility, score))

print(len(np.nonzero(visibility)[0]))
print(np.amax(score))

