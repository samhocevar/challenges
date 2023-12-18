#!/usr/bin/env python

from math import prod

with open('input.txt') as f: data = [(int(l[3]), int(l[11][:-1])) for l in map(str.split, f)]

# If we push at time t:
#  - disk for data[n] is reached at time t+n+1
#  - it is at position (data[n][0]+t+n+1)%data[n][1]
# We therefore have the following equations:
#  t = -data[n][0]-n-1 (mod data[n][1])
# This is trivially solved using the Chinese remainder theorem and
# the modular inverse.
def solve(data):
    p = prod(l[0] for l in data)
    return sum(-(l[1] + n + 1) * p // l[0] * pow(p // l[0], -1, l[0]) for n, l in enumerate(data)) % p

print(solve(data))
print(solve(data + [(11, 0)]))
