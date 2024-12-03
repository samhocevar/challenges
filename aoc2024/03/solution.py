#!/usr/bin/env python

from re import findall, sub

with open('input.txt') as f:
    data = f.read().replace('\n', '')

# Part 1: find all valid mul() statements, multiply pairwise, sum
print(sum(int(a) * int(b) for a, b in findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)))

# Part 2: do the same but first disable the don't() sections
print(sum(int(a) * int(b) for a, b in findall(r'mul\((\d{1,3}),(\d{1,3})\)', sub("don't\(\).*?(do\(\)|$)", "", data))))
