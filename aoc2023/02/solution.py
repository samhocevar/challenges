#!/usr/bin/env python

from itertools import groupby
from math import prod
from operator import itemgetter
from re import split as resplit

rules = { 'red': 12, 'green': 13, 'blue': 14 }

sum1, sum2 = 0, 0

with open('input.txt') as f:
    # Split each line along any of the ":;," characters followed by a space
    for game in map(lambda l: resplit('[:;,] ', l.strip()), f.readlines()):

        # Make a list of all (colour, count) tuples from this game
        data = [(s2, int(s1)) for s1, s2 in map(str.split, game[1:])]

        # Part 1: check that all colour counts are within the rules
        if all(n <= rules[c] for c, n in data):
            sum1 += int(game[0][5:])

        # Part 2: compute the max draw count of each colour and multiply them together
        sum2 += prod(max(n for _, n in t) for _, t in groupby(sorted(data), itemgetter(0)))

print(sum1)
print(sum2)
