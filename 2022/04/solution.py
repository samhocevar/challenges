#!/usr/bin/env python

o1, o2 = 0, 0

with open('input.txt') as f:
    for l in f:
        v = [int(x) for x in l.strip().replace('-',',').split(',')]
        o1 += (v[0]-v[2]) * (v[1]-v[3]) <= 0
        o2 += v[1] >= v[2] and v[3] >= v[0]

print(o1)
print(o2)
