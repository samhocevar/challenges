#!/usr/bin/env python

def score(c):
    return (ord(c) - 38) % 58 # -38 = 27-'A'   58 = 'a'-'A'+26

s1, s2 = 0, 0

with open('input.txt') as f:
    it = map(str.strip, f) # Remove newlines
    for tu in zip(it, it, it): # Read in chunks of 3 lines
        for l in tu:
            s1 += score((set(l[:len(l)//2]) & set(l[len(l)//2:])).pop())
        s2 += score((set(tu[0]) & set(tu[1]) & set(tu[2])).pop())

print(s1)
print(s2)
