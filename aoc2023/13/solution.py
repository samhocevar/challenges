#!/usr/bin/env python

import numpy as np

# Load each pattern separately into a matrix
with open('input.txt') as f:
    data = [np.array([[c == '#' for c in l] for l in m.split('\n')]) for m in f.read().strip().split('\n\n')]

# Compare every vertical slice of the matrix with its possible mirror image. If they
# differ by exactly the smudge amount, return the reflection line position.
def mirror(m, smudges):
    for i in range(1, m.shape[0]):
        a, b = m[max(0, 2 * i - m.shape[0]):i], m[i:min(2 * i, m.shape[0])]
        if np.count_nonzero(a != b[::-1]) == smudges: return i

# Call mirror() on every matrix and its transposition (in order to find horizontal
# mirror lines, too). Part 1 is with smudge value 0 (exact match), part 2 is with
# smudge value 1 (one cell differs).
print(sum(mirror(m.transpose(), 0) or 100 * mirror(m, 0) for m in data))
print(sum(mirror(m.transpose(), 1) or 100 * mirror(m, 1) for m in data))
