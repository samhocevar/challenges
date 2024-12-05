#!/usr/bin/env python

from itertools import takewhile

def is_subseq(seq, subseq): it = iter(seq); return all(x in it for x in subseq)

with open('input.txt') as f:
    rules = {*map(lambda s: tuple(map(int, s.split('|'))), takewhile(len, map(str.strip, f)))}
    updates = [tuple(map(int, l.strip().split(','))) for l in f]

s1, s2 = 0, 0

for u in map(list, updates):
    if not any(is_subseq(u, r[::-1]) for r in rules):
        s1 += u[len(u) // 2]
    else:
        for i in range(len(u)):
            for j in range(i + 1, len(u)):
                if (u[j], u[i]) in rules:
                    u[i], u[j] = u[j], u[i]
        s2 += u[len(u) // 2]

print(s1)
print(s2)
