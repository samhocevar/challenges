#!/usr/bin/env python

with open('input.txt') as f:
    data = list(map(str.strip, f))

w, h = len(data[0]), len(data)

p = 1
for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    n = sum(1 for i, y in enumerate(range(dy, h, dy), 1) if data[y][i * dx % w] == '#')
    if dx == 3 and dy == 1:
        print(n)
    p *= n
print(p)
