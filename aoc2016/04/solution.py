#!/usr/bin/env python

from re import search

with open('input.txt') as f:
    data = [tuple(search('([a-z-]+)([0-9]+).(.*).', l).groups()) for l in f]

def valid(name, n, chk):
    stats = sorted((-name.count(c), c) for c in set(name) - {'-'})
    return int(n) if chk == ''.join([t[1] for t in stats][:5]) else 0

def northpole(name, n):
    shift = ''.join(chr(ord('a') + (ord(c) - ord('a') + int(n)) % 26) if c != '-' else ' ' for c in name)
    return int(n) if 'northpole' in shift else 0

print(sum(valid(name, n, chk) for name, n, chk in data))
print(sum(northpole(name, n) for name, n, _ in data))
