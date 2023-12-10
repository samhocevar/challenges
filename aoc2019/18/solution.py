#!/usr/bin/env python

from re import finditer
from heapq import heappush, heappop

with open('input.txt') as f:
    data = f.readlines()
tokens = {m[0]: (m.start(0), n) for n, l in enumerate(data) for m in finditer(r'[@\w]', l)}
origin = [('@', tokens.pop('@'))]

def visit(start):
    # Find all tokens in the map: keys, gates, and starting positions
    distances, tokens = {}, {m[0]: (m.start(0), n) for n, l in enumerate(data) for m in finditer(r'[@\w]', l)}
    # Special case for part 2: we now have 4 different agents, update data and origin
    if len(start) > 1:
        i, j = origin.pop()[1]
        for n in range(j - 1, j + 2):
            data[n] = data[n][:i - 1] + '#.#.'[(n - j) % 2:][:3] + data[n][i + 2:]
        origin.extend([(str(n), (i + [-1, 1][n % 2], j + [-1, 1][n // 2])) for n in range(4)])
    # Compute distances between tokens using low-level pathfinding
    for tok, pos in (*origin, *tokens.items()):
        distances[tok], todo, done = {}, [(0, *pos)], set()
        while todo:
            cost, x, y = heappop(todo)
            if (x, y) not in done:
                done.add((x, y))
                match data[y][x]:
                    case c if c in ['.', tok]:
                        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                            heappush(todo, (cost + 1, x + dx, y + dy))
                    case c if c in tokens:
                        distances[tok][c] = cost
    # Use high-level pathfinding to explore the map in large steps, going from
    # token to token and not caring about the exact path.
    # FIXME: inefficient, takes almost 2 minutes to complete; we should use a bitmask for keys
    todo, done, target = [(0, start, '')], set(), sum(1 for c in tokens if c.islower())
    while todo:
        cost, pos, keys = heappop(todo)
        # Stop when all keys have been collected
        if len(keys) == target:
            return cost
        if (pos, keys) not in done:
            done.add((pos, keys))
            for n, p in enumerate(pos):
                for t, dist in distances[p].items():
                    if not t.isupper() or t.lower() in keys:
                        newpos = pos[:n] + t + pos[n + 1:]
                        newkeys = ''.join(sorted(keys + t)) if t.islower() and t not in keys else keys
                        heappush(todo, (cost + dist, newpos, newkeys))

# Part 1: visit the map using one agent
print(visit('@'))

# Part 2: visit the map using four agents
print(visit('0123'))
