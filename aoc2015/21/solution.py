#!/usr/bin/env python

from itertools import chain
from math import ceil

# Read input as [HP, damage, armor]
with open('input.txt') as f: data = [int(l.split()[-1]) for l in f]

# This is the data from the problem except there is an empty armor that costs 0
# gold and has 0 stats so that we can change the rules to "must have an armor"
shop = [[ (8, 4, 0), (10, 5, 0),  (25, 6, 0), (40, 7, 0), (74, 8, 0)],
        [ (0, 0, 0), (13, 0, 1),  (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)],
        [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2),  (80, 0, 3)]]

# Determine whether the player wins with the given inventory
def win(inv):
    phits = ceil(data[0] / max(1, sum([*zip(*inv)][1]) - data[2]))
    bhits = ceil(    100 / max(1, data[1] - sum([*zip(*inv)][2])))
    return phits <= bhits

# List all valid inventories
def combine(inv=set()):
    # Any inventory of size ≥ 2 is valid (has at least one weapon and one armor)
    if len(inv) >= 2: yield inv
    # Any inventory of size ≤ 3 can have a new item added to it; just make sure
    # that we don’t add the same item twice (only useful for rings)
    if len(inv) <= 3: yield from chain.from_iterable(combine(inv | {x}) for x in set(shop[min(2, len(inv))]) - inv)

# Part 1: print the min cost of winning inventories
print(min(sum(next(zip(*inv))) for inv in combine() if win(inv)))

# Part 2: print the max cost of losing inventories
print(max(sum(next(zip(*inv))) for inv in combine() if not win(inv)))
