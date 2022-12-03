#!/usr/bin/env python

import numpy as np
import sys

with open('input.txt') as f:
    data = []
    for line in f:
        v = [int(x) for x in line.strip().replace(' -> ', ',').split(',')]
        data.append(v)
    size = max(max(v) for v in data) + 1

g1 = np.zeros(size * size).reshape(size, size)
g2 = np.zeros(size * size).reshape(size, size)

for v in data:
    xd = 1 if v[2] > v[0] else -1
    xs = list(range(v[0], v[2] + xd, xd))
    yd = 1 if v[3] > v[1] else -1
    ys = list(range(v[1], v[3] + yd, yd))

    if len(xs) == 1:
        xs *= len(ys)
    if len(ys) == 1:
        ys *= len(xs)

    if v[0] == v[2] or v[1] == v[3]:
        for x, y in zip(xs, ys):
            g1[(x, y)] += 1

    for x, y in zip(xs, ys):
        g2[(x, y)] += 1

print(len(np.nonzero(g1 > 1)[0]))
print(len(np.nonzero(g2 > 1)[0]))
