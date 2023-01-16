#!/usr/bin/env python

from itertools import combinations
from operator import sub, add

scanners = []
with open('input.txt') as f:
    for l in map(str.strip, f):
        if l[0:2] == '--':
            scanners.append([])
        elif l:
            scanners[-1].append(tuple(int(x) for x in l.split(',')))

def sqdist(p1, p2):
    return sum(x * x for x in map(sub, p1, p2))

def mandist(p1, p2):
    return sum(map(abs, map(sub, p1, p2)))

def rotate(p, r):
    x, y, z = p
    match r // 8:
        case 1: x, y, z = y, z, x
        case 2: x, y, z = z, x, y
    if r & 4:
        x, y = -x, -y
    match r % 4:
        case 1: y, z = z, -y
        case 2: y, z = -y, -z
        case 3: y, z = -z, y
    return x, y, z

# Compute distances between pairs of points
dists = [{} for _ in scanners]
for ds, s in zip(dists, scanners):
    for i in range(len(s)):
        for j in range(i):
            ds[sqdist(s[i], s[j])] = (i, j)

# Try to position a scanner with the help of reference scanners
def match_scanner(n1, refs):
    for r in range(24):
        ptlist1 = [rotate(p, r) for p in scanners[n1]]
        for n0 in refs:
            ptset0 = set(scanners[n0])
            found = False
            for ds, (i0, j0) in dists[n0].items():
                p0 = scanners[n0][i0]
                if ds not in dists[n1]:
                    continue
                i1, j1 = dists[n1][ds]
                for p1 in (ptlist1[i1], ptlist1[j1]):
                    delta = tuple(map(sub, p0, p1))
                    if len(set(scanners[n0]) & set(tuple(map(add, p, delta)) for p in ptlist1)) >= 12:
                        return r, delta
    return -1, 0

# Initialise scanner 0 and study all the others
todo = list(range(1, len(scanners)))
origins = {0: (0, 0, 0)}
while todo:
    n1 = todo.pop()
    r, delta = match_scanner(n1, origins.keys())
    if r >= 0:
        origins[n1] = delta
        scanners[n1] = [tuple(map(add, rotate(p, r), delta)) for p in scanners[n1]]
    else:
        todo = [n1] + todo # Skip this scanner and try again later

print(len(set.union(*map(set, scanners))))
print(max(mandist(p, q) for p, q in combinations(origins.values(), 2)))
