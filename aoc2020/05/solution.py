#!/usr/bin/env python

with open('input.txt') as f:
    data = list(map(str.strip, f))

def rank(s):
    return sum(1 << n for n, c in enumerate(s) if c in 'BR')

ids = [rank(s[6::-1]) * 8 + rank(s[:6:-1]) for s in data]

print(max(ids))
print(max(set(ids) - set([i + 1 for i in ids])) - 1)
