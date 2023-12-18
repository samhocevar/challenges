#!/usr/bin/env python

with open('input.txt') as f: data = [l.split() for l in f.readlines()]

# Use the shoelace formula to compute the global area of the dug shape
# (https://en.wikipedia.org/wiki/Shoelace_formula). Note that this is not
# enough, we also need to dilate the shape by half a pixel (because the
# digging lines have thickness). To do so, we add the ½ length of every
# segment, and finally we add 1 because we did a full clockwise (or
# anticlockwise) rotation when closing the shape (¼ pixel per corner).
# Strong assumption: the path must not self-intersect!
def dig(data, sa=0, sb=0, x2=0, y2=0):
    for d, n in data:
        x2, y2, x1, y1 = x2 + [n, 0, -n, 0][d], y2 + [0, -n, 0, n][d], x2, y2
        sa, sb = sa + (x2 * y1 - y2 * x1), sb + abs(x2 - x1) + abs(y2 - y1)
    return abs(sa) // 2 + sb // 2 + 1

# Part 1: data is found in the first two columns
print(dig([('RULD'.find(a), int(b)) for a, b, _ in data]))

# Part 2: data is now found in the last column
print(dig([(int(c[-2]), int(c[2:-2], 16)) for _, _, c in data]))
