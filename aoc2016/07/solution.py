#!/usr/bin/env python

from re import search, split

# Read data and immediately split the normal parts and the parts inside [] into separate strings
with open('input.txt') as f:
    data = [(' '.join(t[::2]), ' '.join(t[1::2])) for t in [split(r'[\[\]]', l.strip()) for l in f]]

# Part 1: string 'a' must contain an ABBA and string 'b' must not contain one
print(sum(1 for a, b in data if search(r'(.)(.)(?<!\1)\2\1', a) and not search(r'(.)(.)(?<!\1)\2\1', b)))

# Part 2: 'a|b' must match ABA.*|.*BAB
print(sum(1 for a, b in data if search(r'(.)(.)(?<!\1)\1.*[|].*\2\1\2', '|'.join((a, b)))))
