#!/usr/bin/env python

from operator import add, sub

moves = { 'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0) }

rope = [(0, 0)] * 10
visited1 = set()
visited2 = set()

with open('input.txt') as f:
    for direction, count in ((moves[l[0]], int(l[2:])) for l in f):
        for _ in range(count):
            rope[0] = tuple(map(add, rope[0], direction))
            for n in range(1, len(rope)):
                delta = tuple(map(sub, rope[n], rope[n-1]))
                if max(map(abs, delta)) == 2:
                    rope[n] = tuple(map(lambda x, d: x + int(d / 2), rope[n-1], delta))
            visited1.add(rope[1])
            visited2.add(rope[9])

print(len(visited1))
print(len(visited2))
