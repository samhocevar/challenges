#!/usr/bin/env python

from operator import add, mul, sub, floordiv

OPS = {'+': add, '-': sub, '*': mul, '/': floordiv}
INVOPS = {'+': sub, '-': add, '*': floordiv, '/': mul}

data = {}
with open('input.txt') as f:
    for l in map(str.strip, f):
        match l.split():
            case v, n:  data[v[:4]] = int(n)
            case v, *l: data[v[:4]] = tuple(l)

def simplify(rules):
    rules = rules.copy()
    while True:
        changed = False
        for k, v in rules.items():
            if isinstance(v, int):
                continue
            match rules.get(v[0]):
                case int(n): rules[k] = (n, *v[1:]); changed = True
            match rules.get(v[2]):
                case int(n): rules[k] = (*v[:-1], n); changed = True
            match v:
                case int(a), op, int(b): rules[k] = OPS[op](a, b); changed = True
        if not changed:
            return rules

def solve(rules, unknown, expr, n):
    if expr == unknown: return n
    x, op, y = expr
    if isinstance(x, str): x = rules[x]
    if isinstance(y, str): y = rules[y]
    match x, op:
        case int(), '-' | '/': return solve(rules, unknown, y, OPS[op](x, n))
        case int(), _:         return solve(rules, unknown, y, INVOPS[op](n, x))
        case _, _:             return solve(rules, unknown, x, INVOPS[op](n, y))

# Part 1: simplify the whole tree, get root
print(simplify(data)['root'])

# Part 2: simplify without 'humn', then solve for 'humn'
x, _, y = data['root']
data['humn'] = 'humn'
print(solve(simplify(data), 'humn', (x, '-', y), 0))
