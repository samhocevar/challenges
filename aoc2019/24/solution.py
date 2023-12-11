#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    data = np.array([[c == '#' for c in l.strip()] for l in f]).astype(int)

# Part 1: simple iterations
bugs, seen = data, set()
while True:
    tmp = np.pad(bugs, 1, constant_values=0)
    tmp = tmp[1:-1,:-2] + tmp[1:-1,2:] + tmp[:-2,1:-1] + tmp[2:,1:-1]
    bugs = (abs(3 - bugs - 2 * tmp) <= 1).astype(int)
    bio = sum(x << n for n, x in enumerate(bugs.flat))
    if bio in seen: break
    seen.add(bio)

print(bio)

# Part 2: use a list of matrices for the recursion levels
bugs, zero = [data], np.zeros(data.shape).astype(int)
for _ in range(200):
    if bugs[0].any(): bugs.insert(0, zero)
    if bugs[-1].any(): bugs.append(zero)
    neighbours = []
    # First step: count neighbours
    for n in range(len(bugs)):
        tmp = np.pad(bugs[n], 1, constant_values=0)
        tmp = tmp[1:6,:5] + tmp[1:6,2:] + tmp[:5,1:6] + tmp[2:,1:6]
        # Count neighbours from the inside
        if n < len(bugs) - 1:
            for k in (0, 4):
                tmp[1 + k // 2][2] += sum(bugs[n + 1][k])
                tmp[2][1 + k // 2] += sum(bugs[n + 1][:, k])
        # Count neighbours from the outside
        if n > 0:
            for k in (0, 4):
                tmp[k] += bugs[n - 1][1 + k // 2][2]
                tmp[:, k] += bugs[n - 1][2][1 + k // 2]
        neighbours.append(tmp)
    # Second step: compute new bug population
    for n in range(len(bugs)):
        bugs[n] = (abs(3 - bugs[n] - 2 * neighbours[n]) <= 1).astype(int)
        bugs[n][2][2] = 0

print(sum(np.count_nonzero(m) for m in bugs))
