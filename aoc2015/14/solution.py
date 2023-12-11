#!/usr/bin/env python

from re import findall

with open('input.txt') as f: data = [list(map(int, findall('[0-9]+', l))) for l in f]

points = [0] * len(data)
for n in range(1, 2503 + 1):
    pos = list((n // (r[1] + r[2]) * r[1] + min(n % (r[1] + r[2]), r[1])) * r[0] for r in data)
    best = max(pos)
    points = [p + 1 if pos[i] == best else p for i, p in enumerate(points)]

print(best)
print(max(points))
