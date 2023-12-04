#!/usr/bin/env python

with open('input.txt') as f:
    data = [l.strip().split('-') for l in f]

rooms = {kv[0] for kv in data} | {kv[1] for kv in data}

links = { r: set() for r in rooms }
for a, b in data:
    links[a].add(b)
    links[b].add(a)

def visit(room, visited, relaxed):
    n = 0
    visited[room] += 1
    for p in links[room]:
        if p == 'end':
            n += 1
        elif p[0].isupper() or visited[p] == 0:
            n += visit(p, visited, relaxed)
        elif relaxed and p[0].islower() and p != 'start':
            n += visit(p, visited, False)
    visited[room] -= 1
    return n

visited = { r: 0 for r in rooms }

print(visit("start", visited, False))
print(visit("start", visited, True))
