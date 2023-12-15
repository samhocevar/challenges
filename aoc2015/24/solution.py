#!/usr/bin/env python

from math import prod

with open('input.txt') as f: data = list(int(l) for l in f)

def comb(n, l, limit):
    if l[0] == n:
        yield (n,)
    elif len(l) > 1:
        if limit > 1 and l[0] < n:
            for t in comb(n - l[0], l[1:], limit - 1):
                yield (l[0], *t)
        yield from comb(n, l[1:], limit)

# FIXME: this could be made a lot faster by looking for increasingly large
# subsets instead of going directly with len(data)/3.
print(min((len(t), prod(t), t) for t in comb(sum(data) // 3, data, len(data) // 3))[1])
print(min((len(t), prod(t), t) for t in comb(sum(data) // 4, data, len(data) // 3))[1])
