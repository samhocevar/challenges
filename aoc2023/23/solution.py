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
def visit(x0, y0):
    todo, done = [(0, x0, y0)], set()
    while todo:
        cost, x, y = heappop(todo)
        if (x, y) not in done:
            done.add((x, y))
            for d in range(4):
                if data[y][x] not in ('.', '>^<v'[d]): continue
                x2, y2 = x + [1, 0, -1, 0][d], y + [0, -1, 0, 1][d]
                if x2 < 0 or y2 < 0 or x2 >= w or y2 >= h: continue
                if (x2, y2) in nodes and (x2, y2) != (x0, y0): yield x2, y2, cost + 1; break
                heappush(todo, (cost + 1, x2, y2))

# “paths” are oriented paths between nodes
paths = {(x, y): set(visit(x, y)) for x, y in nodes}

# Enumerate the costs of all valid paths
def all_paths(src, dst):
    todo = [(0, {src}, *src)]
    while todo:
        cost, visited, x, y = todo.pop()
        for x2, y2, l in paths[(x, y)]:
            if (x2, y2) == dst: yield cost + l
            elif (x2, y2) not in visited: todo.append((cost + l, visited | {(x2, y2)}, x2, y2))

# Part 1: try all paths and print the length of the longest one
print(max(all_paths(nodes[0], nodes[1])))

# Part 2: mark all return trips as valid and run all_paths again
for src, dst, l in ((a, b[:2], b[2]) for a, v in list(paths.items()) for b in v):
    paths[dst] = paths.get(dst, set()) | {(*src, l)}
print(max(all_paths(nodes[0], nodes[1])))
