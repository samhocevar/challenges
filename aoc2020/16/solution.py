#!/usr/bin/env python

import numpy as np
from itertools import chain
from math import prod

f_names = []
f_descs = []
tickets = []
with open('input.txt') as f:
    for l in map(str.strip, f):
        match l.split(':'):
            case _, '': pass
            case ['']: pass
            case r, f: f_names.append(r); f_descs.append(list(map(int, f.strip().replace(' or ', '-').split('-'))))
            case _: tickets.append(list(map(int, l.split(','))))
f_pos = [-1] * len(f_names)

def is_valid(field, value):
    for a, b in zip(*[iter(field)] * 2):
        if value >= a and value <= b:
            break
    else: return False
    return True

def match_desc(tickets, desc):
    return np.prod(sum((tickets >= a) * (tickets <= b) for a, b in zip(*[iter(desc)] * 2)), axis=0)

# Part 1
invalid = [(n, v) for n, t in enumerate(tickets) for v in t if all(not is_valid(f, v) for f in f_descs)]
print(sum(v for _, v in invalid))

# Part 2
reject = {n for n, _ in invalid}
valid = np.array([t for n, t in enumerate(tickets) if n not in reject])

# Build a matrix with one row per field spec
# Each row contains how the ticket fields matched globally
# Find the column that contains only one 1: we know the 1 comes from the only possible field
# Find the row that provided the 1
# Remove row, repeat until exhausted
matches = np.array([match_desc(valid, desc) for desc in f_descs])
for _ in range(len(f_names)):
    sums = np.sum(matches, axis=0)
    col = np.where(sums == 1)[0][0]
    row = np.where(matches[:,col])[0][0]
    f_pos[row] = col
    matches[row,:] = 0

print(prod(tickets[0][pos] for name, pos in zip(f_names, f_pos) if name[:9] == 'departure'))
