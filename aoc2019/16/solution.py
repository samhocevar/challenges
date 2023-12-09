#!/usr/bin/env python

from math import comb, perm
import numpy as np

with open('input.txt') as f:
    data = next(f).strip()

# Part 1: multiply data vector by the FFT matrix 100 times. Note that we
# cannot use numpy.linalg.matrix_power() because of integer overflows, thus
# the need to do % 10 after each multiplication instead.
def compute(v):
    m = np.array([[[0, 1, 0, -1][(i + 1) // (j + 1) % 4] for i in range(len(v))] for j in range(len(v))])
    for _ in range(100):
        v = abs(m.dot(v)) % 10
    return v[:8]

print(*compute(np.array([int(n) for n in data])), sep='')

# Part 2: we notice that the problem is shifted far enough to the right that
# the [0, 1, 0, -1] array becomes meaningless and we actualy just have to deal
# with an upper triangular matrix and its powers, e.g.:
#
#      [1 1 1 1 1 1]        [1 2 3 4 5 6]        [1 3 6 10 15 21]
#      [0 1 1 1 1 1]        [0 1 2 3 4 5]        [0 1 3  6 10 15]
#  m = [0 0 1 1 1 1]   m² = [0 0 1 2 3 4]   m³ = [0 0 1  3  6 10]
#      [0 0 0 1 1 1]        [0 0 0 1 2 3]        [0 0 0  1  3  6]
#      [0 0 0 0 1 1]        [0 0 0 0 1 2]        [0 0 0  0  1  3]
#      [0 0 0 0 0 1]        [0 0 0 0 0 1]        [0 0 0  0  0  1]
# 
# Other observations:
#  - we can store the matrix coefficients modulo 10
#  - we only care about the first line of the matrix, since the others
#    are just the first line shifted to the right
#  - element i of the (n+1)th power of m is: comb(n + i, n)
#      m[0] = [comb(99 + i, 99) for i in ...]
#  - there is also a simple recurrence formula to compute all coefficients:
#      m[n] = m[n-1] * (99 + n) / n

size, offset = len(data) * 10000, int(data[:7])
v = [int(data[n % len(data)]) for n in range(offset, size)]

l, x = [1], 1
while len(l) < size - offset:
    x = x * (99 + len(l)) // len(l)
    l.append(x % 10)

# Compute 8 dot products, each time shifting v to the right and l to the left
print(*(np.array(v[n:]).dot(l[0:-n or len(l)]) % 10 for n in range(8)), sep='')
