#!/usr/bin/env python

from re import search

with open('input.txt') as f: data = [l.strip() for l in f]

print(sum(1 for s in data if search('[aeiou].*' * 3, s) and search(r'(.)\1', s) and not search('ab|cd|pq|xy', s)))
print(sum(1 for s in data if search(r'(..).*\1', s) and search(r'(.).\1', s)))
