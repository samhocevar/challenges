#!/usr/bin/env python

from re import findall
import numpy as np

# l[6] is ' ' for toggle, 'n' for turn on, 'f' for turn off
with open('input.txt') as f: data = [(l[6], *map(int, findall('[0-9]+', l))) for l in f]

# Part 1: apply rules and count non-zero matrix elements
lights = np.zeros((1000, 1000)).astype(int)
for c, x0, y0, x1, y1 in data:
    if c == ' ': lights[x0:x1 + 1,y0:y1 + 1] ^= 1
    else:        lights[x0:x1 + 1,y0:y1 + 1] = c == 'n'
print(np.count_nonzero(lights))

# Part 1: apply new rules and sum all matrix elements
lights = np.zeros((1000, 1000)).astype(int)
for c, x0, y0, x1, y1 in data:
    if c == 'f': lights[x0:x1 + 1,y0:y1 + 1] = np.maximum(lights[x0:x1 + 1,y0:y1 + 1] - 1, 0)
    else:        lights[x0:x1 + 1,y0:y1 + 1] += 1 if c == 'n' else 2
print(sum(lights.flat))
