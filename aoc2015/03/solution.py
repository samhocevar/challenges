#!/usr/bin/env python

with open('input.txt') as f: data = next(f).strip()

def visit(agents):
    x, y, visited = [0] * agents, [0] * agents, {(0, 0)}
    for a, c in [(n % agents, c) for n, c in enumerate(data)]:
        x[a] += '<^> v'.find(c) % 3 - 1
        y[a] += '^>v <'.find(c) % 3 - 1
        visited.add((x[a], y[a]))
    return len(visited)

print(visit(1))
print(visit(2))
