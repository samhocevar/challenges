#!/usr/bin/env python

def score(s):
    return sum(ord(c) - (96 if c >= 'a' else 38) for c in s)

s1, s2 = 0, 0

with open('input.txt') as f:
    it = map(str.strip, f) # Remove newlines
    for tu in zip(it, it, it): # Read in chunks of 3 lines
        for l in tu:
            s1 += score(set(l[:len(l)//2]) & set(l[len(l)//2:]))
        s2 += score(set(tu[0]) & set(tu[1]) & set(tu[2]))

print(s1)
print(s2)
