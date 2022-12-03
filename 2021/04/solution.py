#!/usr/bin/env python

import sys

# List of masks that indicate a winning grid
M0 = 0b11111
M1 = 0b100001000010000100001
MASKS = [
    M0, M0<<5, M0<<10, M0<<15, M0<<20,
    M1, M1<<1, M1<<2, M1<<3, M1<<4
]

grids = []
luts = []
states = []
wins = set()

with open('input.txt') as f:
    draw = [int(x) for x in f.readline().strip().split(',')]
    while True:
        line = f.readline()
        if not line:
            break
        grid = [[int(x) for x in f.readline().strip().split(' ') if x] for _ in range(5)]
        lut = {}
        for j in range(5):
            for i in range(5):
                lut[grid[j][i]] = 1 << (j * 5 + i)
        grids.append(grid)
        luts.append(lut)
        states.append(0)

def unmarked(k):
    total = 0
    for j in range(5):
        for i in range(5):
            if states[k] & (1 << (j * 5 + i)) == 0:
                total += grids[k][j][i]
    return total

# Draw numbers
for n in draw:
    for k in range(len(grids)):
        m = luts[k].get(n)
        if not m:
            continue
        states[k] |= m
        if k not in wins:
            if any(x & states[k] == x for x in MASKS):
                if len(wins) == 0:
                    # First grid to win!
                    print(n * unmarked(k))
                wins.add(k)
                if len(wins) == len(grids):
                    # Last grid to win!
                    print(n * unmarked(k))
