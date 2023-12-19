#!/usr/bin/env python

from itertools import product
from re import findall

# Read data as {(x, y): (used, avail)}
with open('input.txt') as f: data = {(t[0], t[1]): (t[3], t[4]) for t in [list(map(int, findall('[0-9]+', l))) for l in f] if t}

# Part 1: iterate over all possible pairs
print(sum(1 for a, b in product(data.items(), repeat=2) if a[0] != b[0] and a[1][0] and a[1][0] <= b[1][1]))

# Part 2: I solved this one by hand, because the problem is NP-hard.
#
# There is a "wall" of inaccessible full nodes between (30,19) and (37,19)
# The only empty cell is at (35,21)
#  6 moves to get the empty cell to (29,21)
#  21 moves to get the empty cell to (29,0)
#  8 moves to get the empty cell to (37,0)
#
# Now the data is in (36,0) and we need 5 * 36 moves to get it to (0,0)
# using the following steps:
#  # x .    # x #    # x #    # x #    . x #    x . #
#  # # #    # # .    # . #    . # #    # # #    # # #
#
# TODO: There is a way to make it more automatised using path finding, but
# it’ll still rely on assumptions such as the existence of wall nodes.
print(6 + 21 + 8 + 5 * 36)
