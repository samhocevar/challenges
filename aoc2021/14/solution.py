#!/usr/bin/env python

rules = {}

with open('input.txt') as f:
    chain = next(f).strip()
    letters = {*chain}
    next(f)
    for a, _, b in [l.strip().split(' ') for l in f]:
        rules[a] = [a[0] + b, b + a[1]]
        letters.add(b)

# Initialize stats with chain
stats = { k: 0 for k in rules }
for x, y in zip(chain, chain[1:]):
    stats[x + y] += 1

# Apply rules to the stats instead of the actual chain
def step():
    todo = { k: 0 for k in rules }
    for k, v in rules.items():
        todo[k] -= stats[k]
        todo[v[0]] += stats[k]
        todo[v[1]] += stats[k]
    for k, v in todo.items():
        stats[k] += v

# Don’t forget to count the last character of the chain! It’s not in the stats
def count(l):
    return sum(v for k, v in stats.items() if k[0] == l) + (chain[-1] == l)

for x in range(40):
    step()
    if x + 1 in [10, 40]:
        counts = list(map(count, letters))
        print(max(counts) - min(counts))

