#!/usr/bin/env python

from math import prod

with open('input.txt', 'r') as f:
    print(prod(map(int, f)))
