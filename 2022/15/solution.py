#!/usr/bin/env python

from re import findall
from collections import defaultdict

with open('input.txt') as f:
    data = [tuple(map(int, findall("-?[0-9]+", l))) for l in f]

y0 = 2000000

tmp, ranges = [], []
for sx, sy, bx, by in data:
    delta = abs(sx - bx) + abs(sy - by) - abs(sy - y0)
    if delta >= 0:
        tmp.append([sx - delta, sx + delta + 1])
for i in sorted(tmp):
    if not ranges or ranges[-1][1] < i[0]:
        ranges.append(i)
    elif ranges[-1][1] < i[1]:
        ranges[-1][1] = i[1]

print(sum(i[1] - i[0] for i in ranges) - len(set([s[2] for s in data if s[3] == y0])))

# List all lozenge outlines (dilated 1)
lines = []
for sx, sy, bx, by in data:
    r = abs(sx - bx) + abs(sy - by)
    lines.append([sx - r - 1, sy, sx - 1, sy + r])
    lines.append([sx, sy + r + 1, sx + r, sy + 1])
    lines.append([sx + 1, sy - r, sx + r + 1, sy])
    lines.append([sx - r, sy - 1, sx, sy - r - 1])

# Compute pairwise line intersections
intersects = defaultdict(int)
for i, l in enumerate(lines):
    for b in lines[i + 1:]:
        a = l
        if (a[0] + a[1] + b[0] + b[1]) % 2:
            continue # Wrong parity, lines can’t share any pixels
        if (a[3] - a[1]) * (b[3] - b[1]) > 0:
            continue # Lines are parallel
        if a[3] < a[1]:
            a, b = b, a # Ensure first segment grows in Y
        kx = (b[0] + b[1] + a[0] - a[1]) // 2
        ky = (b[0] + b[1] - a[0] + a[1]) // 2
        if kx >= 0 and ky >= 0 and kx <= 2 * y0 and ky <= 2 * y0:
            intersects[(kx, ky)] += 1

# Check any point that is part of at least 4 intersections
for (x, y), c in intersects.items():
    if c < 4:
        continue
    for sx, sy, bx, by in data:
        if abs(sx - x) + abs(sy - y) <= abs(sx - bx) + abs(sy - by):
            break
    else:
        print(x * 4000000 + y)
        break

