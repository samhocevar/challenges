#!/usr/bin/env python

from re import findall

msg = { 'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1 }

with open('input.txt') as f:
    data = [{k: int(v) for k, v in findall('([a-z]+): ([0-9]+)', l)} for l in f]

# Return the first matching aunt (it’s supposed to be the only one)
def aunt(fn):
    return next(n for n, d in enumerate(data, 1) if all(fn(k, v) for k, v in d.items()))

# Part 1: find the aunt that matches exactly the requirements
print(aunt(lambda k, v: v == msg[k]))

# Part 2: use a more complex checking function
def check(k, v):
    if k in ('cats', 'trees'): return v > msg[k]
    if k in ('pomeranians', 'goldfish'): return v < msg[k]
    return v == msg[k]
print(aunt(check))
