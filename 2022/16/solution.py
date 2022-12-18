#!/usr/bin/env python

from heapq import heappush, heappop

# Read data
data = {}
with open('input.txt') as f:
    for l in map(str.split, f):
        data[l[1]] = [int(l[4][5:-1]), [s[0:2] for s in l[9:]]]

# Build a graph of travel and activation costs (only for non-empty valves)
names = ['AA'] + [k for k, v in data.items() if v[0]]
indices = {r: i for i, r in enumerate(names)}
network = [{} for _ in names]
for i in range(len(names)):
    start = names[i]
    todo, done = [(0, start)], set()
    while todo:
        n, room = heappop(todo)
        if room not in done:
            if room != start and data[room][0]:
                network[i][indices[room]] = n + 1
            done.add(room)
            for room2 in data[room][1]:
                heappush(todo, (n + 1, room2))

# Explore graph from a given position and remaining time, with optional high score history recording
def explore(pos, time, history=None, score=0, done=0):
    hiscore = score
    if history and score > history[done]:
        history[done] = score
    for dest, cost in network[pos].items():
        mask = 1 << dest
        if mask & ~done:
            t2 = time - cost
            if t2 >= 0:
                s2 = score + t2 * data[names[dest]][0]
                hiscore = max(hiscore, explore(dest, t2, history, s2, done | mask))
    return hiscore

# Part 1: just explore from the start with 30 minutes remaining
print(explore(0, 30))

# Part 2: explore with 26 minutes and record history
history = [0] * (1 << len(names))
explore(0, 26, history)

# Complete history for unvisited nodes
for i in range(1, len(names)):
    bit = 1 << i
    for k in range(len(history))[::2]:
        if k & bit:
            history[k] = max(history[k], history[k - bit])

# Print the best combination of paths for player and elephant
mask = (1 << len(names)) - 2
print(max(history[k] + history[mask - k] for k in range(2, mask + 1)[::2]))
