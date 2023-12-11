#!/usr/bin/env python

with open('input.txt') as f: data = list(sorted(map(int, f.readlines())))[::-1]

# Enumerate all the combinations that add up to 150 litres
def combine(total, l, count=0):
    for n, size in enumerate(l):
        if size == total:
            yield count
        elif size < total:
            yield from combine(total - size, l[n + 1:], count + 1)
solutions = sorted(combine(150, data))

# Part 1: print the number of solutions
print(len(solutions))

# Part 2: print how many solutions use the lowest number of containers
print(solutions.count(solutions[0]))
