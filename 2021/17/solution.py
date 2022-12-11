#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    coords = [int(x.strip(',').split('=')[-1:][0]) for x in next(f).replace('.', ' ').split()[2:]]

good_vy0 = set()
good_vx0vy0 = set()

try_vx0 = range(coords[1] + 1)
try_vy0 = range(coords[2] - 1, -coords[2] + 1)

# Find range of good_vx0vy0 y velocities
vy = np.array(try_vy0)
y = np.zeros(vy.shape).astype(int)
while any(vy > coords[2]):
    y += vy
    vy -= 1
    for c in np.argwhere(np.logical_and(y >= coords[2], y <= coords[3])):
        good_vy0.add(try_vy0[c[0]])

# For each valid y velocity, find all the valid x velocities
for vy0 in good_vy0:
    y, vy = 0, vy0
    vx = np.array(try_vx0)
    x = np.zeros(vx.shape)
    while y > coords[2]:
        y += vy
        vy -= 1
        x += vx
        vx = np.fix(vx * 0.9999)
        if y >= coords[2] and y <= coords[3]:
            for c in np.argwhere(np.logical_and(x >= coords[0], x <= coords[1])):
                good_vx0vy0.add((c[0], vy0))

print(max(vy * (vy + 1) // 2 for vy in good_vy0))
print(len(good_vx0vy0))
