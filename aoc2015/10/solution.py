#!/usr/bin/env python

from re import findall

with open('input.txt') as f:
    data = next(f).strip()

def change(s, n):
    return change(''.join(f'{len(x[0])}{x[0][0]}' for x in findall(r'((.)\2*)', s)), n - 1) if n else s

print(len(change(data, 40)))
print(len(change(data, 50)))
