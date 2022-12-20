#!/usr/bin/env python

with open('input.txt') as f:
    data = [(l[0], int(l[1:])) for l in map(str.strip, f)]

def apply(s, mode):
    for c, n in data:
        match c:
            case 'N': s[2 * mode + 1] += n
            case 'S': s[2 * mode + 1] -= n
            case 'E': s[2 * mode] += n
            case 'W': s[2 * mode] -= n
            case 'L': s[3], s[2] = [s[2], -s[3], -s[2], s[3]][n // 90 - 1:][:2]
            case 'R': s[2], s[3] = [s[3], -s[2], -s[3], s[2]][n // 90 - 1:][:2]
            case 'F': s[0] += n * s[2]; s[1] += n * s[3]
    return abs(s[0]) + abs(s[1])

print(apply([0, 0, 1, 0], 0))
print(apply([0, 0, 10, 1], 1))
