#!/usr/bin/env python

with open('input.txt') as f: data = f.read().strip()

def checksum(s):
    if len(s) % 2: return s
    # FIXME: use batched(_, 2) when Python 3.12 is widespread
    return checksum(''.join(map(lambda a, b: '1' if a == b else '0', s[::2], s[1::2])))

def reduce(s, n):
    while len(s) < n: s += '0' + s.translate(str.maketrans('01', '10'))[::-1]
    return checksum(s[:n])

print(reduce(data, 272))
print(reduce(data, 35651584))
