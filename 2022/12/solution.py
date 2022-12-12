#!/usr/bin/env python

from heapq import *
import numpy as np

with open('input.txt') as f:
    grid = np.array([[ord(s) for s in l.strip()] for l in f])

start = tuple(np.argwhere(grid == ord('S'))[0])
end = tuple(np.argwhere(grid == ord('E'))[0])

grid[start] = ord('a')
grid[end] = ord('z')

# Make a list of border cells that we want to ignore
h, w = np.shape(grid)
done  = set((-1, x) for x in range(w))
done |= set((h, x) for x in range(w))
done |= set((y, -1) for y in range(h))
done |= set((y, w) for y in range(h))

# Compute costs for each cell using Dijkstra. Store the frontier
# in a heap so that we always pop the one with the best priority
worst = w * h
costs = np.full(grid.shape, worst)
todo = []
heappush(todo, (0, end))

while todo:
    cost, a = heappop(todo)
    if a in done:
        continue
    costs[a] = cost
    done.add(a)
    for d in [(0,1),(-1,0),(0,-1),(1,0)]:
        b = (a[0] + d[0], a[1] + d[1])
        if b in done or grid[a] - grid[b] > 1:
            continue
        heappush(todo, (cost + 1, b))

print(costs[start])
print(np.where(grid == ord('a'), costs, worst).min())
