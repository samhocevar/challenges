#!/usr/bin/env python

from math import prod
from operator import add, mul

# [0]: items, [1]: op, [2]: test, [3]: true, [4]: false
monkeys = []

with open('input.txt') as f:
    for l in f:
        match l.split():
            case ['Starting', *args]: monkeys.append([[int(x.strip(',')) for x in args[1:]]])
            case ['Operation:', _, _, *op]: monkeys[-1].append(op)
            case ['Test:', _, _, test]: monkeys[-1].append(int(test))
            case ['If', 'true:', _, _, _, t]: monkeys[-1].append(int(t))
            case ['If', 'false:', _, _, _, t]: monkeys[-1].append(int(t))

modulus = prod([m[2] for m in monkeys])

def compute(steps, simple):
    state = [m[0].copy() for m in monkeys]
    activity = [0] * len(monkeys)

    for _ in range(steps):
        for i, m in enumerate(monkeys):
            state[i], items = [], state[i]
            activity[i] += len(items)
            for old in items:
                lut = {'+': add, '*': mul, 'old': old}
                op = list(map(lambda x: lut[x] if x in lut else int(x), m[1]))
                new = op[1](op[0], op[2])
                if simple: new //= 3
                else: new %= modulus
                state[m[4 if new % m[2] else 3]].append(new)

    return prod(sorted(activity)[-2:])

print(compute(20, True))
print(compute(10000, False))
