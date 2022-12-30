#!/usr/bin/env python

from collections import defaultdict
from itertools import chain
from operator import add
import re

steps = {'e':  (2, 0), 'ne':  (1, 1), 'se':  (1, -1),
         'w': (-2, 0), 'nw': (-1, 1), 'sw': (-1, -1)}

vadd = lambda p1, p2: tuple(map(add, p1, p2))

def decode(s):
    x, y = 0, 0
    for d in re.split('(?<=[ew])(?=.)', s):
        x, y = vadd((x, y), steps[d])
    return (x, y)

def step(state):
    neighbours = defaultdict(int)
    for p, n in state.items():
        if n:
            for d in steps.values():
                neighbours[vadd(p, d)] += 1
    for p, n in state.items():
        if n == 1 and neighbours[p] not in (1, 2):
            state[p] = 0
    for p, n in neighbours.items():
        if n == 2 and state[p] == 0:
            state[p] = 1

state = defaultdict(int)
with open('input.txt') as f:
    for l in map(str.strip, f):
        state[decode(l)] ^= 1
print(sum(state.values()))

for _ in range(200):
    step(state)
print(sum(state.values()))
