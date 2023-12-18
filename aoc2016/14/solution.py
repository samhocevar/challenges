#!/usr/bin/env python

from hashlib import md5
from itertools import count
from re import findall
from heapq import heappush, heappop

with open('input.txt') as f: data = f.read().strip()

def hack(stretch):
    candidates, validated = [], []
    for n in count():
        # Expire old candidates (probably not necessary)
        while candidates and candidates[0][0] + 1000 < n:
            candidates = candidates[1:]
        s = data + str(n)
        for _ in range(stretch): s = md5(s.encode('ascii')).hexdigest()
        for i, h in enumerate(findall(r'((.)\2\2+)', s)):
            # The rules say to only consider the first triplet
            if i == 0: candidates.append((n, h[1]))
            # Go back through old candidates to validate them
            if len(h[0]) >= 5:
                for c in candidates.copy():
                    if c[0] != n and c[1] == h[1]:
                        heappush(validated, (-c[0], n))
                        candidates.remove(c)
        # If we have enough keys and the most recent one is old enough, return it
        if len(validated) >= 64 and -validated[0][0] + 1000 < n:
            while len(validated) > 64: heappop(validated)
            return -validated[0][0]

print(hack(1))
print(hack(2017))
