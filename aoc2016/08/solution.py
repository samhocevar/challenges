#!/usr/bin/env python

from re import findall
import numpy as np

# Read data and immediately split the normal parts and the parts inside [] into separate strings
with open('input.txt') as f: data = [findall(r'(row|col|rect|\d+)', l) for l in f]

screen = np.zeros(6 * 50).reshape(6, 50).astype(int)
for op, a, b in data:
    if op == 'rect': screen[:int(b),:int(a)] = 1
    if op == 'row': screen[int(a)] = np.roll(screen[int(a)], int(b))
    if op == 'col': screen[:,int(a)] = np.roll(screen[:,int(a)], int(b))

print(np.count_nonzero(screen))
print(*(''.join(' #'[c] for c in l) for l in screen), sep='\n')
