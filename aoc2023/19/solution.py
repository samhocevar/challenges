#!/usr/bin/env python

from itertools import takewhile
from math import prod

with open('input.txt') as f:
    rules = {l[:l.find('{')]: [s.split(':') for s in l[l.find('{') + 1:-1].split(',')] for l in takewhile(str, map(str.strip, f))}
    data = [{s[0]: int(s[2:]) for s in l.strip()[1:-1].split(',')} for l in f]

# Traverse the tree of rules with a list of bounds, updating the bounds at
# each comparison. For instance if the bounds for 'a' are [1, 4001] and we
# encounter 'a>1234:foo', we compute the combinations for rule 'foo' with
# updated bounds [1235, 4001], and we carry on with the rest of the workflow
# with updated bounds [1, 1235].
def compute(bnd, name='in', ret=0):
    if name in 'AR': return prod(max(0, p[1] - p[0]) for p in bnd.values()) if name == 'A' else 0
    for r in rules[name][:-1]:
        # c is the rating name, n is the number being compared with
        c, n = r[0][0], int(r[0][2:])
        if r[0][1] == '>' and bnd[c][1] > n + 1:
            ret += compute(bnd | {c: [max(n + 1, bnd[c][0]), bnd[c][1]]}, r[1])
            bnd |= {c: [bnd[c][0], min(n + 1, bnd[c][1])]}
        if r[0][1] == '<' and bnd[c][0] < n:
            ret += compute(bnd | {c: [bnd[c][0], min(n, bnd[c][1])]}, r[1])
            bnd |= {c: [max(n, bnd[c][0]), bnd[c][1]]}
    return ret + compute(bnd, rules[name][-1][0])

# Part 1: for each data value, use bounds [n, n + 1] and count the valid combinations (either 1 or 0)
print(sum(sum(d.values()) for d in data if compute({c: [n, n + 1] for c, n in d.items()})))

# Part 2: use the full [1, 4001] bounds to count the combinations
print(compute({c: [1, 4001] for c in 'xmas'}))
