#!/usr/bin/env python

import sys

s = [0] * 9

with open('input.txt') as f:
    for x in f.readline().strip().split(','):
        s[int(x)] += 1

for n in range(257):
    if n == 80 or n == 256:
        print(sum(s))
    s = s[1:] + s[:1]
    s[6] += s[8]
