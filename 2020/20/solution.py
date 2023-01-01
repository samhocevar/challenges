#!/usr/bin/env python

from functools import reduce
from itertools import product
from math import prod, sqrt
import numpy as np

TSIZE = 10
TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3

# Return ith transform of matrix; 0-3 are rotations, 4-7 is horizontal flip then rotations
def transform(t, i):
    if i & 4: t = np.fliplr(t)
    if i & 2: t = np.flip(t)
    return np.rot90(t) if i & 1 else t

def dual(i): return 4 + (4 - i) % 4

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
    tiles[n] = t[1:-1,1:-1] # Crop borders early
    e = [sum([b << k for k, b in enumerate(transform(t, i)[0])]) for i in range(8)]
    edges[n] = e
    for v in e:
        stats[v] += 1

# Find a top-left corner; rotate the tile properly before returning it
def find_corner():
    for n, t in tiles.items():
        e = edges[n]
        for i in range(4):
            if stats[e[(TOP + i) % 4]] == 1 and stats[e[(LEFT + i) % 4]] == 1:
                tiles[n] = transform(t, i)
                edges[n] = e[i:4] + e[:i] + e[8-i:] + e[4:8-i]
                return n

# Keep track of already placed tiles
placed = set()

# Find a tile with the given edge (orientation, value)
def find_edge(o, v):
    for n, t in tiles.items():
        if n in placed:
            continue
        e = edges[n]
        if v in e:
            tmp = e.index(v)
            i = (tmp - o) % 4 + (tmp & 4)
            t = transform(t, i)
            if i >= 4:
                i -= 4
                e = e[4:] + e[:4]
            e = e[i:4] + e[:i] + e[8-i:] + e[4:8-i]
            tiles[n], edges[n] = t, e
            return n
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
                     map(tiles.get, row)) for row in array))
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
