#!/usr/bin/env python

import re

data = []
with open('input.txt') as f:
    for l in map(str.rstrip, f):
        if not l: break
        data.append([" .#".index(c) - 1 for c in l])
    seq = re.split("(?=[LR])|(?=\d)(?<=[LR])", next(f).strip())
h = len(data)

def step_flat(x, y, d):
    match d:
        case 0: # Right
            x = (x + 1) % len(data[y])
            while data[y][x] == -1: x += 1
        case 1: # Down
            y = (y + 1) % h
            while len(data[y]) <= x or data[y][x] == -1:
                y = (y + 1) % h
        case 2: # Left
            x = (x + len(data[y]) - 1) % len(data[y])
            if data[y][x] == -1: x = len(data[y]) - 1
        case 3: # Up
            y = (y + h - 1) % h
            while len(data[y]) <= x or data[y][x] == -1:
                y = (y + h - 1) % h
    return x, y, d

A, B, C, D = (h * n // 4 for n in range(1, 5))

def step_cube(x, y, d):
    # Hand-tuned for my specific shape because I can’t be bothered
    #   0  A  B  C
    # 0    +--+--+
    #      |  |  |
    # A    +--+--+
    #      |  |
    # B +--+--+
    #   |  |  |
    # C +--+--+
    #   |  |
    # D +--+
    match d:
        case 0: # Right
            x += 1
            if x >= len(data[y]):
                if y < A: return B - 1, C - 1 - y, 2
                if y < B: return A + y,     A - 1, 3
                if y < C: return C - 1, C - 1 - y, 2
                return           y - B,     C - 1, 3
        case 1: # Down
            y += 1
            if y >= h or x >= len(data[y]):
                if x < A: return B + x,     0, 1
                if x < B: return A - 1, B + x, 2
                return           B - 1, x - A, 2
        case 2: # Left
            x -= 1
            if x < 0 or data[y][x] == -1:
                if y < A: return     0, C - 1 - y, 0
                if y < B: return y - A,         B, 1
                if y < C: return     A, C - 1 - y, 0
                return           y - B,         0, 1
        case 3: # Up
            y -= 1
            if y < 0 or data[y][x] == -1:
                if x < A: return     A, A + x, 0
                if x < B: return     0, x + B, 0
                return           x - B, D - 1, 3
    return x, y, d

def march(stepper):
    x, y, d = data[0].index(0), 0, 0
    for a in seq:
        match a:
            case 'L': d = (d + 3) % 4
            case 'R': d = (d + 1) % 4
            case _:
                for _ in range(int(a)):
                    x2, y2, d2 = stepper(x, y, d)
                    if data[y2][x2] == 1:
                        break
                    x, y, d = x2, y2, d2
    print(1000 * (y + 1) + 4 * (x + 1) + d)

march(step_flat)
march(step_cube)
