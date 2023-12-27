#!/usr/bin/env python

from heapq import heappush, heappop

# Read vertices as a dictionary of node -> set(node, …), then fill it with
# all the reverse vertices for convenience.
with open('input.txt') as f: data = {l[:3]: {*l[4:].split()} for l in f}
for a, b in ((a, b) for a, v in list(data.items()) for b in v): data[b] = data.get(b, set()) | {a}

# Perform path finding four times, creating a blacklist of edges each time.
# If the 4th path finding fails, it means the nodes are in disjoint groups.
def disjoint(src, dst):
    blacklist = set()
    for n in range(4):
        todo, done = [(0, src, [])], set()
        while todo:
            cost, node, path = heappop(todo)
            if node == dst: blacklist |= set(path); break
            if node not in done:
                done.add(node)
                for nxt in (nxt for nxt in data[node] if node + nxt not in blacklist):
                    heappush(todo, (cost + 1, nxt, [*path, node + nxt]))
        else: return True # Path finding failed; vertices are disjoint

# Pick any vertex and count how many vertices are strongly connected to it.
n = sum(1 for dst in data.keys() if not disjoint(next(iter(data)), dst))
print(n * (len(data) - n))
