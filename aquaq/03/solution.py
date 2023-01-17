#!/usr/bin/env python

n, x, y = 0, 2, 0
with open('input.txt') as f:
    for c in next(f).strip():
        x2, y2 = x, y
        match c:
            case 'U': y2 -= 1
            case 'D': y2 += 1
            case 'L': x2 -= 1
            case 'R': x2 += 1
        if abs(2.5 - x2) + abs(2.5 - y2) <= 3:
            x, y = x2, y2
        n += x + y
print(n)
