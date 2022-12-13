#!/usr/bin/env python

from ast import literal_eval
from itertools import permutations

add = lambda n, m: ['[', *n, ',', *m, ']']

def tostr(l):
    return ''.join(str(t) for t in l)

def mag(n):
    match n:
        case int(): return n
        case str(): return mag(literal_eval(n))
    return 3 * mag(n[0]) + 2 * mag(n[1])

def reduce(s):
    while True:
        opened = 0
        lastn = -1
        for i, t in enumerate(s):
            match t:
                case '[': opened += 1
                case ']': opened -= 1
                case int(): lastn = i
            if opened == 5:
                nextn = next((i + 5 + j for j, t2 in enumerate(s[i + 5:]) if isinstance(t2, int)), -1)
                left, right = s[i + 1], s[i + 3]
                if nextn >= 0:
                    s = s[:nextn] + [s[nextn] + right] + s[nextn + 1:]
                s = s[:i] + [0] + s[i + 5:]
                if lastn >= 0:
                    s = s[:lastn] + [s[lastn] + left] + s[lastn + 1:]
                break
        else: # No explode happened, check for splits
            i = next((i for i, t in enumerate(s) if isinstance(t, int) and t >= 10), -1)
            if i == -1:
                return s
            s = [*s[:i], '[', s[i] // 2, ',', s[i] - s[i] // 2, ']', *s[i+1:]]

with open('input.txt') as f:
    # This is really a shitty structure
    nums = [[c if c in '[],' else ord(c) - ord('0') for c in l.strip()] for l in f]

s = nums[0]
for n in nums[1:]:
    s = reduce(add(s, n))

print(mag(tostr(s)))
print(max(mag(tostr(reduce(add(a, b)))) for a, b in permutations(nums, 2) if a != b))
