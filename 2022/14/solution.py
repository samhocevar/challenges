#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    lines = [list(tuple(map(int, str.split(s, ','))) for s in l.split()[::2]) for l in f]

bottom = max(list(zip(*sum(lines, [])))[-1])
size = bottom + 3

w, h = 2 * size, size
grid = np.zeros(w * h).astype(int).reshape(h, w)

for l in lines:
    for p, q in zip(l, l[1:]):
        if p[0] == q[0]:
            for y in range(min(p[1], q[1]), max(p[1], q[1]) + 1):
                grid[(y, p[0] - 500 + size)] = 9            
        else:
            for x in range(min(p[0], q[0]), max(p[0], q[0]) + 1):
                grid[(p[1], x - 500 + size)] = 9            

def fill(grid, c):
    for n in range(w * h):
        x, y = size, 0
        while True:
            if y + 1 == h:
                return n
            for x2 in (x, x - 1, x + 1):
                if grid[(y + 1, x2)] not in (c, 9):
                    x, y = x2, y + 1
                    break
            else:
                grid[(y, x)] = c
                if y == 0:
                    return n + 1
                break

print(fill(grid, 1))

for x in range(w):
    grid[(bottom + 2, x)] = 9

print(fill(grid, 2))
