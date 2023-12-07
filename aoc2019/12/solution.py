#!/usr/bin/env python

from itertools import count
from math import lcm
from re import findall
import numpy as np

with open('input.txt') as f:
    pos = np.array([[int(n) for n in findall('[-]?[0-9]+', l)] for l in map(str.strip, f)])

vel = np.zeros(pos.shape).astype(int)
states = [{}, {}, {}]
loops = [0, 0, 0]

for n in count(1):
    # Part 1: print energy after 1000 iterations
    if n == 1000:
        print(sum(sum(abs(v)) * sum(abs(vel[n])) for n, v in enumerate(pos)))
    # Apply gravity to velocity
    for i, p in enumerate(pos):
        vel[i] += sum(np.sign(p0 - p) for p0 in pos)
    # Apply velocity to position
    pos += vel
    # Look whether we already found this position somewhere
    for axis in range(3):
        if not loops[axis]:
            k = (*pos[:,axis], *vel[:,axis])
            if n0 := states[axis].get(k, 0):
                loops[axis] = n - n0
            states[axis][k] = n
    # Part 2: if all loops were found, print their least common multiple
    if all(loops):
        print(lcm(*loops))
        break
