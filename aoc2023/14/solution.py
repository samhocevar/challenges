#!/usr/bin/env python

from itertools import count
from re import sub

with open('input.txt') as f: data = tuple(l.strip() for l in f.readlines())

# Rotate (clockwise): transpose the map (zip) and reverse each line
def rot(m): return tuple(''.join(reversed(l)) for l in zip(*m))

# Tilt (eastwards): find all groups of 'O' and '.' and just sort them!
def tilt(m): return tuple(sub("[O.]+", lambda g: ''.join(sorted(g.group(0))), s) for s in m)

# Compute load: count the 'O's on each line
def load(m): return sum(n * l.count('O') for n, l in enumerate(reversed(m), 1))

# Part 1: rotate once, tilt eastwards, rotate 3 more times, and compute load
print(load(rot(rot(rot(tilt(rot(data)))))))

# Perform the 4-time rotate/tilt operation until we find a cycle. Keep a history
# of all the maps we have seen so we can immediately retrieve the one we want.
hist = dict()
for n1 in count():
    if (n0 := hist.get(data)) is not None: break
    hist[data] = n1
    for _ in range(4): data = tilt(rot(data))

# Part 2: compute the load of the map that has the same order as the 1000000000th
print(load(next(m for m, n in hist.items() if n - n0 == (1000000000 - n0) % (n1 - n0))))
