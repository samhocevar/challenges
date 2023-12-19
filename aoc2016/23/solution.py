#!/usr/bin/env python

with open('input.txt') as f: data = f.readlines()

lut = {'jnz': 'cpy', 'cpy': 'jnz', 'inc': 'dec', 'dec': 'inc', 'tgl': 'inc'}

def run(reg, pc=0):
    get = lambda x: reg[x] if x in reg else int(x)
    code = [l.strip().split() for l in data]
    while pc < len(code):
        match code[pc]:
            case 'cpy', x, y:
                if y in 'abcd': reg[y] = get(x)
                pc += 1
            case 'jnz', x, y: pc += get(y) if get(x) else 1
            case 'inc', x: reg[x] += 1; pc += 1
            case 'dec', x: reg[x] -= 1; pc += 1
            case 'tgl', x:
                if (n := pc + get(x)) in range(len(code)): code[n][0] = lut[code[n][0]]
                pc += 1
    return reg['a']

print(run({'a': 7, 'b': 0, 'c': 0, 'd': 0}))

# TODO: this is crazy bruteforce but it completes in human-bearable time,
# so I didn’t bother, but it’s a bit shameful… try to improve this one day.
print(run({'a': 12, 'b': 0, 'c': 0, 'd': 0}))
