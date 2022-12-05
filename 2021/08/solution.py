#!/usr/bin/env python

from functools import reduce

known = {2: 1, 3: 7, 4: 4, 7: 8}

def tobits(s):
    return len(s), sum(1 << (ord(c) - ord('a')) for c in s)

s0, s1 = 0, 0

with open('input.txt') as f:
    for l in f:
        digits, m5, m6 = [0] * 10, [], []
        v = l.strip().split(' ')
        for l, b in map(tobits, v[:10]):
            if l == 5:
                m5.append(b)
            elif l == 6:
                m6.append(b)
            else:
                digits[known[l]] = b
        # 6 is the only 6-segment digit that gives 8 when ORed with 1
        digits[6] = next(x for x in m6 if x | digits[1] == digits[8])
        # 5 is the only 5-segment contained in 6
        digits[5] = next(x for x in m5 if x & digits[6] == x)
        # 9 is 5 merged with 1
        digits[9] = digits[5] | digits[1]
        # 3 contains 1
        digits[3] = next(x for x in m5 if x & digits[1] == digits[1])
        # The rest can be deduced
        digits[2] = digits[3] ^ digits[5] ^ m5[0] ^ m5[1] ^ m5[2]
        digits[0] = digits[6] ^ digits[9] ^ m6[0] ^ m6[1] ^ m6[2]

        s0 += sum(1 for s in v[11:] if len(s) in known)
        s1 += int(''.join(str(digits.index(b)) for _, b in map(tobits, v[11:])))

print(s0)
print(s1)

