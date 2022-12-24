#!/usr/bin/env python

from heapq import *
import numpy as np

with open('input.txt') as f:
    grid = np.array([["#.<>^v".index(s) - 1 for s in l.strip()] for l in f])
grid = np.pad(grid, 1, constant_values=-1)
h, w = np.shape(grid)

def is_free(t, x, y):
    if grid[(y, x)] == -1:
        return False
    l = [(y, (x + t - 2) % (w - 4) + 2),
         (y, (x - t - 2) % (w - 4) + 2),
         ((y + t - 2) % (h - 4) + 2, x),
         ((y - t - 2) % (h - 4) + 2, x)]
    return all(grid[p] != n for n, p in enumerate(l, 1))

def compute(start, end):
    done = set()
    todo = []
    heappush(todo, start)
    while todo:
        t, x, y = heappop(todo)
        if (t, x, y) in done:
            continue
        done.add((t, x, y))
        if not is_free(t, x, y):
            continue
        if (x, y) == end:
            return t
        for x2, y2 in ((x - 1, y), (x + 1, y), (x, y), (x, y - 1), (x, y + 1)):
            heappush(todo, (t + 1, x2, y2))

n = compute((0, 2, 1), (w - 3, h - 2))
print(n)

n = compute((n, w - 3, h - 2), (2, 1))
n = compute((n, 2, 1), (w - 3, h - 2))
print(n)
