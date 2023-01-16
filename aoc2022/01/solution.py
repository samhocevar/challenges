#!/usr/bin/env python

from heapq import *

h, s = [], 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            # Push negative values because the heappop() returns the smallest element
            heappush(h, -s)
            s = 0
        else:
            s += int(line)
    heappush(h, s)

best3 = [heappop(h) for _ in range(3)]
print(-best3[0])
print(-sum(best3))
