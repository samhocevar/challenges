#!/usr/bin/env python

with open('input.txt') as f:
    data = [*map(str.strip, f)]
    lab = {(x, y): c for y, l in enumerate(data) for x, c in enumerate(l)}
    p0 = next(p for p, c in lab.items() if c == '^')

def visit(lab):
    p, d, visited = p0, 1, set()
    while p in lab:
        if (p, d) in visited: return None
        visited.add((p, d))
        p2 = (p[0] + [1, 0, -1, 0][d], p[1] + [0, -1, 0, 1][d])
        match lab.get(p2, None):
            case '#': d = (d + 3) % 4
            case _: p = p2
    return set(p for p, _ in visited)

# Visit the map and record a trace
trace = visit(lab)

# Part 1: print the number of unique locations in the trace
print(len(trace))

# Part 2: find all obstacles locations on the trace that end in a loop
print(sum(1 for p in trace if p != p0 and not visit({**lab, p: '#'})))
