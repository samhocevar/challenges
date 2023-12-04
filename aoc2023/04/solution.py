#!/usr/bin/env python

from operator import and_
from re import findall

# Compute the number of wins for each card using set intersection
with open('input.txt') as f:
    wins = [len(and_(*map(lambda s: set(map(int, s.split())), findall(r'\d+ +[\d ]*', l)))) for l in f]

# Part 1: sum of all scores
print(sum(int(2 ** (w - 1)) for w in wins))

# Part 2: accumulate all numbers of copies and compute their sum
copies = [1] * len(wins)
for n, w in enumerate(wins):
    for k in range(w):
        copies[n + 1 + k] += copies[n]
print(sum(copies))
