#!/usr/bin/env python

from math import lcm, prod
from operator import add, mul

monkeys = []
with open('input.txt') as f:
    for l in f:
        match l.split():
            case 'Monkey', _: monkeys.append(lambda: None)
            case 'Starting', *args:   monkeys[-1].items = [int(x.strip(',')) for x in args[1:]]
            case 'Operation:', *args: monkeys[-1].op = args[2:]
            case 'Test:', *args:      monkeys[-1].test = int(args[2])
            case _, 'true:', *args:   monkeys[-1].true = int(args[3])
            case _, 'false:', *args:  monkeys[-1].false = int(args[3])
modulus = lcm(*(m.test for m in monkeys))

def compute(steps, simple):
    state = [m.items.copy() for m in monkeys]
    activity = [0] * len(monkeys)

    for _ in range(steps):
        for i, m in enumerate(monkeys):
            items, state[i] = state[i], []
            activity[i] += len(items)
            for old in items:
                lut = {'+': add, '*': mul, 'old': old}
                op = list(map(lambda x: lut[x] if x in lut else int(x), m.op))
                new = op[1](op[0], op[2])
                if simple: new //= 3
                else: new %= modulus
                state[m.false if new % m.test else m.true].append(new)

    return prod(sorted(activity)[-2:])

print(compute(20, True))
print(compute(10000, False))
