#!/usr/bin/env python

def all_sums(k, n):
    if k == 1:
        yield n,
    else:
        for i in range(n + 1):
            for l in all_sums(k - 1, n - i):
                yield i, *l

with open('input.txt') as f:
    l = next(f).split()
    s = 0
    for l in all_sums(int(l[0]), int(l[-1])):
        s += ''.join(map(str, l)).count('1')
    print(s)
