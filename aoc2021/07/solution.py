#!/usr/bin/env python

from bisect import bisect_right

with open('input.txt') as f:
    p = sorted(int(x) for x in f.readline().strip().split(','))

# The middle of the array minimises the sum of absolute values
x1 = len(p) // 2
print(sum(p[x1:]) - sum(p[:x1]))

# The mean minimises the sum of squared differences
mean = sum(p) / len(p)
x2 = bisect_right(p, mean)

# Since the two distance functions are convex, the minimum lies between x1 and x2
a = p[x1-1] if x1 < x2 else p[x2-1]
b = p[x1] if x1 > x2 else p[x2]

# Brute force this in our reduced range
print(min(sum(abs(n - x) * (abs(n - x) + 1) for n in p) // 2 for x in range(a, b)))
