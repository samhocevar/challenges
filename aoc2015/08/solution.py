#!/usr/bin/env python

from re import findall

with open('input.txt') as f: data = [l.strip() for l in f]

# Part 1: for each string, add 2 for the double quotes, plus the length of anything after \
print(sum(2 + len(''.join(findall(r'\\("|\\|x[a-f0-9][a-f0-9])', l))) for l in data))

# Part 2: for each string, add 2 for the double quotes, plus anything that needs escaping
print(sum(2 + len(findall(r'["\\]', l)) for l in data))
