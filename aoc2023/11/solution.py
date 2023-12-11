#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    data = np.array([[c == '#' for c in l.strip()] for l in f])

# The list of galaxies is the list of non-zero cells in our world matrix
g = list(zip(*np.nonzero(data)))

# Scan the empty space along each axis (https://en.wikipedia.org/wiki/Prefix_sum)
s = [np.add.accumulate(data.sum(axis=1-k) == 0) for k in range(2)]

# For each pair (a, b) of galaxies, add their Manhattan distances plus the empty space
# between them. The prefix sums make the empty space calculation a simple subtraction.
def compute(n):
    return sum(abs(a[k] - b[k] + (n - 1) * (s[k][a[k]] - s[k][b[k]])) for a in g for b in g for k in range(2) if a > b)

print(compute(2))
print(compute(1000000))
