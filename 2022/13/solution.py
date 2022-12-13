#!/usr/bin/env python

from ast import literal_eval

def cmp(l, r):
    match l, r:
        case int(), int(): return l - r
        case list(), int(): r = [r]
        case int(), list(): l = [l]
    return next((c for c in map(cmp, l, r) if c), len(l) - len(r))

with open('input.txt') as f:
    pkts = list(map(literal_eval, [l for l in f if l.strip()]))

print(sum(i for i, p in enumerate(zip(*[iter(pkts)] * 2), 1) if cmp(*p) <= 0))
print(sum((1 for p in pkts if cmp(p, [[2]]) < 0), 1) * sum((1 for p in pkts if cmp(p, [[6]]) < 0), 2))
