#!/usr/bin/env python

abc = []
with open('input.txt') as f:
    for n, l in enumerate(f):
        # The program contains 14 chunks of 18 instructions. This is the really important part.
        # Each chunk contains the same code except for these constants. Because of how they are
        # chosen, 7 chunks cause z to increase, and 7 other cause it do decrease (provided the
        # right input is given).
        if n % 18 in [4, 5, 15]:
            abc.append(int(l.split()[2]))

def step(inp, z, A, B, C):
    if inp == z % 26 + B:
        return z // A
    return z // A * 26 + inp + C

def solve(order, l=[], z=0):
    if len(l) == 14 and z == 0:
        return ''.join(map(str, l))
    A, B, C = abc[len(l) * 3:][:3]
    tries = order
    if A == 26:
        w = z % 26 + B
        if w < 1 or w > 9:
            return
        tries = [w] # Only this value can lead to z == 0
    for w in tries:
        if ok := solve(order, l + [w], step(w, z, A, B, C)):
            return ok

print(solve(list(range(9, 0, -1))))
print(solve(list(range(1, 10))))
