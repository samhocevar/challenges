#!/usr/bin/env python

with open('input.txt') as f:
    data = [l.strip() for l in f]

# Functions to rotate and slant a string
r = lambda d: [*map(''.join, map(reversed, zip(*d)))]
s = lambda d: [' ' * n + l + ' ' * (len(d) - 1 - n) for n, l in enumerate(d)]

# Part 1: count occurrences of XMAS or SAMX in all rotated versions of the data
print(sum(l.count('XMAS') + l.count('SAMX') for d in (data, r(data), r(s(data)), r(s(r(data)))) for l in d))

# Part 2: find all As and check for S and M on diagonal positions
print(sum(1 for y, l in enumerate(data[1:-1]) for x, c in enumerate(l[1:-1]) if c == 'A' and {data[y][x], data[y + 2][x + 2]} & {data[y][x + 2], data[y + 2][x]} == set('SM')))
