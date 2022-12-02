#!/usr/bin/env python

from heapq import *

h, s = [], 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            heappush(h, -s) # Push negative values because the heappop() returns the smallest element
            s = 0
        else:
            s += int(line)
    heappush(h, s)

a, b, c = -heappop(h), -heappop(h), -heappop(h)
print(a)
print(a + b + c)
