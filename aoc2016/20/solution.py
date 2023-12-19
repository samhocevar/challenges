#!/usr/bin/env python

with open('input.txt') as f: data = list(sorted(tuple(map(int, s.split('-'))) for s in f))

total, inf, sup = 0, -1, -1
for p in data:
    if inf < 0 and sup + 1 < p[0]: inf = sup + 1
    total, sup = total + max(0, p[0] - sup - 1), max(sup, p[1])

print(inf)
print(total)
