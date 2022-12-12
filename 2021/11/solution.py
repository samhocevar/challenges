#!/usr/bin/env python

from itertools import count
import numpy as np

with open('input.txt') as f:
    data = [[int(x) for x in l.strip()] for l in f]
grid = np.array(data)

# Pad grid and make a list of border cells that we want to ignore
padded = np.pad(grid, (1, 1), mode='constant', constant_values=0)
h, w = np.shape(padded)
ignore  = set((0, x) for x in range(w))
ignore |= set((h - 1, x) for x in range(w))
ignore |= set((y, 0) for y in range(h))
ignore |= set((y, w - 1) for y in range(h))

def step(padded):
    padded += 1
    done = set()
    todo = set((a[0], a[1]) for a in np.argwhere(padded > 9)) - ignore
    while todo:
        a = todo.pop()
        padded[a] = 0
        done.add(a)
        for y in range(-1, 2):
            for x in range(-1, 2):
                a2 = (a[0] + y, a[1] + x)
                if a2 in ignore or a2 in done:
                    continue
                padded[a2] += 1
                if padded[a2] > 9:
                    todo.add(a2)
    return len(done) #- len(ignore)

n = 0
for i in count(start=1):
    flashed = step(padded)
    n += flashed
    if i == 100:
        print(n)
    if flashed == np.size(grid):
        print(i)
        break

