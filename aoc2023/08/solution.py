#!/usr/bin/env python

from math import lcm
from re import findall

with open('input.txt') as f:
    code = next(f).strip()
    data = {a: {'L': b, 'R': c} for a, b, c in (findall('[0-9A-Z]+', l) for l in f if l.strip())}

def solve(node, end):
    for n in range(1 + len(data) * len(code)):
        if node.endswith(end): return n
        node = data[node][code[n % len(code)]]

# Part 1: start with AAA and stop at ZZZ
print(solve('AAA', 'ZZZ'))

# Part 2: start with each node that ends with A, stop when the node ends with Z
# Note that the dataset is specially crafted such that the successor of __Z is
# the same as the successor of __A so there is no need to compute actual cycle
# lengths or keep track of offsets; they made it a lot easier.
print(lcm(*(solve(r, 'Z') for r in data if r.endswith('A'))))
