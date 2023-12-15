#!/usr/bin/env python

print(sum(range(1, 101)) ** 2 - sum(n ** 2 for n in range(1, 101)))
