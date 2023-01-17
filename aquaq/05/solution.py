#!/usr/bin/env python

def rotate(c, front, left, top):
    match c:
        case 'U': return 7 - top, left, front
        case 'D': return top, left, 7 - front
        case 'L': return 7 - left, front, top
        case 'R': return left, 7 - front, top

d1 = (1, 2, 3)
d2 = (1, 3, 2)
s = 0
with open('input.txt') as f:
    for n, c in enumerate(next(f).strip()):
        d1 = rotate(c, *d1)
        d2 = rotate(c, *d2)
        if d1[0] == d2[0]:
            s += n
print(s)
