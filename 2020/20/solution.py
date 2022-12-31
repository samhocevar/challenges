#!/usr/bin/env python

from functools import reduce
from itertools import product
from math import prod, sqrt
import numpy as np

TSIZE = 10
TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3

def dual(n): return 4 + (4 - n) % 4

MONSTER = np.array([' #'.index(c) for c in \
    "                  # "
    "#    ##    ##    ###"
    " #  #  #  #  #  #   "]).reshape(3, 20)

# Read all tiles
data = []
with open('input.txt') as f:
    for l in map(str.strip, f):
        if not l: continue
        data.append([int(l[5:9]), np.array([['.#'.index(c) for c in next(f)[:TSIZE]] for _ in range(TSIZE)])])
SIZE = int(sqrt(len(data)))
if SIZE * SIZE != len(data):
    raise Exception('Duh, not a square jigsaw?')

# Store cropped tiles, list all edges, and count how many times each edge appears
tiles, edges = {}, {}
stats = [0] * (1 << TSIZE)
for n, t in data:
    tiles[n] = t[1:-1,1:-1]
    e = []
    for i in range(8):
        v = sum([b << k for k, b in enumerate(t[TOP])])
        e.append(v)
        stats[v] += 1
        t = np.rot90(t)
        if i == 3: t = np.fliplr(t)
    edges[n] = e

# Keep track of already placed tiles
placed = set()

# Find a top-left corner; make sure the tile is properly oriented
def find_corner():
    for n, t in tiles.items():
        if n in placed:
            continue
        e = edges[n]
        for _ in range(4):
            if stats[e[TOP]] == 1 and stats[e[LEFT]] == 1:
                tiles[n], edges[n] = t, e
                return n
            e = e[1:4] + e[:1] + e[7:] + e[4:7]
            t = np.rot90(t)

# Find a tile with the given edge (orientation, value)
def find_edge(o, v):
    for n, t in tiles.items():
        if n in placed:
            continue
        e = edges[n]
        for i in range(8):
            if e[o] == v:
                tiles[n], edges[n] = t, e
                return n
            e = e[1:4] + e[:1] + e[7:] + e[4:7]
            t = np.rot90(t)
            if i == 3:
                t = np.fliplr(t)
                e = e[4:] + e[:4]
    raise Exception('Something went wrong, need to backtrack?')

# Part 1: build the puzzle piece by piece. It looks like every edge
# is unique, at least in my input, so no need to backtrack!
array = np.zeros(SIZE * SIZE).astype(int).reshape(SIZE, SIZE)
for (y, x) in product(*[range(SIZE)] * 2):
    if (y, x) == (0, 0):
        n = find_corner()
    elif x > 0:
        n = find_edge(LEFT, edges[array[(y, x - 1)]][dual(RIGHT)])
    else:
        n = find_edge(TOP, edges[array[(y - 1, x)]][dual(BOTTOM)])
    array[(y, x)] = n
    placed.add(n)

print(prod(array[[0, 0, -1, -1], [0, -1, 0, -1]].tolist()))

# Part 2: create a large matrix and try to fit the monster in each
# of the 8 possible orientations. Stop at the first match.
big = reduce(lambda a, b: np.append(a, b, axis=0),
             (reduce(lambda a, b: np.append(a, b, axis=1),
                     map(tiles.get, array[n])) for n in range(SIZE)))
required = np.count_nonzero(MONSTER)
for i in range(8):
    matches = 0
    for y in range(big.shape[0] - MONSTER.shape[0]):
        for x in range(big.shape[1] - MONSTER.shape[1]):
            t = big[y:y+MONSTER.shape[0],x:x+MONSTER.shape[1]]
            if np.count_nonzero(MONSTER * t) == required:
                matches += 1
    if matches:
        print(np.count_nonzero(big) - matches * required)
        break
    big = np.rot90(big)
    if i== 3: big = np.fliplr(big)
