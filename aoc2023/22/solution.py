#!/usr/bin/env python

with open('input.txt') as f: data = [list(map(int, l.strip().replace('~', ',').split(','))) for l in f]

# Return how much 'a' can fall on top of 'b'. If no blocking occurs, return a negative value.
def dist(a, b):
    return a[2] - b[5] - 1 if a[3] >= b[0] and a[0] <= b[3] and a[4] >= b[1] and a[1] <= b[4] else -1

# List all blocks above and below the nth block that could collide
top = [{k for k in range(len(data)) if dist(data[k], data[n]) >= 0} for n in range(len(data))]
bot = [{k for k in range(len(data)) if dist(data[n], data[k]) >= 0} for n in range(len(data))]

# Topologically sort blocks, using all blocks that have no blocker as a seed
stack, order, path = [n for n in range(len(data)) if not bot[n]], [], set()
while stack:
    path.add(a := stack[-1])
    for b in top[a] - path: stack.append(b); break
    else: order.insert(0, a); stack.pop()

# Make all blocks fall, using topological order so that only one pass is required
for n in order:
    d = min(dist(data[n], data[k]) for k in bot[n]) if bot[n] else data[n][2]
    data[n][2] -= d; data[n][5] -= d

# List all blocks that are the sole supporter of their above block
sup = [{k for k in bot[n] if dist(data[n], data[k]) == 0} for n in range(len(data))]
required = {next(iter(s)) for s in sup if len(s) == 1}

# Part 1: any block that is not a sole supporter can be disintegrated
print(len(data) - len(required))

# Part 2: count falling blocks for each sole supporter, again using topological order
def count_falling(n):
    falling = {n}
    for k in order:
        if sup[k] and not(sup[k] - falling): falling.add(k)
    return len(falling) - 1

print(sum(count_falling(n) for n in required))
