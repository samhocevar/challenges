#!/usr/bin/env python

with open('input.txt') as f: data = [l.strip().replace(',', '') for l in f]

def run(a):
    pc, reg = 0, {'a': a, 'b': 0}
    while pc < len(data):
        match data[pc].split(' '):
            case 'inc', r: reg[r] += 1; pc += 1
            case 'hlf', r: reg[r] //= 2; pc += 1
            case 'tpl', r: reg[r] *= 3; pc += 1
            case 'jmp', n: pc += int(n)
            case 'jie', r, n: pc += 1 if reg[r] % 2 else int(n)
            case 'jio', r, n: pc += int(n) if reg[r] == 1 else 1
    return reg['b']

print(run(0))
print(run(1))
