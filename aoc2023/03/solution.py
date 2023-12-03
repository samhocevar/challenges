#!/usr/bin/env python

from re import search, finditer

with open('input.txt') as f:
    data = list(map(str.strip, f))

# Build lists of all numbers (value, y, xstart, xend) and all symbols (char, y, x)
numbers = sum(([(int(m[0]), n, m.start(0), m.end(0)) for m in finditer('[0-9]+', l)] for n, l in enumerate(data)), [])
symbols = sum(([(m[0], n, m.start(0)) for m in finditer('[^0-9.]', l)] for n, l in enumerate(data)), [])

# Helper function to determine whether a symbol and a number are adjacent
def touch(s, n):
    return abs(n[1] - s[1]) <= 1 and s[2] + 1 >= n[2] and s[2] <= n[3]

# Everything is O(n²) but the dataset is not large enough for it to be a problem

# Part 1: sum of all numbers that touch at least one symbol
print(sum(n[0] for n in numbers if any(touch(s, n) for s in symbols)))

# Part 2: for each '*' symbol, build a list of adjacent numbers, then add their product to the sum if there are exactly 2
l = [[n for n in numbers if touch(s, n)] for s in symbols if s[0] == '*']
print(sum(t[0][0] * t[1][0] for t in l if len(t) == 2))

