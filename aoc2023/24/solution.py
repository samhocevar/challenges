#!/usr/bin/env python

from itertools import product, count
from math import lcm, gcd, prod

with open('input.txt') as f: data = [list(map(int, l.replace('@', ' ').replace(',', ' ').split())) for l in f]

# Simple 2D solver to find the intersection between two rays; this is
# not very readable but a lot faster than numpy…
def solve2d(p, q):
    if not (det := q[3] * p[4] - p[3] * q[4]): return False, 0, 0
    k0 = (q[3] * (q[1] - p[1]) - q[4] * (q[0] - p[0])) / det
    k1 = (p[3] * (q[1] - p[1]) - p[4] * (q[0] - p[0])) / det
    return k0 >= 0 and k1 >= 0, p[0] + k0 * p[3], p[1] + k0 * p[4]

hits = 0
for j in range(len(data)):
    for i in range(j):
        # Solve in 2D for xy
        good, x, y = solve2d(data[i], data[j])
        if good and min(x, y) >= 200000000000000 and max(x, y) <= 400000000000000: hits += 1

# Part 1: print the total number of XY intersections
print(hits)

# Solve x = x1 (mod m1) and x = x2 (mod m2)
def crt(x1, m1, x2, m2):
    g, l = gcd(m1, m2), lcm(m1, m2)
    if not g or not l or (x1 - x2) % g: return 0, 0
    # Compute Bézout coefficients u and v for m1/g, m2/g
    u = pow(m1 // g, -1, m2 // g)
    v = (1 - m1 // g * u) // (m2 // g)
    rem = (x1 * v * m2 + x2 * u * m1) // g
    return rem % l, l

# Chinese remainder theorem solver: find x such that x = xi (mod mi).
# This version tries to find a solution even in the non-strict case, i.e.
# when not all the moduli are coprime.
# The strict version would simply be:
#   p = prod(mn)
#   return sum(x * p // m * pow(p // m, -1, m) for x, m in zip(xn, mn)) % p, p
def full_crt(xn, mn, x=0, m=1):
    for xi, mi in zip(xn, mn):
        if not mi: continue #return 0, 0
        x, m = crt(x, m, xi, mi)
    return x, m

# Part 2: solve x + kᵢ·vx = xᵢ + xᵢ·vᵢ by trying successive values of v
# and finding x using the Chinese Remainder Theorem. Then solve the
# same equation for (y,vy), then for (z,zy). Combining the three gives
# us a solution to the problem.
total = 0
for k in range(3):
    for v in (n * s for n in count(1) for s in (-1, 1)):
        a, b = full_crt([l[k] for l in data], [v - l[k + 3] for l in data])
        if b != 0: total += a; break
print(total)
