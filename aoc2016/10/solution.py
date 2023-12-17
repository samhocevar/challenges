#!/usr/bin/env python

from collections import defaultdict
from math import prod
from re import findall

with open('input.txt') as f: data = [findall('(bot|out|[0-9]+)', l.strip()) for l in f]

s = {'bot': defaultdict(tuple), 'out': defaultdict(tuple)}

while l := data.pop() if data else None:
    if len(l) == 3:
        s['bot'][l[2]] += (int(l[0]),)
    elif len(l) == 6:
        src, tlo, dlo, thi, dhi = l[1:]
        # If bot doesn’t have two values yet, try again later
        if len(s['bot'][src]) != 2:
            data.insert(0, l)
        # Otherwise, distribute low and high values
        else:
            lo, hi = sorted(map(int, s['bot'].pop(src)))
            # Part 1: print the bot that handles (17, 61)
            if (lo, hi) == (17, 61): print(src)
            s[tlo][dlo] += (lo,)
            s[thi][dhi] += (hi,)

# Part 2: print the product of the first 3 inputs
print(prod(s['out'][n][0] for n in ('0', '1', '2')))
