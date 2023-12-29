#!/usr/bin/env python

from heapq import heappush, heappop

with open('input.txt') as f:
    data = [l.strip() for l in f.readlines()]
    w, h = len(data[0]), len(data)

# Count how many walls are around a cell
def walls(x, y): return sum(1 for i, j in ((1, 0), (0, -1), (-1, 0), (0, 1)) if data[y + j][x + i] == '#')

# “nodes” are the start and stop cells, as well as any walkable cells that
# have more than two walkable neighbours, they’re the only interesting cells
# in the map, all the rest is non-branching.
nodes = [(1, 0), (w - 2, h - 1)]
nodes += [(x, y) for y in range(1, h - 1) for x in range(1, w - 1) if data[y][x] != '#' and walls(x, y) < 2]

# Visit all paths starting at (x0, y0) and return all reachable nodes,
# treating wrongly oriented slopes as blockers.
def visit(n0):
    todo, done = [(0, *nodes[n0])], set()
    while todo:
        cost, x, y = heappop(todo)
        if (x, y) not in done:
            done.add((x, y))
            for d in range(4):
                if data[y][x] not in ('.', '>^<v'[d]): continue
                x2, y2 = x + [1, 0, -1, 0][d], y + [0, -1, 0, 1][d]
                if x2 < 0 or y2 < 0 or x2 >= w or y2 >= h: continue
                if (x2, y2) in nodes and (x2, y2) != nodes[n0]: yield nodes.index((x2, y2)), cost + 1; break
                heappush(todo, (cost + 1, x2, y2))

# “paths” are oriented paths between nodes
paths = {n: list(visit(n)) for n in range(len(nodes))}

# Enumerate the costs of all valid paths
def all_paths(src, dst):
    todo = [(0, src, 1 << src)]
    while todo:
        cost, n, visited = todo.pop()
        for n2, l in paths[n]:
            if n2 == dst: yield cost + l
            elif (1 << n2) & visited == 0: todo.append((cost + l, n2, visited | (1 << n2)))

# Part 1: try all paths and print the length of the longest one
print(max(all_paths(0, 1)))

# Part 2: mark all return trips as valid and run all_paths again
for src, dst, w in ((a, b, w) for a, v in list(paths.items()) for b, w in v):
    paths[dst] = [(src, w), *paths.get(dst, list())]
print(max(all_paths(0, 1)))
