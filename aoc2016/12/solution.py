#!/usr/bin/env python

with open('input.txt') as f: data = [l.strip().split() for l in f]

# This could be made faster by replacing the contents of data with precomputed lambdas.
def run(reg, pc=0):
    while pc < len(data):
        match data[pc]:
            case 'cpy', x, y: reg[y] = reg[x] if x in reg else int(x); pc += 1
            case 'inc', x: reg[x] += 1; pc += 1
            case 'dec', x: reg[x] -= 1; pc += 1
            case 'jnz', x, y: pc += int(y) if (reg[x] if x in reg else int(x)) else 1
    return reg['a']

print(run({'a': 0, 'b': 0, 'c': 0, 'd': 0}))
print(run({'a': 0, 'b': 0, 'c': 1, 'd': 0}))

