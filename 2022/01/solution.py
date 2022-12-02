#!/usr/bin/env python

from heapq import *

h, s = [], 0

def keep(h, n):
    return [heappop(h) for _ in range(n)]

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            # Push negative values because the heappop() returns the smallest element
            heappush(h, -s)
            s = 0
        else:
            s += int(line)
        # Optional memory optimisation: keep only the best 3 values
        if len(h) > 100:
            h = keep(h, 3)
            heapify(h)
    heappush(h, s)

best3 = keep(h, 3)
print(-best3[0])
print(-sum(best3))
