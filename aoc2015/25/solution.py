#!/usr/bin/env python

from re import findall

with open('input.txt') as f: j, i = [int(s) for s in findall('[0-9]+', f.read())]

k, a, b = 20151125, 252533, 33554393
n = ((i + j) * (i + j - 1)) // 2 - j
print(k * pow(a, n, b) % b)
