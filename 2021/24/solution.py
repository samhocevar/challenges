#!/usr/bin/env python

chunks = []
with open('input.txt') as f:
    for l in f:
        match l.split():
            case 'inp', a:
                chunks.append([('inp', a)])
            case op, a, b:
                chunks[-1].append((op, a, b))

# This is the really important part of the program. Each chunk contains the same code
# except for these constants. Because of how these constants are chosen, 7 chunks cause
# z to increase, and 7 other cause it do decrease (if the right input is given).
abc = [tuple(map(int, (chunk[4][2], chunk[5][2], chunk[15][2]))) for chunk in chunks]

def step(inp, z, A, B, C):
    if inp == z % 26 + B:
        return z // A
    return z // A * 26 + inp + C

def solve(order, l=[], z=0):
    if len(l) == 14 and z == 0:
        return ''.join(map(str, l))
    A, B, C = abc[len(l)]
    tries = order
    if A == 26:
        w = z % 26 + B
        if w < 1 or w > 9:
            return None # No way this can lead to z == 0
        tries = [w]
    for w in tries:
        if ok := solve(order, l + [w], step(w, z, A, B, C)):
            return ok

print(solve(list(range(9, 0, -1))))
print(solve(list(range(1, 10))))
