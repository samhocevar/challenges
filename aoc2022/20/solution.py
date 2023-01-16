#!/usr/bin/env python

from math import prod

with open('input.txt') as f:
    data = list(map(int, f))

def move(data, i, j):
    data, n = data[:i] + data[i+1:], data[i]
    return [*data[:j], n, *data[j:]]

def mix(data, rounds):
    m = len(data)
    dual = list(range(m))
    for _ in range(rounds):
        for n in range(m):
            i = dual.index(n)
            j = (i + data[i] + (m - 1)) % (m - 1)
            dual = move(dual, i, j)
            data = move(data, i, j)
    k = data.index(0)
    return sum(data[(k + n) % m] for n in (1000, 2000, 3000))

print(mix(data, 1))
print(mix([x * 811589153 for x in data], 10))
