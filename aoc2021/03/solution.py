#!/usr/bin/env python

from bisect import bisect_left

data = []
stats = None

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not stats:
            stats = [0] * len(line)
        data.append(int(line, 2))
        for i in range(len(line)):
            if line[i]=='1':
                stats[i]+=1

BITS = len(stats)
VALUES = len(data)

# Compute gamma/epsilon
gamma = 0
for i in range(BITS):
    if stats[i] > VALUES / 2:
        gamma += 2**(BITS - i - 1)
epsilon = 2**len(stats) - 1 - gamma
print(epsilon * gamma)

# Compute O₂/CO₂
data = sorted(data)

def bisect(direction):
    a, b, k = 0, VALUES, 0
    for i in range(BITS):
        n = bisect_left(data, k + 2**(BITS - i - 1), a, b)
        if (n - a > b - n) == (direction > 0):
            b = n
        else:
            a = n
            k += 2**(BITS - i - 1)
    return data[a if direction > 0 else b - 1]

o2 = bisect(1)
co2 = bisect(-1)
print(o2 * co2)
