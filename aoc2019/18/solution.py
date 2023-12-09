#!/usr/bin/env python

from heapq import heappush, heappop

with open('input.txt') as f:
    data = f.readlines()
start = next((l.index('@'), n, ()) for n, l in enumerate(data) if '@' in l)

# Low-level pathfinding function: list all reachable keys from a given
# position on the map and a list of collected keys. An already opened door
# or an already collected key is considered an empty cell. We use a heap
# for the frontier to make sure we always get the shortest path.
def reachable(start):
    empty = {'.', '@'}.union(start[2]).union(c.upper() for c in start[2])
    todo, done = [(0, *start[:2])], set()
    while todo:
        dist, x, y = heappop(todo)
        if (x, y) not in done:
            done.add((x, y))
            match data[y][x]:
                case c if c in empty:
                    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        heappush(todo, (dist + 1, x + dx, y + dy))
                case c if c >= 'a' and c <= 'z':
                    yield (dist, x, y, c)

# Part 1: use high-level pathfinding to explore the map in large steps,
# jumping from one reachable key to another. Stop when all keys have been
# collected.
todo, done = [(0, start)], set()
while todo:
    cost, state = heappop(todo)
    if state not in done:
        done.add(state)
        targets = list(reachable(state))
        if not targets:
            print(cost)
            break
        for dist, x, y, c in targets:
            heappush(todo, (cost + dist, (x, y, tuple(sorted({c}.union(state[2]))))))
