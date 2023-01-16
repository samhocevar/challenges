#!/usr/bin/env python

from itertools import product
from operator import add, sub

def parse(wire):
    path = [(0, 0)]
    for s in wire.split(','):
        match s[0], int(s[1:]):
            case 'L', n: v = (-n, 0)
            case 'R', n: v = (n, 0)
            case 'U', n: v = (0, n)
            case 'D', n: v = (0, -n)
        path.append(tuple(map(add, path[-1], v)))
    return path

def iter_wire(w): return zip(w, w[1:])
def dist(p1, p2): return sum(map(abs, map(sub, p1, p2)))

def intersect(s1, s2):
    a, b, c, d = s1[0], s1[1], s2[0], s2[1]
    if a[0] >= min(c[0], d[0]) and a[0] <= max(c[0], d[0]):
        if c[1] >= min(a[1], b[1]) and c[1] <= max(a[1], b[1]):
            return (a[0], c[1])
    if c[0] >= min(a[0], b[0]) and c[0] <= max(a[0], b[0]):
        if a[1] >= min(c[1], d[1]) and a[1] <= max(c[1], d[1]):
            return (c[0], a[1])
    return None

with open('input.txt') as f:
    w1 = parse(next(f).strip())
    w2 = parse(next(f).strip())

# Part 1
l1 = [intersect(s1, s2) for s1, s2 in product(iter_wire(w1), iter_wire(w2))]
print(min(d for d in [dist((0, 0), p) for p in l1 if p] if d))

# Part 2
l2 = []
d1 = 0
for s1 in iter_wire(w1):
    d2 = 0
    for s2 in iter_wire(w2):
        if p := intersect(s1, s2):
            if dist((0, 0), p):
                l2.append(d1 + d2 + dist(s1[0], p) + dist(s2[0], p))
        d2 += dist(s2[0], s2[1])
    d1 += dist(s1[0], s1[1])
print(min(l2))
