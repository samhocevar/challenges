#!/usr/bin/env python

rules = {}

with open('input.txt') as f:
    chain = next(f).strip()
    letters = set(chain)
    next(f)
    for a, _, b in [l.strip().split(' ') for l in f]:
        rules[a] = [a[0] + b, b + a[1]]
        letters.add(b)

# Initialize state with chain
state = { k: 0 for k in rules }
for x, y in zip(chain, chain[1:]):
    state[x + y] += 1

# Apply rules to the stats instead of the actual chain
def step():
    todo = { k: 0 for k in rules }
    for k, v in rules.items():
        todo[k] -= state[k]
        todo[v[0]] += state[k]
        todo[v[1]] += state[k]
    for k, v in todo.items():
        state[k] += v

def count(l):
    return sum(v for k, v in state.items() if k[0] == l) + (chain[-1] == l)

for x in range(40):
    step()
    if x + 1 in [10, 40]:
        print(max(map(count, letters)) - min(map(count, letters)))

