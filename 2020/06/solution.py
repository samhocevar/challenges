#!/usr/bin/env python

from functools import reduce
from operator import and_, or_

with open('input.txt') as f:
    data = list(map(str.strip, f.read().split('\n\n')))

print(sum(len(reduce(or_, map(set, g.split('\n')))) for g in data))
print(sum(len(reduce(and_, map(set, g.split('\n')))) for g in data))
