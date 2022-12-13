#!/usr/bin/env python

from functools import cmp_to_key
from math import prod
from ast import literal_eval

mark = [[[2]], [[6]]]

def cmp(l, r):
    match l, r:
        case int(), int(): return l - r
        case list(), int(): r = [r]
        case int(), list(): l = [l]
    return next((c for c in map(cmp, l, r) if c), len(l) - len(r))

with open('input.txt') as f:
    pkts = list(map(literal_eval, [l for l in f if l.strip()]))

print(sum(i for i, p in enumerate(zip(pkts[::2], pkts[1::2]), 1) if cmp(*p) <= 0))
print(prod(i for i, p in enumerate(sorted(pkts + mark, key=cmp_to_key(cmp)), 1) if p in mark))
