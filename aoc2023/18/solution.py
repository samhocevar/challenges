#!/usr/bin/env python

from itertools import pairwise, batched
from re import findall

with open('input.txt') as f: data = [findall(r'\w+', l) for l in f.readlines()]

def dig(data):
    total, x, y, vlines, hlines = 0, 0, 0, [], []
    # Run the digger and just build a list of all the vertical lines
    for d, n in data:
        x, y, oldy = x + [n, 0, -n, 0][d], y + [0, -n, 0, n][d], y
        if d % 2: vlines.append((x, oldy, y))
    # Now consider all the rectangles formed by our Y coordinates and any relevant
    # X coordinates. Don’t forget to remove the cells that were counted twice because
    # they were also in the previous line.
    for ymin, ymax in pairwise(sorted({y for _, y, _ in vlines})):
        hlines, oldlines = list(sorted(x for x, y1, y2 in vlines if min(y1, y2) < (ymin + ymax) / 2 < max(y1, y2))), hlines
        for xmin, xmax in batched(hlines, 2):
            total += (ymax - ymin + 1) * (xmax - xmin + 1)
            total -= sum(max(0, min(x2, xmax) - max(x1, xmin) + 1) for x1, x2 in batched(oldlines, 2))
    return total

# Part 1: data is found in the first two columns
print(dig([('RULD'.find(a), int(b)) for a, b, _ in data]))

# Part 2: data is now found in the last column
print(dig([(int(c[-1]), int(c[:-1], 16)) for _, _, c in data]))
