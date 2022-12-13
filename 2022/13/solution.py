#!/usr/bin/env python

from functools import cmp_to_key
from itertools import takewhile
import json

def cmp(l, r):
    match l, r:
        case int(),  int():  return l - r
        case list(), int():  return cmp(l, [r])
        case int(),  list(): return cmp([l], r)
    for l2, r2 in zip(l, r):
        c = cmp(l2, r2)
        if c != 0:
            return c
    return len(l) - len(r)

with open('input.txt') as f:
    pkts = list(map(json.loads, [l for l in f if l.strip()]))

print(sum(i + 1 for i, (l, r) in enumerate(zip(pkts[::2], pkts[1::2])) if cmp(l, r) <= 0))

pkts.sort(key=cmp_to_key(cmp))
a = 1 + next(i for i, p in enumerate(pkts) if cmp(p, [[2]]) >= 0)
b = 2 + next(i for i, p in enumerate(pkts) if cmp(p, [[6]]) >= 0)
print(a * b)
