#!/usr/bin/env python

from itertools import accumulate

# Simple lookup table containing strings "1", "2", …, "9"
lut = [str(n) for n in range(1, 10)]

# If the string ends with a number, return its integer value, otherwise None
find_number = lambda s: next((n % 9 + 1 for n, k in enumerate(lut) if s.endswith(k)), None)

with open('input.txt') as f:
    lines = f.readlines()

# Part 1: find all digits and convert them to integers
print(sum(10 * d[0] + d[-1] for d in (list(filter(None, map(find_number, accumulate(s)))) for s in lines)))

# Part 2: also search for full words by extending the lookup table
lut.extend(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
print(sum(10 * d[0] + d[-1] for d in (list(filter(None, map(find_number, accumulate(s)))) for s in lines)))
