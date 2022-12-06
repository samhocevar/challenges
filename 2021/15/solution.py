#!/usr/bin/env python

from heapq import *
import numpy as np

# Read grid, subtract 1 from costs for convenience
with open('input.txt') as f:
    grid = np.array([[int(s) - 1 for s in l.strip()] for l in f])

def bestcost(grid):
    # Pad grid and make a list of border cells that we want to ignore
    w, h = np.shape(grid)
    done  = set((-1, x) for x in range(w))
    done |= set((h, x) for x in range(w))
    done |= set((y, -1) for y in range(h))
    done |= set((y, w) for y in range(h))
    costs = np.zeros(grid.shape).astype(int)

    # Compute costs for each cell using Dijkstra. Store the frontier
    # in a heap so that we always pop the one with the best priority
    todo = []
    heappush(todo, (0, (0, 0)))

    while todo:
        cost, a = heappop(todo)
        if a in done:
            continue
        costs[a] = cost
        done.add(a)
        for d in [(0,1),(-1,0),(0,-1),(1,0)]:
            b = (a[0] + d[0], a[1] + d[1])
            if b in done:
                continue
            heappush(todo, (cost + grid[b] + 1, b))

    return costs[(w - 1, h - 1)]


# Small grid
print(bestcost(grid))

# Fat grid
grid = np.hstack(list((grid + n) % 9 for n in range(5)))
grid = np.vstack(list((grid + n) % 9 for n in range(5)))
print(bestcost(grid))

