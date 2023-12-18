#!/usr/bin/env python

from heapq import heappush, heappop

with open('input.txt') as f: seed = int(f.read())

# Slightly shorter way to rewrite x*x + 3*x + 2*x*y + y + y*y + seed
wall = lambda x, y: int.bit_count((x + y + 1) ** 2 + x - y + seed - 1) & 1

todo, done, part1, part2 = [(0, 1, 1)], set(), 0, 0
while todo and not (part1 and part2):
    cost, x, y = heappop(todo)
    if x >= 0 and y >= 0 and not wall(x, y) and (x, y) not in done:
        # Part 1: goal is reached, remember the cost
        if (x, y) == (31, 39): part1 = cost
        # Part 2: if cell has cost 51 or more, remember the visited cell count
        if cost > 50 and not part2: part2 = len(done)
        done.add((x, y))
        for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]: 
            heappush(todo, (cost + 1, x + dx, y + dy))

print(part1)
print(part2)
