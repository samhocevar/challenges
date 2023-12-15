#!/usr/bin/env python

with open('input.txt') as f: data = next(f).strip().split(', ')

def travel(part):
    d, p, done = 0, [0, 0], set()
    for s in data:
        d += ' R'.find(s[0])
        for _ in range(int(s[1:])):
            if part == 2:
                if (*p,) in done: break
                done.add((*p,))
            p[d % 2] += (-1, 0, 1)[d & 2]
    return abs(sum(p))

print(travel(part=1))
print(travel(part=2))
