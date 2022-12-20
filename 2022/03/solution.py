#!/usr/bin/env python

from functools import reduce
from operator import and_

def score(c):
    return (ord(c) - 38) % 58 # -38 = 27-'A'   58 = 'a'-'A'+26

s1, s2 = 0, 0

with open('input.txt') as f:
    for tu in zip(*[map(str.strip, f)] * 3): # Read in chunks of 3 stripped lines
        for l, mid in [(l, len(l) // 2) for l in tu]:
            s1 += score(*reduce(and_, map(set, (l[:mid], l[mid:]))))
        s2 += score(*reduce(and_, map(set, tu)))

print(s1)
print(s2)
