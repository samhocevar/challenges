#!/usr/bin/env python

with open('input.txt') as f:
    data = list(map(int, f))

rate = max(data) + 3
data = sorted([0, rate] + data)
steps = list(j - i for i, j in zip(data, data[1:]))

print(sum(1 for i in steps if i == 1) * sum(1 for i in steps if i == 3))

def get(n, cache={k: 1 if k == rate else 0 for k in data}):
    if cache[n] > 0:
        return cache[n]
    ret = sum(get(d, cache) for d in (n + 1, n + 2, n + 3) if d in cache)
    cache[n] = ret
    return ret

print(get(0))
