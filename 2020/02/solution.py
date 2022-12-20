#!/usr/bin/env python

s0, s1 = 0, 0

with open('input.txt') as f:
    for r, c, p in map(str.split, f):
        bounds = list(map(int, r.split('-')))
        n = sum(1 for x in p if x == c[0])
        s0 += n >= bounds[0] and n <= bounds[1]
        s1 += (p[bounds[0] - 1] == c[0]) != (p[bounds[1] - 1] == c[0])

print(s0)
print(s1)
