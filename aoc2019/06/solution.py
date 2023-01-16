#!/usr/bin/env python

import re

with open('input.txt') as f:
    orbits = {b: a for a, b in [l.split(')') for l in map(str.strip, f)]}

def path(s):
    ret = []
    while s != 'COM':
        s = orbits.get(s)
        ret.append(s)
    return ret

print(sum(len(path(k)) for k in orbits.keys()))

a = set(path('YOU'))
b = set(path('SAN'))
print(len(a) + len(b) - 2 * len(a & b))
