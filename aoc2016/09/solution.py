#!/usr/bin/env python

from re import search

with open('input.txt') as f: data = f.read().strip()

def decomp(s, deep):
    if not (m := search(r'\((\d+)x(\d+)\)', s)):
        return len(s)
    i, j, k, n = *m.span(0), int(m.groups()[0]), int(m.groups()[1])
    return i + n * (decomp(s[j:j + k], deep) if deep else k) + decomp(s[j + k:], deep)

print((decomp(data, deep=False)))
print((decomp(data, deep=True)))
