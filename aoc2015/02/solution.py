#!/usr/bin/env python

with open('input.txt') as f: data = [tuple(int(n) for n in l.split('x')) for l in f]

print(sum(2 * (a * b + b * c + c * a) + a * b * c // max(a, b, c) for a, b, c in data))
print(sum(2 * (a + b + c - max(a, b, c)) + a * b * c for a, b, c in data))
