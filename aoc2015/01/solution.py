#!/usr/bin/env python

from itertools import accumulate

with open('input.txt') as f: data = next(f).strip()

# Part 1: simply count opening and closing parentheses
print(data.count('(') - data.count(')'))

# Part 2: accumulate +1s and -1s until floor is -1
print(next(n + 1 for n, f in enumerate(accumulate(' ('.find(c) for c in data)) if f == -1))
