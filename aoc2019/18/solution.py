#!/usr/bin/env python

from re import finditer
from heapq import heappush, heappop

with open('input.txt') as f:
    data = f.readlines()
distances, tokens = {}, {m[0]: (m.start(0), n) for n, l in enumerate(data) for m in finditer(r'[@\w]', l)}

# Compute the distances between all special tokens
for token, pos in tokens.items():
    distances[token], todo, done = {}, [(0, *pos)], set()
    while todo:
        cost, x, y = heappop(todo)
        if (x, y) not in done:
            done.add((x, y))
            match data[y][x]:
                case c if c in ['.', token]:
                    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        heappush(todo, (cost + 1, x + dx, y + dy))
                case c if c in tokens:
                    distances[token][c] = cost

# Use high-level pathfinding to explore the map in large steps, going from
# tokens to tokens instead of caring about the exact path.
def visit(start):
    todo, done, target = [(0, start, '')], set(), sum(1 for c in tokens if c.islower())
    while todo:
        cost, pos, keys = heappop(todo)
        # Stop when all keys have been collected
        if len(keys) == target:
            return cost
        if (pos, keys) not in done:
            done.add((pos, keys))
            for t, dist in distances[pos].items():
                if not t.isupper() or t.lower() in keys:
                    heappush(todo, (cost + dist, t, ''.join(sorted(keys + t)) if t.islower() and t not in keys else keys))

# Part 1: visit the map using one agent
print(visit('@'))
