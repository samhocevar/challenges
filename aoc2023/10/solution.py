#!/usr/bin/env python

with open('input.txt') as f:
    data = f.readlines()
p0 = next((l.index('S'), n) for n, l in enumerate(data) if 'S' in l)

# Directions are 0, 1, 2, 3 for right, up, left, down. This table
# allows us to find the exit direction when crossing a given tile.
# For instance, if direction is 1 (up) and the tile is '7', the next
# direction will be: outputs[1].find('7') = 2 (left).
outputs = ['-J 7', 'F|7 ', ' L-F', 'L J|']

# Part 1: follow the loop and record all tiles on the way
p, d0, d, loop = p0, 0, 0, set()
while p0 not in loop:
    # If we get stuck, try again with a different starting direction
    if d == -1:
        p, d0, d, loop = p0, d0 + 1, d0 + 1, set()
    # Advance p (position) and d (direction) to the next tile. Also
    # store t0, the tile we _think_ was behind the 'S'.
    p = (p[0] + abs(d - 2) - 1, p[1] + abs(d - 1) - 1)
    loop.add(p)
    t0, d = outputs[d][d0], outputs[d].find(data[p[1]][p[0]])

print((len(loop) + 1) // 2)

# Part 2: trace horizontal lines on the map and switch the inside/outside
# boolean each time we cross the loop. We decide that our imaginary lines
# stand below the middle line, so we ignore 'L' and 'J' tiles.
# We also need to replace the starting tile 'S' with the actual tile that
# should be there.
total, inside = 0, False
for j, line in enumerate(data):
    for i, c in enumerate(line.replace('S', t0)):
        if (i, j) in loop:
            inside = inside != (c in 'F7|')
        elif inside:
            total += 1

print(total)
