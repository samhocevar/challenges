#!/usr/bin/env python

with open('input.txt') as f: data = [l.strip() for l in f.readlines()]

w, h = len(data[0]), len(data)

def run(x0, y0, d0):
    # Keep track of the beams and the already visited cells
    beams, visited = {(x0, y0, d0)}, set()
    while beams:
        x, y, d = beams.pop()
        # Direction is 0, 1, 2, 3 for right, up, left, down
        x, y = x + [1, 0, -1, 0][d], y + [0, -1, 0, 1][d]
        if (x, y, d) not in visited and x >= 0 and y >= 0 and x < w and y < h:
            visited.add((x, y, d))
            # Rotate beam according to the rules; the 2nd and 3rd conditions
            # can both be true, which creates the split.
            if data[y][x] in ('.',  '-|'[d & 1]): beams.add((x, y, d))
            if data[y][x] in ('/',  '|-'[d & 1]): beams.add((x, y, d ^ 1))
            if data[y][x] in ('\\', '|-'[d & 1]): beams.add((x, y, d ^ 3))
    return len({(x, y) for x, y, _ in visited})

# Part 1: launch a single beam from the top-left corner, going right
print(run(-1, 0, 0))

# Part 2: launch beams from all sides of the map
print(max(max(max(run(-1, n, 0), run(w, n, 2)) for n in range(h)),
          max(max(run(n, -1, 3), run(n, h, 1)) for n in range(w))))
