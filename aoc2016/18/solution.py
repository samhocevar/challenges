#!/usr/bin/env python

with open('input.txt') as f: data = tuple('.^'.find(c) for c in f.read().strip())

def safe(s, n, total=0):
    for _ in range(n):
        total += len(s) - sum(s)
        s = (s[1], *(a ^ b for a, b in zip(s, s[2:])), s[-2])
    return total

print(safe(data, 40))
print(safe(data, 400000))
