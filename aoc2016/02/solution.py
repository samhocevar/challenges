#!/usr/bin/env python

from functools import reduce

with open('input.txt') as f: data = [s.strip() for s in f]

def code(s, lut):
    return reduce(lambda c, d: lut['ULRD'.find(d)][int(c, 16) - 1], s, '5')

print(*(code(s, ['123123456', '112445778', '233566899', '456789789']) for s in data), sep='')
print(*(code(s, ['121452349678B', '122355678AABD', '134467899BCCD', '36785ABC9ADCD']) for s in data), sep='')
