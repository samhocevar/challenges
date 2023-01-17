#!/usr/bin/env python

milk, cereal = [0] * 5, 0

with open('input.txt', 'r') as f:
    next(f)
    for l in map(lambda s: s.split(','), f):
        # Buy cereal
        cereal += int(l[2])
        # Use the freshest milk if there is some
        if cereal:
            for n, m in enumerate(milk):
                if m:
                    cereal -= 100
                    milk[n] -= 100
                    break
        # Throw milk away and buy some
        milk = milk[1:] + [int(l[1])]

print(sum(milk) + cereal)
