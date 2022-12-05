#!/usr/bin/env python

from itertools import zip_longest, takewhile

def move(rule):
    with open('input.txt') as f:
        # Read stack data as a matrix and transpose it
        tmp = zip_longest(*(s[1::4] for s in takewhile(str.strip, f)), fillvalue='')
        stacks = [''.join(l[::-1]).strip() for l in tmp]
        # Apply moves
        for l in f:
            n, a, b = (int(x) for x in l.split(' ')[1::2])
            stacks[b-1] += stacks[a-1][-n:][::rule]
            stacks[a-1] = stacks[a-1][:-n]
        # Print last crate of each stack
        print(''.join(s[-1] for s in stacks))

move(-1)
move(1)

