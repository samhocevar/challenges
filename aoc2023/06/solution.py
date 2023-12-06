#!/usr/bin/env python

from math import ceil, floor, sqrt, prod

with open('input.txt') as f:
    data = [l.split(':')[1] for l in f]

# By charging for X milliseconds, we acquire speed X, and can then travel a distance
# of dist = X·(time - X) millimeters.
# In order to beat the record, we therefore need to solve: X² - time·X + dist < 0.
# This function solves the quadratic equation for X the usual way: Δ = b²/4 - a·c,
# then the two roots are: x1, x2 = -b/2 ± √Δ.
# The only subtelty is to carefully use ceil() and floor() in the correct direction.
def compute(time, dist):
    t, δ = time / 2, sqrt(time * time / 4 - dist)
    return ceil(t + δ) - floor(t - δ) - 1

# Part 1: call compute on (t1, d1), (t2, d2), (t3, d3)… and multiply all results together
print(prod(compute(t, d) for t, d in zip(*(map(int, l.split()) for l in data))))

# Part 2: call compute once on (t1t2t3…, d1d2d3…)
print(compute(*(int(l.replace(' ', '')) for l in data)))
