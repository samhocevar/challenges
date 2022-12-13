#!/usr/bin/env python

from heapq import *
from operator import add
import numpy as np

# Read grid, subtract 1 from costs for convenience
with open('input.txt') as f:
    grid = np.array([[int(s) - 1 for s in l.strip()] for l in f])

def bestcost(grid):
    h, w = np.shape(grid)
    costs = np.full(grid.shape, -1)

    # Compute costs for each cell using Dijkstra. Store the frontier
    # in a heap so that we always pop the one with the best priority
    todo = []
    heappush(todo, (0, (0, 0)))

    while todo:
        cost, a = heappop(todo)
        if costs[a] == -1:
            costs[a] = cost
            for d in [(0,1), (-1,0), (0,-1), (1,0)]:
                b = tuple(map(add, a, d))
                if b[0] not in (-1, h) and b[1] not in (-1, w) and costs[b] == -1:
                    heappush(todo, (cost + grid[b] + 1, b))

    return costs[(w - 1, h - 1)]


# Small grid
print(bestcost(grid))

# Fat grid
grid = np.hstack(list((grid + n) % 9 for n in range(5)))
grid = np.vstack(list((grid + n) % 9 for n in range(5)))
print(bestcost(grid))
