#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    data = [[1 if c == '#' else 0 for c in l] for l in map(str.strip, f)]

lut = data[0]
grid = np.pad(np.array(data[2:]), 3)

for n in range(50):
    h, w = np.shape(grid)
    dest = np.zeros((w - 2) * (h - 2)).astype(int).reshape(w - 2, h - 2)
    for y in range(h - 2):
        for x in range(w - 2):
            bits = sum(b << i for i, b in enumerate(grid[y:y+3,x:x+3].reshape(9)[::-1]))
            dest[(y, x)] = lut[bits]
    grid = np.pad(dest, 2, constant_values=dest[(0,0)])
    if n + 1 in [2, 50]:
        print(len(np.nonzero(grid)[0]))
