#!/usr/bin/env python

import numpy as np

with open('input.txt') as f:
    data = np.array([[c == '#' for c in l.strip()] for l in f]).astype(int)

def step(lights, n, bug):
    for _ in range(n):
        tmp = np.pad(lights, 1, constant_values=0)
        tmp = tmp[:,:-2] + tmp[:,1:-1] + tmp[:,2:]
        tmp = tmp[:-2,:] + tmp[1:-1,:] + tmp[2:,:]
        lights = (abs(2 * tmp - 6 - lights) <= 1).astype(int)
        if bug:
            for j in range(2):
                for i in range(2):
                    lights[-j, -i] = 1
    return np.count_nonzero(lights)

print(step(data, 100, False))
print(step(data, 100, True))
