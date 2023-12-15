#!/usr/bin/env python

from functools import reduce
from re import split

with open('input.txt') as f: data = f.read().strip()

def hash(s): return reduce(lambda n, c: (n + ord(c)) * 17 % 256, s, 0)

# Part 1: split string, compute hashes, print sum
print(sum(map(hash, data.split(','))))

# Split data along '-', '=' and ',' then just apply the rules. Python dictionaries
# preserve insertion order so there is really nothing to worry about.
boxes = [{} for _ in range(256)]
for label, n in zip(*[iter(split('[-=,]', data))] * 2):
    if n: boxes[hash(label)][label] = int(n)
    else: boxes[hash(label)].pop(label, None)

# Part 2: enumerate all lenses and compute their focusing power
print(sum(j * i * v for j, b in enumerate(boxes, 1) for i, v in enumerate(b.values(), 1)))
