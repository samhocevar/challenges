#!/usr/bin/env python

from heapq import heappop, heappush

with open('input.txt') as f:
    data = [l.strip() for l in f.readlines()]
    w, h = len(data[0]), len(data)

# Standard heap-based pathfinding. We store x and y, but also the direction and
# the available “energy” which is how many steps remain until we must change
# direction. Directions are 0, 1, 2, 3 for right, up, left, down.
def run(emin, emax):
    todo, done = [(0, 0, 0, 0, emax), (0, 0, 0, 3, emax)], set()
    while todo:
        heat, x, y, d, e = heappop(todo)
        # Advance position according to direction and spend energy.
        x, y, e = x + (1, 0, -1, 0)[d], y + (0, -1, 0, 1)[d], e - 1
        if (x, y, d, e) not in done and x >= 0 and y >= 0 and x < w and y < h:
            done.add((x, y, d, e))
            heat += int(data[y][x])
            if (x, y) == (w - 1, h - 1): return heat
            # Can only continue straight if energy > 0
            if e: heappush(todo, (heat, x, y, d, e))
            # Can only turn if spent energy is >= emin
            if emax - e >= emin:
                for k in (1, 3): heappush(todo, (heat, x, y, (d + k) % 4, emax))

print(run(1, 3))
print(run(4, 10))
