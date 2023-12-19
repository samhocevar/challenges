#!/usr/bin/env python

with open('input.txt') as f: data = [l.strip() for l in f]

# Swap positions a and b
def swap(s, a, b): a, b = min(a, b), max(a, b); return s[:a] + s[b] + s[a + 1:b] + s[a] + s[b + 1:]

# Move position a to b
def move(s, a, b): s, c = s[:a] + s[a + 1:], s[a]; return s[:b] + c + s[b:]

# Rotate left (right if n < 0)
def rot(s, n): return s[n % len(s):] + s[:n % len(s)]

# Lookup table for the 'rotate based on' step
lut = [None, [-1, -2, -3, -4, 2, 1, 0, -1], [1, 1, -2, 2, -1, 3, 0, 4]]

def shuffle(s, d):
    for l in data[::d]:
        match l.split():
            case 'move',             _, a, _, _, b: s = move(s, int(a), int(b)) if d > 0 else move(s, int(b), int(a))
            case 'swap', 'position',    a, _, _, b: s = swap(s, int(a), int(b))
            case 'swap', 'letter',      a, _, _, b: s = swap(s, s.find(a), s.find(b))
            case 'reverse',             _, a, _, b: s = s[:int(a)] + s[int(a):int(b) + 1][::-1] + s[int(b) + 1:]
            case 'rotate', 'based',  _, _, _, _, a: s = rot(s, lut[d][s.find(a)])
            case 'rotate', 'left',   n, _: s = rot(s, int(n) * d)
            case 'rotate', 'right',  n, _: s = rot(s, int(n) * -d)
    return s

print(shuffle('abcdefgh', 1))
print(shuffle('fbgdceah', -1))
