#!/usr/bin/env python

from math import gcd, atan2
import numpy as np

with open('input.txt') as f:
    data = np.array([[-'.'.find(c) for c in l] for l in map(str.strip, f)])

def visibility(y, x):
    tmp = data.copy()
    tmp[(y, x)] = 0
    # For each other asteroid, compute the unit vector leading to it using gcd(), throw
    # a ray away from that asteroid using multiples of this vector, and double the value
    # of anything on the path.
    for y2, x2 in zip(*np.nonzero(tmp)):
        dy, dx = y2 - y, x2 - x
        j, i = dy // gcd(dx, dy), dx // gcd(dx, dy)
        for n in range(1, max(*tmp.shape)):
            y3, x3 = y2 + n * j, x2 + n * i
            if y3 < 0 or x3 < 0 or y3 >= tmp.shape[0] or x3 >= tmp.shape[1]:
                break
            tmp[(y3, x3)] *= 2
    # All visible asteroids are the ones whose value remained 1
    return sum(1 for _ in np.nonzero(tmp == 1)[0]), y, x, tmp

# Part 1: retrieve best asteroid count, coordinates, and the final map; just print the count
num, y0, x0, space = max(visibility(y, x) for y, x in zip(*np.nonzero(data)))
print(num)

# Part 2: sort asteroids first by number of occluders, then by clockwise angle
hit = sorted((space[y, x], -atan2(x - x0, y - y0), y, x, x0 - x, y0 - y) for y, x in zip(*np.nonzero(space)))
print(100 * hit[199][3] + hit[199][2])
