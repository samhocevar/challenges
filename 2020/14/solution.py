#!/usr/bin/env python

from itertools import product

MASK = 0xfffffffff

m1 = MASK
m2 = 0
spread = []

memv1, memv2 = {}, {}

with open('input.txt') as f:
    for l in f:
        match l.split():
            case 'mask', _, s:
                m1 = sum((1 if c == 'X' else 0) << n for n, c in enumerate(s[::-1]))
                m2 = sum((1 if c == '1' else 0) << n for n, c in enumerate(s[::-1]))
                bits = list(1 << n for n, c in enumerate(s[::-1]) if c == 'X')
                # https://stackoverflow.com/a/64320524/111461
                spread = [sum(j for i in sl for j in i) for sl in product(*[[[], [i]] for i in bits])]
            case [a, _, b]:
                ptr, val = int(a[4:][:-1]), int(b)
                # Version 1
                memv1[ptr] = (val & m1) | m2
                # Version 2
                for m3 in spread:
                    memv2[(ptr & ~m1) | m2 | m3] = val

print(sum(memv1.values()))
print(sum(memv2.values()))
