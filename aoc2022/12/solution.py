#!/usr/bin/env python

from heapq import *
from operator import add
import numpy as np

with open('input.txt') as f:
    grid = np.array([[ord(s) for s in l.strip()] for l in f])

start = tuple(np.argwhere(grid == ord('S'))[0])
end = tuple(np.argwhere(grid == ord('E'))[0])

grid[start], grid[end] = ord('a'), ord('z')

# Compute costs for each cell using Dijkstra. Store the frontier
# in a heap so that we always pop the one with the best priority
h, w = np.shape(grid)
UNVISITED = w * h
costs = np.full(grid.shape, UNVISITED)

todo = []
heappush(todo, (0, end))

while todo:
    cost, a = heappop(todo)
    if costs[a] == UNVISITED:
        costs[a] = cost
        for d in [(0,1), (-1,0), (0,-1), (1,0)]:
            b = tuple(map(add, a, d))
            if b[0] not in (-1, h) and b[1] not in (-1, w) and costs[b] == UNVISITED and grid[a] <= grid[b] + 1:
                heappush(todo, (cost + 1, b))

print(costs[start])
print(np.where(grid == ord('a'), costs, UNVISITED).min())
