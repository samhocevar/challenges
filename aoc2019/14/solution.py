#!/usr/bin/env python

from collections import defaultdict
from math import ceil
from re import findall

# TODO: with Python 3.12 itertools, the zip() call can be replaced with batched(l[:-2], 2)
# Read data as a dictionary of reactions: "7 A, 1 B => 1 C" becomes {'C': [1, {'A': 7, 'B': 1}]}
with open('input.txt') as f:
    data = {l[-1]: [int(l[-2]), {b: int(a) for a, b in zip(l[:-2:2], l[1:-2:2])}] for l in map(lambda l: findall('[0-9A-Z]+', l), f)}
data['ORE'] = [0, {}]

# Prepare data: topologically sort reaction components
stack, order, path = ['FUEL'], [], set()
while stack:
    v = stack[-1]
    path.add(v)
    children = [x for x in data[v][1] if x not in path]
    if not children:
        order.insert(0, v)
        stack.pop()
    else: stack.append(children[0])

def compute(fuel):
    # Apply reactions in topological order so that we don’t have to backtrack
    need = defaultdict(int)
    need['FUEL'] = fuel
    for c in order:
        n, reaction = data[c]
        for k, v in reaction.items():
            need[k] += ceil(need[c] / n) * v
    return need['ORE']

# Part 1: compute how much ore is needed for 1 fuel
print(compute(1))

# Part 2: guess bit-by-bit how much fuel we can produce with 10**12 ore
fuel, ore = 0, 10 ** 12
for n in range(40)[::-1]:
    if compute(fuel + 2 ** n) < ore:
        fuel += 2 ** n
print(fuel)
