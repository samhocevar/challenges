#!/usr/bin/env python

with open('input.txt') as f: data = [[int(s) for s in l.split()] for l in f]

# Part 1: straightforward triangle inequality
print(sum(1 for t in data if sum(t) > 2 * max(*t)))

# Part 2: flatten all columns (zip) and read them 3 items at a time (zip again)
data = sum(list(zip(*data)), ())
print(sum(1 for t in zip(*[iter(data)] * 3) if sum(t) > 2 * max(t)))
