#!/usr/bin/env python

from collections import defaultdict
from itertools import cycle

with open('input.txt') as f:
    s = [int(l.split()[4]) for l in f]

# Part 1 is easy
die = cycle(range(1, 101))
state = [s[0], s[1], 0, 0]
for turn, p in enumerate(cycle([0, 1]), 1):
    roll = next(die) + next(die) + next(die)
    state[p] = (state[p] + roll - 1) % 10 + 1
    state[2 + p] += state[p]
    if state[2 + p] >= 1000:
        print(turn * 3 * state[3 - p])
        break

# Part 2 isn’t
forks = { 3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1 }
wins = [0, 0]
universes = {(s[0], s[1], 0, 0): 1}
for p in cycle([0, 1]):
    new = defaultdict(int)
    for s1, c1 in universes.items():
        for roll, c2 in forks.items():
            state = list(s1)
            state[p] = (state[p] + roll - 1) % 10 + 1
            state[2 + p] += state[p]
            if state[2 + p] >= 21:
                wins[p] += c1 * c2
            else:
                new[tuple(state)] += c1 * c2
    universes = new
    if not universes:
        print(max(wins))
        break
