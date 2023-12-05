#!/usr/bin/env python

with open('input.txt') as f:
    seeds = list(map(int, next(f)[7:].split()))
    rules = list(map(str.strip, f))

# Apply rules to an iterable of ranges and return the smallest resulting element
def lowest_location(todo, done=set()):
    for r in rules:
        if 'map:' in r:
            todo, done = done.union(todo), set()
        elif r:
            dst, s1, l1 = map(int, r.split())
            for s2, l2 in [(s2, l2) for s2, l2 in todo if s2 + l2 > s1 and s2 < s1 + l1]:
                todo.remove((s2, l2))
                # Split range in case of a partial match and put non-matching parts back in the todo set
                if s2 < s1: todo.add((s2, s1 - s2))
                if s2 + l2 > s1 + l1: todo.add((s1 + l1, s2 + l2 - s1 - l1))
                # Offset the matching range and put it in the done set
                done.add((dst + max(s2 - s1, 0), min(s2 + l2, s1 + l1) - max(s1, s2)))
    return min(todo | done)[0]

# Part 1: arg is (seed1, 1), (seed2, 1), (seed3, 1), …
print(lowest_location(zip(seeds, [1 for _ in seeds])))

# Part 2: arg is (seed1, len1), (seed2, len2), …
print(lowest_location(zip(seeds[::2], seeds[1::2])))
