#!/usr/bin/env python

from heapq import *

with open('input.txt') as f:
    data = [l.strip() for l in f.readlines()]
    w, h, start = len(data[0]), len(data), max((l.find('S'), n) for n, l in enumerate(data))

# Standard path finding with separate even/odd visited sets
def run(count):
    todo, done = [(0, *start)], [set(), set()]
    while todo:
        cost, x, y = heappop(todo)
        if cost > count: return len(done[count % 2])
        if (x, y) not in done[cost % 2] and data[y % h][x % w] != '#':
            done[cost % 2].add((x, y))
            for x2, y2 in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
                heappush(todo, (cost + 1, x2, y2))

# Part 1: just walk around and count odd steps
print(run(64))

# Part 2: the tiling grows in a diamond shape due to the Manhattan distance,
# all the inner tiles are the same, and all the border tiles are the same, so
# we have values that grow either linearly or quadratically. We just compute
# the parameters for the ax² + bx + c formula. Strong assumption: w == h.
k1, k2, k3 = (run(26501365 % (w + h) + k * (w + h)) for k in range(3))
c = k3 - 3 * (k2 - k1); a = (k2 - 2 * k1 + c) // 2; b = k1 - a - c
x = (26501365 + w + h - 1) // (w + h)
print(a * x ** 2 + b * x + c)
