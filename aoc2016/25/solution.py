#!/usr/bin/env python

from itertools import count

with open('input.txt') as f: data = [l.strip().split() for l in f]

lut = {'jnz': 'cpy', 'cpy': 'jnz', 'inc': 'dec', 'dec': 'inc', 'tgl': 'inc'}

def run(reg, pc=0):
    get = lambda x: reg[x] if x in reg else int(x)
    code = [l.copy() for l in data]
    while pc < len(code):
        match code[pc]:
            case 'cpy', x, y:
                if y in 'abcd': reg[y] = get(x)
                pc += 1
            case 'jnz', x, y: pc += get(y) if get(x) else 1
            case 'inc', x: reg[x] += 1; pc += 1
            case 'dec', x: reg[x] -= 1; pc += 1
            case 'out', x: yield get(x); pc += 1

for a in count():
    for n, out in enumerate(run({'a': a, 'b': 0, 'c': 0, 'd': 0})):
        if n > 10000 or n & 1 != out: break
    if n > 10000: print(a); break
