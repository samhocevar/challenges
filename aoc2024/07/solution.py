#!/usr/bin/env python

from itertools import product
from functools import reduce
from operator import mul, add

with open('input.txt') as f:
    data = [list(map(int, l.replace(':', '').split())) for l in f]

def check(d, operators):
    ops = map(list, product(operators, repeat=len(d) - 2))
    return d[0] if any(reduce(lambda x, y: t.pop()(x, y), d[1:]) == d[0] for t in ops) else 0

print(sum(check(d, (mul, add)) for d in data))
print(sum(check(d, (mul, add, lambda x, y: int(str(x) + str(y)))) for d in data))
